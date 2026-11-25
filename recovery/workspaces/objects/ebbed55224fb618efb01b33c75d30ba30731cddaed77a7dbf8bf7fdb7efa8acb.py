#!/usr/bin/env python3
import itertools
import sys
import time
from functools import lru_cache

def closure(n, succ_bits):
    s = list(succ_bits)
    changed = True
    while changed:
        changed = False
        for i in range(n):
            gi = s[i]
            m = gi
            while m:
                lb = m & -m
                j = lb.bit_length() - 1
                m ^= lb
                nj = s[i] | s[j]
                if nj != s[i]:
                    s[i] = nj
                    changed = True
    return tuple(s)

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
    best = None
    for i,j in incomparable_pairs(n, succ):
        v = 1 + max(m_poset(n, add_relation(n,succ,i,j)), m_poset(n, add_relation(n,succ,j,i)))
        if best is None or v < best:
            best = v
    return best

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

def ext_compare(exts, x, y):
    a = []
    b = []
    for e in exts:
        px = py = -1
        for idx,val in enumerate(e):
            if val == x: px = idx
            elif val == y: py = idx
            if px!=-1 and py!=-1: break
        if px < py:
            a.append(e)
        else:
            b.append(e)
    return tuple(a), tuple(b)

@lru_cache(maxsize=None)
def m_ext(exts_key):
    exts = exts_key
    if len(exts) <= 1:
        return 0
    n = len(exts[0])
    best = None
    for x in range(n):
        for y in range(x+1,n):
            a,b = ext_compare(exts,x,y)
            if not a or not b:
                continue
            ka = tuple(sorted(a)); kb = tuple(sorted(b))
            v = 1 + max(m_ext(ka), m_ext(kb))
            if best is None or v < best:
                best = v
    return best

def canonical(n, succ):
    best = None
    elems = list(range(n))
    for perm in itertools.permutations(elems):
        inv = [0]*n
        for new, old in enumerate(perm):
            inv[old] = new
        s2 = [0]*n
        for old_i in range(n):
            ni = inv[old_i]
            m = succ[old_i]
            bits = 0
            while m:
                lb = m & -m
                old_j = lb.bit_length()-1
                m ^= lb
                bits |= (1 << inv[old_j])
            s2[ni] = bits
        t = tuple(s2)
        if best is None or t < best:
            best = t
    return best

def all_unlabelled_posets(n):
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
    reps = {}
    for s in seen:
        c = canonical(n,s)
        reps[c] = s
    return list(reps.keys())

def profile_condition(n, succ, mval):
    for i,j in incomparable_pairs(n,succ):
        c1 = add_relation(n,succ,i,j)
        c2 = add_relation(n,succ,j,i)
        m1 = m_poset(n,c1)
        m2 = m_poset(n,c2)
        if 1 + max(m1,m2) == mval and min(m1,m2) >= mval-2:
            return True
    return False

def cross_check(n, posets, mode='all', sample=50):
    # mode: all, sample, none
    if mode == 'none':
        print(f"  cross-check: skipped")
        return True
    targets = posets if mode=='all' else posets[:sample]
    for idx,s in enumerate(targets):
        m_ext.cache_clear()
        mp = m_poset(n,s)
        exts = tuple(sorted(gen_linear_extensions(n,s)))
        me = m_ext(exts)
        if mp != me:
            print(f"MISMATCH n={n} poset={s} m_poset={mp} m_ext={me} e={len(exts)}")
            return False
    print(f"  cross-check OK (poset-state vs extension-set) on {len(targets)} posets ({mode})")
    return True

def main():
    max_n = int(sys.argv[1]) if len(sys.argv)>1 else 7
    cross_mode = sys.argv[2] if len(sys.argv)>2 else 'auto'
    for n in range(1, max_n+1):
        t0=time.time()
        m_poset.cache_clear()
        posets = all_unlabelled_posets(n)
        print(f"n={n}: unlabelled posets = {len(posets)} (enum {time.time()-t0:.2f}s)")
        # cross-check
        if cross_mode=='all':
            cm='all'
        elif cross_mode=='none':
            cm='none'
        else:
            cm = 'all' if n<=5 else ('sample' if n==6 else 'none')
        if not cross_check(n,posets,cm, sample=60):
            sys.exit(2)
        # profile
        total_ge2 = satisfy = 0
        counterexamples = []
        min_other_over_opt = None
        worst_gap = None # m(P)-1-min_other on best profile move among optimal moves
        for s in posets:
            mp = m_poset(n,s)
            if mp >= 2:
                total_ge2 += 1
                if profile_condition(n,s,mp):
                    satisfy += 1
                else:
                    # collect details
                    det=[]
                    for i,j in incomparable_pairs(n,s):
                        c1=add_relation(n,s,i,j); c2=add_relation(n,s,j,i)
                        m1=m_poset(n,c1); m2=m_poset(n,c2)
                        det.append((i,j,m1,m2,1+max(m1,m2)==mp))
                    counterexamples.append((s,mp,det))
        print(f"  m(P)>=2: {total_ge2}, satisfy profile (other>=m-2): {satisfy}, counterexamples: {len(counterexamples)}")
        for s, mp, details in counterexamples[:10]:
            print(f"  COUNTEREXAMPLE n={n} m(P)={mp} succ={s}")
            for (i,j,m1,m2,is_opt) in details:
                print(f"    pair ({i},{j}): children {m1},{m2} opt={is_opt}")
        sys.stdout.flush()

if __name__=='__main__':
    main()
