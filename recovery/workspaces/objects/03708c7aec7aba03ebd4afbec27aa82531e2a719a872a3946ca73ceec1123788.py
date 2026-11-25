#!/usr/bin/env python3
"""Print posets (n<=N) with f(P) = m(P)-2 (WL tight)."""
import sys
sys.path.insert(0, 'scripts')
import oracle_n8 as O

def main(maxn=6):
    reps = [tuple([0])]
    for n in range(1, maxn + 1):
        if n > 1:
            reps = O.gen_level(reps, n)
        tight = []
        for rows in reps:
            m = O.m_depth(rows, n)
            if m < 2:
                continue
            best = -1
            bestpairs = []
            for (a, b) in O.incomparable_pairs(rows, n):
                d1 = O.m_depth(O.child_rows(rows, n, a, b), n)
                d2 = O.m_depth(O.child_rows(rows, n, b, a), n)
                mn = min(d1, d2)
                if mn > best:
                    best, bestpairs = mn, [(a, b, d1, d2, 1 + max(d1, d2) == m)]
                elif mn == best:
                    bestpairs.append((a, b, d1, d2, 1 + max(d1, d2) == m))
            if best == m - 2:
                opt = [(a,b,d1,d2) for (a,b) in O.incomparable_pairs(rows,n)
                       for d1,d2 in [(O.m_depth(O.child_rows(rows,n,a,b),n),
                                      O.m_depth(O.child_rows(rows,n,b,a),n))]
                       if 1+max(d1,d2)==m]
                tight.append((O.pairs_from_rows(rows,n), m, bestpairs, opt))
        print(f'=== n={n} tight={len(tight)}')
        for rel, m, bp, opt in tight[:40]:
            print(f'  rel={rel} m={m} bestmin_pairs={bp} optimal={opt}')

if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 6)
