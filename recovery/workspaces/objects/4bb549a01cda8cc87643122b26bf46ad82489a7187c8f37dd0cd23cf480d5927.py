#!/usr/bin/env python3
"""min e for posets with m=3, m=4; and m-saturated m=4 with all f<2 impossible check.
Bounded: enumerate n<=9, prune e<=EC and m<=4."""
import sys, time
from lean import count_le, mdepth, fval, is_msat, gen_level

def run(maxn, EC):
    reps=[(0,)]; t0=time.time()
    mine={3:99,4:99}
    mine_sat={3:99,4:99}
    for n in range(1,maxn+1):
        if n>1: reps=gen_level(reps,n)
        keep=[]
        for rows in reps:
            e=count_le(rows,n,cap=EC)
            if e>EC: continue
            m=mdepth(rows,n)
            if m>4: continue
            keep.append(rows)
            if m in mine:
                mine[m]=min(mine[m],e)
                if is_msat(rows,n):
                    mm,f=fval(rows,n)
                    mine_sat[m]=min(mine_sat[m],e)
        reps=keep
        print(f'n={n} kept={len(keep)} mine(via e<={EC})={mine} mine_sat={mine_sat} '
              f'elapsed={time.time()-t0:.1f}',flush=True)

if __name__=='__main__':
    run(int(sys.argv[1]) if len(sys.argv)>1 else 9,
        int(sys.argv[2]) if len(sys.argv)>2 else 16)
