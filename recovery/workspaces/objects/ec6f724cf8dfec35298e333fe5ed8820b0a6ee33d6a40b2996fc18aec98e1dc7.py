#!/usr/bin/env python3
"""Certified upper-bound witnesses for poset sorting F(P).

Research question (docs/research-upper-witnesses.md): can an explicit
deterministic comparison strategy with a *certified height* U(P) provide a
fast acceptance prune in the budgeted minimax DFS?

Model (docs/problem.md, docs/upper-bound.md, docs/research-budgeted-dfs.md):
  * n distinct labelled keys; a state is the transitively closed poset P
    induced by the comparisons made so far (successor bitmasks: bit j of
    succ[i] iff i < j).
  * S(n) = minimum worst-case number of adaptive pairwise comparisons to sort.
  * Game G(n,k): sorter picks an incomparable pair, adversary answers, P
    becomes its transitive closure. S(n) <= k iff the sorter wins G(n,k).
  * CanSort(P, d) = the sorter can force a total order from P within d
    comparisons; CanSort(P, d) = True iff F(P) <= d.

This script provides *upper* witnesses (explicit strategies with certified
heights), the dual of the lower-bound prunes of
scripts/budgeted_pruning_experiments.py:

  1. Ford-Johnson merge-insertion: an explicit poly-time strategy for total
     orders with certified worst-case height M(n) = sum_{i=1}^n
     ceil(log2(3i/4)); exact (M(n) = S(n)) for n <= 11 (Knuth; Peczarski).
     Since F(P) <= S(n) <= M(n) for every n-element poset, M(n) is a valid
     certified upper bound on F(P) for all n.
  2. Binary insertion under partial information (BIPI): a poly-time certified
     upper bound U_BIPI(P) = sum_k min(m_k, ceil(log2(k+1))) for general
     posets, where m_k counts the chain elements incomparable to the k-th
     inserted element (determined by P alone, hence poly-time).

It then applies the sound acceptance prune
    CanSort(P, d) = True   whenever   U(P) <= d
to the reference DFS and measures call savings.  No asymptotic claim is made.

This is an experiment, not a proof.  It uses no external libraries.
"""

from __future__ import annotations

import argparse
import math
import random
import sys
import time
from functools import lru_cache
from itertools import permutations

sys.setrecursionlimit(100000)

# ---------------------------------------------------------------------------
# Poset machinery (successor bitmasks; same representation as evaluate.py).
# ---------------------------------------------------------------------------


def extend(succ, i, j):
    """Transitive closure after adding i < j to an already closed poset."""
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(len(succ)):
        if x == i or (succ[x] & (1 << i)):
            out[x] |= new_greater
    return tuple(out)


def incomparable_pairs(succ, n):
    return [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if not (succ[i] & (1 << j)) and not (succ[j] & (1 << i))
    ]


def is_total(succ, n):
    return all(
        (succ[i] >> j) & 1 or (succ[j] >> i) & 1
        for i in range(n)
        for j in range(i + 1, n)
    )


def antichain(n):
    return (0,) * n


def total_order(n):
    return tuple(sum(1 << j for j in range(i + 1, n)) for i in range(n))


def crown(n):
    """Crown poset on n elements (n even): a_i < b_i, a_i < b_{i-1}."""
    if n % 2 != 0:
        raise ValueError("crown needs even n")
    half = n // 2
    succ = [0] * n
    for i in range(half):
        a, b = i, half + i
        succ[a] |= 1 << b
        succ[a] |= 1 << half + (i - 1) % half
    return tuple(succ)


