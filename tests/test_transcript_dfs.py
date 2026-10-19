"""Regression checks for the transcript-only budgeted DFS.

Companion to ``scripts/transcript_dfs.py`` and the space refinement proved in
``docs/research-budgeted-dfs.md``.  These pin the reproducible finite facts:
the exact values ``S(n)`` for small ``n``, the threshold boundary on the empty
transcript, agreement with the memoized minimax oracle on **all** labelled
posets for ``n <= 4``, and the shape of the space accounting.  The whole file
runs in a few seconds and adds no heavy workload to CI.

Run with:  python3 -m unittest discover -s tests -v
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from budgeted_dfs import memoized_F  # noqa: E402
from transcript_dfs import (  # noqa: E402
    can_sort,
    compute_s,
    space_accounting,
)

KNOWN_S = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7}


def _closure_raw(succ, n):
    succ = list(succ)
    for k in range(n):
        for i in range(n):
            if (succ[i] >> k) & 1:
                succ[i] |= succ[k]
    return succ


def labelled_posets(n):
    """All transitively closed strict posets on n labelled elements.

    Enumerates the 3^{C(n,2)} orientations and keeps the acyclic closures;
    the deduplicated count is OEIS A001035 (1, 3, 19, 219 for n = 0..4).
    """
    seen = set()
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for code in range(3 ** len(pairs)):
        succ = [0] * n
        c = code
        for i, j in pairs:
            r = c % 3
            c //= 3
            if r == 1:
                succ[i] |= 1 << j
            elif r == 2:
                succ[j] |= 1 << i
        cl = _closure_raw(succ, n)
        if any((cl[i] >> i) & 1 for i in range(n)):
            continue
        seen.add(tuple(cl[i] & ~(1 << i) for i in range(n)))
    return sorted(seen)


def transcript_of(succ, n):
    return tuple((i, j) for i in range(n) for j in range(n)
                 if i != j and (succ[i] >> j) & 1)


class Values(unittest.TestCase):
    def test_exact_values_via_binary_search(self) -> None:
        for n in range(0, 5):
            with self.subTest(n=n):
                value, _dt = compute_s(n)
                self.assertEqual(value, KNOWN_S[n])


class Boundary(unittest.TestCase):
    def test_threshold_boundary_empty_transcript(self) -> None:
        for n in range(2, 6):
            s = KNOWN_S[n]
            with self.subTest(n=n):
                self.assertTrue(can_sort((), n, s))
                self.assertFalse(can_sort((), n, s - 1))

    def test_monotone_in_budget(self) -> None:
        n = 4
        prev = False
        for d in range(0, KNOWN_S[n] + 2):
            with self.subTest(d=d):
                res = can_sort((), n, d)
                self.assertGreaterEqual(res, prev)
                prev = res


class ExhaustiveAgreement(unittest.TestCase):
    def test_all_labelled_posets_n_le_4(self) -> None:
        # can_sort(transcript(P), d) == (F(P) <= d) on every labelled poset.
        expected_counts = {2: 3, 3: 19, 4: 219}
        for n in (2, 3, 4):
            F = memoized_F(n)
            posets = labelled_posets(n)
            self.assertEqual(len(posets), expected_counts[n])
            for succ in posets:
                fval = F[succ]
                tr = transcript_of(succ, n)
                for d in range(0, fval + 2):
                    with self.subTest(n=n, succ=succ, d=d):
                        self.assertEqual(can_sort(tr, n, d), fval <= d)


class TranscriptApi(unittest.TestCase):
    def test_tuple_input_is_not_mutated(self) -> None:
        tr = ((0, 1),)
        before = tuple(tr)
        can_sort(tr, 3, 3)
        self.assertEqual(tr, before)

    def test_list_input_is_not_mutated(self) -> None:
        # The shared mutable transcript is internal; the caller's list is copied
        # once by the wrapper and must be unchanged (and reusable) afterwards.
        tr = [(0, 1)]
        before = list(tr)
        first = can_sort(tr, 3, 3)
        self.assertEqual(tr, before)
        self.assertEqual(can_sort(tr, 3, 3), first)

    def test_empty_transcript_accepts_tuple_and_list(self) -> None:
        self.assertEqual(can_sort((), 3, 3), can_sort([], 3, 3))


class SpaceAccounting(unittest.TestCase):
    def test_transcript_beats_matrix_at_n_5(self) -> None:
        acc = space_accounting(5, KNOWN_S[5])
        self.assertLess(acc["total_bits"], acc["matrix_bits"])

    def test_stack_is_linear_in_budget(self) -> None:
        # Stack bits = (d+1) * (one O(log n)-bit frame), i.e. linear in d.
        per_frame = space_accounting(5, 1)["stack_bits"] - space_accounting(5, 0)["stack_bits"]
        self.assertGreater(per_frame, 0)
        for d in (0, 1, 5, 10):
            with self.subTest(d=d):
                self.assertEqual(space_accounting(5, d)["stack_bits"], (d + 1) * per_frame)


if __name__ == "__main__":
    unittest.main()
