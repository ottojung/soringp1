#!/usr/bin/env python3
"""Search/check small exact-entropy refutations for X_12 and Y_12.

This is a scratch research probe, not a production verifier or a claim that a
compact proof exists.  The search uses exact linear-extension counts computed
from a supplied bounded chain partition.  The checker below is independent of
the move-ordering/search decisions: it verifies only the E/SPLIT/SERIES rules.

Run on Billy, for example:
    python3 scripts/xy_refutation_probe.py --target X --node-limit 200000
    python3 scripts/xy_refutation_probe.py --target Y --node-limit 200000
"""

from __future__ import annotations

import argparse
import itertools
import json
import time
from dataclasses import dataclass
from functools import lru_cache
from typing import Any


State = tuple[int, ...]  # succ[i] bitmask of elements known greater than i
Proof = dict[str, Any]


def add_relation(s: State, i: int, j: int) -> State:
    """Transitive closure after adjoining i<j to a closed poset."""
    out = list(s)
    new_succ = s[j] | (1 << j)
    for x in range(len(s)):
        if x == i or ((s[x] >> i) & 1):
            out[x] |= new_succ
    return tuple(out)


def legal_pairs(s: State) -> list[tuple[int, int]]:
    n = len(s)
    return [(i, j) for i in range(n) for j in range(i + 1, n)
            if not ((s[i] >> j) & 1) and not ((s[j] >> i) & 1)]


def is_poset(s: State) -> bool:
    n = len(s)
    if len(s) != n or any((s[i] >> i) & 1 for i in range(n)):
        return False
    for i in range(n):
        for j in range(n):
            if (s[i] >> j) & 1:
                if (s[j] >> i) & 1 or (s[j] & ~s[i]):
                    return False
    return True


def predecessors(s: State) -> tuple[int, ...]:
    n = len(s)
    pred = [0] * n
    for i in range(n):
        bits = s[i]
        while bits:
            b = bits & -bits
            j = b.bit_length() - 1
            pred[j] |= 1 << i
            bits ^= b
    return tuple(pred)


def count_extensions_by_chains(s: State, chains: tuple[tuple[int, ...], ...]) -> int:
    """Exact ideal DP over prefix vectors of a verified chain partition."""
    n = len(s)
    pred = predecessors(s)
    owner = [-1] * n
    for ci, chain in enumerate(chains):
        for x in chain:
            if x < 0 or x >= n or owner[x] != -1:
                raise ValueError("chains are not a partition")
            owner[x] = ci
    if any(x == -1 for x in owner):
        raise ValueError("chains do not cover the ground set")
    for chain in chains:
        for a, b in zip(chain, chain[1:]):
            if not ((s[a] >> b) & 1):
                raise ValueError("listed chain is not increasing in the poset")

    lens = tuple(map(len, chains))
    zero = (0,) * len(chains)
    dp: dict[tuple[int, ...], int] = {zero: 1}
    # Product-grid order is a topological order for prefix-vector transitions.
    from itertools import product
    for v in product(*(range(m + 1) for m in lens)):
        ways = dp.get(v, 0)
        if not ways:
            continue
        selected = 0
        for ci, k in enumerate(v):
            for x in chains[ci][:k]:
                selected |= 1 << x
        for ci, k in enumerate(v):
            if k == lens[ci]:
                continue
            x = chains[ci][k]
            if pred[x] & ~selected:
                continue
            nxt = list(v)
            nxt[ci] += 1
            nt = tuple(nxt)
            dp[nt] = dp.get(nt, 0) + ways
    return dp[lens]


def incomparability_components(s: State) -> list[tuple[int, ...]]:
    n = len(s)
    adj = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if not ((s[i] >> j) & 1) and not ((s[j] >> i) & 1):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    unseen = set(range(n))
    comps = []
    while unseen:
        root = min(unseen)
        todo = [root]
        unseen.remove(root)
        comp = []
        while todo:
            x = todo.pop()
            comp.append(x)
            nxt = [y for y in tuple(unseen) if (adj[x] >> y) & 1]
            for y in nxt:
                unseen.remove(y)
                todo.append(y)
        comps.append(tuple(sorted(comp)))
    return comps


