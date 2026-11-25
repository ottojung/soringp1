#!/usr/bin/env python3
"""Reproducible checks for docs/research-state-gap-fallacies.md.

This is an experiment, not a proof. It supports the falsification of two naive
inferences about the complexity of evaluating S(n):

  * Inference 1: "the minimax state space has 2^{Theta(n^2)} states, so S(n) is
    hard". Refuted three ways:
      (a) a large state space is an algorithmic artifact, not a problem
          invariant (Nim: exponential game tree, polynomial-time nim-sum);
      (b) a state space of size S forces time Omega(log S) by configuration
          counting; for S = 2^{n^2} that is only Omega(n^2), which is
          polynomial in the unary input length N = n. Exponential time would
          require 2^{2^{Omega(N)}} states, a doubly exponential deficit;
      (c) the poset DP state count is larger than the n! decision-tree leaves,
          so it is not even a decision-tree lower bound.
  * Inference 2: "S(n) is within O(n) of the information lower bound, so the
    gap is small, so S(n) should be easy". Refuted by NP-hard problems with
    PTAS/FPTAS (Euclidean TSP, knapsack) and by the S(n) gap structure itself:
    the gap is 0 for n <= 11 and n = 20, 21, but 1 at n = 12, and the exact
    value is open for n >= 23. Small gap = good approximation, not exactness.

Run:  python3 scripts/state_gap_audit.py
"""

from __future__ import annotations

import argparse
import math
from functools import lru_cache

# S(n) for n = 0..12 (literature; see docs/literature.md). S(20)=62, S(21)=66
# are also known to equal the information bound (Peczarski 2012).
KNOWN_S = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 9: 19,
           10: 22, 11: 26, 12: 30, 20: 62, 21: 66}

# OEIS A001035: labelled partial orders on n elements (the reachable states of
# the memoized poset DP). Values for n <= 7 are the exact sequence values and
# are reproduced by scripts/state_compression.py in this repository.
A001035 = {0: 1, 1: 1, 2: 3, 3: 19, 4: 219, 5: 4231, 6: 130023, 7: 6129859}


def ceil_log2(n: int) -> int:
    """Exact integer ceil(log2 n) for n >= 1; 0 for n <= 1."""
    if n <= 1:
        return 0
    return (n - 1).bit_length()


def info_bound(n: int) -> int:
    """I(n) = ceil(log2 n!), the information-theoretic lower bound on S(n)."""
    if n <= 1:
        return 0
    bits = 0
    for k in range(2, n + 1):
        bits += k.bit_length()
    # log2(n!) = sum_{k=2}^n log2 k; use exact integer ceiling via Fraction-free
    # comparison: find the smallest b with 2^b >= n!.
    f = 1
    for k in range(2, n + 1):
        f *= k
    b = 0
    p = 1
    while p < f:
        p <<= 1
        b += 1
    return b


def gap_table() -> list[tuple[int, int, int, int]]:
    rows = []
    for n in sorted(KNOWN_S):
        ib = info_bound(n)
        rows.append((n, KNOWN_S[n], ib, KNOWN_S[n] - ib))
    return rows


# ---------------------------------------------------------------------------
# Nim counterexample: exponential game tree, polynomial-time solution.
# ---------------------------------------------------------------------------

def nim_state_space(piles: tuple[int, ...]) -> int:
    """Number of positions reachable from a Nim position (including itself)."""
    total = 1
    for p in piles:
        total *= (p + 1)
    return total


@lru_cache(maxsize=None)
def nim_winner_bruteforce(piles: tuple[int, ...]) -> bool:
    """True iff the player to move wins, by full minimax over the game tree."""
    if all(p == 0 for p in piles):
        return False
    for i, p in enumerate(piles):
        for take in range(1, p + 1):
            nxt = list(piles)
            nxt[i] = p - take
            if not nim_winner_bruteforce(tuple(nxt)):
                return True
    return False


