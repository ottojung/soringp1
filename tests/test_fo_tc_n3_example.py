"""Tests for the n=3 elementary FO(TC) strategy-program example."""

import itertools
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from fo_tc_n3_example import (  # noqa: E402
    BUDGET,
    CLOCK,
    N,
    PROGRAM,
    START,
    Reject,
    run_program,
    verify,
)


class N3ExactBudget(unittest.TestCase):
    def test_all_orders_exact_budget(self) -> None:
        worst = 0
        for hidden in itertools.permutations(range(N)):
            out, queries, _ = run_program(PROGRAM, START, hidden, BUDGET, CLOCK)
            self.assertEqual(
                [hidden[k] for k in out], sorted(hidden),
                f"output not sorted for hidden order {hidden}",
            )
            worst = max(worst, queries)
        self.assertEqual(worst, 3)  # S(3)

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
            "e3": ("Halt",),
        }
        rejected = 0
        for hidden in itertools.permutations(range(N)):
            try:
                verify(const_prog, "only", hidden, BUDGET, CLOCK)
            except Reject:
                rejected += 1
        self.assertGreater(rejected, 0)

    def test_program_size_is_constant(self) -> None:
        # 5 internal Ask labels + 6 leaves x 4 labels (3 Emit + Halt).
        self.assertEqual(len(PROGRAM), 5 + 6 * 4)


class N3Script(unittest.TestCase):
    def test_script_passes(self) -> None:
        r = subprocess.run(
            [sys.executable, "scripts/fo_tc_n3_example.py"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("worst_case_queries=3", r.stdout)


if __name__ == "__main__":
    unittest.main()
