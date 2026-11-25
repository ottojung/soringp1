from functools import lru_cache
from itertools import combinations

def enum_posets(n, qmin, qmax):
    # Q[k] is bitmask of earlier vertices incomparable with k
    Q=[]
    def rec(k,q):
        if q>qmax: return
        if q + (n-k)*(n+k-1)//2 < qmin: return
        if k==n:
            if q<qmin: return
            # connectedness
            seen=1; todo=[0]
            while todo:
                i=todo.pop()
                for j in range(n):
                    if ((seen>>j)&1)==0 and ((Q[j]>>i)&1 or (Q[i]>>j)&1):
                        seen|=1<<j;todo.append(j)
            if seen==(1<<n)-1:
                yield tuple(Q),q
            return
        # exact column options valid for transitivity
        for S in range(1<<k):
            s=S.bit_count()
            if q+s>qmax: continue
            ok=True
            for i in range(k):
                if (S>>i)&1:
                    for j in range(i+1,k):
                        if not ((Q[j]>>i)&1) and not ((S>>j)&1):
                            ok=False;break
                    if not ok:break
            if ok:
                Q.append(S)
                yield from rec(k+1,q+s)
                Q.pop()
    yield from rec(0,0)

def extensions(Q,n,limit=13):
    # relation predecessor masks
    pred=[0]*n
    for j in range(n):
        for i in range(j):
            if not ((Q[j]>>i)&1): pred[j]|=1<<i
    full=(1<<n)-1
    out=[]
    def go(done,word):
        if len(out)>=limit:return
        if done==full:
            out.append(tuple(word));return
        for x in range(n):
            if not (done>>x)&1 and pred[x]&~done==0:
                go(done|1<<x,word+[x])
                if len(out)>=limit:return
    go(0,[])
    return out

def width(Q,n):
    # clique number of incomparability graph, brute subsets
    best=0
    for S in range(1,1<<n):
        c=S.bit_count()
        if c<=best:continue
        ok=True
        for i in range(n):
            if (S>>i)&1:
                for j in range(i+1,n):
                    if (S>>j)&1 and not ((Q[j]>>i)&1):
                        ok=False;break
                if not ok:break
        if ok:best=c
    return best

def exact_F(ext,n):
    m=len(ext); pair_masks=[]
    for i in range(n):
      for j in range(i+1,n):
        a=0
        for r,p in enumerate(ext):
          if p.index(i)<p.index(j): a|=1<<r
        if a and a != (1<<m)-1: pair_masks.append(a)
    full=(1<<m)-1
    @lru_cache(None)
    def F(S):
      if S&(S-1)==0:return 0
      best=99
      for a in pair_masks:
        x=S&a;y=S&~a
        if not x or not y:continue
        v=1+max(F(x),F(y))
        if v<best:best=v
        if best==1:return 1
      return best
    return F(full),F.cache_info().currsize
