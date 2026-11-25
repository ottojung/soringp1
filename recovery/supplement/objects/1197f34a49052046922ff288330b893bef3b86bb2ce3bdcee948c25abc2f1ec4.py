#!/usr/bin/env python3
"""Ordinal-sum amplification barrier analysis (optimized).

Uses the verified additivity F(P (+) Q) = F(P) + F(Q) to avoid
recomputing minimax for large ordinal sums.
"""

from __future__ import annotations

import math
from functools import lru_cache
from math import comb


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


@lru_cache(maxsize=None)
def minimax(succ: tuple[int, ...]) -> int:
    pairs = incomparable_pairs(succ)
    if not pairs:
        return 0
    return 1 + min(
        max(minimax(add_relation(succ, i, j)), minimax(add_relation(succ, j, i)))
        for i, j in pairs
    )


def ceil_log2(x: int) -> int:
    return (x - 1).bit_length()


def ordinal_sum(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    a = len(p)
    top_mask = ((1 << (a + len(q))) - 1) ^ ((1 << a) - 1)
    return tuple(s | top_mask for s in p) + tuple(s << a for s in q)


def chains_union(sizes) -> tuple[int, ...]:
    n = sum(sizes)
    succ = [0] * n
    off = 0
    for s in sizes:
        for t in range(s):
            for u in range(t + 1, s):
                succ[off + t] |= 1 << (off + u)
        off += s
    return tuple(succ)


def transitive_reduction_edges(succ: tuple[int, ...]) -> int:
    n = len(succ)
    count = 0
    for i in range(n):
        for j in range(n):
            if i != j and (succ[i] >> j) & 1:
                is_reduction = True
                for k in range(n):
                    if k != i and k != j:
                        if (succ[i] >> k) & 1 and (succ[k] >> j) & 1:
                            is_reduction = False
                            break
                if is_reduction:
                    count += 1
    return count


def grid_poset(a: int, b: int) -> tuple[int, ...]:
    n = a * b
    succ = [0] * n
    for i in range(a):
        for j in range(b):
            idx = i * b + j
            for i2 in range(i + 1, a):
                for j2 in range(j + 1, b):
                    succ[idx] |= 1 << (i2 * b + j2)
    return tuple(succ)


def main():
    print("=" * 70)
    print("Ordinal-sum amplification barrier analysis")
    print("=" * 70)
    print()

    # --- n=5 witness ---
    print("=== n=5 witness (e=8, m=4) ===")
    G5 = (0, 0, 1, 3, 7)
    e5 = linear_extensions(G5)
    m5 = minimax(G5)
    tr5 = transitive_reduction_edges(G5)
    print(f"  G = {G5}")
    print(f"  e(G) = {e5}, ceil(log2 e) = {ceil_log2(e5)}, m(G) = {m5}, gap = {m5 - ceil_log2(e5)}")
    print(f"  transitive reduction edges = {tr5}")
    print()

    # --- Merge family ---
    print("=== Merge family gaps ===")
    print(f"  {'(a,b)':>7} {'n':>3} {'e':>8} {'ceil_log2 e':>11} {'M':>4} {'gap':>5} {'tr':>4}")

    merge_gadgets = []
    for a in range(1, 6):
        for b in range(a, 7):
            if a + b > 8:
                continue
            P = chains_union((a, b))
            e = linear_extensions(P)
            M = minimax(P)
            info = ceil_log2(e)
            gap = M - info
            tr = transitive_reduction_edges(P)
            n = a + b
            print(f"  {str((a,b)):>7} {n:>3} {e:>8} {info:>11} {M:>4} {gap:>5} {tr:>4}")
            if gap > 0:
                merge_gadgets.append((a, b, e, M, gap, tr))
    print()

    # --- Ordinal sum family (using additivity) ---
    print("=== Ordinal sum family: m copies of n=5 witness ===")
    print("  Using F(P (+) Q) = F(P) + F(Q) to avoid recomputation.")
    print()
    print(f"  {'m':>3} {'n=5m':>5} {'e(P)=8^m':>12} {'ceil_log2 e':>11} {'F(P)=4m':>8} "
          f"{'gap':>5} {'tr':>5} {'k':>6} {'k-t':>8} {'F>k-t?':>7}")

    g = 5
    d = tr5
    F_G = m5
    e_G = e5
    r_G = ceil_log2(e_G)

    for m in range(1, 21):
        n = g * m
        e_P = e_G ** m
        F_P = F_G * m
        info_P = ceil_log2(e_P) if e_P < 2**63 else m * r_G
        gap = F_P - info_P
        # Transitive reduction: m copies of G plus (m-1) connecting edges
        # Each copy has tr5 edges; connecting two copies requires
        # edges from max of first to min of second.
        # For the n=5 witness, max elements are {0,1}, min elements are {3,4}.
        # Connecting requires 2*2=4 edges (but some may be implied).
        # Conservative estimate: tr5 per copy + 1 per connection.
        tr_P = m * tr5 + (m - 1) * 4  # upper bound
        k = ceil_log2(math.factorial(n)) if n <= 20 else None
        if k is not None:
            t = tr_P
            remaining = k - t
            f_exceeds = F_P > remaining
            print(f"  {m:>3} {n:>5} {e_P:>12} {info_P:>11} {F_P:>8} "
                  f"{gap:>5} {tr_P:>5} {k:>6} {remaining:>8} {str(f_exceeds):>7}")
        else:
            # Estimate k using Stirling
            k_est = int(n * math.log2(n) - n * math.log2(math.e) + 0.5 * math.log2(2 * math.pi * n)) + 1
            t = tr_P
            remaining = k_est - t
            f_exceeds = F_P > remaining
            print(f"  {m:>3} {n:>5} {e_P:>12} {info_P:>11} {F_P:>8} "
                  f"{gap:>5} {tr_P:>5} {'~'+str(k_est):>6} {remaining:>8} {str(f_exceeds):>7}")

    print()

    # --- Merge(2,4) ordinal sums ---
    print("=== Ordinal sums of Merge(2,4) ===")
    G_m = chains_union((2, 4))
    e_m = linear_extensions(G_m)
    M_m = minimax(G_m)
    tr_m = transitive_reduction_edges(G_m)
    r_m = ceil_log2(e_m)
    g_m = 6

    print(f"  Gadget Merge(2,4): e={e_m}, ceil(log2 e)={r_m}, M={M_m}, gap={M_m - r_m}, tr={tr_m}")
    print()
    print(f"  {'m':>3} {'n=6m':>5} {'F(P)=5m':>8} {'gap':>5} {'tr':>5} {'k':>6} {'k-t':>8} {'F>k-t?':>7}")

    for m in range(1, 21):
        n = g_m * m
        F_P = M_m * m
        gap = (M_m - r_m) * m
        tr_P = m * tr_m + (m - 1) * 1  # Merge(2,4) has unique max and min
        k = ceil_log2(math.factorial(n)) if n <= 20 else None
        if k is not None:
            t = tr_P
            remaining = k - t
            f_exceeds = F_P > remaining
            print(f"  {m:>3} {n:>5} {F_P:>8} {gap:>5} {tr_P:>5} {k:>6} {remaining:>8} {str(f_exceeds):>7}")
        else:
            k_est = int(n * math.log2(n) - n * math.log2(math.e) + 0.5 * math.log2(2 * math.pi * n)) + 1
            t = tr_P
            remaining = k_est - t
            f_exceeds = F_P > remaining
            print(f"  {m:>3} {n:>5} {F_P:>8} {gap:>5} {tr_P:>5} {'~'+str(k_est):>6} {remaining:>8} {str(f_exceeds):>7}")

    print()

    # --- Grid posets ---
    print("=== Grid posets C_a x C_b ===")
    print(f"  {'(a,b)':>7} {'n':>3} {'e':>12} {'ceil_log2 e':>11} {'F':>6} {'gap':>5}")

    for a, b in [(1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (2, 5)]:
        P = grid_poset(a, b)
        e = linear_extensions(P)
        F = minimax(P)
        info = ceil_log2(e)
        gap = F - info
        n = a * b
        print(f"  {str((a,b)):>7} {n:>3} {e:>12} {info:>11} {F:>6} {gap:>5}")

    print()

    # --- Barrier analysis ---
    print("=" * 70)
    print("STRUCTURAL BARRIER")
    print("=" * 70)
    print()
    print("  For an ordinal sum of m copies of a gadget G on g elements:")
    print()
    print("    n = m * g")
    print("    k = ceil(log2 n!) ~ n log2 n - n log2 e + O(log n)")
    print("    F(P) = m * F(G)")
    print("    t ~ m * d (d = transitive reduction edges per copy)")
    print()
    print("    k - t ~ m * g * (log2(m*g) - log2 e) - m * d")
    print("           = m * (g * (log2(m*g) - log2 e) - d)")
    print()
    print("  For F(P) > k - t:")
    print("    m * F(G) > m * (g * (log2(m*g) - log2 e) - d)")
    print("    F(G) > g * (log2(m*g) - log2 e) - d")
    print()
    print("  As m -> infinity:")
    print("    LHS = F(G) = constant")
    print("    RHS ~ g * log2(m) -> infinity")
    print()
    print("  Therefore, for sufficiently large m, F(P) <= k - t.")
    print("  The ordinal sum construction CANNOT produce F(P) > k - t")
    print("  for large m, regardless of the gadget G.")
    print()
    print("  This is a STRUCTURAL BARRIER for the ordinal sum approach.")
    print()
    print("  Key insight: the gap grows as O(m) but the remaining budget")
    print("  grows as O(m log m). The m log m term dominates.")
    print()
    print("  To overcome this barrier, we would need:")
    print("    1. A gadget with gap > g * log2(m) - d (grows with m), OR")
    print("    2. A fundamentally different construction that doesn't")
    print("       rely on ordinal sums")
    print()
    print("  All known gadgets (n=5 witness, merge family) have gap = 1.")
    print("  No gadget with gap > 1 is known.")
    print()
    print("  This does NOT prove that no infinite family exists; it only")
    print("  shows that the ordinal sum construction cannot produce one.")


if __name__ == "__main__":
    main()
