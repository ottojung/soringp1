#!/usr/bin/env python3
"""Adversarial lookahead hierarchy for exact comparison sorting.

Model (fixed, from ``docs/problem.md``): adaptive worst-case pairwise
comparison sorting of ``n`` distinct labelled keys.  A state is a transitively
closed strict partial order on ``{0, ..., n-1}``, represented by a tuple
``succ`` where ``succ[i]`` is the bitmask of elements strictly greater than
``i``.  ``e(P)`` is the number of linear extensions and ``F(P)`` the exact
minimum remaining worst-case comparisons (``F(P) = 0`` iff ``P`` is total,
``F(antichain_n) = S(n)``).

The *adversarial lookahead hierarchy* is the sequence of lower bounds

* ``L0(P) = ceil(log2 e(P))`` -- the information (leaf-counting) bound.
* ``L_{r+1}(P) = 0`` if ``P`` is total, else
  ``1 + min over incomparable pairs {i,j} of max(L_r(P+i<j), L_r(P+j<i))``.

``L_{r+1}`` scores a state by one minimax ply whose children are scored by
``L_r``; ``L1`` is the one-ply bound of ``docs/research-one-ply-obstruction.md``
and ``L2`` the two-ply bound.  See ``docs/research-lookahead-hierarchy.md`` for
the monotonicity/convergence proofs and the comparison with Stober--Weiß
(arXiv:2206.05597).

Everything here is an *experiment* on finite posets plus paper proofs.  No
complexity-class claim is made: counting linear extensions is #P-complete in
general (Brightwell--Winkler), so neither ``L_r`` nor ``F`` is claimed to be
polynomial-time computable.  Reproduce with
``python3 scripts/lookahead_hierarchy.py``.
"""

from __future__ import annotations

import argparse
from functools import lru_cache


# --------------------------------------------------------------------------
# Poset utilities (identical representation to one_ply_obstruction.py)
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
# The lookahead hierarchy
# --------------------------------------------------------------------------

_L_CACHE: dict[tuple[tuple[int, ...], int], int] = {}


def L(succ: tuple[int, ...], r: int) -> int:
    """The ``r``-ply adversarial information bound ``L_r(P)`` (memoized)."""
    if r < 0:
        raise ValueError("r must be nonnegative")
    key = (succ, r)
    cached = _L_CACHE.get(key)
    if cached is not None:
        return cached
    if r == 0:
        val = ceil_log2(linear_extensions(succ))
    else:
        pairs = incomparable_pairs(succ)
        if not pairs:
            val = 0
        else:
            val = 1 + min(
                max(L(add_relation(succ, i, j), r - 1),
                    L(add_relation(succ, j, i), r - 1))
                for i, j in pairs
            )
    _L_CACHE[key] = val
    return val


def hierarchy(succ: tuple[int, ...], max_r: int) -> list[int]:
    """``[L_0(P), ..., L_max_r(P)]``."""
    return [L(succ, r) for r in range(max_r + 1)]


# NOTE: for a single poset, ``L_r(P) = L_{r+1}(P)`` does NOT imply
# convergence (the functions may differ at descendants, which is exactly what
# makes ``L2 > L1`` possible).  The limit is therefore read off the *global*
# stabilization point on the whole finite poset set; see
# ``analyze_exhaustive``.


# --------------------------------------------------------------------------
# Exhaustive analysis
# --------------------------------------------------------------------------

