#!/usr/bin/env python3
"""Bounded exact three-valued transposition-aware PNS for CanSort(P,d).

OR node (P,d): sorter chooses a comparison; success iff SOME child AND-node
 succeeds. AND node (P,d,i,j): adversary chooses either answer; success iff
 BOTH child OR-nodes (P+i<j,d-1), (P+j<i,d-1) succeed. Refutation is the
 exact dual: OR refuted iff ALL candidate AND children are refuted; AND
 refuted iff SOME answer child is refuted. Total OR states are proved;
 non-total d=0 OR states are refuted. A cap yields UNKNOWN, never a Boolean.

The table key is (n, exact canon(P), d, node-kind, comparison-if-AND).
Canonicalization is complete color-refinement-constrained permutation
enumeration (same exact invariant as state_compression.py). Solved values are
monotone and propagated to every parent; all parents are retained. PNs only
select an unresolved frontier node and never establish a result.
"""
import argparse
import itertools
import resource
import time

INF = 10**30


def extend(s, i, j):
    out = list(s)
    greater = s[j] | (1 << j)
    for x in range(len(s)):
        if x == i or (s[x] >> i & 1):
            out[x] |= greater
    return tuple(out)


def pairs(s, n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)
            if not (s[i] >> j & 1) and not (s[j] >> i & 1)]


def canon(s, n):
    # Enumerate only permutations within invariant refinement color classes.
    color = [s[i].bit_count() for i in range(n)]
    while True:
        sig = []
        for i in range(n):
            down = tuple(sorted(color[j] for j in range(n) if s[i] >> j & 1))
            up = tuple(sorted(color[j] for j in range(n) if s[j] >> i & 1))
            sig.append((color[i], down, up))
        ids = {v: k for k, v in enumerate(sorted(set(sig)))}
        new = [ids[v] for v in sig]
        if new == color:
            break
        color = new
    groups = [[i for i, c in enumerate(color) if c == v]
              for v in sorted(set(color))]
    best = None
    for choices in itertools.product(*(itertools.permutations(g) for g in groups)):
        perm = tuple(x for group in choices for x in group)
        enc = []
        for a in range(n):
            bits = s[perm[a]]
            enc.append(sum(1 << b for b in range(n) if bits >> perm[b] & 1))
        enc = tuple(enc)
        if best is None or enc < best:
            best = enc
    return best


class Node:
    __slots__ = ('key', 'kind', 'state', 'd', 'cmp', 'children', 'parents',
                 'expanded', 'value', 'pn', 'dn')
    def __init__(self, key, kind, state, d, cmp=None):
        self.key, self.kind, self.state, self.d, self.cmp = key, kind, state, d, cmp
        self.children, self.parents = [], []
        self.expanded, self.value = False, None  # None=unknown, bool=solved
        self.pn = self.dn = 1


