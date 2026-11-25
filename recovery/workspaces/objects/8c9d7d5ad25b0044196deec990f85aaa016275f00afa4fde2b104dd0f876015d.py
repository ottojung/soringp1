#!/usr/bin/env python3
"""Finite/checkable computations toward S(13) > C(13)=33 (NOT a proof of it).

Model (docs/problem.md): S(n) = minimum worst-case number of adaptive pairwise
comparisons to sort n distinct labelled keys.  A state is the transitively
closed poset P (successor bitmasks).  S(n) <= k iff the sorter wins the minimax
game G(n,k) from the antichain.

Target question (falsifiable): is S(13) <= 33?
  * C(13) = ceil(log2(13!)) = 33 (information bound).  [definition/deduction]
  * Literature reports S(13)=34 (Kasai et al. 1994; Peczarski 2004, cited in
    docs/research-certificates-barriers.md; OEIS A036604).  This script does NOT
    verify that result and makes NO claim that S(13)>33.  [literature, unverified]
  * A *witness* refuting S(13)>33 would be an explicit height-33 comparison
    decision tree (or a checkable certificate) sorting 13 keys; verifying such a
    witness is finite but the witness is exponentially large in the worst case.
  * A *finite obstruction* refuting S(13)<=33 in the Wells one-sided form would
    be an index c with S_c = empty for the admissible heavier-child forward
    search at budget C=33 (see docs/research-n12-nontightness.md §4).  Finding
    such c is a finite computation if it exists, but it may be infeasible.

This script performs ONLY computations that are reproducible on a workstation:
  1. Exact n,C,budget parameters and the one-ply/admissibility analysis.
  2. The Wells admissible heavier-child levels S_0..S_d for small d, quotiented
     by the obvious symmetry classes of the structured states encountered at
     shallow depth (EXACT for the orbit counts reported; see assumptions).
  3. An optional capped budgeted search for a height-33 witness using
     polynomial-space capped extension enumeration and move pruning
     (scripts/budgeted_pruning_experiments.py primitives).  A found witness is
     verifiable in principle; node-cap exhaustion is INCONCLUSIVE.
  4. Exact small-n control: confirm the machinery on known values.

ASSUMPTIONS (stated explicitly; violations invalidate conclusions):
  A1. Adaptive, worst-case, pairwise comparisons of distinct labelled keys.
  A2. Poset states are transitively closed; e(P) = number of linear extensions.
  A3. Admissibility for a height-C tree: a state reached after c comparisons has
      e(P) <= 2^(C-c).  Wells S_c keeps the heavier child of every admissible
      comparison of some P in S_{c-1}.  Empty S_c => S(n) > C.  [deduction]
  A4. Node-cap / time-cap exhaustion is INCONCLUSIVE (never evidence for/against).
  A5. The one-ply bound L1 uses exact e(P) (downset DP, O(2^n) space in this
      implementation) and is feasible here only for local checks, not a full
      n=13 exact minimax.

Reproduce:
  python3 scripts/s13_finite_check.py --summary
  python3 scripts/s13_finite_check.py --wells-depth 2
  python3 scripts/s13_finite_check.py --witness-search --node-cap 200000
  python3 -m unittest tests.test_s13_finite_check -q   (if test exists)
"""

from __future__ import annotations

import argparse
import math
import sys
import time

sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/scripts')
from one_ply_obstruction import (  # noqa: E402
    add_relation, linear_extensions, L0, L1, ceil_log2, incomparable_pairs,
)

N = 13
C = 33  # ceil(log2(13!))
BUDGET = C  # test S(13) <= 33
CAP = lambda depth: 1 << (C - depth)  # admissibility cap after `depth` comparisons


def antichain(n=N):
    return (0,) * n


def canon_key_shallow(succ, n=N):
    """A cheap symmetry signature for shallow structured posets (NOT a complete
    canonical form).  Groups elements by (in-degree mask popcount profile encoded
    via successor/popcount signature) after sorting.  Used only to merge obvious
    isomorphs; distinct keys may still be isomorphic in general, so level sizes
    reported with this key are UPPER BOUNDS on orbit counts.  Exact orbit counts
    at depths 0-2 are derived by the hand analysis in --wells-depth and printed
    separately."""
    pred = [0] * n
    for i in range(n):
        m = succ[i]
        while m:
            j = (m & -m).bit_length() - 1
            m &= m - 1
            pred[j] |= 1 << i
    sig = tuple(sorted((succ[i].bit_count(), pred[i].bit_count()) for i in range(n)))
    return sig


