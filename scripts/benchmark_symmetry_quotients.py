#!/usr/bin/env python3
"""Reproducible microbenchmarks for symmetry quotients of the exact minimax
sorting DP.  Companion to docs/research-compression-next.md.

Model (docs/problem.md, docs/upper-bound.md, SoringP1/Minimax.lean):
  A state is the strict partial order (transitive closure) induced by the
  comparisons made so far, stored as successor bitmasks: succ[i] has bit j set
  iff i < j.  The remaining minimax cost is

      F(P) = 0                                                   if P is total,
      F(P) = 1 + min_{x,y incomparable} max(F(P+x<y), F(P+y<x))   otherwise,

  and S(n) = F(empty poset).  Reachable states are exactly the labelled posets
  on n points (OEIS A001035).

Quotient variants (all must return the same S(n)):
  labelled          memoised DP over labelled posets            (A001035)
  iso               quotient by key relabelling S_n             (A000112)
  iso+dual          additionally quotient by order duality Z_2
  iso+dual+orbits   additionally reduce moves to Aut(P)-orbits of incomparable
                    pairs (sound: Aut(P) acts by value-preserving isomorphisms)

Falsification checks (--falsify):
  * duality may not be used to drop a comparison branch (n=3 witness);
  * degree-based move identification is unsound (n=6 witness);
  * the comparability-graph transition is not well defined on graph classes
    (n=5 witness), even though F happens to be class-invariant for n <= 7.

No external libraries.  The algorithms are deterministic; --seed only controls
an optional move-order shuffle, which must not change any value.
"""

import argparse
import itertools
import random
import time
import tracemalloc
from functools import lru_cache


# --------------------------------------------------------------------------
# Labelled posets as successor bitmasks.
# --------------------------------------------------------------------------

def extend(succ, i, j):
    """Transitive closure after adding i < j to an already closed state."""
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(len(succ)):
        if x == i or (succ[x] & (1 << i)):
            out[x] |= new_greater
    return tuple(out)


def incomparable_pairs(succ, n):
    return [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if not (succ[i] >> j & 1) and not (succ[j] >> i & 1)
    ]


def dual(succ, n):
    """Order dual: i < j in P^op iff j < i in P."""
    out = [0] * n
    for a in range(n):
        m = 0
        for b in range(n):
            if succ[b] >> a & 1:
                m |= 1 << b
        out[a] = m
    return tuple(out)


def _measure(fn):
    tracemalloc.start()
    t0 = time.perf_counter()
    result = fn()
    dt = time.perf_counter() - t0
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result, dt, peak


# --------------------------------------------------------------------------
# Canonical form under S_n: 2-dimensional colour refinement, then the
# lexicographically least encoding over relabellings that preserve colours.
# Any isomorphism preserves colours, so this is a complete invariant.
# --------------------------------------------------------------------------

def refine_colors(succ, n):
    color = [bin(succ[i]).count("1") for i in range(n)]
    while True:
        sig = []
        for i in range(n):
            down = tuple(sorted(color[j] for j in range(n) if succ[i] >> j & 1))
            up = tuple(sorted(color[j] for j in range(n) if succ[j] >> i & 1))
            sig.append((color[i], down, up))
        order = {v: k for k, v in enumerate(sorted(set(sig)))}
        comp = [order[v] for v in sig]
        if comp == color:
            return color
        color = comp


def _encode(succ, perm, n):
    new = []
    for a in range(n):
        bits = succ[perm[a]]
        m = 0
        for b in range(n):
            if bits >> perm[b] & 1:
                m |= 1 << b
        new.append(m)
    return tuple(new)


def make_refined_canon(n):
    cache = {}

    def canon(succ):
        if succ in cache:
            return cache[succ]
        color = refine_colors(succ, n)
        groups = {}
        for i, c in enumerate(color):
            groups.setdefault(c, []).append(i)
        gs = [groups[c] for c in sorted(groups)]
        best = None
        for combo in itertools.product(*(itertools.permutations(g) for g in gs)):
            perm = [x for p in combo for x in p]
            e = _encode(succ, perm, n)
            if best is None or e < best:
                best = e
        cache[succ] = best
        return best

    return canon


def automorphisms(succ, n):
    """All permutations p with p(a) preserving succ (a -> p[a] is an iso)."""
    result = []
    for p in itertools.permutations(range(n)):
        ok = True
        for a in range(n):
            img = 0
            for b in range(n):
                if succ[a] >> b & 1:
                    img |= 1 << p[b]
            if img != succ[p[a]]:
                ok = False
                break
        if ok:
            result.append(p)
    return result


