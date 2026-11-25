"""Two-phase compositional barrier (docs/research-fo-tc-twophase.md).

A strict sort-(n-1)-then-binary-insert program needs at least
S(n-1) + ceil(log2(n)) worst-case comparisons.  At n=5 that is 5 + 3 = 8,
which misses S(5) = 7; at n=6 and n=7 the same shape achieves the exact
values 10 and 13, respectively, both self-certified by the information bound.

Run with:  python3 -m unittest discover -s tests -v
"""

import sys
import unittest
from math import ceil, factorial, log2
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from fo_tc_twophase_barrier import (
    compile_trie,
    run_program,
    strategy_worst_case,
    verify_program,
)


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
        for n in (5, 6, 7, 8):
            program, _, _ = compile_trie(n)
            for rule in program.values():
                if rule[0] == "ask":
                    self.assertIsInstance(rule[1], int)
                    self.assertIsInstance(rule[2], int)
                    self.assertNotEqual(rule[1], rule[2])

    def test_polynomial_clock(self) -> None:
        for n, budget in ((5, 8), (6, 10), (7, 13), (8, 16)):
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

    def test_n8_two_phase_self_certifies_exact_budget(self) -> None:
        self.assertLess(2 ** 15, factorial(8))
        self.assertLessEqual(factorial(8), 2 ** 16)  # C(8) = 16
        result = verify_program(8, 16)
        self.assertEqual(result["worst_queries"], 16)
        self.assertEqual(result["total_orders"], 40320)
        self.assertEqual(result["ask_labels"], 40319)
        self.assertEqual(result["strictness_rejects"], 40319)


    def test_n9_two_phase_misses_exact_budget_strategy_level(self) -> None:
        # S(9) = 19 per the value table in docs/research-plan.md (Knuth,
        # Wells, Stober-Weiss lineage). The full 9! trie (362,880 leaves)
        # is not compiled; the strategy-level transcript count is checked
        # exhaustively instead -- same decision procedure, no trie.
        worst, total = strategy_worst_case(9)
        self.assertEqual(total, 362880)
        self.assertEqual(worst, 16 + 4)  # S(8) + ceil(log2(9)) = 20
        self.assertGreater(worst, 19)  # S(9) = 19: second miss after n=5

    def test_compositional_exactness_characterization(self) -> None:
        # Known S(n) for 1 <= n <= 12 per docs/research-plan.md baseline.
        known_s = {1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10,
                   7: 13, 8: 16, 9: 19, 10: 22, 11: 26, 12: 30}
        exact, miss = [], []
        for n in range(2, 13):
            bound = known_s[n - 1] + ceil(log2(n))
            (exact if bound == known_s[n] else miss).append(n)
            self.assertGreaterEqual(bound, known_s[n])
        self.assertEqual(exact, [2, 3, 4, 6, 7, 8, 11, 12])
        self.assertEqual(miss, [5, 9, 10])


if __name__ == "__main__":
    unittest.main()