def summary():
    f13 = math.factorial(N)
    print('== s13 finite check summary ==')
    print(f'n={N}, 13!={f13}, bit_length={f13.bit_length()}')
    print(f'C(13)=ceil(log2(13!))={ceil_log2(f13)}  [deduction]')
    print(f'target budget for S(13)<=33? C={C}')
    print(f'2^33={2**33}, 13!/2^33={f13/2**33:.6f} (global slack ratio)')
    print('Literature (unverified here): Kasai et al. 1994 / Peczarski 2004 report S(13)=34. [literature]')
    print('This script makes NO claim that S(13)>33.')
    print()
    A = antichain()
    eA = linear_extensions(A) if N <= 13 else None  # 13! fits in int; DP table 2^13*small
    print(f'e(antichain)={eA} (expected 13!)' if eA is not None else 'e(antichain)=13! (not computed)')
    # one-ply from antichain
    t = time.perf_counter()
    # for antichain, by symmetry L1 is determined by any pair -> P1
    P1 = add_relation(A, 0, 1)
    e1 = linear_extensions(P1)
    l1a = 1 + ceil_log2(max(e1, e1))
    print(f'P1={{0<1}} e={e1} (=13!/2) L0={ceil_log2(e1)} 1+L0={l1a} (depth-1 one-ply)')
    print(f'depth-1 admissible cap 2^(33-1)={CAP(1)} => P1 admissible? {e1 <= CAP(1)}')
    print(f'all {N*(N-1)//2} first moves form 1 orbit under S_{N}; heavier child ~ P1. [deduction/symmetry]')
    # depth-2 classes from P1
    print()
    print('Depth-2 from P1 (orbit classes under Aut(P1)=Sym({2..12})):')
    for name, (i, j) in [('V {0<1,0<2}', (0, 2)), ('Lambda {0<1,2<1}', (1, 2)), ('disjoint {0<1,2<3}', (2, 3))]:
        c1 = add_relation(P1, i, j); c2 = add_relation(P1, j, i)
        ea, eb = linear_extensions(c1), linear_extensions(c2)
        h = max(ea, eb)
        ok = ea <= CAP(2) and eb <= CAP(2)
        mult = 11 if name.startswith('V') or name.startswith('L') else math.comb(11, 2)
        print(f'  {name:24s} mult={mult:2d} e=({ea},{eb}) heavier={h} cap2={CAP(2)} admissible={ok}')
    print(f'elapsed {time.perf_counter()-t:.3f}s')


def wells_levels(max_depth=2):
    """Compute Wells S_c heavier-child levels up to max_depth.

    EXACT for depth 0-1 by symmetry.  For depth >=2 this uses the shallow
    canon_key_shallow to merge states (upper bound on distinct orbits, never a
    false negative on emptiness if run to completion without cap).  With
    node/state caps it is INCONCLUSIVE.
    """
    print(f'== Wells admissible heavier-child levels, n={N}, C={C}, max_depth={max_depth} ==')
    A = antichain()
    levels = [[A]]
    for c in range(1, max_depth + 1):
        cap = CAP(c)
        prev = levels[c - 1]
        nxt = {}
        moves = adm = 0
        t = time.perf_counter()
        for P in prev:
            for (i, j) in incomparable_pairs(P):
                moves += 1
                c1 = add_relation(P, i, j); c2 = add_relation(P, j, i)
                e1 = linear_extensions(c1); e2 = linear_extensions(c2)
                if e1 <= cap and e2 <= cap:
                    adm += 1
                    h = c1 if e1 >= e2 else c2
                    nxt[canon_key_shallow(h)] = h
        levels.append(list(nxt.values()))
        dt = time.perf_counter() - t
        print(f'S_{c}: prev_states={len(prev)} moves={moves} admissible={adm} '
              f'heavier_child_classes(shallow)={len(nxt)} cap={cap} {dt:.3f}s')
        if not nxt:
            print(f'  => S_{c} EMPTY (finite obstruction, under assumptions A1-A3).')
            print('  WARNING: only claim S(13)>33 if this run is complete, exact, and audited.')
            return levels
        # report e distribution
        es = sorted(linear_extensions(x) for x in nxt.values())
        print(f'  e(min/med/max)={es[0]}/{es[len(es)//2]}/{es[-1]}  L0 range [{ceil_log2(es[0])},{ceil_log2(es[-1])}]')
    print('INCONCLUSIVE: no empty level reached within max_depth (not evidence for S(13)<=33).')
    print('Minimal next finite computation: extend S_c with exact canonical labeling / stronger pruning until empty or resource limit; any empty level is a checkable obstruction certificate.')
    return levels


