#!/usr/bin/env python3
"""Instrumented copy of Ford-Johnson merge-insertion from
scripts/upper_witness.py (fj_order / fj_sort / fj_upper_bound).

Nothing here modifies the original script.  This file is a scratch copy
used only to measure per-insertion comparison counts and worst cases.

Records per insertion (one per pending schedule index i, 1..K):
  i         schedule index; K = #pairs (+1 if n odd; index K is the straggler)
  q         q(i) = min{r >= 1 : J_r >= i}  (block index)
  m         size of the searched interval at insertion time
            (m = winner_pos for regular indices, m = len(chain) for the
            straggler); the search cost is g(m,p) for realized position p
  mmax      i-1 + b_i with b_i = number of schedule indices before i
  cost      exact comparisons spent on this insertion
  L         chain length before the insertion
  straggler True iff winner is None (odd n)

Modes:
  actual    binary search with true key comparisons (verbatim behaviour)
  worst     every comparison answered "less", i.e. insert at position 0
            = the all-below / all-less pattern (proved attainable).
"""
import os
import sys

NMAX = 40
VER = "instrument-fj-recurrence v2"


def jac(limit):
    """J_0..J_k with J_k (k>=limit... just extend until J[-1] >= limit)."""
    J = [0, 1]
    while J[-1] < limit:
        J.append(J[-1] + 2 * J[-2])
    return J


def fj_order_c(K, J):
    """Copy of fj_order(K) from scripts/upper_witness.py."""
    order = []
    pairs = [(J[1], J[0] + 1)]
    for k in range(3, len(J)):
        pairs.append((J[k], J[k - 1] + 1))
    for hi, lo in pairs:
        for idx in range(hi, lo - 1, -1):
            if idx <= K:
                order.append(idx)
        if hi >= K:
            break
    return order


def fj_sort_instr(items, J, mode):
    """Instrumented merge-insertion.  Returns (sorted, records, total)."""
    records = []
    total = [0]

    def rec(i, qv, m, mmax, L, straggler, cost, p):
        records.append((i, qv, m, mmax, L, straggler, cost, p))

    def search(bound, winner):
        """Insert loser below `bound` chain positions (0..bound-1).
        Returns (position, cost).  worst mode: always answer 'less'."""
        chain_ = chain  # closure
        lo, hi, cost = 0, bound, 0
        while lo < hi:
            mid = (lo + hi) // 2
            cost += 1
            if mode == "worst":
                below = True
            else:
                below = loser_cmp(loser, chain_[mid])
            if below:
                hi = mid
            else:
                lo = mid + 1
        total[0] += cost
        return lo, cost

    def loser_cmp(a, b):
        # in 'actual' mode: true comparison; in 'worst': never called
        if mode == "worst":
            raise AssertionError
        return a < b

    def sort(items):
        n = len(items)
        if n <= 1:
            return list(items), [], 0
        pr = []
        for i in range(0, n - 1, 2):
            total[0] += 1
            if items[i] <= items[i + 1]:
                pr.append((items[i], items[i + 1]))
            else:
                pr.append((items[i + 1], items[i]))
        st = items[-1] if n % 2 == 1 else None
        winners = [w for (_, w) in pr]
        losers = [l for (l, _) in pr]
        sw, _, _ = sort(winners)
        k = len(winners)
        pos = {w: i for i, w in enumerate(sw)}
        pend = {pos[winners[i]] + 1: (losers[i], winners[i]) for i in range(k)}
        K = k
        if st is not None:
            K = k + 1
            pend[K] = (st, None)
        chain = list(sw)
        wp = {w: i for i, w in enumerate(chain)}
        sched = fj_order_c(K, J)
        records = []
        for bi, idx in enumerate(sched):
            lom, win = pend[idx]
            qv = q_of(idx, J)
            mmax = idx - 1 + bi                       # i-1 + b_i
            L = len(chain)
            bound = L if win is None else wp[win]
            # nested search needs true comparisons in actual mode
            if mode == "actual":
                lo, hi, cost = 0, bound, 0
                while lo < hi:
                    mid = (lo + hi) // 2
                    cost += 1
                    total[0] += 1
                    if lom < chain[mid]:
                        hi = mid
                    else:
                        lo = mid + 1
                p = lo
            else:
                p, cost = 0, bit_cost(bound)
                total[0] += cost
            records.append((idx, qv, bound, mmax, L, win is None, cost, p))
            chain.insert(p, lom)
            for w, pp in list(wp.items()):
                if pp >= p:
                    wp[w] = pp + 1
        return chain, records, total[0]

    chain, records, t = sort(list(items))
    if mode == "actual" and chain != sorted(items):
        raise AssertionError("did not sort")
    return chain, records, t


def bit_cost(m):
    """Exact worst-case cost g over positions for interval size m:
    f(m) = ceil(log2(m+1))."""
    return (m).bit_length() if m else 0  # ceil(log2(m+1)) for m>=0


def q_of(j, J):
    r = 1
    while J[r] < j:
        r += 1
    return r


def ceil_log2(x):
    return (x - 1).bit_length() if x >= 1 else 0


def main():
    import random
    from itertools import permutations
    J = jac(NMAX * 2 + 10)
    ok = True

    # ---- exhaustive n <= 9: measured worst over all permutations ----
    print("n | exhaustive-worst | identity | q-rec | max-dev")
    for n in range(2, 10):
        worst = 0
        for perm in permutations(range(n)):
            t = fj_actual(perm, J)
            if t > worst:
                worst = t
        ident = sum(ceil_log2_frac(3 * j) for j in range(1, n + 1))
        qrec = q_rec(n, J)
        flag = "OK" if worst == ident == qrec else "FAIL"
        ok = ok and (flag == "OK")
        print(f"{n} | {worst} | {ident} | {qrec} | {flag}")

    # ---- sampled worst n = 10..40 ----
    rng = random.Random(0)
    for n in range(10, NMAX + 1):
        worst = 0
        for _ in range(20000):
            perm = list(range(n))
            rng.shuffle(perm)
            t = fj_actual(perm, J)
            if t > worst:
                worst = t
        ident = sum(ceil_log2_frac(3 * j) for j in range(1, n + 1))
        qrec = q_rec(n, J)
        flag = "OK" if worst <= ident else "FAIL"
        ok = ok and (worst <= ident)
        eq = "EQ" if worst == ident else "lt"
        print(f"{n} | {worst} | {ident} | {qrec} | {flag} {eq}")

    print("ALL OK" if ok else "SOME FAILED")


def ceil_log2_frac(x4):
    """ceil(log2(x/4)) for integer x >= 4 (x = 3j)."""
    if x4 <= 4:
        return 0
    return (x4 - 1).bit_length() - 2


def q_rec(n, J):
    """T(n) = T(floor(n/2)) + floor(n/2) + sum_{j<=ceil(n/2)} (q(j)-1)."""
    T = [0] * (n + 1)
    for v in range(2, n + 1):
        m = (v + 1) // 2
        T[v] = T[v // 2] + v // 2 + sum(q_of(j, J) - 1 for j in range(1, m + 1))
    return T[n]


def fj_actual(perm, J):
    """True-comparison run of the copied algorithm; returns comparisons."""
    _out, _recs, t = fj_sort_instr(perm, J, "actual")
    return t


if __name__ == "__main__":
    raise SystemExit(main())
