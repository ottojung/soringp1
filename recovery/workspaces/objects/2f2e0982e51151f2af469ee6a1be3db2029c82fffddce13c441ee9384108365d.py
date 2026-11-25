#!/usr/bin/env python3
"""General shallow-child analysis: T = A + {p,q} + B (ordinal sum, p||q).
Enumerate A-size a, B-size b, remove one relation d<c from T -> Q.
Report all m=4 Q with f<2 (counterexamples) and the min f among m=4 msat Q."""
from lean import tc, incpairs, count_le, mdepth, fval, is_msat

def make_T(a,b):
    # elements: A=0..a-1 chain, p=a, q=a+1, B=a+2..a+b+1 chain
    n=a+2+b; rows=[0]*n
    def add(i,j): rows[i]|=1<<j
    for i in range(a-1): add(i,i+1)              # A chain
    for i in range(a):                            # A < p,q
        add(i,a); add(i,a+1)
    for j in range(b):                            # p,q < B
        add(a,a+2+j); add(a+1,a+2+j)
    for j in range(b-1): add(a+2+j,a+3+j)        # B chain
    return tc(tuple(rows),n),n

def remove_rel(rows,n,d,c):
    r=list(rows); r[d]&=~(1<<c); return tc(tuple(r),n)

def main():
    hits=[]; minf=99
    for a in range(0,5):
        for b in range(0,5):
            t,n=make_T(a,b)
            rel=[(i,j) for i in range(n) for j in range(n) if t[i]&(1<<j)]
            for d,c in rel:
                q=remove_rel(n and t,n,d,c)
                if q==t: continue
                m=mdepth(q,n)
                if m==4:
                    mm,f=fval(q,n); ms=is_msat(q,n); e=count_le(q,n,cap=16)
                    if ms: minf=min(minf,f)
                    if f<2:
                        hits.append((a,b,d,c,f,e,ms,incpairs(q,n),q))
    print('counterexamples (m=4, msat, f<2):')
    for h in hits: print('  ',h)
    print('count=',len(hits),' min f among m=4 msat Q from T-construction=',minf)

if __name__=='__main__': main()
