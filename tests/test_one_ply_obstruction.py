"""Regression checks for the one-ply adversarial information lower bound.

These pin the reproducible finite facts behind
``docs/research-one-ply-obstruction.md`` fast enough for CI (< 10 s): the two
theorem inequalities ``L0 <= L1 <= F`` (exhaustive for ``n <= 4``, the explicit
``n = 5`` witness, and a fixed small deterministic ``n = 5`` sample with shared
memoized ``F``), the smallest strict witness at ``n = 5`` with ``e = 8`` and its
child splits, and the ceiling identity used in the ``L1 >= L0`` argument.  The
inequalities have general mathematical proofs, so no exhaustive ``n = 5``
``F`` computation is performed here.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from one_ply_obstruction import (  # noqa: E402
    L0,
    L1,
    N5_WITNESS,
    all_posets,
    ceil_log2,
    linear_extensions,
    minimax,
    validate,
    witness_splits,
)


class CeilingIdentity(unittest.TestCase):
    """The ``L1 >= L0`` step: ``1 + ceil(log2 ceil(e/2)) >= ceil(log2 e)``."""

    def test_identity_small(self) -> None:
        for e in range(1, 512):
            self.assertGreaterEqual(1 + ceil_log2((e + 1) // 2), ceil_log2(e))

    def test_half_is_not_always_enough(self) -> None:
        # At e = 8 the larger child has >= 5 extensions, so one ply already
        # forces 1 + ceil(log2 5) = 4 > ceil(log2 8) = 3.
        self.assertEqual(1 + ceil_log2(5), 4)
        self.assertEqual(ceil_log2(8), 3)


class SmallestWitness(unittest.TestCase):
    def test_n5_witness_values(self) -> None:
        self.assertEqual(linear_extensions(N5_WITNESS), 8)
        self.assertEqual(L0(N5_WITNESS), 3)
        self.assertEqual(L1(N5_WITNESS), 4)
        self.assertEqual(minimax(N5_WITNESS), 4)

    def test_n5_witness_splits(self) -> None:
        # The four incomparable pairs split 8 extensions as 5/3, 5/3, 6/2, 6/2
        # (orientation-independent: normalize each split to (min, max)).
        splits = sorted(tuple(sorted(s)) for s in witness_splits(N5_WITNESS))
        self.assertEqual(splits, [(2, 6), (2, 6), (3, 5), (3, 5)])

    def test_n5_witness_is_strict_and_valid(self) -> None:
        self.assertGreater(L1(N5_WITNESS), L0(N5_WITNESS))
        self.assertLessEqual(L1(N5_WITNESS), minimax(N5_WITNESS))

    def test_no_strict_witness_below_n5(self) -> None:
        for n in range(1, 5):
            for P in all_posets(n):
                self.assertEqual(L1(P), L0(P), f"strict witness at n={n}: {P}")


class TheoremInequalities(unittest.TestCase):
    """``L0 <= L1 <= F`` on a fast bounded set (NO exhaustive n=5 ``F``)."""

    def test_exhaustive_n_le_4(self) -> None:
        for n in range(1, 5):
            for P in all_posets(n):
                l0, l1, f = L0(P), L1(P), minimax(P)
                self.assertGreaterEqual(l1, l0, f"L1 < L0 at n={n}: {P}")
                self.assertLessEqual(l1, f, f"L1 > F at n={n}: {P}")

    def test_validate_summary(self) -> None:
        summary = validate(4, n5_sample=40)
        self.assertEqual(summary["max_n_exhaustive"], 4)
        self.assertEqual(summary["n5_sample_size"], 40)
        self.assertEqual(summary["witness"], N5_WITNESS)
        self.assertGreater(summary["checked"], 0)


if __name__ == "__main__":
    unittest.main()
