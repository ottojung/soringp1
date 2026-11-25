#!/usr/bin/env python3
"""Structural lower bounds for the exact minimax sorting number.

Companion program for ``docs/research-structural-lower-bounds.md``.  It is an
*experimental* probe, not a proof and not a Lean file.  Model: adaptive
worst-case pairwise-comparison sorting of ``n`` distinct labelled keys.  A
state is a transitively closed strict partial order on ``{0, ..., n-1}``,
represented by a tuple ``succ`` where ``succ[i]`` is the bitmask of elements
strictly greater than ``i``.

Definitions (see the note for proofs and provenance):

* ``F(P)`` = minimum remaining worst-case comparisons that sorts every linear
  extension of ``P`` (``minimax`` below); ``F(antichain_n) = S(n)``.
* ``e(P)`` = number of linear extensions of ``P`` (``linear_extensions``).
* ``ceil_log2(e)`` = node-level information lower bound for ``F`` at ``P``.
* ``Merge(a, b)`` = disjoint union of an ``a``-chain and a ``b``-chain
  (parallel composition, *no* cross relations); ``F(Merge(a, b)) = M(a, b)``
  is the exact minimum worst-case two-list merge cost.
* ``delta(a, b) = M(a, b) - ceil_log2 C(a+b, a)`` >= 0 is the *merge gap*:
  the amount by which the exact merge cost beats leaf counting.

The two mathematical contents checked here:

* Theorem A (extension monotonicity): ``P subseteq Q => F(P) >= F(Q)``.
  Verified computationally for every *cover* ``P < Q`` on ``n <= 5``;
  monotonicity for arbitrary comparable pairs follows by transitivity.
* Theorem B (merge-factor compositional lower bound): if the ordinal-sum
  (series) decomposition of ``P`` contains certified non-tight merge factors
  ``Merge(a_i, b_i)`` with gaps ``delta_i > 0``, then
  ``F(P) >= sum_i ceil(log2 e(P_i)) + sum_i delta_i``, strictly stronger than the
  information bound.  Checked for every poset on ``n <= 5`` (no strict
  witness occurs below ``n = 6``); the smallest strict witness is
  ``Merge(2, 4)`` on ``n = 6``, where ``e = 15``, ``ceil(log2 15) = 4`` and
  ``F = 5``.  Targeted ``n = 6`` merge states are also checked.

Certified merge values (literature ranges; no universal ``a+b-1`` formula is
assumed):

* ``a = 1``: ``M(1, b) = ceil(log2(b+1))`` (Hwang-Lin 1972).
* tape range ``a <= b <= floor(3a/2)+1``: ``M(a, b) = a+b-1``
  (Stockmeyer-Yao 1980; Christen 1978; Murphy-Paull 1979).
* outside these ranges the value is ``None`` (not certified here); exact
  minimax values used in the *targeted* experiments are labelled
  ``[experiment]`` in the note.

Reproduce with ``python3 scripts/structural_lower_bounds.py``.
"""

from __future__ import annotations

import argparse
import time
from functools import lru_cache
from math import comb

# ---------------------------------------------------------------------------
# Poset machinery (self-contained; same representation as the other probes)
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


def chain(k: int) -> tuple[int, ...]:
    """A ``k``-element chain."""
    return tuple(sum(1 << t for t in range(i + 1, k)) for i in range(k))


