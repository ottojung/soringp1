#!/usr/bin/env python3
"""Verify the rectangular-chain winning frontier construction.

From docs/research-winning-frontier-barrier.md:
- s columns, L levels, n = sL
- Each column is a chain of length L (s disjoint chains)
- Additional forward edges between adjacent levels
- All constructed states are winning: F(P) <= B = (s-1) + (n-1) ceil(log2 s)
- Count of nonisomorphic winning states: 2^((1/4-o(1)) n (log n)^2)

This script verifies the construction for small parameters and checks
whether it can be modified to produce losing states (F(P) > k-t).
"""

import math
from functools import lru_cache
from math import comb


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


def build_rectangular_chain(s, L, extra_edges):
    """Build a rectangular-chain poset.

    s columns, L levels, n = sL.
    Element (i, x) is labelled i * s + x (level i, column x).
    Each column is a chain: (0,x) < (1,x) < ... < (L-1,x).
    extra_edges: list of ((i,x), (i+1,y)) with x != y.
    """
    n = s * L
    succ = [0] * n

    # Column chains
    for x in range(s):
        for i in range(L - 1):
            succ[i * s + x] |= 1 << ((i + 1) * s + x)

    # Extra forward edges
    for (i, x), (i2, y) in extra_edges:
        assert i2 == i + 1 and x != y
        succ[i * s + x] |= 1 << (i2 * s + y)

    # Transitive closure
    changed = True
    while changed:
        changed = False
        for a in range(n):
            for b in range(n):
                if (succ[a] >> b) & 1:
                    new_bits = succ[b] & ~succ[a]
                    if new_bits:
                        succ[a] |= new_bits
                        changed = True

    return tuple(succ)


def verify_small():
    """Verify the construction for small s, L."""
    print("=== Rectangular-chain construction (small verification) ===")
    print()

    for s, L in [(2, 2), (2, 3), (3, 2), (3, 3)]:
        n = s * L
        t0 = s * (L - 1)  # initial chain edges
        B = (s - 1) + (n - 1) * ceil_log2(s)
        k = ceil_log2(math.factorial(n))

        # Build base poset (no extra edges)
        base = build_rectangular_chain(s, L, [])
        e_base = linear_extensions(base)
        F_base = minimax(base)

        print(f"  s={s}, L={L}, n={n}:")
        print(f"    t0={t0}, B={B}, k={k}, k-t0={k-t0}")
        print(f"    Base: e={e_base}, F={F_base}, F<=B? {F_base <= B}")
        print(f"    F <= k-t0? {F_base <= k - t0}")
        print()

        # Add one extra edge
        if L >= 2 and s >= 2:
            extra = [((0, 0), (1, 1))]
            P = build_rectangular_chain(s, L, extra)
            e_P = linear_extensions(P)
            F_P = minimax(P)
            t = t0 + 1
            print(f"    With 1 extra edge: t={t}, e={e_P}, F={F_P}")
            print(f"      F <= k-t? {F_P <= k - t}")
            print(f"      e <= 2^(k-t)? {e_P <= 2**(k-t) if k-t < 63 else 'N/A'}")
            print()


def analyze_losing_state_possibility():
    """Can the rectangular-chain construction produce losing states?"""
    print("=== Can rectangular-chain produce losing states? ===")
    print()
    print("  The construction gives F(P) <= B = (s-1) + (n-1) ceil(log2 s).")
    print("  For losing states, we need F(P) > k - t.")
    print()
    print("  With t = t0 + m (m extra edges), k - t = k - t0 - m.")
    print("  For F(P) > k - t, we need B > k - t0 - m, i.e., m > k - t0 - B.")
    print()
    print("  But the construction requires m <= k - t0 - B (so that F(P) <= k-t).")
    print("  So the construction CANNOT produce losing states by design.")
    print()
    print("  To produce losing states, we would need to add edges that increase")
    print("  F(P) beyond B. This requires adding edges that create incomparable")
    print("  pairs, which would also increase e(P).")
    print()
    print("  The question is: can we add edges such that:")
    print("    - F(P) > k - t (losing)")
    print("    - e(P) <= 2^{k-t} (information bound satisfied)")
    print()
    print("  This is exactly the local information-bound failure question.")
    print("  The rectangular-chain construction does NOT address this.")
    print()


def analyze_ordinal_sum_vs_rectangular():
    """Compare ordinal sum and rectangular-chain approaches."""
    print("=== Ordinal sum vs rectangular-chain: complementary barriers ===")
    print()
    print("  Ordinal sum of m copies of a gadget G:")
    print("    F(P) = m * F(G) = O(m)")
    print("    t = O(m) (linear in m)")
    print("    k - t = O(m log m) (grows faster than F(P))")
    print("    => F(P) > k-t fails for large m")
    print()
    print("  Rectangular-chain construction:")
    print("    F(P) <= B = O(n log s) (small)")
    print("    t = t0 + m (can be large)")
    print("    k - t = k - t0 - m (small when m is large)")
    print("    => F(P) <= k-t holds (winning states)")
    print()
    print("  These are COMPLEMENTARY:")
    print("    - Ordinal sum: losing states at shallow depth (k-t large)")
    print("    - Rectangular-chain: winning states at deep depth (k-t small)")
    print()
    print("  Neither produces losing states at deep depth (F(P) > k-t with t ~ k).")
    print()
    print("  To produce losing states at deep depth, we need:")
    print("    - F(P) large (hard to sort)")
    print("    - t large (close to k)")
    print("    - k - t small (little remaining budget)")
    print("  This requires a poset that is hard to sort even after many comparisons.")
    print()
    print("  The n=12 witness is such a poset (S(12)=30, C(12)=29),")
    print("  but it's not clear how to generalize it to an infinite family.")


def main():
    print("=" * 70)
    print("Rectangular-chain construction verification")
    print("=" * 70)
    print()

    verify_small()
    analyze_losing_state_possibility()
    analyze_ordinal_sum_vs_rectangular()

    print("=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print()
    print("  The rectangular-chain construction produces WINNING states")
    print("  (F(P) <= k-t), not losing states (F(P) > k-t).")
    print()
    print("  The ordinal sum construction produces losing states at")
    print("  shallow depths, but F(P) > k-t fails for large m.")
    print()
    print("  These are complementary barriers:")
    print("  - Ordinal sum: gap grows as O(m), but k-t grows as O(m log m)")
    print("  - Rectangular-chain: F(P) is small, so F(P) <= k-t")
    print()
    print("  To produce an infinite family with F(P) > k-t, we need")
    print("  a fundamentally different construction that produces")
    print("  posets that are both hard to sort and hard to reach.")
    print()
    print("  Key open question: does there exist a gadget with gap > 1?")
    print("  All known gadgets have gap = 1.")


if __name__ == "__main__":
    main()
