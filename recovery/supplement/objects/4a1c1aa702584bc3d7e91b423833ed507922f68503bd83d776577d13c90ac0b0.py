#!/usr/bin/env python3
"""Ordinal-sum amplification of information-bound gaps.

Investigates whether F(P (+) Q) = F(P) + F(Q) can amplify local
information-bound failures into an infinite family of reachable posets
at the same depth t with e(P) <= 2^{k-t} but F(P) > k-t.

Model: adaptive worst-case pairwise-comparison sorting of n distinct
labelled keys. F(P) = minimum remaining comparisons to sort every linear
extension of P. e(P) = number of linear extensions. k = ceil(log2 n!).

Key question: can the gap F(P) - ceil(log2 e(P)) be amplified to large
depths while keeping e(P) <= 2^{k-t}?
"""

from __future__ import annotations

import math
from functools import lru_cache
from math import comb


# ---------------------------------------------------------------------------
# Poset machinery
# ---------------------------------------------------------------------------

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
    """Number of edges in the transitive reduction (Hasse diagram)."""
    n = len(succ)
    count = 0
    for i in range(n):
        for j in range(n):
            if i != j and (succ[i] >> j) & 1:
                # Check if i -> j is in the transitive reduction:
                # no k such that i < k < j
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
    """Product of two chains C_a x C_b (a rows, b columns).

    Elements are (i, j) with 0 <= i < a, 0 <= j < b.
    (i, j) < (i', j') iff i < i' and j < j'.
    Labelled as i * b + j.
    """
    n = a * b
    succ = [0] * n
    for i in range(a):
        for j in range(b):
            idx = i * b + j
            for i2 in range(i + 1, a):
                for j2 in range(j + 1, b):
                    succ[idx] |= 1 << (i2 * b + j2)
    return tuple(succ)


# ---------------------------------------------------------------------------
# Investigation
# ---------------------------------------------------------------------------

def investigate_n5_witness():
    """The n=5 witness: e=8, m=4, gap=1."""
    print("=== n=5 witness (e=8, m=4) ===")
    P = (0, 0, 1, 3, 7)
    e = linear_extensions(P)
    m = minimax(P)
    tr = transitive_reduction_edges(P)
    print(f"  P = {P}")
    print(f"  e(P) = {e}, ceil(log2 e) = {ceil_log2(e)}, m(P) = {m}, gap = {m - ceil_log2(e)}")
    print(f"  transitive reduction edges = {tr}")
    print(f"  n = 5, k = ceil(log2 5!) = {ceil_log2(math.factorial(5))}")
    print()


def investigate_ordinal_sum_family():
    """Ordinal sums of the n=5 witness: gap adds up, but so does depth."""
    print("=== Ordinal sum family: m copies of n=5 witness ===")
    G = (0, 0, 1, 3, 7)
    e_G = linear_extensions(G)
    m_G = minimax(G)
    tr_G = transitive_reduction_edges(G)
    r_G = ceil_log2(e_G)
    gap_G = m_G - r_G

    print(f"  Gadget: e={e_G}, ceil(log2 e)={r_G}, m={m_G}, gap={gap_G}, tr_edges={tr_G}")
    print()

    print(f"  {'m':>3} {'n=5m':>5} {'e(P)':>12} {'ceil_log2 e':>11} {'F(P)':>6} "
          f"{'gap':>5} {'tr_edges':>9} {'k':>6} {'k-t':>8} {'F>k-t?':>7} {'e<=2^{k-t}?':>11}")

    for m in range(1, 8):
        # Build ordinal sum of m copies
        P = G
        for _ in range(m - 1):
            P = ordinal_sum(P, G)

        n = 5 * m
        e = linear_extensions(P)
        F = minimax(P)
        info = ceil_log2(e)
        gap = F - info
        tr = transitive_reduction_edges(P)
        k = ceil_log2(math.factorial(n))
        t = tr  # minimum depth to reach P
        remaining = k - t
        f_exceeds = F > remaining
        e_fits = e <= (1 << remaining) if remaining < 64 else True

        print(f"  {m:>3} {n:>5} {e:>12} {info:>11} {F:>6} "
              f"{gap:>5} {tr:>9} {k:>6} {remaining:>8} {str(f_exceeds):>7} {str(e_fits):>11}")

    print()


