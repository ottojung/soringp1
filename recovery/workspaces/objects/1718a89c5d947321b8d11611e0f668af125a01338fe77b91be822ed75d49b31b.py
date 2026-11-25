#!/usr/bin/env python3
"""Cross-check oracle.py (labelled recurrence) vs oracle_n8.m_depth at n=9
on hand-picked posets. Not a search; only a validation of the two cores."""
import sys, time
sys.path.insert(0, 'scripts')
import oracle as OLD
import oracle_n8 as NEW

CASES = {
    # 9 elements, 0<1<2<3<4<5<6<7<8 with a single incomparable pair (3,4):
    'one-gap': [(i,j) for i in range(9) for j in range(i+1,9) if (i,j)!=(3,4)],
    # height-2: minima 0,1,2,3; maxima 4,5,6,7,8; chain-like bipartite
    'height2-a': [(0,4),(0,5),(1,5),(1,6),(2,6),(2,7),(3,7),(3,8)],
    # height-2 crown-ish
    'height2-b': [(0,4),(0,5),(1,5),(1,6),(2,6),(2,7),(3,7),(3,8),(4,8)],
}

def rows_of(rel, n):
    r = [0]*n
    for a,b in rel:
        r[a] |= 1 << b
    return NEW.tc(tuple(r), n)

def main():
    n = 9
    for name, rel in CASES.items():
        relc = OLD.closure(set(rel), n)
        if set(relc) != set(rel):
            print(name, 'NOT CLOSED', sorted(set(relc)-set(rel)), flush=True)
            continue
        t = time.time()
        mold = OLD.m_depth(n, frozenset(rel))
        mnew = NEW.m_depth(rows_of(rel, n), n)
        print(name, 'old=', mold, 'new=', mnew, 'agree=', mold==mnew,
              'secs=%.1f' % (time.time()-t), flush=True)

if __name__ == '__main__':
    main()
