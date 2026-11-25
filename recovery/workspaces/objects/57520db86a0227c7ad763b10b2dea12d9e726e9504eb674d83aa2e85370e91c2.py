#!/usr/bin/env python3
"""Check: if some comparison has a child of depth m(P), is there a balanced
optimal comparison (strong property)?  Exhaustive n<=6."""
import sys
sys.path.insert(0, 'scripts')
import oracle_n8 as O

def main(maxn=6):
    reps = [tuple([0])]
    tot = bad = 0
    for n in range(1, maxn + 1):
        if n > 1:
            reps = O.gen_level(reps, n)
        for rows in reps:
            m = O.m_depth(rows, n)
            if m < 2:
                continue
            depths = []
            strong = False
            for (a, b) in O.incomparable_pairs(rows, n):
                d1 = O.m_depth(O.child_rows(rows, n, a, b), n)
                d2 = O.m_depth(O.child_rows(rows, n, b, a), n)
                depths.append((d1, d2))
                if 1 + max(d1,d2) == m and min(d1,d2) >= m-2:
                    strong = True
            if any(max(d1,d2) >= m for d1,d2 in depths):
                tot += 1
                if not strong:
                    bad += 1
                    print('BAD', n, O.pairs_from_rows(rows,n), m, depths)
    print('depth-preserving posets:', tot, 'without strong:', bad)

if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv)>1 else 6)
