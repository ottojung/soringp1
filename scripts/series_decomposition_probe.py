#!/usr/bin/env python3
"""Series (ordinal-sum) decomposition of the exact minimax sorting number.

This is an *experimental* probe, not a proof.  It checks the candidate rule

    F(A (+) B) = F(A) + F(B)          (ordinal sum of posets)

where F(P) is the worst-case minimum number of further pairwise comparisons
needed to identify the unknown linear extension of the poset P (the exact
query complexity of "sorting under partial information", SUPI).  For the
antichain on n elements, F(antichain_n) = S(n).

Posets are represented as a tuple of n bitmasks ``successors``: bit j of
``successors[i]`` is set iff i < j in the transitive closure.  The representation
is already transitively closed, so detecting an ordinal-sum cut is a graph
computation on the incomparability graph (complement of the comparability
graph), which is O(n^2).

The probe is bounded to n <= 5 so that it never competes with other agents'
n >= 6 exhaustive searches.
"""

from __future__ import annotations

import argparse
import time
from itertools import permutations

# ---------------------------------------------------------------------------
# Basic poset machinery
# ---------------------------------------------------------------------------


def extend(successors: tuple[int, ...], i: int, j: int) -> tuple[int, ...]:
    """Transitive closure after adding i < j to an already closed state."""
    out = list(successors)
    new_greater = successors[j] | (1 << j)
    for x in range(len(successors)):
        if x == i or (successors[x] & (1 << i)):
            out[x] |= new_greater
    return tuple(out)


def incomparability_components(successors: tuple[int, ...]) -> list[list[int]]:
    """Connected components of the incomparability graph.

    Two elements are adjacent iff they are incomparable.  This is exactly the
    vertex partition of the unique ordinal-sum decomposition into ordinally
    indecomposable factors (Pouzet-Zaguia, Lemma 2.1; Erne-Stege 1995).
    """
    n = len(successors)
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(n):
        for j in range(i + 1, n):
            if not (successors[i] & (1 << j)) and not (successors[j] & (1 << i)):
                ri, rj = find(i), find(j)
                if ri != rj:
                    parent[ri] = rj
    comps: dict[int, list[int]] = {}
    for i in range(n):
        comps.setdefault(find(i), []).append(i)
    return list(comps.values())


def induced(successors: tuple[int, ...], subset: list[int]) -> tuple[int, ...]:
    """Induced subposet on ``subset``, relabelled to 0..m-1."""
    index = {e: k for k, e in enumerate(subset)}
    return tuple(
        sum((1 << index[j]) for j in subset if successors[i] & (1 << j))
        for i in subset
    )


def ordered_blocks(successors: tuple[int, ...]) -> list[list[int]]:
    """Ordinal-sum blocks, ordered bottom-to-top.

    Returns the connected components of the incomparability graph, sorted so
    that every element of an earlier block precedes every element of a later
    block.  Raises ValueError if the state is not a genuine ordinal sum.
    """
    comps = incomparability_components(successors)
    if len(comps) == 1:
        return comps

    def below(a: list[int], b: list[int]) -> bool:
        return all(successors[x] & (1 << y) for x in a for y in b)

    # The blocks are totally ordered by the poset order; insertion sort is
    # enough for the tiny sizes used here.
    ordered = list(comps)
    for i in range(1, len(ordered)):
        key = ordered[i]
        j = i - 1
        while j >= 0 and below(key, ordered[j]):
            ordered[j + 1] = ordered[j]
            j -= 1
        ordered[j + 1] = key
    # Verify the total order and the complete cross-block comparability.
    for a in range(len(ordered)):
        for b in range(a + 1, len(ordered)):
            if not below(ordered[a], ordered[b]):
                raise ValueError("state is not an ordinal sum of its components")
    return ordered


def is_series_prime(successors: tuple[int, ...]) -> bool:
    """True iff the incomparability graph is connected."""
    return len(incomparability_components(successors)) == 1


# ---------------------------------------------------------------------------
# Exact minimax evaluator
# ---------------------------------------------------------------------------


class Minimax:
    """Memoised exact evaluator over variable-size poset states."""

    def __init__(self, use_decomposition: bool = False) -> None:
        self.use_decomposition = use_decomposition
        self.memo: dict[tuple[int, ...], int] = {}
        self.expansions = 0
        self.decomposition_hits = 0

    def solve(self, successors: tuple[int, ...]) -> int:
        if successors in self.memo:
            return self.memo[successors]
        if self.use_decomposition and len(successors) > 1:
            comps = incomparability_components(successors)
            if len(comps) > 1:
                self.decomposition_hits += 1
                value = sum(self.solve(induced(successors, c)) for c in comps)
                self.memo[successors] = value
                return value
        pairs = [
            (i, j)
            for i in range(len(successors))
            for j in range(i + 1, len(successors))
            if not (successors[i] & (1 << j)) and not (successors[j] & (1 << i))
        ]
        if not pairs:
            self.memo[successors] = 0
            return 0
        self.expansions += 1
        best = min(
            1 + max(self.solve(extend(successors, i, j)),
                    self.solve(extend(successors, j, i)))
            for i, j in pairs
        )
        self.memo[successors] = best
        return best


