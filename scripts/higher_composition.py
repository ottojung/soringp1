#!/usr/bin/env python3
"""Higher composition: the decomposed lookahead bound ``B_r`` and its gap
to the global horizon-``r`` bound.  Companion program for
``docs/research-higher-composition.md``.

Model (fixed, from ``docs/problem.md``): adaptive worst-case pairwise
comparison sorting of ``n`` distinct labelled keys.  A state is a
transitively closed strict partial order on ``{0, ..., n-1}``, represented
by a tuple ``succ`` where ``succ[i]`` is the bitmask of elements strictly
greater than ``i``.  ``F(P)`` is the minimum remaining worst-case
comparisons that identifies the unknown linear extension of ``P`` (so
``F(P) = 0`` iff ``P`` is total and ``F(antichain_n) = S(n)``).  ``e(P)``
is the number of linear extensions.

Bounds (see the note for proofs and provenance):

* ``L0(P) = ceil(log2 e(P))`` -- the information (leaf-counting) bound.
* ``Lr(P, r)`` -- the horizon-``r`` adversarial information bound:
  ``r`` minimax plies whose leaves are scored by ``L0`` (the hierarchy of
  ``docs/research-lookahead-hierarchy.md``).
* ``Br(P) = sum_i Lr(P_i)`` -- the *higher-composition* bound: the sum of
  the per-factor horizon-``r`` bounds over the series decomposition
  ``P = P_1 (+) ... (+) P_k`` into maximal ordinal-sum factors (the
  connected components of the incomparability graph).

Main theorem (proved in the note): for every ``r >= 0`` and every finite
poset ``P``,

    Lr(P) <= Br(P) <= F(P),

and ``Br`` is nondecreasing in ``r``.  The proof is an induction on ``r``
whose key step is ordinal-sum subadditivity of ``Lr``:
``Lr(A (+) B) <= Lr(A) + Lr(B)``.

Negative result (proved in the note): on the family ``Q^t`` for
``Q = (2, 0, 0)`` (``e = 3``, ``F = Lr = 2`` for every ``r``),
``Br(Q^t) = F(Q^t) = 2t`` while the global bound satisfies
``Lr(Q^t) <= ceil(t log2 3) + r``; since ``log2 3 < 2`` the gap is
unbounded for each fixed ``r``.  Likewise ``W^t`` for
``W = (26, 0, 10, 0, 8)`` (``e = 8``, ``L0 = 3``, ``Lr = F = 4`` for
``r >= 1``): ``Br(W^t) = F(W^t) = 4t`` for ``r >= 1`` while
``Lr(W^t) <= 3t + r < 4t`` once ``t > r``.

Everything here is an *experiment* on finite posets plus the proved
inequalities of the note.  No complexity-class, hardness, or
algorithm lower-bound claim is made; ``e(P)`` is #P-complete to compute
exactly in general.  Reproduce with
``python3 scripts/higher_composition.py``.
"""

from __future__ import annotations

import argparse
import math
import time
from functools import lru_cache

# ---------------------------------------------------------------------------
# Poset machinery (same representation as the other probes)
# ---------------------------------------------------------------------------


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
    """Exact ``e(P)`` via a downset DP.  PROTOTYPE TOOL: ``O(2^n)`` space."""
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
    """Exact ``F(P)``: minimum remaining worst-case comparisons (memoized)."""
    pairs = incomparable_pairs(succ)
    if not pairs:
        return 0
    return 1 + min(
        max(minimax(add_relation(succ, i, j)), minimax(add_relation(succ, j, i)))
        for i, j in pairs
    )


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


def ceil_log2(x: int) -> int:
    return (x - 1).bit_length()


# ---------------------------------------------------------------------------
# The bounds L_r and the higher-composition bound B_r
# ---------------------------------------------------------------------------

_LR_MEMO: dict[tuple[tuple[int, ...], int], int] = {}


