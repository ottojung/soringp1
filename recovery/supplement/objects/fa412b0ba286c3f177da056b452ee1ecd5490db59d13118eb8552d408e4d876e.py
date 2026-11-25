#!/usr/bin/env python3
"""Sanity check of the depth-partition theorem for optimal sorting trees.

Theorem (elementary).  For any correct decision tree of height h, the distinct
partial-order states at depth t have pairwise disjoint linear-extension sets
whose union is all n! permutations; hence sum_{P at depth t} e(P) = n! and
|S_t| >= n! / 2^(h-t).

We build one optimal tree (greedy on F) for n<=6 and check, at every depth,
that sum e(P) = n! and that the states are pairwise distinct.  This is a
correctness check of the proof, not a research table.
"""

import sys
from collections import defaultdict

sys.path.insert(0, "scripts")
from benchmark_symmetry_quotients import extend, incomparable_pairs  # noqa: E402


def build(n):
    F = {}
    E = {}

    def f(succ):
        if succ in F:
            return F[succ]
        ps = incomparable_pairs(succ, n)
        if not ps:
            F[succ] = 0
            return 0
        best = 1 + min(
            max(f(extend(succ, i, j)), f(extend(succ, j, i))) for i, j in ps
        )
        F[succ] = best
        return best

    def e(succ):
        if succ in E:
            return E[succ]
        ps = incomparable_pairs(succ, n)
        if not ps:
            E[succ] = 1
            return 1
        i, j = ps[0]
        v = e(extend(succ, i, j)) + e(extend(succ, j, i))
        E[succ] = v
        return v

    root = (0,) * n
    f(root)
    levels = defaultdict(list)
    stack = [(root, 0)]
    seen_nodes = set()
    while stack:
        succ, d = stack.pop()
        levels[d].append(succ)
        ps = incomparable_pairs(succ, n)
        if not ps:
            continue
        i, j = min(
            ps, key=lambda ij: max(f(extend(succ, *ij)), f(extend(succ, ij[1], ij[0])))
        )
        stack.append((extend(succ, i, j), d + 1))
        stack.append((extend(succ, j, i), d + 1))
    for states in levels.values():
        for s in states:
            e(s)
    return levels, F, E


def main():
    import math
    for n in range(2, 7):
        levels, F, E = build(n)
        h = F[(0,) * n]
        ok = True
        for d in sorted(levels):
            states = levels[d]
            distinct = len(set(states))
            total_e = sum(E[s] for s in states)
            if distinct != len(states) or total_e != math.factorial(n):
                ok = False
            bound = math.factorial(n) / (2 ** (h - d))
            print(f"n={n} d={d} nodes={len(states)} distinct={distinct} "
                  f"sum_e={total_e} n!={math.factorial(n)} "
                  f"lower={bound:.1f}")
        print(f"n={n} h=S(n)={h} identity_ok={ok}\n")


if __name__ == "__main__":
    main()
