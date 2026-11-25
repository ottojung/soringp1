#!/usr/bin/env python3
"""Adversary ("resistance") certificates for S(n) > k, unary target.

Model (docs/problem.md, docs/research-certificates-barriers.md):
  A state is a transitively closed strict partial order on n labelled keys,
  represented by a tuple succ with succ[i] bit j set iff i < j.
  m(P) = minimum remaining worst-case comparisons to sort every linear
  extension of P;  S(n) = m(empty antichain).

A *certificate of S(n) > k* is a graded family of finite sets
(Nodes_0, ..., Nodes_k) of non-total posets with P0 in Nodes_k and, for every
P in Nodes_r (r >= 1) and every incomparable pair {x,y} of P, at least one
answer d in {x<y, y<x} with (P+d) in Nodes_{r-1} (or, in the "counting
shortcut" variant, with ceil(log2 e(P+d)) > r-1).  Such a family witnesses
that no sorter strategy reaches a total order within k comparisons, because
an adversary can always answer into the next lower level.

Three certificate styles are generated and measured:
  * two-sided full resistance DAG (exact minimax values);
  * two-sided with the information-bound shortcut on subtrees;
  * one-sided heavy-child (Wells / Peczarski / Stober-Weiss) forward search.

Stdlib only.  Experiments, not proofs of complexity-class claims.
"""

from __future__ import annotations

import argparse
import itertools
import math
import time
from functools import lru_cache


# --------------------------------------------------------------------------
# Poset primitives
# --------------------------------------------------------------------------

def extend(succ, i, j):
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(len(succ)):
        if x == i or (succ[x] & (1 << i)):
            out[x] |= new_greater
    return tuple(out)


def incomparable_pairs(succ):
    n = len(succ)
    return [(i, j) for i in range(n) for j in range(i + 1, n)
            if not (succ[i] & (1 << j)) and not (succ[j] & (1 << i))]


def is_total(succ):
    n = len(succ)
    return all((succ[i] >> j & 1) or (succ[j] >> i & 1)
               for i in range(n) for j in range(i + 1, n))


def dual(succ):
    n = len(succ)
    out = [0] * n
    for i in range(n):
        for j in range(n):
            if (succ[i] >> j) & 1:
                out[j] |= 1 << i
    return tuple(out)


@lru_cache(maxsize=None)
def linear_extensions(succ):
    n = len(succ)
    full = (1 << n) - 1
    dp = [0] * (1 << n)
    dp[0] = 1
    for S in range(1, 1 << n):
        tot = 0
        m = S
        while m:
            x = (m & -m).bit_length() - 1
            m &= m - 1
            if (succ[x] & (S ^ (1 << x))) == 0:
                tot += dp[S ^ (1 << x)]
        dp[S] = tot
    return dp[full]


def ceil_log2(x):
    return (x - 1).bit_length()


# --------------------------------------------------------------------------
# Exact minimax over all labelled posets (n <= 7 feasible)
# --------------------------------------------------------------------------

def minimax_values(n, cap=None):
    states = {}
    order = []

    def solve(succ):
        r = states.get(succ)
        if r is not None:
            return r
        pairs = incomparable_pairs(succ)
        if not pairs:
            states[succ] = 0
            return 0
        best = 1 + min(max(solve(extend(succ, i, j)), solve(extend(succ, j, i)))
                       for i, j in pairs)
        states[succ] = best
        order.append(succ)
        return best

    solve((0,) * n)
    return states


# --------------------------------------------------------------------------
# Canonical relabelling used only for de-duplication.
#
# IMPORTANT soundness property: relabel(P) is a valid poset matrix obtained by
# relabelling P.  Hence relabel(P) == relabel(Q) implies P and Q are
# isomorphic.  If the procedure is not isomorphism-invariant it may fail to
# merge isomorphic posets (over-counting), but it can never merge
# non-isomorphic ones (no under-counting).  Over-counting is sound for the
# direction "some level is empty".
# --------------------------------------------------------------------------

def refine_colors(succ):
    n = len(succ)
    color = [bin(succ[i]).count("1") for i in range(n)]
    while True:
        sig = []
        for i in range(n):
            down = tuple(sorted(color[j] for j in range(n) if (succ[i] >> j) & 1))
            up = tuple(sorted(color[j] for j in range(n) if (succ[j] >> i) & 1))
            sig.append((color[i], down, up))
        order = {v: k for k, v in enumerate(sorted(set(sig)))}
        comp = [order[v] for v in sig]
        if comp == color:
            return color
        color = comp


def relabel(succ):
    n = len(succ)
    color = refine_colors(succ)
    order = sorted(range(n), key=lambda i: (color[i], i))
    new = [0] * n
    for a in range(n):
        bits = succ[order[a]]
        m = 0
        for b in range(n):
            if (bits >> order[b]) & 1:
                m |= 1 << b
        new[a] = m
    return tuple(new)


def relabel_dual(succ):
    return min(relabel(succ), relabel(dual(succ)))


