"""Independent verification of the two-phase exact sorting witnesses.

Mirrors tests/test_fo_tc_twophase_barrier.py but exercises the independent
checker (own Ford-Johnson, transcript-prefix-tuple program encoding), see
docs/research-fo-tc-twophase.md "Independent verification".

Run with:  python3 -m unittest discover -s tests -v
The exhaustive 9!-order run is gated behind SORINGP1_SLOW=1.
"""

import os
import sys
import unittest
from math import ceil, factorial, log2
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from twophase_independent_check import verify_independent  # noqa: E402


class IndependentTwoPhaseWitness(unittest.TestCase):
    def test_info_bound_n8_is_16(self) -> None:
        self.assertLess(2 ** 15, factorial(8))
        self.assertLessEqual(factorial(8), 2 ** 16)

    def test_n8_independent_witness(self) -> None:
        result = verify_independent(8, 16)
        self.assertEqual(result["worst_queries"], 16)
        self.assertEqual(result["internal_ask_nodes"], 40319)
        self.assertEqual(result["leaves"], 40320)
        self.assertEqual(result["strictness_rejects"], 40319)
        self.assertTrue(result["info_bound_self_certifies"])
        self.assertEqual(result["total_orders"], 40320)
        self.assertLessEqual(result["worst_steps"], result["clock"])

    def test_n5_miss_against_S5(self) -> None:
        result = verify_independent(5, 8)
        self.assertEqual(result["worst_queries"], 8)
        self.assertGreater(result["worst_queries"], 7)  # S(5) = 7

    def test_two_phase_exactness_characterization_n6_n7(self) -> None:
        # exactness iff S(n) = S(n-1) + ceil(log2 n); literature table
        # (docs/research-plan.md, OEIS A036604).
        S = {4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 9: 19}
        self.assertEqual(S[5], S[4] + ceil(log2(5)) - 1)  # misses by one
        self.assertEqual(S[6], S[5] + ceil(log2(6)))      # exact
        self.assertEqual(S[7], S[6] + ceil(log2(7)))      # exact
        self.assertEqual(S[8], S[7] + ceil(log2(8)))      # exact
        self.assertEqual(S[9], S[8] + ceil(log2(9)) - 1)  # misses by one

    @unittest.skipUnless(os.environ.get("SORINGP1_SLOW"),
                         "exhaustive 9!-order run; set SORINGP1_SLOW=1")
    def test_n9_two_phase_misses_exact_budget(self) -> None:
        self.assertLess(2 ** 18, factorial(9))
        self.assertLessEqual(factorial(9), 2 ** 19)  # C(9) = 19 < 20 = worst
        result = verify_independent(9, 20)
        self.assertEqual(result["worst_queries"], 20)
        self.assertEqual(result["internal_ask_nodes"], 362879)
        self.assertEqual(result["leaves"], 362880)
        self.assertFalse(result["info_bound_self_certifies"])

    @unittest.skipUnless(os.environ.get("SORINGP1_SLOW"),
                         "exhaustive 9!-order run; set SORINGP1_SLOW=1")
    def test_n9_info_bound_is_19(self) -> None:
        self.assertLess(2 ** 18, factorial(9))
        self.assertLessEqual(factorial(9), 2 ** 19)  # C(9) = 19 < 20


if __name__ == "__main__":
    unittest.main()
