"""Regression checks for the n=13 non-tightness finite-check probe.

Fast CI-friendly checks (< 10 s): small-n S(n) controls, C(13)=33, and the
Wells admissible heavier-child analysis at depths 1-2 under S_13 symmetry.
This does NOT verify S(13)>33 and makes no separation claim.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from s13_finite_check import (  # noqa: E402
    N, C, CAP, antichain, canon_key_shallow, add_relation, linear_extensions,
    ceil_log2, incomparable_pairs,
)
from one_ply_obstruction import minimax  # noqa: E402


class Controls(unittest.TestCase):
    def test_c13(self):
        import math
        self.assertEqual(N, 13)
        self.assertEqual(C, 33)
        self.assertEqual(ceil_log2(math.factorial(13)), 33)

    def test_small_s(self):
        self.assertEqual(minimax((0,) * 4), 5)
        self.assertEqual(minimax((0,) * 5), 7)


class WellsDepth2(unittest.TestCase):
    def test_depth1_all_admissible_one_orbit(self):
        A = antichain()
        cap = CAP(1)
        adm = 0
        classes = {}
        for (i, j) in incomparable_pairs(A):
            c1 = add_relation(A, i, j); c2 = add_relation(A, j, i)
            e1 = linear_extensions(c1); e2 = linear_extensions(c2)
            if e1 <= cap and e2 <= cap:
                adm += 1
                h = c1 if e1 >= e2 else c2
                classes[canon_key_shallow(h)] = h
        self.assertEqual(adm, 78)
        self.assertEqual(len(classes), 1)
        h = next(iter(classes.values()))
        self.assertEqual(linear_extensions(h), 3113510400)  # 13!/2

    def test_depth2_classes(self):
        A = antichain()
        P1 = add_relation(A, 0, 1)
        cap = CAP(2)
        nxt = {}
        adm = 0
        for (i, j) in incomparable_pairs(P1):
            c1 = add_relation(P1, i, j); c2 = add_relation(P1, j, i)
            e1 = linear_extensions(c1); e2 = linear_extensions(c2)
            if e1 <= cap and e2 <= cap:
                adm += 1
                h = c1 if e1 >= e2 else c2
                nxt[canon_key_shallow(h)] = h
        self.assertEqual(adm, 77)
        self.assertEqual(len(nxt), 3)
        es = sorted(linear_extensions(x) for x in nxt.values())
        import math
        self.assertEqual(es, [math.factorial(13)//4, math.factorial(13)//3, math.factorial(13)//3])
        for x in nxt.values():
            self.assertTrue(linear_extensions(x) <= cap)


if __name__ == '__main__':
    unittest.main()
