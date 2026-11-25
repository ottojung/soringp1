#!/usr/bin/env python3
"""All m=4 posets Q = S_n - (d<c), S_n near-chain (V at bottom). Report m,f,e,incgraph."""
from lean import tc, incpairs, count_le, mdepth, fval, is_msat

def S(n):
    rows=[0]*n
    for j in range(3,n):
        for k in range(j+1,n): rows[j-1]|=(1<<(k-1))
    for j in range(3,n):
        rows[0]|=(1<<(j-1)); rows[1]|=(1<<(j-1))
    return tc(tuple(rows),n)

def remove_rel(rows,n,a,b):
    r=list(rows); r[a]&=~(1<<b); return tc(tuple(r),n)

def main():
    for n in range(3,9):
        s=S(n)
        rel=[(i,j) for i in range(n) for j in range(n) if s[i]&(1<<j)]
        for d,c in rel:
            q=remove_rel(s,n,d,c)
            if q==s: continue
            m=mdepth(q,n)
            if m==4:
                mm,f=fval(q,n); e=count_le(q,n,cap=16); ms=is_msat(q,n)
                inc=incpairs(q,n)
                print(f'n={n} rm {d}<{c}: f={f} e={e} msat={ms} inc={inc}')
        print(f'-- n={n} done')

if __name__=='__main__': main()
