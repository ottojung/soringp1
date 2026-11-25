#!/usr/bin/env python3
"""Case analysis: S_n = c1||c2 both below chain c3<...<cn (e=2).
For every relation b<a in S_n, set Q = S_n - (b<a) and compute m,f,e,msat.
Report all Q with m=4 and f<2 (would be counterexamples)."""
import sys, itertools
from lean import tc, child, incpairs, count_le, mdepth, fval, is_msat, pair_depths

def S(n):
    # c1,c2 minimal, incomparable; c3<...<cn chain; c1,c2 < c3..cn
    rows=[0]*n
    for j in range(3,n):        # c3..cn form chain: c3<c4<...
        for k in range(j+1,n):
            rows[j-1] |= (1<<(k-1))
    for j in range(3,n):        # c1,c2 below c3..cn
        rows[0]|=(1<<(j-1)); rows[1]|=(1<<(j-1))
    return tc(tuple(rows),n)

def all_rel(rows,n):
    return [(i,j) for i in range(n) for j in range(n) if rows[i]&(1<<j)]

def remove_rel(rows,n,a,b):
    # remove relation a<b from transitive poset, then close
    r=list(rows); r[a]&=~(1<<b)
    return tc(tuple(r),n)

def main():
    for n in range(3,11):
        s=S(n)
        for a,b in all_rel(s,n):
            q=remove_rel(s,n,a,b)
            if q==s: continue
            m=mdepth(q,n)
            if m==4:
                mm,f=fval(q,n)
                ms=is_msat(q,n)
                e=count_le(q,n,cap=16)
                if f<2 or (ms and f<2):
                    print(f'n={n} remove {a}<{b}: m={m} f={f} e={e} msat={ms} rows={q}')
        print(f'n={n} done',flush=True)

if __name__=='__main__': main()
