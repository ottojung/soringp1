#!/usr/bin/env python3
"""Experiments on non-tightness of the information bound for S(n).

Model: adaptive pairwise-comparison decision trees on n distinct labelled
keys, worst case height.  S(n) is the minimum height.

This script supports the research note docs/research-n12-nontightness.md.
It is exploratory, not a proof.  See scripts/evaluate.py for the reference
minimax evaluator.

Experiments
-----------
A. slack ratios: 2^ceil(log2 n!) / n! and tightness of the information bound.
B. monotonicity of the minimax value in the number of linear extensions.
   This tests whether any invariant that is a *function only of e(P)* (in
   particular efficiency) can explain sortability.
C. admissibility of comparisons at a node, and the forced balanced prefix.
"""

from __future__ import annotations

import argparse
import math
from functools import lru_cache


# --------------------------------------------------------------------------
# Poset utilities.  A poset on {0..n-1} is a tuple succ where succ[i] is a
# bitmask of the elements strictly greater than i (transitively closed).
# --------------------------------------------------------------------------

def add_relation(succ: tuple[int, ...], i: int, j: int) -> tuple[int, ...]:
    """Transitive closure after adding i < j to an already closed state."""
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(len(succ)):
        if x == i or (succ[x] >> i) & 1:
            out[x] |= new_greater
    return tuple(out)


def incomparable_pairs(succ: tuple[int, ...]) -> list[tuple[int, int]]:
    n = len(succ)
    return [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if not (succ[i] >> j) & 1 and not (succ[j] >> i) & 1
    ]


def predecessors(succ: tuple[int, ...]) -> list[int]:
    n = len(succ)
    pred = [0] * n
    for i in range(n):
        for j in range(n):
            if (succ[i] >> j) & 1:
                pred[j] |= 1 << i
    return pred


@lru_cache(maxsize=None)
def linear_extensions(succ: tuple[int, ...]) -> int:
    """Number of linear extensions, via a DP over downsets."""
    n = len(succ)
    pred = predecessors(succ)
    full = (1 << n) - 1
    dp = [0] * (1 << n)
    dp[0] = 1
    for S in range(1, 1 << n):
        total = 0
        m = S
        while m:
            x = (m & -m).bit_length() - 1
            m &= m - 1
            # x is maximal in S iff S \ {x} is a downset, i.e. no y in S\{x}
            # with x < y.  Equivalently x has no successor inside S\{x}.
            if succ[x] & (S ^ (1 << x)) == 0:
                total += dp[S ^ (1 << x)]
        dp[S] = total
    return dp[full]


def all_posets(n: int):
    """All transitively closed posets on n labelled elements (as succ tuples)."""
    start = (0,) * n
    seen = {start}
    stack = [start]
    while stack:
        s = stack.pop()
        for i, j in incomparable_pairs(s):
            for t in (add_relation(s, i, j), add_relation(s, j, i)):
                if t not in seen:
                    seen.add(t)
                    stack.append(t)
    return seen


# --------------------------------------------------------------------------
# Experiment A: slack ratio vs tightness (literature values).
# --------------------------------------------------------------------------

# S(n) for n=0..22, from Peczarski (2012) / Stober-Weiss (2022).
KNOWN_S = {
    0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 9: 19,
    10: 22, 11: 26, 12: 30, 13: 34, 14: 38, 15: 42, 16: 46, 17: 50,
    18: 54, 19: 58, 20: 62, 21: 66, 22: 71,
}


def experiment_A(max_n: int = 22) -> None:
    print("== Experiment A: slack ratio 2^C(n)/n! vs tightness ==")
    print(f"{'n':>3} {'n!':>18} {'C(n)':>5} {'2^C/n!':>9} {'S(n)':>5} {'tight?':>7}")
    for n in range(2, max_n + 1):
        fact = math.factorial(n)
        C = (fact - 1).bit_length()  # ceil(log2 n!) for n! >= 1
        ratio = (2 ** C) / fact
        s = KNOWN_S.get(n)
        tight = "" if s is None else ("yes" if s == C else "NO")
        print(f"{n:>3} {fact:>18} {C:>5} {ratio:>9.4f} {str(s):>5} {tight:>7}")


