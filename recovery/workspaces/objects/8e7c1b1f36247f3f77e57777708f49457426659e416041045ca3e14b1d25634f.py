#!/usr/bin/env python3
import sys, itertools

def closure(rel, n):
    less = [[False]*n for _ in range(n)]
    for (a,b) in rel:
        less[a][b] = True
    for k in range(n):
        for i in range(n):
            if less[i][k]:
                for j in range(n):
                    if less[k][j]:
                        less[i][j] = True
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

MEMO = {}

def rel_tuple(rel):
    return tuple(sorted(rel))

def m_depth(n, rel):
    key = (n, rel_tuple(rel))
    if key in MEMO:
        return MEMO[key]
    if is_total(rel, n):
        MEMO[key] = 0
        return 0
    best = None
    for (a,b) in incomparable_pairs(rel, n):
        r1 = closure(set(rel) | {(a,b)}, n)
        r2 = closure(set(rel) | {(b,a)}, n)
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
    for (a,b) in incomparable_pairs(rel, n):
        r1 = closure(set(rel) | {(a,b)}, n)
        r2 = closure(set(rel) | {(b,a)}, n)
        d1 = m_depth(n, r1)
        d2 = m_depth(n, r2)
        if 1 + max(d1,d2) != m:
            continue
        if max(d1,d2) != m-1:
            continue
        if min(d1,d2) >= m-2:
            return True, m, ((a,b), d1, d2)
    return False, m, None

def canonical_key(n, rel):
    best = None
    elems = list(range(n))
    for perm in itertools.permutations(elems):
        newrel = set()
        for (a,b) in rel:
            newrel.add((perm[a], perm[b]))
        key = tuple(sorted(newrel))
        if best is None or key < best:
            best = key
    return best

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
        for rel in enumerate_posets(n):
            ck = canonical_key(n, rel) if n <= 6 else None
            if ck is not None:
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
                        f.write(f"# Counterexample n={n}\n\nPoset comparabilities: {sorted(rel)}\n\nm={m}\n")
        print(f"classes={count_classes} tested={count_tested} counterexamples={len(counterexamples)}", flush=True)

if __name__ == '__main__':
    main()
