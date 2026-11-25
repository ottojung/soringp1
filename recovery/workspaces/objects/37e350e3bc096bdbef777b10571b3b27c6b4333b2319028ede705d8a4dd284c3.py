#!/usr/bin/env python3
"""Bounded search: m-saturated m=4 posets, record e(Q), f(Q), incomparability count.

Filter by e(P)<=ECAP early (cheap) before exact minimax.  No full n=9 enumeration.
"""
import sys, time
from lean import (tc, child, incpairs, npairs, count_le, mdepth, fval,
                  is_msat, canon, gen_level, pair_depths)

def run(maxn, ec):
    reps=[(0,)]
    t0=time.time()
    for n in range(1,maxn+1):
        if n>1: reps=gen_level(reps,n)
        msat4=[]
        small_e=0
        for rows in reps:
            e=count_le(rows,n,cap=ec)
            if e>ec: continue
            small_e+=1
            m=mdepth(rows,n)
            if m!=4: continue
            if is_msat(rows,n):
                mm,f=fval(rows,n)
                msat4.append((e,len(incpairs(rows,n)),f,rows))
        print(f'n={n} classes={len(reps)} e<={ec}:{small_e} '
              f'msat4={len(msat4)} elapsed={time.time()-t0:.1f}',flush=True)
        for e,ni,f,rows in msat4[:40]:
            flag = '  <== F<2 COUNTEREXAMPLE' if f<2 else ''
            print(f'   e={e} nincomp={ni} f={f}{flag} rows={rows}',flush=True)
        if msat4:
            lo=min(x[0] for x in msat4)
            print(f'   min e among msat4 = {lo}',flush=True)
        sys.stdout.flush()

if __name__=='__main__':
    maxn=int(sys.argv[1]) if len(sys.argv)>1 else 8
    ec=int(sys.argv[2]) if len(sys.argv)>2 else 12
    run(maxn,ec)
