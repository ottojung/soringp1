"""Tests for the critical-depth reachable-class barrier
(docs/research-critical-depth-memo-barrier.md)."""

import unittest

from scripts.critical_depth_memo_barrier import (
    ci_noiso,
    ci_lower_bound_log2,
    exact_classes_noiso,
    exponent_L,
    lg2_fact,
    reachable_in_exactly_j,
)

import math
from math import factorial


class MicroCheck(unittest.TestCase):
    def test_height2_reachability_small(self):
        for m in (3, 4):
            self.assertTrue(reachable_in_exactly_j(m, trials=200))


class InclusionExclusion(unittest.TestCase):
    def test_ci_matches_bruteforce(self):
        m = 4
        for j in range(1, m * m + 1):
            subsets = 0
            import itertools
            alledges = [(a, m + b) for a in range(m) for b in range(m)]
            for chosen in itertools.combinations(alledges, j):
                if ({a for a, _ in chosen} == set(range(m))
                        and {b - m for _, b in chosen} == set(range(m))):
                    subsets += 1
            self.assertEqual(ci_noiso(m, j), subsets, (m, j))

    def test_orbit_bound_small(self):
        for m, j in ((3, 4), (3, 6), (4, 6), (4, 8)):
            cls, n_sub = exact_classes_noiso(m, j)
            lower = ci_noiso(m, j) / factorial(m) ** 2
            self.assertGreaterEqual(cls, lower, (m, j))


class ExponentTable(unittest.TestCase):
    def test_positive_beyond_8(self):
        for n in range(8, 25):
            m, k, j, L = exponent_L(n)
            self.assertIsNotNone(L, n)
            self.assertGreater(L, 0.0, n)

    def test_monotone_growth_window(self):
        vals = [exponent_L(n)[3] for n in range(16, 25, 2)]
        for a, b in zip(vals, vals[1:]):
            self.assertGreater(b, a)

    def test_asymptotic_anchor(self):
        m, k, j, L = exponent_L(32)
        self.assertGreater(L, 150.0)

    def test_union_bound_positive_small(self):
        for n in (8, 12, 16, 20, 24):
            m, k, j, _ = exponent_L(n)
            t = 2 * m * (1 - 1.0 / m) ** j
            self.assertLess(t, 1.0, n)

    def test_k_below_S_sanctioned_by_information_bound(self):
        # literature fact: S(n) >= ceil(log2 n!) (decision-tree bound);
        # the probe budget k = ceil(log2 n!) - 1 is a *no-instance*
        # threshold: S(n) >= l > k for every n >= 3.
        from math import lgamma
        for n in range(8, 25):
            l = math.ceil(lgamma(n + 1) / math.log(2))
            self.assertEqual(exponent_L(n)[1], l - 1)
            self.assertGreater(l - 1, 0)


if __name__ == "__main__":
    unittest.main()
