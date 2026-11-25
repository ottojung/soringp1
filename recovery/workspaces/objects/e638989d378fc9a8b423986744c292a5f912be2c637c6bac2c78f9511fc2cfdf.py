#!/usr/bin/env python3
import itertools, time, sys
from functools import lru_cache

# ---------- poset bitmask utilities ----------
def transitive_closure(succ):
    n=len(succ)
    out=list(succ)
    changed=True
    while changed:
        changed=False
        for i in range(n):
            nb=out[i]
            add=0
            x=nb
            while x:
                lsb=x & -x
                j=(lsb.bit_length()-1)
                add |= out[j]
                x ^= lsb
            if add & ~nb:
                out[i]=nb|add
                changed=True
    return tuple(out)

def extend(succ, i, j):
    # add i<j
    n=len(succ)
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(n):
        if x == i or (succ[x] & (1 << i)):
            out[x] |= new_greater
    return tuple(out)

def incomparable_pairs(succ, n):
    res=[]
    for i in range(n):
        for j in range(i+1, n):
            if not (succ[i] >> j & 1) and not (succ[j] >> i & 1):
                res.append((i,j))
    return res

def is_total(succ,n):
    return len(incomparable_pairs(succ,n))==0

# ---------- isomorphism canonicalization ----------
def refine_colors(succ, n):
    color = [bin(succ[i]).count("1") for i in range(n)]
    while True:
        sig = []
        for i in range(n):
            down = tuple(sorted(color[j] for j in range(n) if (succ[i] >> j) & 1))
            up = tuple(sorted(color[j] for j in range(n) if (succ[j] >> i) & 1))
            sig.append((color[i], down, up))
        order = {v: k for k, v in enumerate(sorted(set(sig)))}
        comp = [order[v] for v in sig]
        if comp == color:
            return color
        color = comp

def _encode(succ, perm, n):
    new = [0]*n
    for a in range(n):
        bits = succ[perm[a]]
        m = 0
        bbits = bits
        while bbits:
            lsb=bbits & -bbits
            b_old=lsb.bit_length()-1
            # find where b_old went? perm maps new index -> old element, we need inverse
            bbits ^= lsb
        # easier loop over n small
    # simpler
    out=[0]*n
    for a in range(n):
        m=0
        sa=succ[perm[a]]
        for b in range(n):
            if (sa >> perm[b]) & 1:
                m |= 1<<b
        out[a]=m
    return tuple(out)

def make_refined_canon(n):
    cache = {}
    def canon(succ):
        if succ in cache:
            return cache[succ]
        color = refine_colors(succ, n)
        groups = {}
        for i, c in enumerate(color):
            groups.setdefault(c, []).append(i)
        gs = [groups[c] for c in sorted(groups)]
        best = None
        for combo in itertools.product(*(itertools.permutations(g) for g in gs)):
            perm = [x for p in combo for x in p]
            e = _encode(succ, perm, n)
            if best is None or e < best:
                best = e
        cache[succ] = best
        return best
    return canon

# ---------- linear extensions count e(P) ----------
def count_linear_extensions(succ, n):
    # count topological orders; DP over subsets represented by bitmask
    # downsets? number of linear extensions = sum_{v minimal in P\S} e(S union {v})
    # iterate by adding elements in allowed order (prefix closed downsets in some forms?) actually standard: f(mask)=number of ways to form order of elements in mask given complement already placed? better: f(S)=ways to order set S as prefix: f(empty)=1, f(S)=sum_{x in S, predecessors(x) subset S} f(S\{x}).
    allmask=(1<<n)-1
    # precompute preds mask: elements that must come before i
    preds=[0]*n
    for i in range(n):
        m=0
        for j in range(n):
            if (succ[j] >> i) & 1:
                m |= 1<<j
        preds[i]=m
    dp=[0]*(1<<n)
    dp[0]=1
    for mask in range(1<<n):
        v=dp[mask]
        if v==0: continue
        # can append any x not in mask with preds[x] subset mask
        avail = allmask ^ mask
        xbits=avail
        while xbits:
            lsb=xbits & -xbits
            x=lsb.bit_length()-1
            if (preds[x] & ~mask)==0:
                dp[mask|lsb]+=v
            xbits ^= lsb
    return dp[allmask]