# --------------------------------------------------------------------------
# Counting certificate
# --------------------------------------------------------------------------

def counting_certificate(n, k):
    """Return (proves, nfact, bound, bits).

    proves = (2**k < n!), i.e. the information bound already gives S(n) > k.
    bits = a rough description length of the counting proof (number of bits of
    k plus the single inequality), which is O(log n).
    """
    nfact = math.factorial(n)
    proves = (1 << k) < nfact
    bits = k.bit_length() + n.bit_length() + 2
    return proves, nfact, ceil_log2(nfact), bits


# --------------------------------------------------------------------------
# Two-sided resistance certificate
# --------------------------------------------------------------------------

def build_two_sided(n, k, m, use_count_shortcut=False, cap=None):
    """Build a graded resistance certificate.

    Returns dict with levels (list of sets of labelled posets),
    chosen ((P,pair) -> child), stats.
    """
    root = (0,) * n
    if m[root] <= k:
        raise ValueError("root is not resistant at this budget")
    levels = [None] * (k + 1)
    levels[k] = {root}
    chosen = {}
    covered_by_count = 0
    expanded_pairs = 0

    for r in range(k, 0, -1):
        cur = levels[r]
        # frequency of candidate children for max-coverage greedy
        freq = {}
        candidates = []
        for P in cur:
            for (i, j) in incomparable_pairs(P):
                a = extend(P, i, j)
                b = extend(P, j, i)
                if use_count_shortcut:
                    # child is already certified by the information bound if
                    # ceil(log2 e(child)) > r-1
                    def ok(c):
                        return m[c] > r - 1
                    val = [c for c in (a, b) if ok(c)]
                    short = [c for c in (a, b) if ceil_log2(linear_extensions(c)) > r - 1]
                    if short:
                        covered_by_count += 1
                        # no need to expand this pair at all
                        chosen[(P, (i, j))] = ('count', short[0])
                        continue
                else:
                    val = [c for c in (a, b) if m[c] > r - 1]
                if not val:
                    raise RuntimeError("non-resistant node in certificate")
                candidates.append((P, (i, j), val))
                for c in val:
                    freq[c] = freq.get(c, 0) + 1
        nxt = set()
        for (P, pair, val) in candidates:
            expanded_pairs += 1
            pick = None
            bestf = -1
            for c in val:
                if c in nxt:
                    pick = c
                    break
                f = freq.get(c, 0)
                if f > bestf:
                    bestf = f
                    pick = c
            nxt.add(pick)
            chosen[(P, pair)] = pick
        levels[r - 1] = nxt
        if cap is not None and len(nxt) > cap:
            return {"levels": levels, "chosen": chosen,
                    "capped": True, "covered_by_count": covered_by_count}
    return {"levels": levels, "chosen": chosen, "capped": False,
            "covered_by_count": covered_by_count}


def two_sided_stats(levels, chosen):
    allnodes = set()
    for s in levels:
        allnodes |= s
    dag_nodes = len(allnodes)
    # raw tree size via DP over (P, r)
    memo = {}

    def tree_size(P, r):
        if r == 0:
            return 1
        key = (P, r)
        if key in memo:
            return memo[key]
        total = 1
        for pair in incomparable_pairs(P):
            e = chosen.get((P, pair))
            if e is None:
                continue
            if isinstance(e, tuple) and e and e[0] == 'count':
                total += 1  # a count-certified leaf, no expansion
            else:
                total += tree_size(e, r - 1)
        memo[key] = total
        return total

    root = (0,) * len(next(iter(allnodes)))
    raw = tree_size(root, len(levels) - 1)
    quot = len({relabel_dual(P) for P in allnodes})
    return {"dag_nodes": dag_nodes, "raw_tree_nodes": raw, "quotient_nodes": quot}


# --------------------------------------------------------------------------
# One-sided heavy-child (Wells) certificate
# --------------------------------------------------------------------------

def wells_forward(n, C, cap=None, max_seconds=None, use_dual=True):
    """One-sided heavy-child forward search.

    Level 0 = {P0}.  Level c+1 = for each P in level c and each incomparable
    pair, if both children have e <= 2^(C-c-1), keep the heavier child.
    If a level is empty, no height-C tree exists.  Levels are stored
    de-duplicated by a sound canonical relabelling key.
    """
    keyfn = relabel_dual if use_dual else relabel
    root = (0,) * n
    levels = [{keyfn(root): root}]
    t0 = time.perf_counter()
    capped = False
    c = 0
    while levels[-1] and c < C:
        if max_seconds is not None and time.perf_counter() - t0 > max_seconds:
            capped = True
            break
        cur = levels[-1]
        nxt = {}
        thr = 1 << (C - c - 1)
        for P in cur.values():
            for (i, j) in incomparable_pairs(P):
                a = extend(P, i, j)
                b = extend(P, j, i)
                ea = linear_extensions(a)
                eb = linear_extensions(b)
                if ea <= thr and eb <= thr:
                    child = a if ea >= eb else b
                    k = keyfn(child)
                    if k not in nxt:
                        nxt[k] = child
        levels.append(nxt)
        c += 1
        if cap is not None and len(nxt) > cap:
            capped = True
            break
    return {"levels": levels, "capped": capped, "seconds": time.perf_counter() - t0}


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

