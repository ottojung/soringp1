"""Regression tests for ``scripts/higher_composition.py``.

Bounded by design: exhaustive checks only for ``n <= 4`` and ``r <= 3``,
targeted series powers ``Q^t`` (``t <= 3``) and ``W^t`` (``t <= 2``),
horizons ``r <= 2`` on the powers.  No unbounded scans; no minimax on
states larger than ``n = 5`` (powers get ``F`` by ordinal-sum
additivity, never by direct search).

Run with ``python3 -m unittest tests.test_higher_composition -q``.
"""

from __future__ import annotations

import os
import sys
import unittest

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"),
)

import higher_composition as hc  # noqa: E402


class TestChainRegression(unittest.TestCase):
    """Exhaustive n <= 4: ``Lr <= Br <= F`` and ``Br`` nondecreasing in r."""

    def test_chain_and_monotonicity_n_leq_4(self) -> None:
        for n in range(1, 5):
            for P in hc.all_posets(n):
                f = hc.minimax(P)
                prev_b = None
                for r in range(4):
                    lr = hc.Lr(P, r)
                    br = hc.Br(P, r)
                    self.assertLessEqual(
                        lr, br, msg=f"Lr > Br at n={n}, r={r}: P={P}"
                    )
                    self.assertLessEqual(
                        br, f, msg=f"Br > F at n={n}, r={r}: P={P}"
                    )
                    if prev_b is not None:
                        self.assertLessEqual(
                            prev_b, br,
                            msg=f"Br not monotone at n={n}, r={r}: P={P}",
                        )
                    prev_b = br

    def test_edge_cases(self) -> None:
        # Total posets: every bound is 0 (single factor, no pairs).
        total3 = (6, 4, 0)  # 0 < 1 < 2
        self.assertEqual(hc.minimax(total3), 0)
        for r in range(4):
            self.assertEqual(hc.Lr(total3, r), 0)
            self.assertEqual(hc.Br(total3, r), 0)
        # Antichain on 3 elements is a single 3-element factor: Br = Lr.
        anti3 = (0, 0, 0)
        for r in range(4):
            self.assertEqual(hc.Br(anti3, r), hc.Lr(anti3, r))
        # A 2-antichain plus an isolated singleton: two factors.
        # Q^2 below covers the general multi-factor case.
        two_anti = (0, 0)
        self.assertEqual(hc.minimax(two_anti), 1)
        for r in range(3):
            self.assertEqual(hc.Lr(two_anti, r), hc.Br(two_anti, r))

    def test_two_factor_Q_squared(self) -> None:
        # Q (+) Q: e = 9, F = 4 by additivity; global L_r = B_r = 4 for r >= 0.
        q2 = hc.series_power(hc.Q_MERGE_2_1, 2)
        self.assertEqual(hc.linear_extensions(q2), 9)
        for r in range(3):
            self.assertEqual(hc.Lr(q2, r), 4, msg=f"r={r}")
            self.assertEqual(hc.Br(q2, r), 4, msg=f"r={r}")

    def test_first_strict_example_Q_cubed_r0(self) -> None:
        # Q^3: L_0 = ceil(log2 27) = 5 < 6 = B_0 = F (rounding strictness at
        # r = 0); at r >= 1 the global bound has caught up: L_r = B_r = 6.
        q3 = hc.series_power(hc.Q_MERGE_2_1, 3)
        self.assertEqual(hc.linear_extensions(q3), 27)
        self.assertEqual(hc.Lr(q3, 0), 5)
        self.assertEqual(hc.Br(q3, 0), 6)
        for r in (1, 2):
            self.assertEqual(hc.Lr(q3, r), 6, msg=f"r={r}")
            self.assertEqual(hc.Br(q3, r), 6, msg=f"r={r}")


