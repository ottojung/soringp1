"""Exhaustive correctness checks for the compiled n=8 Ford--Johnson trie."""

import itertools
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from fo_tc_n8_fj import BUDGET, N, TREE, count_nodes, run_program, verify_tree  # noqa: E402
from generate_fo_tc_n8_fj import build  # noqa: E402
from upper_witness import ceil_log2, fj_upper_bound  # noqa: E402


class FordJohnsonN8Program(unittest.TestCase):
    def test_compiled_trie_matches_instrumented_fj_and_is_optimal(self):
        self.assertEqual(build(), TREE)
        self.assertEqual(fj_upper_bound(N), BUDGET)
        self.assertEqual(ceil_log2(__import__("math").factorial(N)), BUDGET)
        internal, leaves = count_nodes(TREE)
        self.assertGreater(internal, 0)
        self.assertEqual(leaves, 40320)
        self.assertEqual(verify_tree(), BUDGET)

    def test_every_permutation_reaches_its_sorted_output_within_budget(self):
        for hidden in itertools.permutations(range(N)):
            output, queries = run_program(TREE, hidden)
            self.assertEqual(tuple(sorted(output, key=hidden.__getitem__)), tuple(output))
            self.assertLessEqual(queries, BUDGET)


if __name__ == "__main__":
    unittest.main()
