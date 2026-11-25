"""Fresh independent verifier for T(5) claims.
Poset given by predecessor bitmask list pred[i] = {j : j < i}.
"""
from functools import lru_cache
import sys
sys.setrecursionlimit(100000)

def closure_pred(pred):
    n=len(pred)
    reach=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if pred[i]>>j & 1: reach[i][j]=True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    if reach[k][j]: reach[i][j]=True
    out=[]
    for i in range(n):
        mask=0
        for j in range(n):
            if reach[i][j]: mask|=1<<j
        out.append(mask)
    return tuple(out)

def count_ext(pred):
    n=len(pred); full=(1<<n)-1
    @lru_cache(None)
    def f(done):
        if done==full: return 1
        s=0
        for x in range(n):
            if not (done>>x)&1 and pred[x]&~done==0:
                s+=f(done|1<<x)
        return s
    return f(0)

def succ_from_pred(pred):
    n=len(pred); succ=[0]*n
    for i in range(n):
        for j in range(n):
            if pred[i]>>j & 1: succ[j]|=1<<i
    return tuple(succ)

def add_less(succ,i,j):
    n=len(succ)
    s=list(succ)
    dj=succ[j] | (1<<j)              # j and everything above it
    s[i] |= dj                       # i < j and above
    for x in range(n):               # everything below i (or i) also < dj
        if x==i or (succ[x]>>i)&1:
            s[x] |= dj
    return tuple(s)

def minimax_succ(succ):
    n=len(succ)
    @lru_cache(None)
    def f(S):
        inc=[(i,j) for i in range(n) for j in range(i+1,n)
             if not (S[i]>>j)&1 and not (S[j]>>i)&1]
        if not inc: return 0
        best=10**9
        for i,j in inc:
            v=1+max(f(add_less(S,i,j)), f(add_less(S,j,i)))
            if v<best: best=v
        return best
    return f(succ)

def ext_list(pred):
    n=len(pred); out=[]
    def go(done,w):
        if done==(1<<n)-1: out.append(tuple(w)); return
        for x in range(n):
            if not (done>>x)&1 and pred[x]&~done==0:
                go(done|1<<x,w+[x])
    go(0,[]); return out

def minimax_subsets(pred):
    ex=ext_list(pred); e=len(ex); full=(1<<e)-1
    n=len(pred); masks=set()
    for i in range(n):
        for j in range(i+1,n):
            m=0
            for r,w in enumerate(ex):
                if w.index(i)<w.index(j): m|=1<<r
            if m and m!=full: masks.add(m)
    masks=list(masks)
    @lru_cache(None)
    def g(S):
        if S & (S-1)==0: return 0
        best=10**9
        for a in masks:
            x=S&a; y=S&~a
            if x and y:
                v=1+max(g(x),g(y))
                if v<best: best=v
        return best
    return g(full), e, len(masks)

def show(name,pred):
    pred=closure_pred(pred)
    succ=succ_from_pred(pred)
    e=count_ext(pred)
    m1=minimax_succ(succ)
    m2,ee,nm=minimax_subsets(pred)
    assert e==ee
    print(f"{name}: n={len(pred)} e={e} m(poset-DP)={m1} m(subset-DP)={m2} splitmasks={nm}")
    return e,m1

W=[0,0,1,3,7,15,31]
show("W",W)

def merge_pred(a,b):
    p=[]
    for x in range(a+b):
        if x<a: p.append((1<<x)-1)
        else:   p.append(((1<<(x-a))-1)<<a)
    return p
show("Merge(2,6)",merge_pred(2,6))
show("Merge(2,5)",merge_pred(2,5))
show("Merge(2,4)",merge_pred(2,4))
show("Merge(3,5)",merge_pred(3,5))
show("chain7",[(1<<i)-1 for i in range(7)])
