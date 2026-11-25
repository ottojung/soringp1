#!/usr/bin/env python3
"""
Exact minimax F(P) for posets and disjoint-union defect study.

Two solvers cross-checked:
  (S1) memoized minimax DP on reachable poset states from P (labelled-state memo).
  (S2) iso-canonical minimax over reachable classes (same recurrence, states
       canonicalized by refined colour + lex-min relabelling) giving F for the
       class; F(P)=F_S2(canon(P)).

Enumeration: unlabelled posets = isomorphism classes via canonicalization over
all transitively-closed labelled posets reachable from antichains of each size
(quotient_classes). No external libraries.
"""
import itertools
import sys
import time
from functools import lru_cache

# ---------- poset basics ----------

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

def is_total(succ, n):
    return len(incomparable_pairs(succ, n)) == 0

# ---------- canon (from benchmark_symmetry_quotients) ----------

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

# ---------- S1: plain memoized minimax from given poset ----------

def F_plain(succ):
    n = len(succ)
    memo = {}
    def solve(s):
        if s in memo:
            return memo[s]
        ps = incomparable_pairs(s, n)
        if not ps:
            memo[s] = 0
            return 0
        best = None
        for i, j in ps:
            v = 1 + max(solve(extend(s, i, j)), solve(extend(s, j, i)))
            if best is None or v < best:
                best = v
        memo[s] = best
        return best
    return solve(succ), len(memo)

# ---------- S2: iso-quotient classes (all classes of size n) ----------

def quotient_classes(n):
    canon = make_refined_canon(n)
    vals = {}
    def solve(c):
        if c in vals:
            return vals[c]
        ps = incomparable_pairs(c, n)
        if not ps:
            vals[c] = 0
            return 0
        best = 1 + min(
            max(solve(canon(extend(c, i, j))), solve(canon(extend(c, j, i))))
            for i, j in ps
        )
        vals[c] = best
        return best
    solve(canon((0,) * n))
    return vals, canon

# ---------- disjoint union ----------

def disjoint_union(A, B):
    a = len(A)
    return tuple(list(A) + [m << a for m in B])

# ---------- main study ----------

A000112 = {0:1,1:1,2:2,3:5,4:16,5:63,6:318,7:2045,8:16999}

