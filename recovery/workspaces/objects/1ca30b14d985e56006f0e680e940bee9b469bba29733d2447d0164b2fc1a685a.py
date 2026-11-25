#!/usr/bin/env python3
"""Optimized exact minimax oracle for the Fibonacci-split property.

Improvements over oracle3.py
-----------------------------
* Relations are stored as a tuple of n bitmask rows (row[i] = up-set of i),
  so transitive closure / child construction use O(n^2) bit operations.
* Posets are enumerated LEVEL BY LEVEL as canonical representatives only:
  a new MAXIMAL element is added to each (n-1)-poset with every possible
  down-set, then deduplicated by the 1-WL canonical form.  This generates
  every isomorphism class of n-posets (every poset has a maximal element)
  while avoiding the Theta(millions) labelled posets that oracle3.py
  canonicalised at n=7.
* The 1-WL canonical form is cached by the raw labelled rows tuple, so a
  given labelled state is canonicalised at most once.
* Memo key is (n, canonical form) -- the fix for the earlier memo bug is
  preserved.

Checks both properties for every class:
  strong : some OPTIMAL comparison has both children >= m-2
  weak   : some comparison (not necessarily optimal) has both children >= m-2

Usage:
  python3 scripts/oracle_n8.py 7                 # validate n<=7
  python3 scripts/oracle_n8.py 8 --deadline 1400 # bounded n=8 run
  python3 scripts/oracle_n8.py 8 --family width3 # principled subset
"""
import sys, time, itertools, math, resource, json, argparse

EXPECTED = {1: 1, 2: 2, 3: 5, 4: 16, 5: 63, 6: 318, 7: 2045, 8: 16999}
ANTICHAIN_S = {1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 9: 19}

# ---------------------------------------------------------------- bitmask core

def tc(rows, n):
    """Transitive closure of a rows-tuple poset."""
    rows = list(rows)
    for k in range(n):
        rk = rows[k]
        bk = 1 << k
        for i in range(n):
            if rows[i] & bk:
                rows[i] |= rk
    return tuple(rows)

def child_rows(rows, n, a, b):
    """rows with relation a<b added (a,b already incomparable), then closed."""
    r = list(rows)
    r[a] |= (1 << b)
    return tc(tuple(r), n)

def incomparable_pairs(rows, n):
    out = []
    for i in range(n):
        ri = rows[i]
        for j in range(i + 1, n):
            if not (ri & (1 << j)) and not (rows[j] & (1 << i)):
                out.append((i, j))
    return out

def pairs_from_rows(rows, n):
    return tuple(sorted((i, j) for i in range(n) for j in range(n)
                        if rows[i] & (1 << j)))

# ---------------------------------------------------------------- 1-WL canonical form

def refine_colors(rows, n):
    color = []
    for i in range(n):
        dc = sum(1 for x in range(n) if rows[x] & (1 << i))
        uc = bin(rows[i]).count('1')
        color.append((dc, uc))
    uniq = sorted(set(color))
    mp = {c: i for i, c in enumerate(uniq)}
    color = [mp[c] for c in color]
    while True:
        new = []
        for i in range(n):
            in_c = tuple(sorted(color[x] for x in range(n) if rows[x] & (1 << i)))
            out_c = tuple(sorted(color[y] for y in range(n) if rows[i] & (1 << y)))
            new.append((color[i], in_c, out_c))
        uniq = sorted(set(new))
        mp = {c: i for i, c in enumerate(uniq)}
        new_int = [mp[c] for c in new]
        if new_int == color:
            return new_int
        color = new_int

CANON_CACHE = {}

def canonical_key(rows, n):
    ck = CANON_CACHE.get(rows)
    if ck is not None:
        return ck
    color = refine_colors(rows, n)
    groups = {}
    for i in range(n):
        groups.setdefault(color[i], []).append(i)
    cells = [groups[c] for c in sorted(groups)]
    starts = []
    s = 0
    for cell in cells:
        starts.append(s)
        s += len(cell)
    cell_perms = [list(itertools.permutations(cell)) for cell in cells]
    best = None
    rel = pairs_from_rows(rows, n)
    for combo in itertools.product(*cell_perms):
        perm = [0] * n
        for ci, cp in enumerate(combo):
            st = starts[ci]
            for idx, v in enumerate(cp):
                perm[v] = st + idx
        key = tuple(sorted((perm[a], perm[b]) for (a, b) in rel))
        if best is None or key < best:
            best = key
    CANON_CACHE[rows] = best
    return best

