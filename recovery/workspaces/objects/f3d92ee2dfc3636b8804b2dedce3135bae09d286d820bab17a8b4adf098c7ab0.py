#!/usr/bin/env python3
"""Exact one-ply adversarial information bound L1 for the glued height-2 posets R_t.

Model (docs/problem.md, docs/research-one-ply-obstruction.md):
  F(P) = min remaining worst-case comparisons identifying the unknown linear extension.
  e(P) = number of linear extensions.
  L0(P) = ceil(log2 e(P)).
  L1(P) = 0 if P total, else 1 + min over incomparable unordered pairs {i,j} of
          max(L0(P+i<j), L0(P+j<i)).

R_t definition (from #301 post 2026-11-10T21:19:55Z, re-verified here):
  minima A = {y, a_1..a_t}; maxima B = {x, b_1, c_1, ..., b_t, c_t}.
  y below all of B; each a_i below b_i and c_i only; all other cross pairs incomparable.
  n = 3t + 2.

e(P) by subset ideal-DP: e(S) = sum over x minimal in S of e(S \ {x}), e(empty)=1.
"""

import sys
import time
from math import log2, ceil


def build_R(t):
    """Return (n, pred) where pred[i] is a bitmask of strict predecessors of i."""
    # index layout: 0 = y, 1 = x, 2..1+t = a_1..a_t, then for each i: b_i, c_i
    n = 3 * t + 2
    pred = [0] * n

    def a(i):   # a_i, i in 1..t
        return 1 + i

    def b(i):   # b_i, i in 1..t
        return 2 + t + 2 * (i - 1)

    def c(i):   # c_i, i in 1..t
        return 3 + t + 2 * (i - 1)

    y, x = 0, 1
    # y below all of B = {x} U {b_i, c_i}; minima A are mutually incomparable
    pred[x] |= 1 << y
    for i in range(1, t + 1):
        pred[b(i)] |= 1 << y
        pred[c(i)] |= 1 << y
    # each a_i below b_i, c_i only
    for i in range(1, t + 1):
        pred[b(i)] |= 1 << a(i)
        pred[c(i)] |= 1 << a(i)
    return n, pred


def closure(pred, n):
    pred = list(pred)
    changed = True
    while changed:
        changed = False
        for k in range(n):
            pk = pred[k]
            for i in range(n):
                if (pred[i] >> k) & 1:
                    new = pred[i] | pk
                    if new != pred[i]:
                        pred[i] = new
                        changed = True
    return pred


def e_dp(pred, n):
    """Exact number of linear extensions by subset ideal-DP."""
    size = 1 << n
    e = [0] * size
    e[0] = 1
    # precompute predecessor-union per subset is overkill; iterate bits
    for S in range(1, size):
        total = 0
        bits = S
        while bits:
            low = bits & -bits
            x = low.bit_length() - 1
            # x minimal in S iff no predecessor of x lies in S
            if pred[x] & S == 0:
                total += e[S ^ low]
            bits ^= low
        e[S] = total
    return e[size - 1]


def ceil_log2(v):
    assert v >= 1
    return v.bit_length() - 1 if v & (v - 1) == 0 else v.bit_length()


def l0_from_e(e):
    return ceil_log2(e)


def incomparable_pairs(pred, n):
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if not ((pred[j] >> i) & 1) and not ((pred[i] >> j) & 1):
                pairs.append((i, j))
    return pairs


def add_relation(pred, n, i, j):
    """Return pred of P + i<j (strict), transitively closed."""
    p = list(pred)
    p[j] |= 1 << i
    return closure(p, n)


def analyze(t, direct_both=True, verbose=True):
    n, pred = build_R(t)
    assert all(pred[i] == 0 for i in range(n) if i == 0 or 2 <= i <= 1 + t), \
        "minima must have no predecessors"
    e = e_dp(pred, n)
    l0 = l0_from_e(e)
    pairs = incomparable_pairs(pred, n)
    best = None
    argmins = []
    rows = []
    for (i, j) in pairs:
        p1 = add_relation(pred, n, i, j)
        e1 = e_dp(p1, n)
        if direct_both:
            p2 = add_relation(pred, n, j, i)
            e2 = e_dp(p2, n)
            assert e1 + e2 == e, (t, i, j, e1, e2, e)
        else:
            e2 = e - e1
        l1a, l1b = l0_from_e(e1), l0_from_e(e2)
        m = max(l1a, l1b)
        rows.append((i, j, e1, e2, l1a, l1b, m))
        if best is None or m < best:
            best = m
            argmins = [(i, j, e1, e2, l1a, l1b)]
        elif m == best:
            argmins.append((i, j, e1, e2, l1a, l1b))
    L1 = 1 + best
    if verbose:
        print(f"R_{t}: n={n}, e={e}, L0={l0}, #incomparable pairs={len(pairs)}, "
              f"L1={L1}, #argmin pairs={len(argmins)}")
        print(f"  argmin pairs (i,j,e_left,e_right,L0_left,L0_right):")
        for r in argmins:
            print(f"    {r}")
        # show worst pair too
        worst = max(rows, key=lambda r: r[6])
        print(f"  worst pair: {worst}")
    return dict(t=t, n=n, e=e, l0=l0, L1=L1, pairs=pairs, rows=rows,
                argmins=argmins, best=best)


