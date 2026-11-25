"""Regression checks for the k-ply hierarchy and root-balancing obstruction.

These pin the finite facts behind
``docs/research-unary-ply-obstruction.md``:

* the hierarchy is sound and monotone: ``L0 <= L1 <= ... <= F``;
* the root-balancing theorem (Theorem 1): at a chain-and-free poset with ``f``
  free elements, ``L_k = L0`` for ``k <= floor(f/2)``; in particular at the
  antichain ``L_k(P0) = C(n)`` for ``k <= floor(n/2)``;
* the contrast: the hierarchy is *strict* at the ``n = 5`` one-ply witness but
  *not* at the root;
* the width-based potential of falsification attempt F3 is not a valid lower
  bound.

All checks are bounded to ``n <= 5`` so that CI stays fast; the theorem has a
general proof, so no exhaustive ``n >= 5`` search is performed here.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from unary_ply_obstruction import (  # noqa: E402
    add_relation,
    ceil_log2,
    info_bound,
    linear_extensions,
    minimax,
    ply_hierarchy,
)

# Smallest one-ply strict witness (docs/research-one-ply-obstruction.md).
N5_WITNESS = (26, 0, 10, 0, 8)


def chain_and_free(n, chain_lengths, free):
    """Build a disjoint union of chains (of the given lengths) and free elements."""
    succ = (0,) * n
    idx = 0
    for length in chain_lengths:
        for i in range(length - 1):
            succ = add_relation(succ, idx + i, idx + i + 1)
        idx += length
    # remaining ``free`` elements are isolated by construction
    return succ


class HierarchyInequalities(unittest.TestCase):
    """``L0 <= L1 <= ... <= L_k <= F`` on a bounded poset set."""

    def test_l1_between_l0_and_f(self) -> None:
        L, _ = ply_hierarchy(5)
        from unary_ply_obstruction import all_posets

        for n in range(1, 5):
            for P in all_posets(n):
                l0, l1, f = info_bound(P), L(P, 1), minimax(P)
                with self.subTest(n=n, P=P):
                    self.assertGreaterEqual(l1, l0)
                    self.assertLessEqual(l1, f)

    def test_hierarchy_monotone(self) -> None:
        L, _ = ply_hierarchy(4)
        from unary_ply_obstruction import all_posets

        for P in all_posets(4):
            vals = [L(P, k) for k in range(0, 5)]
            with self.subTest(P=P):
                self.assertEqual(vals, sorted(vals))


class RootBalancing(unittest.TestCase):
    """Theorem 1: ``L_k(P0) = C(n)`` for ``k <= floor(n/2)``."""

    def test_antichain(self) -> None:
        for n in range(2, 6):
            L, _ = ply_hierarchy(n)
            P0 = (0,) * n
            C = info_bound(P0)
            for k in range(0, n // 2 + 1):
                with self.subTest(n=n, k=k):
                    self.assertEqual(L(P0, k), C)

    def test_chain_and_free_general_form(self) -> None:
        # 1 two-chain + 1 three-chain + f free: f free elements -> floor(f/2) plies.
        for f in range(0, 4):
            P = chain_and_free(5 + f, [2, 3], f)
            self.assertEqual(len(P), 5 + f)
            L, _ = ply_hierarchy(len(P))
            base = info_bound(P)
            for k in range(0, f // 2 + 1):
                with self.subTest(f=f, k=k):
                    self.assertEqual(L(P, k), base)

    def test_root_uses_all_n_free_elements(self) -> None:
        # The bound is tight in f: at f = 2 the two free elements let exactly one
        # balancing comparison happen (k = 1 = floor(2/2)).
        P = chain_and_free(4, [2], 2)  # one 2-chain + 2 free
        L, _ = ply_hierarchy(4)
        self.assertEqual(L(P, 0), info_bound(P))
        self.assertEqual(L(P, 1), info_bound(P))


class RootContrast(unittest.TestCase):
    """The hierarchy is strict at a non-root poset but not at the root."""

    def test_strict_at_n5_witness(self) -> None:
        L, _ = ply_hierarchy(5)
        self.assertEqual(info_bound(N5_WITNESS), 3)
        self.assertEqual(L(N5_WITNESS, 1), 4)
        self.assertGreater(L(N5_WITNESS, 1), info_bound(N5_WITNESS))

    def test_not_strict_at_root(self) -> None:
        L, _ = ply_hierarchy(5)
        P0 = (0,) * 5
        self.assertEqual(L(P0, 1), info_bound(P0))


class WidthPotentialFalsified(unittest.TestCase):
    """Falsification attempt F3: ``ceil(log2 e) + width - 1`` is not a bound."""

    def test_width_potential_exceeds_f(self) -> None:
        # P = {0 < 1, 2 free}: e = 3, width = 2, so phi = 2 + 1 = 3, but F = 2.
        P = (2, 0, 0)
        self.assertEqual(linear_extensions(P), 3)
        self.assertEqual(minimax(P), 2)
        phi = ceil_log2(linear_extensions(P)) + 2 - 1
        self.assertGreater(phi, minimax(P))


if __name__ == "__main__":
    unittest.main()