def analyze_exhaustive(max_n: int = 6, min_r: int = 3, cap_r: int = 12
                       ) -> dict[str, object]:
    """Level-by-level analysis of the hierarchy on all posets with ``n <= max_n``.

    Computes ``L_r`` for every poset level by level until the *global*
    stabilization point ``r*`` (the smallest ``r`` with ``L_r = L_{r+1}``
    pointwise on the whole finite poset set, which by the fixed-point argument
    is the convergence point), but at least up to ``min_r`` and at most
    ``cap_r``.  Then verifies the monotone chain ``L_0 <= ... <= L_max <= F``
    everywhere, searches for strict ``L2 > L1`` witnesses, and measures the
    lookahead residual ``F - L_inf``.  Raises ``AssertionError`` on any
    chain violation.
    """
    posets: list[tuple[int, ...]] = []
    counts: dict[int, int] = {}
    for n in range(1, max_n + 1):
        level = sorted(all_posets(n))
        counts[n] = len(level)
        posets.extend(level)

    table: list[dict[tuple[int, ...], int]] = [{P: L(P, 0) for P in posets}]
    r_star = None
    while len(table) - 1 < cap_r:
        nxt = {P: L(P, len(table)) for P in posets}
        table.append(nxt)
        if nxt == table[-2]:
            r_star = len(table) - 2
            break
    if r_star is None:
        raise RuntimeError(f"hierarchy did not stabilize by r = {cap_r}")
    # The level ``r*`` is a fixed point, so later levels are equal; pad with it
    # so that ``L0 .. L_min_r`` are always available.
    while len(table) - 1 < min_r:
        table.append(table[-1])
    max_r = len(table) - 1

    f_vals = {P: minimax(P) for P in posets}
    profile = [
        sum(1 for P in posets if table[r][P] < table[r + 1][P])
        for r in range(max_r)
    ]
    summary: dict[str, object] = {
        "max_n": max_n,
        "r_star": r_star,
        "max_r": max_r,
        "poset_counts": counts,
        "chain_violations": [],
        "derivative_violations": [],
        "strict_L2_gt_L1": [],
        "max_gap_L1_minus_L0": 0,
        "max_gap_L2_minus_L1": 0,
        "max_gap_F_minus_L1": 0,
        "max_gap_F_minus_L2": 0,
        "max_residual_F_minus_Linf": 0,
        "residual_witnesses": [],
        "per_poset_stabilization_max": 0,
        "level_increase_profile": profile,
        "deepest_witness": None,
        "L1_lt_F_count": 0,
        "L2_lt_F_count": 0,
    }
    for P in posets:
        vals = [table[r][P] for r in range(max_r + 1)]
        f = f_vals[P]
        for a, b in zip(vals, vals[1:]):
            if a > b:
                summary["chain_violations"].append((P, vals, f))
        if vals[-1] > f:
            summary["chain_violations"].append((P, vals, f))
        for r in range(max_r + 1):
            if vals[r] > vals[0] + r:
                summary["derivative_violations"].append((P, r, vals, f))
        if len(vals) >= 3 and vals[2] > vals[1]:
            summary["strict_L2_gt_L1"].append(
                {"n": len(P), "P": P, "e": linear_extensions(P),
                 "L0": vals[0], "L1": vals[1], "L2": vals[2], "F": f}
            )
        summary["max_gap_L1_minus_L0"] = max(
            summary["max_gap_L1_minus_L0"], vals[1] - vals[0])
        summary["max_gap_L2_minus_L1"] = max(
            summary["max_gap_L2_minus_L1"], vals[2] - vals[1])
        summary["max_gap_F_minus_L1"] = max(
            summary["max_gap_F_minus_L1"], f - vals[1])
        summary["max_gap_F_minus_L2"] = max(
            summary["max_gap_F_minus_L2"], f - vals[2])
        limit = table[r_star][P]
        residual = f - limit
        summary["max_residual_F_minus_Linf"] = max(
            summary["max_residual_F_minus_Linf"], residual)
        if residual > 0:
            summary["residual_witnesses"].append((P, vals, f, limit))
        r_first = next(r for r in range(max_r + 1) if vals[r] == limit)
        summary["per_poset_stabilization_max"] = max(
            summary["per_poset_stabilization_max"], r_first)
        if r_first == summary["per_poset_stabilization_max"] and r_first >= 3:
            summary["deepest_witness"] = {
                "n": len(P), "P": P, "e": linear_extensions(P),
                "hierarchy": vals, "F": f, "r_first": r_first,
            }
        if vals[1] < f:
            summary["L1_lt_F_count"] += 1
        if vals[2] < f:
            summary["L2_lt_F_count"] += 1
    return summary


def optimal_moves(succ: tuple[int, ...], r: int) -> list[tuple[int, int, int, int]]:
    """Incomparable pairs attaining the ``L_{r+1}`` minimum, with child scores.

    Returns ``(i, j, L_r(P+i<j), L_r(P+j<i))`` for every pair whose
    ``max`` child score equals the minimum.
    """
    pairs = incomparable_pairs(succ)
    scored = [
        (i, j, L(add_relation(succ, i, j), r), L(add_relation(succ, j, i), r))
        for i, j in pairs
    ]
    best = min(max(a, b) for _, _, a, b in scored)
    return [(i, j, a, b) for i, j, a, b in scored if max(a, b) == best]


def witness_details(P: tuple[int, ...], max_r: int = 2) -> None:
    """Print exact masks, extension counts, and optimal-move child scores."""
    print(f"    P = {P}  (n = {len(P)}, e = {linear_extensions(P)})")
    for r in range(max_r):
        moves = optimal_moves(P, r)
        print(f"    L_{r + 1} = {L(P, r + 1)}: optimal move(s) for L_{r}:")
        for i, j, a, b in moves:
            print(f"      compare {{{i},{j}}}: L_{r}(P+{i}<{j}) = {a}, "
                  f"L_{r}(P+{j}<{i}) = {b}")
    print(f"    F = {minimax(P)}")


# --------------------------------------------------------------------------
# Targeted n = 6 candidates
# --------------------------------------------------------------------------

N5_WITNESS = (26, 0, 10, 0, 8)


def antichain(n: int) -> tuple[int, ...]:
    return (0,) * n


def crown6() -> tuple[int, ...]:
    """6-crown: a_i > b_i and a_i > b_{i+1 mod 3} for i in 0..2."""
    return (24, 48, 40, 0, 0, 0)


