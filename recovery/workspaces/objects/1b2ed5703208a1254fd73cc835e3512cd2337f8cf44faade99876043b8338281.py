#!/usr/bin/env python3
"""Independent verifier: relation-set based, no bitmasks. Cross-checks m,f,msat."""
import sys, itertools

def closure(rel, n):
    less=[[False]*n for _ in range(n)]
    for a,b in rel: less[a][b]=True
    for k in range(n):
        for i in range(n):
            if less[i][k]:
                for j in range(n):
                    if less[k][j]: less[i][j]=True
    return frozenset((i,j) for i in range(n) for j in range(n) if less[i][j])

def incp(rel,n):
    return [(a,b) for a in range(n) for b in range(a+1,n)
            if (a,b) not in rel and (b,a) not in rel]

MEMO={}
def m(rel,n):
    key=(n,tuple(sorted(rel)))
    if key in MEMO: return MEMO[key]
    if len(rel)==n*(n-1)//2:
        MEMO[key]=0; return 0
    best=99
    for a,b in incp(rel,n):
        d1=m(closure(set(rel)|{(a,b)},n),n)
        d2=m(closure(set(rel)|{(b,a)},n),n)
        best=min(best,1+max(d1,d2))
    MEMO[key]=best; return best

def rows_to_rel(rows,n):
    return frozenset((i,j) for i in range(n) for j in range(n) if rows[i]&(1<<j))

def report(rows,n):
    rel=rows_to_rel(rows,n)
    assert closure(rel,n)==rel, 'not transitive!'
    mm=m(rel,n)
    pairs=[]
    for a,b in incp(rel,n):
        d1=m(closure(set(rel)|{(a,b)},n),n)
        d2=m(closure(set(rel)|{(b,a)},n),n)
        pairs.append(((a,b),d1,d2))
    f=max(min(x[1],x[2]) for x in pairs) if pairs else None
    msat=all(d1<=mm-1 and d2<=mm-1 for _,d1,d2 in pairs)
    print(f'n={n} m={mm} f={f} msat={msat} npairs={len(pairs)}')
    for p in pairs: print('   ',p)
    print('   strong_ok=', any(1+max(d1,d2)==mm and min(d1,d2)>=mm-2 for _,d1,d2 in pairs))
    print('   weak_ok=', any(min(d1,d2)>=mm-2 for _,d1,d2 in pairs))

if __name__=='__main__':
    n=int(sys.argv[1])
    rows=tuple(int(x) for x in sys.argv[2:])
    report(rows,n)
