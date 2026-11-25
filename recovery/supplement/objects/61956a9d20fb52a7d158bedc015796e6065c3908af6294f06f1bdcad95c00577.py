#!/usr/bin/env python3
"""Optimal-first-move structure and the one-round difference lemma for S(n).

Model (docs/problem.md, docs/upper-bound.md, SoringP1/Minimax.lean):
  A state is a strict partial order (transitive closure) on [n], stored as
  successor bitmasks.  F(P) = 0 if P is total, else
      F(P) = 1 + min_{x||y} max(F(P+x<y), F(P+y<x)).
  S(n) = F(empty antichain).

This probe investigates the *one-round difference* structure
      Q(P,q) = 1 + max(F(P+q+), F(P+q-)),   F(P) <= Q(P,q) <= F(P)+1,
and asks whether restricting an exact evaluator to optimal moves (Q = F)
is a genuine uniform speedup.

Experiments:
  A. Root characterization: for A_n, count optimal first moves and orbits.
  B. Deeper levels: number of optimal moves per state reachable in optimal
     play, and the optimal-move branching factor.
  C. Branch-and-bound exact DP: prune a move q before recursing when a
     one-round lower bound on Q(P,q) exceeds the current best.  Compare
     child-evaluation counts and time with the reference memoized DP.
  D. Root triviality: the branch-and-bound prunes zero root moves.

This is an experiment, not a proof.  It uses no external libraries.
"""

import argparse
import itertools
import time
from functools import lru_cache

from state_compression import (
    extend,
    incomparable_pairs,
    make_refined_canon,
)


def is_total(succ, n):
    return all(
        (succ[i] >> j & 1) or (succ[j] >> i & 1)
        for i in range(n) for j in range(i + 1, n)
    )


# --------------------------------------------------------------------------
# A. Root characterization.
# --------------------------------------------------------------------------

def labelled_F(n):
    """Exact minimax values for every labelled poset reachable from A_n."""
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


def quotient_F(n):
    """Exact minimax values on the S_n-quotient (isomorphism classes)."""
    canon = make_refined_canon(n)
    states = {}

    def solve(c):
        if c in states:
            return states[c]
        pairs = incomparable_pairs(c, n)
        if not pairs:
            states[c] = 0
            return 0
        best = None
        for i, j in pairs:
            v = 1 + max(solve(canon(extend(c, i, j))),
                        solve(canon(extend(c, j, i))))
            if best is None or v < best:
                best = v
        states[c] = best
        return best

    solve(canon((0,) * n))
    return states, canon


def root_analysis_labelled(n, states):
    """For A_n: count optimal first moves and verify the one-round lemma."""
    root = (0,) * n
    F = states[root]
    pairs = incomparable_pairs(root, n)
    Qs = [1 + max(states[extend(root, i, j)], states[extend(root, j, i)])
          for i, j in pairs]
    optimal = sum(1 for q in Qs if q == F)
    # All pairs form one S_n-orbit; verify Q is constant (the orbit invariant).
    distinct_Q = sorted(set(Qs))
    return dict(n=n, S=F, pairs=len(pairs), optimal=optimal,
                orbits=1, distinct_Q=distinct_Q,
                lemma_ok=all(F <= q <= F + 1 for q in Qs))


def root_analysis_quotient(n, states, canon):
    """Root analysis on the quotient: one child class, one orbit."""
    root = canon((0,) * n)
    F = states[root]
    i, j = incomparable_pairs(root, n)[0]
    a = canon(extend(root, i, j))
    b = canon(extend(root, j, i))
    Q = 1 + max(states[a], states[b])
    return dict(n=n, S=F, pairs=n * (n - 1) // 2, optimal=n * (n - 1) // 2,
                orbits=1, distinct_Q=[Q],
                lemma_ok=(F <= Q <= F + 1), child=F - 1)


# --------------------------------------------------------------------------
# B. Deeper-level optimal-move statistics.
# --------------------------------------------------------------------------

