#!/usr/bin/env python3
"""PR #32 winning-frontier family under iso, e, and bisimulation quotients.

Family (docs/research-winning-frontier-barrier.md): s columns, L levels,
n = sL.  Base edges (i,x)<(i+1,x); extra edges (i,x)<(i+1,y), x!=y, one
possible slot per adjacent level pair and ordered column pair.  Choose any
subset A of the M=(L-1)(s^2-s) slots; the transitive closure is P_A.

Reports, for small (s,L): number of constructed P_A, distinct isomorphism
classes, distinct e-values, and distinct unpaired/paired bisim classes
(paired = unpaired by the referee result).  Exact integers only.
"""

import itertools
import sys

sys.path.insert(0, "scripts")
from benchmark_symmetry_quotients import (  # noqa: E402
    extend,
    make_refined_canon,
    quotient_classes,
)
import bisim_paired_referee as bpr  # noqa: E402


def closure(n, edges):
    succ = [0] * n
    for a, b in edges:
        succ = list(extend(tuple(succ), a, b))
    return tuple(succ)


def pr32_posets(s, L):
    n = s * L
    vid = lambda i, x: i * s + x
    base = []
    for x in range(s):
        for i in range(L - 1):
            base.append((vid(i, x), vid(i + 1, x)))
    extra = []
    for i in range(L - 1):
        for x in range(s):
            for y in range(s):
                if x != y:
                    extra.append((vid(i, x), vid(i + 1, y)))
    out = []
    for m in range(len(extra) + 1):
        for combo in itertools.combinations(extra, m):
            out.append(closure(n, base + list(combo)))
    return out, len(extra)


def extension_counts(n, reps):
    canon = make_refined_canon(n)
    vals = {}

    def solve(c):
        if c in vals:
            return vals[c]
        from benchmark_symmetry_quotients import incomparable_pairs
        ps = incomparable_pairs(c, n)
        if not ps:
            vals[c] = 1
            return 1
        i, j = ps[0]
        v = solve(canon(extend(c, i, j))) + solve(canon(extend(c, j, i)))
        vals[c] = v
        return v

    for c in reps:
        solve(c)
    return vals


def main():
    print("s,L,n | constructed | iso classes | distinct e | bisim classes | M")
    for s, L in [(2, 2), (2, 3), (3, 2), (2, 4), (4, 2), (3, 3)]:
        n = s * L
        if n > 8:
            print(f"{s},{L},{n} | skipped (n>8)")
            continue
        canon = make_refined_canon(n)
        reps = list(quotient_classes(n).keys())
        ev = extension_counts(n, reps)
        reps_lts, vals, actions, term = bpr.build_lts(n)
        idx = {c: i for i, c in enumerate(reps_lts)}
        blk = bpr.greatest_bisim(actions, True)
        posets, M = pr32_posets(s, L)
        iso = set()
        bcls = set()
        eset = set()
        for p in posets:
            c = canon(p)
            iso.add(c)
            bcls.add(blk[idx[c]])
            eset.add(ev[c])
        print(f"{s},{L},{n} | {len(posets)} | {len(iso)} | {len(eset)} | "
              f"{len(bcls)} | {M}")


if __name__ == "__main__":
    main()
