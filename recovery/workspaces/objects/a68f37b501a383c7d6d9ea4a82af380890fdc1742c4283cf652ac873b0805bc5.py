#!/usr/bin/env python3
"""Independent probe for the obstruction audit (docs/research-obstruction-next.md).

Self-contained; it deliberately does *not* import the staging draft in
``soring301-research``.  Model: adaptive worst-case pairwise-comparison sorting
of ``n`` distinct labelled keys.  A state is a transitively closed strict
partial order on ``{0, ..., n-1}``, represented by a tuple ``succ`` where
``succ[i]`` is the bitmask of elements strictly greater than ``i``.

Definitions used below:

* ``e(P)`` = number of linear extensions of ``P`` (``linear_extensions``).
* ``m(P)`` = minimum remaining worst-case comparisons to sort every linear
  extension of ``P`` (``minimax``); ``m(P) = 0`` iff ``P`` is a total order.
* ``ceil_log2(e)`` = information-theoretic lower bound for ``m`` at ``P``.
* ``width(P)`` = size of a maximum antichain.

Everything here is an *experiment* on finite posets; no complexity-class or
``S(12)`` conclusion is claimed.  Reproduce with ``python3
scripts/obstruction_probe.py``.
"""

from __future__ import annotations

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
    """Number of linear extensions, via a DP over downsets."""
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


def all_posets(n: int):
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
    """Minimum remaining worst-case comparisons (memoized)."""
    pairs = incomparable_pairs(succ)
    if not pairs:
        return 0
    return 1 + min(
        max(minimax(add_relation(succ, i, j)), minimax(add_relation(succ, j, i)))
        for i, j in pairs
    )


def minimax_all(n: int) -> dict[tuple[int, ...], int]:
    return {P: minimax(P) for P in all_posets(n)}


def ceil_log2(x: int) -> int:
    return (x - 1).bit_length()


def width(succ: tuple[int, ...]) -> int:
    """Maximum antichain size (brute force; intended for small ``n``)."""
    n = len(succ)
    best = 0
    for S in range(1 << n):
        c = bin(S).count("1")
        if c <= best:
            continue
        ok = True
        for i in range(n):
            if not (S >> i) & 1:
                continue
            for j in range(n):
                if i != j and (S >> j) & 1 and (succ[i] >> j) & 1:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            best = c
    return best


def chains_union(sizes) -> tuple[int, ...]:
    """Disjoint union of chains with the given sizes (a merge state)."""
    n = sum(sizes)
    succ = [0] * n
    off = 0
    for s in sizes:
        for t in range(s):
            for u in range(t + 1, s):
                succ[off + t] |= 1 << (off + u)
        off += s
    return tuple(succ)


# --------------------------------------------------------------------------
# Audit facts
# --------------------------------------------------------------------------

H3_WITNESS = (0, 0, 1, 3, 7)                 # n=5, e=8, m=4  (local ITLB failure)
H2_P1 = (20, 16, 0, 23, 0, 22)               # n=6, e=13, m=5
H2_P2 = (0, 37, 1, 39, 1, 0)                 # n=6, e=14, m=4
N6_E8_TIGHT = (2, 0, 43, 3, 43, 0)           # n=6, e=8, width=2, m=3
N5_E8_LOOSE = (26, 0, 10, 0, 8)              # n=5, e=8, width=2, m=4


def e_levels(max_n: int = 5) -> dict[int, set[int]]:
    """For ``n <= max_n``, map each ``e`` to the set of realised ``m`` values."""
    levels: dict[int, set[int]] = {}
    for n in range(1, max_n + 1):
        for P in all_posets(n):
            levels.setdefault(linear_extensions(P), set()).add(minimax(P))
    return levels


def first_local_failure(max_n: int = 5) -> int | None:
    """Smallest ``e`` with a poset on ``n <= max_n`` elements where m > ceil(log2 e)."""
    for e in sorted(e_levels(max_n)):
        if max(e_levels(max_n)[e]) > ceil_log2(e):
            return e
    return None


def same_e_different_m(max_n: int = 5) -> list[tuple[int, list[int]]]:
    """``e`` values whose posets realise more than one ``m`` (smallest first)."""
    return [
        (e, sorted(ms))
        for e, ms in sorted(e_levels(max_n).items())
        if len(ms) > 1
    ]


def merge_violations(max_total: int = 6) -> list[tuple[tuple[int, ...], int, int, int]]:
    """Two-chain merges ``Merge(a,b)`` whose exact ``m`` exceeds ``ceil(log2 e)``.

    ``m`` is computed by minimax (no formula).  Note ``M(a,b)`` is *not*
    universally ``a+b-1``; e.g. ``M(1,4) = 3`` and ``M(2,4) = 5``.
    """
    out = []
    for a in range(1, max_total + 1):
        for b in range(a, max_total + 1 - a):
            if a + b > max_total:
                continue
            P = chains_union((a, b))
            e, mv = linear_extensions(P), minimax(P)
            if mv > ceil_log2(e):
                out.append(((a, b), e, ceil_log2(e), mv))
    return out


def two_chain_merge_table(max_size: int = 6) -> list[tuple[int, int, int, int, int]]:
    """Exact ``M(a,b)`` for two-chain merges, ``a <= b <= max_size``.

    Returns ``(a, b, e, ceil_log2(e), M)`` with ``M`` computed by minimax, so
    no merge formula is assumed.  Used by the §3.3 table.
    """
    rows = []
    for a in range(1, max_size + 1):
        for b in range(a, max_size + 1):
            P = chains_union((a, b))
            e = linear_extensions(P)
            rows.append((a, b, e, ceil_log2(e), minimax(P)))
    return rows


def report() -> None:
    print("== Independent obstruction probe ==")
    print("\nH3 witness n=5:", H3_WITNESS,
          "e =", linear_extensions(H3_WITNESS),
          "m =", minimax(H3_WITNESS))
    print("H2 witnesses n=6: P1 e =", linear_extensions(H2_P1), "m =", minimax(H2_P1),
          "; P2 e =", linear_extensions(H2_P2), "m =", minimax(H2_P2))

    print("\nSame-e different-m levels for n <= 5:", same_e_different_m(5))
    print("First local failure (n <= 5): e =", first_local_failure(5))

    print("\n(e, width) collision at n = 6:")
    for name, P in (("tight", N6_E8_TIGHT), ("loose", N5_E8_LOOSE)):
        print(f"  {name}: n={len(P)} e={linear_extensions(P)} width={width(P)} m={minimax(P)}")

    print("\nDisjoint-union-of-chains (merge) local violations, total <= 6:")
    for sizes, e, lb, mv in merge_violations(6):
        print(f"  chains {sizes}: e={e} ceil(log2 e)={lb} m={mv}")

    print("\nTwo-chain merge table M(a,b), exact minimax (a <= b <= 6):")
    print(f"  {'(a,b)':>7} {'e':>6} {'ceil':>5} {'M':>4}  {'a+b-1':>6} {'tight':>6}")
    for a, b, e, lb, mv in two_chain_merge_table(6):
        print(f"  {str((a,b)):>7} {e:>6} {lb:>5} {mv:>4}  {a+b-1:>6} "
              f"{'yes' if mv <= lb else 'NO':>6}")


if __name__ == "__main__":
    report()
