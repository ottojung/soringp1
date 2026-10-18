"""Regression tests for the staircase no-orbit-savings family."""
import sys
import unittest
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from time_exponent_probe import (
    staircase, odd_staircase, incomparable_pairs, automorphism_count, check,
)


class StaircaseTests(unittest.TestCase):
    def test_exact_incomparability_count(self):
        for m in range(1, 7):
            self.assertEqual(len(incomparable_pairs(staircase(m))), 3 * comb(m, 2))

    def test_distinct_degrees(self):
        for m in range(1, 6):
            s = staircase(m)
            self.assertEqual([s[i].bit_count() for i in range(m)],
                             list(range(1, m + 1)))
            pred = [sum(bool(s[i] & (1 << (m + j))) for i in range(m))
                    for j in range(m)]
            self.assertEqual(pred, list(range(m, 0, -1)))

    def test_automorphisms_small(self):
        for m in (1, 2, 3, 4):
            self.assertEqual(automorphism_count(staircase(m)), 1)

    def test_odd_family(self):
        for m in (1, 2, 3):
            s = odd_staircase(m)
            self.assertEqual(len(incomparable_pairs(s)), 3 * comb(m, 2))
            self.assertEqual(automorphism_count(s), 1)

    def test_size_cap(self):
        with self.assertRaises(ValueError):
            automorphism_count(staircase(5))

    def test_bad_parameter(self):
        with self.assertRaises(ValueError):
            staircase(0)


if __name__ == "__main__":
    unittest.main()
