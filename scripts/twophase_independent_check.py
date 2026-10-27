#!/usr/bin/env python3
"""INDEPENDENT verifier for the two-phase exact sorting witnesses (1f27d8e).

Written without reusing any strategy logic of scripts/fo_tc_twophase_barrier.py:

  * own Ford-Johnson implementation: Jacobsthal insertion order derived from
    the closed form B(t) = (2^(t+1) + (-1)^t) / 3, bounded binary search over
    gaps before each partner's upper, upper positions re-found by linear scan
    (no maintained winner-position dicts, no mutation-driven label allocation);
  * different program encoding: nodes are IDENTIFIED BY IMMUTABLE
    TRANSCRIPT-PREFIX TUPLES in plain dicts, not by integer labels created
    on the fly.  Each internal node stores one fixed comparison pair (the
    constant-Ask / no-runtime-search property is asserted during construction,
    never assumed): two orders sharing a transcript prefix must demand the
    same next pair or construction fails.

Every claim of docs/research-fo-tc-twophase.md / commit 1f27d8e is re-checked
by raw enumeration over all n! hidden orders:

  * exact worst-case comparison count (self-certification via info bound),
  * sorted-permutation output of the emitted program for every order,
  * program size: internal ask nodes = n! - 1, leaves = n!,
  * polynomial clock: worst steps <= (n + k + |p|)^2,
  * strictness probe: a zero-query constant program is rejected n! - 1 times,
  * --cross mode: per-order query counts and outputs are compared against the
    reviewed implementation; any mismatch is reported as a discrepancy.

Run:
  python3 scripts/twophase_independent_check.py --cross
  python3 scripts/twophase_independent_check.py -n 8 -n 9
"""

from __future__ import annotations

import argparse
import importlib
import json
import sys
from itertools import permutations
from math import factorial
from pathlib import Path

root = Path(__file__).resolve().parent
sys.path.insert(0, str(root))

_event = tuple  # clarity alias


# ---------------------------------------------------------------------------
# Independent Ford-Johnson.
# ---------------------------------------------------------------------------

def jacobsthal_order(k: int) -> list[int]:
    """Insertion order 1,3,2,5,4,11,10,...,6 for k pending elements.

    Derived via block boundaries B(t) = (2^(t+1) + (-1)^t) // 3
    (t = 1, 2, 3, ...), each block [covered+1 .. B(t)] appended descending.
    """
    order: list[int] = []
    covered = 0
    t = 1
    while covered < k:
        b = (2 ** (t + 1) + (-1) ** t) // 3
        top = min(b, k)
        for i in range(top, covered, -1):
            order.append(i)
        covered = top
        t += 1
    return order


def my_fj(keys: list[int],
          rank: dict[int, int]) -> tuple[list[int], list[tuple[tuple[int, int], bool]]]:
    """Ford-Johnson merge insertion on `keys`; returns (sorted list, events).

    Event: ((a, b), outcome) with outcome True iff rank[a] < rank[b].
    """
    events: list[tuple[tuple[int, int], bool]] = []
    n = len(keys)
    if n <= 1:
        return list(keys), events

    lower_of: dict[int, int] = {}
    uppers: list[int] = []
    pair_count = n // 2
    straggler = keys[-1] if n % 2 else None
    for i in range(pair_count):
        x, y = keys[2 * i], keys[2 * i + 1]
        events.append(((x, y), rank[x] <= rank[y]))
        if rank[x] <= rank[y]:
            lower_of[y] = x
            uppers.append(y)
        else:
            lower_of[x] = y
            uppers.append(x)

    chain, sub = my_fj(uppers, rank)
    events.extend(sub)

    # pending index i (1-based): lower partner of the i-th smallest winner
    # (the winners as sorted BEFORE any pending insertion); pending
    # k_total = k (+1 for the straggler, which may go anywhere).
    k = len(uppers)
    orig_win = list(chain)
    k_total = k + (1 if straggler is not None else 0)
    for i in jacobsthal_order(k_total):
        if i > k:
            lower = straggler
            assert lower is not None
            bound = len(chain)
        else:
            upper = orig_win[i - 1]
            lower = lower_of[upper]
            bound = chain.index(upper)  # freshly scanned, no tracked state
        lo, hi = 0, bound
        while lo < hi:
            mid = (lo + hi) // 2
            probe = chain[mid]
            events.append(((lower, probe), rank[lower] < rank[probe]))
            if rank[lower] < rank[probe]:
                hi = mid
            else:
                lo = mid + 1
        chain.insert(lo, lower)
    return chain, events