def orbit_reps(succ, n):
    """One unordered incomparable pair per Aut(P)-orbit (sound move quotient)."""
    aut = automorphisms(succ, n)
    covered = set()
    reps = []
    for (i, j) in incomparable_pairs(succ, n):
        if (i, j) in covered:
            continue
        reps.append((i, j))
        for p in aut:
            a, b = p[i], p[j]
            covered.add((min(a, b), max(a, b)))
    return reps


def orbit_stats(n):
    """Aggregate move-orbit data over isomorphism classes of posets on n points."""
    vals = labelled_values(n)
    canon = make_refined_canon(n)
    seen = set()
    total_pairs = total_orbits = sum_aut = nontrivial = 0
    for succ in vals:
        c = canon(succ)
        if c in seen:
            continue
        seen.add(c)
        ps = incomparable_pairs(c, n)
        aut = automorphisms(c, n)
        reps = orbit_reps(c, n)
        total_pairs += len(ps)
        total_orbits += len(reps)
        sum_aut += len(aut)
        if len(aut) > 1:
            nontrivial += 1
    return {
        "classes": len(seen),
        "pairs": total_pairs,
        "orbits": total_orbits,
        "classes_nontrivial_aut": nontrivial,
        "sum_aut": sum_aut,
    }


# --------------------------------------------------------------------------
# DP variants.
# --------------------------------------------------------------------------

def labelled_solve(n):
    states = {}

    def solve(succ):
        if succ in states:
            return states[succ]
        ps = incomparable_pairs(succ, n)
        if not ps:
            states[succ] = 0
            return 0
        best = 1 + min(
            max(solve(extend(succ, i, j)), solve(extend(succ, j, i)))
            for i, j in ps
        )
        states[succ] = best
        return best

    value = solve((0,) * n)
    return value, len(states)


def iso_solve(n, use_dual=False, use_orbits=False, shuffle=False, rng=None):
    canon = make_refined_canon(n)

    def C(succ):
        c = canon(succ)
        if use_dual:
            d = canon(dual(succ, n))
            if d < c:
                c = d
        return c

    states = {}
    stats = {"canon_calls": 0, "moves": 0}

    def solve(c):
        if c in states:
            return states[c]
        ps = incomparable_pairs(c, n)
        if not ps:
            states[c] = 0
            return 0
        if use_orbits:
            ps = orbit_reps(c, n)
        if shuffle:
            ps = list(ps)
            rng.shuffle(ps)
        best = None
        for i, j in ps:
            stats["moves"] += 1
            stats["canon_calls"] += 2
            a = C(extend(c, i, j))
            b = C(extend(c, j, i))
            v = 1 + max(solve(a), solve(b))
            if best is None or v < best:
                best = v
        states[c] = best
        return best

    value = solve(C((0,) * n))
    return value, len(states), stats["canon_calls"], stats["moves"]


# --------------------------------------------------------------------------
# Falsification witnesses.
# --------------------------------------------------------------------------

def labelled_values(n):
    states = {}

    def solve(succ):
        if succ in states:
            return states[succ]
        ps = incomparable_pairs(succ, n)
        if not ps:
            states[succ] = 0
            return 0
        best = 1 + min(
            max(solve(extend(succ, i, j)), solve(extend(succ, j, i)))
            for i, j in ps
        )
        states[succ] = best
        return best

    solve((0,) * n)
    return states


def falsify_dual_branch():
    """The two children of one comparison can have different F, so duality does
    not license dropping a branch.  Smallest witness at n=3."""
    n = 3
    vals = labelled_values(n)
    for succ in vals:
        for (i, j) in incomparable_pairs(succ, n):
            a = vals[extend(succ, i, j)]
            b = vals[extend(succ, j, i)]
            if a != b:
                return n, succ, (i, j), a, b
    return None


def _canon_brute(succ, n):
    best = None
    for p in itertools.permutations(range(n)):
        e = _encode(succ, p, n)
        if best is None or e < best:
            best = e
    return best


def falsify_degree_move(n=6):
    """Two incomparable pairs whose endpoints have matching (in,out) degrees but
    whose move values differ: degree is not a sound move invariant."""
    vals = labelled_values(n)
    seen = set()
    for succ in vals:
        c = _canon_brute(succ, n)
        if c in seen:
            continue
        seen.add(c)
        indeg = [bin(c[i]).count("1") for i in range(n)]
        outdeg = [sum(1 for j in range(n) if c[j] >> i & 1) for i in range(n)]
        deg = list(zip(indeg, outdeg))
        sig_map = {}
        for (i, j) in incomparable_pairs(c, n):
            sig = (min(deg[i], deg[j]), max(deg[i], deg[j]))
            v = max(vals[extend(c, i, j)], vals[extend(c, j, i)])
            sig_map.setdefault(sig, set()).add(v)
        for sig, vs in sig_map.items():
            if len(vs) > 1:
                return n, c, deg, sig, sorted(vs)
    return None


