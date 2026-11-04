"""Finite checks for the realizability-window analysis (n <= 5).

Run with:  python3 -m unittest discover -s tests -v
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from realizability_window import analyze, canon, extend  # noqa: E402


class RealizabilityWindowTests(unittest.TestCase):
    def test_window_exact_up_to_n5(self):
        for n, S, total, real in ((1, 0, 1, 1), (2, 1, 2, 2), (3, 3, 5, 5),
                                  (4, 5, 16, 12), (5, 7, 63, 29)):
            S2, classes, stat, depths, reach = analyze(n)
            self.assertEqual(S2, S)
            self.assertEqual(len(classes), total)
            self.assertEqual(len(depths), real)
            for succ, ds in depths.items():
                e, cov, pi, fv = stat[succ]
                self.assertEqual(ds, [d for d in range(S + 1)
                                      if cov <= d <= S - max(fv, pi)
                                      and e <= 2 ** (S - d)])

    def test_e8_pair_fate(self):
        # The documented linear-extension-count counterexample pair
        # (docs/research-state-compression.md, n=5): both have e=8 with
        # F(P)=3, F(Q)=4.  Experiment: the F=4 member Q is NOT realizable
        # at any depth; the F=3 member P is realizable at depth 4 only.
        n = 5
        _, classes, stat, depths, _ = analyze(n, check=False)

        def build(rels):
            succ = (0,) * n
            for (x, y) in rels:
                succ = extend(succ, x, y, n)
            return canon(succ, n)

        P = build(((4, 3), (4, 2), (3, 0), (3, 1)))
        Q = build(((2, 0), (4, 2), (3, 0), (3, 1), (4, 1)))
        self.assertEqual((stat[P][0], stat[P][3]), (8, 3))
        self.assertEqual((stat[Q][0], stat[Q][3]), (8, 4))
        self.assertEqual(depths.get(P, []), [4])
        self.assertIsNone(depths.get(Q))

    def test_ordinal_sum_witness(self):
        # C_2 (+) A_3 (chain below a 3-element antichain) IS realizable,
        # at depth exactly 4 on a height-7 tree; window = [4, 4].
        n = 5
        _, classes, stat, depths, _ = analyze(n, check=False)
        succ = extend(extend((0,) * n, 0, 1, n), 1, 2, n)  # 0<1, 1<2
        succ = extend(succ, 0, 2, n)
        succ = extend(succ, 1, 3, n)
        succ = extend(succ, 1, 4, n)
        succ = canon(succ, n)
        e, cov, pi, fv = stat[succ]
        self.assertEqual((e, cov, fv), (6, 4, 3))
        self.assertEqual(depths.get(succ, []), [4])


if __name__ == "__main__":
    unittest.main()