# --------------------------------------------------------------------------
# Experiment B: minimax value m(P) vs number of linear extensions e(P).
# --------------------------------------------------------------------------

def minimax_all(n: int):
    """Return dict poset -> minimax remaining comparisons m(poset).

    m(P) = 0 if P is a total order, else 1 + min over incomparable pairs
    (i,j) of max(m(P+i<j), m(P+j<i)).
    """
    @lru_cache(maxsize=None)
    def m(succ: tuple[int, ...]) -> int:
        pairs = incomparable_pairs(succ)
        if not pairs:
            return 0
        return 1 + min(
            max(m(add_relation(succ, i, j)), m(add_relation(succ, j, i)))
            for i, j in pairs
        )

    table = {}
    for P in all_posets(n):
        table[P] = m(P)
    return table, m


def experiment_B(n: int) -> None:
    print(f"== Experiment B: monotonicity of m(P) in e(P), n={n} ==")
    table, _ = minimax_all(n)
    by_poset = {P: (linear_extensions(P), table[P]) for P in table}
    # Look for e(P1) < e(P2) but m(P1) > m(P2).  Sweep e in increasing order
    # and remember the maximum m seen so far, with a witness.
    items = sorted(by_poset.items(), key=lambda kv: kv[1][0])
    print(f"  posets examined: {len(items)}")
    violations = 0
    best = None  # smallest e(P2), then largest drop m1 - m2
    maxm = -1
    witness = None  # poset attaining maxm among strictly smaller e
    i = 0
    while i < len(items):
        # process all posets with the same e together, then update maxm
        j = i
        group = []
        while j < len(items) and items[j][1][0] == items[i][1][0]:
            group.append(items[j])
            j += 1
        for P2, (e2, m2) in group:
            if maxm > m2:
                violations += 1
                if best is None or (e2, -(maxm - m2)) < best[0]:
                    best = ((e2, -(maxm - m2)), witness, (witness[1]), P2, (e2, m2))
        for P2, (e2, m2) in group:
            if m2 > maxm:
                maxm = m2
                witness = (P2, (e2, m2))
        i = j
    print(f"  pairs (witnessed) with e(P1)<e(P2) and m(P1)>m(P2): {violations}")
    if best:
        _, P1w, (e1, m1), P2, (e2, m2) = best
        P1 = P1w[0]
        print(f"  example: P1 e={e1} m={m1} ; P2 e={e2} m={m2}")
        print(f"    P1 succ = {P1}")
        print(f"    P2 succ = {P2}")
    print(f"  m nondecreasing in e over all posets? {violations == 0}")
    # Poset-level tightness of the information bound: m(P) vs ceil(log2 e(P)).
    loose = []
    for P, (e, mv) in by_poset.items():
        lb = (e - 1).bit_length()
        if mv > lb:
            loose.append((e, lb, mv, P))
    loose.sort()
    print(f"  posets with m(P) > ceil(log2 e(P)) (local ITLB failure): {len(loose)}")
    for e, lb, mv, P in loose[:3]:
        print(f"    e={e} lb={lb} m={mv} succ={P}")


# --------------------------------------------------------------------------
# Experiment C: admissibility and the forced balanced prefix.
# --------------------------------------------------------------------------

def split_fractions(succ: tuple[int, ...]) -> list[tuple[tuple[int, int], int, int]]:
    """For each incomparable pair, return (pair, e_child1, e_child2)."""
    e = linear_extensions(succ)
    out = []
    for i, j in incomparable_pairs(succ):
        a = linear_extensions(add_relation(succ, i, j))
        b = e - a
        out.append(((i, j), a, b))
    return out


