#!/usr/bin/env python3
"""m-saturated posets: every incomparable pair is an optimal comparison.
Equivalently every proper one-relation extension lowers m.
Reduction: WL for an m-saturated extension Q of P implies WL for P.
"""
import sys, collections
sys.path.insert(0, 'scripts')
import oracle_n8 as O

def main(maxn=6):
    reps = [tuple([0])]
    for n in range(1, maxn + 1):
        if n > 1:
            reps = O.gen_level(reps, n)
        sat = []
        for rows in reps:
            m = O.m_depth(rows, n)
            if m < 1:
                continue
            ok = True
            for (a,b) in O.incomparable_pairs(rows,n):
                d1 = O.m_depth(O.child_rows(rows,n,a,b),n)
                d2 = O.m_depth(O.child_rows(rows,n,b,a),n)
                if 1+max(d1,d2) != m:
                    ok = False
                    break
            if ok:
                tset = sorted({min(O.m_depth(O.child_rows(rows,n,a,b),n),
                                   O.m_depth(O.child_rows(rows,n,b,a),n))
                               for (a,b) in O.incomparable_pairs(rows,n)})
                sat.append((m, O.pairs_from_rows(rows,n), tset))
        c = collections.Counter(m for m,_,_ in sat)
        print(f'n={n} saturated={len(sat)}  m-profile={sorted(c.items())}')
        if n <= 5:
            for m, rel, tset in sat[:25]:
                print('   ', m, rel, 'min-depths=', tset)

if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv)>1 else 6)
