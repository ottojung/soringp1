"""Regression tests for the budgeted-DFS pruning / move-reduction experiments.

These are computational checks on the experimental evaluator, not Lean proofs.
They are bounded to n <= 4 (exhaustive) and n = 5 (structured) so that they
never compete with other agents' n >= 6 exhaustive searches.

Soundness contract: every optimization in
scripts/budgeted_pruning_experiments.py must return the SAME boolean as the
reference can_sort, and must preserve the exact S(n) values.  The tests below
re-verify that contract exhaustively for n <= 4 and on structured n = 5 posets.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from budgeted_pruning_experiments import (  # noqa: E402
    all_posets,
    can_sort_pruned,
    can_sort_reference,
    compute_s,
    e_at_most,
    e_exceeds,
    factorial,
    F_value,
    linear_extensions,
    linear_extensions_bruteforce,
    memoized_F,
    merge_sort_upper_bound,
    ordinal_sum_blocks,
    structured_posets,
    width,
)

KNOWN_S = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7}

PRUNED_CONFIGS = (
    {"ext": "width"},
    {"ext": "enum"},
    {"ext": "exact"},
    {"hi_base": True},
    {"ext": "enum", "hi_base": True},
    {"orbits": True},
    {"ext": "enum", "orbits": True},
)


class ExtensionCountExactness(unittest.TestCase):
    def test_e_exceeds_matches_exact_for_all_posets_n4(self):
        for n in range(0, 5):
            for P in all_posets(n):
                e = linear_extensions(P, n)
                with self.subTest(n=n, P=P):
                    self.assertEqual(e, linear_extensions_bruteforce(P, n))
                    for cap in (0, 1, 3, 7, 8, 16, 64, 128):
                        self.assertEqual(e_exceeds(P, n, cap), e > cap)
                        self.assertEqual(e_at_most(P, n, cap), e <= cap)

    def test_width_factorial_is_a_valid_lower_bound_n4(self):
        # e(P) >= width(P)! for every poset with n <= 4 (certified range).
        for n in range(0, 5):
            for P in all_posets(n):
                with self.subTest(n=n, P=P):
                    self.assertGreaterEqual(
                        linear_extensions(P, n), factorial(width(P, n))
                    )


class DecisionEquivalence(unittest.TestCase):
    def _check(self, P, n, d):
        c_ref = [0]
        r_ref, cap_ref = can_sort_reference(P, n, d, c_ref, 2_000_000)
        for kw in PRUNED_CONFIGS:
            cq = [0]
            r_q, cap_q = can_sort_pruned(P, n, d, cq, 2_000_000, **kw)
            with self.subTest(P=P, d=d, cfg=kw):
                self.assertFalse(cap_q)
                self.assertEqual(r_q, r_ref)

    def test_exhaustive_n4(self):
        for n in range(0, 5):
            U = merge_sort_upper_bound(n)
            F = memoized_F(n) if n >= 2 else {(0,) * n: 0}
            for P in all_posets(n):
                fval = F[P]
                for d in range(0, min(fval + 2, U + 1)):
                    self._check(P, n, d)

    def test_structured_n5(self):
        for name, P in structured_posets(5).items():
            F = memoized_F(5)
            fval = F[P]
            for d in (max(0, fval - 1), fval):
                with self.subTest(poset=name, d=d):
                    self._check(P, 5, d)

    def test_hanamura_iwata_acceptance_is_sound(self):
        # Whenever e(P) <= 7 and d >= 3, the reference decision is True
        # (Hanamura-Iwata 2011), so the hi_base shortcut never lies.
        for n in range(2, 6):
            F = memoized_F(n)
            for P in all_posets(n):
                if e_at_most(P, n, 7):
                    for d in range(3, merge_sort_upper_bound(n) + 1):
                        c = [0]
                        r, cap = can_sort_reference(P, n, d, c, 2_000_000)
                        with self.subTest(n=n, P=P, d=d):
                            self.assertFalse(cap)
                            self.assertTrue(r)


class OrdinalSumAdditivity(unittest.TestCase):
    def test_allocation_matches_memoized_F_n4(self):
        for n in range(0, 5):
            F = memoized_F(n) if n >= 2 else {(0,) * n: 0}
            for P in all_posets(n):
                with self.subTest(n=n, P=P):
                    self.assertEqual(
                        F_value(P, n, use_ordinal_sum=True), F[P]
                    )

    def test_blocks_are_genuine_ordinal_sums_n4(self):
        for n in range(0, 5):
            for P in all_posets(n):
                blocks = ordinal_sum_blocks(P, n)
                if blocks is None:
                    continue
                # every earlier block is entirely below every later block
                for a in range(len(blocks)):
                    for b in range(a + 1, len(blocks)):
                        for x in blocks[a]:
                            for y in blocks[b]:
                                with self.subTest(n=n, P=P, x=x, y=y):
                                    self.assertTrue(P[x] >> y & 1)


class ValuesPreserved(unittest.TestCase):
    def test_pruned_binary_search_preserves_S(self):
        for n in range(0, 6):
            for kw in PRUNED_CONFIGS:
                val, calls, dt, cap = compute_s(
                    n, can_sort_pruned, node_cap=20_000_000, **kw)
                with self.subTest(n=n, cfg=kw):
                    self.assertFalse(cap)
                    self.assertEqual(val, KNOWN_S[n])

    def test_extension_cutoff_reduces_calls_n5(self):
        # The poly-space extension cutoff must not increase, and should sharply
        # decrease, the binary-search call count at n = 5.
        _, ref_calls, _, _ = compute_s(5, can_sort_reference)
        _, enum_calls, _, _ = compute_s(
            5, can_sort_pruned, node_cap=20_000_000, ext="enum")
        with self.subTest():
            self.assertLess(enum_calls, ref_calls // 10)


if __name__ == "__main__":
    unittest.main()