# ---------- minimax m(P): poset-state memo ----------
def m_poset_state(succ, n=None):
    if n is None: n=len(succ)
    memo={}
    def solve(s):
        if s in memo: return memo[s]
        ps=incomparable_pairs(s,n)
        if not ps:
            memo[s]=0; return 0
        best=None
        for i,j in ps:
            v=1+max(solve(extend(s,i,j)), solve(extend(s,j,i)))
            if best is None or v<best: best=v
            if best==1: break # can't be 0
        memo[s]=best; return best
    return solve(succ)

# ---------- minimax m(P): extension-set solver ----------
def all_linear_extensions_list(succ,n):
    preds=[0]*n
    for i in range(n):
        m=0
        for j in range(n):
            if (succ[j]>>i)&1: m|=1<<j
        preds[i]=m
    allmask=(1<<n)-1
    res=[]
    order=[0]*n
    def dfs(mask, depth):
        if mask==allmask:
            res.append(tuple(order))
            return
        avail=allmask^mask
        xbits=avail
        while xbits:
            lsb=xbits & -xbits
            x=lsb.bit_length()-1
            if (preds[x] & ~mask)==0:
                order[depth]=x
                dfs(mask|lsb, depth+1)
            xbits ^= lsb
    dfs(0,0)
    return res

def m_extension_set(succ,n=None):
    if n is None: n=len(succ)
    exts = all_linear_extensions_list(succ,n)
    # represent set by indices
    idxs = tuple(range(len(exts)))
    # precompute for each pair (i,j) which extensions have i before j
    pair = {}
    for i in range(n):
        for j in range(i+1,n):
            s_ij=[]; s_ji=[]
            for k,ext in enumerate(exts):
                pos=[0]*n
                for p,x in enumerate(ext): pos[x]=p
                if pos[i]<pos[j]: s_ij.append(k)
                else: s_ji.append(k)
            pair[(i,j)]=(frozenset(s_ij), frozenset(s_ji))
    memo={}
    def solve(sset):
        if len(sset)<=1:
            return 0
        key=frozenset(sset)
        if key in memo: return memo[key]
        # find incomparable pairs relative to this set? any pair that splits
        best=None
        for (i,j),(a,b) in pair.items():
            s1 = [x for x in sset if x in a]
            s2 = [x for x in sset if x in b]
            if not s1 or not s2: continue
            v=1+max(solve(tuple(s1)), solve(tuple(s2)))
            if best is None or v<best: best=v
            if best==1: break
        if best is None: best=0
        memo[key]=best
        return best
    return solve(idxs)

# ---------- enumeration of all poset classes ----------
A000112 = {0:1,1:1,2:2,3:5,4:16,5:63,6:318,7:2045,8:16999,9:183231}

def enumerate_all_classes(n):
    canon = make_refined_canon(n)
    vals = {}
    def dfs(s):
        c=canon(s)
        if c in vals: return
        vals[c]=s # store rep (itself canonical)
        ps=incomparable_pairs(c,n)
        for i,j in ps:
            dfs(extend(c,i,j))
            dfs(extend(c,j,i))
    dfs((0,)*n)
    return list(vals.keys())

# ---------- Fibonacci and fences ----------
def fib_upto(k):
    # F_1=1,F_2=1,...
    F=[0,1,1]
    while len(F)<=k:
        F.append(F[-1]+F[-2])
    return F

def fence_W(m):
    # standard fence on m elements 1..m: 1<2, 3<2, 3<4, 5<4,...
    # return succ bitmask tuple on elements 0..m-1
    succ=[0]*m
    for i in range(m-1): # relation between i,i+1 (0-based)
        a=i; b=i+1
        if i%2==0:
            # a < b
            succ[a]|=1<<b
        else:
            # b < a
            succ[b]|=1<<a
    return transitive_closure(tuple(succ))