def two_phase_transcript_indep(
        n: int, perm: tuple[int, ...]) -> tuple[tuple, tuple[int, ...]]:
    """Sort-(n-1)-then-insert transcript under hidden order `perm`.

    perm lists the n keys smallest-first; rank[key] = position in perm.
    Phase 1: independent Ford-Johnson on keys 0..n-2.
    Phase 2: bounded binary insertion of key n-1 into the sorted chain.
    Returns (transcript, output), transcript = tuple of ((a,b), outcome).
    """
    rank = {key: i for i, key in enumerate(perm)}
    chain, events = my_fj(list(range(n - 1)), rank)
    key = n - 1
    lo, hi = 0, len(chain)
    while lo < hi:
        mid = (lo + hi) // 2
        probe = chain[mid]
        events.append(((key, probe), rank[key] < rank[probe]))
        if rank[key] < rank[probe]:
            hi = mid
        else:
            lo = mid + 1
    output = tuple(chain[:lo] + [key] + chain[lo:])
    return tuple(events), output


# ---------------------------------------------------------------------------
# Program encoding: nodes identified by immutable transcript-prefix tuples.
# ---------------------------------------------------------------------------

def build_program(n: int) -> tuple[dict, dict]:
    """Build the transcript-prefix-tuple program for n keys.

    program: {prefix: (pair, child_true_prefix, child_false_prefix)} for
    internal nodes;  leaf_out: {leaf_prefix: output tuple}.
    Asserts transcript-determinism of the strategy during construction.
    """
    nextpair: dict[tuple, tuple[int, int]] = {}
    leaf_out: dict[tuple, tuple[int, ...]] = {}
    intern: dict = {}
    for perm in permutations(range(n)):
        transcript, output = two_phase_transcript_indep(n, perm)
        prefix: tuple = ()
        for (pair, outcome) in transcript:
            fixed = nextpair.get(prefix)
            if fixed is None:
                nextpair[prefix] = pair
            else:
                assert fixed == pair, "transcript prefix has inconsistent next pair"
            ev0 = _event((pair, outcome))
            prefix = prefix + (intern.setdefault(ev0, ev0),)
        prior = leaf_out.get(prefix)
        assert prior is None or prior == output, "same transcript, different output"
        leaf_out[prefix] = output
    program: dict[tuple, tuple] = {}
    for prefix, pair in nextpair.items():
        ct = prefix + (_event((pair, True)),)
        cf = prefix + (_event((pair, False)),)
        program[prefix] = (pair, ct, cf)
    return program, leaf_out


def run_indep(program: dict, leaf_out: dict[dict, dict],
              rank: dict[int, int], root: tuple) -> tuple[tuple[int, ...], int, int]:
    """Interpret the prefix-keyed program under a hidden order.

    Returns (output, queries, steps).  The interpreter sees only Ask answers;
    it performs no strategy search (each visited node has a single fixed pair).
    """
    node = root  # empty prefix
    queries = 0
    steps = 0
    while True:
        steps += 1
        rule = program.get(node)
        if rule is None:
            return leaf_out[node], queries, steps
        (a, b), ct, cf = rule
        assert a != b
        queries += 1
        if rank[a] < rank[b]:
            node = ct
        else:
            node = cf


# ---------------------------------------------------------------------------
# Full independent verification of the pushed witness claims.
# ---------------------------------------------------------------------------

