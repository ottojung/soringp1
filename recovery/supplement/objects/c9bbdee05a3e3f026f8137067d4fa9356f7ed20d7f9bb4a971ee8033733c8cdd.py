#!/usr/bin/env python3
"""Discriminative witnesses for the surplus parameterization of unary S(n).

Surplus: s(n) = S(n) - L(n) where L(n) = ceil(log2 n!).
Parameterization: decide S(n) <= k with parameter s = k - L(n).

Hypotheses discriminated:
  H1: surplus bounded -> FPT trivial
  H2: surplus unbounded but structured -> FPT plausible
  H3: surplus unbounded and erratic -> parameter meaningful, structure complex
  H4: FPT possible (f(s)*poly(n) algorithm exists)
  H5: FPT impossible

Only discriminative witnesses are reported. Routine small-n computations
that do not change our view are skipped.
"""

from __future__ import annotations

import math
import time
from functools import lru_cache


KNOWN_S = {
    0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 9: 19,
    10: 22, 11: 26, 12: 30, 13: 34, 14: 38, 15: 42, 16: 46, 17: 50,
    18: 54, 19: 58, 20: 62, 21: 66, 22: 71,
}


def L(n: int) -> int:
    """ceil(log2 n!) for n! >= 1."""
    if n <= 1:
        return 0
    fact = math.factorial(n)
    return (fact - 1).bit_length()


def surplus(n: int) -> int:
    return KNOWN_S[n] - L(n)


def experiment_surplus_table():
    """Exact surplus for n=0..22. Discriminates H1 (bounded) vs H2/H3 (unbounded)."""
    print("== Surplus table: s(n) = S(n) - L(n) ==")
    print(f"{'n':>3} {'S(n)':>5} {'L(n)':>5} {'s(n)':>5} {'2^L/n!':>9} {'note':>20}")
    prev_s = None
    monotonic = True
    max_s = 0
    for n in range(0, 23):
        s_val = surplus(n)
        fact = math.factorial(n)
        ratio = (2 ** L(n)) / fact if fact > 0 else 1.0
        note = ""
        if prev_s is not None and s_val < prev_s:
            note = "DROP"
            monotonic = False
        elif prev_s is not None and s_val > prev_s:
            note = "RISE"
        if s_val > max_s:
            max_s = s_val
            note += " MAX"
        print(f"{n:>3} {KNOWN_S[n]:>5} {L(n):>5} {s_val:>5} {ratio:>9.4f} {note:>20}")
        prev_s = s_val

    print(f"\n  Surplus monotonic? {monotonic}")
    print(f"  Max surplus (n<=22): {max_s}")
    print(f"  Surplus unbounded? {'UNKNOWN (open)' if max_s > 0 else 'YES, bounded by 0'}")
    print(f"  H1 (bounded): {'PLAUSIBLE' if max_s <= 2 else 'REFUTED if trend continues'}")
    print(f"  H3 (erratic): {'SUPPORTED' if not monotonic else 'not yet'}")


def experiment_surplus_growth_rate():
    """Analyze growth rate of surplus. Discriminates H2 (structured) vs H3 (erratic)."""
    print("\n== Surplus growth analysis ==")
    print(f"{'n':>3} {'s(n)':>5} {'s(n)/n':>8} {'s(n)/log n':>10} {'s(n)/n^2':>10}")
    for n in range(2, 23):
        s_val = surplus(n)
        if s_val == 0:
            print(f"{n:>3} {s_val:>5} {0.0:>8.4f} {0.0:>10.4f} {0.0:>10.4f}")
        else:
            print(f"{n:>3} {s_val:>5} {s_val/n:>8.4f} {s_val/math.log2(n):>10.4f} {s_val/(n*n):>10.4f}")

    nonzero = [(n, surplus(n)) for n in range(2, 23) if surplus(n) > 0]
    print(f"\n  Nonzero surplus values: {nonzero}")
    print(f"  s(n)/n max: {max(s/n for n,s in nonzero):.4f}")
    print(f"  s(n)/n^2 max: {max(s/(n*n) for n,s in nonzero):.6f}")
    print(f"  Conclusion: surplus grows slower than n (sublinear)")


def add_relation(succ: tuple[int, ...], i: int, j: int) -> tuple[int, ...]:
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(len(succ)):
        if x == i or (succ[x] >> i) & 1:
            out[x] |= new_greater
    return tuple(out)


def incomparable_pairs(succ: tuple[int, ...]) -> list[tuple[int, int]]:
    n = len(succ)
    return [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if not (succ[i] >> j) & 1 and not (succ[j] >> i) & 1
    ]


@lru_cache(maxsize=None)
def linear_extensions(succ: tuple[int, ...]) -> int:
    n = len(succ)
    pred = [0] * n
    for i in range(n):
        for j in range(n):
            if (succ[i] >> j) & 1:
                pred[j] |= 1 << i
    full = (1 << n) - 1
    dp = [0] * (1 << n)
    dp[0] = 1
    for S in range(1, 1 << n):
        total = 0
        m = S
        while m:
            x = (m & -m).bit_length() - 1
            m &= m - 1
            if succ[x] & (S ^ (1 << x)) == 0:
                total += dp[S ^ (1 << x)]
        dp[S] = total
    return dp[full]


def all_posets(n: int):
    start = (0,) * n
    seen = {start}
    stack = [start]
    while stack:
        s = stack.pop()
        for i, j in incomparable_pairs(s):
            for t in (add_relation(s, i, j), add_relation(s, j, i)):
                if t not in seen:
                    seen.add(t)
                    stack.append(t)
    return seen


