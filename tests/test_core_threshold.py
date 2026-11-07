"""Tests for the core census behind the finite comparison thresholds.

These pin the facts used by ``docs/research-core-threshold.md``: the generator
reproduces the independently known core counts, the staircase family carries
``e = F(n+1)``, ``m = n-1``, every core with ``e <= 33`` sorts within six
comparisons, and the decision procedure does report a shortfall when the
budget is one too small.
"""

import random
import unittest

from scripts.core_threshold_census import (
    canonical,
    enumerate_cores,
    is_core,
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
        levels = enumerate_cores(12)
        self.assertEqual(sum(len(v) for v in levels.values()), 63)
        # Per-level classes, so duplicate/wrong classes cannot cancel out.
        self.assertEqual(
            {n: len(v) for n, v in levels.items()},
            {2: 1, 3: 2, 4: 7, 5: 15, 6: 21, 7: 10, 8: 3, 9: 1, 10: 1, 11: 1, 12: 1},
        )
        self.assertEqual(sum(len(v) for v in enumerate_cores(20).values()), 250)

    def test_canonical_is_relabelling_invariant(self):
        cores = [up for v in enumerate_cores(12).values() for up, _ in v.values()]
        for up in cores:
            base = canonical(up)
            for _ in range(5):
                perm = list(range(len(up)))
                random.shuffle(perm)
                moved = [0] * len(up)
                inverse = [0] * len(up)
                for i, p in enumerate(perm):
                    inverse[p] = i
                for a in range(len(up)):
                    mask = up[a]
                    out = 0
                    while mask:
                        bit = mask & -mask
                        mask -= bit
                        out |= 1 << inverse[bit.bit_length() - 1]
                    moved[inverse[a]] = out
                self.assertEqual(canonical(tuple(moved)), base)

    def test_empty_poset_is_not_a_core(self):
        self.assertFalse(is_core(()))
        with self.assertRaises(ValueError):
            enumerate_cores(5)

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