def series_cuts(s: State) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    """Return all nontrivial ordinal cuts, if incomparability is disconnected."""
    comps = incomparability_components(s)
    if len(comps) < 2:
        return []
    # Distinct incomparability components are completely comparable.  Recover
    # their total order by the direction of any cross pair.
    def before(ca: tuple[int, ...], cb: tuple[int, ...]) -> bool:
        return all((s[a] >> b) & 1 for a in ca for b in cb)

    ordered = sorted(comps, key=lambda c: sum(
        1 for other in comps if other != c and before(other, c)))
    for i in range(len(ordered) - 1):
        if not before(ordered[i], ordered[i + 1]):
            raise ValueError("incomparability components not ordinally ordered")
    out = []
    for cut in range(1, len(ordered)):
        a = tuple(x for c in ordered[:cut] for x in c)
        b = tuple(x for c in ordered[cut:] for x in c)
        if all((s[x] >> y) & 1 for x in a for y in b):
            out.append((a, b))
    return out


def induced(s: State, subset: tuple[int, ...]) -> State:
    idx = {old: new for new, old in enumerate(subset)}
    out = []
    for old in subset:
        mask = 0
        for other in subset:
            if (s[old] >> other) & 1:
                mask |= 1 << idx[other]
        out.append(mask)
    return tuple(out)


@dataclass
class SearchStats:
    calls: int = 0
    memo_hits: int = 0
    e_leaves: int = 0
    series_nodes: int = 0
    split_nodes: int = 0
    failures: int = 0
    max_depth: int = 0
    start_time: float = 0.0


class Refuter:
    def __init__(self, chains: tuple[tuple[int, ...], ...], node_limit: int):
        self.chains = chains
        self.node_limit = node_limit
        self.stats = SearchStats(start_time=time.monotonic())
        self.memo: dict[tuple[State, tuple[tuple[int, ...], ...], int], Proof | None] = {}
        self.e_cache: dict[tuple[State, tuple[tuple[int, ...], ...]], int] = {}

    def e(self, s: State, chains: tuple[tuple[int, ...], ...]) -> int:
        key = (s, chains)
        if key not in self.e_cache:
            self.e_cache[key] = count_extensions_by_chains(s, chains)
        return self.e_cache[key]

    @staticmethod
    def query_orbits(s: State, group: tuple[tuple[int, ...], ...]):
        remaining = set(legal_pairs(s))
        out = []
        while remaining:
            rep = min(remaining)
            images: dict[tuple[int, int], tuple[int, ...]] = {}
            for g in group:
                q = tuple(sorted((g[rep[0]], g[rep[1]])))
                if q in remaining:
                    images.setdefault(q, g)
            # The identity is always present for the groups built below.
            orbit = tuple(sorted(images))
            out.append((rep, images))
            remaining.difference_update(orbit)
        return out

    def prove(self, s: State, chains: tuple[tuple[int, ...], ...],
              d: int, group: tuple[tuple[int, ...], ...], depth: int = 0) -> Proof | None:
        key = (s, chains, d)
        if key in self.memo:
            self.stats.memo_hits += 1
            return self.memo[key]
        self.stats.calls += 1
        self.stats.max_depth = max(self.stats.max_depth, depth)
        if self.stats.calls > self.node_limit:
            raise RuntimeError("node limit reached")
        if d < 0:
            raise ValueError("negative budget")
        e = self.e(s, chains)
        if e > (1 << d):
            p: Proof = {"type": "E", "state": s, "chains": chains,
                        "d": d, "e": e}
            self.stats.e_leaves += 1
            self.memo[key] = p
            return p

        # Try ordinal decomposition first.  Budget pairs are searched in a
        # deterministic order; this affects discovery, never certificate trust.
        for a, b in series_cuts(s):
            sa, sb = induced(s, a), induced(s, b)
            amap = {old: new for new, old in enumerate(a)}
            bmap = {old: new for new, old in enumerate(b)}
            ca = tuple(tuple(amap[x] for x in chain if x in amap)
                       for chain in chains)
            cb = tuple(tuple(bmap[x] for x in chain if x in bmap)
                       for chain in chains)
            ca = tuple(c for c in ca if c)
            cb = tuple(c for c in cb if c)
            for da in range(d + 1):
                pa = self.prove(sa, ca, da, identity_group(len(sa)), depth + 1)
                if pa is None:
                    continue
                pb = self.prove(sb, cb, d - da, identity_group(len(sb)), depth + 1)
                if pb is not None:
                    p = {"type": "SERIES", "state": s, "chains": chains, "d": d,
                         "a": a, "b": b, "da": da, "left": pa, "right": pb}
                    self.stats.series_nodes += 1
                    self.memo[key] = p
                    return p

        # Query order is a search heuristic only.  For each query, try the
        # larger-extension child first, but a split node is accepted only after
        # a complete child refutation is found for every legal q.
        orbits = self.query_orbits(s, group)
        # Move-ordering heuristic only: the checker independently verifies the
        # complete orbit partition and the chosen child for each orbit.
        orbits.sort(key=lambda item: max(
            self.e(add_relation(s, *item[0]), chains),
            self.e(add_relation(s, item[0][1], item[0][0]), chains)), reverse=True)
        branches = []
        for (i, j), transports in orbits:
            children = [(add_relation(s, i, j), (i, j)),
                        (add_relation(s, j, i), (j, i))]
            children.sort(key=lambda z: self.e(z[0], chains), reverse=True)
            chosen = None
            # Any subgroup fixing the ordered endpoints pointwise is an
            # automorphism subgroup of the chosen child, so it is safe to use
            # recursively even if this is smaller than the full stabilizer.
            child_group = tuple(g for g in group if g[i] == i and g[j] == j)
            for child, orient in children:
                cp = self.prove(child, chains, d - 1, child_group, depth + 1)
                if cp is not None:
                    chosen = (orient, cp)
                    break
            if chosen is None:
                self.stats.failures += 1
                self.memo[key] = None
                return None
            branches.append({"rep": (i, j), "orientation": chosen[0],
                             "transports": tuple((q, g) for q, g in sorted(transports.items())),
                             "child": chosen[1]})
        if not orbits:
            self.memo[key] = None
            return None
        p = {"type": "ORBIT_SPLIT", "state": s, "chains": chains,
             "d": d, "branches": branches}
        self.stats.split_nodes += 1
        self.memo[key] = p
        return p


