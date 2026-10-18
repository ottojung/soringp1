"""Regression tests for the structural lower bounds probe.

These are computational checks on the experimental evaluator, not Lean proofs.
They are bounded to n <= 5 (exhaustive) plus targeted n = 6 merge witnesses so
that they never compete with other agents' n >= 6 searches.

The two candidate rules checked are:

* Theorem A (extension monotonicity): ``P subseteq Q => F(P) >= F(Q)``.
* Theorem B (structural bound): if the ordinal-sum decomposition of ``P``
  contains certified merge factors ``Merge(a_i, b_i)`` with gaps
  ``delta_i = M(a_i, b_i) - ceil(log2 C(a_i+b_i, a_i)) > 0``, then
  ``F(P) >= ceil(log2 e(P)) + sum delta_i``.
"""

import sys
import unittest
from math import comb, factorial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from structural_lower_bounds import (  # noqa: E402
    all_posets,
    ceil_log2,
    chain,
    chains_union,
    check_bound,
    check_monotonicity_covers,
    certified_merge_value,
    induced,
    linear_extensions,
    merge_factor,
    minimax,
    ordinal_sum,
    smallest_strict_witness,
    targeted,
)


class PosetMachinery(unittest.TestCase):
    def test_linear_extensions_known(self) -> None:
        # Antichain: every permutation is an extension.
        for n in range(0, 6):
            with self.subTest(n=n):
                self.assertEqual(linear_extensions((0,) * n), factorial(n))
        # A chain has exactly one extension.
        self.assertEqual(linear_extensions(chain(5)), 1)
        # Merge(2, 4) interleaves a 2-chain and a 4-chain: C(6, 2) = 15.
        self.assertEqual(linear_extensions(chains_union((2, 4))), 15)
        self.assertEqual(linear_extensions(chains_union((3, 3))), comb(6, 3))

    def test_minimax_known_values(self) -> None:
        # S(n) for n <= 5 (antichain states).
        self.assertEqual([minimax((0,) * n) for n in range(0, 6)], [0, 0, 1, 3, 5, 7])
        # Certified merge costs on n = 6.
        self.assertEqual(minimax(chains_union((1, 5))), 3)
        self.assertEqual(minimax(chains_union((2, 4))), 5)
        self.assertEqual(minimax(chains_union((3, 3))), 5)

    def test_ordinal_sum_additivity(self) -> None:
        # F(A (+) B) = F(A) + F(B) for the series (ordinal-sum) decomposition.
        for n in range(0, 5):
            for s in all_posets(n):
                from structural_lower_bounds import incomparability_components

                blocks = incomparability_components(s)
                if len(blocks) <= 1:
                    continue
                with self.subTest(poset=s):
                    self.assertEqual(
                        minimax(s),
                        sum(minimax(induced(s, b)) for b in blocks),
                    )


class TheoremA(unittest.TestCase):
    def test_monotonicity_on_covers(self) -> None:
        checked, failures = check_monotonicity_covers(5)
        self.assertEqual(failures, 0)
        self.assertGreater(checked, 0)


class TheoremB(unittest.TestCase):
    def test_structural_bound_all_posets(self) -> None:
        rows = check_bound(5)
        for row in rows:
            with self.subTest(n=row["n"]):
                self.assertEqual(row["failures"], 0)
                self.assertEqual(row["posets"], len(all_posets(row["n"])))

    def test_no_strict_witness_below_n6(self) -> None:
        for row in check_bound(5):
            with self.subTest(n=row["n"]):
                self.assertEqual(row["strict"], 0)

    def test_smallest_strict_witness(self) -> None:
        w = smallest_strict_witness()
        self.assertEqual(w["e"], 15)
        self.assertEqual(w["info"], 4)
        self.assertEqual(w["bound"], 5)
        self.assertEqual(w["F"], 5)
        self.assertGreater(w["bound"], w["info"])

    def test_targeted_n6_witnesses(self) -> None:
        by_name = {row["name"]: row for row in targeted()}
        self.assertEqual(by_name["Merge(2,4)"]["bound"], 5)
        self.assertEqual(by_name["Merge(2,4)"]["F"], 5)
        self.assertGreater(by_name["Merge(2,4)"]["bound"], by_name["Merge(2,4)"]["info"])
        # Every targeted witness is a valid lower bound and is n = 6.
        for row in targeted():
            with self.subTest(name=row["name"]):
                self.assertEqual(row["n"], 6)
                self.assertGreaterEqual(row["F"], row["bound"])
                self.assertGreaterEqual(row["bound"], row["info"])


class MergeCertification(unittest.TestCase):
    def test_one_element_merge_cost(self) -> None:
        for b in range(1, 6):
            with self.subTest(b=b):
                self.assertEqual(certified_merge_value(1, b), ceil_log2(b + 1))

    def test_tape_range_cost(self) -> None:
        for a in range(2, 6):
            for b in range(a, (3 * a) // 2 + 2):
                with self.subTest(a=a, b=b):
                    self.assertEqual(certified_merge_value(a, b), a + b - 1)

    def test_outside_certified_ranges_is_none(self) -> None:
        # The tape formula a+b-1 is NOT universal; outside the certified
        # ranges the value must not be guessed.
        self.assertIsNone(certified_merge_value(2, 5))
        self.assertIsNone(certified_merge_value(3, 6))
        self.assertIsNone(certified_merge_value(4, 8))

    def test_certified_values_match_minimax(self) -> None:
        for a in range(1, 4):
            for b in range(a, 7 - a + 1):
                m = certified_merge_value(a, b)
                if m is None:
                    continue
                with self.subTest(a=a, b=b):
                    self.assertEqual(minimax(chains_union((a, b))), m)

    def test_merge_factor_recognition(self) -> None:
        self.assertEqual(merge_factor(chains_union((2, 4))), (2, 4))
        self.assertEqual(merge_factor(chains_union((1, 1))), (1, 1))
        self.assertIsNone(merge_factor(chain(3)))
        # A "V" (one minimal below two incomparable) is not a two-clique merge.
        v = ordinal_sum((0,), (0, 0))
        self.assertIsNone(merge_factor(v))


if __name__ == "__main__":
    unittest.main()