def admissible(succ: tuple[int, ...], remaining: int):
    """Pairs whose heavier child fits in 2^(remaining-1)."""
    budget = 1 << (remaining - 1)
    res = []
    for (pair, a, b) in split_fractions(succ):
        if max(a, b) <= budget:
            res.append((pair, max(a, b), min(a, b)))
    return res


def experiment_C(n: int, height: int, depth: int = 4) -> None:
    """Enumerate the forced balanced prefix for a target height.

    Breadth-first over posets reachable from the antichain by *admissible*
    comparisons only, keeping all children (not just the heavier one).
    WARNING: labelled states grow fast; use small depth for large n.
    """
    print(f"== Experiment C: admissible prefix, n={n}, target height={height} ==")
    antichain = (0,) * n
    level = {antichain}
    for c in range(depth):
        remaining = height - c
        nxt = {}
        for P in level:
            for (pair, hi, lo) in admissible(P, remaining):
                for child in (add_relation(P, *pair), add_relation(P, pair[1], pair[0])):
                    nxt.setdefault(child, linear_extensions(child))
        print(f"  depth {c}: {len(level)} poset(s) -> admissible children {len(nxt)}")
        level = set(nxt.keys())
        if not level:
            print(f"  DEAD at depth {c} (no admissible comparison)")
            return
    print(f"  distinct posets at depth {depth}: {len(level)}")


def chains_poset(n: int, k: int) -> tuple[int, ...]:
    """k disjoint 2-chains 0<1, 2<3, ..., rest free."""
    succ = [0] * n
    for c in range(k):
        succ[2 * c] |= 1 << (2 * c + 1)
    return tuple(succ)


