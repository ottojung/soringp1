"""Regression and correctness tests for the disjoint-union (parallel) module
reversal study.

Companion to scripts/parallel_module_probe.py and
docs/research-parallel-duality.md.

The central encoding fact guarded here is that the disjoint union A || B
shifts the second block's successor bitmasks left by len(A).  An earlier probe
forgot the shift, producing relations from B back into A and spurious F values;
the tests below fail loudly if that regression reappears.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from benchmark_symmetry_quotients import (  # noqa: E402
    dual,
    make_refined_canon,
    quotient_classes,
)
from parallel_module_probe import (  # noqa: E402
    _binom,
    disjoint_union,
    dual_union,
    is_self_dual,
    linear_extensions,
    verify,
    within_blocks,
)


class DisjointUnionEncoding(unittest.TestCase):
    def test_shift_keeps_relations_inside_blocks(self) -> None:
        # V = 0<1, 0<2 ; Lam = 0<2, 1<2 (on their own labels)
        V = (0b110, 0, 0)
        Lam = (0b100, 0b100, 0)
        for A, B in ((V, Lam), (Lam, V), (V, V), (Lam, Lam)):
            with self.subTest(A=A, B=B):
                P = disjoint_union(A, B)
                ok, off = within_blocks(P, len(A), len(B))
                self.assertTrue(ok, f"cross-block relation at {off}")

    def test_unshifted_second_block_is_not_a_disjoint_union(self) -> None:
        # Documents the corrected bug: copying B's masks verbatim points B's
        # relations back into A, so the cross-block check must fail.
        V = (0b110, 0, 0)
        Lam = (0b100, 0b100, 0)
        bad = tuple(list(V) + list(Lam))
        ok, off = within_blocks(bad, 3, 3)
        self.assertFalse(ok)
        self.assertIsNotNone(off)

    def test_dual_of_union_is_union_of_duals(self) -> None:
        V = (0b110, 0, 0)
        Lam = (0b100, 0b100, 0)
        P = disjoint_union(V, Lam)
        self.assertEqual(dual(P, 6), dual_union(V, Lam))

    def test_corrected_V_Lam_values(self) -> None:
        # The correct disjoint unions (all 6 keys, e = 80) have F = 7.
        V = (0b110, 0, 0)
        Lam = (0b100, 0b100, 0)
        for A, B in ((V, Lam), (Lam, V), (V, V), (Lam, Lam)):
            with self.subTest(A=A, B=B):
                P = disjoint_union(A, B)
                self.assertEqual(linear_extensions(P), 80)
                self.assertEqual(quotient_classes(6)[
                    make_refined_canon(6)(P)], 7)


class LinearExtensionIdentity(unittest.TestCase):
    def test_e_identity_n_le_5(self) -> None:
        for n in range(2, 6):
            by_size = {k: list(quotient_classes(k).keys())
                       for k in range(n + 1)}
            for a in range(1, n):
                b = n - a
                for A in by_size[a]:
                    for B in by_size[b]:
                        with self.subTest(n=n, a=a, A=A, B=B):
                            P = disjoint_union(A, B)
                            self.assertEqual(
                                linear_extensions(P),
                                _binom(n, a) * linear_extensions(A)
                                * linear_extensions(B))

    def test_e_identity_n6(self) -> None:
        # Spot-check the largest split rather than all 215 pairs.
        by_size = {k: list(quotient_classes(k).keys())
                   for k in range(7)}
        for A in by_size[3]:
            for B in by_size[3]:
                P = disjoint_union(A, B)
                self.assertEqual(
                    linear_extensions(P),
                    _binom(6, 3) * linear_extensions(A)
                    * linear_extensions(B))


class RestrictedTheorem(unittest.TestCase):
    def test_restricted_holds_n_le_6(self) -> None:
        for n in range(2, 7):
            with self.subTest(n=n):
                st = verify(n, check_e=False)
                self.assertEqual(st["restricted_violations"], 0)
                self.assertGreater(st["restricted_pairs"], 0)
                self.assertEqual(st["block_violations"], 0)

    def test_restricted_holds_n7(self) -> None:
        st = verify(7, check_e=False)
        self.assertEqual(st["restricted_violations"], 0)
        self.assertGreater(st["restricted_pairs"], 0)

    def test_self_dual_detection(self) -> None:
        V = (0b110, 0, 0)
        Lam = (0b100, 0b100, 0)
        chain = (0b110, 0b100, 0)
        antichain = (0, 0, 0)
        self.assertFalse(is_self_dual(V, 3, make_refined_canon(3)))
        self.assertFalse(is_self_dual(Lam, 3, make_refined_canon(3)))
        self.assertTrue(is_self_dual(chain, 3, make_refined_canon(3)))
        self.assertTrue(is_self_dual(antichain, 3, make_refined_canon(3)))


class GeneralCase(unittest.TestCase):
    def test_no_counterexample_n_le_6(self) -> None:
        # Evidence only: the general non-selfdual case is unresolved, but no
        # counterexample is found up to n=6.
        for n in range(2, 7):
            with self.subTest(n=n):
                st = verify(n, check_e=False)
                self.assertEqual(st["general_violations"], 0)

    def test_no_counterexample_n7(self) -> None:
        st = verify(7, check_e=False)
        self.assertEqual(st["general_violations"], 0)


if __name__ == "__main__":
    unittest.main()