def nim_winner_formula(piles: tuple[int, ...]) -> bool:
    """Bouton's theorem: the player to move wins iff the nim-sum is nonzero."""
    x = 0
    for p in piles:
        x ^= p
    return x != 0


def nim_report() -> None:
    print("== Nim: large state space, polynomial-time solution ==")
    cases = [(2, 3), (3, 4, 5), (1, 1, 1, 1), (3, 4, 5, 6), (5, 6, 7, 8)]
    print("  piles          | states (prod(p+1)) | brute-force | nim-sum | agree")
    for piles in cases:
        s = nim_state_space(piles)
        b = nim_winner_bruteforce(piles)
        f = nim_winner_formula(piles)
        print(f"  {str(piles):>14} | {s:>18} | {str(b):>11} | "
              f"{str(f):>7} | {b == f}")
    nim_winner_bruteforce.cache_clear()


# ---------------------------------------------------------------------------
# Quantitative refutation of Inference 1.
# ---------------------------------------------------------------------------

def state_space_table() -> None:
    print("\n== State-space size vs. the time lower bound it can force ==")
    print("  A deterministic TM running in time T has at most 2^{O(T)}")
    print("  configurations, so M distinguishable states force T >= Omega(log M).")
    print()
    print("  n | poset states 2^{n^2} | log2 (forced time lower bound) | "
          "states needed for 2^{Omega(n)} time")
    for n in (8, 12, 16, 24, 32):
        log_states = n * n
        print(f"  {n:>2} | 2^{log_states:<18} | Omega({log_states}) | "
              f"2^(2^{n}) = 2^{2 ** n}")
    print()
    print("  For the unary encoding N = n: 2^{n^2} states force only Omega(N^2)")
    print("  time, which is polynomial. Exponential time 2^{Omega(N)} needs")
    print("  2^{2^{Omega(N)}} states -- a doubly exponential deficit.")


def dp_states_vs_leaves() -> None:
    print("\n== DP state count vs. decision-tree leaf count ==")
    print("  n | labelled posets (DP states) | n! (reduced tree leaves) | DP > leaves")
    for n in range(2, 8):
        dp = A001035[n]
        leaves = math.factorial(n)
        print(f"  {n:>2} | {dp:>26} | {leaves:>24} | {dp > leaves}")
    print("  The poset DP explores MORE states than there are permutations, so")
    print("  its state count is not a decision-tree lower bound either.")


# ---------------------------------------------------------------------------
# Inference 2: gap structure.
# ---------------------------------------------------------------------------

def gap_report() -> None:
    print("\n== Gap S(n) - ceil(log2 n!) ==")
    print("  n | S(n) | I(n) | gap | note")
    notes = {11: "last gap-0 before n=12", 12: "first obstruction (Wells)",
             20: "gap 0 again (literature)", 21: "gap 0 again (literature)"}
    for n, s, ib, g in gap_table():
        print(f"  {n:>2} | {s:>4} | {ib:>4} | {g:>3} | {notes.get(n, '')}")
    print("  Small gap = the information bound is a good approximation. It does")
    print("  NOT make the exact value easy: the exact value is open for n >= 23.")


def approx_vs_exact_report() -> None:
    print("\n== NP-hard problems with arbitrarily good approximation ==")
    print("  problem             | approximation | exact")
    print("  Euclidean TSP       | PTAS (1+eps)  | NP-hard (Papadimitriou 1977)")
    print("  0-1 knapsack        | FPTAS (1-eps) | NP-hard (weakly)")
    print("  metric TSP          | 1.5-approx    | NP-hard")
    print("  vertex cover        | 2-approx (LP) | NP-hard")
    print("  A small gap/approximation ratio says nothing about exactness.")


def report() -> None:
    print("== Gap table ==")
    for n, s, ib, g in gap_table():
        print(f"  n={n:>2} S={s:>3} I={ib:>3} gap={g}")
    nim_report()
    state_space_table()
    dp_states_vs_leaves()
    gap_report()
    approx_vs_exact_report()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quiet", action="store_true", help="suppress report")
    args = ap.parse_args()
    if not args.quiet:
        report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