def Lr(succ: tuple[int, ...], r: int) -> int:
    """Horizon-``r`` adversarial information bound: ``r`` minimax plies,
    leaves scored by ``L0``.  ``Lr(P, 0) = L0(P)``; ``Lr(P, r) = 0`` for
    total ``P``."""
    if r < 0:
        raise ValueError("r must be nonnegative")
    key = (succ, r)
    if key in _LR_MEMO:
        return _LR_MEMO[key]
    pairs = incomparable_pairs(succ)
    if not pairs or r == 0:
        val = 0 if not pairs else ceil_log2(linear_extensions(succ))
    else:
        val = 1 + min(
            max(Lr(add_relation(succ, i, j), r - 1),
                Lr(add_relation(succ, j, i), r - 1))
            for i, j in pairs
        )
    _LR_MEMO[key] = val
    return val


def ordinal_sum(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Ordinal sum ``p (+) q``: every element of ``p`` below every of ``q``."""
    a = len(p)
    top_mask = ((1 << (a + len(q))) - 1) ^ ((1 << a) - 1)
    return tuple(s | top_mask for s in p) + tuple(s << a for s in q)


def series_power(p: tuple[int, ...], t: int) -> tuple[int, ...]:
    """The ``t``-fold ordinal (series) power ``p (+) p (+) ... (+) p``."""
    if t < 0:
        raise ValueError("t must be nonnegative")
    out: tuple[int, ...] = ()
    for _ in range(t):
        out = ordinal_sum(out, p) if out else p
    return out


def incomparability_components(succ: tuple[int, ...]) -> list[list[int]]:
    """Connected components of the incomparability graph (series factors)."""
    n = len(succ)
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(n):
        for j in range(i + 1, n):
            if not (succ[i] >> j) & 1 and not (succ[j] >> i) & 1:
                ri, rj = find(i), find(j)
                if ri != rj:
                    parent[ri] = rj
    comps: dict[int, list[int]] = {}
    for i in range(n):
        comps.setdefault(find(i), []).append(i)
    return list(comps.values())


def induced(succ: tuple[int, ...], subset: list[int]) -> tuple[int, ...]:
    """Induced subposet on ``subset``, relabelled to 0..m-1."""
    index = {e: k for k, e in enumerate(subset)}
    return tuple(
        sum((1 << index[j]) for j in subset if succ[i] & (1 << j)) for i in subset
    )


def Br(succ: tuple[int, ...], r: int) -> int:
    """Higher-composition bound ``sum_i Lr(P_i)`` over series factors."""
    return sum(Lr(induced(succ, c), r) for c in incomparability_components(succ))


def ordinal_sum_additive_F(p: tuple[int, ...], q: tuple[int, ...]) -> int:
    """``F(p (+) q) = F(p) + F(q)`` (ordinal-sum additivity, used on the
    small base posets only; powers get ``F`` by additivity, never by
    direct minimax on the large state)."""
    return minimax(p) + minimax(q)


# ---------------------------------------------------------------------------
# The two families
# ---------------------------------------------------------------------------

# Q = Merge(2, 1): a 2-chain disjoint union (||) a singleton; e = 3, F = 2.
Q_MERGE_2_1 = (2, 0, 0)

# W = smallest strict one-ply witness (docs/research-one-ply-obstruction.md):
# e = 8, L0 = 3, L1 = F = 4.
N5_WITNESS = (26, 0, 10, 0, 8)


# ---------------------------------------------------------------------------
# Bounded experiments
# ---------------------------------------------------------------------------


def chain_regression(max_n: int, r_max: int) -> dict[str, object]:
    """Check ``Lr <= Br <= F`` and ``Br <= B(r+1)`` for every poset on
    ``n <= max_n`` elements and all ``0 <= r <= r_max``.

    Raises ``AssertionError`` on any violation.  Returns a summary dict.
    """
    rows: list[dict[str, object]] = []
    for n in range(1, max_n + 1):
        posets = all_posets(n)
        strict_br_gt_lr = strict_br_lt_br_next = 0
        max_gap_br_minus_lr = 0
        for P in posets:
            f = minimax(P)
            prev_b = None
            for r in range(r_max + 1):
                lr = Lr(P, r)
                br = Br(P, r)
                assert lr <= br, f"Lr > Br at n={n}, r={r}: P={P}"
                assert br <= f, f"Br > F at n={n}, r={r}: P={P}"
                if br > lr:
                    strict_br_gt_lr += 1
                    max_gap_br_minus_lr = max(max_gap_br_minus_lr, br - lr)
                if prev_b is not None:
                    assert prev_b <= br, f"Br not monotone at n={n}, r={r}: P={P}"
                    if br > prev_b:
                        strict_br_lt_br_next += 1
                prev_b = br
        rows.append(
            {
                "n": n,
                "posets": len(posets),
                "strict_Br_gt_Lr": strict_br_gt_lr,
                "strict_Br_lt_Br_next": strict_br_lt_br_next,
                "max_gap_Br_minus_Lr": max_gap_br_minus_lr,
            }
        )
    return {"rows": rows}


def q_family_report(t_max: int, r_max: int) -> list[dict[str, object]]:
    """Finite checks on the series powers ``Q^t`` of ``Q = (2, 0, 0)``.

    Direct exact computation of ``e``, global ``Lr`` (for ``r <= r_max``)
    and ``Br`` (via ``Lr(Q)``); ``F(Q^t) = t * F(Q) = 2t`` by ordinal-sum
    additivity (never by direct minimax on the large state).
    """
    q = Q_MERGE_2_1
    assert linear_extensions(q) == 3
    assert minimax(q) == 2
    for r in range(r_max + 1):
        assert Lr(q, r) == 2, (r, Lr(q, r))  # Lr(Q) = 2 for every r
    rows: list[dict[str, object]] = []
    for t in range(1, t_max + 1):
        P = series_power(q, t)
        e = linear_extensions(P)
        row: dict[str, object] = {
            "t": t,
            "n": len(P),
            "e": e,
            "F": 2 * t,
            "Lr_Q": Lr(q, 0),
        }
        assert e == 3**t, (t, e)
        for r in range(r_max + 1):
            bound = ceil_log2(3**t) + r
            val = Lr(P, r)
            assert val <= bound, (t, r, val, bound)
            row[f"Lr_r{r}"] = val
            assert Br(P, r) == 2 * t, (t, r, Br(P, r))
            row[f"Br_r{r}"] = 2 * t
        rows.append(row)
    return rows


def w_family_report(t_max: int, r_max: int) -> list[dict[str, object]]:
    """Finite checks on the series powers ``W^t`` of ``W = (26,0,10,0,8)``.

    Direct exact computation of ``e``, global ``Lr`` (for ``r <= r_max``)
    and ``Br``; ``F(W^t) = t * F(W) = 4t`` by ordinal-sum additivity.
    """
    w = N5_WITNESS
    assert linear_extensions(w) == 8
    assert minimax(w) == 4
    assert Lr(w, 0) == 3
    for r in range(1, r_max + 1):
        assert Lr(w, r) == 4, (r, Lr(w, r))  # Lr(W) = F(W) = 4 for r >= 1
    rows: list[dict[str, object]] = []
    for t in range(1, t_max + 1):
        P = series_power(w, t)
        e = linear_extensions(P)
        row: dict[str, object] = {"t": t, "n": len(P), "e": e, "F": 4 * t}
        assert e == 8**t, (t, e)
        for r in range(r_max + 1):
            row[f"Lr_r{r}"] = Lr(P, r)
            row[f"Br_r{r}"] = Br(P, r)
            assert Br(P, r) == t * Lr(w, r), (t, r, Br(P, r))
        rows.append(row)
    return rows


def gap_table(r_max: int) -> dict[str, object]:
    """Pure arithmetic: the minimal power ``t`` at which the proved global
    bound provably drops below the exact value.

    * ``Q^t``: ``ceil(t log2 3) + r < 2t = F(Q^t)`` (fixed ``r``, unbounded
      gap).
    * ``W^t``, ``r >= 1``: ``3t + r < 4t = F(W^t)``, i.e. ``t > r``.
    """
    q_rows: list[dict[str, object]] = []
    for r in range(r_max + 1):
        t = 1
        while not (ceil_log2(3**t) + r < 2 * t):
            t += 1
        q_rows.append(
            {"r": r, "t_min": t, "Lr_bound": ceil_log2(3**t) + r, "F": 2 * t}
        )
    w_rows: list[dict[str, object]] = []
    for r in range(1, r_max + 1):
        t = r + 1
        w_rows.append({"r": r, "t_min": t, "Lr_bound": 3 * t + r, "F": 4 * t})
    return {"Q": q_rows, "W": w_rows}


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=4,
                        help="exhaustive chain-regression cap (default 4)")
    parser.add_argument("--r-max", type=int, default=4,
                        help="largest horizon in the exhaustive regression (default 4)")
    parser.add_argument("--q-t", type=int, default=3,
                        help="largest series power Q^t checked directly (default 3)")
    parser.add_argument("--q-r", type=int, default=2,
                        help="largest horizon for direct Q^t checks (default 2)")
    parser.add_argument("--w-t", type=int, default=2,
                        help="largest series power W^t checked directly (default 2)")
    parser.add_argument("--w-r", type=int, default=2,
                        help="largest horizon for direct W^t checks (default 2)")
    parser.add_argument("--gap-r", type=int, default=5,
                        help="largest horizon in the arithmetic gap table (default 5)")
    args = parser.parse_args()
    if not 1 <= args.max_n <= 5:
        raise SystemExit("max-n is bounded to 1..5 by design")
    if not 1 <= args.q_t <= 4 or not 1 <= args.w_t <= 3:
        raise SystemExit("series powers are bounded by design (no large-state search)")
    if args.q_r > 3 or args.w_r > 3:
        raise SystemExit("direct horizons are bounded to 0..3 by design")

    print("=== Higher composition Br vs global Lr (experimental) ===\n")

    t0 = time.time()
    reg = chain_regression(args.max_n, args.r_max)
    print(f"Chain regression Lr <= Br <= F, Br monotone in r, n <= {args.max_n}, "
          f"r <= {args.r_max}:")
    for row in reg["rows"]:
        print(f"  n={row['n']}: posets={row['posets']} "
              f"strict Br>Lr={row['strict_Br_gt_Lr']} "
              f"strict Br(r)<Br(r+1)={row['strict_Br_lt_Br_next']} "
              f"max gap Br-Lr={row['max_gap_Br_minus_Lr']}")
    print(f"  ({round(time.time() - t0, 2)} s)\n")

    t0 = time.time()
    print(f"Q family (Q = {Q_MERGE_2_1}, e = 3, F = Lr = 2 for all r):")
    for row in q_family_report(args.q_t, args.q_r):
        print(f"  t={row['t']}: n={row['n']} e={row['e']} "
              + " ".join(f"Lr(r{r})={row[f'Lr_r{r}']}" for r in range(args.q_r + 1))
              + " | "
              + " ".join(f"Br(r{r})={row[f'Br_r{r}']}" for r in range(args.q_r + 1))
              + f" | F={row['F']}")
    print(f"  ({round(time.time() - t0, 2)} s)\n")

    t0 = time.time()
    print(f"W family (W = {N5_WITNESS}, e = 8, L0 = 3, Lr = F = 4 for r >= 1):")
    for row in w_family_report(args.w_t, args.w_r):
        print(f"  t={row['t']}: n={row['n']} e={row['e']} "
              + " ".join(f"Lr(r{r})={row[f'Lr_r{r}']}" for r in range(args.w_r + 1))
              + " | "
              + " ".join(f"Br(r{r})={row[f'Br_r{r}']}" for r in range(args.w_r + 1))
              + f" | F={row['F']}")
    print(f"  ({round(time.time() - t0, 2)} s)\n")

    gaps = gap_table(args.gap_r)
    print("Arithmetic gap table (proved bounds, minimal t per horizon):")
    for row in gaps["Q"]:
        print(f"  Q^t, r={row['r']}: t={row['t_min']} gives "
              f"Lr <= {row['Lr_bound']} < {row['F']} = F(Q^t)")
    for row in gaps["W"]:
        print(f"  W^t, r={row['r']}: t={row['t_min']} gives "
              f"Lr <= {row['Lr_bound']} < {row['F']} = F(W^t)")


if __name__ == "__main__":
    main()