def brute_force_e(pred, n):
    """Independent check: count permutations that are linear extensions."""
    import itertools
    count = 0
    for perm in itertools.permutations(range(n)):
        pos = {v: k for k, v in enumerate(perm)}
        ok = True
        for i in range(n):
            bits = pred[i]
            while bits:
                low = bits & -bits
                u = low.bit_length() - 1
                if pos[u] > pos[i]:
                    ok = False
                    break
                bits ^= low
            if not ok:
                break
        if ok:
            count += 1
    return count


def shuffle_count(a_order, b_order, predA_mask, a_index):
    """Number of interleavings of the fixed A-order and B-order consistent with pred.

    predA_mask[b] = bitmask (over A positions) of A-elements that must precede b.
    a_index maps A element -> its position in a_order.
    """
    m, k = len(a_order), len(b_order)
    # prefix[i] = bitmask of A positions placed after i A-elements
    prefix = [0] * (m + 1)
    acc = 0
    for i, a in enumerate(a_order):
        acc |= 1 << a_index[a]
        prefix[i + 1] = acc
    dp = [[0] * (k + 1) for _ in range(m + 1)]
    dp[0][0] = 1
    for i in range(m + 1):
        pi = prefix[i]
        row = dp[i]
        for j in range(k + 1):
            v = row[j]
            if v == 0:
                continue
            if i < m:
                dp[i + 1][j] += v
            if j < k:
                if predA_mask[b_order[j]] & ~pi == 0:
                    row[j + 1] += v
    return dp[m][k]


def e_by_shuffle_sum(pred, n, t):
    """Independent e(P) for R_t: sum over A-order x B-order of valid shuffle counts."""
    import itertools
    A = [0] + [1 + i for i in range(1, t + 1)]          # y, a_1..a_t
    B = [1] + [x for i in range(1, t + 1)
               for x in (2 + t + 2 * (i - 1), 3 + t + 2 * (i - 1))]
    a_set = set(A)
    a_index = {a: i for i, a in enumerate(A)}
    a_mask = 0
    for a in A:
        a_mask |= 1 << a
    predA_mask = {}
    for b in B:
        m_b = 0
        bits = pred[b] & a_mask
        while bits:
            low = bits & -bits
            u = low.bit_length() - 1
            m_b |= 1 << a_index[u]
            bits ^= low
        predA_mask[b] = m_b
    total = 0
    for ao in itertools.permutations(A):
        for bo in itertools.permutations(B):
            total += shuffle_count(ao, bo, predA_mask, a_index)
    return total


def main():
    # Independent brute-force cross-check of the DP on small cases.
    for t in (1, 2):
        n, pred = build_R(t)
        e_dp_val = e_dp(pred, n)
        e_bf = brute_force_e(pred, n)
        print(f"[cross-check] R_{t}: DP e={e_dp_val}, brute-force e={e_bf}, "
              f"match={e_dp_val == e_bf}")
        assert e_dp_val == e_bf
    # Independent shuffle-sum cross-check at t=3 (the key case).
    n3, pred3 = build_R(3)
    t0 = time.time()
    e3_shuffle = e_by_shuffle_sum(pred3, n3, 3)
    print(f"[cross-check] R_3: DP e={e_dp(pred3, n3)}, shuffle-sum e={e3_shuffle}, "
          f"match={e_dp(pred3, n3) == e3_shuffle} ({time.time()-t0:.2f}s)")
    assert e_dp(pred3, n3) == e3_shuffle == 366240
    print()
    results = {}
    for t in (1, 2, 3):
        t0 = time.time()
        results[t] = analyze(t, direct_both=True)
        print(f"  [R_{t} took {time.time()-t0:.3f}s]")
        print()
    # R_4: time it; skip if > 60s
    t0 = time.time()
    n, pred = build_R(4)
    e4 = e_dp(pred, n)
    l04 = l0_from_e(e4)
    pairs4 = incomparable_pairs(pred, n)
    print(f"R_4: n={n}, e={e4}, L0={l04}, #incomparable pairs={len(pairs4)}")
    # For R_4 use complement identity to stay cheap, but verify it on a few pairs.
    best = None
    argmins = []
    rows = []
    checked = 0
    for (i, j) in pairs4:
        e1 = e_dp(add_relation(pred, n, i, j), n)
        e2 = e4 - e1
        if checked < 5:
            e2d = e_dp(add_relation(pred, n, j, i), n)
            assert e1 + e2d == e4, (i, j, e1, e2d, e4)
            checked += 1
        l1a, l1b = l0_from_e(e1), l0_from_e(e2)
        m = max(l1a, l1b)
        rows.append((i, j, e1, e2, l1a, l1b, m))
        if best is None or m < best:
            best = m
            argmins = [(i, j, e1, e2, l1a, l1b)]
        elif m == best:
            argmins.append((i, j, e1, e2, l1a, l1b))
    L14 = 1 + best
    dt = time.time() - t0
    print(f"R_4: L1={L14}, #argmin pairs={len(argmins)}, wall={dt:.2f}s")
    print(f"  argmin pairs (first 20): {argmins[:20]}")
    results[4] = dict(t=4, n=n, e=e4, l0=l04, L1=L14, pairs=pairs4, rows=rows,
                      argmins=argmins, best=best, wall=dt)
    print()
    print("Summary:")
    for t in sorted(results):
        r = results[t]
        print(f"  R_{t}: n={r['n']}, e={r['e']}, L0={r['l0']}, L1={r['L1']}, "
              f"known F={'4' if t==1 else '11' if t==2 else '[19,24]' if t==3 else '?'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
