#!/usr/bin/env python3
"""Compositional one-ply (lookahead) lower bounds for the exact minimax
sorting number.  Companion program for
``docs/research-compositional-lookahead.md``.

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
* ``L1(P)`` -- the one-ply adversarial information bound of
  ``docs/research-one-ply-obstruction.md``: a single minimax ply whose
  children are scored by ``L0``.
* ``Lr(P, r)`` -- the horizon-``r`` generalisation: ``r`` minimax plies
  whose leaves are scored by ``L0``.
* ``B(P) = sum_i L1(P_i)`` -- the *compositional* one-ply bound: decompose
  ``P`` into its ordinal-sum (series) factors ``P_i`` (the connected
  components of the incomparability graph) and sum the per-factor one-ply
  bounds.  Proved in the note: for every poset ``P``,
  ``L0(P) <= L1(P) <= B(P) <= F(P)``.

Two further proved contents checked here:

* Amplification along series powers: ``e(Q^t) = e(Q)^t``,
  ``F(Q^t) = t * F(Q)`` and ``Lr(Q^t, r) <= ceil(t * log2 e(Q)) + r``.
  With ``Q = Merge(2, 1)`` (a 2-chain disjoint union a singleton,
  ``e = 3``, ``F = 2``) this yields a *no-fixed-horizon* negative result:
  for every fixed ``r`` there are posets (large series powers ``Q^t``) with
  ``Lr < F``, so no fixed lookahead horizon equals ``F`` on all posets.
* The exact gap family ``W^t`` for the smallest strict one-ply witness
  ``W = (26, 0, 10, 0, 8)`` (``e = 8``, ``L0 = 3``, ``L1 = 4``, ``F = 4``):
  the note proves ``L1(W^t) = 3t + 1`` exactly while
  ``B(W^t) = F(W^t) = 4t``, so the decomposed bound is tight and the
  global one-ply bound falls behind by ``t - 1``.

Prototype space vs prune space (kept explicitly distinct):

* ``linear_extensions`` below is the *prototype exact tool*: a downset DP
  using ``O(2^n)`` space.  It is used for the exact ``e``/``L0``/``L1``
  values in the bounded regression.
* ``capped_pair_census`` / ``prune_verdict`` implement the *optional capped
  linear-extension polynomial-space prune* of
  ``docs/research-one-ply-obstruction.md` §2: it enumerates linear
  extensions with a cap of ``2^d + 1`` using ``O(n^2 (d+1))`` bits of
  counters plus an ``O(n)``-deep stack -- polynomial space, ``O(2^d n^2)``
  time -- and never allocates the ``O(2^n)`` downset array.

Everything here is an *experiment* on finite posets plus the proved
inequalities of the note.  No complexity-class, ``S(12)``, or
polynomial-time claim is made; ``e(P)`` is #P-complete to compute exactly
in general.  Reproduce with ``python3 scripts/compositional_lookahead.py``.
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
# The bounds L0, L1, Lr and the compositional bound B
# ---------------------------------------------------------------------------


def L0(succ: tuple[int, ...]) -> int:
    """Information bound ``ceil(log2 e(P))``."""
    return ceil_log2(linear_extensions(succ))


def L1(succ: tuple[int, ...]) -> int:
    """One-ply adversarial information bound (global, single state)."""
    pairs = incomparable_pairs(succ)
    if not pairs:
        return 0
    return 1 + min(
        max(L0(add_relation(succ, i, j)), L0(add_relation(succ, j, i)))
        for i, j in pairs
    )


_LR_MEMO: dict[tuple[tuple[int, ...], int], int] = {}


def Lr(succ: tuple[int, ...], r: int) -> int:
    """Horizon-``r`` adversarial information bound: ``r`` minimax plies,
    leaves scored by ``L0``.  ``Lr(P, 0) = L0(P)``, ``Lr(P, 1) = L1(P)``."""
    if r < 0:
        raise ValueError("r must be nonnegative")
    key = (succ, r)
    if key in _LR_MEMO:
        return _LR_MEMO[key]
    pairs = incomparable_pairs(succ)
    if not pairs or r == 0:
        val = 0 if not pairs else L0(succ)
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


def B(succ: tuple[int, ...]) -> int:
    """Compositional one-ply bound ``sum_i L1(P_i)`` over series factors."""
    return sum(L1(induced(succ, c)) for c in incomparability_components(succ))


# ---------------------------------------------------------------------------
# The two families
# ---------------------------------------------------------------------------

# Smallest strict one-ply witness (docs/research-one-ply-obstruction.md).
N5_WITNESS = (26, 0, 10, 0, 8)

# Q = Merge(2, 1): a 2-chain disjoint union (||) a singleton; e = 3, F = 2.
Q_MERGE_2_1 = (2, 0, 0)


# ---------------------------------------------------------------------------
# Optional capped linear-extension polynomial-space prune
# ---------------------------------------------------------------------------


def capped_pair_census(
    succ: tuple[int, ...], d: int
) -> tuple[int | None, list[list[int]] | None]:
    """Polynomial-space capped linear-extension census (note §7).

    Returns ``(e, c)`` where ``e`` is the exact number of linear extensions
    when it is ``<= 2**d`` and ``None`` otherwise (meaning: more than
    ``2**d`` extensions exist), and ``c[i][j]`` is the number of
    extensions with ``i`` before ``j`` (meaningful only when ``e`` is not
    ``None``).

    Complexity (amortized). Every prefix of a linear extension of a finite
    poset extends to at least one whole extension, so a depth-``n`` DFS
    that stops after ``2^d + 1`` leaves visits at most
    ``n * (2^d + 1)`` prefixes; each prefix tests ``O(n)`` candidate
    minimal elements against predecessor masks and each leaf does
    ``O(n^2)`` counter work, giving conservative worst-case time
    ``O(n^2 * 2^d)``. Space: ``O(n^2 (d + 1))`` bits of counters plus an
    ``O(n)``-deep recursion stack -- polynomial space.  No ``O(2^n)``
    full-downset array is allocated anywhere here (contrast with the
    prototype exact tool ``linear_extensions``, which does allocate one).
    """
    if d < 0:
        raise ValueError("d must be nonnegative")
    n = len(succ)
    pred = [0] * n
    for i in range(n):
        for j in range(n):
            if (succ[i] >> j) & 1:
                pred[j] |= 1 << i
    limit = 1 << d
    full = (1 << n) - 1
    count = 0
    over = False
    c = [[0] * n for _ in range(n)]
    order = [0] * n

    def rec(placed: int, pos: int) -> None:
        nonlocal count, over
        if over:
            return
        if placed == full:
            count += 1
            if count > limit:
                over = True
                return
            for a in range(n):
                ca = c[order[a]]
                for b in range(a + 1, n):
                    ca[order[b]] += 1
            return
        m = full & ~placed
        while m:
            x = (m & -m).bit_length() - 1
            m &= m - 1
            if (pred[x] & ~placed) == 0:
                order[pos] = x
                rec(placed | (1 << x), pos + 1)
                if over:
                    return

    rec(0, 0)
    if over:
        return None, None
    return count, c


def prune_verdict(succ: tuple[int, ...], d: int) -> bool | None:
    """Optional capped linear-extension polynomial-space L1 prune.

    Returns ``False`` when ``L1(succ) > d`` (sound: ``F(succ) > d`` by the
    one-ply theorem), ``None`` when inconclusive.  Exactly the §2 rule of
    ``docs/research-one-ply-obstruction.md``: with ``e <= 2^d`` extensions
    enumerated, ``L1 > d`` iff every incomparable pair has
    ``max(c_ij, e - c_ij) > 2^(d-1)``; if more than ``2^d`` extensions are
    seen the ordinary information bound already rejects.

    Edge cases. A total poset has no incomparable pairs and ``F = 0 <= d``
    for every ``d >= 0``, so it is never rejected (returns ``None``).  At
    ``d = 0`` the threshold is ``0`` and the prune fires exactly on the
    non-total posets, matching ``L1 > 0``; ``d < 0`` rejects outright.
    """
    if d < 0:
        return False
    pairs = incomparable_pairs(succ)
    if not pairs:
        return None
    e, c = capped_pair_census(succ, d)
    if e is None:
        return False
    thresh = (1 << (d - 1)) if d >= 1 else 0
    for i, j in pairs:
        if max(c[i][j], e - c[i][j]) <= thresh:
            return None
    return False


# ---------------------------------------------------------------------------
# Bounded fast regression: the chain L0 <= L1 <= B <= F
# ---------------------------------------------------------------------------


def regression_chain(max_n: int) -> dict[str, object]:
    """Check ``L0 <= L1 <= B <= F`` for every poset on ``n <= max_n`` elements.

    Also records where the decomposed bound is strictly stronger than the
    global one-ply bound (``B > L1``).  Returns a summary dict; raises
    ``AssertionError`` on any violation.
    """
    rows: list[dict[str, object]] = []
    for n in range(1, max_n + 1):
        total = strict = 0
        for P in all_posets(n):
            l0, l1, b, f = L0(P), L1(P), B(P), minimax(P)
            assert l0 <= l1, f"L0 > L1 at n={n}: P={P}"
            assert l1 <= b, f"L1 > B at n={n}: P={P}"
            assert b <= f, f"B > F at n={n}: P={P}"
            total += 1
            if b > l1:
                strict += 1
        rows.append({"n": n, "posets": total, "strict_B_gt_L1": strict})
    return {"rows": rows}


# ---------------------------------------------------------------------------
# Witness family W^t: exact global L1 = 3t + 1 vs decomposed B = F = 4t
# ---------------------------------------------------------------------------


def witness_report(t_max: int) -> list[dict[str, object]]:
    """Finite checks for the series powers ``W^t``, ``1 <= t <= t_max``.

    Direct exact computation of ``e``, ``L0``, global ``L1``, ``B`` and
    ``F`` (``F`` via ordinal-sum additivity from ``F(W) = 4``).  For
    ``t >= 3`` the direct global ``L1`` at ``n = 5t`` is replaced by the
    proved value ``3t + 1`` plus a direct check of the two representative
    pair children (extension counts ``5*8^(t-1)``, ``3*8^(t-1)``,
    ``6*8^(t-1)``, ``2*8^(t-1)``) that the proof reduces to.
    """
    rows: list[dict[str, object]] = []
    for t in range(1, t_max + 1):
        P = series_power(N5_WITNESS, t)
        e = linear_extensions(P)
        row: dict[str, object] = {
            "t": t,
            "n": len(P),
            "e": e,
            "L0": L0(P),
            "B": B(P),
            "F": t * minimax(N5_WITNESS),
        }
        assert e == 8**t, (t, e)
        assert row["L0"] == 3 * t, (t, row["L0"])
        assert row["B"] == 4 * t, (t, row["B"])
        assert row["F"] == 4 * t, (t, row["F"])
        if t <= 2:
            row["L1"] = L1(P)
            assert row["L1"] == 3 * t + 1, (t, row["L1"])
        else:
            # Mechanism check: children of the representative pairs {0,2}
            # (split 5/3) and {2,4} (split 6/2) inside the first copy.
            for (i, j), lo, hi in (((0, 2), 3, 5), ((2, 4), 2, 6)):
                e_lo = linear_extensions(add_relation(P, j, i))
                e_hi = linear_extensions(add_relation(P, i, j))
                assert e_lo == lo * 8 ** (t - 1), (t, i, j, e_lo)
                assert e_hi == hi * 8 ** (t - 1), (t, i, j, e_hi)
            row["L1"] = 3 * t + 1
            row["L1_method"] = "proved formula + representative pair children"
        row["gap_B_minus_L1"] = 4 * t - (3 * t + 1)
        rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# Amplification: e(Q^t) = e(Q)^t, F(Q^t) = t F(Q), Lr <= ceil(t log e(Q)) + r
# ---------------------------------------------------------------------------


def amplification_report(r_max: int, t_direct_max: int = 3) -> dict[str, object]:
    """Check the amplification bounds and the no-fixed-horizon witnesses.

    Directly verifies ``e(Q^t) = 3^t`` and ``Lr(Q^t, r) <= ceil(t log2 3) + r``
    for ``t <= t_direct_max``, ``r <= 2`` (small ``n = 3t``), and computes,
    for each horizon ``r <= r_max``, the minimal ``t`` with
    ``ceil(t log2 3) + r < 2t`` -- a series power where horizon ``r`` is
    provably strictly below ``F``.
    """
    Q = Q_MERGE_2_1
    e_q = linear_extensions(Q)
    f_q = minimax(Q)
    assert (e_q, f_q) == (3, 2), (e_q, f_q)
    direct: list[dict[str, object]] = []
    for t in range(1, t_direct_max + 1):
        P = series_power(Q, t)
        assert linear_extensions(P) == e_q**t, (t, linear_extensions(P))
        assert t * f_q == t * minimax(Q)
        for r in range(0, 3):
            bound = ceil_log2(e_q**t) + r
            val = Lr(P, r)
            assert val <= bound, (t, r, val, bound)
            direct.append({"t": t, "r": r, "Lr": val, "bound": bound})
    no_fixed_horizon: list[dict[str, object]] = []
    for r in range(0, r_max + 1):
        t = 1
        while not (ceil_log2(3**t) + r < 2 * t):
            t += 1
        no_fixed_horizon.append(
            {
                "r": r,
                "t_min": t,
                "Lr_bound": ceil_log2(3**t) + r,
                "F": 2 * t,
            }
        )
    return {
        "Q": Q,
        "e_Q": e_q,
        "F_Q": f_q,
        "direct": direct,
        "no_fixed_horizon": no_fixed_horizon,
    }


# ---------------------------------------------------------------------------
# Prune regression: soundness and exact equivalence with L1 > d
# ---------------------------------------------------------------------------


def prune_report(max_n: int, d_max: int) -> dict[str, object]:
    """Check the capped polynomial-space prune on all posets ``n <= max_n``.

    For every poset and ``0 <= d <= d_max``: ``prune_verdict`` returns
    ``False`` iff ``L1 > d`` (exact equivalence), and whenever it returns
    ``False``, ``F > d`` (soundness).  Also checks that the prune fires at
    the ``n = 5`` witness ``W`` for ``d = 3`` even though ``e(W) = 8 <=
    2^3`` (strictly stronger than the ordinary information prune), and that
    it is inconclusive at ``d = 4 = L1(W)``.
    """
    checked = equivalent = fired = 0
    for n in range(1, max_n + 1):
        for P in all_posets(n):
            for d in range(0, d_max + 1):
                v = prune_verdict(P, d)
                fires = L1(P) > d
                assert (v is False) == fires, (n, P, d, v, fires)
                if v is False:
                    assert minimax(P) > d, (n, P, d)
                    fired += 1
                checked += 1
                equivalent += 1
    w = N5_WITNESS
    assert prune_verdict(w, 3) is False
    assert linear_extensions(w) == 8 <= 2**3
    assert prune_verdict(w, 4) is None
    return {
        "max_n": max_n,
        "d_max": d_max,
        "checked": checked,
        "equivalent": equivalent,
        "fired": fired,
        "witness_d3": "fires (e = 8 <= 2^3, so the info prune is silent)",
        "witness_d4": "inconclusive (L1 = 4 <= 4)",
    }


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regression-max-n", type=int, default=4,
                        help="exhaustive chain-regression cap (default 4)")
    parser.add_argument("--witness-t", type=int, default=2,
                        help="largest series power W^t checked directly (default 2, max 3)")
    parser.add_argument("--amplification-r", type=int, default=5,
                        help="largest horizon r in the no-fixed-horizon table (default 5)")
    parser.add_argument("--prune", action="store_true",
                        help="also run the capped polynomial-space prune regression")
    parser.add_argument("--prune-max-n", type=int, default=4)
    parser.add_argument("--prune-d-max", type=int, default=4)
    args = parser.parse_args()
    if not 1 <= args.regression_max_n <= 5:
        raise SystemExit("regression-max-n is bounded to 1..5 by design")
    if not 1 <= args.witness_t <= 3:
        raise SystemExit("witness-t is bounded to 1..3 by design (no n >= 15 search)")

    print("=== Compositional one-ply lower bounds (experimental) ===")
    print("Prototype e-DP space: O(2^n); prune space: O(n^2 (d+1)) bits.\n")

    t0 = time.time()
    reg = regression_chain(args.regression_max_n)
    print(f"Chain regression L0 <= L1 <= B <= F, n <= {args.regression_max_n}:")
    for row in reg["rows"]:
        print(f"  n={row['n']}: posets={row['posets']} "
              f"strict B>L1={row['strict_B_gt_L1']}")
    print(f"  ({round(time.time() - t0, 2)} s)\n")

    t0 = time.time()
    print(f"Witness family W^t (W = {N5_WITNESS}):")
    for row in witness_report(args.witness_t):
        print(f"  t={row['t']}: n={row['n']} e={row['e']} L0={row['L0']} "
              f"L1={row['L1']} B={row['B']} F={row['F']} "
              f"gap B-L1={row['gap_B_minus_L1']}")
    print(f"  ({round(time.time() - t0, 2)} s)\n")

    t0 = time.time()
    amp = amplification_report(args.amplification_r)
    print(f"Amplification for Q = Merge(2,1) = {amp['Q']} "
          f"(e={amp['e_Q']}, F={amp['F_Q']}):")
    print("  direct Lr(Q^t, r) <= ceil(t log2 3) + r checks: "
          f"{len(amp['direct'])} ok")
    print("  no-fixed-horizon witnesses (minimal t per r):")
    for row in amp["no_fixed_horizon"]:
        print(f"    r={row['r']}: t={row['t_min']} gives "
              f"Lr <= {row['Lr_bound']} < {row['F']} = F(Q^t)")
    print(f"  ({round(time.time() - t0, 2)} s)\n")

    if args.prune:
        t0 = time.time()
        rep = prune_report(args.prune_max_n, args.prune_d_max)
        print(f"Capped polynomial-space prune regression, n <= {rep['max_n']}, "
              f"d <= {rep['d_max']}:")
        print(f"  (prune False) == (L1 > d) in all {rep['equivalent']} checks; "
              f"fired {rep['fired']} times, always with F > d")
        print(f"  {rep['witness_d3']}; {rep['witness_d4']}")
        print(f"  ({round(time.time() - t0, 2)} s)")


if __name__ == "__main__":
    main()
