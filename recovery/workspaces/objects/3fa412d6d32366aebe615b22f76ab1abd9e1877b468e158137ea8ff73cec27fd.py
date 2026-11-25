#!/usr/bin/env python3
"""Test: is every m-saturated poset information-tight, m = ceil(log2 e(P))?
Exhaustive n<=7 using oracle_n8's generator; e(P) by down-set DP."""
import sys, math, functools
sys.path.insert(0, 'scripts')
import oracle_n8 as O

def count_le(rows, n):
    full = (1 << n) - 1
    @functools.lru_cache(None)
    def f(S):
        if S == full:
            return 1
        tot = 0
        for x in range(n):
            if not (S >> x) & 1:
                # x is minimal in complement: all predecessors in S
                pred = 0
                for y in range(n):
                    if rows[y] & (1 << x):
                        pred |= 1 << y
                if pred & ~S == 0:
                    tot += f(S | (1 << x))
        return tot
    return f(0)

def main(maxn=7):
    reps = [tuple([0])]
    for n in range(1, maxn + 1):
        if n > 1:
            reps = O.gen_level(reps, n)
        nsat = ntight = 0
        bad = []
        for rows in reps:
            m = O.m_depth(rows, n)
            if m < 1:
                continue
            sat = all(1 + max(O.m_depth(O.child_rows(rows,n,a,b),n),
                              O.m_depth(O.child_rows(rows,n,b,a),n)) == m
                      for (a,b) in O.incomparable_pairs(rows,n))
            if not sat:
                continue
            nsat += 1
            e = count_le(rows, n)
            ceil_log2 = (e - 1).bit_length()
            if ceil_log2 == m:
                ntight += 1
            else:
                bad.append((O.pairs_from_rows(rows,n), m, e, ceil_log2))
        print(f'n={n} saturated={nsat} info-tight={ntight} failures={len(bad)}', bad[:4])

if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv)>1 else 7)
