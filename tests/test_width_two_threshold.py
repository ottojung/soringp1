"""Checks for the width-two Fibonacci threshold note.

The theorem itself is a paper result conditional on Peczarski's published proof
of the Gold Partition Conjecture for width-two posets. These tests check the
arithmetic of the induction, the tightness family, and the statement on the
small width-two cores the census can enumerate exactly.
"""

import unittest
from decimal import Decimal, getcontext

from scripts.core_threshold_census import (
    enumerate_cores,
    extensions_by_permutation,
    predecessors,
    sortable,
    staircase,
)

getcontext().prec = 60

FIB = [0, 1, 1]
while len(FIB) < 80:
    FIB.append(FIB[-1] + FIB[-2])
PHI = (Decimal(5).sqrt() + 1) / 2


def width(up):
    """Size of a largest antichain, by exhaustive search (small n only)."""
    n = len(up)
    best = 0

    def rec(i, chain):
        nonlocal best
        if i == n:
            best = max(best, len(chain))
            return
        if len(chain) + (n - i) <= best:
            return
        if all(
            not ((up[i] >> j) & 1) and not ((up[j] >> i) & 1)
            for j in chain
        ):
            chain.append(i)
            rec(i + 1, chain)
            chain.pop()
        rec(i + 1, chain)

    rec(0, [])
    return best


def exact_m(up, exts):
    exts = tuple(sorted(exts))
    for budget in range(0, len(up) + 2):
        if sortable(exts, budget):
            return budget
    raise AssertionError("no budget sorted the poset")


class WidthTwoThresholdTest(unittest.TestCase):
    def test_binet_inequalities(self):
        for r in range(0, 61):
            t = FIB[r + 3] - 1
            with self.subTest(r=r):
                # a <= e/phi with e <= T(r) forces a <= T(r-1)
                self.assertLess(Decimal(t) / PHI, FIB[r + 2])
                # b < e/phi^2 with e <= T(r) forces b <= T(r-2)
                if r >= 2:
                    self.assertLess(Decimal(t) / (PHI * PHI), FIB[r + 1])

    def test_staircase_is_width_two_and_tight(self):
        for n in range(2, 11):
            up = staircase(n)
            with self.subTest(n=n):
                self.assertEqual(width(up), 2)
                exts = extensions_by_permutation(up)
                self.assertEqual(len(exts), FIB[n + 1])
                self.assertEqual(exact_m(up, exts), n - 1)

    def test_width_two_cores_obey_the_bound(self):
        checked = 0
        for n, classes in enumerate_cores(20).items():
            if n > 9:
                continue
            for up, exts in classes.values():
                if width(up) > 2:
                    continue
                m = exact_m(up, exts)
                with self.subTest(n=n, e=len(exts), m=m):
                    self.assertGreaterEqual(len(exts), FIB[m + 2])
                checked += 1
        # Anti-vacuity: the filter must actually select most small cores.
        self.assertGreater(checked, 100)


if __name__ == "__main__":
    unittest.main()
