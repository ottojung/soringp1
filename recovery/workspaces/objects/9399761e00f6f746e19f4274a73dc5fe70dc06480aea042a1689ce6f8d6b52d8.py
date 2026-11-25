#!/usr/bin/env python3
import sys, itertools, time

def closure(rel, n):
    less = [[False]*n for _ in range(n)]
    for (a,b) in rel:
        less[a][b] = True
    for k in range(n):
        for i in range(n):
            if less[i][k]:
                row = less[i]
                lk = less[k]
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

def canonical_key(n, rel):
    best = None
    elems = list(range(n))
    for perm in itertools.permutations(elems):
        newrel = []
        for (a,b) in rel:
            newrel.append((perm[a], perm[b]))
        newrel.sort()
        key = tuple(newrel)
        if best is None or key < best:
            best = key
    return best

# memo by canonical key
MEMO = {}

def m_depth(n, rel):
    ck = canonical_key(n, rel)
    if ck in MEMO:
        return MEMO[ck]
    if len(ck) == total_pairs(n):
        MEMO[ck] = 0
        return 0
    # reconstruct rel set from ck for operations? We can work with ck as sorted tuple of pairs.
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
    MEMO[ck] = best
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

def enumerate_posets(n):
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    m = len(pairs)
    total = 3**m
    for code in range(total):
        rel = set()
        x = code
        for (i,j) in pairs:
            r = x % 3
            x //= 3
            if r == 1:
                rel.add((i,j))
            elif r == 2:
                rel.add((j,i))
        cl = closure(rel, n)
        if set(cl) != set(rel):
            continue
        yield frozenset(rel)

def main():
    maxn = int(sys.argv[1]) if len(sys.argv)>1 else 5
    for n in range(1, maxn+1):
        print(f"=== n={n} ===", flush=True)
        seen_canonical = set()
        count_classes = 0
        count_tested = 0
        counterexamples = []
        t0 = time.time()
        for rel in enumerate_posets(n):
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
            if count_classes % 50 == 0:
                print(f"  progress classes={count_classes} time={time.time()-t0:.1f}", flush=True)
        print(f"classes={count_classes} tested={count_tested} counterexamples={len(counterexamples)} time={time.time()-t0:.1f}", flush=True)

if __name__ == '__main__':
    main()