def experiment_C2(n: int, height: int, max_chains: int = 6) -> None:
    """Split fractions along the all-balanced prefix, on explicit shapes.

    After c perfectly balanced (1/2) comparisons the poset is k = c disjoint
    2-chains plus free elements (while 2k <= n).  The fraction threshold for
    an admissible comparison is F = 2^(h-1)/n! (constant along such a prefix).
    """
    print(f"== Experiment C2: balanced prefix shapes, n={n}, height={height} ==")
    F = (2 ** (height - 1)) / math.factorial(n)
    print(f"  threshold fraction F = 2^(h-1)/n! = {F:.4f}")
    print(f"  {'c':>2} {'shape':>14} {'e(P)':>12} {'#pairs':>6} {'min frac':>9} "
          f"{'max frac':>9} {'#admissible':>11}")
    for c in range(0, min(max_chains, n // 2) + 1):
        P = chains_poset(n, c)
        e = linear_extensions(P)
        fracs = []
        for (pair, a, b) in split_fractions(P):
            fracs.append(max(a, b) / e)
        adm = sum(1 for f in fracs if f <= F + 1e-12)
        shape = f"{c}x2-chain" + ("+free" if 2 * c < n else "")
        print(f"  {c:>2} {shape:>14} {e:>12} {len(fracs):>6} "
              f"{min(fracs):>9.4f} {max(fracs):>9.4f} {adm:>11}")
        if adm == 0:
            print(f"     -> NO admissible comparison at this shape for h={height}")
    # After the perfect matching (all elements in 2-chains), the only
    # comparisons are between elements of different chains; report the
    # distinct fractions and whether each is admissible.
    if n % 2 == 0:
        P = chains_poset(n, n // 2)
        e = linear_extensions(P)
        print("  perfect-matching shape fractions:")
        for (pair, a, b) in sorted(split_fractions(P), key=lambda t: -max(t[1], t[2])):
            f = max(a, b) / e
            tag = "adm" if f <= F + 1e-12 else "NO"
            print(f"    pair {pair}: frac={f:.4f} [{tag}]")



def experiment_D(n: int, C: int, cap: int = 3_000_000) -> None:
    """Wells/Peczarski forward search: keep, for every admissible comparison,
    only the heavier child.  If a level becomes empty, P0 is not sortable in
    C comparisons.  Labelled states (no congruence quotient): a superset of
    the quotient search, so an empty level is still a valid obstruction.
    """
    print(f"== Experiment D: forward search n={n}, C={C} ==")
    level = {(0,) * n}
    for c in range(1, C + 1):
        budget = 1 << (C - c)
        nxt = set()
        for P in level:
            e = linear_extensions(P)
            for i, j in incomparable_pairs(P):
                a = linear_extensions(add_relation(P, i, j))
                b = e - a
                if max(a, b) <= budget:
                    if a >= b:
                        nxt.add(add_relation(P, i, j))
                    else:
                        nxt.add(add_relation(P, j, i))
        print(f"  level {c}: |S_{c}| = {len(nxt)} (budget 2^{C-c} = {budget})")
        if not nxt:
            print(f"  DEAD at level {c}: {n} elements are not sortable in {C} comparisons")
            return
        level = nxt
        if len(level) > cap:
            print(f"  cap exceeded at level {c}: {len(level)} > {cap}")
            return
    print(f"  survived all {C} levels (no obstruction found by this search)")


def aut_size(succ: tuple[int, ...]) -> int:
    """Order of the automorphism group, by brute force over permutations."""
    import itertools
    n = len(succ)
    cnt = 0
    for perm in itertools.permutations(range(n)):
        ok = True
        for i in range(n):
            m = 0
            s = succ[i]
            while s:
                b = (s & -s).bit_length() - 1
                s &= s - 1
                m |= 1 << perm[b]
            if m != succ[perm[i]]:
                ok = False
                break
        if ok:
            cnt += 1
    return cnt


def experiment_E(n: int, emax: int = 64) -> None:
    """Symmetry vs local tightness of the information bound.

    Hypothesis: a poset whose information bound is locally loose
    (m(P) > ceil(log2 e(P))) has trivial automorphism group.
    Restricted to posets with e(P) <= emax to keep the brute-force
    automorphism test affordable.
    """
    print(f"== Experiment E: symmetry vs local tightness, n={n}, e <= {emax} ==")
    table, _ = minimax_all(n)
    sel = [P for P in table if linear_extensions(P) <= emax]
    print(f"  posets with e <= {emax}: {len(sel)}")
    loose = 0
    loose_nontrivial_aut = 0
    maxgap = 0
    for P in sel:
        e = linear_extensions(P)
        mv = table[P]
        lb = (e - 1).bit_length()
        if mv > lb:
            loose += 1
            maxgap = max(maxgap, mv - lb)
            if aut_size(P) > 1:
                loose_nontrivial_aut += 1
    print(f"  locally loose posets: {loose}")
    print(f"  loose posets with nontrivial automorphism group: {loose_nontrivial_aut}")
    print(f"  max local gap m(P) - ceil(log2 e(P)): {maxgap}")
    print(f"  hypothesis 'loose => trivial Aut' holds? {loose_nontrivial_aut == 0}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--experiment", choices=["A", "B", "C", "C2", "D", "E", "all"], default="all")
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--height", type=int, default=7)
    ap.add_argument("--depth", type=int, default=4)
    ap.add_argument("--cap", type=int, default=3_000_000)
    ap.add_argument("--emax", type=int, default=64)
    args = ap.parse_args()

    if args.experiment in ("A", "all"):
        experiment_A()
        print()
    if args.experiment in ("B", "all"):
        for n in range(3, args.n + 1):
            experiment_B(n)
            print()
    if args.experiment in ("C", "all"):
        experiment_C(args.n, args.height, args.depth)
    if args.experiment in ("C2", "all"):
        for n in (5, 10, 11, 12):
            C = (math.factorial(n) - 1).bit_length()
            experiment_C2(n, C)
            print()
    if args.experiment == "D":
        experiment_D(args.n, args.height, args.cap)
    if args.experiment == "E":
        experiment_E(args.n, args.emax)


if __name__ == "__main__":
    main()