def deeper_stats_labelled(n, states):
    """Over all states reachable in optimal play, count optimal moves.

    Returns (states_visited, total_pairs, total_optimal, max_optimal,
             distribution_of_optimal_counts).
    """
    seen = set()
    total_pairs = 0
    total_optimal = 0
    max_optimal = 0
    dist = {}

    def walk(succ):
        if succ in seen:
            return
        seen.add(succ)
        if is_total(succ, n):
            return
        F = states[succ]
        pairs = incomparable_pairs(succ, n)
        opt = 0
        for i, j in pairs:
            q = 1 + max(states[extend(succ, i, j)], states[extend(succ, j, i)])
            if q == F:
                opt += 1
        nonlocal total_pairs, total_optimal, max_optimal
        total_pairs += len(pairs)
        total_optimal += opt
        if opt > max_optimal:
            max_optimal = opt
        dist[opt] = dist.get(opt, 0) + 1
        for i, j in pairs:
            q = 1 + max(states[extend(succ, i, j)], states[extend(succ, j, i)])
            if q == F:
                walk(extend(succ, i, j))
                walk(extend(succ, j, i))

    walk((0,) * n)
    return len(seen), total_pairs, total_optimal, max_optimal, dist


# --------------------------------------------------------------------------
# C. Branch-and-bound exact DP with a one-round lower bound.
# --------------------------------------------------------------------------

_E_CACHE = {}


def linear_extensions(succ, n):
    """Exact e(P) by the minimal-element order-ideal DP (O(2^n) space).

    Module-level cache: identical child posets recur across the DP, and e is
    a pure function of the labelled poset, so sharing is exact.
    """
    key = (succ, n)
    hit = _E_CACHE.get(key)
    if hit is not None:
        return hit

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

    val = count(tuple(range(n)))
    _E_CACHE[key] = val
    return val


def ceil_log2(m):
    if m <= 1:
        return 0
    return (m - 1).bit_length()


def L0(succ, n):
    """Information lower bound ceil(log2 e(P))."""
    return ceil_log2(linear_extensions(succ, n))


def reference_DP(n):
    """Reference memoized DP.  Returns (F_root, states, evaluations, seconds)."""
    states = {}
    evals = [0]

    def solve(succ):
        if succ in states:
            return states[succ]
        pairs = incomparable_pairs(succ, n)
        if not pairs:
            states[succ] = 0
            return 0
        evals[0] += len(pairs)
        best = 1 + min(
            max(solve(extend(succ, i, j)), solve(extend(succ, j, i)))
            for i, j in pairs
        )
        states[succ] = best
        return best

    t0 = time.perf_counter()
    val = solve((0,) * n)
    dt = time.perf_counter() - t0
    return val, len(states), evals[0], dt


def width(succ, n):
    """Size of a maximum antichain by exhaustive subset scan (2^n time)."""
    best = 0
    for mask in range(1, 1 << n):
        els = [i for i in range(n) if mask >> i & 1]
        if len(els) <= best:
            continue
        ok = True
        for a in els:
            for b in els:
                if a != b and ((succ[a] >> b & 1) or (succ[b] >> a & 1)):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            best = len(els)
    return best


def LB(succ, n, mode):
    """A sound lower bound on F(P)."""
    if mode == "info":
        return L0(succ, n)
    if mode == "width":
        return ceil_log2(_fact(width(succ, n)))
    raise ValueError(mode)


def _fact(m):
    r = 1
    for k in range(2, m + 1):
        r *= k
    return r


def bb_DP(n, lb_mode="info"):
    """Branch-and-bound exact DP.

    For each move q, a one-round lower bound lb(q) = 1 + max(LB(child+),
    LB(child-)) is computed; if lb(q) >= current best the move is skipped.
    Sound: LB <= F <= Q, so lb(q) <= Q(P,q); skipping when lb(q) >= best
    cannot remove the minimum.  lb_mode selects the lower bound:
    'info' = ceil(log2 e) (exact, O(2^n) space); 'width' = ceil(log2 width!).
    """
    states = {}
    evals = [0]          # full child-evaluations (solve calls)
    lb_calls = [0]       # lower-bound computations
    pruned = [0]         # moves skipped by the bound

    def solve(succ):
        if succ in states:
            return states[succ]
        pairs = incomparable_pairs(succ, n)
        if not pairs:
            states[succ] = 0
            return 0
        best = None
        for i, j in pairs:
            a = extend(succ, i, j)
            b = extend(succ, j, i)
            lb_calls[0] += 2
            lb = 1 + max(LB(a, n, lb_mode), LB(b, n, lb_mode))
            if best is not None and lb >= best:
                pruned[0] += 1
                continue
            evals[0] += 2
            v = 1 + max(solve(a), solve(b))
            if best is None or v < best:
                best = v
        states[succ] = best
        return best

    t0 = time.perf_counter()
    val = solve((0,) * n)
    dt = time.perf_counter() - t0
    return val, len(states), evals[0], lb_calls[0], pruned[0], dt


