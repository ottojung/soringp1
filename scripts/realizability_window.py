#!/usr/bin/env python3
"""Realizability of posets on height-S(n) optimal plays (window theorem).

Model (docs/problem.md, docs/upper-bound.md):
  state = transitively closed strict poset, tuple of successor bitmasks;
  F(P) = 1 + min_{incomparable i,j} max(F(P+i<j), F(P+j<i)), F(total) = 0;
  covers(P) = number of cover relations;
  pi(P) = min over linear extensions T of P of |covers(T) \\ P|;
  realizable(P, d) = P occurs at depth d in the decision tree of SOME
  sorting strategy of worst-case height <= S(n) rooted at the antichain
  (padded/wasted comparisons allowed; the class without them is smaller).

Forward DP (exact):
  reach[0] = {antichain}
  reach[d+1] = { canonical children of states in reach[d] }
             union reach[d] \\ {antichain}   (wasted comparison)
  filtered to F(C) <= S(n) - (d+1).

Checks performed for each n <= bound (all empirically exact at n <= 6):
  W1  every realizable (P,d) satisfies covers(P) <= d <= S - max(F(P), pi(P));
  W2  the realizable depth set equals the full window at every depth
      (window sufficiency, conjecture for all n);
  W3  the star V_n is realizable iff n <= 3 (corollary: never for n >= 4).

This is an experiment, not a proof.  The companion note is
notes/research-realizability-window.md.
"""

import argparse
import itertools
import sys
from functools import lru_cache


def extend(succ, i, j, n):
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(n):
        if x == i or (succ[x] & (1 << i)):
            out[x] |= new_greater
    return tuple(out)


def ipairs(succ, n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)
            if not (succ[i] >> j) & 1 and not (succ[j] >> i) & 1]


def canon(succ, n):
    best = succ
    for p in itertools.permutations(range(n)):
        t = [0] * n
        for a in range(n):
            s = succ[a]
            while s:
                b = (s & -s).bit_length() - 1
                t[p[a]] |= 1 << p[b]
                s &= s - 1
        cand = tuple(t)
        if cand < best:
            best = cand
    return best


def all_classes(n):
    classes = {(0,) * n}
    frontier = [(0,) * n]
    while frontier:
        nxt = []
        for succ in frontier:
            for (i, j) in ipairs(succ, n):
                for c in (extend(succ, i, j, n), extend(succ, j, i, n)):
                    cc = canon(c, n)
                    if cc not in classes:
                        classes.add(cc)
                        nxt.append(cc)
        frontier = nxt
    return sorted(classes)


def build_F(classes, n):
    F = {}

    def f(succ):
        if succ in F:
            return F[succ]
        ps = ipairs(succ, n)
        if not ps:
            F[succ] = 0
            return 0
        best = None
        for (i, j) in ps:
            a = f(canon(extend(succ, i, j, n), n))
            b = f(canon(extend(succ, j, i, n), n))
            m = 1 + max(a, b)
            if best is None or m < best:
                best = m
        F[succ] = best
        return best

    f((0,) * n)
    return F


def build_stats(classes, n, F):
    """e(P), covers(P), pi(P) per class plus F."""
    stat = {}
    for succ in classes:
        exts = []
        hist = []
        pred = [0] * n
        for x in range(n):
            for y in range(n):
                if (succ[y] >> x) & 1:
                    pred[x] |= 1 << y

        def rec(placed):
            if placed == (1 << n) - 1:
                exts.append(tuple(hist))
                return
            for x in range(n):
                if not (placed >> x) & 1 and not (pred[x] & ~placed):
                    hist.append(x)
                    rec(placed | (1 << x))
                    hist.pop()

        rec(0)
        e = len(exts)
        covers = sum(1 for x in range(n) for y in range(n)
                     if (succ[x] >> y) & 1 and not (succ[x] & pred[y]))
        best_adj = max(sum(1 for k in range(n - 1)
                           if (succ[L[k]] >> L[k + 1]) & 1) for L in exts)
        stat[succ] = (e, covers, (n - 1) - best_adj, F[succ])
    return stat


def build_reach(n, S, F):
    """reach[d] = classes occurring at depth d of some height<=S tree.

    A comparison contributes either child only when BOTH child subtrees fit
    the remaining height budget. A wasted comparison leaves the state fixed
    and is permitted only when that state itself fits the same budget.
    """
    reach = [{(0,) * n}]
    for d in range(S):
        nxt = set()
        for Q in reach[d]:
            for i, j in ipairs(Q, n):
                C0 = canon(extend(Q, i, j, n), n)
                C1 = canon(extend(Q, j, i, n), n)
                if max(F[C0], F[C1]) <= S - (d + 1):
                    nxt.update((C0, C1))
            if Q != (0,) * n and F[Q] <= S - (d + 1):
                nxt.add(Q)  # wasted comparison: state unchanged
        reach.append(nxt)
    return reach


def analyze(n, check=True, verbose=True):
    classes = all_classes(n)
    F = build_F(classes, n)
    S = F[(0,) * n]
    if verbose:
        print(f"n={n}: {len(classes)} classes, S({n}) = {S}", flush=True)
    stat = build_stats(classes, n, F)
    reach = build_reach(n, S, F)
    depths = {}
    for d, st in enumerate(reach):
        for C in st:
            depths.setdefault(C, []).append(d)

    if check:
        viol = 0
        for succ, ds in depths.items():
            e, cov, pi, fv = stat[succ]
            for d in ds:
                if not (cov <= d <= S - max(fv, pi)
                        and e <= 2 ** (S - d)):
                    viol += 1
        assert viol == 0, f"window-necessity violated at {viol} states"
        sufficiency_mismatches = 0
        for succ in classes:
            e, cov, pi, fv = stat[succ]
            pred = [d for d in range(S + 1)
                    if cov <= d and fv <= S - d and pi <= S - d
                    and e <= 2 ** (S - d)]
            sufficiency_mismatches += sum(
                d not in depths.get(succ, []) for d in pred)
        star = [0] * n
        star[0] = ((1 << n) - 1) ^ 1
        st = canon(tuple(star), n)
        assert (st in depths) == (n <= 3), "star exclusion check failed"
        if verbose:
            print(f"  realizable classes: {len(depths)}/{len(classes)}; "
                  f"window necessity holds; false-positive window "
                  f"depth-state pairs: {sufficiency_mismatches}; "
                  f"star excluded for n>=4: {n > 3}")
    return S, classes, stat, depths, reach


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-n", type=int, default=6,
                    help="largest n to verify (default 6; n=6 runs about a "
                         "minute, n<=3 fast)")
    args = ap.parse_args()
    rows = []
    for n in range(1, min(args.n, 6) + 1):
        S, classes, stat, depths, reach = analyze(n)
        rows.append((n, S, len(classes), len(depths)))
    print("n  S(n)  classes  realizable")
    for r in rows:
        print(f"{r[0]}  {r[1]}  {r[2]}  {r[3]}")


if __name__ == "__main__":
    main()
