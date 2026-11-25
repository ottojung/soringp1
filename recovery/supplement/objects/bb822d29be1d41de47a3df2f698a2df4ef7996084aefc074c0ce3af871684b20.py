#!/usr/bin/env python3
"""Verify the 2026-10-20T20:33 lever and test the e-injectivity conjecture.

Lever: for every comparison-poset P with e(P) > 1,
    e(P) = min_{children Q} e(Q) + max_{children Q} e(Q),
where children run over BOTH orientations of EVERY incomparable pair.
Equivalently, the child of maximum e and the child of minimum e are siblings
(orientations of the same incomparable pair).

Conjecture (tested, not assumed): on the set of unpaired-bisim child classes
of a fixed P, the map class -> e(class) is injective.

If the conjecture held for every P, then e(P)-e(child) would identify the
action partner of each child class and unpaired bisim would force paired
bisim.  We test it exactly for n <= 8.

Exact integers only.
"""

import sys
import time

sys.path.insert(0, "scripts")
from benchmark_symmetry_quotients import (  # noqa: E402
    extend,
    incomparable_pairs,
    make_refined_canon,
    quotient_classes,
)


def extension_counts(n, reps):
    """e on iso-classes via e(P)=e(P+x<y)+e(P+y<x), computed for every rep."""
    canon = make_refined_canon(n)
    vals = {}

    def solve(c):
        if c in vals:
            return vals[c]
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
    print("n | classes | lever holds | child-e injective | first counterexample | s")
    for n in range(2, 9):
        t0 = time.perf_counter()
        canon = make_refined_canon(n)
        reps = list(quotient_classes(n).keys())
        ev = extension_counts(n, reps)
        lever_ok = True
        inj_ok = True
        counter = None
        for c, ep in ev.items():
            ps = incomparable_pairs(c, n)
            if not ps:
                continue
            child_vals = []
            child_classes = {}
            for i, j in ps:
                for a, b in ((i, j), (j, i)):
                    ch = canon(extend(c, a, b))
                    child_vals.append(ev[ch])
                    child_classes.setdefault(ch, ev[ch])
            # lever: max over all children + min over all children == e(P)
            if min(child_vals) + max(child_vals) != ep:
                lever_ok = False
            # injectivity: distinct child classes carry distinct e
            seen = {}
            for ch, val in child_classes.items():
                if val in seen and seen[val] != ch:
                    inj_ok = False
                    if counter is None:
                        counter = (c, seen[val], ch, val, ep)
                else:
                    seen.setdefault(val, ch)
        dt = time.perf_counter() - t0
        print(f"{n} | {len(ev)} | {lever_ok} | {inj_ok} | "
              f"{'none' if counter is None else counter} | {dt:.2f}s")


if __name__ == "__main__":
    main()
