"""Finite checks for the realizability-window analysis (n <= 5).

Run with:  python3 -m unittest discover -s tests -v
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from realizability_window import analyze, canon, extend  # noqa: E402


class RealizabilityWindowTests(unittest.TestCase):
    def test_corrected_reachability_up_to_n5(self):
        for n, S, total, real in ((1, 0, 1, 1), (2, 1, 2, 2), (3, 3, 5, 5),
                                  (4, 5, 16, 12), (5, 7, 63, 19)):
            S2, classes, stat, depths, reach = analyze(n, check=False)
            self.assertEqual(S2, S)
            self.assertEqual(len(classes), total)
            self.assertEqual(len(depths), real)
            for d, states in enumerate(reach):
                for succ in states:
                    e, cov, pi, fv = stat[succ]
                    self.assertLessEqual(cov, d)
                    self.assertLessEqual(d, S - max(fv, pi))
                    self.assertLessEqual(e, 2 ** (S - d))

    def test_window_sufficiency_counterexample(self):
        # The old one-child budget filter admitted this state, although its
        # occurrence window holds. At its predecessor's comparison, the
        # sibling continuation is one comparison too expensive.
        n = 5
        S, classes, stat, depths, reach = analyze(n, check=False)
        succ = (0, 0, 0, 1, 9)
        self.assertEqual(S, 7)
        self.assertIn(succ, classes)
        self.assertEqual(stat[succ], (20, 2, 2, 5))
        self.assertNotIn(succ, reach[2])
        self.assertLessEqual(2, S - max(stat[succ][2], stat[succ][3]))

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

    def test_ordinal_sum_claimed_witness_is_not_reachable(self):
        # The earlier note claimed C_2 (+) A_3 was reached at depth 4 by
        # this declaration order. The comparison at depth 2 is invalid:
        # one sibling needs 5 further comparisons, but only 4 remain.
        n = 5
        _, classes, stat, depths, _ = analyze(n, check=False)
        succ = extend(extend((0,) * n, 0, 1, n), 1, 2, n)  # 0<1, 1<2
        succ = extend(succ, 0, 2, n)
        succ = extend(succ, 1, 3, n)
        succ = extend(succ, 1, 4, n)
        succ = canon(succ, n)
        e, cov, pi, fv = stat[succ]
        self.assertEqual((e, cov, fv), (6, 4, 3))
        self.assertNotIn(4, depths.get(succ, []))
        parent = canon((0, 0, 0, 1, 2), n)
        c0 = canon(extend(parent, 0, 2, n), n)
        c1 = canon(extend(parent, 2, 0, n), n)
        self.assertEqual(sorted((stat[c0][3], stat[c1][3])), [4, 5])


if __name__ == "__main__":
    unittest.main()
