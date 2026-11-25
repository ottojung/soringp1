#!/usr/bin/env python3
"""
R3 greedy adversary + greedy splitter bounds.
All counts exact via subset ideal-DP over 2048 subsets.
"""
from __future__ import annotations
import heapq
import math
import time

# Elements: 0-based indices
# 0: y
# 1,2,3: a1,a2,a3
# 4: x
# 5,6: b1,c1
# 7,8: b2,c2
# 9,10: b3,c3
NAMES = ['y','a1','a2','a3','x','b1','c1','b2','c2','b3','c3']
N = 11
ALL_MASK = (1 << N) - 1

def build_R3():
    # less[i] bitmask of j such that i < j? or preds/succs.
    # closure_succ[i]: bits j with i<j
    # closure_pred[j]: bits i with i<j
    succ = [0]*N
    pred = [0]*N
    def add(i,j):
        if not (succ[i] >> j) & 1:
            # add i<j
            pi = pred[i] | (1<<i)
            sj = succ[j] | (1<<j)
            # for all p in pi, s in sj: p<s
            # iterate bits
            x = pi
            while x:
                lsb = x & -x
                p = lsb.bit_length()-1
                x ^= lsb
                if (succ[p] & sj) != sj:
                    succ[p] |= sj
                # preds of s updated
            y = sj
            while y:
                lsb = y & -y
                s = lsb.bit_length()-1
                y ^= lsb
                if (pred[s] & pi) != pi:
                    pred[s] |= pi
    y,a1,a2,a3,x,b1,c1,b2,c2,b3,c3 = range(11)
    B = [x,b1,c1,b2,c2,b3,c3]
    for v in B:
        add(y,v)
    for i,(ai,bi,ci) in enumerate([(a1,b1,c1),(a2,b2,c2),(a3,b3,c3)]):
        add(ai,bi); add(ai,ci)
    return succ, pred

SUCC0, PRED0 = build_R3()

def verify_R3():
    y,a1,a2,a3,x,b1,c1,b2,c2,b3,c3 = range(11)
    assert (SUCC0[y]>>x)&1
    assert (SUCC0[a1]>>b1)&1 and (SUCC0[a1]>>c1)&1
    assert not (SUCC0[a1]>>x)&1
    assert not (SUCC0[a1]>>b2)&1
    assert not (SUCC0[b1]>>c1)&1 and not (SUCC0[c1]>>b1)&1
    minima = [i for i in range(N) if PRED0[i]==0]
    maxima = [i for i in range(N) if SUCC0[i]==0]
    assert set(minima)=={0,1,2,3}
    assert set(maxima)=={4,5,6,7,8,9,10}
    print('verify_R3 ok', flush=True)

# count extensions given closure by pred bitmasks: element v available if (pred[v] & mask)==pred[v]

_COUNT_CACHE = {}

def count_extensions(pred):
    k = pred if isinstance(pred, tuple) else tuple(pred)
    v = _COUNT_CACHE.get(k)
    if v is not None:
        return v
    dp = [0]*(1<<N)
    dp[0]=1
    for mask in range(1<<N):
        ways = dp[mask]
        if ways==0:
            continue
        rem = ALL_MASK ^ mask
        m = rem
        while m:
            lsb = m & -m
            vtx = lsb.bit_length()-1
            m ^= lsb
            if (k[vtx] & mask) == k[vtx]:
                dp[mask | lsb] += ways
    res = dp[ALL_MASK]
    _COUNT_CACHE[k]=res
    return res

def clear_count_cache():
    _COUNT_CACHE.clear()

def state_key(pred):
    return tuple(pred)

def incomparable_pairs_from_pred(pred, succ):
    pairs=[]
    for i in range(N):
        for j in range(i+1,N):
            if not ((succ[i]>>j)&1) and not ((succ[j]>>i)&1):
                pairs.append((i,j))
    return pairs

def add_comparison(pred, succ, i, j):
    # force i<j
    if (succ[j]>>i)&1:
        return None
    if (succ[i]>>j)&1:
        # already
        return pred, succ
    nsucc = list(succ)
    npred = list(pred)
    pi = npred[i] | (1<<i)
    sj = nsucc[j] | (1<<j)
    # check cycle
    if pi & sj:
        return None
    x = pi
    while x:
        lsb = x & -x
        p = lsb.bit_length()-1
        x ^= lsb
        nsucc[p] |= sj
    y = sj
    while y:
        lsb = y & -y
        s = lsb.bit_length()-1
        y ^= lsb
        npred[s] |= pi
    return tuple(npred), tuple(nsucc)

def pair_str(i,j):
    return f"{NAMES[i]}<{NAMES[j]}"

def balanced_split_pair(pred, succ):
    pairs = incomparable_pairs_from_pred(pred, succ)
    best = None
    # minimize max(e1,e2), then minimize min(e1,e2) large? tie-break deterministic
    for i,j in pairs:
        r1 = add_comparison(pred,succ,i,j)
        r2 = add_comparison(pred,succ,j,i)
        if r1 is None or r2 is None:
            continue
        e1 = count_extensions(r1[0])
        e2 = count_extensions(r2[0])
        key = (max(e1,e2), min(e1,e2), i, j)
        if best is None or key < best[0]:
            best = (key, (i,j), e1, e2)
    return best  # (key,pair,e1,e2)