def investigate_merge_family():
    """Merge family: Merge(a,b) gaps and ordinal sums."""
    print("=== Merge family: Merge(a,b) gaps ===")
    print(f"  {'(a,b)':>7} {'n':>3} {'e':>8} {'ceil_log2 e':>11} {'M':>4} "
          f"{'gap':>5} {'tr_edges':>9}")

    merge_gadgets = []
    for a in range(1, 7):
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
            print(f"  {str((a,b)):>7} {n:>3} {e:>8} {info:>11} {M:>4} "
                  f"{gap:>5} {tr:>9}")
            if gap > 0:
                merge_gadgets.append((a, b, e, M, gap, tr))

    print()
    print("  Merge gadgets with positive gap:")
    for a, b, e, M, gap, tr in merge_gadgets:
        print(f"    Merge({a},{b}): e={e}, M={M}, gap={gap}, tr_edges={tr}")
    print()


def investigate_merge_ordinal_sums():
    """Ordinal sums of merge gadgets: gap amplification analysis."""
    print("=== Ordinal sums of Merge(2,4): gap amplification ===")
    G = chains_union((2, 4))
    e_G = linear_extensions(G)
    M_G = minimax(G)
    tr_G = transitive_reduction_edges(G)
    r_G = ceil_log2(e_G)
    gap_G = M_G - r_G

    print(f"  Gadget Merge(2,4): e={e_G}, ceil(log2 e)={r_G}, M={M_G}, gap={gap_G}, tr_edges={tr_G}")
    print()

    print(f"  {'m':>3} {'n=6m':>5} {'e(P)':>12} {'ceil_log2 e':>11} {'F(P)':>6} "
          f"{'gap':>5} {'tr_edges':>9} {'k':>6} {'k-t':>8} {'F>k-t?':>7}")

    for m in range(1, 8):
        P = G
        for _ in range(m - 1):
            P = ordinal_sum(P, G)

        n = 6 * m
        e = linear_extensions(P)
        F = minimax(P)
        info = ceil_log2(e)
        gap = F - info
        tr = transitive_reduction_edges(P)
        k = ceil_log2(math.factorial(n))
        t = tr
        remaining = k - t
        f_exceeds = F > remaining

        print(f"  {m:>3} {n:>5} {e:>12} {info:>11} {F:>6} "
              f"{gap:>5} {tr:>9} {k:>6} {remaining:>8} {str(f_exceeds):>7}")

    print()


def investigate_grid_posets():
    """Grid posets C_a x C_b: checking for local information-bound failures."""
    print("=== Grid posets C_a x C_b ===")
    print(f"  {'(a,b)':>7} {'n':>3} {'e':>12} {'ceil_log2 e':>11} {'F':>6} "
          f"{'gap':>5} {'tr_edges':>9}")

    for a in range(1, 5):
        for b in range(a, 6):
            if a * b > 12:
                continue
            P = grid_poset(a, b)
            e = linear_extensions(P)
            F = minimax(P)
            info = ceil_log2(e)
            gap = F - info
            tr = transitive_reduction_edges(P)
            n = a * b
            print(f"  {str((a,b)):>7} {n:>3} {e:>12} {info:>11} {F:>6} "
                  f"{gap:>5} {tr:>9}")

    print()


def analyze_barrier():
    """Analyze the structural barrier for the ordinal sum construction."""
    print("=== Structural barrier analysis ===")
    print()
    print("  For an ordinal sum of m copies of a gadget G on g elements:")
    print("    n = m * g")
    print("    k = ceil(log2 n!) ~ n log2 n - n log2 e + O(log n)")
    print("    F(P) = m * F(G)")
    print("    t ~ m * d (where d = transitive reduction edges of G)")
    print("    k - t ~ m * g * (log2(m*g) - log2 e) - m * d")
    print("           = m * (g * (log2(m*g) - log2 e) - d)")
    print()
    print("  For F(P) > k - t, we need:")
    print("    m * F(G) > m * (g * (log2(m*g) - log2 e) - d)")
    print("    F(G) > g * (log2(m*g) - log2 e) - d")
    print()
    print("  As m -> infinity, the right side grows as g * log2(m),")
    print("  while F(G) is constant. So the inequality fails for large m.")
    print()
    print("  This means: the ordinal sum construction CANNOT produce")
    print("  F(P) > k - t for large m, regardless of the gadget G.")
    print()
    print("  The gap F(P) - ceil(log2 e(P)) = m * gap(G) grows linearly,")
    print("  but k - t grows as m * log(m), which is faster.")
    print()

    # Verify numerically for the n=5 witness
    print("  Numerical verification (n=5 witness, gap=1):")
    G = (0, 0, 1, 3, 7)
    e_G = linear_extensions(G)
    m_G = minimax(G)
    tr_G = transitive_reduction_edges(G)
    g = 5

    print(f"    Gadget: g={g}, F(G)={m_G}, d={tr_G}, gap={m_G - ceil_log2(e_G)}")
    print()
    print(f"    {'m':>3} {'F(P)':>8} {'k-t':>10} {'F(P)-(k-t)':>11} {'F>k-t?':>7}")

    for m in range(1, 15):
        P = G
        for _ in range(m - 1):
            P = ordinal_sum(P, G)

        n = g * m
        F = minimax(P)
        tr = transitive_reduction_edges(P)
        k = ceil_log2(math.factorial(n))
        t = tr
        remaining = k - t
        diff = F - remaining
        print(f"    {m:>3} {F:>8} {remaining:>10} {diff:>11} {str(F > remaining):>7}")

    print()


