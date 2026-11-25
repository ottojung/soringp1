#!/usr/bin/env python3
"""Lean bounded oracle for the m=4 front. Scratch only; no canonical repo.

Poset = tuple of n bitmask rows, row[i] = bits of j with i<j (transitively closed).
m(P) exact by the recurrence, memo keyed by (n, rows) -- labeled, no canonical
form, so no factorial blowup. Used only on small n / small-e posets.
"""
import sys, itertools, time

# ---------- bitmask core ----------
def tc(rows, n):
    rows = list(rows)
    for k in range(n):
        bk = 1 << k
        rk = rows[k]
        for i in range(n):
            if rows[i] & bk:
                rows[i] |= rk
    return tuple(rows)

def child(rows, n, a, b):
    r = list(rows); r[a] |= (1 << b)
    return tc(tuple(r), n)

def incpairs(rows, n):
    out = []
    for i in range(n):
        ri = rows[i]
        for j in range(i+1, n):
            if not (ri & (1<<j)) and not (rows[j] & (1<<i)):
                out.append((i,j))
    return out

def npairs(rows, n):
    return sum(bin(r).count('1') for r in rows)

# ---------- linear extension count (capped) ----------
def count_le(rows, n, cap=None):
    # dp over down-sets (subsets S of placed elements). dp[S] = #ways.
    full = (1<<n) - 1
    dp = [0]*(full+1); dp[0] = 1
    for S in range(full+1):
        if not dp[S]: continue
        # element i can be placed next if all its predecessors are in S
        for i in range(n):
            if S & (1<<i): continue
            # preds of i: bits j with rows[j] has i
            ok = True
            for j in range(n):
                if (rows[j] & (1<<i)) and not (S & (1<<j)):
                    ok = False; break
            if ok:
                dp[S | (1<<i)] += dp[S]
                if cap and dp[S | (1<<i)] > cap:
                    return cap+1
    return dp[full]

# ---------- minimax ----------
MEMO = {}
def mdepth(rows, n):
    key = (n, rows)
    v = MEMO.get(key)
    if v is not None: return v
    if npairs(rows, n) == n*(n-1)//2:
        MEMO[key] = 0; return 0
    best = 99
    for (a,b) in incpairs(rows, n):
        d1 = mdepth(child(rows,n,a,b), n)
        d2 = mdepth(child(rows,n,b,a), n)
        val = 1 + max(d1,d2)
        if val < best: best = val
    MEMO[key] = best; return best

def pair_depths(rows, n):
    m = mdepth(rows, n)
    out = []
    for (a,b) in incpairs(rows, n):
        d1 = mdepth(child(rows,n,a,b), n)
        d2 = mdepth(child(rows,n,b,a), n)
        out.append(((a,b),d1,d2))
    return m, out

def fval(rows, n):
    m, pd = pair_depths(rows, n)
    if not pd: return m, None
    return m, max(min(d1,d2) for _,d1,d2 in pd)

def is_msat(rows, n):
    m = mdepth(rows, n)
    for (a,b) in incpairs(rows, n):
        d1 = mdepth(child(rows,n,a,b), n)
        d2 = mdepth(child(rows,n,b,a), n)
        if d1 > m-1 or d2 > m-1: return False
    return True

# ---------- generation: add a maximal element ----------
def downsets(rows, k):
    res = []
    for mask in range(1<<k):
        ok = True
        for x in range(k):
            if mask & (1<<x):
                for y in range(k):
                    if (rows[y] & (1<<x)) and not (mask & (1<<y)):
                        ok=False; break
                if not ok: break
        if ok: res.append(mask)
    return res

# cheap canonical form via brute-force min over perms, only for small n and
# only when cells are small (guard against blowup)
def canon(rows, n, maxperms=20000):
    # initial coloring by (downsize, upsetsize) then refine once
    col = []
    for i in range(n):
        dc = sum(1 for x in range(n) if rows[x] & (1<<i))
        uc = bin(rows[i]).count('1')
        col.append((dc,uc))
    uniq = sorted(set(col)); mp = {c:i for i,c in enumerate(uniq)}
    col = [mp[c] for c in col]
    # refine
    for _ in range(n):
        new = []
        for i in range(n):
            ic = tuple(sorted(col[x] for x in range(n) if rows[x]&(1<<i)))
            oc = tuple(sorted(col[y] for y in range(n) if rows[i]&(1<<y)))
            new.append((col[i],ic,oc))
        uniq = sorted(set(new)); mp = {c:i for i,c in enumerate(uniq)}
        ni = [mp[c] for c in new]
        if ni==col: break
        col = ni
    groups={}
    for i in range(n): groups.setdefault(col[i],[]).append(i)
    cells=[groups[c] for c in sorted(groups)]
    import math
    nperm=1
    for c in cells: nperm*=math.factorial(len(c))
    if nperm>maxperms:
        # fallback: use sorted (col, adjacency signature) as a *sound* but
        # incomplete key is unsafe; instead return rows (labeled) -> no dedup
        return ('L', rows)
    rel = tuple(sorted((i,j) for i in range(n) for j in range(n) if rows[i]&(1<<j)))
    best=None
    for combo in itertools.product(*[list(itertools.permutations(c)) for c in cells]):
        perm=[0]*n; s=0
        for ci,cp in enumerate(combo):
            for idx,v in enumerate(cp): perm[v]=s+idx
            s+=len(cp)
        key=tuple(sorted((perm[a],perm[b]) for a,b in rel))
        if best is None or key<best: best=key
    return ('C',best)

def gen_level(reps, n):
    k=n-1; seen=set(); out=[]
    v=k
    for prev in reps:
        for dm in downsets(prev,k):
            rows=list(prev)+[0]
            m=dm
            while m:
                b=m&-m; d=b.bit_length()-1; rows[d]|=(1<<v); m^=b
            rows=tc(tuple(rows),n)
            ck=canon(rows,n)
            if ck in seen: continue
            seen.add(ck); out.append(rows)
    return out

if __name__=='__main__':
    cmd = sys.argv[1] if len(sys.argv)>1 else 'verify'
    if cmd=='verify':
        # verify: e(P)=2  <=>  exactly one incomparable pair, for n<=6
        print('=== verify e=2 <=> one incomparable pair, n<=6 ===')
        reps=[(0,)]
        for n in range(1,7):
            if n>1: reps=gen_level(reps,n)
            bad=0; e2=0
            for rows in reps:
                e=count_le(rows,n,cap=3)
                ni=len(incpairs(rows,n))
                if e==2:
                    e2+=1
                    if ni!=1: bad+=1; print('  E2MULTI n=',n,rows,'ni=',ni)
                if ni==1 and e!=2:
                    bad+=1; print('  ONENI_E n=',n,rows,'e=',e)
            print(f'n={n} classes={len(reps)} e2={e2} bad={bad}')
        print('MEMO',len(MEMO))
