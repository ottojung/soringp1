#!/usr/bin/env python3
import sys, time
from functools import lru_cache

def add_relation(n, succ, i, j):
    s = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(n):
        if x == i or ((succ[x] >> i) & 1):
            s[x] |= new_greater
    return tuple(s)

def incomparable_pairs(n, succ):
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if not ((succ[i] >> j) & 1) and not ((succ[j] >> i) & 1):
                pairs.append((i,j))
    return pairs

def is_total(n, succ):
    c = 0
    for i in range(n):
        c += succ[i].bit_count()
    return c == n*(n-1)//2

@lru_cache(maxsize=None)
def m_poset(n, succ):
    if is_total(n, succ):
        return 0
    best = 10**9
    for i,j in incomparable_pairs(n, succ):
        v = 1 + max(m_poset(n, add_relation(n,succ,i,j)), m_poset(n, add_relation(n,succ,j,i)))
        if v < best:
            best = v
    return best

def all_labelled_posets(n):
    start = tuple([0]*n)
    seen = {start}
    stack = [start]
    while stack:
        s = stack.pop()
        for i,j in incomparable_pairs(n,s):
            for t in (add_relation(n,s,i,j), add_relation(n,s,j,i)):
                if t not in seen:
                    seen.add(t)
                    stack.append(t)
    return seen

def profile_ok(n,succ,mp):
    for i,j in incomparable_pairs(n,succ):
        c1 = add_relation(n,succ,i,j); c2 = add_relation(n,succ,j,i)
        m1 = m_poset(n,c1); m2 = m_poset(n,c2)
        if 1 + max(m1,m2) == mp and min(m1,m2) >= mp-2:
            return True
    return False

def main():
    max_n = int(sys.argv[1]) if len(sys.argv)>1 else 6
    for n in range(1,max_n+1):
        t0=time.time()
        m_poset.cache_clear()
        posets = all_labelled_posets(n)
        print(f"n={n}: labelled posets = {len(posets)} (gen {time.time()-t0:.2f}s)")
        sys.stdout.flush()
        t1=time.time()
        total_ge2 = sat = 0
        first_ce = None
        for s in posets:
            mp = m_poset(n,s)
            if mp >= 2:
                total_ge2 += 1
                if profile_ok(n,s,mp):
                    sat += 1
                elif first_ce is None:
                    det=[]
                    for i,j in incomparable_pairs(n,s):
                        c1=add_relation(n,s,i,j); c2=add_relation(n,s,j,i)
                        m1=m_poset(n,c1); m2=m_poset(n,c2)
                        det.append((i,j,m1,m2,1+max(m1,m2)==mp))
                    first_ce=(s,mp,det)
        print(f"  m(P)>=2: {total_ge2}, satisfy: {sat}, counterexamples: {total_ge2-sat} (check {time.time()-t1:.2f}s)")
        if first_ce:
            s,mp,det=first_ce
            print(f"  FIRST COUNTEREXAMPLE n={n} m(P)={mp} succ={s}")
            for d in det: print(f"    pair {d[0]}: depths {d[1]},{d[2]} opt={d[3]}")
        sys.stdout.flush()

if __name__=='__main__':
    main()
