"""Regression tests for the bidirectional advice prototype (Stober-Weiss 2023).

These are computational checks on the experimental evaluator, not Lean proofs.
They verify:
1. Exact S(n) values for n<=5 are reproduced.
2. Advice tables are sound: every stored entry matches independent re-evaluation.
3. UNKNOWN != FALSE: partial tables do not cause false negatives.
4. Forward search with full advice never does more work than plain DFS.
5. Table size matches known labeled poset counts (A001035-related).

Run with:  python3 -m unittest discover -s tests -v
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from bidirectional_advice import (  # noqa: E402
    backward_table,
    backward_table_partial,
    forward_search,
    plain_dfs,
    precompute_pair_masks,
    setup,
    verify_advice_sound,
    KNOWN_S,
)


class TestExactValues(unittest.TestCase):
    """S(n) values for n<=5 must be reproduced exactly."""

    def test_known_values(self):
        for n in range(1, 6):
            perms, nperm, perm_idx = setup(n)
            pairs = precompute_pair_masks(n, perms, perm_idx)
            full_mask = (1 << nperm) - 1
            advice = backward_table(n, pairs, full_mask)
            s_n = KNOWN_S[n]
            self.assertEqual(advice[full_mask], s_n,
                             f"S({n}) should be {s_n}, got {advice[full_mask]}")


class TestSoundness(unittest.TestCase):
    """Every advice table entry must match independent re-evaluation."""

    def test_soundness_all_n(self):
        for n in range(1, 6):
            perms, nperm, perm_idx = setup(n)
            pairs = precompute_pair_masks(n, perms, perm_idx)
            full_mask = (1 << nperm) - 1
            advice = backward_table(n, pairs, full_mask)
            errors = verify_advice_sound(n, pairs, advice)
            self.assertEqual(errors, [],
                             f"Soundness failure for n={n}: {errors[:3]}")


class TestUnknownNotFalse(unittest.TestCase):
    """Partial tables must not cause false negatives in forward search."""

    def test_partial_table_no_false_negative(self):
        for n in range(1, 6):
            perms, nperm, perm_idx = setup(n)
            pairs = precompute_pair_masks(n, perms, perm_idx)
            full_mask = (1 << nperm) - 1
            s_n = KNOWN_S[n]
            for partial_budget in range(0, s_n):
                partial_advice = backward_table_partial(n, pairs, full_mask, partial_budget)
                solvable, nodes, comps = forward_search(
                    n, pairs, full_mask, s_n, partial_advice)
                self.assertTrue(solvable,
                                f"n={n}, partial_budget={partial_budget}: "
                                f"forward search returned False (false negative)")


class TestForwardVsDFS(unittest.TestCase):
    """Forward search with advice must never do more work than plain DFS."""

    def test_forward_never_worse(self):
        for n in range(1, 6):
            perms, nperm, perm_idx = setup(n)
            pairs = precompute_pair_masks(n, perms, perm_idx)
            full_mask = (1 << nperm) - 1
            s_n = KNOWN_S[n]
            advice = backward_table(n, pairs, full_mask)
            _, nodes_fwd, _ = forward_search(n, pairs, full_mask, s_n, advice)
            _, nodes_dfs = plain_dfs(n, pairs, full_mask, s_n)
            self.assertLessEqual(nodes_fwd, nodes_dfs,
                                 f"n={n}: fwd={nodes_fwd} > dfs={nodes_dfs}")


class TestTableSizes(unittest.TestCase):
    """Table sizes must match known labeled poset counts."""

    def test_table_size_bounds(self):
        expected = {1: 1, 2: 3, 3: 19, 4: 219, 5: 4231}
        for n in range(1, 6):
            perms, nperm, perm_idx = setup(n)
            pairs = precompute_pair_masks(n, perms, perm_idx)
            full_mask = (1 << nperm) - 1
            advice = backward_table(n, pairs, full_mask)
            self.assertEqual(len(advice), expected[n],
                             f"n={n}: expected {expected[n]} states, got {len(advice)}")


if __name__ == '__main__':
    unittest.main()
