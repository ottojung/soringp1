#!/usr/bin/env python3
"""Does greatest-bisimulation compression collapse the PR #32 winning frontier?

Builds the rectangular-chain family of docs/research-winning-frontier-barrier.md
for small (s,L), maps each constructed poset to its bisimulation class in the
full n-element quotient, and counts distinct classes.  Also reports the
iso+dual quotient size for comparison.  Exact integers only.
"""

import itertools
import sys

sys.path.insert(0, "scripts")
from benchmark_symmetry_quotients import (  # noqa: E402
    dual,
    extend,
    make_refined_canon,
    quotient_classes,
)
import bisim_compression as bc  # noqa: E402


def closure(n, edges):
    succ = [0] * n
    for a, b in edges:
        succ = list(extend(tuple(succ), a, b))
    return tuple(succ)


def pr32_posets(s, L):
    """All posets from the PR #32 family with m=0..M extra edges."""
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
    M = len(extra)
    out = []
    for m in range(M + 1):
        for combo in itertools.combinations(extra, m):
            out.append(closure(n, base + list(combo)))
    return out, M


def iso_dual_classes(n):
    canon = make_refined_canon(n)
    vals = quotient_classes(n)
    seen = set()
    for c in vals:
        d = canon(dual(c, n))
        seen.add(min(c, d))
    return len(seen)


def main():
    print("iso+dual quotient sizes (exact):")
    for n in range(2, 8):
        print(f"  n={n}: iso+dual={iso_dual_classes(n)} "
              f"bisim={len(set(bc.greatest_bisim(bc.build_lts(n)[2])))}")

    print("\nPR #32 family: distinct bisimulation classes among constructed states")
    for s, L in [(2, 2), (2, 3), (3, 2), (2, 4), (4, 2)]:
        n = s * L
        if n > 7:
            print(f"  s={s},L={L}: n={n} skipped (quotient too large)")
            continue
        reps, vals, succ, term = bc.build_lts(n)
        blk = bc.greatest_bisim(succ)
        canon = make_refined_canon(n)
        idx = {c: i for i, c in enumerate(reps)}
        posets, M = pr32_posets(s, L)
        classes = set()
        for p in posets:
            classes.add(blk[idx[canon(p)]])
        print(f"  s={s},L={L},n={n}: {len(posets)} constructed posets, "
              f"{M} extra-edge slots, {len(classes)} distinct bisim classes")


if __name__ == "__main__":
    main()
