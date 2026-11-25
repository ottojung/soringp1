#!/usr/bin/env python3
import sys, itertools, math, time
from functools import lru_cache
from collections import Counter, defaultdict

# --- poset primitives (successor bitmasks: succ[i] has bit j iff i<j, transitively closed) ---

def extend(succ, i, j):
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    bit_i = 1 << i
    for x in range(len(succ)):
        if x == i or (succ[x] & bit_i):
            out[x] |= new_greater
    return tuple(out)

def incomparable_pairs(succ, n):
    return [(i, j) for i in range(n) for j in range(i+1, n)
            if not (succ[i] >> j & 1) and not (succ[j] >> i & 1)]

def is_total(succ, n):
    return all((succ[i] >> j & 1) or (succ[j] >> i & 1)
               for i in range(n) for j in range(i+1, n))

def dual(succ, n):
    out = [0]*n
    for a in range(n):
        m = 0
        for b in range(n):
            if succ[b] >> a & 1:
                m |= 1 << b
        out[a] = m
    return tuple(out)

def disjoint_union(A, B):
    a = len(A)
    return tuple(A) + tuple(m << a for m in B)

# --- Solver 1: poset-state minimax with memoization ---

def F_poset_state(succ):
    n = len(succ)
    memo = {}
    def solve(s):
        if s in memo: return memo[s]
        ps = incomparable_pairs(s, n)
        if not ps:
            memo[s] = 0
            return 0
        best = None
        for i,j in ps:
            v = 1 + max(solve(extend(s,i,j)), solve(extend(s,j,i)))
            if best is None or v < best:
                best = v
                if best == 1: break
        memo[s] = best
        return best
    return solve(succ)

# --- Solver 2: extension-set minimax with memoization ---
# State = frozenset of permutation tuples (indices in order from bottom to top)
# Each permutation p means p[0]<p[1]<...<p[n-1]

def all_linear_extensions(succ):
    n = len(succ)
    # recursive generation
    preds_mask = [0]*n
    for i in range(n):
        for j in range(n):
            if succ[j] >> i & 1:
                preds_mask[i] |= 1 << j
    full = (1<<n)-1
    res = []
    def dfs(done, perm):
        if done == full:
            res.append(tuple(perm))
            return
        avail = full & ~done
        # minimal among avail: no predecessor in avail
        x = avail
        while x:
            lsb = x & -x
            i = (lsb.bit_length()-1)
            x ^= lsb
            if (preds_mask[i] & avail) == 0:
                dfs(done|lsb, perm+[i])
    dfs(0, [])
    return frozenset(res)

def F_extension_set(succ):
    n = len(succ)
    if n <= 1:
        return 0
    exts = all_linear_extensions(succ)
    # precompute index of each element in each extension? easier: position map
    # represent ext as tuple p where p[k]=element at rank k; need to answer i<j?
    # better store rank array per extension
    # but frozenset of tuples of ranks: rank[e] = position
    def to_ranks(p):
        r = [0]*n
        for k,e in enumerate(p):
            r[e]=k
        return tuple(r)
    ext_ranks = frozenset(to_ranks(p) for p in exts)
    memo = {}
    def solve(state):
        if state in memo: return memo[state]
        if len(state) <= 1:
            memo[state] = 0
            return 0
        # find an incomparable pair present (splits state)
        # collect pairs that actually split
        pairs = []
        for i in range(n):
            for j in range(i+1,n):
                # check if comparable in all? incomparable means both orders appear
                has_ij = has_ji = False
                for r in state:
                    if r[i] < r[j]: has_ij = True
                    else: has_ji = True
                    if has_ij and has_ji: break
                if has_ij and has_ji:
                    pairs.append((i,j))
        if not pairs:
            memo[state] = 0
            return 0
        best = None
        for i,j in pairs:
            s1 = frozenset(r for r in state if r[i] < r[j])
            s2 = state - s1
            v = 1 + max(solve(s1), solve(s2))
            if best is None or v < best:
                best = v
                if best == 1: break
        memo[state] = best
        return best
    return solve(ext_ranks)

if __name__ == '__main__':
    # quick self-test
    pass
