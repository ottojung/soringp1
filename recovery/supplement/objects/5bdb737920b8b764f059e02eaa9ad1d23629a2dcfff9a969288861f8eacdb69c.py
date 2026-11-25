#!/usr/bin/env python3
"""Small witness that automorphism-orbit pruning need not shrink n² move sets."""

from itertools import permutations
from math import comb


def staircase(m: int) -> tuple[int, ...]:
    """Height-two poset b_i<t_j iff j<=i; bottoms precede tops."""
    if m < 1:
        raise ValueError("m must be positive")
    return tuple(sum(1 << (m + j) for j in range(i + 1))
                 for i in range(m)) + (0,) * m


def odd_staircase(m: int) -> tuple[int, ...]:
    """Ordinal sum of staircase(m) and a singleton greatest element."""
    s = staircase(m)
    n = len(s)
    return tuple(bits | (1 << n) for bits in s) + (0,)


def incomparable_pairs(s: tuple[int, ...]) -> list[tuple[int, int]]:
    return [(i, j) for i in range(len(s)) for j in range(i + 1, len(s))
            if not (s[i] & (1 << j)) and not (s[j] & (1 << i))]


def automorphism_count(s: tuple[int, ...]) -> int:
    """Independent brute-force automorphism verifier for n<=8 only."""
    n = len(s)
    if n > 8:
        raise ValueError("brute-force automorphisms limited to n<=8")
    count = 0
    for perm in permutations(range(n)):
        if all(bool(s[i] & (1 << j)) == bool(s[perm[i]] & (1 << perm[j]))
               for i in range(n) for j in range(n)):
            count += 1
    return count


def check(m: int) -> tuple[int, int, int]:
    s = staircase(m)
    actual = len(incomparable_pairs(s))
    expected = 3 * comb(m, 2)
    if actual != expected:
        raise AssertionError((m, actual, expected))
    aut = automorphism_count(s) if 2 * m <= 8 else -1
    if aut != -1 and aut != 1:
        raise AssertionError((m, aut))
    return (len(s), actual, aut)


def main() -> None:
    for m in (2, 3, 4):
        n, pairs, automorphisms = check(m)
        print(f"m={m} n={n}: incomparable={pairs}, automorphisms={automorphisms}")
    for m in (2, 3):
        s = odd_staircase(m)
        assert len(incomparable_pairs(s)) == 3 * comb(m, 2)
        assert automorphism_count(s) == 1
        print(f"odd n={len(s)}: incomparable={len(incomparable_pairs(s))}, "
              f"automorphisms=1")


if __name__ == "__main__":
    main()
