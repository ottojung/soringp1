"""Independent regression checks for PR #22 (compositional-lookahead).

These tests exercise the *reviewer's* disjoint primitives in
``scripts/review_compositional_lookahead.py``, not the author's functions
directly, and pin the finite facts used in
``docs/review-compositional-lookahead.md``.  Bounded by design: exhaustive
enumeration only for ``n <= 4``; the ``n <= 6`` no-strict-gap claim is the
complete targeted ordinal-sum enumeration; the ``n = 7`` witness and the
``W^t``/``Q^t`` families are checked directly.  No exhaustive ``n >= 5``
minimax scan and no ``n >= 15`` computation.

Run:  python3 -m unittest tests.test_review_compositional_lookahead -q
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import compositional_lookahead as C  # noqa: E402
import review_compositional_lookahead as R  # noqa: E402


class _Base(unittest.TestCase):
    def setUp(self) -> None:
        R.FAILS.clear()

    def assertNoFails(self) -> None:
        self.assertEqual(R.FAILS, [], f"independent checks failed: {R.FAILS}")


class Machinery(_Base):
    def test_machinery(self) -> None:
        n = R.check_machinery(4)
        self.assertGreater(n, 0)
        self.assertNoFails()


class Series(_Base):
    def test_series(self) -> None:
        n = R.check_series(4)
        self.assertGreater(n, 0)
        self.assertNoFails()


class Chain(_Base):
    def test_chain(self) -> None:
        stats = R.check_chain(4)
        self.assertEqual(stats["posets"], 242)
        self.assertEqual(stats["strict_B_gt_L1"], 0)
        self.assertNoFails()


class NoGapBelowSeven(_Base):
    def test_no_gap_below_seven(self) -> None:
        stats = R.check_no_gap_below_7()
        # Complete for posets with >= 2 series factors (n <= 6); none strict.
        self.assertEqual(stats["strict"], 0)
        self.assertEqual(stats["max_n_strict"], -1)
        self.assertNoFails()


class N7Witness(_Base):
    def test_n7(self) -> None:
        out = R.check_n7_witness()
        self.assertEqual(out, {"e": 16, "L0": 4, "L1": 4, "B": 5, "F": 5})
        self.assertNoFails()

    def test_n7_against_author(self) -> None:
        P = (124, 124, 0, 0, 4, 12, 28)
        self.assertEqual(C.linear_extensions(P), 16)
        self.assertEqual(C.L0(P), 4)
        self.assertEqual(C.L1(P), 4)
        self.assertEqual(C.B(P), 5)
        self.assertEqual(C.minimax(P), 5)


class WitnessFamily(_Base):
    def test_w_family(self) -> None:
        out = R.check_w_family()
        self.assertEqual(out["splits"], [(0, 2, 5, 3), (1, 3, 5, 3),
                                         (1, 4, 2, 6), (2, 4, 6, 2)])
        rows = {r["t"]: r for r in out["rows"]}
        self.assertEqual(rows[1]["L1"], 4)
        self.assertEqual(rows[2]["L1"], 7)
        self.assertEqual(rows[3]["e"], 512)
        self.assertEqual(rows[3]["L1"], 10)
        self.assertEqual(rows[3]["B"], 12)
        self.assertNoFails()


class QFamily(_Base):
    def test_q_family(self) -> None:
        out = R.check_q_family()
        horizon = {h["r"]: h["t_min"] for h in out["horizon"]}
        self.assertEqual(horizon, {0: 3, 1: 5, 2: 8, 3: 10, 4: 13, 5: 15})
        self.assertNoFails()


class Prune(_Base):
    def test_prune(self) -> None:
        stats = R.check_prune(4, 5)
        self.assertGreater(stats["checks"], 0)
        self.assertEqual(stats["fired"], 471)
        self.assertNoFails()


if __name__ == "__main__":
    unittest.main()
