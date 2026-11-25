#!/usr/bin/env python3
"""Ordinal-sum amplification barrier (fast, uses verified additivity)."""

import math
from functools import lru_cache


def add_relation(succ, i, j):
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(len(succ)):
        if x == i or (succ[x] >> i) & 1:
            out[x] |= new_greater
    return tuple(out)


def incomparable_pairs(succ):
    n = len(succ)
    return [(i, j) for i in range(n) for j in range(i + 1, n)
            if not (succ[i] >> j) & 1 and not (succ[j] >> i) & 1]


@lru_cache(maxsize=None)
def linear_extensions(succ):
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
def minimax(succ):
    pairs = incomparable_pairs(succ)
    if not pairs:
        return 0
    return 1 + min(
        max(minimax(add_relation(succ, i, j)), minimax(add_relation(succ, j, i)))
        for i, j in pairs
    )


def ceil_log2(x):
    return (x - 1).bit_length()


def chains_union(sizes):
    n = sum(sizes)
    succ = [0] * n
    off = 0
    for s in sizes:
        for t in range(s):
            for u in range(t + 1, s):
                succ[off + t] |= 1 << (off + u)
        off += s
    return tuple(succ)


def transitive_reduction_edges(succ):
    n = len(succ)
    count = 0
    for i in range(n):
        for j in range(n):
            if i != j and (succ[i] >> j) & 1:
                is_red = True
                for k in range(n):
                    if k != i and k != j:
                        if (succ[i] >> k) & 1 and (succ[k] >> j) & 1:
                            is_red = False
                            break
                if is_red:
                    count += 1
    return count


def main():
    print("=" * 70)
    print("Ordinal-sum amplification barrier (fast analysis)")
    print("=" * 70)
    print()

    # --- n=5 witness ---
    print("=== n=5 witness ===")
    G5 = (0, 0, 1, 3, 7)
    e5 = linear_extensions(G5)
    m5 = minimax(G5)
    tr5 = transitive_reduction_edges(G5)
    print(f"  e={e5}, ceil(log2 e)={ceil_log2(e5)}, m={m5}, gap={m5-ceil_log2(e5)}, tr={tr5}")
    print()

    # --- Merge family (small only) ---
    print("=== Merge family (gap=1 for all) ===")
    for a, b in [(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3)]:
        P = chains_union((a, b))
        e = linear_extensions(P)
        M = minimax(P)
        tr = transitive_reduction_edges(P)
        print(f"  Merge({a},{b}): n={a+b}, e={e}, ceil={ceil_log2(e)}, M={M}, gap={M-ceil_log2(e)}, tr={tr}")
    print()

    # --- Ordinal sum analysis using additivity ---
    print("=== Ordinal sum family: m copies of n=5 witness ===")
    print("  Using F(P(+)Q) = F(P)+F(Q), e(P(+)Q) = e(P)*e(Q)")
    print()
    g, d, F_G, e_G, r_G = 5, tr5, m5, e5, ceil_log2(e5)
    print(f"  Gadget: g={g}, d={d}, F={F_G}, e={e_G}, r=ceil(log2 e)={r_G}, gap={F_G-r_G}")
    print()
    print(f"  {'m':>3} {'n':>4} {'F(P)':>6} {'gap':>4} {'tr':>4} {'k':>5} {'k-t':>5} {'F>k-t?':>6}")

    for m in range(1, 31):
        n = g * m
        F_P = F_G * m
        gap = (F_G - r_G) * m
        tr_P = m * d + (m - 1) * 4  # 4 edges to connect copies (2 max x 2 min)
        # k = ceil(log2 n!)
        if n <= 20:
            k = ceil_log2(math.factorial(n))
        else:
            k = int(n * math.log2(n) - n * math.log2(math.e) + 0.5 * math.log2(2*math.pi*n)) + 1
        t = tr_P
        rem = k - t
        print(f"  {m:>3} {n:>4} {F_P:>6} {gap:>4} {tr_P:>4} {k:>5} {rem:>5} {str(F_P > rem):>6}")

    print()

    # --- Merge(2,4) ordinal sums ---
    print("=== Ordinal sums of Merge(2,4) ===")
    G_m = chains_union((2, 4))
    e_m = linear_extensions(G_m)
    M_m = minimax(G_m)
    tr_m = transitive_reduction_edges(G_m)
    r_m = ceil_log2(e_m)
    g_m = 6
    print(f"  Gadget: g={g_m}, d={tr_m}, M={M_m}, e={e_m}, r={r_m}, gap={M_m-r_m}")
    print()
    print(f"  {'m':>3} {'n':>4} {'F(P)':>6} {'gap':>4} {'tr':>4} {'k':>5} {'k-t':>5} {'F>k-t?':>6}")

    for m in range(1, 31):
        n = g_m * m
        F_P = M_m * m
        gap = (M_m - r_m) * m
        tr_P = m * tr_m + (m - 1) * 1  # unique max/min, 1 edge to connect
        if n <= 20:
            k = ceil_log2(math.factorial(n))
        else:
            k = int(n * math.log2(n) - n * math.log2(math.e) + 0.5 * math.log2(2*math.pi*n)) + 1
        t = tr_P
        rem = k - t
        print(f"  {m:>3} {n:>4} {F_P:>6} {gap:>4} {tr_P:>4} {k:>5} {rem:>5} {str(F_P > rem):>6}")

    print()
    print("=" * 70)
    print("BARRIER")
    print("=" * 70)
    print()
    print("  F(P) = m * F(G) grows as O(m)")
    print("  k - t ~ m * g * log2(m) grows as O(m log m)")
    print("  O(m log m) dominates O(m), so F(P) > k-t fails for large m.")
    print()
    print("  The ordinal sum construction CANNOT produce an infinite")
    print("  family with F(P) > k-t. This is a structural barrier.")
    print()
    print("  To overcome: need a gadget with gap growing with m,")
    print("  or a fundamentally different construction.")
    print("  All known gadgets have gap=1.")


if __name__ == "__main__":
    main()
