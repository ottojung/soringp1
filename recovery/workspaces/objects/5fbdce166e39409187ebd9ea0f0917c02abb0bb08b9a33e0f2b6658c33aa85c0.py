#!/usr/bin/env python3
"""
Small-n experiment for automorphism/isomorphism-quotient winning states.
Counts labelled reachable states, isomorphism classes, and winning states
(F(P) <= S(n)-depth) for n <= 5 by exhaustive transcript DFS.

Labels: [experiment]. Run: python3 scripts/autquotient_smalln_report.py
"""
import itertools
from functools import lru_cache


def closure(n, rel):
    r = [row[:] for row in rel]
    changed = True
    while changed:
        changed = False
        for i in range(n):
            for k in range(n):
                if r[i][k]:
                    for j in range(n):
                        if r[k][j] and not r[i][j]:
                            r[i][j] = True
                            changed = True
    return tuple(tuple(row) for row in r)


def is_total(n, rel):
    for i in range(n):
        for j in range(i + 1, n):
            if not rel[i][j] and not rel[j][i]:
                return False
    return True


def incomparable_pairs(n, rel):
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if not rel[i][j] and not rel[j][i]:
                pairs.append((i, j))
    return pairs


def add_cmp(n, rel, i, j, outcome):
    r = [list(row) for row in rel]
    if outcome:
        r[i][j] = True
    else:
        r[j][i] = True
    return closure(n, r)


def canonical(n, rel):
    best = None
    elems = list(range(n))
    for perm in itertools.permutations(elems):
        bits = []
        for i in range(n):
            pi = perm[i]
            for j in range(n):
                pj = perm[j]
                bits.append('1' if rel[pi][pj] else '0')
        s = ''.join(bits)
        if best is None or s < best:
            best = s
    return best


def S_value(n):
    vals = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7}
    return vals[n]


def main():
    for n in range(1, 6):
        S = S_value(n)
        empty = closure(n, [[False] * n for _ in range(n)])

        @lru_cache(None)
        def F(rel):
            if is_total(n, rel):
                return 0
            best = None
            for i, j in incomparable_pairs(n, rel):
                v = max(F(add_cmp(n, rel, i, j, True)), F(add_cmp(n, rel, i, j, False)))
                if best is None or v < best:
                    best = v
            return 1 + best

        states_at_depth = [set() for _ in range(S + 1)]
        states_at_depth[0].add(empty)
        seen = set()

        def dfs(rel, d):
            if d == S:
                return
            key = (rel, d)
            if key in seen:
                return
            seen.add(key)
            for i, j in incomparable_pairs(n, rel):
                for out in (True, False):
                    nr = add_cmp(n, rel, i, j, out)
                    states_at_depth[d + 1].add(nr)
                    dfs(nr, d + 1)

        dfs(empty, 0)
        print(f"n={n}, S(n)={S}")
        for d in range(S + 1):
            rels = states_at_depth[d]
            cans = set(canonical(n, r) for r in rels)
            win = [r for r in rels if F(r) <= S - d]
            winc = set(canonical(n, r) for r in win)
            print(
                f"  depth {d}: labelled reachable={len(rels)}, "
                f"isom classes={len(cans)}, winning labelled={len(win)}, "
                f"winning isom={len(winc)}"
            )
        print()


if __name__ == '__main__':
    main()
