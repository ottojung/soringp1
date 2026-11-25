"""Regression and correctness tests for the symmetry-quotient benchmarks."""

import itertools
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from benchmark_symmetry_quotients import (  # noqa: E402
    A000112,
    DUAL_CLASSES,
    KNOWN,
    dual,
    extend,
    falsify_dual_branch,
    falsify_graph_transition,
    incomparable_pairs,
    iso_solve,
    labelled_solve,
    labelled_values,
    orbit_reps,
    quotient_classes,
)


class KnownValues(unittest.TestCase):
    def test_all_variants_return_known_s(self) -> None:
        for n in range(0, 6):
            with self.subTest(n=n):
                self.assertEqual(labelled_solve(n)[0], KNOWN[n])
                self.assertEqual(iso_solve(n)[0], KNOWN[n])
                self.assertEqual(iso_solve(n, use_dual=True)[0], KNOWN[n])
                self.assertEqual(
                    iso_solve(n, use_dual=True, use_orbits=True)[0], KNOWN[n])

    def test_shuffled_moves_do_not_change_values(self) -> None:
        import random
        for n in range(2, 6):
            with self.subTest(n=n):
                rng = random.Random(0)
                self.assertEqual(
                    iso_solve(n, use_dual=True, use_orbits=True,
                              shuffle=True, rng=rng)[0],
                    KNOWN[n])


class QuotientCounts(unittest.TestCase):
    def test_iso_class_counts_match_a000112(self) -> None:
        for n in range(0, 6):
            with self.subTest(n=n):
                self.assertEqual(iso_solve(n)[1], A000112[n])

    def test_dual_class_counts(self) -> None:
        for n in range(0, 6):
            with self.subTest(n=n):
                self.assertEqual(iso_solve(n, use_dual=True)[1], DUAL_CLASSES[n])


class DualityInvariance(unittest.TestCase):
    def test_f_is_duality_invariant(self) -> None:
        for n in range(0, 5):
            vals = labelled_values(n)
            for succ, value in vals.items():
                with self.subTest(n=n, succ=succ):
                    self.assertEqual(vals[dual(succ, n)], value)


class MoveOrbitExactness(unittest.TestCase):
    def test_orbit_reps_are_sound_at_n5(self) -> None:
        n = 5
        vals = labelled_values(n)
        checked = 0
        for succ in vals:
            ps = incomparable_pairs(succ, n)
            if not ps:
                continue
            reps = orbit_reps(succ, n)
            full = min(
                max(vals[extend(succ, i, j)], vals[extend(succ, j, i)])
                for i, j in ps
            )
            reduced = min(
                max(vals[extend(succ, i, j)], vals[extend(succ, j, i)])
                for i, j in reps
            )
            self.assertEqual(full, reduced)
            checked += 1
        self.assertGreater(checked, 0)


class Falsifications(unittest.TestCase):
    def test_dual_branch_may_not_be_dropped(self) -> None:
        witness = falsify_dual_branch()
        self.assertIsNotNone(witness)
        _, _, _, a, b = witness
        self.assertNotEqual(a, b)

    def test_comparability_graph_transition_ill_defined(self) -> None:
        witness = falsify_graph_transition(5)
        self.assertIsNotNone(witness)
        _, _, _, _, _, g1, g2 = witness
        self.assertNotEqual(g1, g2)

    def test_comparability_graph_does_not_determine_F(self) -> None:
        n = 7
        a = (0, 0, 1, 3, 5, 5, 37)
        b = (0, 0, 2, 1, 1, 9, 59)
        vals = quotient_classes(n)
        self.assertEqual(vals[a], 6)
        self.assertEqual(vals[b], 7)

        def edges(s):
            return frozenset(
                (min(i, j), max(i, j))
                for i in range(n) for j in range(n) if s[i] >> j & 1)

        ea, eb = edges(a), edges(b)
        isomorphic = any(
            frozenset((min(p[i], p[j]), max(p[i], p[j])) for (i, j) in ea) == eb
            for p in itertools.permutations(range(n))
        )
        self.assertTrue(isomorphic, "witness posets must have isomorphic graphs")


if __name__ == "__main__":
    unittest.main()
