"""Tests for module reversal of posets and the exact minimax value F.

Companion to docs/research-orientation-modules.md and
scripts/orientation_modules_probe.py.

The headline facts under test:

  * interval modules (every outside key comparable to the module) have
    reversal-invariant F and e (proved theorem);
  * ALL module reversals preserve F for n <= 6 (a small-size false positive);
  * module reversal does NOT preserve F at n = 7: the comparability-graph
    witness pair A, B lies in one module-reversal class and one MDT class, yet
    F(A) = 6 != 7 = F(B);
  * the module condition is essential (non-module reversal is cyclic or
    changes F already at n = 3).
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from benchmark_symmetry_quotients import (  # noqa: E402
    _cgraph,
    make_refined_canon,
    quotient_classes,
)
from orientation_modules_probe import (  # noqa: E402
    all_modules,
    falsify_nonmodule_reversal,
    is_module,
    linear_extensions,
    mdt_signature,
    reverse_module,
)

A = (0, 0, 1, 3, 5, 5, 37)   # F = 6
B = (0, 0, 2, 1, 1, 9, 59)   # F = 7, same comparability graph and MDT as A

_N7_CACHE = {}


def n7_values():
    if "vals" not in _N7_CACHE:
        _N7_CACHE["vals"] = quotient_classes(7)
        _N7_CACHE["canon"] = make_refined_canon(7)
    return _N7_CACHE["vals"], _N7_CACHE["canon"]


def interval_module(succ, n, S):
    """S is an interval module: a module comparable to every outside key."""
    if not is_module(succ, n, S):
        return False
    elems = [i for i in range(n) if S >> i & 1]
    out = [i for i in range(n) if not (S >> i & 1)]
    return all((succ[a] >> b & 1) or (succ[b] >> a & 1)
               for a in elems for b in out)


class IntervalTheorem(unittest.TestCase):
    def test_interval_reversal_preserves_F_and_e(self) -> None:
        for n in range(0, 6):
            vals = quotient_classes(n)
            canon = make_refined_canon(n)
            for c in vals:
                for S in all_modules(c, n):
                    if S == 0 or S == (1 << n) - 1:
                        continue
                    if not interval_module(c, n, S):
                        continue
                    r = reverse_module(c, n, S)
                    with self.subTest(n=n, c=c, S=S):
                        self.assertIsNotNone(r)
                        self.assertEqual(vals[canon(r)], vals[c])
                        self.assertEqual(linear_extensions(r, n),
                                         linear_extensions(c, n))

    def test_series_quotients_are_interval_modules(self) -> None:
        # every series-quotient module is an interval module
        for n in range(2, 6):
            vals = quotient_classes(n)
            for c in vals:
                for S in all_modules(c, n):
                    if S in (0, (1 << n) - 1):
                        continue
                    out = [i for i in range(n) if not (S >> i & 1)]
                    complete = all(
                        (c[a] >> b & 1) or (c[b] >> a & 1)
                        for a in [i for i in range(n) if S >> i & 1] for b in out)
                    if complete:
                        with self.subTest(n=n, c=c, S=S):
                            self.assertTrue(interval_module(c, n, S))


class SmallNFalsePositive(unittest.TestCase):
    def test_all_module_reversals_preserve_F_up_to_n6(self) -> None:
        """n <= 6 gives no counterexample: this is why n = 7 is needed."""
        for n in range(0, 7):
            vals = quotient_classes(n)
            canon = make_refined_canon(n)
            for c in vals:
                for S in all_modules(c, n):
                    if S == 0 or S == (1 << n) - 1:
                        continue
                    r = reverse_module(c, n, S)
                    with self.subTest(n=n, c=c, S=S):
                        self.assertIsNotNone(r)
                        self.assertEqual(vals[canon(r)], vals[c])


class N7Counterexample(unittest.TestCase):
    def test_module_reversal_changes_F_at_n7(self) -> None:
        vals, canon = n7_values()
        P = (0, 0, 2, 1, 1, 9, 59)          # = B, F = 7
        S = 0b111001                        # keys {0,3,4,5}
        self.assertTrue(is_module(P, 7, S))
        r = reverse_module(P, 7, S)
        self.assertIsNotNone(r)
        self.assertEqual(vals[P], 7)
        self.assertEqual(vals[canon(r)], 6)

    def test_witness_pair_is_one_module_reversal_class(self) -> None:
        vals, canon = n7_values()
        self.assertEqual(vals[A], 6)
        self.assertEqual(vals[B], 7)
        # A --reverse S--> ... --reverse S'--> B, via the two intermediates
        inter = canon(reverse_module(A, 7, 0b1110100))
        self.assertNotEqual(inter, A)
        self.assertIn(inter, {(0, 0, 1, 1, 3, 5, 45)})
        self.assertEqual(vals[inter], 7)
        # B reverses to the F=6 intermediate
        self.assertEqual(vals[canon(reverse_module(B, 7, 0b111001))], 6)

    def test_same_comparability_graph(self) -> None:
        self.assertEqual(_cgraph(A, 7), _cgraph(reverse_module(A, 7, 0b1110100), 7))

    def test_same_modular_decomposition_tree(self) -> None:
        self.assertEqual(mdt_signature(A, 7), mdt_signature(B, 7))
        self.assertEqual(mdt_signature(A, 7),
                         mdt_signature(reverse_module(B, 7, 0b111001), 7))


class NonModuleFalsification(unittest.TestCase):
    def test_module_condition_is_essential(self) -> None:
        w = falsify_nonmodule_reversal(4)
        self.assertIsNotNone(w["cyclic"])
        self.assertIsNotNone(w["value"])
        # cyclic: reversing a non-module can leave the poset world entirely
        n, c, S = w["cyclic"]
        self.assertIsNone(reverse_module(c, n, S))
        # value: reversing a non-module can change F (already at n = 3)
        n, c, S, fc, fr = w["value"]
        self.assertNotEqual(fc, fr)


if __name__ == "__main__":
    unittest.main()
