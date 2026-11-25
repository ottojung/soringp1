#!/usr/bin/env python3
import itertools
import math
import sys
from functools import lru_cache

# Poset represented as tuple of int bitmasks: succ[i] has bit j set if i < j.

def closure(n, succ_bits):
    # succ_bits: list of ints, not necessarily transitively closed? we build by adding edges and closing
    s = list(succ_bits)
    changed = True
    while changed:
        changed = False
        for i in range(n):
            gi = s[i]
            m = gi
            while m:
                lb = m & -m
                j = lb.bit_length() - 1
                m ^= lb
                nj = s[i] | s[j]
                if nj != s[i]:
                    s[i] = nj
                    changed = True
    return tuple(s)

def add_relation(n, succ, i, j):
    # assume succ closed, add i<j
    s = list(succ)
    # all x with x==i or x<i (i.e. j' in pred of i?) easier: if i in succ[x] or x==i
    new_greater = succ[j] | (1 << j)
    for x in range(n):
        if x == i or ((succ[x] >> i) & 1):
            s[x] |= new_greater
    return tuple(s)

def incomparable_pairs(n, succ):
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if not ((succ[i] >> j) & 1) and not ((succ[j] >> i) & 1):
                pairs.append((i,j))
    return pairs

def is_total(n, succ):
    # total if n*(n-1)/2 relations
    c = 0
    for i in range(n):
        c += succ[i].bit_count()
    return c == n*(n-1)//2

@lru_cache(maxsize=None)
def m_poset(n, succ):
    if is_total(n, succ):
        return 0
    best = None
    for i,j in incomparable_pairs(n, succ):
        v = 1 + max(m_poset(n, add_relation(n,succ,i,j)), m_poset(n, add_relation(n,succ,j,i)))
        if best is None or v < best:
            best = v
            if best == 1: # though impossible unless becomes total in 1? m>=1 here
                pass
    return best

# Extension-set solver
def linear_extensions_list(n, succ):
    # generate all linear orders consistent with succ
    pred_count_base = [0]*n
    preds = [0]*n
    for i in range(n):
        # preds[j] includes i if i<j
        pass
    # compute predecessors mask/count
    pred_mask = [0]*n
    for i in range(n):
        m = succ[i]
        while m:
            lb = m & -m
            j = lb.bit_length()-1
            m ^= lb
            pred_mask[j] |= (1 << i)
    res = []
    used = 0
    order = []
    def dfs():
        if len(order) == n:
            # store rank permutation as tuple where p[pos]=element or element->pos; easier store tuple of elements in increasing order
            res.append(tuple(order))
            return
        for v in range(n):
            if not (used >> v) & 1:
                if (pred_mask[v] & ~used) == 0:
                    # available
                    nonlocal_used = None
    # iterative backtrack simpler
    # We'll implement recursive with nonlocal
    return res

def gen_linear_extensions(n, succ):
    pred_mask = [0]*n
    for i in range(n):
        m = succ[i]
        while m:
            lb = m & -m
            j = lb.bit_length()-1
            m ^= lb
            pred_mask[j] |= (1 << i)
    res = []
    order = [-1]*n
    used = 0
    def bt(k, used_mask):
        if k == n:
            res.append(tuple(order))
            return
        # find all minimal available
        avail = ((1<<n)-1) & ~used_mask
        m = avail
        # collect candidates to be deterministic
        while m:
            lb = m & -m
            v = lb.bit_length()-1
            m ^= lb
            if (pred_mask[v] & ~used_mask) == 0:
                order[k] = v
                bt(k+1, used_mask | lb)
    bt(0,0)
    return res

# Extension-set state: frozenset of linear orders (each tuple elements in increasing rank order index->element? wait: order[pos]=element means element is at position pos)
# Comparing elements x,y splits extensions into those where x before y and vice versa.

def ext_compare(exts, x, y):
    # exts iterable of tuples order[pos]=element
    a = []
    b = []
    for e in exts:
        # find positions
        px = -1; py = -1
        # can precompute index map, but small n
        # e is tuple length n
        for idx,val in enumerate(e):
            if val == x: px = idx
            elif val == y: py = idx
        if px < py:
            a.append(e)
        else:
            b.append(e)
    return tuple(a), tuple(b)

