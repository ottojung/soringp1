#!/usr/bin/env python3
"""Generalized split-schema (phase-coupling) barrier for strategy programs.

Research question (Antonina issue fervor; umbrella #301): the strict
two-phase schema (sort n-1 keys, then insert the last one) is already ruled
out as a uniform exact route (docs/research-fo-tc-twophase.md).  This script
pins down the strictly broader *split-schema* compiler route: phase 1 fully
sorts a fixed m-subset of the keys, phase 2 performs arbitrary further
comparisons.  Lemma (paper proof, see docs/research-fo-tc-split-schema.md):

    any deterministic split-(m, n-m) program needs at least
        B(m,n) = S(m) + ceil(log2(n! / m!))
    comparisons worst-case.

The script then computes, by exact exhaustive minimax search over knowledge
states, the true optimal *completion cost* C(m,n) (phase-2 minimax cost given
a sorted m-chain) for small cells, and checks whether the information-bound
price ceil(log2(n!/m!)) is achievable -- i.e. whether phase coupling lets a
split program reach B(m,n), and whether B(m,n) = S(n) (exact) or not.

Run with:  python3 scripts/fo_tc_split_schema.py
"""

from __future__ import annotations

import math
import sys
from itertools import permutations

# Known exact sorting numbers S(0)..S(12) (docs/problem.md, docs/literature.md;
# OEIS A036604; Wells 1965; Peczarski 2002/2004; Stober-Weiss 2023).
S_KNOWN = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10,
           7: 13, 8: 16, 9: 19, 10: 22, 11: 26, 12: 30}


def info_price(m, n):
    """ceil(log2(n!/m!)): number of completions phase 2 must distinguish."""
    return math.ceil(math.log2(math.factorial(n) // math.factorial(m)))


def split_bound(m, n):
    """Lower bound B(m,n) = S(m) + ceil(log2(n!/m!)) for split programs."""
    return S_KNOWN[m] + info_price(m, n)


# ---------------------------------------------------------------------------
# Exact minimax completion cost C(m,n) by exhaustive search over knowledge
# states.  Chain keys are 0..m-1 (fixed relative order); loose keys are
# m..n-1.  A knowledge state is the frozenset of linear extensions (rank
# tuples) still consistent with all answers so far.  Chain--chain pairs are
# never queried (already known).  Search is exact: every splitting pair is
# tried, with memoization and information-bound pruning.
# ---------------------------------------------------------------------------

def initial_state(m, n):
    ok = []
    for p in permutations(range(n)):
        if all(p[i] < p[i + 1] for i in range(m - 1)):
            ok.append(p)
    return frozenset(ok)


def allowed_pairs(m, n):
    return tuple((a, b) for a in range(n) for b in range(a + 1, n)
                 if not (a < m and b < m))


def _lb(state):
    return math.ceil(math.log2(len(state))) if len(state) > 1 else 0


def _split(state, a, b):
    less = frozenset(p for p in state if p[a] < p[b])
    if not less or len(less) == len(state):
        return None
    return less, state - less


def greedy_ub(state, pairs, memo):
    """Feasible completion cost via most-balanced-first descent (upper bound)."""
    s = state
    cost = 0
    while len(s) > 1:
        best, best_key = None, None
        for (a, b) in pairs:
            r = _split(s, a, b)
            if r is None:
                continue
            imbalance = abs(len(r[0]) - len(r[1]))
            if best is None or imbalance < best:
                best, best_key = imbalance, ((a, b), r)
        if best_key is None:  # pragma: no cover - cannot happen for m < n
            raise AssertionError("no splitting query but state not singleton")
        (_, r) = best_key
        s = r[0] if len(r[0]) >= len(r[1]) else r[1]
        cost += 1
    return cost


def min_completion(m, n):
    """Return (C(m,n), witness_tree) with C(m,n) the exact minimax cost.

    witness_tree is nested ('q', a, b, left, right) / ('done', perm) and
    replays correctly over every initial extension (checked by tests).
    """
    pairs = allowed_pairs(m, n)
    memo = {}

    def solve(state):
        if len(state) <= 1:
            return 0
        if state in memo:
            return memo[state]
        lb = _lb(state)
        ub = greedy_ub(state, pairs, memo)
        best = ub
        queries = []
        for (a, b) in pairs:
            r = _split(state, a, b)
            if r is None:
                continue
            queries.append(((a, b), r))
        queries.sort(key=lambda q: abs(len(q[1][0]) - len(q[1][1])))
        for (_, (left, right)) in queries:
            if 1 + max(_lb(left), _lb(right)) >= best:
                continue
            c = 1 + max(solve(left), solve(right))
            if c < best:
                best = c
                if best <= lb:
                    break
        memo[state] = best
        return best

    def build(state):
        if len(state) <= 1:
            return ("done", next(iter(state)))
        target = solve(state)
        for (a, b) in pairs:
            r = _split(state, a, b)
            if r is None:
                continue
            left, right = r
            if 1 + max(solve(left), solve(right)) == target:
                return ("q", a, b, build(left), build(right))
        raise AssertionError("no optimal query found")  # pragma: no cover

    init = initial_state(m, n)
    cost = solve(init)
    return cost, build(init)


def replay(tree, perm):
    """Simulate witness tree on hidden rank-tuple perm; return (output, cost)."""
    cost = 0
    node = tree
    while node[0] == "q":
        _, a, b, left, right = node
        cost += 1
        node = left if perm[a] < perm[b] else right
    assert node[1] == perm, "witness tree mis-sorts an extension"
    return node[1], cost


def main():
    print("m n  P=n!/m! info B(m,n)=S(m)+info S(n) exact? C(m,n)")
    for n in range(2, 13):
        for m in range(1, n):
            p = math.factorial(n) // math.factorial(m)
            b = split_bound(m, n)
            s = S_KNOWN[n]
            print(f"{m} {n}  {p} {info_price(m, n)} {b} {s} "
                  f"{'exact' if b == s else 'miss'}")
    print()
    print("exact completion costs C(m,n) for small cells:")
    for (m, n) in [(2, 4), (3, 5), (2, 5), (4, 6), (3, 6), (5, 7), (4, 7)]:
        c, tree = min_completion(m, n)
        init = initial_state(m, n)
        worst = 0
        for perm in init:
            _, k = replay(tree, perm)
            worst = max(worst, k)
        assert worst == c, f"replay worst {worst} != claimed {c}"
        print(f"C({m},{n}) = {c}  (info price {info_price(m, n)}, "
              f"B={split_bound(m, n)}, S({n})={S_KNOWN[n]}, "
              f"replay over {len(init)} extensions OK)")


if __name__ == "__main__":
    sys.exit(main())
