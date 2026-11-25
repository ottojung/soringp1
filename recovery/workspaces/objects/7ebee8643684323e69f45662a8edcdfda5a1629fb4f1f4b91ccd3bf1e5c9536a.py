#!/usr/bin/env python3
import itertools, time, sys
from functools import lru_cache

def extend(succ, i, j):
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(len(succ)):
        if x == i or (succ[x] & (1 << i)):
            out[x] |= new_greater
    return tuple(out)

def incomparable_pairs(succ, n):
    return [(i, j) for i in range(n) for j in range(i+1, n)
            if not (succ[i] >> j & 1) and not (succ[j] >> i & 1)]

def refine_colors(succ, n):
    color = [bin(succ[i]).count("1") for i in range(n)]
    while True:
        sig = []
        for i in range(n):
            down = tuple(sorted(color[j] for j in range(n) if succ[i] >> j & 1))
            up = tuple(sorted(color[j] for j in range(n) if succ[j] >> i & 1))
            sig.append((color[i], down, up))
        order = {v: k for k, v in enumerate(sorted(set(sig)))}
        comp = [order[v] for v in sig]
        if comp == color:
            return color
        color = comp

def _encode(succ, perm, n):
    new = []
    for a in range(n):
        bits = succ[perm[a]]
        m = 0
        for b in range(n):
            if bits >> perm[b] & 1:
                m |= 1 << b
        new.append(m)
    return tuple(new)

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

# S1 plain minimax (for spot checks)
def F_plain(succ):
    n = len(succ)
    memo = {}
    def solve(s):
        if s in memo: return memo[s]
        ps = incomparable_pairs(s, n)
        if not ps:
            memo[s]=0; return 0
        best = None
        for i,j in ps:
            v = 1 + max(solve(extend(s,i,j)), solve(extend(s,j,i)))
            if best is None or v < best: best = v
        memo[s]=best; return best
    return solve(succ)

# S2 iso-quotient
def quotient_classes(n):
    canon = make_refined_canon(n)
    vals = {}
    def solve(c):
        if c in vals: return vals[c]
        ps = incomparable_pairs(c, n)
        if not ps:
            vals[c]=0; return 0
        best = 1 + min(max(solve(canon(extend(c,i,j))), solve(canon(extend(c,j,i)))) for i,j in ps)
        vals[c]=best; return best
    solve(canon((0,)*n))
    return vals, canon

def disjoint_union(A,B):
    a = len(A)
    return tuple(list(A) + [m << a for m in B])

A000112 = {0:1,1:1,2:2,3:5,4:16,5:63,6:318,7:2045,8:16999}

def main():
    max_total = int(sys.argv[1]) if len(sys.argv)>1 else 7
    t0=time.time()
    classes_by_n={}; canon_by_n={}
    for n in range(max_total+1):
        t=time.time()
        vals, canon = quotient_classes(n)
        classes_by_n[n]=vals; canon_by_n[n]=canon
        print(f"n={n}: {len(vals)} classes (A000112={A000112.get(n,'?')}) in {time.time()-t:.3f}s", flush=True)
    # spot cross-check: a few reps per size up to 7
    import random; random.seed(0)
    mism=0; checked=0
    for n in range(min(max_total,7)+1):
        reps=list(classes_by_n[n].keys())
        sample = reps if n<=5 else random.sample(reps, min(40,len(reps)))
        for rep in sample:
            f1=F_plain(rep); f2=classes_by_n[n][rep]
            checked+=1
            if f1!=f2: mism+=1; print('MISMATCH rep',n,rep,f1,f2)
    print(f"Spot cross-check S1 vs S2: {checked} reps, mismatches={mism}", flush=True)

    margins=[]; min_defect=None; witnesses=[]; total_pairs=0
    s1_checks=0; s1_mism=0
    for s in range(3, max_total+1):
        for a in range(1,s):
            b=s-a
            if a>b: continue
            repsA=list(classes_by_n[a].keys()); repsB=list(classes_by_n[b].keys())
            for A in repsA:
                fA=classes_by_n[a][A]
                for B in repsB:
                    fB=classes_by_n[b][B]
                    P=disjoint_union(A,B)
                    cP=canon_by_n[s](P)
                    fAB=classes_by_n[s][cP]
                    # S1 spot check: deterministic sample
                    if (total_pairs % 997 == 0):
                        f1=F_plain(P); s1_checks+=1
                        if f1!=fAB: s1_mism+=1; print('PAIR MISMATCH',a,b,f1,fAB)
                    defect=fAB-fA-fB
                    bound=min(a,b)+1
                    margin=defect-bound
                    rec=(margin,defect,bound,a,b,fA,fB,fAB,A,B)
                    margins.append(rec); total_pairs+=1
                    if min_defect is None or defect<min_defect:
                        min_defect=defect; witnesses=[rec]
                    elif defect==min_defect:
                        witnesses.append(rec)
    print(f"Pairs: {total_pairs}, S1 pair spot-checks: {s1_checks}, mismatches: {s1_mism}", flush=True)
    print(f"Minimum defect delta: {min_defect}", flush=True)
    violations=[r for r in margins if r[0]<0]
    tight=[r for r in margins if r[0]==0]
    print(f"Violations: {len(violations)}", flush=True)
    print(f"Tight (margin==0): {len(tight)}", flush=True)
    if violations:
        violations.sort(key=lambda r:(r[3]+r[4],r[0],r[1]))
        for r in violations[:20]:
            margin,defect,bound,a,b,fA,fB,fAB,A,B=r
            print(f"  VIOL |A|={a}|B|={b} F(A)={fA} F(B)={fB} F(A+B)={fAB} delta={defect} bound={bound} margin={margin}")
            print(f"    A={A}"); print(f"    B={B}")
    uniq={}
    for r in witnesses:
        key=(r[3],r[4],r[5],r[6],r[7],r[1],r[2]); uniq.setdefault(key,r)
    print(f"Min-defect witness types: {len(uniq)}", flush=True)
    for r in list(uniq.values())[:30]:
        margin,defect,bound,a,b,fA,fB,fAB,A,B=r
        print(f"  WIT |A|={a}|B|={b} F(A)={fA} F(B)={fB} F(A+B)={fAB} delta={defect} bound={bound} margin={margin}")
        print(f"    A={A}"); print(f"    B={B}")
    from collections import Counter
    by_margin=Counter(r[0] for r in margins)
    print("Margin distribution:", flush=True)
    for m in sorted(by_margin): print(f"  {m}: {by_margin[m]}")
    by_s={}
    for r in margins: by_s.setdefault(r[3]+r[4],[]).append(r[1])
    print("Min defect per total size:", flush=True)
    for s in sorted(by_s): print(f"  n={s}: min={min(by_s[s])} max={max(by_s[s])}")
    # also report min margin per (a,b)
    by_ab={}
    for r in margins:
        ab=(r[3],r[4]); by_ab.setdefault(ab,[]).append(r)
    print("Min margin/defect per split (a,b):", flush=True)
    for ab in sorted(by_ab):
        rs=by_ab[ab]; md=min(x[1] for x in rs); mm=min(x[0] for x in rs)
        print(f"  {ab}: pairs={len(rs)} min_delta={md} min_margin={mm}")
    print(f"Done in {time.time()-t0:.3f}s", flush=True)

if __name__=='__main__': main()
