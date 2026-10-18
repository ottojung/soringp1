"""Regression checks for the budgeted DFS (docs/research-budgeted-dfs.md).

These pin the reproducible finite facts for the pure budgeted DFS
``CanSort(P, d)``: the exact values ``S(n)`` for small ``n``, the threshold
boundary ``S(n)-1``/``S(n)`` on the empty poset, and agreement with the
memoized minimax oracle on a few structured posets. No node caps are used: every
assertion is an exact result.

Run with:  python3 -m unittest discover -s tests -v
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from budgeted_dfs import (  # noqa: E402
    antichain,
    can_sort,
    chain_plus_isolated,
    compute_s_dfs,
    crown,
    disjoint_chains,
    memoized_F,
    total_order,
)

KNOWN_S = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7}


class Values(unittest.TestCase):
    def test_exact_values_via_binary_search(self) -> None:
        for n, expected in KNOWN_S.items():
            with self.subTest(n=n):
                value, _calls, _dt, hit_cap = compute_s_dfs(n)
                self.assertFalse(hit_cap, f"n={n}: node cap triggered, not exact")
                self.assertEqual(value, expected)


class Boundary(unittest.TestCase):
    def test_threshold_boundary_empty_poset(self) -> None:
        # CanSort(empty, S(n)) = True and CanSort(empty, S(n)-1) = False.
        for n in range(2, 6):
            s = KNOWN_S[n]
            with self.subTest(n=n):
                counter = [0]
                res, cap = can_sort(antichain(n), n, s, counter)
                self.assertFalse(cap)
                self.assertTrue(res)
                counter = [0]
                res, cap = can_sort(antichain(n), n, s - 1, counter)
                self.assertFalse(cap)
                self.assertFalse(res)

    def test_monotone_in_budget(self) -> None:
        # CanSort(P, d) is monotone in d on the empty poset.
        n = 4
        prev = None
        for d in range(0, KNOWN_S[n] + 2):
            with self.subTest(d=d):
                counter = [0]
                res, cap = can_sort(antichain(n), n, d, counter)
                self.assertFalse(cap)
                if prev is not None:
                    self.assertLessEqual(prev, res)
                prev = res


class StructuredPosets(unittest.TestCase):
    def test_agrees_with_memoized_oracle(self) -> None:
        # CanSort(P, d) == (F(P) <= d) on structured posets, small budgets.
        for n in (4, 5):
            F = memoized_F(n)
            posets = {
                "antichain": antichain(n),
                "total": total_order(n),
                "chain+iso": chain_plus_isolated(n),
                "2-chains": disjoint_chains(n, 2),
                "crown": crown(n) if n % 2 == 0 else None,
            }
            for name, P in posets.items():
                if P is None:
                    continue
                fval = F[P]
                for d in range(0, min(fval + 2, 5)):
                    with self.subTest(n=n, poset=name, d=d):
                        counter = [0]
                        res, cap = can_sort(P, n, d, counter)
                        self.assertFalse(cap)
                        self.assertEqual(res, fval <= d)

    def test_total_poset_is_immediately_true(self) -> None:
        # A total order is sorted regardless of remaining budget.
        for n in (3, 4, 5):
            with self.subTest(n=n):
                counter = [0]
                res, cap = can_sort(total_order(n), n, 0, counter)
                self.assertFalse(cap)
                self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