# --------------------------------------------------------------------------
# Driver.
# --------------------------------------------------------------------------

KNOWN = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 9: 19, 12: 30}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root-max-n", type=int, default=8)
    ap.add_argument("--deeper-max-n", type=int, default=6)
    ap.add_argument("--bb-max-n", type=int, default=5)
    ap.add_argument("--bb", action="store_true")
    ap.add_argument("--deeper", action="store_true")
    args = ap.parse_args()

    print("=" * 78)
    print("A. ROOT CHARACTERIZATION: optimal first moves of the antichain A_n")
    print("=" * 78)
    print("n | S(n) | pairs C(n,2) | optimal | orbits | distinct Q | lemma")
    for n in range(2, args.root_max_n + 1):
        if n <= 6:
            states = labelled_F(n)
            r = root_analysis_labelled(n, states)
        else:
            states, canon = quotient_F(n)
            r = root_analysis_quotient(n, states, canon)
        print(f"{n} | {r['S']} | {r['pairs']} | {r['optimal']} | "
              f"{r['orbits']} | {r['distinct_Q']} | {r['lemma_ok']}")
    print("Interpretation: at A_n every first move is optimal (one S_n-orbit),")
    print("so restricting the first move to optimal moves prunes nothing.")

    if args.deeper:
        print()
        print("=" * 78)
        print("B. DEEPER LEVELS: optimal moves over states reachable in optimal play")
        print("=" * 78)
        print("n | states | total pairs | total optimal | max optimal | "
              "avg optimal/pairs")
        for n in range(2, args.deeper_max_n + 1):
            states = labelled_F(n)
            s, tp, to, mo, dist = deeper_stats_labelled(n, states)
            avg = to / tp if tp else 0.0
            print(f"{n} | {s} | {tp} | {to} | {mo} | {avg:.4f}")
        print("Distribution of #optimal moves per state (n=5):")
        states = labelled_F(5)
        s, tp, to, mo, dist = deeper_stats_labelled(5, states)
        print("  ", dict(sorted(dist.items())))

    if args.bb:
        print()
        print("=" * 78)
        print("C. BRANCH-AND-BOUND DP vs reference DP (exact e lower bound)")
        print("=" * 78)
        print("n | S(n) | ref states | ref evals | ref t(s) | "
              "bb evals | bb lb-calls | bb pruned | bb t(s)")
        for n in range(2, args.bb_max_n + 1):
            rv, rs, re, rt = reference_DP(n)
            bv, bs, be, bl, bp, bt = bb_DP(n, lb_mode="info")
            ok = (rv == bv == KNOWN[n])
            print(f"{n} | {rv} | {rs} | {re} | {rt:.3f} | {be} | {bl} | "
                  f"{bp} | {bt:.3f} | {'OK' if ok else 'MISMATCH'}")
        print("Root check (n=2..5): at A_n the bound skips all but the first")
        print("move (ties included); this is the trivial S_n symmetry, not new")
        print("information about non-optimality.")
        for n in range(2, min(6, args.bb_max_n + 1)):
            root = (0,) * n
            pairs = incomparable_pairs(root, n)
            states = labelled_F(n)
            first = pairs[0]
            best = 1 + max(states[extend(root, *first)],
                           states[extend(root, first[1], first[0])])
            skipped = 0
            for i, j in pairs:
                if (i, j) == first:
                    continue
                lb = 1 + max(L0(extend(root, i, j), n),
                             L0(extend(root, j, i), n))
                if lb >= best:
                    skipped += 1
            print(f"  n={n}: root best={best}, skipped {skipped}/{len(pairs)} "
                  f"(all moves are optimal, distinct Q = {sorted(set(1+max(states[extend(root,i,j)],states[extend(root,j,i)]) for i,j in pairs))})")


if __name__ == "__main__":
    main()