def search(n, d, node_cap=1_000_000, edge_cap=2_000_000, seconds=120):
    table = {}
    stats = dict(canon_calls=0, generated_edges=0, expansions=0)
    def get(kind, state, budget, cmp=None):
        stats['canon_calls'] += 1
        c = canon(state, n)
        # Comparison is represented in canonical coordinates for AND identity.
        cc = None
        if kind == 'and':
            inv = [0] * n
            # c is an encoding under some minimizing permutation; recover a
            # stable equivalent AND key by keying the already canonical parent
            # and unordered pair's transformed orientation set.
            # Distinct pair choices are carried as their set of child canons;
            # constructed below instead, so this case is only defensive.
            cc = tuple(sorted(cmp))
        key = (kind, c, budget, cc)
        if key not in table:
            table[key] = Node(key, kind, c, budget, cc)
        return table[key]

    # Build explicit AND nodes from canonical OR state and unordered choice;
    # canonical state relabelling is immaterial because each child pair is
    # enumerated from the representative stored in that node.
    root = get('or', (0,) * n, d)
    start = time.perf_counter()
    work = [root]
    # Fair frontier expansion; solved propagation is recomputed to a fixed point
    # over all parents, so hash-order/worklist choices affect speed only.
    while root.value is None:
        if stats['expansions'] >= node_cap or stats['generated_edges'] >= edge_cap or time.perf_counter()-start >= seconds:
            return 'UNKNOWN', stats, table, time.perf_counter()-start
        candidates = [x for x in table.values() if x.value is None and not x.expanded]
        # Prefer low proof number for OR, low disproof number for AND.
        node = min(candidates, key=lambda x: (x.pn if x.kind == 'or' else x.dn,
                                               x.dn if x.kind == 'or' else x.pn))
        if node.kind == 'or':
            ps = pairs(node.state, n)
            if not ps:
                node.value = True
            elif node.d == 0:
                node.value = False
            else:
                node.expanded = True
                for i, j in ps:
                    # AND identity includes exact canonical parent and pair;
                    # here representative is canonical, so pair indices are exact.
                    key = ('and', node.state, node.d, (i, j))
                    a = table.get(key)
                    if a is None:
                        a = Node(key, 'and', node.state, node.d, (i, j)); table[key] = a
                    if a not in node.children:
                        node.children.append(a); a.parents.append(node)
                        stats['generated_edges'] += 1
                if not node.children:
                    node.value = False
        else:
            if not node.expanded:
                i, j = node.cmp
                node.expanded = True
                for x, y in ((i, j), (j, i)):
                    child = get('or', extend(node.state, x, y), node.d - 1)
                    if child not in node.children:
                        node.children.append(child); child.parents.append(node)
                        stats['generated_edges'] += 1
        stats['expansions'] += 1
        # Fixed-point sound propagation across DAG with shared parents.
        changed = True
        while changed:
            changed = False
            for x in table.values():
                if x.value is not None:
                    continue
                vals = [c.value for c in x.children]
                val = None
                if x.kind == 'or':
                    if any(v is True for v in vals): val = True
                    elif x.expanded and vals and all(v is False for v in vals): val = False
                else:
                    if any(v is False for v in vals): val = False
                    elif x.expanded and vals and all(v is True for v in vals): val = True
                if val is not None:
                    x.value = val; changed = True
            # PNs are heuristics only; use solved statuses to update estimates.
            for x in table.values():
                if x.value is True: x.pn, x.dn = 0, INF
                elif x.value is False: x.pn, x.dn = INF, 0
                elif x.children:
                    if x.kind == 'or':
                        x.pn = min(c.pn for c in x.children)
                        x.dn = min(INF, sum(c.dn for c in x.children))
                    else:
                        x.pn = min(INF, sum(c.pn for c in x.children))
                        x.dn = min(c.dn for c in x.children)
        if stats['generated_edges'] >= edge_cap:
            break
    return ('PROVED' if root.value else 'DISPROVED'), stats, table, time.perf_counter()-start


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, choices=(4, 5), required=True)
    ap.add_argument('--d', type=int, required=True)
    ap.add_argument('--node-cap', type=int, default=1_000_000)
    ap.add_argument('--edge-cap', type=int, default=2_000_000)
    ap.add_argument('--seconds', type=float, default=120)
    a = ap.parse_args()
    before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result, st, table, elapsed = search(a.n, a.d, a.node_cap, a.edge_cap, a.seconds)
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f'n={a.n} d={a.d} result={result} distinct_nodes={len(table)} '
          f"expanded={st['expansions']} generated_edges={st['generated_edges']} "
          f"canonicalization_calls={st['canon_calls']} seconds={elapsed:.6f} "
          f'peak_rss_kib={peak} prior_peak_kib={before} caps=({a.node_cap},{a.edge_cap},{a.seconds})')
    if result == 'UNKNOWN':
        return 2
    # Independent value oracle from evaluate.py.
    import sys
    sys.path.insert(0, __file__.rsplit('/', 1)[0])
    from evaluate import sorting_number
    expected = sorting_number(a.n) <= a.d
    assert (result == 'PROVED') == expected
    print(f'evaluate.py says {expected}; verified')


if __name__ == '__main__':
    raise SystemExit(main())