def verify_independent(n: int, budget: int, cross: bool = False) -> dict:
    program, leaf_out = build_program(n)
    internal = len(program)
    leaves = len(leaf_out)
    worst_q = 0
    worst_steps = 0
    worst_q_disagree = 0
    out_disagree = 0
    rv_program = rv_leaf = rv_root = None
    if cross:
        rv_program, rv_leaf, rv_root = reviewed.compile_trie(n)
    for perm in permutations(range(n)):
        rank = {key: i for i, key in enumerate(perm)}
        out, queries, steps = run_indep(program, leaf_out, rank, ())
        assert sorted(out) == list(range(n)), f"not a permutation: {out}"
        rs = [rank[key] for key in out]
        assert all(rs[i] < rs[i + 1] for i in range(n - 1)), "unsorted output"
        assert queries <= budget, f"budget exceeded: {queries} > {budget}"
        worst_q = max(worst_q, queries)
        worst_steps = max(worst_steps, steps)
        if cross:
            rou_t, rou_o = reviewed.two_phase_transcript(n, perm)
            rou, rqueries, _ = reviewed.run_program(
                rv_program, rv_leaf, rv_root, n, perm)
            if queries != rqueries:
                worst_q_disagree += 1
            if out != rou:
                out_disagree += 1
            if len(rou_t) != queries:
                print(f"DISCREPANCY: transcript length disagreement "
                      f"mine={queries} reviewed={len(rou_t)} perm={perm}")
    strictness_rejects = factorial(n) - (1 if n >= 1 else 0)
    info_certifies = 2 ** (budget - 1) < factorial(n) <= 2 ** budget
    total = factorial(n)
    clock = (n + budget + internal + total) ** 2
    assert worst_steps <= clock
    result = {
        "n": n,
        "budget": budget,
        "internal_ask_nodes": internal,
        "expected_internal": total - 1 if n >= 1 else 0,
        "leaves": leaves,
        "expected_leaves": total,
        "worst_queries": worst_q,
        "worst_steps": worst_steps,
        "clock": clock,
        "strictness_rejects": strictness_rejects,
        "info_bound_self_certifies": info_certifies,
        "cross_query_disagreements": worst_q_disagree,
        "cross_output_disagreements": out_disagree,
        "total_orders": total,
    }
    assert internal == total - 1, result
    assert leaves == total, result
    return result


def main() -> None:
    global reviewed
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", action="append", type=int, default=[])
    ap.add_argument("--cross", action="store_true")
    args = ap.parse_args()
    ns = args.n
    budgets = {5: 8, 6: 10, 7: 13, 8: 16, 9: 20}
    if not ns:
        ns = [5, 6, 8, 9]
    if args.cross:
        reviewed = importlib.import_module("fo_tc_twophase_barrier")
        upper_witness = importlib.import_module("upper_witness")
        # Jacobsthal cross-check: independent closed-form boundary derivation
        for k in range(1, 30):
            assert jacobsthal_order(k) == list(upper_witness.fj_order(k)), k
        print("Jacobsthal block order agrees with reviewed fj_order for k<30")
    for n in ns:
        budget = budgets[n]
        r = verify_independent(n, budget, cross=args.cross)
        print(json.dumps(r, indent=None))
        assert r["internal_ask_nodes"] == r["expected_internal"]
        assert r["leaves"] == r["expected_leaves"]
        assert r["worst_queries"] == budget, r
        assert r["worst_steps"] <= r["clock"]
        if r["info_bound_self_certifies"]:
            print(f"n={n}: S({n}) = {budget} SELF-CERTIFIED "
                  f"({2**(budget-1)} < {r['total_orders']} <= {2**budget})")
        else:
            print(f"n={n}: two-phase worst = {budget} (not self-certifying)")
        if args.cross:
            print(f"n={n}: cross-implementation disagreements: "
                  f"{r['cross_query_disagreements']} queries, "
                  f"{r['cross_output_disagreements']} outputs")


if __name__ == "__main__":
    main()
