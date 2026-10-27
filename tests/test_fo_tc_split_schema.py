"""Tests for the generalized split-schema (phase-coupling) barrier.

Verification strategy (two-sided, non-circular):
  * Upper bound: each witness tree is replayed over every initial extension;
    replay asserts the emitted order equals the hidden order and records the
    height.  This independently checks the claimed C(m,n).
  * Lower bound: an independent depth-bounded existence prover (plain
    recursion, no memoization, no greedy upper bound -- a different code
    path from the solver) confirms no completion tree of height C(m,n)-1
    exists for the three phase-coupling penalty cells.
  * Arithmetic: the split bound B(m,n) = S(m) + ceil(log2(n!/m!)) is checked
    against hand-computed values, including reproduction of the strict
    two-phase numbers B(n-1,n) = S(n-1) + ceil(log2 n).
"""

import math
import sys
from itertools import permutations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from fo_tc_split_schema import (  # noqa: E402
    S_KNOWN,
    allowed_pairs,
    initial_state,
    info_price,
    min_completion,
    replay,
    split_bound,
    _split,
)


def exists_tree(state, pairs, depth):
    """Independent prover: is there a completion tree of height <= depth?"""
    if len(state) <= 1:
        return True
    if depth == 0:
        return False
    if math.ceil(math.log2(len(state))) > depth:
        return False
    for (a, b) in pairs:
        r = _split(state, a, b)
        if r is None:
            continue
        if exists_tree(r[0], pairs, depth - 1) and exists_tree(
            r[1], pairs, depth - 1
        ):
            return True
    return False


def check_cell(m, n, expected_c):
    c, tree = min_completion(m, n)
    assert c == expected_c, f"C({m},{n}) = {c}, expected {expected_c}"
    assert c >= info_price(m, n), "completion beats the information bound?!"
    init = initial_state(m, n)
    assert len(init) == math.factorial(n) // math.factorial(m)
    worst = 0
    for perm in init:
        out, k = replay(tree, perm)
        assert out == perm
        worst = max(worst, k)
    assert worst == c, f"replay worst {worst} != claimed {c}"
    return c


def test_tight_completions():
    # Completion meets the information price: split schema can hit B(m,n).
    check_cell(2, 4, 4)
    check_cell(3, 5, 5)
    check_cell(2, 5, 6)
    check_cell(5, 7, 6)


def test_phase_coupling_penalties():
    # Completion strictly exceeds the information price: the counting bound
    # B(m,n) is unachievable; true split cost is S(m) + C(m,n) > B(m,n).
    check_cell(4, 6, 6)
    check_cell(3, 6, 8)
    check_cell(4, 7, 9)


def test_penalty_lower_bounds_independent():
    # No completion tree of height C(m,n)-1 (independent code path).
    for (m, n, c) in [(4, 6, 6), (3, 6, 8), (4, 7, 9)]:
        st, pr = initial_state(m, n), allowed_pairs(m, n)
        assert not exists_tree(st, pr, c - 1), f"height-{c - 1} tree exists?!"


def test_split_bound_arithmetic():
    assert S_KNOWN[5] == 7 and S_KNOWN[6] == 10 and S_KNOWN[7] == 13
    # Strict two-phase numbers reproduced: B(n-1,n) = S(n-1)+ceil(log2 n).
    assert split_bound(4, 5) == 5 + 3
    assert split_bound(8, 9) == 16 + 4
    # Hand-checked cells.
    assert split_bound(2, 5) == 1 + 6 == S_KNOWN[5]  # exact-looking
    assert split_bound(4, 6) == 5 + 5 == S_KNOWN[6]  # exact-looking
    assert split_bound(3, 5) == 3 + 5 == 8 > S_KNOWN[5]  # miss


def test_new_barriers():
    # True split-schema cost S(m)+C(m,n) strictly exceeds S(n) even where
    # the counting bound B(m,n) looked exact: (4,6), (3,6), (4,7).
    assert S_KNOWN[4] + 6 == 11 > S_KNOWN[6] == 10
    assert S_KNOWN[3] + 8 == 11 > S_KNOWN[6] == 10
    assert S_KNOWN[4] + 9 == 14 > S_KNOWN[7] == 13
    # Positive contrast: split-(2,3) hits S(5) where strict two-phase misses.
    assert S_KNOWN[2] + 6 == 7 == S_KNOWN[5]