def main():
    max_n=int(sys.argv[1]) if len(sys.argv)>1 else 7
    t0=time.time()
    F=fib_upto(max_n+10)
    print('Fibs F_1..:', F[1:15])

    # verify reduction note
    print('\nReduction check (algebraic): T(r)<=F_{r+3}-1 means e(P)<=F_{r+3}-1 => m(P)<=r.')
    print('Contrapositive with m=m(P): m>=r+1 => e(P)>=F_{r+3}. Set r=m-1 (m>=2): e(P)>=F_{m+2}. m<=1 trivial. So equivalent.')

    # fence checks
    print('\nFence-family check:')
    for m in range(1, max_n+2):
        w=fence_W(m)
        e=count_linear_extensions(w,m)
        mp=m_poset_state(w,m)
        target=F[m+2] if m+2 < len(F) else None
        print(f'  W_{m}: n={m}, e={e}, m(P)={mp}, F_{{m+2}}={target}, equality={e==target}')

    # cross-check solvers on small n
    print('\nCross-check poset-state vs extension-set m(P):')
    mism=0; checked=0
    for n in range(0, min(max_n,6)+1):
        classes=enumerate_all_classes(n)
        for c in classes:
            m1=m_poset_state(c,n)
            m2=m_extension_set(c,n)
            checked+=1
            if m1!=m2:
                mism+=1
                print('MISMATCH',n,c,m1,m2)
    print(f'  checked {checked} classes (n<= {min(max_n,6)}), mismatches={mism}')

    # main enumeration and inequality test
    print('\nMain inequality test: e(P) >= F_{m(P)+2} ?')
    total=0; viol=[]; tight_examples=[]
    min_slack=None
    by_n={}
    for n in range(0, max_n+1):
        t=time.time()
        classes=enumerate_all_classes(n)
        if A000112.get(n) is not None and len(classes)!=A000112[n]:
            print(f'WARNING n={n}: got {len(classes)} classes, A000112={A000112[n]}')
        else:
            print(f'n={n}: {len(classes)} classes in {time.time()-t:.3f}s', flush=True)
        nv=0
        for c in classes:
            e=count_linear_extensions(c,n)
            mp=m_poset_state(c,n)
            bound=F[mp+2]
            slack=e-bound
            total+=1
            rec=(n,e,mp,bound,slack,c)
            if slack<0:
                viol.append(rec); nv+=1
            if slack==0:
                tight_examples.append(rec)
            if min_slack is None or slack<min_slack: min_slack=slack
        by_n[n]=(len(classes),nv)
    print(f'\nTotal posets checked: {total} (n<= {max_n})')
    print(f'Violations: {len(viol)}')
    if viol:
        for r in viol[:20]:
            n,e,mp,bound,slack,c=r
            print(f'  VIOL n={n} e={e} m={mp} F_m+2={bound} slack={slack} rep={c}')
    print(f'Min slack over all: {min_slack}')
    print(f'Tight (slack==0) count: {len(tight_examples)}')
    # show some tight by (n,m)
    tight_examples.sort(key=lambda r:(r[0],r[2],r[1]))
    print('Sample tight cases (n,e,m,F):')
    seen=set()
    for r in tight_examples:
        n,e,mp,bound,slack,c=r
        key=(n,mp,e)
        if key in seen: continue
        seen.add(key)
        print(f'  n={n} e={e} m={mp} F={bound} rep={c}')
        if len(seen)>=40: break

    print('\nPer-n summary (classes, violations):')
    for n in sorted(by_n):
        print(f'  n={n}: {by_n[n][0]} classes, {by_n[n][1]} violations')
    print(f'Done in {time.time()-t0:.3f}s')

if __name__=='__main__':
    main()