def check_proof(root_state: State, root_d: int, proof: Proof,
                chains: tuple[tuple[int, ...], ...]) -> tuple[bool, str, int]:
    """Independent local checker; does not use search memo, ordering, or F."""
    seen: set[int] = set()
    active: set[int] = set()
    checked = 0

    def visit(node: Proof, expected_s: State,
              expected_chains: tuple[tuple[int, ...], ...], expected_d: int) -> None:
        nonlocal checked
        oid = id(node)
        if oid in active:
            raise ValueError("cyclic proof DAG")
        if oid in seen:
            if (node["state"] != expected_s or node["chains"] != expected_chains
                    or node["d"] != expected_d):
                raise ValueError("shared node has wrong judgement")
            return
        active.add(oid)
        checked += 1
        if (node.get("state") != expected_s or node.get("chains") != expected_chains
                or node.get("d") != expected_d):
            raise ValueError("node judgement mismatch")
        if not is_poset(expected_s):
            raise ValueError("invalid poset")
        typ = node.get("type")
        if typ == "E":
            actual = count_extensions_by_chains(expected_s, expected_chains)
            if node.get("e") != actual or actual <= (1 << expected_d):
                raise ValueError("invalid entropy leaf")
        elif typ == "ORBIT_SPLIT":
            expected = set(legal_pairs(expected_s))
            records = node.get("branches", [])
            covered = set()
            for rec in records:
                rep = tuple(rec["rep"])
                if rep not in expected:
                    raise ValueError("orbit representative is not a legal pair")
                orbit_here = set()
                transports = rec.get("transports", ())
                for q_raw, g_raw in transports:
                    q, g = tuple(q_raw), tuple(g_raw)
                    if q not in expected or q in orbit_here:
                        raise ValueError("duplicate or illegal pair in orbit transport list")
                    if sorted((g[rep[0]], g[rep[1]])) != list(q):
                        raise ValueError("transport does not map representative pair")
                    # Check g is a permutation and an automorphism of P.
                    if len(g) != len(expected_s) or set(g) != set(range(len(expected_s))):
                        raise ValueError("transport is not a permutation")
                    mapped = [0] * len(expected_s)
                    for x in range(len(expected_s)):
                        bits = expected_s[x]
                        while bits:
                            bit = bits & -bits
                            y = bit.bit_length() - 1
                            mapped[g[x]] |= 1 << g[y]
                            bits ^= bit
                    if tuple(mapped) != expected_s:
                        raise ValueError("transport is not a poset automorphism")
                    orbit_here.add(q)
                if rep not in orbit_here or covered & orbit_here:
                    raise ValueError("orbit cover is incomplete or overlaps")
                covered |= orbit_here
                orient = tuple(rec["orientation"])
                if orient not in (rep, (rep[1], rep[0])):
                    raise ValueError("chosen outcome is not an orientation of representative")
                child = add_relation(expected_s, *orient)
                visit(rec["child"], child, expected_chains, expected_d - 1)
            if covered != expected:
                raise ValueError("ORBIT_SPLIT does not cover all legal comparisons")
        elif typ == "SERIES":
            a, b = tuple(node["a"]), tuple(node["b"])
            if set(a) & set(b) or set(a) | set(b) != set(range(len(expected_s))):
                raise ValueError("series blocks do not partition keys")
            if not a or not b or not all((expected_s[x] >> y) & 1 for x in a for y in b):
                raise ValueError("not an ordinal sum cut")
            da = node["da"]
            if da < 0 or da > expected_d:
                raise ValueError("invalid series budget split")
            amap = {old: new for new, old in enumerate(a)}
            bmap = {old: new for new, old in enumerate(b)}
            ca = tuple(tuple(amap[x] for x in chain if x in amap)
                       for chain in expected_chains)
            cb = tuple(tuple(bmap[x] for x in chain if x in bmap)
                       for chain in expected_chains)
            ca = tuple(c for c in ca if c)
            cb = tuple(c for c in cb if c)
            visit(node["left"], induced(expected_s, a), ca, da)
            visit(node["right"], induced(expected_s, b), cb, expected_d - da)
        else:
            raise ValueError("unknown proof node type")
        active.remove(oid)
        seen.add(oid)

    try:
        visit(proof, root_state, chains, root_d)
        return True, "accepted", checked
    except Exception as exc:
        return False, str(exc), checked


