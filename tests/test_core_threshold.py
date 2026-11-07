"""Tests for the core census behind the finite comparison thresholds.

These pin the facts used by ``docs/research-core-threshold.md``: the generator
reproduces the independently known core counts, the staircase family carries
``e = F(n+1)``, ``m = n-1``, every core with ``e <= 33`` sorts within six
comparisons, and the decision procedure does report a shortfall when the
budget is one too small.
"""

import unittest

from scripts.core_threshold_census import (
    enumerate_cores,
    extensions_by_permutation,
    sortable,
    staircase,
)


def _min_budget(up):
    exts = tuple(sorted(extensions_by_permutation(up)))
    for budget in range(0, len(up) + 2):
        if sortable(exts, budget):
            return len(exts), budget
    raise AssertionError("no budget sorted the poset")


class CoreCensusTest(unittest.TestCase):
    def test_generator_matches_known_core_counts(self):
        self.assertEqual(sum(len(v) for v in enumerate_cores(12).values()), 63)
        self.assertEqual(sum(len(v) for v in enumerate_cores(20).values()), 250)

    def test_staircase_is_the_fibonacci_witness(self):
        expected = [(2, 1), (3, 2), (5, 3), (8, 4), (13, 5), (21, 6), (34, 7), (55, 8)]
        for n, (fib, depth) in enumerate(expected, start=2):
            with self.subTest(n=n):
                self.assertEqual(_min_budget(staircase(n)), (fib, depth))

    def test_all_cores_with_e_at_most_33_sort_in_six(self):
        failures = [
            (n, len(exts))
            for n, classes in enumerate_cores(33).items()
            for _, exts in classes.values()
            if not sortable(tuple(sorted(exts)), 6)
        ]
        self.assertEqual(failures, [])

    def test_short_budget_is_detected(self):
        failures = [
            (n, len(exts))
            for n, classes in enumerate_cores(20).items()
            for _, exts in classes.values()
            if not sortable(tuple(sorted(exts)), 4)
        ]
        self.assertNotEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
