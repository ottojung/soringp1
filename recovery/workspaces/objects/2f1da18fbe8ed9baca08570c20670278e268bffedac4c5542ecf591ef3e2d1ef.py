#!/usr/bin/env python3
"""Reproducible checks for docs/research-hardness-boundaries.md.

This script is an experiment, not a proof. It supports three claims of the note:

  * The two 5-element posets P1, P2 both have e = 8 but different exact
    comparison costs F (3 and 4). Hence F is not a function of e, so counting
    linear extensions does not determine the exact sorting cost.
  * The antichain embedding 1^n#1^k -> (antichain_n, k) is polynomial-time for
    the unary encoding of n (matrix size Theta(n^2)) but exponential for the
    binary encoding (matrix size 2^{Theta(m)} where m = Theta(log n)).
  * The P/log length cutoff t_L and the binary guaranteed-member count used in
    the encoding audit.

Model: a poset on {0..n-1} is a tuple ``succ`` where ``succ[i]`` is a bitmask of
the elements strictly greater than i (transitively closed), exactly as in
``scripts/structural_lower_bounds.py``. F(P) is the exact minimax remaining
comparison count; F(antichain_n) = S(n).

Run:  python3 scripts/hardness_boundaries.py
"""

from __future__ import annotations

import argparse

import structural_lower_bounds as slb

# S(n) for n = 0..11 (literature; see docs/literature.md). Used only for the
# P/log cutoff table, which needs n <= L-1.
KNOWN_S = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 9: 19,
           10: 22, 11: 26}

# The two 5-element witnesses with equal e but different F.
P1 = (8, 12, 8, 0, 12)
P2 = (26, 0, 10, 0, 8)


def witness() -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return (P1, P2): equal e, different F."""
    return P1, P2


def smallest_collision(max_n: int = 5) -> tuple[int, tuple[int, int, tuple[int, ...], tuple[int, ...]]] | None:
    """Smallest n with an e-value attained by two posets of different F.

    Returns (n, e, P_low, P_high) with F(P_low) < F(P_high), or None.
    """
    for n in range(2, max_n + 1):
        by_e: dict[int, list[tuple[int, tuple[int, ...]]]] = {}
        for P in slb.all_posets(n):
            by_e.setdefault(slb.linear_extensions(P), []).append((slb.minimax(P), P))
        for e in sorted(by_e):
            entries = by_e[e]
            lo = min(entries, key=lambda t: t[0])
            hi = max(entries, key=lambda t: t[0])
            if lo[0] < hi[0]:
                return n, e, lo[1], hi[1]
    return None


def matrix_bits(n: int) -> int:
    """Size in bits of the explicit n x n comparability matrix of a poset."""
    return n * n


def transfer_sizes(n: int) -> tuple[int, int, int]:
    """Return (unary_length, matrix_bits, binary_length) for the antichain on n.

    unary_length = n (the encoding 1^n), matrix_bits = n^2 (explicit antichain),
    binary_length = |bin(n)| = floor(log2 n) + 1 (the encoding bin(n)).
    """
    unary_length = n
    binary_length = n.bit_length() if n > 0 else 1
    return unary_length, matrix_bits(n), binary_length


def ceil_log2(n: int) -> int:
    """Exact integer ceil(log2 n) for n >= 1; 0 for n <= 1."""
    if n <= 1:
        return 0
    return (n - 1).bit_length()


def merge_sort_upper_bound(n: int) -> int:
    """U(n) = n * ceil(log2(max(2, n))); a valid merge-sort bound on S(n)."""
    if n <= 1:
        return 0
    return n * ceil_log2(max(2, n))


def plog_cutoffs(max_L: int) -> list[tuple[int, int]]:
    """t_L = max{ n <= L-1 : n + S(n) <= L-1 } for L = 1..max_L."""
    rows = []
    for L in range(1, max_L + 1):
        t = 0
        for n in range(0, L):
            if n + KNOWN_S.get(n, 10**9) <= L - 1:
                t = n
        rows.append((L, t))
    return rows


def binary_guaranteed_count(m: int) -> int:
    """Number of guaranteed members bin(n)#bin(k) of SORT-BOUND-B of length <= m.

    For each 1 <= n <= 2^{m/3}, every k with |bin(k)| <= K_n := m - 1 - |bin(n)|
    and k >= U(n) is in the language. The count is exact for this guaranteed set.
    """
    if m < 4:
        return 0
    total = 0
    for n in range(1, 2 ** (m // 3) + 1):
        k_bits = m - 1 - n.bit_length()
        if k_bits < 0:
            continue
        hi = 2 ** k_bits  # k in [0, 2^k_bits)
        u = merge_sort_upper_bound(n)
        if hi > u:
            total += hi - u
    return total


def report() -> None:
    print("== Witness: equal e, different F ==")
    for name, P in (("P1", P1), ("P2", P2)):
        rels = [(i, j) for i in range(len(P)) for j in range(len(P)) if (P[i] >> j) & 1]
        print(f"  {name} succ={P} e={slb.linear_extensions(P)} F={slb.minimax(P)}")
        print(f"     relations={rels}")
    print(f"  P1,P2 equal e and different F: "
          f"{slb.linear_extensions(P1) == slb.linear_extensions(P2) and slb.minimax(P1) != slb.minimax(P2)}")

    print("\n== Smallest collision ==")
    c = smallest_collision(5)
    if c is None:
        print("  none for n <= 5")
    else:
        n, e, lo, hi = c
        print(f"  n={n} e={e}: F({lo})={slb.minimax(lo)} < F({hi})={slb.minimax(hi)}")

    print("\n== Antichain embedding sizes (unary vs binary) ==")
    print("  n | unary 1^n (bits) | matrix n^2 (bits) | binary bin(n) (bits)")
    for n in (4, 8, 16, 32, 64):
        u, m, b = transfer_sizes(n)
        print(f"  {n:>2} | {u:>16} | {m:>17} | {b:>20}")

    print("\n== P/log cutoff t_L ==")
    print("  L | t_L | bits ceil(log2 L)")
    for L, t in plog_cutoffs(12):
        print(f"  {L:>2} | {t:>3} | {ceil_log2(L):>16}")

    print("\n== Binary guaranteed members of length <= m ==")
    print("  m | count | 2^(m-3)")
    for m in (8, 12, 16, 20, 24):
        c = binary_guaranteed_count(m)
        print(f"  {m:>2} | {c:>5} | {2 ** (m - 3) if m >= 3 else 0:>6}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quiet", action="store_true", help="suppress report")
    args = ap.parse_args()
    if not args.quiet:
        report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
