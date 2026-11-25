#!/usr/bin/env python3
import sys, itertools, time

def closure(rel, n):
    less = [[False]*n for _ in range(n)]
    for (a,b) in rel:
        less[a][b] = True
    for k in range(n):
        for i in range(n):
            if less[i][k]:
                lk = less[k]
                row = less[i]
                for j in range(n):
                    if lk[j]:
                        row[j] = True
    out = set()
    for i in range(n):
        for j in range(n):
            if less[i][j]:
                out.add((i,j))
    return frozenset(out)

def total_pairs(n):
    return n*(n-1)//2

def is_total(rel, n):
    return len(rel) == total_pairs(n)

def incomparable_pairs(rel, n):
    res = []
    for a in range(n):
        for b in range(a+1, n):
            if (a,b) not in rel and (b,a) not in rel:
                res.append((a,b))
    return res

def refine_colors(n, relset):
    less = [[False]*n for _ in range(n)]
    for (a,b) in relset:
        less[a][b] = True
    # initial color by (down_count, up_count)
    color = []
    for i in range(n):
        dc = sum(1 for x in range(n) if less[x][i])
        uc = sum(1 for y in range(n) if less[i][y])
        color.append((dc, uc))
    # compress
    uniq = sorted(set(color))
    mp = {c:i for i,c in enumerate(uniq)}
    color = [mp[c] for c in color]
    while True:
        new = []
        for i in range(n):
            in_colors = sorted(color[x] for x in range(n) if less[x][i])
            out_colors = sorted(color[y] for y in range(n) if less[i][y])
            new.append((color[i], tuple(in_colors), tuple(out_colors)))
        uniq = sorted(set(new))
        mp = {c:i for i,c in enumerate(uniq)}
        new_int = [mp[c] for c in new]
        # check stability of partition
        stable = True
        for i in range(n):
            for j in range(n):
                if (new_int[i]==new_int[j]) != (color[i]==color[j]):
                    stable = False; break
            if not stable: break
        if stable:
            return new_int
        color = new_int

def canonical_key(n, relset):
    relset = set(relset)
    color = refine_colors(n, relset)
    # groups by color
    groups = {}
    for i in range(n):
        groups.setdefault(color[i], []).append(i)
    # sort groups by color int
    sorted_colors = sorted(groups.keys())
    cells = [groups[c] for c in sorted_colors]
    # block starts
    starts = []
    s = 0
    for cell in cells:
        starts.append(s)
        s += len(cell)
    # if all cells size 1, single perm
    total_perms = 1
    for cell in cells:
        total_perms *= len(cell)  # factorial? need factorial
    # compute factorial product
    import math
    total_perms = 1
    for cell in cells:
        total_perms *= math.factorial(len(cell))
    best = None
    # iterate product of permutations per cell
    cell_perms = [list(itertools.permutations(cell)) for cell in cells]
    for combo in itertools.product(*cell_perms):
        perm = [0]*n
        for ci, cp in enumerate(combo):
            st = starts[ci]
            for idx, v in enumerate(cp):
                perm[v] = st + idx
        key = tuple(sorted((perm[a], perm[b]) for (a,b) in relset))
        if best is None or key < best:
            best = key
    return best

# memo by canonical key
MEMO = {}

def m_depth(n, rel):
    # rel can be set/frozenset
    ck = canonical_key(n, set(rel))
    key = (n, ck)
    if key in MEMO:
        return MEMO[key]
    if len(ck) == total_pairs(n):
        MEMO[key] = 0
        return 0
    relset = set(ck)
    best = None
    for (a,b) in incomparable_pairs(relset, n):
        r1 = closure(relset | {(a,b)}, n)
        r2 = closure(relset | {(b,a)}, n)
        d1 = m_depth(n, r1)
        d2 = m_depth(n, r2)
        val = 1 + max(d1, d2)
        if best is None or val < best:
            best = val
    MEMO[key] = best
    return best

def has_lemmaA_split(n, rel):
    m = m_depth(n, rel)
    if m < 2:
        return True, m, None
    relset = set(rel)
    for (a,b) in incomparable_pairs(relset, n):
        r1 = closure(relset | {(a,b)}, n)
        r2 = closure(relset | {(b,a)}, n)
        d1 = m_depth(n, r1)
        d2 = m_depth(n, r2)
        if 1 + max(d1,d2) != m:
            continue
        if max(d1,d2) != m-1:
            continue
        if min(d1,d2) >= m-2:
            return True, m, ((a,b), d1, d2)
    return False, m, None

# recursive generator from gen.py
def downsets(parent_rel, n):
    res = []
    for mask in range(1<<n):
        S = set()
        for i in range(n):
            if mask & (1<<i):
                S.add(i)
        ok = True
        for x in S:
            for y in range(n):
                if (y,x) in parent_rel and y not in S:
                    ok = False; break
            if not ok: break
        if ok:
            res.append(frozenset(S))
    return res

def upsets(parent_rel, n):
    res = []
    for mask in range(1<<n):
        S = set()
        for i in range(n):
            if mask & (1<<i):
                S.add(i)
        ok = True
        for x in S:
            for y in range(n):
                if (x,y) in parent_rel and y not in S:
                    ok = False; break
            if not ok: break
        if ok:
            res.append(frozenset(S))
    return res

def gen_posets(n):
    if n <= 1:
        yield frozenset()
        return
    for parent in gen_posets(n-1):
        parent_rel = set(parent)
        ds = downsets(parent_rel, n-1)
        us = upsets(parent_rel, n-1)
        for L in ds:
            for U in us:
                if L & U:
                    continue
                good = True
                for d in L:
                    for u in U:
                        if (d,u) not in parent_rel:
                            good = False; break
                    if not good: break
                if not good:
                    continue
                newrel = set(parent_rel)
                v = n-1
                for d in L:
                    newrel.add((d,v))
                for u in U:
                    newrel.add((v,u))
                cl = closure(newrel, n)
                if set(cl) != set(newrel):
                    continue
                yield frozenset(newrel)

def main():
    maxn = int(sys.argv[1]) if len(sys.argv)>1 else 6
    for n in range(1, maxn+1):
        print(f"=== n={n} ===", flush=True)
        seen_canonical = set()
        count_classes = 0
        count_tested = 0
        counterexamples = []
        t0 = time.time()
        for rel in gen_posets(n):
            ck = canonical_key(n, rel)
            if ck in seen_canonical:
                continue
            seen_canonical.add(ck)
            count_classes += 1
            ok, m, info = has_lemmaA_split(n, rel)
            count_tested += 1
            if m is not None and m >= 2 and not ok:
                counterexamples.append((rel, m, info))
                print("COUNTEREXAMPLE:", sorted(rel), "m=", m, flush=True)
                if len(counterexamples) == 1:
                    with open('/home/lubko/soring301-exec-fibonacci-split-20261124/notes/counterexample.md','w') as f:
                        f.write(f"# Counterexample n={n}\n\nPoset comparabilities: {sorted(rel)}\n\nm={m}\ninfo={info}\n")
            if count_classes % 100 == 0:
                print(f"  progress classes={count_classes} time={time.time()-t0:.1f}", flush=True)
            # Expected number of unlabelled posets on n elements; stop early once all found.
            expected = {1:1,2:2,3:5,4:16,5:63,6:318,7:2045}
            if count_classes >= expected.get(n, 10**9):
                break
        print(f"classes={count_classes} tested={count_tested} counterexamples={len(counterexamples)} time={time.time()-t0:.1f}", flush=True)

if __name__ == '__main__':
    main()