def main():
    max_total = 8
    if len(sys.argv) > 1:
        max_total = int(sys.argv[1])
    t0 = time.time()
    # compute classes and canons per size
    classes_by_n = {}
    canon_by_n = {}
    for n in range(0, max_total + 1):
        t = time.time()
        vals, canon = quotient_classes(n)
        classes_by_n[n] = vals
        canon_by_n[n] = canon
        print(f"n={n}: {len(vals)} classes (A000112={A000112.get(n,'?')}) in {time.time()-t:.3f}s", flush=True)

    # cross-check S1 vs S2 on class representatives (full up to 7, sample/skip heavy for 8+)
    print("Cross-checking S1 vs S2 on class representatives...", flush=True)
    mismatches = 0
    checked = 0
    for n in range(0, max_total + 1):
        vals = classes_by_n[n]
        reps = list(vals.keys())
        if n >= 8:
            # expensive to F_plain all; check every 200th + first 50 as sanity
            sample_idx = set(range(min(50, len(reps))))
            sample_idx.update(range(0, len(reps), 200))
            reps_to_check = [reps[i] for i in sorted(sample_idx)]
        else:
            reps_to_check = reps
        for rep in reps_to_check:
            f2 = vals[rep]
            f1, _ = F_plain(rep)
            checked += 1
            if f1 != f2:
                print(f"MISMATCH n={n} rep={rep} S1={f1} S2={f2}")
                mismatches += 1
    print(f"Cross-check: {checked} representatives checked, mismatches={mismatches}", flush=True)

    # study pairs
    print("\nDisjoint-union defect study:", flush=True)
    min_defect = None
    witnesses = []
    total_pairs = 0
    pair_mismatches = 0
    pair_s1_checked = 0
    margins = []
    for s in range(3, max_total + 1):
        for a in range(1, s):
            b = s - a
            if a > b:
                continue  # unordered by component sizes (union commutative up to iso)
            repsA = list(classes_by_n[a].keys())
            repsB = list(classes_by_n[b].keys())
            for A in repsA:
                fA2 = classes_by_n[a][A]
                for B in repsB:
                    fB2 = classes_by_n[b][B]
                    P = disjoint_union(A,B)
                    # S2: canonical class lookup
                    cP = canon_by_n[s](P)
                    fP2 = classes_by_n[s][cP]
                    # S1 cross-check on a sample (all for s<=7, sparse for s>=8)
                    do_s1 = (s <= 7) or (total_pairs % 500 == 0)
                    if do_s1:
                        fP1, _ = F_plain(P)
                        pair_s1_checked += 1
                        if fP1 != fP2:
                            pair_mismatches += 1
                            print(f"PAIR MISMATCH a={a},b={b} fP1={fP1} fP2={fP2}")
                    fAB = fP2
                    defect = fAB - fA2 - fB2
                    bound = min(a,b) + 1
                    margin = defect - bound
                    total_pairs += 1
                    rec = (margin, defect, bound, a, b, fA2, fB2, fAB, A, B)
                    margins.append(rec)
                    if min_defect is None or defect < min_defect:
                        min_defect = defect
                        witnesses = [rec]
                    elif defect == min_defect:
                        witnesses.append(rec)
    print(f"Pairs checked (a<=b, all class pairs): {total_pairs}", flush=True)
    print(f"Pair S1 cross-checks run: {pair_s1_checked}, mismatches: {pair_mismatches}", flush=True)
    print(f"Pairs checked (size-unordered a<=b, all class pairs): {total_pairs}", flush=True)
    print(f"Pair solver mismatches: {pair_mismatches}", flush=True)
    if min_defect is not None:
        print(f"Minimum defect delta=F(A+B)-F(A)-F(B): {min_defect}", flush=True)
    # summarize margins
    violations = [r for r in margins if r[0] < 0]
    tight = [r for r in margins if r[0] == 0]
    print(f"Violations (margin<0): {len(violations)}", flush=True)
    print(f"Tight (margin==0, defect==min(a,b)+1): {len(tight)}", flush=True)
    if violations:
        # smallest violation by total size then margin
        violations.sort(key=lambda r: (r[3]+r[4], r[0], r[1]))
        print("Smallest violations:", flush=True)
        for r in violations[:10]:
            margin, defect, bound, a,b,fA,fB,fAB,A,B = r
            print(f"  |A|={a},|B|={b}, F(A)={fA}, F(B)={fB}, F(A+B)={fAB}, delta={defect}, bound={bound}, margin={margin}")
    # report all min-defect witnesses (unique by values maybe many; limit)
    print(f"Min-defect witnesses count: {len(witnesses)}", flush=True)
    # group witnesses by (a,b,fA,fB,fAB)
    uniq = {}
    for r in witnesses:
        key = (r[3],r[4],r[5],r[6],r[7],r[1],r[2])
        if key not in uniq:
            uniq[key] = r
    print(f"Unique min-defect witness types (by sizes/values): {len(uniq)}", flush=True)
    for key, r in list(uniq.items())[:20]:
        margin, defect, bound, a,b,fA,fB,fAB,A,B = r
        print(f"  |A|={a},|B|={b}, F(A)={fA}, F(B)={fB}, F(A+B)={fAB}, delta={defect}, bound={bound}, margin={margin}")
        print(f"    A={A}")
        print(f"    B={B}")
    # distribution summary
    from collections import Counter
    by_margin = Counter(r[0] for r in margins)
    print("Margin distribution (margin = delta - (min(a,b)+1)):", flush=True)
    for m in sorted(by_margin):
        print(f"  margin {m}: {by_margin[m]}")
    # also min defect per total size
    by_s = {}
    for r in margins:
        s = r[3]+r[4]
        by_s.setdefault(s, []).append(r[1])
    print("Min defect per total size:", flush=True)
    for s in sorted(by_s):
        print(f"  n={s}: min_delta={min(by_s[s])}")
    print(f"Done in {time.time()-t0:.3f}s", flush=True)

if __name__ == '__main__':
    main()
