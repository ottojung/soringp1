#!/usr/bin/env python3
"""Ply-depth obstruction to closing the information bound for S(n).

Model (fixed, from ``docs/problem.md``): adaptive worst-case pairwise
comparison sorting of ``n`` distinct labelled keys.  A state is a transitively
closed strict partial order on ``{0, ..., n-1}`` represented by a successor
bitmask tuple ``succ``.  ``F(P)`` is the minimum remaining worst-case number of
comparisons that sorts every linear extension of ``P``; ``F(antichain_n)=S(n)``.
``e(P)`` is the number of linear extensions.

The information bound is ``L0(P)=ceil(log2 e(P))``.  The *k-ply hierarchy*
``L_k`` is the natural one-level-at-a-time strengthening:

    L_0(P) = ceil(log2 e(P)),
    L_k(P) = 0 if P is total, else
             1 + min over incomparable {i,j} of max(L_{k-1}(P+i<j), L_{k-1}(P+j<i)).

``L_k`` is the value of the game in which the sorter minimises, the adversary
maximises, and the leaf payoff is the information bound ``L0``.  Hence
``L0 <= L1 <= ... <= L_k <= ... <= F`` pointwise, and ``L_k`` converges to ``F``.

The question this probe answers is: **how many plies does the hierarchy need at
the root (the antichain) before it exceeds the information bound?**  The answer
is ``Omega(n)`` plies: the sorter can keep splitting the extension set exactly
in half by comparing two free elements, so the local lookahead never improves on
``L0``.  Consequently no bounded-ply (in particular no succinct) lower-bound
certificate built from local lookahead can close the information gap.

Everything here is a finite experiment over posets; no complexity-class claim is
made.  ``e(P)`` is #P-complete in general, so the probe is not a polynomial-time
algorithm.  Reproduce with::

    python3 scripts/unary_ply_obstruction.py --max-n 8 --kmax 8
"""

from __future__ import annotations

import argparse
from functools import lru_cache


# --------------------------------------------------------------------------
# Poset utilities
# --------------------------------------------------------------------------

def add_relation(succ: tuple[int, ...], i: int, j: int) -> tuple[int, ...]:
    """Transitive closure after adding ``i < j`` to an already closed state."""
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
    """Number of linear extensions, via a DP over downsets (memoized)."""
    n = len(succ)
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


def ceil_log2(x: int) -> int:
    return (x - 1).bit_length()


def all_posets(n: int) -> set[tuple[int, ...]]:
    """All transitively closed posets on ``n`` labelled elements."""
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


def info_bound(succ: tuple[int, ...]) -> int:
    return ceil_log2(linear_extensions(succ))


@lru_cache(maxsize=None)
def minimax(succ: tuple[int, ...]) -> int:
    """Exact ``F(P)``: minimum remaining worst-case comparisons (memoized)."""
    pairs = incomparable_pairs(succ)
    if not pairs:
        return 0
    return 1 + min(
        max(minimax(add_relation(succ, i, j)),
            minimax(add_relation(succ, j, i)))
        for i, j in pairs
    )


# --------------------------------------------------------------------------
# The k-ply hierarchy
# --------------------------------------------------------------------------

def ply_hierarchy(n: int):
    """Return ``L(succ, k)`` with memoization on ``(succ, k)``."""
    stats = {"states": 0}

    @lru_cache(maxsize=None)
    def L(succ: tuple[int, ...], k: int) -> int:
        stats["states"] += 1
        if k == 0:
            return info_bound(succ)
        pairs = incomparable_pairs(succ)
        if not pairs:
            return 0
        return 1 + min(
            max(L(add_relation(succ, i, j), k - 1),
                L(add_relation(succ, j, i), k - 1))
            for i, j in pairs
        )

    return L, stats


def report(n: int, kmax: int) -> None:
    L, stats = ply_hierarchy(n)
    antichain = (0,) * n
    C = info_bound(antichain)
    print(f"== n = {n}: C(n) = {C}, floor(n/2) = {n // 2} ==")
    print(f"  {'k':>3} {'L_k(P0)':>9} {'L_k - C':>8}  {'== C?':>6}")
    for k in range(0, kmax + 1):
        v = L(antichain, k)
        print(f"  {k:>3} {v:>9} {v - C:>8}  {str(v == C):>6}")
    print(f"  memoized (poset, ply) states: {stats['states']}")
    print(f"  L_k(P0) == C(n) for all k <= floor(n/2)? "
          f"{all(L(antichain, k) == C for k in range(0, n // 2 + 1))}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-n", type=int, default=8)
    ap.add_argument("--kmax", type=int, default=8)
    args = ap.parse_args()
    for n in range(2, args.max_n + 1):
        report(n, args.kmax)
        print()


if __name__ == "__main__":
    main()