def sorting_number(n: int, use_decomposition: bool = False) -> int:
    """F(antichain_n) = S(n)."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    return Minimax(use_decomposition).solve((0,) * n)


# ---------------------------------------------------------------------------
# Enumeration of all posets reachable from the antichain
# ---------------------------------------------------------------------------


def all_posets(n: int) -> set[tuple[int, ...]]:
    seen = {(0,) * n}
    frontier = [(0,) * n]
    while frontier:
        nxt = []
        for s in frontier:
            for i in range(n):
                for j in range(i + 1, n):
                    if not (s[i] & (1 << j)) and not (s[j] & (1 << i)):
                        for t in (extend(s, i, j), extend(s, j, i)):
                            if t not in seen:
                                seen.add(t)
                                nxt.append(t)
        frontier = nxt
    return seen


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------


def verify_additivity(n: int) -> tuple[int, int]:
    """Check F(P) = sum F(block) for every poset on n labelled elements.

    Returns (checked, failures).
    """
    solver = Minimax()
    checked = failures = 0
    for s in all_posets(n):
        blocks = incomparability_components(s)
        if len(blocks) == 1:
            continue
        checked += 1
        total = sum(solver.solve(induced(s, c)) for c in blocks)
        if total != solver.solve(s):
            failures += 1
    return checked, failures


def verify_decomposition(n: int) -> tuple[int, int]:
    """Check that the incomparability components form an ordinal sum.

    Returns (checked, failures).
    """
    checked = failures = 0
    for s in all_posets(n):
        try:
            ordered_blocks(s)
        except ValueError:
            failures += 1
        else:
            checked += 1
    return checked, failures


def subset_counterexample() -> tuple[int, int, int]:
    """A correlated subset of an ordinal sum where additivity fails.

    P = A (+) B with A = B = antichain on two elements.  The full product has
    F = 2, but the correlated subset {0123, 1032} has F = 1 while each
    projection has F = 1, so 1 < 1 + 1.
    """

    def adv(perms: tuple[tuple[int, ...], ...]) -> int:
        perms = frozenset(perms)
        if len(perms) <= 1:
            return 0
        m = len(next(iter(perms)))
        pairs = [
            (i, j)
            for i in range(m)
            for j in range(i + 1, m)
            if any(p[i] < p[j] for p in perms) and any(p[j] < p[i] for p in perms)
        ]
        if not pairs:
            return 0
        return 1 + min(
            max(adv(tuple(p for p in perms if p[i] < p[j])),
                adv(tuple(p for p in perms if p[j] < p[i])))
            for i, j in pairs
        )

    # L(A (+) B): the two A-elements occupy the two smallest positions.
    full = tuple(
        p for p in permutations(range(4))
        if max(p.index(0), p.index(1)) < min(p.index(2), p.index(3))
    )
    sub = ((0, 1, 2, 3), (1, 0, 3, 2))
    return adv(full), adv(sub), adv(tuple(p[:2] for p in sub)) + adv(
        tuple(p[2:] for p in sub)
    )


def benchmark(n: int) -> dict[str, object]:
    out: dict[str, object] = {"n": n}
    for label, decomp in (("standard", False), ("decomposed", True)):
        t0 = time.time()
        solver = Minimax(decomp)
        value = solver.solve((0,) * n)
        out[label] = {
            "S": value,
            "states": len(solver.memo),
            "expansions": solver.expansions,
            "hits": solver.decomposition_hits,
            "seconds": round(time.time() - t0, 4),
        }
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=5)
    parser.add_argument("--verify-up-to", type=int, default=4,
                        help="enumerate all posets up to this n (bounded)")
    args = parser.parse_args()

    print("=== Series decomposition probe (bounded, experimental) ===")
    print("S(n) standard / decomposed:")
    for n in range(args.max_n + 1):
        row = benchmark(n)
        std, dec = row["standard"], row["decomposed"]
        assert std["S"] == dec["S"], (n, std, dec)
        print(
            f"  n={n}: S={std['S']} "
            f"(states {std['states']} -> {dec['states']}, "
            f"expansions {std['expansions']} -> {dec['expansions']}, "
            f"hits {dec['hits']})"
        )

    print("Additivity / decomposition verification:")
    for n in range(args.verify_up_to + 1):
        checked, failures = verify_additivity(n)
        dchecked, dfailures = verify_decomposition(n)
        print(
            f"  n={n}: additivity {checked - failures}/{checked} ok, "
            f"decomposition {dchecked - dfailures}/{dchecked} ok"
        )

    full, sub, projections = subset_counterexample()
    print(
        f"Subset counterexample: F(L(P))={full}, F(correlated S)={sub}, "
        f"F(S_A)+F(S_B)={projections}"
    )


if __name__ == "__main__":
    main()
