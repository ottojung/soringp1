#!/usr/bin/env python3
"""One-ply adversarial information lower bound (docs/research-one-ply-obstruction.md).

A *structural* lower bound for the exact worst-case comparison-sorting number
that is strictly stronger than the leaf-counting (information) bound on an
infinite family, with the smallest strict witness at ``n = 5``.

Model (fixed, from ``docs/problem.md``): adaptive worst-case pairwise
comparison sorting of ``n`` distinct labelled keys.  A state is a transitively
closed strict partial order on ``{0, ..., n-1}``, represented by a tuple
``succ`` where ``succ[i]`` is the bitmask of elements strictly greater than
``i``.  ``F(P)`` is the minimum remaining worst-case comparisons that sorts
every linear extension of ``P`` (so ``F(P) = 0`` iff ``P`` is a total order and
``F(antichain_n) = S(n)``).  ``e(P)`` is the number of linear extensions.

Definitions (the two bounds):

* ``L0(P) = ceil(log2 e(P))`` -- the information (leaf-counting) bound.
* ``L1(P) = 0`` if ``P`` is total, else
  ``1 + min over incomparable pairs {i,j} of max(L0(P+i<j), L0(P+j<i))``.

``L1`` is the *one-ply* lookahead: a single minimax level whose children are
scored by the information bound ``L0`` instead of the full recursion.

Everything here is an *experiment* on finite posets.  The default CLI is *not*
exhaustive: it checks ``L0 <= L1 <= F`` for all posets on ``n <= 4`` elements,
the explicit ``n = 5`` witness, and a fixed small deterministic ``n = 5``
sample with shared memoized ``F``.  No complexity-class, ``S(12)``, or
polynomial-time claim is made.  In particular ``e(P)`` is #P-complete to
compute exactly in general, so neither ``L0`` nor ``L1`` is claimed to be
polynomial-time computable; the one-ply minimum costs ``O(n^2)`` extension-count
subcalls per state and is cheaper than the full optimal min-max only
empirically.  Reproduce with ``python3 scripts/one_ply_obstruction.py``.
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


def ceil_log2(x: int) -> int:
    return (x - 1).bit_length()


# --------------------------------------------------------------------------
# The two bounds
# --------------------------------------------------------------------------

def L0(succ: tuple[int, ...]) -> int:
    """Information bound ``ceil(log2 e(P))``."""
    return ceil_log2(linear_extensions(succ))


def L1(succ: tuple[int, ...]) -> int:
    """One-ply adversarial information bound (see module docstring)."""
    pairs = incomparable_pairs(succ)
    if not pairs:
        return 0
    return 1 + min(
        max(L0(add_relation(succ, i, j)), L0(add_relation(succ, j, i)))
        for i, j in pairs
    )


# --------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------

# Smallest strict witness: n = 5, e = 8, L0 = 3, L1 = 4, F = 4.
N5_WITNESS = (26, 0, 10, 0, 8)


def append_total_suffix(succ: tuple[int, ...], t: int) -> tuple[int, ...]:
    """Ordinal-sum the given poset with a new t-element totally ordered suffix.

    Every original key precedes every suffix key. This is a fast constructive
    infinite family of strict one-ply witnesses when applied to N5_WITNESS.
    """
    if t < 0:
        raise ValueError("t must be nonnegative")
    n = len(succ)
    old_to_new = ((1 << t) - 1) << n
    first = tuple(mask | old_to_new for mask in succ)
    tail = tuple(sum(1 << j for j in range(n + i + 1, n + t))
                 for i in range(t))
    return first + tail


def witness_splits(succ: tuple[int, ...]) -> list[tuple[int, int]]:
    """Extension counts ``(e(P+i<j), e(P+j<i))`` for each incomparable pair."""
    return [
        (linear_extensions(add_relation(succ, i, j)),
         linear_extensions(add_relation(succ, j, i)))
        for i, j in incomparable_pairs(succ)
    ]


def validate(max_n: int = 4, n5_sample: int = 40) -> dict[str, object]:
    """Check ``L0 <= L1 <= F`` on a fast, bounded poset set.

    Exhaustively checks every poset on ``n <= max_n`` elements, the explicit
    ``n = 5`` witness ``N5_WITNESS``, and a fixed deterministic ``n = 5`` sample
    (the first ``n5_sample`` posets in sorted order) with shared memoized ``F``.
    Returns a summary dict.  Raises ``AssertionError`` on any violation.
    """
    summary: dict[str, object] = {}
    checked = 0
    for n in range(1, max_n + 1):
        for P in all_posets(n):
            assert L1(P) >= L0(P), f"L1 < L0 at n={n}: P={P}"
            assert L1(P) <= minimax(P), f"L1 > F at n={n}: P={P}"
            checked += 1
    # Explicit n = 5 witness.
    assert L1(N5_WITNESS) > L0(N5_WITNESS)
    assert L1(N5_WITNESS) <= minimax(N5_WITNESS)
    checked += 1
    # Fixed deterministic n = 5 sample (sorted for reproducibility).
    sample = sorted(all_posets(5))[:n5_sample]
    for P in sample:
        assert L1(P) >= L0(P), f"L1 < L0 in n=5 sample: P={P}"
        assert L1(P) <= minimax(P), f"L1 > F in n=5 sample: P={P}"
        checked += 1
    summary["max_n_exhaustive"] = max_n
    summary["n5_sample_size"] = n5_sample
    summary["witness"] = N5_WITNESS
    summary["checked"] = checked
    return summary


def report() -> None:
    print("== One-ply adversarial information lower bound ==")
    w = N5_WITNESS
    print(f"\nSmallest strict witness n=5: {w}")
    print(f"  e = {linear_extensions(w)}, L0 = {L0(w)}, "
          f"L1 = {L1(w)}, F = {minimax(w)}")
    print(f"  child extension splits: {sorted(witness_splits(w))}")
    print(f"  strict: L1 > L0 is {L1(w) > L0(w)}; valid: L1 <= F is {L1(w) <= minimax(w)}")

    summary = validate()
    print(f"\nBounded validation (NOT exhaustive n=5):")
    print(f"  exhaustive for n <= {summary['max_n_exhaustive']}, "
          f"plus n=5 witness + {summary['n5_sample_size']}-poset sample")
    print(f"  posets checked: {summary['checked']}")
    print(f"  L0 <= L1 <= F holds everywhere checked: True")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--max-n", type=int, default=4,
        help="exhaustive enumeration cap (default 4; the n=5 witness and a "
             "small sample are always included)",
    )
    parser.add_argument(
        "--n5-sample", type=int, default=40,
        help="size of the fixed deterministic n=5 sample (default 40)",
    )
    args = parser.parse_args()
    if args.max_n > 5:
        raise SystemExit("this probe is bounded to n <= 5 by design")
    report()
