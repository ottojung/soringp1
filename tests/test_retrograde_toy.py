"""Regression checks for the retrograde toy (docs/research-retrograde-toy.md).

These pin the finite, reproducible facts of the backward (retrograde) DP.

Bounded and CI-friendly: exhaustive validation only for ``n <= 3``, plus a
targeted set of ``n = 4`` posets including the antichain (``S(4) = 5``) and its
depth-5 certificate.  The comprehensive n=4 sweep is available offline as
``validate(n_max=4, d_max=5)`` and is deliberately NOT run here; run it with
``python3 scripts/retrograde_toy.py``.  Whole file runs in well under 5 s.

What is checked:
  * the exhaustive 3-state relation generation yields exactly the labelled
    posets A001035(n), and equals the comparison-reachable set from the
    antichain (so the ``219 states`` n=4 fixture is correct);
  * the layer-wise backward F agrees with an INDEPENDENT forward memoized
    ``CanSort(P, d)`` for every poset on ``n <= 3`` and every ``d <= 5``, and
    for the targeted n=4 posets;
  * the known values ``S(0..4) = 0,0,1,3,5`` are reproduced;
  * a genuine backward certificate for the n=4 antichain at depth 5 exists, is
    internally consistent, and has height exactly ``S(4)``;
  * one fixed comparison can have several predecessors (the source's Section
    4.1/5.7 point), which is why the reverse graph is built offline over all
    states rather than by inverting a single Hasse edge.

All assertions are exact finite results; none is asymptotic.

Run with:  python3 -m unittest discover -s tests -v
"""

import sys
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from retrograde_toy import (  # noqa: E402
    A001035,
    KNOWN_S,
    Retrograde,
    comparison_reachable,
    enumerate_posets,
    extend,
    find_multi_predecessor,
    is_chain,
    predecessors_for_pair,
    target_n4_posets,
    validate,
    validate_targeted_n4,
)


class Fixture(unittest.TestCase):
    def test_labelled_poset_counts(self) -> None:
        for n, expected in A001035.items():
            with self.subTest(n=n):
                posets, index = enumerate_posets(n)
                self.assertEqual(len(posets), expected)
                self.assertEqual(len(index), expected)

    def test_exhaustive_equals_comparison_reachable(self) -> None:
        # From the antichain, legal comparisons reach every labelled poset.
        for n in range(0, 5):
            with self.subTest(n=n):
                posets, _ = enumerate_posets(n)
                self.assertEqual(comparison_reachable(n), set(posets))

    def test_state_counts_n4(self) -> None:
        self.assertEqual(Retrograde(4).state_count(), 219)


class BackwardMatchesForward(unittest.TestCase):
    def test_exhaustive_n_le_3(self) -> None:
        rows, checks, ok = validate(n_max=3, d_max=5)
        self.assertTrue(ok)
        self.assertEqual(checks, (1 + 1 + 3 + 19) * 6)
        for r in rows:
            with self.subTest(n=r["n"]):
                self.assertEqual(r["states"], r["a001035"])
                self.assertEqual(r["S"], r["known_S"])

    def test_targeted_n4(self) -> None:
        F_by_name, checks, ok = validate_targeted_n4(d_max=5)
        self.assertTrue(ok)
        self.assertEqual(checks, len(target_n4_posets(4)) * 6)
        self.assertEqual(F_by_name["antichain"], 5)
        self.assertEqual(F_by_name["chain"], 0)

    def test_known_small_values(self) -> None:
        for n, expected in KNOWN_S.items():
            with self.subTest(n=n):
                self.assertEqual(Retrograde(n).S, expected)

    def test_f_is_min_over_moves(self) -> None:
        # F(P) = 1 + min over legal comparisons of max(F(children)), chains 0.
        R = Retrograde(4)
        for p in range(R.state_count()):
            with self.subTest(p=p):
                if not R.moves_of[p]:
                    self.assertEqual(R.F[p], 0)
                    continue
                best = min(
                    1 + max(R.F[c1], R.F[c2])
                    for (c1, c2) in (R.move_children[m] for m in R.moves_of[p])
                )
                self.assertEqual(R.F[p], best)


class BackwardCertificate(unittest.TestCase):
    def test_certificate_for_antichain_n4_depth_5(self) -> None:
        R = Retrograde(4)
        cert = R.certificate()
        self.assertEqual(R.S, 5)
        self.assertEqual(cert["succ"], (0, 0, 0, 0))
        self.assertEqual(cert["F"], 5)
        self.assertFalse(cert["leaf"])
        i, j = cert["compare"]
        c1, c2 = cert["children"]
        # The chosen comparison really produces the two referenced children.
        self.assertEqual(extend(cert["succ"], i, j), c1["succ"])
        self.assertEqual(extend(cert["succ"], j, i), c2["succ"])
        # F = 1 + max(child F) and both children are certified within 4.
        self.assertEqual(cert["F"], 1 + max(c1["F"], c2["F"]))
        self.assertLessEqual(c1["F"], 4)
        self.assertLessEqual(c2["F"], 4)
        self.assertTrue(R.check_certificate(cert))
        self.assertEqual(R.certificate_height(cert), 5)

    def test_certificate_leaves_are_chains(self) -> None:
        R = Retrograde(4)
        cert = R.certificate()

        def leaves(node):
            if node["leaf"]:
                yield node
            else:
                for c in node["children"]:
                    yield from leaves(c)

        found = list(leaves(cert))
        self.assertGreater(len(found), 0)
        for leaf in found:
            self.assertTrue(is_chain(leaf["succ"], 4))
            self.assertEqual(R.F[R.index[leaf["succ"]]], 0)
            self.assertEqual(leaf["F"], 0)


class MultiplePredecessors(unittest.TestCase):
    def test_one_comparison_can_have_two_predecessors(self) -> None:
        R = Retrograde(4)
        found = find_multi_predecessor(R)
        self.assertIsNotNone(found)
        child, (i, j), preds = found
        self.assertGreaterEqual(len(preds), 2)
        self.assertEqual(len(set(preds)), len(preds))
        for P in preds:
            self.assertFalse(P[i] & (1 << j))
            self.assertFalse(P[j] & (1 << i))
            self.assertEqual(extend(P, i, j), child)

    def test_chain_n3_witness(self) -> None:
        # Chain 0<1<2 on n=3 arises from adding 1<2 to either 0<1 (only) or
        # 0<1,0<2 -- two distinct predecessors for the same comparison.
        R = Retrograde(3)
        child = (6, 4, 0)
        preds = predecessors_for_pair(R.posets, child, 1, 2)
        self.assertEqual(set(preds), {(2, 0, 0), (6, 0, 0)})


class Runtime(unittest.TestCase):
    def test_ci_validation_under_5s(self) -> None:
        t0 = time.perf_counter()
        _, _, ok3 = validate(n_max=3, d_max=5)
        _, _, ok4 = validate_targeted_n4(d_max=5)
        dt = time.perf_counter() - t0
        self.assertTrue(ok3 and ok4)
        self.assertLess(dt, 5.0, f"CI validation took {dt:.3f}s (>5s)")


if __name__ == "__main__":
    unittest.main()
