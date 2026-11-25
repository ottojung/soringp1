#!/usr/bin/env python3
"""Local diagnostic: is the sibling pairing of a parent P determined by the
set of child classes together with their extension counts e?

The e-route to unpaired = paired only needs: for each P, the set of sibling
pairs {c1,c2} (with e(c1)+e(c2)=e(P)) is the unique matching compatible with
the child class set and the e-labels.  Ambiguity can only arise when two
complementary e-values v and e(P)-v each label at least two distinct child
classes.  We search for the first such P, and also report the first P whose
actual sibling-pair set is not the unique e-compatible matching.

Exact integers only.
"""

import sys
import time
from itertools import combinations

sys.path.insert(0, "scripts")
from benchmark_symmetry_quotients import (  # noqa: E402
    extend,
    incomparable_pairs,
    make_refined_canon,
    quotient_classes,
)


def extension_counts(n, reps):
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


def unique_matching(child_classes, ev, ep):
    """Is the sibling pairing the unique perfect matching with e-sum == ep?

    child_classes: set of distinct child classes.
    Returns (is_unique, actual_pairs) where actual_pairs is the real pairing.
    """
    # actual pairing from actions is supplied by caller; here we test whether
    # *any* matching of the child occurrences with e-sum ep differs.  We only
    # have the class set (not multiplicities), so we test the simplest
    # necessary condition: the bipartite "e-complement" relation is a partial
    # function.  If every child class c has at most one *class* c' with
    # e(c')=ep-e(c), pairing is forced.
    by_e = {}
    for c in child_classes:
        by_e.setdefault(ev[c], set()).add(c)
    forced = True
    for c in child_classes:
        comp = ep - ev[c]
        if len(by_e.get(comp, ())) > 1:
            forced = False
    return forced


def main():
    print("n | classes | first P with both e-sides >=2 | first P with ambiguous pairing")
    for n in range(2, 9):
        t0 = time.perf_counter()
        canon = make_refined_canon(n)
        reps = list(quotient_classes(n).keys())
        ev = extension_counts(n, reps)
        both = None
        ambig = None
        for c in reps:
            ps = incomparable_pairs(c, n)
            if not ps:
                continue
            ep = ev[c]
            child = set()
            actual = set()
            for i, j in ps:
                a = canon(extend(c, i, j))
                b = canon(extend(c, j, i))
                child.add(a)
                child.add(b)
                actual.add(frozenset((a, b)))
            by_e = {}
            for x in child:
                by_e.setdefault(ev[x], set()).add(x)
            for v in by_e:
                w = ep - v
                if v < w and len(by_e[v]) >= 2 and len(by_e.get(w, ())) >= 2:
                    if both is None:
                        both = (c, v, sorted(by_e[v]), w, sorted(by_e.get(w, ())))
            if not unique_matching(child, ev, ep):
                # find whether the actual pairing could be ambiguous: two
                # distinct pairs with the same e-multiset that are both
                # e-compatible would be a real ambiguity.
                if ambig is None:
                    ambig = (c, sorted((ev[a], ev[b]) for a, b in actual))
        dt = time.perf_counter() - t0
        print(f"{n} | {len(reps)} | {both} | {ambig} | {dt:.1f}s")


if __name__ == "__main__":
    main()
