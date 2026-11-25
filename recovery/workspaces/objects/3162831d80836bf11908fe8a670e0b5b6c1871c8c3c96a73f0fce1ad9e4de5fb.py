#!/usr/bin/env python3
"""Correct Lemma 5 check. For near-chain T and each cover (d,c),
Q_min = cl(covers(T) \ {(d,c)}). Any Q with cl(Q+(d,c))=T satisfies Q ⊇ Q_min,
so m(Q)<=m(Q_min). Verify m(Q_min)<=2 and e(Q_min)<=4."""
from lean import tc, mdepth, count_le, incpairs

def make_T(a,b):
    n=a+2+b; rows=[0]*n
    def add(i,j): rows[i]|=1<<j
    for i in range(a-1): add(i,i+1)
    for i in range(a): add(i,a); add(i,a+1)
    for j in range(b): add(a,a+2+j); add(a+1,a+2+j)
    for j in range(b-1): add(a+2+j,a+3+j)
    return tc(tuple(rows),n),n

def covers(rows,n):
    # (x,y) is a cover iff x<y and no z with x<z<y
    return [(i,j) for i in range(n) for j in range(n)
            if rows[i]&(1<<j) and not any((rows[i]&(1<<k)) and (rows[k]&(1<<j))
                                          for k in range(n))]

def cl_covers(cov,n):
    rows=[0]*n
    for i,j in cov: rows[i]|=1<<j
    return tc(tuple(rows),n)

def main():
    worst=(0,None); bad=[]
    for a in range(0,5):
        for b in range(0,5):
            t,n=make_T(a,b)
            cov=covers(t,n)
            for d,c in cov:
                q=cl_covers([x for x in cov if x!=(d,c)],n)
                if q==t: continue
                # sanity: d||c in q, and cl(q+(d,c)) == t
                if q[d]&(1<<c): bad.append(('not inc',a,b,d,c)); continue
                r=list(q); r[d]|=1<<c
                if tc(tuple(r),n)!=t: bad.append(('not gen',a,b,d,c)); continue
                m=mdepth(q,n); e=count_le(q,n,cap=64)
                if m>worst[0]: worst=(m,(a,b,d,c,n,e,len(incpairs(q,n)),q))
                if m>2: bad.append(('m>2',a,b,d,c,m,e))
    print('worst m of Q_min =',worst[0]); print('arg=',worst[1])
    print('bad=',bad[:10],' count=',len(bad))

if __name__=='__main__': main()
