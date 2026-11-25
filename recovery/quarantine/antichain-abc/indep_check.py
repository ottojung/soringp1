"""Independent from-scratch check of F/H with corrected A/B/C certification.

Written directly from the definitions (Peczarski Order 23 (2006)):
  - state: transitive closed strict partial order, succ[i] bit j = i<j
  - e(P): linear extensions by subset DP
  - F(P) = 0 if total else 1 + min_{x,y inc} max(F(P+x<y), F(P+y<x))
  - slave(u,v) = |{z>u : z||v}| + |{z<v : z||u}|  (w.r.t. CURRENT P)
  - A(u,v): slaves<=1 and 2*e(P+u<v) >= e(P)
  - B(u,v): 2*e(P+u<v) == e(P)
  - C: x,y,z distinct: e(P+xy+yz) <= max{e(P+yx), e(P+zy)} <= e(P)/2
       (certifies the FIRST comparison {x,y}, node-local reading)
  - H(P) = 0 if total else 1 + min over CERTIFIED pairs of max(H(children)),
           INF if no certified pair.
No code shared with abc.cpp/abcppar2.cpp; canon by brute force over n!.
"""
import itertools, functools, sys

def closure(n, rel):
    # rel: set of (i,j) with i<j meaning i<j; return succ masks of transitive closure
    succ = [0]*n
    for (i,j) in rel: succ[i] |= 1<<j
    changed = True
    while changed:
        changed = False
        for i in range(n):
            for j in range(n):
                if succ[i]>>j&1:
                    add = succ[j] & ~succ[i]
                    if add: succ[i] |= add; changed = True
    return tuple(succ)

def extensions(succ, n):
    pred = [0]*n
    for i in range(n):
        for j in range(n):
            if succ[i]>>j&1: pred[j] |= 1<<i
    full = (1<<n)-1
    @functools.lru_cache(maxsize=None)
    def cnt(mask):
        if mask == 0: return 1
        s = 0
        for v in range(n):
            if mask>>v&1 and not (pred[v] & ~mask):
                s += cnt(mask ^ (1<<v))
        return s
    return cnt(full), pred

def incomparable(succ, n):
    return [(i,j) for i in range(n) for j in range(i+1,n)
            if not (succ[i]>>j&1) and not (succ[j]>>i&1)]

def is_total(succ, n):
    return not incomparable(succ, n)

def slaves(succ, pred, u, v):
    # z>u incomparable v, or z<v incomparable u  (w.r.t. CURRENT poset)
    c = 0
    for z in range(n):
        zu = (succ[u]>>z&1) or (pred[u]>>z&1) or z==u
        zv = (succ[v]>>z&1) or (pred[v]>>z&1) or z==v
        if (succ[u]>>z&1) and not zv: c += 1
        if (pred[v]>>z&1) and not zu: c += 1
    return c

def certified(succ, n, x, y):
    total, pred = extensions(succ, n)
    # children extension counts
    e_xy = extensions(closure(n, {(x,y)} | {(i,j) for i in range(n) for j in range(n) if succ[i]>>j&1}), n)[0] if True else 0
    rel = [(i,j) for i in range(n) for j in range(n) if succ[i]>>j&1]
    e_xy = extensions(closure(n, rel+[(x,y)]), n)[0]
    e_yx = extensions(closure(n, rel+[(y,x)]), n)[0]
    for (u,v,eu) in ((x,y,e_xy),(y,x,e_yx)):
        sl = slaves(succ, pred, u, v)
        if sl <= 1 and 2*eu >= total: return True
        if 2*eu == total: return True
    for (u,v) in ((x,y),(y,x)):
        evu = e_yx if (u,v)==(x,y) else e_xy
        for z in range(n):
            if z in (x,y): continue
            e1 = extensions(closure(n, rel+[(u,v),(v,z)]), n)[0]
            e2 = extensions(closure(n, rel+[(z,v)]), n)[0]
            bound = max(evu, e2)
            if 2*bound <= total and e1 <= bound: return True
    return False

def solve(succ, n, memo):
    key = canon(succ, n)
    if key in memo: return memo[key]
    s = canon_succ(key, n)  # solve on canonical rep
    if is_total(s, n):
        memo[key] = (0,0); return memo[key]
    total, pred = extensions(s, n)
    rel = [(i,j) for i in range(n) for j in range(n) if s[i]>>j&1]
    pairs = incomparable(s, n)
    e_of = {}
    for (x,y) in pairs:
        e_of[(x,y)] = extensions(closure(n, rel+[(x,y)]), n)[0]
        e_of[(y,x)] = extensions(closure(n, rel+[(y,x)]), n)[0]
    bestF = min(1+max(solve(closure(n, rel+[(x,y)]), n, memo)[0],
                      solve(closure(n, rel+[(y,x)]), n, memo)[0]) for (x,y) in pairs)
    cpairs = [(x,y) for (x,y) in pairs if certified(s, n, x, y)]
    if not cpairs:
        bestH = 10**9
    else:
        bestH = min(1+max(solve(closure(n, rel+[(x,y)]), n, memo)[1],
                          solve(closure(n, rel+[(y,x)]), n, memo)[1]) for (x,y) in cpairs)
    memo[key] = (bestF, bestH)
    return memo[key]

def canon(succ, n):
    best = None
    for p in itertools.permutations(range(n)):
        rows = []
        for a in range(n):
            m = 0
            src = succ[p[a]]
            for b in range(n):
                if src>>p[b]&1: m |= 1<<b
            rows.append(m)
        t = tuple(rows)
        if best is None or t < best: best = t
    return best

def canon_succ(key, n):
    return key

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv)>1 else 6
    memo = {}
    # enumerate all labelled posets via subsets of comparable pairs over a fixed order? 
    # simpler: all subsets of i<j pairs, keep transitive ones
    allpairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    seen = set()
    res = {}
    anti = tuple([0]*n)
    for r in range(len(allpairs), -1, -1):
        pass
    # too many subsets for n=6 (2^15=32768, fine!)
    for mask in range(1<<len(allpairs)):
        rel = [allpairs[k] for k in range(len(allpairs)) if mask>>k&1]
        s = closure(n, rel)
        if s in seen: continue
        seen.add(s)
    print(f'labelled posets on {n} elements: {len(seen)}')
    classes = {}
    for s in seen:
        classes.setdefault(canon(s, n), s)
    print(f'unlabeled classes: {len(classes)}')
    F, H = {}, {}
    antikey = canon(anti, n)
    fA, hA = solve(anti, n, memo)
    print(f'A_{n}: F={fA} H={hA} (memo classes used: {len(memo)})')
    over = 0
    for c in classes:
        f,h = solve(classes[c], n, memo)
        F[c], H[c] = f, h
        if h > f: over += 1
    print(f'classes with H>F: {over}')
    # S(n) literature check
    S6 = {5:7, 6:10}
    print(f'S({n}) literature = {S6.get(n,"?")}; F(A_n) computed = {fA}')