@lru_cache(maxsize=None)
def m_ext(exts_key):
    # exts_key is tuple of extension tuples, sorted for canonical key
    exts = exts_key
    if len(exts) <= 1:
        return 0
    n = len(exts[0])
    # all pairs? but some comparisons may not split; still allowed? in poset game only incomparable pairs in current poset; but extension-set of a poset: any pair comparable in all gives no split - but optimal won't choose.
    best = None
    for x in range(n):
        for y in range(x+1,n):
            a,b = ext_compare(exts,x,y)
            if not a or not b:
                continue
            v = 1 + max(m_ext(tuple(sorted(a))), m_ext(tuple(sorted(b))))
            if best is None or v < best:
                best = v
    return best

# Unlabelled poset enumeration via canonical form
def canonical(n, succ):
    # return lexicographically smallest tuple over all relabelings
    # succ is tuple of bitmasks under current labeling
    best = None
    elems = list(range(n))
    for perm in itertools.permutations(elems):
        # perm[new]=old? build image: new succ'
        inv = [0]*n
        for new, old in enumerate(perm):
            inv[old] = new
        s2 = [0]*n
        for old_i in range(n):
            ni = inv[old_i]
            m = succ[old_i]
            bits = 0
            while m:
                lb = m & -m
                old_j = lb.bit_length()-1
                m ^= lb
                bits |= (1 << inv[old_j])
            s2[ni] = bits
        t = tuple(s2)
        if best is None or t < best:
            best = t
    return best

def all_unlabelled_posets(n):
    # generate all labelled transitively closed posets then canonicalize
    start = tuple([0]*n)
    seen = {start}
    stack = [start]
    while stack:
        s = stack.pop()
        for i,j in incomparable_pairs(n,s):
            for t in (add_relation(n,s,i,j), add_relation(n,s,j,i)):
                if t not in seen:
                    seen.add(t)
                    stack.append(t)
    # canonicalize
    reps = {}
    for s in seen:
        c = canonical(n,s)
        reps[c] = s  # keep one representative
    return list(reps.keys())

def profile_condition(n, succ, mval):
    # exists optimal move with worse child depth == mval-1 and other >= mval-2
    pairs = incomparable_pairs(n,succ)
    ok = False
    details = []
    for i,j in pairs:
        c1 = add_relation(n,succ,i,j)
        c2 = add_relation(n,succ,j,i)
        m1 = m_poset(n,c1)
        m2 = m_poset(n,c2)
        worst = 1 + max(m1,m2)
        other = min(m1,m2)
        is_opt = (worst == mval)
        if is_opt and other >= mval-2:
            ok = True
        details.append((i,j,m1,m2,is_opt))
    return ok, details

def main():
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    print(f"Enumerating and testing n<= {max_n}")
    for n in range(1, max_n+1):
        m_poset.cache_clear()
        # for extension solver we cache per n separately by key content; clear not needed as keys differ
        posets = all_unlabelled_posets(n)
        print(f"n={n}: unlabelled posets = {len(posets)}")
        # cross-check solvers on all posets
        for idx,s in enumerate(posets):
            mp = m_poset(n,s)
            exts = tuple(sorted(gen_linear_extensions(n,s)))
            me = m_ext(exts)
            if mp != me:
                print(f"MISMATCH n={n} poset={s} m_poset={mp} m_ext={me} e={len(exts)}")
                raise SystemExit(2)
        print(f"  cross-check OK (poset-state vs extension-set) for all {len(posets)} posets")
        # test profile condition
        counterexamples = []
        total_ge2 = 0
        satisfy = 0
        for s in posets:
            mp = m_poset(n,s)
            if mp >= 2:
                total_ge2 += 1
                ok, details = profile_condition(n,s,mp)
                if ok:
                    satisfy += 1
                else:
                    counterexamples.append((s, mp, details))
        print(f"  m(P)>=2: {total_ge2}, satisfy profile: {satisfy}, counterexamples: {len(counterexamples)}")
        for s, mp, details in counterexamples:
            print(f"  COUNTEREXAMPLE n={n} m(P)={mp} succ={s}")
            # show all optimal moves if any? and all moves
            for (i,j,m1,m2,is_opt) in details:
                print(f"    pair ({i},{j}): children depths {m1},{m2} opt={is_opt}")
        sys.stdout.flush()

if __name__ == '__main__':
    main()