def _cgraph(succ, n):
    return frozenset(
        (min(i, j), max(i, j))
        for i in range(n)
        for j in range(i + 1, n)
        if (succ[i] >> j & 1) or (succ[j] >> i & 1)
    )


def quotient_classes(n):
    """Map each isomorphism class (canonical rep) to its value F."""
    canon = make_refined_canon(n)
    vals = {}

    def solve(c):
        if c in vals:
            return vals[c]
        ps = incomparable_pairs(c, n)
        if not ps:
            vals[c] = 0
            return 0
        best = 1 + min(
            max(solve(canon(extend(c, i, j))), solve(canon(extend(c, j, i))))
            for i, j in ps
        )
        vals[c] = best
        return best

    solve(canon((0,) * n))
    return vals


def _adjacency(succ, n):
    adj = [0] * n
    for i in range(n):
        for j in range(n):
            if succ[i] >> j & 1:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    return tuple(adj)


def _wl_graph_hist(adj, n):
    color = [bin(adj[i]).count("1") for i in range(n)]
    while True:
        sig = [(color[i], tuple(sorted(color[j] for j in range(n) if adj[i] >> j & 1)))
               for i in range(n)]
        order = {v: k for k, v in enumerate(sorted(set(sig)))}
        comp = [order[v] for v in sig]
        if comp == color:
            return tuple(sorted(color))
        color = comp


def _graph_canon(adj, n):
    best = None
    ps = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for p in itertools.permutations(range(n)):
        e = tuple(sorted((min(p[i], p[j]), max(p[i], p[j]))
                         for (i, j) in ps if adj[i] >> j & 1))
        if best is None or e < best:
            best = e
    return best


def falsify_comparability_graph(n=7):
    """Two posets with isomorphic comparability graphs but different F: the
    graph is a comparability invariant for e(P) but not for F.  Witness n=7."""
    vals = quotient_classes(n)
    adj_of = {c: _adjacency(c, n) for c in vals}
    buckets = {}
    for c, v in vals.items():
        buckets.setdefault(_wl_graph_hist(adj_of[c], n), []).append((c, v))
    for members in buckets.values():
        if len({v for _, v in members}) <= 1:
            continue
        by_graph = {}
        for c, v in members:
            by_graph.setdefault(_graph_canon(adj_of[c], n), []).append((c, v))
        for g, ms in by_graph.items():
            by_f = {}
            for c, v in ms:
                by_f.setdefault(v, c)
            if len(by_f) > 1:
                return n, g, sorted(by_f.items())
    return None


def falsify_graph_transition(n=5):
    """Two posets with the same comparability graph and a common non-edge whose
    closures have different comparability graphs: the graph transition is not
    well defined, so the graph cannot serve as a DP state."""
    vals = labelled_values(n)
    by_g = {}
    for s in vals:
        by_g.setdefault(_cgraph(s, n), []).append(s)
    for g, ss in by_g.items():
        if len(ss) < 2:
            continue
        for s in ss:
            for (i, j) in incomparable_pairs(s, n):
                g1 = _cgraph(extend(s, i, j), n)
                for t in ss:
                    if t is s or _cgraph(t, n) != g:
                        continue
                    g2 = _cgraph(extend(t, i, j), n)
                    if g1 != g2:
                        return n, g, s, t, (i, j), g1, g2
    return None


def run_falsifications():
    print("Falsification witnesses")
    w = falsify_dual_branch()
    print(f"  duality branch-drop (n={w[0]}): poset {w[1]} pair {w[2]} "
          f"-> children F={w[3]} vs F={w[4]}  (differ; branch may not be dropped)")
    w = falsify_degree_move(6)
    if w:
        print(f"  degree move quotient (n={w[0]}): poset {w[1]} degrees {w[2]} "
              f"signature {w[3]} -> move values {w[4]} (unsound)")
    w = falsify_comparability_graph(7)
    if w:
        n, g, by_f = w
        print(f"  comparability graph not F-invariant (n={n}): same graph {g} "
              f"realised by posets with F values {[v for v, _ in by_f]} "
              f"(posets {[c for _, c in by_f]})")
    w = falsify_graph_transition(5)
    if w:
        print(f"  comparability-graph transition (n={w[0]}): same graph, pair "
              f"{w[4]} -> successor graphs differ by "
              f"{sorted(w[5] ^ w[6])} (transition ill defined)")