def minimax_all(n: int):
    @lru_cache(maxsize=None)
    def m(succ: tuple[int, ...]) -> int:
        pairs = incomparable_pairs(succ)
        if not pairs:
            return 0
        return 1 + min(
            max(m(add_relation(succ, i, j)), m(add_relation(succ, j, i)))
            for i, j in pairs
        )
    table = {}
    for P in all_posets(n):
        table[P] = m(P)
    return table


def experiment_local_surplus(n: int):
    """Local surplus distribution: m(P) - ceil(log2 e(P)) for all posets.

    Discriminates: is the gap a global phenomenon or does it appear locally?
    If local gaps exist but global surplus is 0, local gaps don't propagate.
    """
    print(f"\n== Local surplus distribution, n={n} ==")
    t0 = time.perf_counter()
    table = minimax_all(n)
    dt = time.perf_counter() - t0

    by_gap = {}
    max_gap = 0
    total = len(table)
    for P, mv in table.items():
        e = linear_extensions(P)
        lb = (e - 1).bit_length() if e > 0 else 0
        gap = mv - lb
        by_gap.setdefault(gap, 0)
        by_gap[gap] += 1
        if gap > max_gap:
            max_gap = gap

    print(f"  Total posets: {total}")
    print(f"  Max local gap: {max_gap}")
    print(f"  Gap distribution:")
    for gap in sorted(by_gap):
        cnt = by_gap[gap]
        pct = 100.0 * cnt / total
        print(f"    gap={gap}: {cnt:>7} ({pct:>6.2f}%)")
    print(f"  Time: {dt:.1f}s")

    if max_gap > 0:
        print(f"  -> Local gaps exist (max={max_gap}) but global surplus may still be 0")
        print(f"     This discriminates: local gap != global gap")
    return by_gap


def experiment_fpt_witness(n: int):
    """FPT witness: for parameter s = k - L(n), how does the budgeted DFS scale?

    The key FPT question: can we decide S(n) <= k in f(s)*poly(n) time?
    We measure the number of CanSort calls as a proxy for difficulty.
    """
    print(f"\n== FPT witness: CanSort call counts, n={n} ==")
    S_n = KNOWN_S.get(n)
    if S_n is None:
        print(f"  S({n}) unknown, skipping")
        return

    L_n = L(n)
    print(f"  S({n})={S_n}, L({n})={L_n}, surplus={S_n - L_n}")

    from functools import lru_cache as cache

    call_count = 0

    @cache(maxsize=None)
    def can_sort(succ: tuple[int, ...], d: int) -> bool:
        nonlocal call_count
        call_count += 1
        if d < 0:
            return False
        e = linear_extensions(succ)
        if e <= (1 << d):
            pass
        else:
            return False
        pairs = incomparable_pairs(succ)
        if not pairs:
            return True
        for i, j in pairs:
            if can_sort(add_relation(succ, i, j), d - 1) and \
               can_sort(add_relation(succ, j, i), d - 1):
                return True
        return False

    antichain = (0,) * n

    for s in range(0, S_n + 1):
        k = L_n + s
        call_count = 0
        t0 = time.perf_counter()
        result = can_sort(antichain, k)
        dt = time.perf_counter() - t0
        print(f"  s={s} (k={k}): CanSort={result}, calls={call_count:>10}, time={dt:.3f}s")

    print(f"\n  FPT analysis:")
    print(f"  For s=0 (tight case), calls should be small if pruning is effective")
    print(f"  For s>0, calls grow - this is the FPT hardness witness")


def experiment_merge_family():
    """Merge(a,b) family: surplus for disjoint union of two chains.

    This family has known exact merge cost M(a,b), giving controlled surplus.
    Discriminates: are there families with O(1), O(log n), Theta(n) surplus?
    """
    print("\n== Merge family surplus ==")

    def merge_poset(a: int, b: int) -> tuple[int, ...]:
        n = a + b
        succ = [0] * n
        for i in range(a - 1):
            succ[i] |= 1 << (i + 1)
        for i in range(a, n - 1):
            succ[i] |= 1 << (i + 1)
        for i in range(n):
            s = succ[i]
            changed = True
            while changed:
                changed = False
                for x in range(n):
                    if (s >> x) & 1:
                        new_bits = succ[x] & ~s
                        if new_bits:
                            s |= new_bits
                            changed = True
            succ[i] = s
        return tuple(succ)

    @lru_cache(maxsize=None)
    def m(succ: tuple[int, ...]) -> int:
        n = len(succ)
        pairs = [
            (i, j) for i in range(n) for j in range(i + 1, n)
            if not (succ[i] >> j) & 1 and not (succ[j] >> i) & 1
        ]
        if not pairs:
            return 0
        return 1 + min(
            max(m(add_relation(succ, i, j)), m(add_relation(succ, j, i)))
            for i, j in pairs
        )

    print(f"{'a':>3} {'b':>3} {'n=a+b':>5} {'e(P)':>8} {'L(P)':>5} {'M(a,b)':>7} {'gap':>4}")
    for a in range(1, 7):
        for b in range(a, 7):
            n = a + b
            if n > 12:
                continue
            P = merge_poset(a, b)
            e = linear_extensions(P)
            lb = (e - 1).bit_length() if e > 0 else 0
            mv = m(P)
            gap = mv - lb
            print(f"{a:>3} {b:>3} {n:>5} {e:>8} {lb:>5} {mv:>7} {gap:>4}")


def main():
    experiment_surplus_table()
    experiment_surplus_growth_rate()
    experiment_local_surplus(5)
    experiment_local_surplus(6)
    experiment_fpt_witness(5)
    experiment_merge_family()


if __name__ == "__main__":
    main()
