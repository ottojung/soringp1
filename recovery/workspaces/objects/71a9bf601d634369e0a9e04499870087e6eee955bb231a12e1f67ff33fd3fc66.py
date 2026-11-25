"""Regression checks for docs/research-hardness-boundaries.md.

These pin the reproducible finite facts behind the note's two barriers:

* the non-reduction barrier: two 5-element posets with equal number of linear
  extensions e = 8 but different exact comparison costs F = 3 and F = 4, so F is
  not a function of e;
* the encoding-sensitive containment: the explicit antichain matrix has Theta(n^2)
  bits, polynomial in the unary length n but exponential in the binary length.

Run with:  python3 -m unittest discover -s tests -v
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from hardness_boundaries import (  # noqa: E402
    P1,
    P2,
    binary_guaranteed_count,
    plog_cutoffs,
    smallest_collision,
    transfer_sizes,
    witness,
)
import structural_lower_bounds as slb  # noqa: E402


class NonReductionBarrier(unittest.TestCase):
    def test_witness_equal_e_different_f(self) -> None:
        self.assertEqual(slb.linear_extensions(P1), 8)
        self.assertEqual(slb.linear_extensions(P2), 8)
        self.assertEqual(slb.minimax(P1), 3)
        self.assertEqual(slb.minimax(P2), 4)
        self.assertNotEqual(slb.minimax(P1), slb.minimax(P2))

    def test_witness_is_returned(self) -> None:
        self.assertEqual(witness(), (P1, P2))

    def test_smallest_collision_is_n5_e8(self) -> None:
        c = smallest_collision(5)
        self.assertIsNotNone(c)
        n, e, lo, hi = c
        self.assertEqual(n, 5)
        self.assertEqual(e, 8)
        self.assertLess(slb.minimax(lo), slb.minimax(hi))

    def test_no_collision_below_n5(self) -> None:
        self.assertIsNone(smallest_collision(4))


class EncodingSensitiveContainment(unittest.TestCase):
    def test_transfer_sizes(self) -> None:
        for n in (4, 8, 16, 32):
            with self.subTest(n=n):
                unary, matrix, binary = transfer_sizes(n)
                self.assertEqual(unary, n)
                self.assertEqual(matrix, n * n)
                self.assertEqual(binary, n.bit_length())

    def test_matrix_is_polynomial_in_unary_but_exponential_in_binary(self) -> None:
        # matrix = n^2 = poly(n) in the unary length, but n^2 = 2^{2 log2 n}
        # = 2^{Theta(m)} in the binary length m = Theta(log n).
        for n in (8, 16, 32, 64):
            with self.subTest(n=n):
                _unary, matrix, binary = transfer_sizes(n)
                self.assertLessEqual(matrix, n * n)
                self.assertGreater(matrix, 2 * n)  # superlinear in n
                self.assertGreater(matrix, 2 ** binary)  # > 2^{|bin(n)|}


class EncodingAudit(unittest.TestCase):
    def test_plog_cutoff_values(self) -> None:
        self.assertEqual(
            plog_cutoffs(7),
            [(1, 0), (2, 1), (3, 1), (4, 2), (5, 2), (6, 2), (7, 3)],
        )

    def test_binary_language_is_not_sparse(self) -> None:
        # The guaranteed members already exceed 2^(m-3) for m >= 12.
        for m in (12, 16, 20):
            with self.subTest(m=m):
                self.assertGreater(binary_guaranteed_count(m), 2 ** (m - 3))


if __name__ == "__main__":
    unittest.main()