# --------------------------------------------------------------------------
# Benchmark driver.
# --------------------------------------------------------------------------

KNOWN = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 12: 30}
A001035 = {0: 1, 1: 1, 2: 3, 3: 19, 4: 219, 5: 4231, 6: 130023}
A000112 = {0: 1, 1: 1, 2: 2, 3: 5, 4: 16, 5: 63, 6: 318, 7: 2045}
DUAL_CLASSES = {0: 1, 1: 1, 2: 2, 3: 4, 4: 12, 5: 39, 6: 184}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--max-n", type=int, default=5)
    ap.add_argument("--labelled-cap", type=int, default=6,
                    help="largest n for the labelled DP (n=7 is ~185 s)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--shuffle-moves", action="store_true",
                    help="shuffle move order with --seed (value must not change)")
    ap.add_argument("--falsify", action="store_true")
    args = ap.parse_args()

    random.seed(args.seed)
    rng = random.Random(args.seed)

    print(f"seed={args.seed} shuffle_moves={args.shuffle_moves} "
          f"max_n={args.max_n}")
    print()
    header = ("n | S(n) | labelled S (states, time, mem) "
              "| iso S (classes, time, mem) "
              "| iso+dual S (classes, time, mem) "
              "| +orbits S (moves, time, mem)")
    print(header)
    print("-" * len(header))
    ok = True
    move_rows = []
    for n in range(0, args.max_n + 1):
        cells = [f"{n}", str(KNOWN.get(n, "?"))]

        if n <= args.labelled_cap:
            (val, states), dt, peak = _measure(lambda: labelled_solve(n))
            cells.append(f"{val} ({states}, {dt:.3f}s, {peak/1024:.0f}K)")
            if val != KNOWN[n]:
                ok = False
        else:
            cells.append("skipped")

        (val, cls, calls, moves), dt, peak = _measure(
            lambda: iso_solve(n, use_dual=False, use_orbits=False,
                              shuffle=args.shuffle_moves, rng=rng))
        cells.append(f"{val} ({cls}, {dt:.3f}s, {peak/1024:.0f}K)")
        if val != KNOWN[n]:
            ok = False
        iso_classes = cls

        (val, cls, calls, moves), dt, peak = _measure(
            lambda: iso_solve(n, use_dual=True, use_orbits=False,
                              shuffle=args.shuffle_moves, rng=rng))
        cells.append(f"{val} ({cls}, {dt:.3f}s, {peak/1024:.0f}K)")
        if val != KNOWN[n]:
            ok = False
        dual_classes = cls
        moves_noorbit = moves

        (val, cls, calls, moves), dt, peak = _measure(
            lambda: iso_solve(n, use_dual=True, use_orbits=True,
                              shuffle=args.shuffle_moves, rng=rng))
        cells.append(f"{val} ({moves}, {dt:.3f}s, {peak/1024:.0f}K)")
        if val != KNOWN[n]:
            ok = False

        print(" | ".join(cells))
        move_rows.append((n, iso_classes, dual_classes, moves_noorbit, moves))

    print()
    print("State/move counts by variant")
    print("n | iso classes A000112 | iso+dual classes | iso+dual move terms "
          "| +orbit move terms")
    for n, ic, dc, mn, mo in move_rows:
        ref = A000112.get(n, "?")
        dref = DUAL_CLASSES.get(n, "?")
        print(f"{n} | {ic} (ref {ref}) | {dc} (ref {dref}) | {mn} | {mo}")

    print()
    print("Automorphism pair-orbit statistics over isomorphism classes")
    print("n | classes | incomparable pairs | Aut-orbits | reduction "
          "| classes with nontrivial Aut | sum |Aut|")
    for n in range(0, args.max_n + 1):
        st = orbit_stats(n)
        red = 1.0 - st["orbits"] / st["pairs"] if st["pairs"] else 0.0
        print(f"{n} | {st['classes']} | {st['pairs']} | {st['orbits']} "
              f"| {red:.1%} | {st['classes_nontrivial_aut']} | {st['sum_aut']}")

    print()
    print("ALL VALUES MATCH KNOWN S(n)" if ok else "MISMATCH DETECTED")

    if args.falsify:
        print()
        run_falsifications()


if __name__ == "__main__":
    main()
