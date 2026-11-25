#!/usr/bin/env python3
"""List m-saturated m=4 posets with e<=8, with structure details; search n up to N
with pruning e<=EC and m<=4 (sound because e and m are monotone under deleting a
maximal element / taking induced subposet)."""
import sys, time
from lean import (count_le, mdepth, fval, is_msat, gen_level, incpairs)

def run(maxn, ec):
    reps=[(0,)]; t0=time.time()
    for n in range(1,maxn+1):
        if n>1: reps=gen_level(reps,n)
        keep=[]; found=[]
        for rows in reps:
            e=count_le(rows,n,cap=ec)
            if e>ec: continue
            m=mdepth(rows,n)
            if m>4: continue          # sound prune: induced subposet => m nondecreasing
            keep.append(rows)
            if m==4 and is_msat(rows,n):
                mm,f=fval(rows,n)
                found.append((e,n,f,len(incpairs(rows,n)),rows))
        reps=keep
        f_lt2=[x for x in found if x[2]<2]
        print(f'n={n} kept={len(keep)} msat4={len(found)} '
              f'COUNTER={len(f_lt2)} elapsed={time.time()-t0:.1f}',flush=True)
        for e,nn,f,ni,rows in found:
            print(f'   e={e} n={nn} f={f} ni={ni} rows={rows}',flush=True)
        if f_lt2:
            print('   !!! COUNTEREXAMPLE FOUND',flush=True); return
    print('DONE',flush=True)

if __name__=='__main__':
    run(int(sys.argv[1]) if len(sys.argv)>1 else 10,
        int(sys.argv[2]) if len(sys.argv)>2 else 8)
