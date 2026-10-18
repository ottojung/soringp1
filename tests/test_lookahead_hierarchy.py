"""Regression checks for the adversarial lookahead hierarchy.

These pin the reproducible finite facts behind
``docs/research-lookahead-hierarchy.md`` fast enough for CI (< 5 s):

* the structural chain ``L0 <= L1 <= ... <= F`` and the derivative bound
  ``L_r <= L0 + r`` on *every labelled poset* with ``n <= 5`` (0.3 s);
* that ``L1 = F`` and ``L2 = L1`` for all ``n <= 5`` (no strict ``L2 > L1``
  below ``n = 6``, and the one-ply bound is already exact there);
* the smallest strict ``L2 > L1`` witness at ``n = 6`` with its exact masks,
  extension count, hierarchy and optimal moves;
* the deepest-stabilization ``n = 6`` witness, which needs five plies
  (``L_4 = 8 < 9 = F = L_5``).

The *exhaustive* ``n = 6`` audit (130023 labelled posets, ~26 s) is
deliberately **not** run in CI; only the two explicit ``n = 6`` witnesses are.
Poset counts below are for labelled posets (OEIS A001035); the hierarchy is
invariant under relabelling, so the same results hold for isomorphism classes.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from lookahead_hierarchy import (  # noqa: E402
    L,
    N5_WITNESS,
    all_posets,
    analyze_exhaustive,
    linear_extensions,
    minimax,
    optimal_moves,
)


class ChainAndDerivative(unittest.TestCase):
    """``L0 <= L1 <= L2 <= L3 <= F`` and ``L_r <= L0 + r`` for all ``n <= 5``."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.summary = analyze_exhaustive(5)

    def test_labelled_poset_counts(self) -> None:
        # Labelled posets, OEIS A001035.
        self.assertEqual(
            self.summary["poset_counts"],
            {1: 1, 2: 3, 3: 19, 4: 219, 5: 4231},
        )

    def test_no_chain_violations(self) -> None:
        self.assertEqual(self.summary["chain_violations"], [])

    def test_no_derivative_violations(self) -> None:
        self.assertEqual(self.summary["derivative_violations"], [])

    def test_one_ply_exact_below_n6(self) -> None:
        # L1 = F and L2 = L1 for every labelled poset with n <= 5.
        self.assertEqual(self.summary["max_gap_F_minus_L1"], 0)
        self.assertEqual(self.summary["max_gap_L2_minus_L1"], 0)
        self.assertEqual(self.summary["strict_L2_gt_L1"], [])
        self.assertEqual(self.summary["r_star"], 1)


class N5OnePlyWitness(unittest.TestCase):
    def test_values(self) -> None:
        self.assertEqual(linear_extensions(N5_WITNESS), 8)
        self.assertEqual([L(N5_WITNESS, r) for r in range(4)], [3, 4, 4, 4])
        self.assertEqual(minimax(N5_WITNESS), 4)


class SmallestL2Witness(unittest.TestCase):
    """First labelled poset with ``L2 > L1``: n = 6, e = 30, 5/5/6, F = 6."""

    P = (0, 0, 0, 1, 3, 27)

    def test_values(self) -> None:
        self.assertEqual(linear_extensions(self.P), 30)
        self.assertEqual([L(self.P, r) for r in range(3)], [5, 5, 6])
        self.assertEqual(minimax(self.P), 6)

    def test_strictly_two_ply(self) -> None:
        self.assertGreater(L(self.P, 2), L(self.P, 1))
        self.assertEqual(L(self.P, 2), minimax(self.P))

    def test_L1_optimal_move_splits_30_into_L0_4(self) -> None:
        moves = optimal_moves(self.P, 0)
        self.assertTrue(moves)
        self.assertTrue(all(max(a, b) == 4 for _, _, a, b in moves))
        self.assertEqual(L(self.P, 1), 5)


class DeepStabilizationWitness(unittest.TestCase):
    """n = 6 poset needing five plies: ``L_4 = 8 < 9 = F = L_5``."""

    P = (48, 0, 0, 0, 0, 0)

    def test_values(self) -> None:
        self.assertEqual(linear_extensions(self.P), 240)
        self.assertEqual([L(self.P, r) for r in range(6)], [8, 8, 8, 8, 8, 9])
        self.assertEqual(minimax(self.P), 9)

    def test_five_plies_needed(self) -> None:
        self.assertLess(L(self.P, 4), minimax(self.P))
        self.assertEqual(L(self.P, 5), minimax(self.P))


if __name__ == "__main__":
    unittest.main()