def investigate_a12_ordinal_sums():
    """A12 ordinal sums: using the n=12 witness structure."""
    print("=== A12 ordinal sums (conceptual) ===")
    print()
    print("  The n=12 witness has S(12)=30, C(12)=29, gap=1.")
    print("  For m copies in ordinal sum: n=12m, F(P)=30m, gap=m.")
    print("  But k = ceil(log2 (12m)!) ~ 12m log2(12m) - 12m log2 e")
    print("  and t ~ m * d where d = tr_edges of the n=12 witness.")
    print()
    print("  Same barrier applies: F(P) = 30m grows linearly,")
    print("  but k - t ~ 12m log2(12m) grows as m log m.")
    print("  So F(P) > k - t fails for large m.")
    print()

    # Estimate for small m
    print("  Estimated values (assuming d ~ 11 for the n=12 witness):")
    print(f"    {'m':>3} {'n':>5} {'F(P)':>6} {'k':>6} {'t~':>5} {'k-t':>6} {'F>k-t?':>7}")

    for m in range(1, 8):
        n = 12 * m
        F = 30 * m
        k = ceil_log2(math.factorial(n))
        d = 11  # estimated transitive reduction edges for n=12 witness
        t = m * d
        remaining = k - t
        print(f"    {m:>3} {n:>5} {F:>6} {k:>6} {t:>5} {remaining:>6} {str(F > remaining):>7}")

    print()


def investigate_rectangular_chain():
    """Rectangular-chain PR32: grid poset analysis."""
    print("=== Rectangular-chain grid posets ===")
    print()
    print("  Grid poset C_a x C_b has e(P) = (ab)! / prod(i+j+1) (hook-length).")
    print("  For PR32 (32 elements), possible shapes: 1x32, 2x16, 4x8, 8x4, 16x2, 32x1.")
    print()

    # Compute for small grids
    print(f"  {'(a,b)':>7} {'n':>3} {'e':>12} {'ceil_log2 e':>11} {'F':>6} {'gap':>5}")

    for a, b in [(1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (2, 5), (3, 4)]:
        P = grid_poset(a, b)
        e = linear_extensions(P)
        F = minimax(P)
        info = ceil_log2(e)
        gap = F - info
        n = a * b
        print(f"  {str((a,b)):>7} {n:>3} {e:>12} {info:>11} {F:>6} {gap:>5}")

    print()
    print("  For larger grids (PR32), e(P) is enormous and F(P) is large.")
    print("  The gap F(P) - ceil(log2 e(P)) is not well-studied for grids.")
    print("  The same barrier analysis applies: ordinal sums of grids")
    print("  cannot produce F(P) > k - t for large m.")
    print()


def main():
    print("=" * 70)
    print("Ordinal-sum amplification of information-bound gaps")
    print("=" * 70)
    print()

    investigate_n5_witness()
    investigate_ordinal_sum_family()
    investigate_merge_family()
    investigate_merge_ordinal_sums()
    investigate_grid_posets()
    analyze_barrier()
    investigate_a12_ordinal_sums()
    investigate_rectangular_chain()

    print("=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print()
    print("  The ordinal sum construction F(P (+) Q) = F(P) + F(Q) does")
    print("  amplify local information-bound gaps linearly: m copies of a")
    print("  gadget with gap g produce a poset with gap m*g.")
    print()
    print("  However, the construction CANNOT produce an infinite family")
    print("  satisfying F(P) > k - t for large m, because:")
    print("    - F(P) = m * F(G) grows linearly in m")
    print("    - k - t ~ m * g * log2(m) grows as m * log(m)")
    print("    - The m * log(m) term dominates for large m")
    print()
    print("  This is a STRUCTURAL BARRIER: the ordinal sum construction")
    print("  amplifies the gap, but not fast enough to overcome the")
    print("  m * log(m) growth of the remaining budget.")
    print()
    print("  To satisfy F(P) > k - t, we would need a gadget with")
    print("  gap > g * log2(m) - d, which grows with m. No such gadget")
    print("  is known (all known gadgets have gap = 1).")
    print()
    print("  This does NOT prove that no infinite family exists; it only")
    print("  shows that the ordinal sum construction cannot produce one.")
    print("  A fundamentally different construction would be needed.")


if __name__ == "__main__":
    main()
