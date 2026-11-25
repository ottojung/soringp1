"""Tests for the n=4 elementary FO(TC) strategy-program example."""

import itertools
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from fo_tc_n4_example import (  # noqa: E402
    BUDGET,
    CLOCK,
    N,
    PROGRAM,
    START,
    Reject,
    run_program,
    verify,
)


class N4ExactBudget(unittest.TestCase):
    def test_all_orders_exact_budget(self) -> None:
        worst = 0
        for hidden in itertools.permutations(range(N)):
            out, queries, _ = run_program(PROGRAM, START, hidden, BUDGET, CLOCK)
            self.assertEqual(
                [hidden[k] for k in out], sorted(hidden),
                f"output not sorted for hidden order {hidden}",
            )
            worst = max(worst, queries)
        self.assertEqual(worst, 5)  # S(4) = ceil(log2(24)) = 5

    def test_verifier_accepts_all_orders(self) -> None:
        for hidden in itertools.permutations(range(N)):
            with self.subTest(hidden=hidden):
                self.assertLessEqual(
                    verify(PROGRAM, START, hidden, BUDGET, CLOCK), BUDGET
                )

    def test_verifier_rejects_constant_output(self) -> None:
        const_prog = {
            "only": ("Emit", 0, 0, "e1"),
            "e1": ("Emit", 1, 1, "e2"),
            "e2": ("Emit", 2, 2, "e3"),
            "e3": ("Emit", 3, 3, "e4"),
            "e4": ("Halt",),
        }
        rejected = 0
        for hidden in itertools.permutations(range(N)):
            try:
                verify(const_prog, "only", hidden, BUDGET, CLOCK)
            except Reject:
                rejected += 1
        self.assertGreater(rejected, 0)

    def test_program_size_is_fixed(self) -> None:
        # 5 phase-1 Ask labels + 6 triples x (3 insertion Asks +
        # 4 outcomes x 5 labels per Emit-chain+Halt).
        self.assertEqual(len(PROGRAM), 5 + 6 * (3 + 4 * 5))
        asks = sum(1 for r in PROGRAM.values() if r[0] == "Ask")
        self.assertEqual(asks, 5 + 6 * 3)

    def test_all_ask_rules_are_constant_pairs(self) -> None:
        # Every Ask rule is a constant (i, j): trivially FO(TC)_v-expressible.
        for label, rule in PROGRAM.items():
            if rule[0] == "Ask":
                _, i, j, yes, no = rule
                self.assertNotEqual(i, j, f"self-query at {label}")
                self.assertTrue(0 <= i < N and 0 <= j < N, f"bad pair at {label}")
                self.assertIn(yes, PROGRAM, f"dangling branch at {label}")
                self.assertIn(no, PROGRAM, f"dangling branch at {label}")


class N4Script(unittest.TestCase):
    def test_script_passes(self) -> None:
        r = subprocess.run(
            [sys.executable, "scripts/fo_tc_n4_example.py"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("worst_case_queries=5", r.stdout)


if __name__ == "__main__":
    unittest.main()