# ---------------------------------------------------------------- minimax memo

MEMO = {}

def m_depth(rows, n):
    ck = canonical_key(rows, n)
    key = (n, ck)
    v = MEMO.get(key)
    if v is not None:
        return v
    rel = ck  # sorted tuple of pairs in canonical labelling
    if len(rel) == n * (n - 1) // 2:
        MEMO[key] = 0
        return 0
    relset = set(rel)
    best = None
    for (a, b) in incomparable_pairs_from_rel(relset, n):
        r1 = tc_rel(relset | {(a, b)}, n)
        r2 = tc_rel(relset | {(b, a)}, n)
        d1 = m_depth(rows_from_rel(r1, n), n)
        d2 = m_depth(rows_from_rel(r2, n), n)
        val = 1 + (d1 if d1 > d2 else d2)
        if best is None or val < best:
            best = val
    MEMO[key] = best
    return best

def incomparable_pairs_from_rel(relset, n):
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) not in relset and (j, i) not in relset:
                out.append((i, j))
    return out

def rows_from_rel(relset, n):
    r = [0] * n
    for (a, b) in relset:
        r[a] |= (1 << b)
    return tuple(r)

def tc_rel(relset, n):
    return pairs_from_rows(tc(rows_from_rel(relset, n), n), n)

# ---------------------------------------------------------------- level generator

def downsets(rows, k):
    """All down-sets of the k-element poset (rows on 0..k-1), as frozensets."""
    res = []
    # a subset S is a down-set iff for every x in S, all y<x are also in S
    for mask in range(1 << k):
        ok = True
        for x in range(k):
            if mask & (1 << x):
                # all y with y<x must be in mask
                for y in range(k):
                    if (rows[y] & (1 << x)) and not (mask & (1 << y)):
                        ok = False
                        break
                if not ok:
                    break
        if ok:
            res.append(mask)
    return res

def gen_level(reps_prev, n, family=None, deadline=None):
    """Generate canonical representatives of n-posets by adding a maximal element."""
    k = n - 1
    seen = set()
    out = []
    v = k
    for prev in reps_prev:
        if deadline and time.time() > deadline:
            return out
        for dmask in downsets(prev, k):
            rows = list(prev) + [0]
            m = dmask
            while m:
                b = m & -m
                d = b.bit_length() - 1
                rows[d] |= (1 << v)
                m ^= b
            rows = tc(tuple(rows), n)
            if family and not family_ok(rows, n, family):
                continue
            ck = canonical_key(rows, n)
            if ck in seen:
                continue
            seen.add(ck)
            out.append(rows)
    return out

# ---------------------------------------------------------------- family filters

def height(rows, n):
    # longest chain length via DP on the DAG (rows already transitively closed)
    order = sorted(range(n), key=lambda i: bin(rows[i]).count('1'))
    dp = [1] * n
    best = 0
    for i in order:
        for j in range(n):
            if rows[i] & (1 << j):
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        if dp[i] > best:
            best = dp[i]
    return best

def width(rows, n):
    # Dilworth: min chain cover = max antichain; bipartite matching i_L -> i_R
    # edge i_L -> j_R iff i<j (strict comparability)
    matchR = [-1] * n

    def aug(u, seen):
        for v in range(n):
            if (rows[u] & (1 << v)) and not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or aug(matchR[v], seen):
                    matchR[v] = u
                    return True
        return False

    matching = 0
    for u in range(n):
        if aug(u, [False] * n):
            matching += 1
    return n - matching

def is_series_parallel(rows, n):
    """N-free: no induced 4-element poset isomorphic to the 'N' poset.
    N = relations a<b, c<b, c<d (and no others among a,b,c,d).
    We test all 4-subsets and all labellings of the N pattern."""
    for quad in itertools.combinations(range(n), 4):
        q = list(quad)
        # induced comparability pattern
        for perm in itertools.permutations(q):
            a, b, c, d = perm
            # required comparabilities
            req = [(a, b), (c, b), (c, d)]
            # forbidden comparabilities (all other ordered pairs among the 4)
            allpairs = [(x, y) for x in q for y in q if x != y]
            reqset = set(req)
            ok = True
            for (x, y) in allpairs:
                comp = bool(rows[x] & (1 << y))
                if (x, y) in reqset:
                    if not comp:
                        ok = False
                        break
                else:
                    if comp:
                        ok = False
                        break
            if ok:
                return False
    return True