def witness_search(node_cap=200000):
    """Capped search for a height-33 sorting tree (witness for S(13)<=33).

    Uses the reference/pruned decision idea from budgeted_pruning_experiments but
    implemented locally with poly-space capped extension enumeration (e_exceeds
    via exact DP here is O(2^n) space; for n=13 that's 8192 entries - trivial).
    A returned True would mean a witness exists (checkable in principle by
    emitting the strategy).  Node-cap hit is INCONCLUSIVE.
    """
    print(f'== Capped witness search: can_sort(antichain_{N}, {BUDGET}) node_cap={node_cap} ==')
    print('NOTE: result True => witness exists (refutes S(13)>33 under A1-A3).')
    print('      node-cap / False-from-cap => INCONCLUSIVE.')
    # small-n safe e<=cap test
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def e_count(succ):
        # order-ideal DP, O(2^n) space
        nloc = N
        predm = [0] * nloc
        for ii in range(nloc):
            mm = succ[ii]
            while mm:
                jj = (mm & -mm).bit_length() - 1
                mm &= mm - 1
                predm[jj] |= 1 << ii
        full = (1 << nloc) - 1
        dp = [0] * (1 << nloc)
        dp[0] = 1
        for S in range(1 << nloc):
            if dp[S] == 0:
                continue
            avail = full ^ S
            mm = avail
            while mm:
                x = (mm & -mm).bit_length() - 1
                mm &= mm - 1
                if (predm[x] & S) == predm[x]:
                    dp[S | (1 << x)] += dp[S]
        return dp[full]

    counter = [0]; t0 = time.perf_counter()

    def solve(succ, d):
        counter[0] += 1
        if counter[0] > node_cap:
            return None
        if is_total_local(succ):
            return True
        if d == 0:
            return False
        # extension-count prune (safe)
        ec = e_count(succ)
        if ec > (1 << d):
            return False
        for (i, j) in incomparable_pairs(succ):
            a = solve(add_relation(succ, i, j), d - 1)
            if a is None:
                return None
            if a:
                b = solve(add_relation(succ, j, i), d - 1)
                if b is None:
                    return None
                if b:
                    return True
        return False

    res = solve(antichain(), BUDGET)
    dt = time.perf_counter() - t0
    status = 'WITNESS_EXISTS (can_sort=True)' if res is True else ('INCONCLUSIVE (node cap)' if res is None else 'NO_WITNESS_FOUND (search complete?)')
    print(f'result={status} nodes={counter[0]} {dt:.3f}s')
    if res is False and counter[0] <= node_cap:
        print('NOTE: a complete False with no cap hit would mean no height-33 tree exists under this exact search; verify completeness/audit before claiming S(13)>33.')
    return res


def is_total_local(succ):
    n = len(succ)
    for i in range(n):
        for j in range(i + 1, n):
            if not (succ[i] >> j & 1) and not (succ[j] >> i & 1):
                return False
    return True


def controls():
    print('== Small-n controls (exact) ==')
    from one_ply_obstruction import minimax
    for n, expect in [(4, 5), (5, 7)]:
        got = minimax((0,) * n)
        print(f'S({n})={got} expected {expect} {"OK" if got == expect else "FAIL"}')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--summary', action='store_true')
    ap.add_argument('--wells-depth', type=int, default=0)
    ap.add_argument('--witness-search', action='store_true')
    ap.add_argument('--node-cap', type=int, default=200000)
    ap.add_argument('--controls', action='store_true')
    args = ap.parse_args()
    if not any([args.summary, args.wells_depth, args.witness_search, args.controls]):
        args.summary = True
        args.wells_depth = 2
        args.controls = True
    if args.controls:
        controls(); print()
    if args.summary:
        summary(); print()
    if args.wells_depth:
        wells_levels(args.wells_depth); print()
    if args.witness_search:
        witness_search(args.node_cap)


if __name__ == '__main__':
    main()
