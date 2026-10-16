#!/usr/bin/env python3
"""Exact partial-order minimax reference for small n (not a Lean proof)."""

import argparse
from functools import cache


def sorting_number(n: int) -> int:
    """Minimum worst-case comparisons for n distinct labelled keys."""
    if n < 0:
        raise ValueError("n must be nonnegative")

    def extend(successors: tuple[int, ...], i: int, j: int) -> tuple[int, ...]:
        """Transitive closure after adding i < j to an already closed state."""
        out = list(successors)
        new_greater = successors[j] | (1 << j)
        for x in range(n):
            if x == i or (successors[x] & (1 << i)):
                out[x] |= new_greater
        return tuple(out)

    @cache
    def solve(successors: tuple[int, ...]) -> int:
        pairs = [
            (i, j)
            for i in range(n)
            for j in range(i + 1, n)
            if not (successors[i] & (1 << j))
            and not (successors[j] & (1 << i))
        ]
        if not pairs:
            return 0
        return 1 + min(
            max(solve(extend(successors, i, j)),
                solve(extend(successors, j, i)))
            for i, j in pairs
        )

    return solve((0,) * n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int)
    print(sorting_number(parser.parse_args().n))
