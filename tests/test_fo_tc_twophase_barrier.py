"""Two-phase compositional barrier (docs/research-fo-tc-twophase.md).

A strict sort-(n-1)-then-binary-insert program needs at least
S(n-1) + ceil(log2(n)) worst-case comparisons.  At n=5 that is 5 + 3 = 8,
which misses S(5) = 7; at n=6 and n=7 the same shape achieves the exact
values 10 and 13, respectively, both self-certified by the information bound.

Run with:  python3 -m unittest discover -s tests -v
"""

import sys
import unittest
from math import factorial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from fo_tc_twophase_barrier import compile_trie, run_program, verify_program


class TwoPhaseBarrier(unittest.TestCase):
    def test_n5_two_phase_misses_exact_budget(self) -> None:
        result = verify_program(5, 8)
        self.assertEqual(result["worst_queries"], 8)
        self.assertGreater(result["worst_queries"], 7)  # S(5) = 7
        self.assertEqual(result["strictness_rejects"], 119)

    def test_n6_two_phase_certifies_exact_budget(self) -> None:
        self.assertEqual(2 ** 9 < factorial(6), True)
        self.assertLessEqual(factorial(6), 2 ** 10)  # C(6) = 10
        result = verify_program(6, 10)
        self.assertEqual(result["worst_queries"], 10)  # hence S(6) = 10
        self.assertEqual(result["strictness_rejects"], 719)

    def test_insertion_phase_needs_three_queries(self) -> None:
        # Lemma premise: 5 rank slots need a height->=3 decision tree.
        self.assertLess(2 ** 2, 5)
        self.assertLessEqual(5, 2 ** 3)

    def test_runtime_performs_no_search(self) -> None:
        # Every internal label is a constant Ask pair fixed at compile time.
        for n in (5, 6, 7):
            program, _, _ = compile_trie(n)
            for rule in program.values():
                if rule[0] == "ask":
                    self.assertIsInstance(rule[1], int)
                    self.assertIsInstance(rule[2], int)
                    self.assertNotEqual(rule[1], rule[2])

    def test_polynomial_clock(self) -> None:
        for n, budget in ((5, 8), (6, 10), (7, 13)):
            program, leaf_output, root = compile_trie(n)
            worst_steps = 0
            from itertools import permutations
            for perm in permutations(range(n)):
                _, _, steps = run_program(program, leaf_output, root, n, perm)
                worst_steps = max(worst_steps, steps)
            clock = (n + budget + len(program)) ** 2
            self.assertLessEqual(worst_steps, clock)

    def test_n7_two_phase_self_certifies_exact_budget(self) -> None:
        self.assertLess(2 ** 12, factorial(7))
        self.assertLessEqual(factorial(7), 2 ** 13)  # C(7) = 13
        result = verify_program(7, 13)
        self.assertEqual(result["worst_queries"], 13)
        self.assertEqual(result["total_orders"], 5040)
        self.assertEqual(result["ask_labels"], 5039)
        self.assertEqual(result["strictness_rejects"], 5039)


if __name__ == "__main__":
    unittest.main()
