import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "encoded_strategy_program", ROOT / "scripts/encoded_strategy_program.py"
)
ESP = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = ESP
SPEC.loader.exec_module(ESP)


class EncodedStrategyProgramTests(unittest.TestCase):
    def test_optimal_small_n_correct_and_within_budget(self):
        cases = [
            (ESP.optimal_program_n1, 1, 0),
            (ESP.optimal_program_n2, 2, 1),
            (ESP.optimal_program_n3, 3, 3),
            (ESP.optimal_program_n4, 4, 5),
        ]
        for ctor, n, k in cases:
            with self.subTest(n=n):
                p = ctor()
                self.assertEqual(p.n, n)
                self.assertEqual(p.k, k)
                res = ESP.check_program_on_all_orders(p)
                self.assertTrue(res["ok"], res)
                self.assertEqual(res["orders"], __import__("math").factorial(n))
                self.assertLessEqual(res["worst_q"], k)
                # combined runtime proxy: steps bounded by a small polynomial in (n, |code|)
                self.assertLessEqual(res["worst_steps"], 10 * n * (len(p.code) + n + 1))
                self.assertGreater(p.encoding_size_bits(), 0)

    def test_rejects_budget_exceeded_and_bad_emit(self):
        # force budget 0 but ask
        p = ESP.Program(
            n=2,
            k=0,
            regs=3,
            code=[
                ESP.Instruction("SET", (0, 0)),
                ESP.Instruction("SET", (1, 1)),
                ESP.Instruction("ASK", (0, 1, 2)),
                ESP.Instruction("EMIT_PERM"),
                ESP.Instruction("HALT"),
            ],
        )
        res = ESP.run_program(p, [0, 1])
        self.assertFalse(res.accepted)
        self.assertEqual(res.reason, "budget exceeded")

        # emit without total knowledge (no comparisons, n=2)
        p2 = ESP.Program(n=2, k=0, regs=0, code=[ESP.Instruction("EMIT_PERM"), ESP.Instruction("HALT")])
        res2 = ESP.run_program(p2, [0, 1])
        self.assertFalse(res2.accepted)
        self.assertEqual(res2.reason, "emit on non-total state")

    def test_binary_insertion_strategy_restricted_family(self):
        # Sound, polynomial-step, charged-oracle strategy at budget B(n) (not S(n) in general).
        results = ESP.check_binary_insertion_family(max_n=8)
        for n, info in results.items():
            with self.subTest(n=n):
                self.assertTrue(info["ok"], info)
                self.assertEqual(info["worst_q"], info["budget"])
                # steps proxy bounded polynomially (comparison steps + insert bookkeeping)
                self.assertLessEqual(info["worst_steps"], 5 * n * n * (n.bit_length() + 2))
        # known non-optimality example: B(5)=8 > S(5)=7, while still a valid restricted witness.
        self.assertEqual(results[5]["budget"], 8)

    def test_merge_sort_strategy_restricted_family(self):
        # Standard top-down merge sort as an adaptive charged-oracle strategy.
        # Sound and polynomial-step at budget M(n) (worst-case comparisons), not S(n) in general.
        results = ESP.check_merge_sort_family(max_n=8)
        expected = {1: 0, 2: 1, 3: 3, 4: 5, 5: 8, 6: 11, 7: 14, 8: 17}
        self.assertEqual(set(results), set(expected))
        for n, info in results.items():
            with self.subTest(n=n):
                self.assertTrue(info["ok"], info)
                self.assertEqual(info["budget"], expected[n])
                self.assertEqual(info["worst_q"], info["budget"])
                # bookkeeping + comparisons are O(n log n) per run in this accounting
                self.assertLessEqual(info["worst_steps"], 20 * max(n, 1) * (n.bit_length() + 1))
        # non-optimality examples: M(5)=8 > S(5)=7, M(6)=11 > S(6)=10 (S values are literature/kernel facts).
        self.assertEqual(results[5]["budget"], 8)
        self.assertEqual(results[6]["budget"], 11)

    def test_transitive_closure_knowledge_suffices(self):
        # after 0<1 and 1<2, state becomes total for n=3 without third ASK
        p = ESP.Program(
            n=3,
            k=2,
            regs=4,
            code=[
                ESP.Instruction("SET", (0, 0)),
                ESP.Instruction("SET", (1, 1)),
                ESP.Instruction("SET", (3, 2)),
                ESP.Instruction("ASK", (0, 1, 2)),  # 0<1
                ESP.Instruction("ASK", (1, 3, 2)),  # 1<2
                ESP.Instruction("EMIT_PERM"),
                ESP.Instruction("HALT"),
            ],
        )
        # X where 0<1<2
        res = ESP.run_program(p, [0, 1, 2])
        self.assertTrue(res.accepted, res.reason)
        self.assertEqual(res.output, [0, 1, 2])
        self.assertEqual(res.comparisons, 2)


if __name__ == "__main__":
    unittest.main()
