"""Regression checks for the compositional one-ply lower bounds.

These pin the reproducible finite facts behind
``docs/research-compositional-lookahead.md`` fast enough for CI (< 5 s):
the chain ``L0 <= L1 <= B <= F`` (exhaustive for ``n <= 4``), the exact
gap family ``W^t`` (``L1 = 3t + 1`` vs ``B = F = 4t``, direct for
``t <= 2`` plus the pair-child mechanism at ``t = 3``), the series-power
amplification bounds for ``Q = Merge(2, 1)`` and the resulting
no-fixed-horizon witnesses, and the exact equivalence of the capped
polynomial-space prune with ``L1 > d`` (sound: never fires when
``F <= d``).  The inequalities have general mathematical proofs (see the
note), so no exhaustive ``n >= 5`` minimax search is performed here.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from compositional_lookahead import (  # noqa: E402
    B,
    L0,
    L1,
    Lr,
    add_relation,
    N5_WITNESS,
    Q_MERGE_2_1,
    all_posets,
    capped_pair_census,
    ceil_log2,
    linear_extensions,
    minimax,
    prune_verdict,
    series_power,
)


class ChainInequalities(unittest.TestCase):
    """``L0 <= L1 <= B <= F`` on every poset with ``n <= 4`` (242 posets)."""

    def test_exhaustive_n_le_4(self) -> None:
        for n in range(1, 5):
            for P in all_posets(n):
                l0, l1, b, f = L0(P), L1(P), B(P), minimax(P)
                self.assertLessEqual(l0, l1, f"L0 > L1 at n={n}: {P}")
                self.assertLessEqual(l1, b, f"L1 > B at n={n}: {P}")
                self.assertLessEqual(b, f, f"B > F at n={n}: {P}")

    def test_B_equals_L1_throughout_n_le_4(self) -> None:
        # The decomposition is never harmful; the first strict B > L1 in
        # this project is W (+) W at n = 10 (see WitnessFamily below).
        for n in range(1, 5):
            for P in all_posets(n):
                self.assertEqual(B(P), L1(P), f"B != L1 at n={n}: {P}")


class WitnessFamily(unittest.TestCase):
    """``W^t``: exact global ``L1 = 3t + 1`` vs decomposed ``B = F = 4t``."""

    def test_w_values(self) -> None:
        self.assertEqual(linear_extensions(N5_WITNESS), 8)
        self.assertEqual(L0(N5_WITNESS), 3)
        self.assertEqual(L1(N5_WITNESS), 4)
        self.assertEqual(minimax(N5_WITNESS), 4)

    def test_w_squared_direct(self) -> None:
        P = series_power(N5_WITNESS, 2)
        self.assertEqual(len(P), 10)
        self.assertEqual(linear_extensions(P), 64)
        self.assertEqual(L0(P), 6)
        self.assertEqual(L1(P), 7)
        self.assertEqual(B(P), 8)
        self.assertEqual(minimax(N5_WITNESS) * 2, 8)
        self.assertEqual(B(P), 2 * minimax(N5_WITNESS))
        self.assertGreater(B(P), L1(P))

    def test_w_cubed_mechanism(self) -> None:
        # n = 15: e and L0 direct; the two representative pair children of
        # the first copy have e = 5*64, 3*64 and 6*64, 2*64, which is the
        # exact mechanism behind L1(W^3) = 3*3 + 1 = 10.
        P = series_power(N5_WITNESS, 3)
        self.assertEqual(len(P), 15)
        self.assertEqual(linear_extensions(P), 512)
        self.assertEqual(L0(P), 9)
        self.assertEqual(B(P), 12)
        self.assertEqual(3 * minimax(N5_WITNESS), 12)
        for (i, j), lo, hi in (((0, 2), 3, 5), ((2, 4), 2, 6)):
            self.assertEqual(
                linear_extensions(add_relation(P, j, i)), lo * 64
            )
            self.assertEqual(
                linear_extensions(add_relation(P, i, j)), hi * 64
            )
        self.assertEqual(3 * 3 + 1, 10)

    def test_gap_grows_linearly(self) -> None:
        for t in (1, 2, 3):
            P = series_power(N5_WITNESS, t)
            self.assertEqual(linear_extensions(P), 8**t)
            self.assertEqual(L0(P), 3 * t)
            self.assertEqual(B(P), 4 * t)
            self.assertEqual(4 * t - (3 * t + 1), t - 1)


class Amplification(unittest.TestCase):
    """Series powers of ``Q = Merge(2, 1)``: ``e = 3``, ``F = 2``."""

    def test_q_values(self) -> None:
        self.assertEqual(linear_extensions(Q_MERGE_2_1), 3)
        self.assertEqual(L0(Q_MERGE_2_1), 2)
        self.assertEqual(L1(Q_MERGE_2_1), 2)
        self.assertEqual(minimax(Q_MERGE_2_1), 2)

    def test_series_power_extension_counts(self) -> None:
        for t in range(1, 5):
            P = series_power(Q_MERGE_2_1, t)
            self.assertEqual(len(P), 3 * t)
            self.assertEqual(linear_extensions(P), 3**t)

    def test_lr_bound_direct(self) -> None:
        # Lr(Q^t, r) <= ceil(t log2 3) + r, checked exactly for small n.
        for t in range(1, 4):
            P = series_power(Q_MERGE_2_1, t)
            for r in range(0, 3):
                self.assertLessEqual(Lr(P, r), ceil_log2(3**t) + r)

    def test_no_fixed_horizon_witnesses(self) -> None:
        # For each r, the minimal t with ceil(t log2 3) + r < 2t: a series
        # power where horizon r is provably strictly below F = 2t.
        expected = {0: 3, 1: 5, 2: 8, 3: 10, 4: 13, 5: 15}
        for r, t in expected.items():
            self.assertLess(ceil_log2(3**t) + r, 2 * t)
            if t == 3:  # direct check at n = 9
                P = series_power(Q_MERGE_2_1, t)
                self.assertLessEqual(Lr(P, r), ceil_log2(3**t) + r)
                self.assertLess(Lr(P, r), 2 * t)


class CappedPrune(unittest.TestCase):
    """The capped linear-extension polynomial-space prune."""

    def test_equivalence_with_L1(self) -> None:
        # prune_verdict(P, d) is False iff L1(P) > d, for all n <= 4, d <= 4.
        for n in range(1, 5):
            for P in all_posets(n):
                for d in range(0, 5):
                    v = prune_verdict(P, d)
                    self.assertEqual(v is False, L1(P) > d, (n, P, d, v))
                    if v is False:
                        self.assertGreater(minimax(P), d, (n, P, d))

    def test_stricter_than_info_bound_at_witness(self) -> None:
        # e(W) = 8 <= 2^3, so the ordinary info prune is silent at d = 3,
        # while the capped L1 prune fires (L1(W) = 4 > 3).
        self.assertEqual(linear_extensions(N5_WITNESS), 8)
        self.assertIs(prune_verdict(N5_WITNESS, 3), False)
        self.assertIsNone(prune_verdict(N5_WITNESS, 4))

    def test_census_cap(self) -> None:
        # antichain_4 has e = 24 > 2^2: the census reports "over" (None).
        e, _ = capped_pair_census((0,) * 4, 2)
        self.assertIsNone(e)
        # At d = 5 the census is exact and the pair counts are consistent.
        e, c = capped_pair_census((0,) * 4, 5)
        self.assertEqual(e, 24)
        self.assertEqual(c[0][1] + c[1][0], 24)
        self.assertEqual(c[0][1], 12)


if __name__ == "__main__":
    unittest.main()