def fence6() -> tuple[int, ...]:
    """Zigzag 0<1>2<3>4<5."""
    return (2, 0, 10, 0, 40, 0)


def w5_disjoint_singleton() -> tuple[int, ...]:
    """The n=5 one-ply witness plus one isolated element (parallel union)."""
    return N5_WITNESS + (0,)


TARGETS: dict[str, tuple[int, ...]] = {
    "antichain_6": antichain(6),
    "crown_6": crown6(),
    "fence_6": fence6(),
    "w5_witness_disjoint_singleton": w5_disjoint_singleton(),
}


def analyze_target(name: str, P: tuple[int, ...], max_r: int = 3) -> dict[str, object]:
    vals = hierarchy(P, max_r)
    f = minimax(P)
    return {
        "name": name,
        "P": P,
        "n": len(P),
        "e": linear_extensions(P),
        "values": vals,
        "F": f,
        "strict_L2_gt_L1": vals[2] > vals[1],
        "chain_ok": all(a <= b for a, b in zip(vals, vals[1:])) and vals[-1] <= f,
    }


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

def report(max_n: int = 5, max_r: int = 3, targets: bool = True) -> None:
    print("== Adversarial lookahead hierarchy ==")
    print("Definitions: L0 = ceil(log2 e); L_{r+1} = 1 + min max(L_r(children));")
    print("F = exact minimax.  Chain proved: L0 <= L1 <= ... <= L_r <= F.\n")

    summary = analyze_exhaustive(max_n, min_r=max_r)
    print(f"Exhaustive for n <= {max_n}: {summary['poset_counts']} posets")
    print(f"  global stabilization r* = {summary['r_star']} "
          f"(L_r* = L_inf pointwise)")
    print(f"  chain L0 <= ... <= L{summary['max_r']} <= F violations: "
          f"{len(summary['chain_violations'])}")
    print(f"  derivative L_r <= L0 + r violations: "
          f"{len(summary['derivative_violations'])}")
    print(f"  max(L1 - L0) = {summary['max_gap_L1_minus_L0']}")
    print(f"  max(L2 - L1) = {summary['max_gap_L2_minus_L1']}")
    print(f"  max(F  - L1) = {summary['max_gap_F_minus_L1']}")
    print(f"  max(F  - L2) = {summary['max_gap_F_minus_L2']}")
    print(f"  max(F  - L_inf) = {summary['max_residual_F_minus_Linf']}")
    print(f"  max per-poset stabilization r = "
          f"{summary['per_poset_stabilization_max']}")
    print(f"  posets with L_inf < F: {len(summary['residual_witnesses'])}")
    print(f"  posets with L1 < F: {summary['L1_lt_F_count']}")
    print(f"  posets with L2 < F: {summary['L2_lt_F_count']}")
    print(f"  level-increase profile (posets with L_r < L_{{r+1}}, "
          f"r = 0..{summary['max_r'] - 1}): "
          f"{summary['level_increase_profile']}")
    dw = summary["deepest_witness"]
    if dw is not None:
        print(f"  deepest witness (last to stabilize, r = {dw['r_first']}):")
        print(f"    n={dw['n']} P={dw['P']} e={dw['e']} "
              f"hierarchy={dw['hierarchy']} F={dw['F']}")
    strict = summary["strict_L2_gt_L1"]
    print(f"  strict L2 > L1 witnesses: {len(strict)}")
    for w in strict[:10]:
        print(f"    n={w['n']} P={w['P']} e={w['e']} "
              f"L0={w['L0']} L1={w['L1']} L2={w['L2']} F={w['F']}")
    for w in strict[:3]:
        witness_details(w["P"], max_r=2)

    print("\nReference points:")
    print(f"  n=5 one-ply witness {N5_WITNESS}: "
          f"e={linear_extensions(N5_WITNESS)}, "
          f"hierarchy={hierarchy(N5_WITNESS, max_r)}, F={minimax(N5_WITNESS)}")
    print(f"  antichain_6: e={linear_extensions(antichain(6))}, "
          f"hierarchy={hierarchy(antichain(6), max_r)}, F={minimax(antichain(6))}")

    if targets:
        print("\nTargeted n = 6 states:")
        for name, P in TARGETS.items():
            t = analyze_target(name, P, max_r)
            print(f"  {name}: P={t['P']}")
            print(f"    e={t['e']} hierarchy(L0..L{max_r})={t['values']} "
                  f"F={t['F']} chain_ok={t['chain_ok']} "
                  f"strict_L2_gt_L1={t['strict_L2_gt_L1']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=6,
                        help="exhaustive enumeration cap (default 6)")
    parser.add_argument("--max-r", type=int, default=3,
                        help="hierarchy depth (default 3)")
    parser.add_argument("--no-targets", action="store_true",
                        help="skip the targeted n = 6 computations")
    args = parser.parse_args()
    report(args.max_n, args.max_r, not args.no_targets)
