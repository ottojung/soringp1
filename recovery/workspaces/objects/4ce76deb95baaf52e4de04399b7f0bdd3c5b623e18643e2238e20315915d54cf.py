"""Regression checks for certified upper-bound witnesses
(docs/research-upper-witnesses.md).

Companion program: scripts/upper_witness.py.

The central soundness property is: for every poset P on n <= 5 labelled
elements, the exact minimax F(P) satisfies

    leaf_bound(P) <= F(P) <= U_BIPI(P)   and   F(P) <= M(n),

so both U_BIPI(P) and the Ford-Johnson value M(n) are certified upper bounds,
and their minimum is a sound acceptance witness.  In addition, the explicit
BIPI strategy is simulated on every linear extension to confirm that it sorts
correctly and that its exact worst-case height does not exceed U_BIPI(P).

Run with:  python3 -m unittest discover -s tests -v
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from upper_witness import (  # noqa: E402
    antichain,
    bipi_strategy_height,
    bipi_upper_bound,
    can_sort_reference,
    can_sort_with_witness,
    combined_witness,
    crown,
    disjoint_chains,
    fj_upper_bound,
    fj_worst_case_height,
    greedy_policy_height,
    leaf_bound,
    memoized_F,
    reported_state_check,
    structured_posets,
    total_order,
    verify_all,
)

KNOWN_S = {1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10}
KNOWN_M = {1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16,
           9: 19, 10: 22, 11: 26, 12: 30}


class FordJohnson(unittest.TestCase):
    def test_upper_bound_matches_known_M(self) -> None:
        for n, expected in KNOWN_M.items():
            with self.subTest(n=n):
                self.assertEqual(fj_upper_bound(n), expected)

    def test_simulated_worst_case_matches_M(self) -> None:
        for n in range(1, 7):
            with self.subTest(n=n):
                height, exact = fj_worst_case_height(n)
                self.assertTrue(exact, "exhaustive for n <= 6")
                self.assertEqual(height, KNOWN_M[n])

    def test_fj_is_exact_for_small_n(self) -> None:
        for n in range(1, 7):
            with self.subTest(n=n):
                self.assertEqual(fj_upper_bound(n), KNOWN_S[n])


class ReviewFlaggedState(unittest.TestCase):
    """Regression for the state called out in review: succ=(0,0,0,0,5).

    The correct values are F=6, U_BIPI=8, strategy height=7.  In particular
    U_BIPI >= F and the strategy height >= F, so the bound is sound; there is
    no 6-comparison certified strategy claimed for this state.
    """

    def test_reported_state_values(self) -> None:
        r = reported_state_check()
        self.assertEqual(r["P"], (0, 0, 0, 0, 5))
        self.assertEqual(r["F"], 6)
        self.assertEqual(r["leaf"], 6)
        self.assertEqual(r["U_BIPI"], 8)
        self.assertEqual(r["strategy_height"], 7)
        self.assertTrue(r["sorted_ok"])
        self.assertEqual(r["M"], 7)
        self.assertEqual(r["combined"], 7)

    def test_reported_state_is_sound(self) -> None:
        r = reported_state_check()
        self.assertGreaterEqual(r["U_BIPI"], r["F"])
        self.assertGreaterEqual(r["strategy_height"], r["F"])
        self.assertGreaterEqual(r["combined"], r["F"])


class Soundness(unittest.TestCase):
    def test_exhaustive_bounds_and_strategy_n4(self) -> None:
        failures, checks = verify_all(4)
        self.assertEqual(failures, [])
        self.assertGreater(checks, 0)

    def test_exhaustive_bounds_and_strategy_n5(self) -> None:
        failures, checks = verify_all(5)
        self.assertEqual(failures, [])
        self.assertGreater(checks, 0)

    def test_leaf_bound_is_lower(self) -> None:
        for n in range(2, 7):
            F = memoized_F(n)
            for name, P in structured_posets(n).items():
                with self.subTest(n=n, poset=name):
                    self.assertLessEqual(leaf_bound(P, n), F[P])

    def test_combined_witness_upper(self) -> None:
        for n in range(1, 6):
            F = memoized_F(n)
            for P, fp in F.items():
                with self.subTest(n=n, P=P):
                    self.assertGreaterEqual(combined_witness(P, n), fp)


class GreedyPolicy(unittest.TestCase):
    def test_greedy_is_certified_upper(self) -> None:
        for n in range(1, 5):
            F = memoized_F(n)
            for P, fp in F.items():
                with self.subTest(n=n, P=P):
                    h, capped = greedy_policy_height(P, n)
                    self.assertFalse(capped)
                    self.assertGreaterEqual(h, fp)

    def test_greedy_is_sometimes_strictly_worse(self) -> None:
        # Not a new lower bound: the heuristic is not always optimal.
        F = memoized_F(5)
        worse = sum(
            1
            for P, fp in F.items()
            if greedy_policy_height(P, 5)[0] > fp
        )
        self.assertGreater(worse, 0)


class AcceptancePrune(unittest.TestCase):
    def test_prune_decisions_match_reference(self) -> None:
        for n in range(2, 6):
            for name, P in structured_posets(n).items():
                for d in range(0, min(2 * n, 10)):
                    with self.subTest(n=n, poset=name, d=d):
                        c1 = [0]
                        r1 = can_sort_reference(P, n, d, c1)
                        c2 = [0]
                        r2 = can_sort_with_witness(
                            P, n, d, c2, lambda Q, n=n: combined_witness(Q, n)
                        )
                        self.assertEqual(r1, r2)

    def test_prune_saves_calls_on_empty_poset(self) -> None:
        # For a generous budget the certified witness accepts immediately.
        n = 5
        d = 9
        c1 = [0]
        r1 = can_sort_reference(antichain(n), n, d, c1)
        c2 = [0]
        r2 = can_sort_with_witness(
            antichain(n), n, d, c2, lambda Q: combined_witness(Q, n)
        )
        self.assertTrue(r1)
        self.assertTrue(r2)
        self.assertLess(c2[0], c1[0])


if __name__ == "__main__":
    unittest.main()