def greedy_adversary_paths(base_pred, base_succ, splitter_policy='balanced'):
    # For each first pair p, simulate. At each state adversary answers side with larger e.
    # ties: record both, follow max -> explore both.
    # splitter_policy: how to choose next comparison after first? 'balanced' uses balanced split pair.
    results = {}
    inc0 = incomparable_pairs_from_pred(base_pred, base_succ)
    for idx, first in enumerate(inc0):
        # DFS over tie branches
        stack = []  # (pred,succ,depth,path)
        # apply first comparison choices
        i,j = first
        branches = []
        r1 = add_comparison(base_pred,base_succ,i,j)
        r2 = add_comparison(base_pred,base_succ,j,i)
        sides = []
        if r1 is not None:
            e1=count_extensions(r1[0]); sides.append((e1,r1,(i,j)))
        if r2 is not None:
            e2=count_extensions(r2[0]); sides.append((e2,r2,(j,i)))
        if not sides:
            continue
        maxe = max(s[0] for s in sides)
        for e_ans, state, ans in sides:
            if e_ans == maxe:
                stack.append((state[0],state[1],1,[(first,ans,e_ans)]))
        max_depth = 0
        max_path = None
        seen_local = 0
        while stack:
            pred,succ,depth,path = stack.pop()
            seen_local += 1
            e_cur = count_extensions(pred)
            if e_cur <= 1:
                if depth > max_depth:
                    max_depth = depth; max_path = path
                continue
            # choose next comparison
            bs = balanced_split_pair(pred,succ) if splitter_policy=='balanced' else None
            if bs is None:
                if depth > max_depth:
                    max_depth = depth; max_path = path
                continue
            _, (ci,cj), ce1, ce2 = bs
            # adversary answers
            r1 = add_comparison(pred,succ,ci,cj)
            r2 = add_comparison(pred,succ,cj,ci)
            sides=[]
            if r1 is not None:
                e1=count_extensions(r1[0]); sides.append((e1,r1,(ci,cj)))
            if r2 is not None:
                e2=count_extensions(r2[0]); sides.append((e2,r2,(cj,ci)))
            if not sides:
                if depth > max_depth:
                    max_depth = depth; max_path = path
                continue
            maxe = max(s[0] for s in sides)
            for e_ans,state,ans in sides:
                if e_ans == maxe:
                    stack.append((state[0],state[1],depth+1,path+[((ci,cj),ans,e_ans)]))
        results[first]=(max_depth,max_path,seen_local)
        if (idx+1)%10==0:
            print(f'  (a) done {idx+1}/{len(inc0)} first pairs', flush=True)
    return results

def greedy_balanced_split_tree(base_pred, base_succ, node_cap=200000):
    # Full tree: at each state pick pair minimizing max(e1,e2), recurse on BOTH sides.
    # memo by state_key -> depth (worst-case comparisons remaining?) or just compute tree depth.
    # We want total worst-case comparisons of this explicit strategy = max depth over leaves.
    sysset = {}
    nodes = 0
    cap_hit = False
    memo = {}

    from functools import lru_cache

    # recursion with explicit stack? recursion depth small (<=19) fine.
    def solve(pred,succ):
        nonlocal nodes, cap_hit
        k = state_key(pred)
        if k in memo:
            return memo[k]
        e = count_extensions(pred)
        if e <= 1:
            memo[k]=0
            return 0
        if nodes >= node_cap:
            cap_hit = True
            # optimistic lower bound 0? but we need upper bound certified; cap means unknown
            memo[k]=None
            return None
        nodes += 1
        bs = balanced_split_pair(pred,succ)
        if bs is None:
            memo[k]=0
            return 0
        _, (i,j), _, _ = bs
        r1 = add_comparison(pred,succ,i,j)
        r2 = add_comparison(pred,succ,j,i)
        d1 = solve(r1[0],r1[1]) if r1 else 0
        d2 = solve(r2[0],r2[1]) if r2 else 0
        if d1 is None or d2 is None:
            memo[k]=None
            return None
        res = 1 + max(d1,d2)
        memo[k]=res
        return res

    D = solve(base_pred, base_succ)
    return D, nodes, cap_hit, len(memo)

def main():
    t0=time.time()
    verify_R3()
    base_pred = tuple(PRED0)
    base_succ = tuple(SUCC0)
    e = count_extensions(base_pred)
    print('e(R3)=', e)
    print('C=ceil(log2 e)=', (e-1).bit_length())
    inc = incomparable_pairs_from_pred(base_pred, base_succ)
    print('initial incomparable pairs=', len(inc))
    print('pairs sample=', [f"{NAMES[i]},{NAMES[j]}" for i,j in inc[:10]])

    print('\n--- (a) greedy adversary (splitter uses balanced pairs after first) ---', flush=True)
    t1=time.time()
    a_res = greedy_adversary_paths(base_pred, base_succ, splitter_policy='balanced')
    best_d = -1; best_pairs=[]; best_path=None
    for p,(d,path,seen) in a_res.items():
        if d > best_d:
            best_d=d; best_pairs=[p]; best_path=path
        elif d==d and d==best_d:
            best_pairs.append(p)
    print('max depth over first pairs=', best_d)
    print('argmax first pairs=', [f"({NAMES[p[0]]},{NAMES[p[1]]})" for p in best_pairs[:10]], 'count', len(best_pairs))
    if best_path:
        print('witness path (pair_compared, answer_forced, e_after):')
        for step in best_path:
            (ci,cj), ans, ea = step
            print(' ', f"cmp({NAMES[ci]},{NAMES[cj]}) -> {NAMES[ans[0]]}<{NAMES[ans[1]]} e={ea}")
    print('(a) elapsed', time.time()-t1)

    print('\n--- (b) greedy balanced-split tree ---', flush=True)
    t2=time.time()
    D, nodes, cap_hit, memo_n = greedy_balanced_split_tree(base_pred, base_succ, node_cap=200000)
    print('D=', D, 'nodes_expanded=', nodes, 'cap_hit=', cap_hit, 'memo_states=', memo_n)
    print('(b) elapsed', time.time()-t2)

    print('\nTOTAL elapsed', time.time()-t0)

if __name__=='__main__':
    main()