def ordinal_sum(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Ordinal sum ``p (+) q``: every element of ``p`` below every of ``q``."""
    a = len(p)
    top_mask = ((1 << (a + len(q))) - 1) ^ ((1 << a) - 1)
    return tuple(s | top_mask for s in p) + tuple(s << a for s in q)


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


def ordered_blocks(succ: tuple[int, ...]) -> list[list[int]]:
    """Ordinal-sum blocks, ordered bottom-to-top (raises if not a sum)."""
    comps = incomparability_components(succ)

    def below(a: list[int], b: list[int]) -> bool:
        return all(succ[x] & (1 << y) for x in a for y in b)

    ordered = list(comps)
    for i in range(1, len(ordered)):
        key = ordered[i]
        j = i - 1
        while j >= 0 and below(key, ordered[j]):
            ordered[j + 1] = ordered[j]
            j -= 1
        ordered[j + 1] = key
    for a in range(len(ordered)):
        for b in range(a + 1, len(ordered)):
            if not below(ordered[a], ordered[b]):
                raise ValueError("state is not an ordinal sum of its components")
    return ordered


# ---------------------------------------------------------------------------
# Merge-factor recognition and certified merge values
# ---------------------------------------------------------------------------


def comparability_components(succ: tuple[int, ...]) -> list[list[int]]:
    """Connected components of the comparability graph."""
    n = len(succ)
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(n):
        for j in range(i + 1, n):
            if (succ[i] >> j) & 1 or (succ[j] >> i) & 1:
                ri, rj = find(i), find(j)
                if ri != rj:
                    parent[ri] = rj
    comps: dict[int, list[int]] = {}
    for i in range(n):
        comps.setdefault(find(i), []).append(i)
    return list(comps.values())


def is_clique(succ: tuple[int, ...], comp: list[int]) -> bool:
    k = len(comp)
    edges = sum(
        1
        for x in comp
        for y in comp
        if x < y and ((succ[x] >> y) & 1 or (succ[y] >> x) & 1)
    )
    return edges == k * (k - 1) // 2


def is_chain(succ: tuple[int, ...]) -> bool:
    """True iff every distinct pair is comparable (a total order)."""
    return not incomparable_pairs(succ)


def merge_factor(succ: tuple[int, ...]) -> tuple[int, int] | None:
    """Return ``(a, b)``, ``a <= b``, iff ``succ`` is ``Merge(a, b)``.

    ``Merge(a, b)`` is exactly a poset whose comparability graph is a disjoint
    union of two cliques (each clique is a chain, cross pairs incomparable).
    This is a *certification*: an arbitrary interleaving of two chains that
    fails the two-clique test is not a merge factor.
    """
    comps = comparability_components(succ)
    if len(comps) != 2 or not all(is_clique(succ, c) for c in comps):
        return None
    return tuple(sorted((len(comps[0]), len(comps[1]))))  # type: ignore[return-value]


def certified_merge_value(a: int, b: int) -> int | None:
    """Certified exact ``M(a, b)`` from literature ranges, else ``None``.

    * ``a = 1``: ``M(1, b) = ceil(log2(b+1))`` (Hwang-Lin 1972).
    * tape range ``a <= b <= floor(3a/2)+1``: ``M(a, b) = a+b-1``
      (Stockmeyer-Yao 1980; Christen 1978; Murphy-Paull 1979).
    """
    a, b = min(a, b), max(a, b)
    if a < 1:
        return None
    if a == 1:
        return ceil_log2(b + 1)
    if b <= (3 * a) // 2 + 1:
        return a + b - 1
    return None


def merge_gap(a: int, b: int) -> int | None:
    """Certified gap ``delta(a, b) = M(a, b) - ceil(log2 C(a+b, a))``."""
    m = certified_merge_value(a, b)
    if m is None:
        return None
    return m - ceil_log2(comb(a + b, a))


# ---------------------------------------------------------------------------
# Theorem B: structural analysis of a state
# ---------------------------------------------------------------------------


def analyze(succ: tuple[int, ...]) -> dict:
    """Series decomposition plus certified merge gaps for a state.

    Returns a dict with the factor list, the total certified gap, the
    information bound and the structural bound ``ceil(log2 e) + total gap``.
    """
    e = linear_extensions(succ)
    info = ceil_log2(e)
    factors: list[dict] = []
    total_delta = 0
    block_info_sum = 0
    for block in ordered_blocks(succ):
        if len(block) <= 1:
            factors.append({"kind": "singleton", "size": 1})
            continue
        sub = induced(succ, block)
        block_info_sum += ceil_log2(linear_extensions(sub))
        mf = merge_factor(sub)
        if mf is not None:
            a, b = mf
            m = certified_merge_value(a, b)
            gap = merge_gap(a, b)
            if gap is None:
                # Uncertified merge cost: do not claim a gap.
                factors.append(
                    {
                        "kind": "merge-uncertified",
                        "sizes": (a, b),
                        "M": None,
                        "delta": 0,
                    }
                )
            else:
                total_delta += gap
                factors.append(
                    {"kind": "merge", "sizes": (a, b), "M": m, "delta": gap}
                )
        elif is_chain(sub):
            factors.append({"kind": "chain", "size": len(block)})
        else:
            factors.append(
                {"kind": "other", "size": len(block), "e": linear_extensions(sub)}
            )
    return {
        "e": e,
        "info": info,
        "total_delta": total_delta,
        "block_info_sum": block_info_sum,
        "bound": block_info_sum + total_delta,
        "factors": factors,
        "F": minimax(succ),
    }


# ---------------------------------------------------------------------------
# Theorem A: monotonicity, checked on covers
# ---------------------------------------------------------------------------


def covers(succ: tuple[int, ...]):
    """States obtained by adding one comparability (and its transitives)."""
    for i, j in incomparable_pairs(succ):
        yield add_relation(succ, i, j)
        yield add_relation(succ, j, i)


def check_monotonicity_covers(max_n: int) -> tuple[int, int]:
    """Check ``F(P) >= F(Q)`` for every cover ``P < Q``, ``n <= max_n``.

    Every comparable pair ``P subseteq Q`` is linked by a cover chain, so
    cover-monotonicity plus transitivity is full monotonicity on this range.
    """
    checked = failures = 0
    for n in range(max_n + 1):
        for p in all_posets(n):
            fp = minimax(p)
            for q in covers(p):
                checked += 1
                if fp < minimax(q):
                    failures += 1
    return checked, failures


# ---------------------------------------------------------------------------
# Theorem B: the structural bound on all posets of a given size
# ---------------------------------------------------------------------------


def check_bound(max_n: int) -> list[dict]:
    """For every poset on ``n <= max_n`` elements check ``F >= bound >= info``.

    Returns per-size statistics including the number of states where the
    structural bound is *strictly* stronger than the information bound.
    """
    rows = []
    for n in range(max_n + 1):
        total = strict = failures = 0
        examples: list[tuple] = []
        for p in all_posets(n):
            an = analyze(p)
            if an["F"] < an["info"] or an["F"] < an["bound"]:
                failures += 1
            total += 1
            if an["bound"] > an["info"]:
                strict += 1
                if len(examples) < 3:
                    examples.append(
                        (p, an["e"], an["info"], an["bound"], an["F"])
                    )
        rows.append(
            {
                "n": n,
                "posets": total,
                "failures": failures,
                "strict": strict,
                "examples": examples,
            }
        )
    return rows


# ---------------------------------------------------------------------------
# Targeted witnesses (plain minimax, no decomposition used)
# ---------------------------------------------------------------------------


def smallest_strict_witness() -> dict:
    """The smallest poset where the structural bound beats leaf counting.

    Exhaustive enumeration for ``n <= 5`` has no strict witness.  On ``n = 6``
    the unique strict witness up to relabelling is ``Merge(2, 4)``: it has
    ``e = 15`` linear extensions, ``ceil(log2 15) = 4`` and ``F = 5``.
    """
    p = chains_union((2, 4))
    an = analyze(p)
    assert an["bound"] > an["info"], an
    return {"poset": p, **an}


def targeted() -> list[dict]:
    """Targeted ``n = 6`` merge witnesses verified by the plain minimax evaluator.

    Only ``n <= 6`` states are included: the plain minimax evaluator is
    exponential, and the task scope is exhaustive ``n <= 5`` plus targeted
    ``n = 6``.
    """
    states = {
        "Merge(1,5)": chains_union((1, 5)),
        "Merge(2,4)": chains_union((2, 4)),
        "Merge(3,3)": chains_union((3, 3)),
        "Merge(2,3) (+) singleton": ordinal_sum(chains_union((2, 3)), (0,)),
        "Merge(2,2) (+) singleton (+) singleton": ordinal_sum(
            ordinal_sum(chains_union((2, 2)), (0,)), (0,)
        ),
    }
    out = []
    for name, p in states.items():
        t0 = time.time()
        an = analyze(p)
        out.append(
            {
                "name": name,
                "n": len(p),
                "e": an["e"],
                "info": an["info"],
                "bound": an["bound"],
                "F": an["F"],
                "factors": an["factors"],
                "seconds": round(time.time() - t0, 3),
            }
        )
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--monotonicity-up-to", type=int, default=5)
    parser.add_argument("--bound-up-to", type=int, default=5)
    args = parser.parse_args()

    print("=== Structural lower bounds probe (experimental) ===")

    t0 = time.time()
    checked, failures = check_monotonicity_covers(args.monotonicity_up_to)
    print(
        f"\nTheorem A (monotonicity on covers, n <= {args.monotonicity_up_to}): "
        f"{checked} cover checks, {failures} failures "
        f"({round(time.time() - t0, 2)} s)"
    )

    t0 = time.time()
    print(
        f"\nTheorem B (structural bound F >= ceil(log2 e) + sum delta, "
        f"n <= {args.bound_up_to}):"
    )
    for row in check_bound(args.bound_up_to):
        print(
            f"  n={row['n']}: posets={row['posets']} failures={row['failures']} "
            f"strict={row['strict']}"
        )
        for p, e, info, bound, f_val in row["examples"]:
            print(
                f"      strict witness {p}: e={e} info={info} "
                f"bound={bound} F={f_val}"
            )
    print(f"  ({round(time.time() - t0, 2)} s)")

    witness = smallest_strict_witness()
    print(
        f"\nSmallest strict witness (structural bound beats leaf counting):\n"
        f"  {witness['poset']}: e={witness['e']} info={witness['info']} "
        f"bound={witness['bound']} F={witness['F']}"
    )

    print("\nTargeted n = 6 merge witnesses (plain minimax):")
    for row in targeted():
        fac = ", ".join(
            f"{f['kind']}{f.get('sizes', f.get('size', ''))}"
            for f in row["factors"]
        )
        print(
            f"  {row['name']}: n={row['n']} e={row['e']} info={row['info']} "
            f"bound={row['bound']} F={row['F']} [{fac}] "
            f"({row['seconds']} s)"
        )


if __name__ == "__main__":
    main()
