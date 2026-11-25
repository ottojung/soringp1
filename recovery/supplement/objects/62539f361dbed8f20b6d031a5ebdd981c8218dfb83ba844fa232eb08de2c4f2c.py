#!/usr/bin/env python3
"""Robustness of the optimal-policy quotient collapse across tie-breaks.

For each n, build several optimal single-policy trees (different tie-breaks of
the minimax argmin), and report:
  - distinct iso classes visited (whole tree, as a DAG)
  - distinct bisim classes visited
  - max over depths of distinct bisim classes at that depth
Also verify the labelled tree is a correct optimal strategy: it must have
exactly n! leaves and height S(n).
"""

import sys
from collections import defaultdict

sys.path.insert(0, "scripts")
from benchmark_symmetry_quotients import (  # noqa: E402
    extend,
    incomparable_pairs,
    make_refined_canon,
    quotient_classes,
)
import bisim_paired_referee as bpr  # noqa: E402


def build_tree(n, canon, vals, mode):
    root = canon((0,) * n)
    levels = defaultdict(set)
    stack = [(root, 0)]
    visited = set()
    while stack:
        c, d = stack.pop()
        if (c, d) in visited:
            continue
        visited.add((c, d))
        levels[d].add(c)
        ps = incomparable_pairs(c, n)
        if not ps:
            continue
        scored = []
        for ij in ps:
            a = canon(extend(c, *ij))
            b = canon(extend(c, ij[1], ij[0]))
            scored.append((max(vals[a], vals[b]), ij, a, b))
        best = min(s[0] for s in scored)
        cand = [s for s in scored if s[0] == best]
        if mode == "first":
            _, ij, a, b = cand[0]
        elif mode == "last":
            _, ij, a, b = cand[-1]
        else:
            _, ij, a, b = cand[len(cand) // 2]
        stack.append((a, d + 1))
        stack.append((b, d + 1))
    return levels


def labelled_check(n, canon, vals, mode):
    """Count labelled leaves and height for the corresponding labelled tree."""
    root = canon((0,) * n)

    def rec(c, d):
        ps = incomparable_pairs(c, n)
        if not ps:
            return 1, d
        scored = []
        for ij in ps:
            a = canon(extend(c, *ij))
            b = canon(extend(c, ij[1], ij[0]))
            scored.append((max(vals[a], vals[b]), ij, a, b))
        best = min(s[0] for s in scored)
        cand = [s for s in scored if s[0] == best]
        if mode == "first":
            _, ij, a, b = cand[0]
        elif mode == "last":
            _, ij, a, b = cand[-1]
        else:
            _, ij, a, b = cand[len(cand) // 2]
        l1, h1 = rec(a, d + 1)
        l2, h2 = rec(b, d + 1)
        return l1 + l2, max(h1, h2)

    return rec(root, 0)


def main():
    import math
    for n in range(2, 9):
        canon = make_refined_canon(n)
        vals = quotient_classes(n)
        reps_lts, _, actions, term = bpr.build_lts(n)
        idx = {c: i for i, c in enumerate(reps_lts)}
        blk = bpr.greatest_bisim(actions, True)
        line = [f"n={n}"]
        for mode in ("first", "last", "mid"):
            levels = build_tree(n, canon, vals, mode)
            allc = set()
            for s in levels.values():
                allc |= s
            kb = len({blk[idx[c]] for c in allc})
            maxk = max(len({blk[idx[c]] for c in s}) for s in levels.values())
            leaves, h = labelled_check(n, canon, vals, mode)
            assert leaves == math.factorial(n) and h == vals[canon((0,) * n)], (n, mode, leaves, h)
            line.append(f"{mode}: iso={len(allc)} bisim={kb} maxK_d={maxk}")
        print(" | ".join(line))


if __name__ == "__main__":
    main()
