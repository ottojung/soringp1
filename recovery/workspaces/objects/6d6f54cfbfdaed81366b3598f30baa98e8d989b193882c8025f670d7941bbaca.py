#!/usr/bin/env python3
"""Check a finite comparison strategy DAG with permutation frames.

All nodes are numbered topologically, root=0. The verifier propagates
the guaranteed strict partial order at each node, intersecting incoming
branches. An edge permutation maps old slot indices to new slot indices.
This is polynomial in n and the explicit graph size; for SORT-BOUND-U
the number n is already supplied in unary. Polynomial-size completeness
for *optimal* sorting strategies is not asserted.
"""
import argparse
import json
from pathlib import Path


class InvalidCertificate(ValueError):
    pass


def _closure(rows, n):
    rows = list(rows)
    for mid in range(n):
        bit = 1 << mid
        for i in range(n):
            if rows[i] & bit:
                rows[i] |= rows[mid]
    if any(rows[i] & (1 << i) for i in range(n)):
        raise InvalidCertificate("cyclic guaranteed order")
    return rows


def _rename(rows, perm, n):
    renamed = [0] * n
    for i in range(n):
        rem = rows[i]
        while rem:
            bit = rem & -rem
            j = bit.bit_length() - 1
            renamed[perm[i]] |= 1 << perm[j]
            rem -= bit
    return renamed


def check_certificate(cert):
    """Return longest reachable path, or raise InvalidCertificate.

    Format: {"n":n,"budget":k,"nodes":[
      {"compare":[a,b],"lt":{"next":v,"perm":[...]},
                         "gt":{"next":v,"perm":[...]}}, ..., {"leaf":true}
    ]}
    'lt' records a<b; 'gt' records b<a before relabelling.
    Both outgoing edges are specified even when an outcome is impossible.
    """
    if not isinstance(cert, dict):
        raise InvalidCertificate("expected JSON object")
    n, budget, nodes = cert.get("n"), cert.get("budget"), cert.get("nodes")
    if type(n) is not int or n < 0:
        raise InvalidCertificate("n must be nonnegative integer")
    if type(budget) is not int or budget < 0:
        raise InvalidCertificate("budget must be nonnegative integer")
    if not isinstance(nodes, list) or not nodes:
        raise InvalidCertificate("missing nodes")
    relations = [None] * len(nodes)
    depths = [None] * len(nodes)
    relations[0], depths[0] = [0] * n, 0
    for v, node in enumerate(nodes):
        if not isinstance(node, dict):
            raise InvalidCertificate(f"node {v} is not an object")
        if node.get("leaf") is True:
            if any(key in node for key in ("compare", "lt", "gt")):
                raise InvalidCertificate(f"leaf {v} has outgoing query")
            if relations[v] is not None:
                rows = relations[v]
                for i in range(n):
                    for j in range(i + 1, n):
                        if not (rows[i] & (1 << j) or rows[j] & (1 << i)):
                            raise InvalidCertificate(f"leaf {v} does not sort {i},{j}")
            continue
        pair = node.get("compare")
        if (not isinstance(pair, list) or len(pair) != 2 or
                any(type(i) is not int or not 0 <= i < n for i in pair) or
                pair[0] == pair[1]):
            raise InvalidCertificate(f"invalid query in node {v}")
        a, b = pair
        for outcome in ("lt", "gt"):
            edge = node.get(outcome)
            if not isinstance(edge, dict):
                raise InvalidCertificate(f"missing {outcome} edge at {v}")
            child, perm = edge.get("next"), edge.get("perm")
            if type(child) is not int or not v < child < len(nodes):
                raise InvalidCertificate(f"nonforward edge from {v}")
            if (not isinstance(perm, list) or len(perm) != n or
                    any(type(x) is not int for x in perm) or
                    set(perm) != set(range(n))):
                raise InvalidCertificate(f"invalid frame at {v}")
            if relations[v] is None:
                continue
            smaller, larger = (a, b) if outcome == "lt" else (b, a)
            if relations[v][larger] & (1 << smaller):
                continue  # logically impossible branch
            rows = list(relations[v])
            rows[smaller] |= 1 << larger
            rows = _rename(_closure(rows, n), perm, n)
            if relations[child] is None:
                relations[child] = rows
            else:
                relations[child] = [x & y for x, y in zip(relations[child], rows)]
            depths[child] = max(depths[child] or 0, depths[v] + 1)
    if any(d is not None and d > budget for d in depths):
        raise InvalidCertificate("depth exceeds budget")
    return max(d for d in depths if d is not None)


def triangular_bubble_certificate(n):
    """Length n(n-1)/2 path with branch frames representing compare-exchange."""
    if type(n) is not int or n < 0:
        raise ValueError("n must be nonnegative")
    nodes, identity = [], list(range(n))
    for p in range(n - 1):
        for i in range(n - 1 - p):
            swap = identity.copy()
            swap[i], swap[i + 1] = swap[i + 1], swap[i]
            nxt = len(nodes) + 1
            nodes.append({"compare": [i, i + 1],
                          "lt": {"next": nxt, "perm": identity.copy()},
                          "gt": {"next": nxt, "perm": swap}})
    nodes.append({"leaf": True})
    return {"n": n, "budget": n * (n - 1) // 2, "nodes": nodes}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", type=Path)
    parser.add_argument("--bubble", type=int, help="generate and verify bubble witness")
    args = parser.parse_args()
    if (args.file is None) == (args.bubble is None):
        parser.error("specify exactly one of FILE and --bubble N")
    cert = (json.loads(args.file.read_text()) if args.file is not None
            else triangular_bubble_certificate(args.bubble))
    try:
        depth = check_certificate(cert)
    except InvalidCertificate as exc:
        parser.exit(1, f"REJECT: {exc}\n")
    print(f"ACCEPT: n={cert['n']}, depth={depth}, nodes={len(cert['nodes'])}")


if __name__ == "__main__":
    main()
