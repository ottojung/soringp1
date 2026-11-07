#!/usr/bin/env python3
"""Independent validation for the core-reduction enumeration.

Checks performed (all must pass):
  1. every stored extension set really is the linear-extension set of its poset;
  2. its size equals an independent subset-DP extension count;
  3. for n <= 6 it equals a brute-force topological-order enumeration;
  4. the canonical form is invariant under all relabellings (n <= 6);
  5. the labelled census of posets with e <= 12 matches the DP implementation
     for n = 4,5,6 (218 / 3110 / 42330) and orbit sizes are consistent;
  6. the two implementations agree on class counts and on every core's depth
     for E = 12, and on class counts for E = 20 at n = 5.
"""
import itertools
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core_sets as cs
import dp_reference as dp


def add(s, a, b):
    return dp.add_rel(s, a, b)


def incomps(s):
    n = len(s)
    return [(a, b) for a in range(n) for b in range(a + 1, n)
            if not (s[a] >> b & 1) and not (s[b] >> a & 1)]


def labelled_posets(n):
    seen = {(0,) * n}
    stack = [(0,) * n]
    while stack:
        s = stack.pop()
        for a, b in incomps(s):
            for t in (add(s, a, b), add(s, b, a)):
                if t not in seen:
                    seen.add(t)
                    stack.append(t)
    return seen


def relabel(s, p):
    n = len(s)
    out = [0] * n
    for x in range(n):
        q = s[x]
        while q:
            y = (q & -q).bit_length() - 1
            q &= q - 1
            out[p[x]] |= 1 << p[y]
    return tuple(out)


def main():
    levels = cs.enumerate_levels(12, 12, None, None)
    failures = []
    for n, cl in levels.items():
        for up, ex in cl.values():
            if cs.up_from_exts(ex, n) != up:
                failures.append(('extension-set/poset mismatch', n))
                break
            if len(ex) != dp.ecount(up):
                failures.append(('count mismatch', n))
                break
            if n <= 6:
                brute = set()

                def dfs(mask, order):
                    if mask == (1 << n) - 1:
                        brute.add(tuple(order))
                        return
                    for x in range(n):
                        if mask >> x & 1:
                            continue
                        if any((up[y] >> x) & 1 for y in range(n) if not (mask >> y) & 1):
                            continue
                        order.append(x)
                        dfs(mask | 1 << x, order)
                        order.pop()

                dfs(0, [])
                if brute != set(tuple(e) for e in ex):
                    failures.append(('brute mismatch', n))
                    break
        if failures:
            break

    # canonical invariance under all relabellings, n <= 6
    for n in range(2, 7):
        perms = list(itertools.permutations(range(n)))
        for up, ex in levels[n].values():
            c0 = cs.canonical(up)
            for p in perms:
                if cs.canonical(relabel(up, p)) != c0:
                    failures.append(('canonical not invariant', n))
                    break
            if failures:
                break
        if failures:
            break

    # labelled census cross-check for E = 12 and orbit sums
    for n, expected in ((4, 218), (5, 3110), (6, 42330)):
        lab = [s for s in labelled_posets(n) if dp.ecount(s) <= 12]
        if len(lab) != expected:
            failures.append(('labelled census', n))
        perms = list(itertools.permutations(range(n)))
        total = 0
        for up, ex in levels[n].values():
            aut = sum(1 for p in perms if relabel(up, p) == up)
            total += len(perms) // aut
        if total != expected:
            failures.append(('orbit sum', n))

    # cross-implementation agreement at E = 12
    reps = dp.enumerate_classes()
    for n in range(2, 13):
        if len(reps[n]) != len(levels[n]):
            failures.append(('class-count disagreement', n))
        for up, ex in levels[n].values():
            c = cs.canonical(up)
            if c not in reps[n]:
                failures.append(('poset missing from DP enumeration', n))
        for up, ex in levels[n].values():
            if cs.minimax(ex) != dp.minimax(cs.canonical(up)):
                failures.append(('depth disagreement', n))

    # E = 20 class count at n = 5 agrees with the labelled census orbit sum
    lv20 = cs.enumerate_levels(20, 5, None, None)
    lab = [s for s in labelled_posets(5) if dp.ecount(s) <= 20]
    perms = list(itertools.permutations(range(5)))
    total = 0
    for up, ex in lv20[5].values():
        aut = sum(1 for p in perms if relabel(up, p) == up)
        total += len(perms) // aut
    if total != len(lab):
        failures.append(('E=20 labelled count', 5))

    if failures:
        print('FAILURES:', failures)
        return 1
    print('all validation checks passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
