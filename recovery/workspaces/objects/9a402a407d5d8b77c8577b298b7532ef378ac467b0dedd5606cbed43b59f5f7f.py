#!/usr/bin/env python3
"""For near-chain T and cover (d,c), Q_min=cl(covers minus (d,c)).
Check which have: m(Q)=4, m(Q^{d<c})=1, m(Q^{c<d})=3, msat, f<2."""
from lean import tc, mdepth, child, count_le, incpairs, fval, is_msat

def make_T(a,b):
    n=a+2+b; rows=[0]*n
    def add(i,j): rows[i]|=1<<j
    for i in range(a-1): add(i,i+1)
    for i in range(a): add(i,a); add(i,a+1)
    for j in range(b): add(a,a+2+j); add(a+1,a+2+j)
    for j in range(b-1): add(a+2+j,a+3+j)
    return tc(tuple(rows),n),n

def covers(rows,n):
    return [(i,j) for i in range(n) for j in range(n)
            if rows[i]&(1<<j) and not any((rows[i]&(1<<k)) and (rows[k]&(1<<j))
                                          for k in range(n) if k!=i and k!=j)]

def cl_covers(cov,n):
    rows=[0]*n
    for i,j in cov: rows[i]|=1<<j
    return tc(tuple(rows),n)

def main():
    found=[]
    for a in range(0,5):
        for b in range(0,5):
            t,n=make_T(a,b)
            cov=covers(t,n)
            for d,c in cov:
                q=cl_covers([x for x in cov if x!=(d,c)],n)
                if q==t: continue
                m=mdepth(q,n)
                if m!=4: continue
                if mdepth(child(q,n,d,c),n)!=1: continue
                if mdepth(child(q,n,c,d),n)!=3: continue
                mm,f=fval(q,n); ms=is_msat(q,n); e=count_le(q,n,cap=32)
                found.append((a,b,d,c,f,ms,e,incpairs(q,n),q))
    print('Q with m=4, m(Q^{d<c})=1, m(Q^{c<d})=3:',len(found))
    for x in found[:30]: print('  ',x)
    print('any with f<2 and msat:',any(x[4]<2 and x[5] for x in found))

if __name__=='__main__': main()