def encode_dag(root: Proof) -> dict[str, Any]:
    """Serialize shared proof objects as an explicit node table with references."""
    ids: dict[int, int] = {}
    records: list[dict[str, Any] | None] = []

    def visit(node: Proof) -> int:
        oid = id(node)
        if oid in ids:
            return ids[oid]
        idx = len(records)
        ids[oid] = idx
        records.append(None)
        rec: dict[str, Any] = {
            "type": node["type"],
            "state": list(node["state"]),
            "chains": [list(c) for c in node["chains"]],
            "d": node["d"],
        }
        if node["type"] == "E":
            rec["e"] = node["e"]
        elif node["type"] == "ORBIT_SPLIT":
            branches = []
            for b in node["branches"]:
                branches.append({
                    "rep": list(b["rep"]),
                    "orientation": list(b["orientation"]),
                    "transports": [[list(q), list(g)] for q, g in b["transports"]],
                    "child": visit(b["child"]),
                })
            rec["branches"] = branches
        elif node["type"] == "SERIES":
            rec.update({"a": list(node["a"]), "b": list(node["b"]),
                        "da": node["da"], "left": visit(node["left"]),
                        "right": visit(node["right"])})
        records[idx] = rec
        return idx

    root_id = visit(root)
    return {"format": "xy-orbit-refutation-v1", "root": root_id,
            "nodes": records}


def decode_dag(cert: dict[str, Any]) -> Proof:
    """Decode the standalone node-table format, rejecting malformed references."""
    if cert.get("format") != "xy-orbit-refutation-v1":
        raise ValueError("unsupported certificate format")
    raw = cert.get("nodes")
    if not isinstance(raw, list) or not raw:
        raise ValueError("missing node table")
    nodes: list[Proof] = []
    for r in raw:
        if not isinstance(r, dict):
            raise ValueError("malformed node record")
        node: Proof = {
            "type": r.get("type"),
            "state": tuple(r.get("state", ())),
            "chains": tuple(tuple(c) for c in r.get("chains", ())),
            "d": r.get("d"),
        }
        if node["type"] == "E":
            node["e"] = r.get("e")
        elif node["type"] == "ORBIT_SPLIT":
            node["branches"] = []
            for b in r.get("branches", ()):
                node["branches"].append({
                    "rep": tuple(b.get("rep", ())),
                    "orientation": tuple(b.get("orientation", ())),
                    "transports": tuple((tuple(q), tuple(g))
                                         for q, g in b.get("transports", ())),
                    "child_id": b.get("child"),
                })
        elif node["type"] == "SERIES":
            node.update({"a": tuple(r.get("a", ())), "b": tuple(r.get("b", ())),
                         "da": r.get("da"), "left_id": r.get("left"),
                         "right_id": r.get("right")})
        nodes.append(node)

    # Link references only after all records exist; proof cycles are rejected by
    # check_proof's active-stack guard.
    for node in nodes:
        if node["type"] == "ORBIT_SPLIT":
            for b in node["branches"]:
                idx = b.pop("child_id")
                if not isinstance(idx, int) or idx < 0 or idx >= len(nodes):
                    raise ValueError("invalid child reference")
                b["child"] = nodes[idx]
        elif node["type"] == "SERIES":
            li, ri = node.pop("left_id"), node.pop("right_id")
            if not isinstance(li, int) or not isinstance(ri, int) or not (0 <= li < len(nodes)) or not (0 <= ri < len(nodes)):
                raise ValueError("invalid series child reference")
            node["left"], node["right"] = nodes[li], nodes[ri]
    root_id = cert.get("root")
    if not isinstance(root_id, int) or root_id < 0 or root_id >= len(nodes):
        raise ValueError("invalid root reference")
    return nodes[root_id]


