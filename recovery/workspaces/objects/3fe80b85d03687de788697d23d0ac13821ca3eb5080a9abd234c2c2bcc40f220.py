#!/usr/bin/env python3
"""Cheap structural statistics on all posets up to n=6, using oracle_n8's verified core."""
import sys
sys.path.insert(0, 'scripts')
import oracle_n8 as O

def gen_all(maxn):
    reps = [tuple([0])]
    for n in range(1, maxn + 1):
        if n > 1:
            reps = O.gen_level(reps, n)
        yield n, reps

def main(maxn=6):
    deficit = {}
    child_eq_m = []
    root_imb = {}
    for n, reps in gen_all(maxn):
        for rows in reps:
            m = O.m_depth(rows, n)
            if m < 2:
                continue
            mn_max = -1
            mx_over = None
            for (a, b) in O.incomparable_pairs(rows, n):
                d1 = O.m_depth(O.child_rows(rows, n, a, b), n)
                d2 = O.m_depth(O.child_rows(rows, n, b, a), n)
                mn = min(d1, d2)
                if mn > mn_max:
                    mn_max = mn
                if max(d1, d2) > m - 1:
                    mx_over = (a, b, d1, d2)
            d = (m - 2) - mn_max  # WL wants d <= 0
            deficit[d] = deficit.get(d, 0) + 1
            # Does every WL-satisfying comparison have an optimal companion?
            weak_only = True
            for (a, b) in O.incomparable_pairs(rows, n):
                d1 = O.m_depth(O.child_rows(rows, n, a, b), n)
                d2 = O.m_depth(O.child_rows(rows, n, b, a), n)
                if min(d1, d2) >= m - 2 and 1 + max(d1, d2) == m:
                    weak_only = False
                    break
            if weak_only and mn_max >= m - 2:
                print('WEAK-ONLY', n, O.pairs_from_rows(rows, n), m, mn_max)
            if mx_over:
                child_eq_m.append((n, O.pairs_from_rows(rows, n), m, mx_over))
            # imbalance of optimal roots
            imbs = set()
            for (a, b) in O.incomparable_pairs(rows, n):
                d1 = O.m_depth(O.child_rows(rows, n, a, b), n)
                d2 = O.m_depth(O.child_rows(rows, n, b, a), n)
                if 1 + max(d1, d2) == m:
                    imbs.add(abs(d1 - d2))
            for x in imbs:
                root_imb[x] = root_imb.get(x, 0) + 1
    print('deficit (m-2)-f  counts:', sorted(deficit.items()))
    print('pairs with a child depth > m-1:', len(child_eq_m), child_eq_m[:5])
    print('optimal-root depth gaps:', sorted(root_imb.items()))

if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 6)
