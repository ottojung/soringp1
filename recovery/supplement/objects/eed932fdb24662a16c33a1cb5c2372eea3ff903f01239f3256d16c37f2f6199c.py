#!/usr/bin/env python3
"""Frontier state/class counts for an exact OPTIMAL single-policy tree.

Builds one optimal decision tree over isomorphism classes (greedy on F),
then at each depth reports:
  - N_d  : nodes at depth d (distinct labelled states, = distinct iso classes)
  - A_d  : sum of e(P) over INTERNAL nodes at depth d  (= n! - frozen leaves)
  - T_d  : frozen terminal leaves at depth < d
  - K_d  : distinct bisim classes among the nodes at depth d
The invariant is A_d + T_d = n! at every depth.  We test whether frontier
nodes stay in distinct bisim classes (K_d = N_d) or collapse.
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


def main():
    import math
    for n in range(2, 9):
        canon = make_refined_canon(n)
        vals = quotient_classes(n)
        reps_lts, _, actions, term = bpr.build_lts(n)
        idx = {c: i for i, c in enumerate(reps_lts)}
        blk = bpr.greatest_bisim(actions, True)
        # e on iso classes
        ev = {}

        def e(c):
            if c in ev:
                return ev[c]
            ps = incomparable_pairs(c, n)
            if not ps:
                ev[c] = 1
                return 1
            i, j = ps[0]
            v = e(canon(extend(c, i, j))) + e(canon(extend(c, j, i)))
            ev[c] = v
            return v

        root = canon((0,) * n)
        e(root)
        levels = defaultdict(list)
        stack = [(root, 0)]
        while stack:
            c, d = stack.pop()
            levels[d].append(c)
            ps = incomparable_pairs(c, n)
            if not ps:
                continue
            i, j = min(
                ps, key=lambda ij: max(
                    vals[canon(extend(c, *ij))],
                    vals[canon(extend(c, ij[1], ij[0]))]))
            stack.append((canon(extend(c, i, j)), d + 1))
            stack.append((canon(extend(c, j, i)), d + 1))
        maxd = max(levels)
        h = vals[root]
        frozen = 0
        rows = []
        for d in range(maxd + 1):
            nodes = levels[d]
            internal = [c for c in nodes if incomparable_pairs(c, n)]
            leaves_here = len(nodes) - len(internal)
            A = sum(e(c) for c in internal)
            K = len({blk[idx[c]] for c in nodes})
            rows.append((d, len(nodes), len(internal), A, frozen, K))
            frozen += leaves_here
        # invariant check: A + frozen = n! at each depth
        inv_ok = all(A + fr == math.factorial(n) for _, _, _, A, fr, _ in rows)
        collapse = any(K < N for _, N, _, _, _, K in rows)
        print(f"n={n} S(n)={h} invariant_ok={inv_ok} "
              f"frontier_collapses_under_bisim={collapse}")
        for d, N, I, A, fr, K in rows:
            print(f"   d={d:2d} N_d={N:5d} internal={I:5d} A_d={A:8d} "
                  f"frozen={fr:5d} K_d(bisim)={K:5d}")
        print()


if __name__ == "__main__":
    main()