def make_x() -> tuple[State, tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]:
    n = 12
    s = [0] * n
    chains = ((0, 1), (2, 3), (4, 5), (6,), (7,), (8,), (9,), (10,), (11,))
    for chain in chains:
        for i, x in enumerate(chain):
            for y in chain[i + 1:]:
                s[x] |= 1 << y
    # Generators for S_3 permuting the directed 2-chains and S_6 on isolates.
    gens = []
    for perm in ((1, 0, 2), (1, 2, 0)):
        g = list(range(n))
        for oldc, newc in enumerate(perm):
            g[2 * oldc] = 2 * newc
            g[2 * oldc + 1] = 2 * newc + 1
        gens.append(tuple(g))
    for i in range(6, 11):
        g = list(range(n))
        g[i], g[i + 1] = g[i + 1], g[i]
        gens.append(tuple(g))
    group = closure_group(tuple(gens), n)
    return tuple(s), chains, group


def make_y() -> tuple[State, tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]:
    n = 12
    s = [0] * n
    # Core a=0,b=1,c=2,d=3 with a<b, a<c<d.
    s[0] |= (1 << 1) | (1 << 2) | (1 << 3)
    s[2] |= 1 << 3
    chains = ((0, 1), (2, 3)) + tuple((i,) for i in range(4, 12))
    gens = []
    for i in range(4, 11):
        g = list(range(n))
        g[i], g[i + 1] = g[i + 1], g[i]
        gens.append(tuple(g))
    group = closure_group(tuple(gens), n)
    return tuple(s), chains, group


def closure_group(generators: tuple[tuple[int, ...], ...], n: int) -> tuple[tuple[int, ...], ...]:
    """Enumerate the modest initial symmetry groups (|Aut(X)|=4320, |Aut(Y)|=40320)."""
    identity = tuple(range(n))
    seen = {identity}
    todo = [identity]
    while todo:
        p = todo.pop()
        for g in generators:
            comp = tuple(g[p[i]] for i in range(n))
            if comp not in seen:
                seen.add(comp)
                todo.append(comp)
    return tuple(seen)


def identity_group(n: int) -> tuple[tuple[int, ...], ...]:
    return (tuple(range(n)),)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", choices=("X", "Y"), required=True)
    ap.add_argument("--node-limit", type=int, default=100000)
    ap.add_argument("--verify", help="verify a serialized certificate instead of searching")
    args = ap.parse_args()
    state, chains, group = make_x() if args.target == "X" else make_y()
    print(f"target={args.target} n=12 legal_moves={len(legal_pairs(state))} "
          f"e={count_extensions_by_chains(state, chains)} d=26 aut_subgroup={len(group)}")
    if args.verify:
        with open(args.verify) as f:
            cert = json.load(f)
        proof = decode_dag(cert)
        ok, msg, checked = check_proof(state, 26, proof, chains)
        print(f"independent_checker={ok} message={msg} distinct_nodes_checked={checked}")
        raise SystemExit(0 if ok else 1)
    search = Refuter(chains, args.node_limit)
    try:
        proof = search.prove(state, chains, 26, group)
        print("search_result=REFUTED" if proof else "search_result=NOT_REFUTED_BY_THIS_CALCULUS")
        if proof:
            ok, msg, checked = check_proof(state, 26, proof, chains)
            print(f"independent_checker={ok} message={msg} distinct_nodes_checked={checked}")
            if not ok:
                raise SystemExit(2)
            with open(f"/tmp/{args.target.lower()}12_refutation.json", "w") as f:
                json.dump(encode_dag(proof), f, separators=(",", ":"))
            print(f"certificate=/tmp/{args.target.lower()}12_refutation.json")
    except RuntimeError as exc:
        print(f"search_result=INCOMPLETE ({exc})")
    st = search.stats
    print(f"calls={st.calls} memo_hits={st.memo_hits} E_leaves={st.e_leaves} "
          f"series_nodes={st.series_nodes} split_nodes={st.split_nodes} "
          f"failed_states={st.failures} max_depth={st.max_depth} "
          f"elapsed={time.monotonic()-st.start_time:.3f}s")


if __name__ == "__main__":
    main()
