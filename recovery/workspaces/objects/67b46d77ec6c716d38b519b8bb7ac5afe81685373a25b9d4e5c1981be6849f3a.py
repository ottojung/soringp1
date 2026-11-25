#!/usr/bin/env python3
"""Max m over Q = T - (d<c), T = A + {p,q} + B near-chain. a,b up to 6."""
from lean import tc, mdepth, fval, is_msat, count_le

def make_T(a,b):
    n=a+2+b; rows=[0]*n
    def add(i,j): rows[i]|=1<<j
    for i in range(a-1): add(i,i+1)
    for i in range(a): add(i,a); add(i,a+1)
    for j in range(b): add(a,a+2+j); add(a+1,a+2+j)
    for j in range(b-1): add(a+2+j,a+3+j)
    return tc(tuple(rows),n),n

def remove_rel(rows,d,c):
    r=list(rows); r[d]&=~(1<<c); return tc(tuple(r),len(rows))

def main():
    maxm=0; arg=None; msat4=0
    for a in range(0,7):
        for b in range(0,7):
            t,n=make_T(a,b)
            rel=[(i,j) for i in range(n) for j in range(n) if t[i]&(1<<j)]
            for d,c in rel:
                q=remove_rel(t,d,c)
                if q==t: continue
                m=mdepth(q,n)
                if m>maxm: maxm=m; arg=(a,b,d,c,n,q)
                if m==4 and is_msat(q,n):
                    msat4+=1
                    print('MSAT4',a,b,d,c,fval(q,n),q)
    print('max m =',maxm,'arg=',arg[:5] if arg else None)
    print('msat4 count =',msat4)

if __name__=='__main__': main()