def disjoint_chains(n, k):
    """Disjoint union of k chains as evenly sized as possible."""
    succ = [0] * n
    sizes = [n // k + (1 if i < n % k else 0) for i in range(k)]
    idx = 0
    for s in sizes:
        for a in range(idx, idx + s):
            for b in range(a + 1, idx + s):
                succ[a] |= 1 << b
        idx += s
    return tuple(succ)


def random_poset(n, p, rng):
    """Random DAG-based poset: orient i<j with prob p, take transitive closure."""
    succ = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < p:
                succ[i] |= 1 << j
    for k in range(n):
        for i in range(n):
            if succ[i] >> k & 1:
                succ[i] |= succ[k]
    return tuple(succ)


def ceil_log2(x):
    """Exact integer ceil(log2(x)) for x >= 1, no floating point."""
    if x <= 1:
        return 0
    return (x - 1).bit_length()


def ceil_log2_frac(a, b):
    """Exact integer ceil(log2(a/b)) for positive ints a, b."""
    k = 0
    while (1 << k) * b < a:
        k += 1
    return k


# ---------------------------------------------------------------------------
# Linear extensions and the leaf (information) bound.
# ---------------------------------------------------------------------------


def linear_extensions(succ, n):
    """Exact e(P) by the minimal-element order-ideal DP (O(2^n) space)."""

    @lru_cache(maxsize=None)
    def count(remaining):
        if not remaining:
            return 1
        rem = tuple(remaining)
        return sum(
            count(tuple(y for y in rem if y != x))
            for x in rem
            if not any(succ[y] & (1 << x) for y in rem if y != x)
        )

    return count(tuple(range(n)))


def leaf_bound(succ, n):
    """ceil(log2 e(P)): a certified lower bound on F(P)."""
    return ceil_log2(linear_extensions(succ, n))


# ---------------------------------------------------------------------------
# Exact minimax oracle F(P) (from scripts/evaluate.py), memoized over all
# reachable posets.
# ---------------------------------------------------------------------------


def memoized_F(n):
    states = {}

    def solve(succ):
        if succ in states:
            return states[succ]
        pairs = incomparable_pairs(succ, n)
        if not pairs:
            states[succ] = 0
            return 0
        best = 1 + min(
            max(solve(extend(succ, i, j)), solve(extend(succ, j, i)))
            for i, j in pairs
        )
        states[succ] = best
        return best

    solve((0,) * n)
    return states


# ---------------------------------------------------------------------------
# 1. Ford-Johnson merge-insertion: an explicit poly-time certified witness for
#    total orders.  M(n) = sum_{i=1}^n ceil(log2(3i/4)).
# ---------------------------------------------------------------------------


def fj_order(K):
    """Insertion order over indices 1..K: Jacobsthal-driven, descending in
    groups [J_{2g-1} .. J_{2g-2}+1].  For K<=12: 1,3,2,5,4,11..6,12."""
    J = [0, 1]
    while J[-1] < K:
        J.append(J[-1] + 2 * J[-2])
    order = []
    pairs = [(J[1], J[0] + 1)]
    for k in range(3, len(J)):
        pairs.append((J[k], J[k - 1] + 1))
    for hi, lo in pairs:
        for idx in range(hi, lo - 1, -1):
            if idx <= K:
                order.append(idx)
        if hi >= K:
            break
    return order


def fj_sort(items, counter):
    """Ford-Johnson merge-insertion.  Returns the sorted list; increments
    counter[0] by the exact number of comparisons performed."""
    n = len(items)
    if n <= 1:
        return list(items)
    pairs = []
    for i in range(0, n - 1, 2):
        counter[0] += 1
        if items[i] <= items[i + 1]:
            pairs.append((items[i], items[i + 1]))  # (loser, winner)
        else:
            pairs.append((items[i + 1], items[i]))
    straggler = items[-1] if n % 2 == 1 else None
    winners = [w for (_, w) in pairs]
    losers = [l for (l, _) in pairs]
    sorted_winners = fj_sort(winners, counter)
    k = len(winners)
    pos_in_sorted = {w: i for i, w in enumerate(sorted_winners)}
    pending = {}
    for i in range(k):
        pending[pos_in_sorted[winners[i]] + 1] = (losers[i], winners[i])
    K = k
    if straggler is not None:
        K = k + 1
        pending[K] = (straggler, None)
    chain = list(sorted_winners)
    winner_pos = {w: i for i, w in enumerate(chain)}
    for idx in fj_order(K):
        loser, winner = pending[idx]
        bound = len(chain) if winner is None else winner_pos[winner]
        lo, hi = 0, bound
        while lo < hi:
            mid = (lo + hi) // 2
            counter[0] += 1
            if loser < chain[mid]:
                hi = mid
            else:
                lo = mid + 1
        chain.insert(lo, loser)
        for w, p in list(winner_pos.items()):
            if p >= lo:
                winner_pos[w] = p + 1
    return chain


def fj_upper_bound(n):
    """M(n) = sum_{i=1}^n ceil(log2(3i/4)); certified worst-case height."""
    if n <= 1:
        return 0
    return sum(ceil_log2_frac(3 * i, 4) for i in range(1, n + 1))


def fj_worst_case_height(n, samples=20000, seed=20261018):
    """Certified worst-case height of the explicit FJ strategy: exhaustive for
    n <= 6, otherwise a deterministic random sample.  Returns (height, exact).
    """
    if n <= 6:
        worst = 0
        for perm in permutations(range(n)):
            c = [0]
            out = fj_sort(list(perm), c)
            if out != list(range(n)):
                raise AssertionError(f"FJ did not sort {perm}")
            worst = max(worst, c[0])
        return worst, True
    rng = random.Random(seed)
    worst = 0
    for _ in range(samples):
        perm = list(range(n))
        rng.shuffle(perm)
        c = [0]
        out = fj_sort(perm, c)
        if out != list(range(n)):
            raise AssertionError(f"FJ did not sort {perm}")
        worst = max(worst, c[0])
    return worst, False


# ---------------------------------------------------------------------------
# 2. Binary insertion under partial information (BIPI): a poly-time certified
#    upper bound for general posets.
# ---------------------------------------------------------------------------


def lex_linear_extension(succ, n):
    """Lexicographically smallest linear extension of P."""
    remaining = set(range(n))
    order = []
    while remaining:
        mins = [
            x
            for x in remaining
            if not any(succ[y] & (1 << x) for y in remaining if y != x)
        ]
        x = min(mins)
        order.append(x)
        remaining.remove(x)
    return order


def bipi_incomparable_counts(succ, n, order=None):
    """m_k = number of elements among order[0..k-1] incomparable to order[k].

    Determined by P and the insertion order alone (not by the actual chain
    order), hence poly-time computable."""
    if order is None:
        order = lex_linear_extension(succ, n)
    counts = []
    for k in range(1, n):
        x = order[k]
        m = sum(
            1
            for j in range(k)
            if not (succ[order[j]] & (1 << x)) and not (succ[x] & (1 << order[j]))
        )
        counts.append(m)
    return counts


def bipi_upper_bound(succ, n, order=None):
    """U_BIPI(P) = sum_k min(m_k, ceil(log2(k+1))); a certified upper bound on
    F(P).

    [deduction] Inserting order[k] into the sorted chain of the first k elements
    needs at most min(m_k, ceil(log2(k+1))) comparisons: at most m_k because a
    comparison is only needed against an incomparable chain element (a comparable
    one is skipped using the known relation), and at most ceil(log2(k+1)) because
    binary search over k elements has that height.  The bound is poly-time and
    adapts to P (m_k depends on P)."""
    counts = bipi_incomparable_counts(succ, n, order)
    return sum(min(m, ceil_log2(k + 1)) for k, m in enumerate(counts, start=1))


def bipi_strategy_height(succ, n, order=None, cap=None):
    """Exact worst-case height of the BIPI strategy, by simulating the binary
    insertion (skipping comparable midpoints) on every linear extension of P.
    Returns (height, sorted_ok).  Exponential in e(P); small n."""
    if order is None:
        order = lex_linear_extension(succ, n)
    extensions = []

    def enum(remaining, built):
        if not remaining:
            extensions.append(tuple(built))
            return
        rem = tuple(remaining)
        for x in rem:
            if not any(succ[y] & (1 << x) for y in rem if y != x):
                enum(tuple(y for y in rem if y != x), built + [x])

    enum(tuple(range(n)), [])
    if cap is not None and len(extensions) > cap:
        raise ValueError("too many linear extensions for exact BIPI height")
    worst = 0
    sorted_ok = True
    for ext in extensions:
        chain = []
        cmps = 0
        for x in order:
            lo, hi = 0, len(chain)
            while lo < hi:
                mid = (lo + hi) // 2
                y = chain[mid]
                if succ[x] & (1 << y):
                    hi = mid  # x < y known: no comparison needed
                elif succ[y] & (1 << x):
                    lo = mid + 1  # y < x known: no comparison needed
                else:
                    cmps += 1  # genuinely incomparable: one comparison
                    if ext.index(x) < ext.index(y):
                        hi = mid
                    else:
                        lo = mid + 1
            chain.insert(lo, x)
        if chain != list(ext):
            sorted_ok = False
        worst = max(worst, cmps)
    return worst, sorted_ok


# ---------------------------------------------------------------------------
# 3. Greedy leaf-count policy: a heuristic with an exact certified height
#    (not poly-time: needs e(child) for every candidate pair).
# ---------------------------------------------------------------------------


def greedy_policy_height(succ, n, node_cap=None):
    """Exact certified height of the greedy policy that compares, at each state,
    the incomparable pair minimizing max(e(child1), e(child2)).  Computed by a
    memoized policy-tree DFS.  Returns (height, capped)."""
    e = lambda P: linear_extensions(P, n)  # noqa: E731
    memo = {}
    calls = [0]
    capped = [False]

    def h(P):
        if P in memo:
            return memo[P]
        calls[0] += 1
        if node_cap is not None and calls[0] > node_cap:
            capped[0] = True
            return 0
        if is_total(P, n):
            memo[P] = 0
            return 0
        pairs = incomparable_pairs(P, n)
        best = None
        for i, j in pairs:
            a = extend(P, i, j)
            b = extend(P, j, i)
            score = max(e(a), e(b))
            if best is None or score < best[0]:
                best = (score, a, b)
        _, a, b = best
        val = 1 + max(h(a), h(b))
        memo[P] = val
        return val

    height = h(succ)
    return height, capped[0]


# ---------------------------------------------------------------------------
# 4. Acceptance prune.
# ---------------------------------------------------------------------------


def can_sort_reference(succ, n, d, counter, node_cap=None):
    """Verbatim reference budgeted DFS from scripts/budgeted_dfs.py."""
    counter[0] += 1
    if node_cap is not None and counter[0] > node_cap:
        return None
    if is_total(succ, n):
        return True
    if d == 0:
        return False
    for i, j in incomparable_pairs(succ, n):
        if can_sort_reference(extend(succ, i, j), n, d - 1, counter, node_cap):
            if can_sort_reference(extend(succ, j, i), n, d - 1, counter, node_cap):
                return True
    return False


def combined_witness(succ, n, order=None):
    """A valid certified upper bound on F(succ): min(M(n), U_BIPI(succ)).
    M(n) is valid for every n-element poset because F(P) <= S(n) <= M(n)."""
    return min(fj_upper_bound(n), bipi_upper_bound(succ, n, order))


def can_sort_with_witness(succ, n, d, counter, witness, node_cap=None):
    """Sound acceptance prune: if witness(succ) <= d, accept immediately;
    otherwise fall back to the reference DFS.  The witness is a certified upper
    bound on F(succ)."""
    counter[0] += 1
    if node_cap is not None and counter[0] > node_cap:
        return None
    if is_total(succ, n):
        return True
    if d == 0:
        return False
    if witness(succ) <= d:
        return True
    for i, j in incomparable_pairs(succ, n):
        if can_sort_with_witness(extend(succ, i, j), n, d - 1, counter, witness, node_cap):
            if can_sort_with_witness(extend(succ, j, i), n, d - 1, counter, witness, node_cap):
                return True
    return False


# ---------------------------------------------------------------------------
# Exhaustive verification against exact F.
# ---------------------------------------------------------------------------


def verify_all(max_n=5, verbose=False):
    """Exhaustively check, for every labelled poset P with n <= max_n:
      (a) leaf_bound(P) <= F(P) <= U_BIPI(P) and F(P) <= M(n), hence the
          combined witness min(M(n), U_BIPI(P)) is a certified upper bound;
      (b) the BIPI strategy sorts correctly and its exact height <= U_BIPI(P)
          (n <= 5, where the simulation is feasible);
      (c) the greedy policy height is a certified upper bound (height >= F(P)).
    Returns (failures, checks)."""
    failures = []
    checks = 0
    for n in range(1, max_n + 1):
        F = memoized_F(n)
        for P in sorted(F.keys()):
            fp = F[P]
            lb = leaf_bound(P, n)
            ub = bipi_upper_bound(P, n)
            mn = fj_upper_bound(n)
            cw = min(mn, ub)
            checks += 1
            if not (lb <= fp and fp <= ub and fp <= mn and fp <= cw):
                failures.append((n, P, "bound", lb, fp, ub, mn, cw))
            if n <= 5:
                h, sorted_ok = bipi_strategy_height(P, n)
                checks += 1
                if (not sorted_ok) or h > ub:
                    failures.append((n, P, "strategy", h, ub, sorted_ok))
                gh, capped = greedy_policy_height(P, n)
                checks += 1
                if (not capped) and gh < fp:
                    failures.append((n, P, "greedy", gh, fp, capped))
            if verbose and (n <= 4 or len(failures) == 0):
                print(f"  n={n} P={P} F={fp} leaf={lb} U_BIPI={ub} "
                      f"M={mn} combined={cw}")
    return failures, checks


# A state called out in review: (0,0,0,0,5) has F=6, U_BIPI=8, strategy height 7.
REPORTED_STATE = (0, 0, 0, 0, 5)


def reported_state_check():
    """Return the certified values for the review-flagged state (0,0,0,0,5)."""
    n = 5
    P = REPORTED_STATE
    F = memoized_F(n)
    fp = F[P]
    ub = bipi_upper_bound(P, n)
    h, sorted_ok = bipi_strategy_height(P, n)
    mn = fj_upper_bound(n)
    return {
        "n": n,
        "P": P,
        "F": fp,
        "leaf": leaf_bound(P, n),
        "U_BIPI": ub,
        "strategy_height": h,
        "sorted_ok": sorted_ok,
        "M": mn,
        "combined": min(mn, ub),
    }


# ---------------------------------------------------------------------------
# Report / CLI.
# ---------------------------------------------------------------------------


def structured_posets(n):
    out = {
        "antichain": antichain(n),
        "total": total_order(n),
        "2-chains": disjoint_chains(n, 2),
        "crown": crown(n) if n % 2 == 0 else None,
    }
    return {k: v for k, v in out.items() if v is not None}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-n", type=int, default=6)
    ap.add_argument("--node-cap", type=int, default=20_000_000)
    ap.add_argument("--skip-heavy", action="store_true")
    ap.add_argument("--verify", action="store_true",
                    help="exhaustive cross-check against exact F for n<=max-n")
    args = ap.parse_args()

    if args.verify:
        failures, checks = verify_all(args.max_n, verbose=(args.max_n <= 4))
        print(f"verify_all(n<={args.max_n}): {checks} checks, "
              f"{len(failures)} failures")
        for f in failures[:10]:
            print("  FAILURE", f)
        return 0 if not failures else 1

    ok = True

    # Table 1: Ford-Johnson exact witness for total orders.
    known_S = {1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16,
               9: 19, 10: 22, 11: 26, 12: 30}
    print("=== Table 1: Ford-Johnson exact upper witness for total orders ===")
    print("n | M(n) | simulated worst | leaf bound ceil(log2 n!) | S(n) | M=S?")
    for n in range(1, min(args.max_n, 6) + 1):
        h, exact = fj_worst_case_height(n)
        M = fj_upper_bound(n)
        lb = ceil_log2(math.factorial(n))
        match = (M == known_S[n])
        ok = ok and match and exact
        print(f"{n} | {M} | {h} ({'exact' if exact else 'sampled'}) | {lb} | "
              f"{known_S[n]} | {'yes' if match else 'NO'}")
    print()

    # Table 2: certified upper bounds vs exact minimax and leaf bound.
    print("=== Table 2: certified upper bounds vs minimax and leaf bound ===")
    print("n | poset | T=e(P) | leaf | F(P) | U_BIPI | greedy (n<=5)")
    for n in range(2, args.max_n + 1):
        F = memoized_F(n)
        for name, P in structured_posets(n).items():
            T = linear_extensions(P, n)
            lb = ceil_log2(T)
            fp = F[P]
            ub = bipi_upper_bound(P, n)
            greedy = ""
            if n <= 5 and not args.skip_heavy:
                gh, capped = greedy_policy_height(P, n)
                greedy = f"{gh}{'?' if capped else ''}"
                ok = ok and (gh >= fp)
            ok = ok and (ub >= fp) and (lb <= fp)
            print(f"{n} | {name} | {T} | {lb} | {fp} | {ub} | {greedy}")
    print()

    # Table 3: acceptance prune call savings (empty poset).
    print("=== Table 3: acceptance-prune call savings (empty poset) ===")
    print("n | d | reference calls | witness calls | decision")
    for n in range(2, args.max_n + 1):
        def witness(P, n=n):
            return combined_witness(P, n)

        for d in range(0, min(2 * n, 12)):
            c1 = [0]
            r1 = can_sort_reference(antichain(n), n, d, c1, args.node_cap)
            c2 = [0]
            r2 = can_sort_with_witness(antichain(n), n, d, c2, witness, args.node_cap)
            ok = ok and (r1 == r2)
            print(f"{n} | {d} | {c1[0]} | {c2[0]} | {r1}")
    print()

    print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