class TestQFamily(unittest.TestCase):
    """``Q^t``: ``Br = F = 2t`` for every r, global ``Lr <= ceil(t log2 3) + r``."""

    def test_base(self) -> None:
        q = hc.Q_MERGE_2_1
        self.assertEqual(hc.linear_extensions(q), 3)
        self.assertEqual(hc.minimax(q), 2)
        for r in range(4):
            self.assertEqual(hc.Lr(q, r), 2, msg=f"r={r}")

    def test_powers_direct(self) -> None:
        for t in (1, 2, 3):
            P = hc.series_power(hc.Q_MERGE_2_1, t)
            self.assertEqual(hc.linear_extensions(P), 3**t, msg=f"t={t}")
            for r in range(3):
                self.assertLessEqual(
                    hc.Lr(P, r),
                    hc.ceil_log2(3**t) + r,
                    msg=f"t={t}, r={r}",
                )
                self.assertEqual(hc.Br(P, r), 2 * t, msg=f"t={t}, r={r}")

    def test_F_by_additivity(self) -> None:
        # F(Q^t) = t * F(Q) via additivity; verified directly by minimax
        # for t <= 2 (n <= 6) and by the additivity identity beyond.
        for t in (1, 2):
            P = hc.series_power(hc.Q_MERGE_2_1, t)
            self.assertEqual(hc.minimax(P), 2 * t, msg=f"t={t}")
        for t in (3, 4):
            self.assertEqual(t * hc.minimax(hc.Q_MERGE_2_1), 2 * t, msg=f"t={t}")


class TestWFamily(unittest.TestCase):
    """``W^t``: ``Lr(W) = 4`` for ``r >= 1``, so ``Br = F = 4t``; global gap."""

    def test_base(self) -> None:
        w = hc.N5_WITNESS
        self.assertEqual(hc.linear_extensions(w), 8)
        self.assertEqual(hc.minimax(w), 4)
        self.assertEqual(hc.Lr(w, 0), 3)
        for r in (1, 2, 3):
            self.assertEqual(hc.Lr(w, r), 4, msg=f"r={r}")

    def test_W2_direct(self) -> None:
        w2 = hc.series_power(hc.N5_WITNESS, 2)
        self.assertEqual(hc.linear_extensions(w2), 64)
        # L1(W^2) = 7 (proved formula 3t+1 of the compositional note).
        self.assertEqual(hc.Lr(w2, 0), 6)
        self.assertEqual(hc.Lr(w2, 1), 7)
        self.assertEqual(hc.Lr(w2, 2), 7)
        self.assertEqual(hc.Br(w2, 0), 6)
        self.assertEqual(hc.Br(w2, 1), 8)
        self.assertEqual(hc.Br(w2, 2), 8)
        # F(W^2) = 8 by additivity (never direct minimax at n = 10).
        self.assertEqual(2 * hc.minimax(hc.N5_WITNESS), 8)
        # Strict gap between global Lr and Br at every horizon r >= 1;
        # at r = 0 the rounding gap is absent (both are 6).
        self.assertEqual(hc.Lr(w2, 0), hc.Br(w2, 0))
        for r in (1, 2):
            self.assertLess(hc.Lr(w2, r), hc.Br(w2, r), msg=f"r={r}")


class TestGapTables(unittest.TestCase):
    """Pure arithmetic: minimal powers where the proved global bound drops
    below the exact value, for each fixed horizon r."""

    def test_q_minimal_t(self) -> None:
        expected = {0: 3, 1: 5, 2: 8, 3: 10, 4: 13, 5: 15}
        for r, t in expected.items():
            self.assertLess(
                hc.ceil_log2(3**t) + r,
                2 * t,
                msg=f"r={r}, t={t}",
            )
            if t > 1:
                self.assertGreaterEqual(
                    hc.ceil_log2(3 ** (t - 1)) + r,
                    2 * (t - 1),
                    msg=f"r={r}, t={t} not minimal",
                )

    def test_w_minimal_t(self) -> None:
        for r in range(1, 6):
            t = r + 1
            self.assertLess(3 * t + r, 4 * t, msg=f"r={r}")
            self.assertGreaterEqual(3 * (t - 1) + r, 4 * (t - 1), msg=f"r={r}")


if __name__ == "__main__":
    unittest.main()