KNOWN_S = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16,
           9: 19, 10: 22, 11: 26, 12: 30}


def report_counting(pairs):
    print("=" * 74)
    print("COUNTING CERTIFICATE (information bound) for S(n) > k")
    print("=" * 74)
    print(f"{'(n,k)':>9} {'N=n+k+1':>8} {'n!':>14} {'2^k':>14} "
          f"{'2^k<n!?':>8} {'ceil(log2 n!)':>13}")
    for (n, k) in pairs:
        proves, nfact, bound, bits = counting_certificate(n, k)
        print(f"{str((n,k)):>9} {n+k+1:>8} {nfact:>14} {1<<k:>14} "
              f"{str(proves):>8} {bound:>13}")
    print()
    print("If 2^k < n! the one-line counting argument already certifies")
    print("S(n) > k; its description length is O(log n) bits (just the")
    print("inequality, recomputed from the input).")


def report_two_sided(n, k):
    print("-" * 74)
    print(f"TWO-SIDED RESISTANCE CERTIFICATE  n={n} k={k} (S(n)={KNOWN_S.get(n)})")
    print("-" * 74)
    t0 = time.perf_counter()
    m = minimax_values(n)
    t1 = time.perf_counter()
    print(f"exact minimax over {len(m)} labelled posets: {t1-t0:.2f}s")
    res = build_two_sided(n, k, m)
    if res.get("capped"):
        print("CAP EXCEEDED")
        return
    st = two_sided_stats(res["levels"], res["chosen"])
    print(f"levels sizes: {[len(s) for s in res['levels']]}")
    print(f"  raw tree nodes      = {st['raw_tree_nodes']}")
    print(f"  DAG-shared nodes    = {st['dag_nodes']}")
    print(f"  symmetry-quotient   = {st['quotient_nodes']}")
    print(f"  N = n+k+1           = {n+k+1}")
    print()


def report_two_sided_shortcut(n, k):
    print("-" * 74)
    print(f"TWO-SIDED + COUNTING SHORTCUT  n={n} k={k}")
    print("-" * 74)
    m = minimax_values(n)
    res = build_two_sided(n, k, m, use_count_shortcut=True)
    if res.get("capped"):
        print("CAP EXCEEDED")
        return
    st = two_sided_stats(res["levels"], res["chosen"])
    print(f"levels sizes: {[len(s) for s in res['levels']]}")
    print(f"  raw tree nodes      = {st['raw_tree_nodes']}")
    print(f"  DAG-shared nodes    = {st['dag_nodes']}")
    print(f"  symmetry-quotient   = {st['quotient_nodes']}")
    print(f"  pairs covered by count shortcut = {res['covered_by_count']}")
    print()


def report_wells(n, C, cap=None, max_seconds=None):
    res = wells_forward(n, C, cap=cap, max_seconds=max_seconds)
    sizes = [len(s) for s in res["levels"]]
    total = sum(sizes)
    empty_at = None
    for i, s in enumerate(res["levels"]):
        if not s:
            empty_at = i
            break
    status = "capped" if res["capped"] else "complete"
    print(f"n={n:>2} C={C:>2} N={n+C+1:>3} status={status:>8} "
          f"time={res['seconds']:.2f}s total_nodes={total}")
    print(f"      level sizes: {sizes}")
    if empty_at is not None:
        print(f"      -> level {empty_at} EMPTY: certificate proves S({n}) > {C}")
    print()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mode", default="counting",
                    choices=["counting", "two-sided", "two-sided-shortcut",
                             "wells", "all"])
    ap.add_argument("--n", type=int, default=6)
    ap.add_argument("--k", type=int, default=None)
    ap.add_argument("--cap", type=int, default=200000)
    ap.add_argument("--seconds", type=float, default=120.0)
    args = ap.parse_args()

    cases = [(5, 6), (6, 9), (7, 12), (8, 15), (12, 29)]

    if args.mode in ("counting", "all"):
        report_counting(cases)

    if args.mode in ("two-sided", "all"):
        for (n, k) in [(5, 6), (6, 9)]:
            report_two_sided(n, k)
        if args.mode == "all":
            report_two_sided(7, 12)

    if args.mode == "two-sided-shortcut":
        report_two_sided_shortcut(args.n, args.k)

    if args.mode in ("wells", "all"):
        print("=" * 74)
        print("ONE-SIDED HEAVY-CHILD (WELLS) CERTIFICATES")
        print("=" * 74)
        for (n, k) in cases:
            report_wells(n, k, cap=args.cap, max_seconds=args.seconds)


if __name__ == "__main__":
    main()
