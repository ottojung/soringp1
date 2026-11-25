"""Regression checks for the obstruction audit (docs/research-obstruction-next.md).

These pin the reproducible finite facts used in the audit: the local
information-bound frontier, the smallest same-``e`` different-``m`` witnesses,
and the counterexample to the tempting ``(e, width)`` scalar hypothesis.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from obstruction_probe import (  # noqa: E402
    H2_P1,
    H2_P2,
    H3_WITNESS,
    N5_E8_LOOSE,
    N6_E8_TIGHT,
    ceil_log2,
    chains_union,
    e_levels,
    first_local_failure,
    linear_extensions,
    merge_violations,
    minimax,
    width,
)


class LocalFrontier(unittest.TestCase):
    def test_h3_witness(self) -> None:
        self.assertEqual(linear_extensions(H3_WITNESS), 8)
        self.assertEqual(ceil_log2(8), 3)
        self.assertEqual(minimax(H3_WITNESS), 4)

    def test_first_local_failure_is_e8(self) -> None:
        self.assertEqual(first_local_failure(5), 8)

    def test_e7_level_is_tight(self) -> None:
        levels = e_levels(5)
        self.assertEqual(levels[7], {3})
        for e in range(1, 8):
            self.assertEqual(max(levels[e]), ceil_log2(e))

    def test_same_e_different_m_exists_at_e8(self) -> None:
        self.assertEqual(e_levels(5)[8], {3, 4})


class ScalarHypotheses(unittest.TestCase):
    def test_e_and_width_do_not_determine_m(self) -> None:
        self.assertEqual(linear_extensions(N6_E8_TIGHT), 8)
        self.assertEqual(width(N6_E8_TIGHT), 2)
        self.assertEqual(minimax(N6_E8_TIGHT), 3)

        self.assertEqual(linear_extensions(N5_E8_LOOSE), 8)
        self.assertEqual(width(N5_E8_LOOSE), 2)
        self.assertEqual(minimax(N5_E8_LOOSE), 4)

    def test_h2_non_monotonicity_witnesses(self) -> None:
        self.assertEqual(linear_extensions(H2_P1), 13)
        self.assertEqual(minimax(H2_P1), 5)
        self.assertEqual(linear_extensions(H2_P2), 14)
        self.assertEqual(minimax(H2_P2), 4)
        self.assertLess(linear_extensions(H2_P1), linear_extensions(H2_P2))
        self.assertGreater(minimax(H2_P1), minimax(H2_P2))


class MergeObstruction(unittest.TestCase):
    def test_merge_cost_is_not_universal_a_plus_b_minus_1(self) -> None:
        # M(1,4) = 3 by binary insertion, although a+b-1 = 4.
        P = chains_union((1, 4))
        self.assertEqual(linear_extensions(P), 5)
        self.assertEqual(minimax(P), 3)

    def test_equal_size_merge_is_two_m_minus_one(self) -> None:
        # M(m,m) = 2m-1 (tape merge optimal for equal sizes).
        for mm in range(1, 5):
            with self.subTest(m=mm):
                self.assertEqual(minimax(chains_union((mm, mm))), 2 * mm - 1)

    def test_two_four_merge_is_locally_loose(self) -> None:
        P = chains_union((2, 4))
        self.assertEqual(linear_extensions(P), 15)
        self.assertEqual(ceil_log2(15), 4)
        self.assertEqual(minimax(P), 5)

    def test_merge_violation_list(self) -> None:
        sizes = {v[0] for v in merge_violations(6)}
        self.assertIn((2, 4), sizes)
        self.assertNotIn((1, 4), sizes)  # tight: M(1,4) = 3 = ceil(log2 5)
        self.assertNotIn((3, 3), sizes)


if __name__ == "__main__":
    unittest.main()
