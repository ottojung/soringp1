#!/usr/bin/env python3
import random, sys
from solve3 import add_relation, incomparable_pairs, is_total, m_poset, all_labelled_posets
from functools import lru_cache

def gen_linear_extensions(n, succ):
    pred_mask = [0]*n
    for i in range(n):
        m = succ[i]
        while m:
            lb = m & -m
            j = lb.bit_length()-1
            m ^= lb
            pred_mask[j] |= (1 << i)
    res = []
    order = [-1]*n
    def bt(k, used_mask):
        if k == n:
            res.append(tuple(order))
            return
        avail = ((1<<n)-1) & ~used_mask
        m = avail
        while m:
            lb = m & -m
            v = lb.bit_length()-1
            m ^= lb
            if (pred_mask[v] & ~used_mask) == 0:
                order[k] = v
                bt(k+1, used_mask | lb)
    bt(0,0)
    return res

def ext_compare(exts,x,y):
    a=[]; b=[]
    for e in exts:
        px=py=-1
        for idx,val in enumerate(e):
            if val==x: px=idx
            elif val==y: py=idx
            if px!=-1 and py!=-1: break
        if px<py: a.append(e)
        else: b.append(e)
    return tuple(a), tuple(b)

@lru_cache(maxsize=None)
def m_ext(exts_key):
    exts=exts_key
    if len(exts)<=1: return 0
    n=len(exts[0])
    best=None
    for x in range(n):
        for y in range(x+1,n):
            a,b=ext_compare(exts,x,y)
            if not a or not b: continue
            v=1+max(m_ext(tuple(sorted(a))), m_ext(tuple(sorted(b))))
            if best is None or v<best: best=v
    return best

def main():
    n=6
    posets=list(all_labelled_posets(n))
    print('labelled', len(posets))
    random.seed(0)
    # pick diverse sample: antichain, and some random across sizes
    sample=set()
    sample.add(tuple([0]*n))
    # total orders
    # random
    for _ in range(120):
        sample.add(random.choice(posets))
    # by number of relations
    by_r={}
    for s in posets:
        r=sum(x.bit_count() for x in s)
        by_r.setdefault(r,[]).append(s)
    for r,arr in by_r.items():
        sample.add(arr[0])
        if len(arr)>1: sample.add(arr[-1])
    targets=list(sample)
    print('sample', len(targets))
    for idx,s in enumerate(targets):
        m_ext.cache_clear()
        m_poset.cache_clear() # not necessary but fine
        mp=m_poset(n,s)
        exts=tuple(sorted(gen_linear_extensions(n,s)))
        me=m_ext(exts)
        if mp!=me:
            print('MISMATCH', s, mp, me, len(exts))
            sys.exit(2)
        if (idx+1)%20==0:
            print('checked', idx+1)
    print('OK all sample cross-checked:', len(targets))

if __name__=='__main__':
    main()
