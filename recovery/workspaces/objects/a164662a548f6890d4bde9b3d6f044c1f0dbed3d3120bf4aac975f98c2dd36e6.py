#!/usr/bin/env python3
"""Probe for deliverable 3 (SoringP1 #301): restricted-family candidates.

Greedy-lexicographic strategy: at every non-total state, pick the
lexicographically smallest incomparable pair (the probe's `incomparable_pairs`
order, i.e. smallest (i, j) with i < j).  This is the "pure greedy" candidate
family; it is FO(TC)-expressible (local lex-min over the incomparable
relation), and its optimality is tested here against S(n) for n <= 6.
"""

import sys

sys.path.insert(0, "/home/lubko/soring301/scripts")

from strategy_dag_probe import (
    extend,
    incomparable_pairs,
    is_total,
    minimax_values,
)


def greedy_height(n):
    P = (0,) * n
    steps = 0
    while not is_total(P, n):
        pair = incomparable_pairs(P, n)[0]
        assert pair is not None
        P = extend(P, pair[0], pair[1])
        steps += 1
        if steps > 100:
            raise AssertionError("diverges")
    return steps


def main():
    print("greedy-lexicographic strategy height vs DP value S(n):")
    for n in range(0, 7):
        values = minimax_values(n)
        S = values[(0,) * n]
        h = greedy_height(n)
        print(f"  n={n}: S(n)={S}, greedy height={h}, optimal={h == S}")


if __name__ == "__main__":
    main()
