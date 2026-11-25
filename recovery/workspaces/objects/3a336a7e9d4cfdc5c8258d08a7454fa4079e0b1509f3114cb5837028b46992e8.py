"""Regression tests for the series (ordinal-sum) decomposition probe.

These are computational checks on the experimental evaluator, not Lean proofs.
They are bounded to n <= 5 so that they never compete with n >= 6 searches.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from series_decomposition_probe import (  # noqa: E402
    all_posets,
    benchmark,
    incomparability_components,
    is_series_prime,
    ordered_blocks,
    sorting_number,
    subset_counterexample,
    verify_additivity,
    verify_decomposition,
)


class SeriesDecomposition(unittest.TestCase):
    def test_additivity_all_posets(self) -> None:
        for n in range(0, 5):
            with self.subTest(n=n):
                checked, failures = verify_additivity(n)
                self.assertEqual(failures, 0)
                if n >= 2:
                    self.assertGreater(checked, 0)

    def test_decomposition_is_ordinal_sum(self) -> None:
        for n in range(0, 5):
            with self.subTest(n=n):
                checked, failures = verify_decomposition(n)
                self.assertEqual(failures, 0)
                self.assertGreater(checked, 0)

    def test_series_prime_iff_connected_incomparability_graph(self) -> None:
        for n in range(0, 5):
            for s in all_posets(n):
                self.assertEqual(
                    is_series_prime(s), len(incomparability_components(s)) == 1
                )

    def test_decomposition_rule_preserves_S(self) -> None:
        expected = (0, 0, 1, 3, 5, 7)
        for n, value in enumerate(expected):
            with self.subTest(n=n):
                self.assertEqual(sorting_number(n, use_decomposition=True), value)
                self.assertEqual(sorting_number(n), value)

    def test_subset_counterexample(self) -> None:
        full, sub, projections = subset_counterexample()
        # The full ordinal sum obeys additivity, but the correlated subset does not.
        self.assertEqual(full, projections)
        self.assertLess(sub, projections)

    def test_benchmark_reports_unchanged_value(self) -> None:
        for n in range(0, 6):
            with self.subTest(n=n):
                row = benchmark(n)
                self.assertEqual(row["standard"]["S"], row["decomposed"]["S"])


if __name__ == "__main__":
    unittest.main()