def family_ok(rows, n, fam):
    if fam == 'all':
        return True
    if fam.startswith('height'):
        return height(rows, n) <= int(fam[6:])
    if fam.startswith('width'):
        return width(rows, n) <= int(fam[5:])
    if fam == 'sp':
        return is_series_parallel(rows, n)
    raise ValueError(fam)

# ---------------------------------------------------------------- property check

def check(rows, n):
    m = m_depth(rows, n)
    if m < 2:
        return True, True, m, None
    strong = False
    weak = False
    best_min = -1
    optimal = []
    for (a, b) in incomparable_pairs(rows, n):
        r1 = child_rows(rows, n, a, b)
        r2 = child_rows(rows, n, b, a)
        d1 = m_depth(r1, n)
        d2 = m_depth(r2, n)
        mn = min(d1, d2)
        if mn > best_min:
            best_min = mn
        if mn >= m - 2:
            weak = True
        if 1 + max(d1, d2) == m:
            optimal.append(((a, b), d1, d2))
            if mn >= m - 2:
                strong = True
    info = {'m': m, 'best_min': best_min, 'optimal': optimal,
            'pairs_from_rows': pairs_from_rows(rows, n)}
    return strong, weak, m, info

# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('maxn', type=int)
    ap.add_argument('--deadline', type=float, default=None,
                    help='hard wall-clock budget in seconds for the whole run')
    ap.add_argument('--family', default='all')
    ap.add_argument('--mem-mb', type=int, default=5000)
    ap.add_argument('--log', default=None)
    args = ap.parse_args()

    try:
        cap = args.mem_mb * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (cap, cap))
    except Exception as e:
        print('mem rlimit failed:', e, flush=True)

    out = open(args.log, 'w') if args.log else sys.stdout
    def log(*a):
        print(*a, file=out, flush=True)

    start = time.time()
    deadline = start + args.deadline if args.deadline else None
    log(f'# start {time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())} '
        f'family={args.family} deadline={args.deadline}')

    reps = [tuple([0])]  # n=1
    for n in range(1, args.maxn + 1):
        if n > 1:
            new_reps = gen_level(reps, n, family=args.family if n == args.maxn else 'all',
                                 deadline=deadline)
            reps = new_reps
        log(f'=== n={n} classes={len(reps)} elapsed={time.time()-start:.1f}')
        if deadline and time.time() > deadline:
            log('DEADLINE reached during generation')
            break
        # validation for n<=7: counts and antichain S(n)
        exp = EXPECTED.get(n)
        if exp is not None and args.family == 'all' and n <= 7:
            if len(reps) != exp:
                log(f'VALIDATION FAIL count {len(reps)} != {exp}')
            else:
                log(f'VALIDATION OK count={len(reps)}')
        strong_bad = []
        weak_bad = []
        t0 = time.time()
        for idx, rows in enumerate(reps):
            if deadline and time.time() > deadline:
                log(f'DEADLINE reached at class {idx}/{len(reps)}')
                break
            s, w, m, info = check(rows, n)
            if not s:
                strong_bad.append(info)
            if not w:
                weak_bad.append(info)
            if (idx + 1) % 500 == 0:
                log(f'  progress {idx+1}/{len(reps)} elapsed={time.time()-start:.1f} '
                    f'memo={len(MEMO)} canon={len(CANON_CACHE)}')
        log(f'RESULT n={n} tested_so_far={min(len(reps), idx+1 if n<=args.maxn else len(reps))} '
            f'strong_counterexamples={len(strong_bad)} weak_counterexamples={len(weak_bad)} '
            f'time={time.time()-t0:.1f} memo={len(MEMO)} canon={len(CANON_CACHE)}')
        if strong_bad:
            log('FIRST STRONG COUNTEREXAMPLE ' + json.dumps(strong_bad[0]))
        if weak_bad:
            log('FIRST WEAK COUNTEREXAMPLE ' + json.dumps(weak_bad[0]))
        # antichain check
        if args.family == 'all' and n <= len(ANTICHAIN_S):
            ac = tuple([0] * n)
            am = m_depth(ac, n)
            log(f'ANTICHAIN S({n})={am} expected={ANTICHAIN_S[n]} '
                f'{"OK" if am==ANTICHAIN_S[n] else "FAIL"}')

if __name__ == '__main__':
    main()
