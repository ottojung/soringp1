#!/usr/bin/env python3
"""Greatest-bisimulation compression of the exact minimax poset state space.

Unary-only state compression for S(n).  A state is a labelled strict partial
order P on [n]; F(P) is the minimax remaining comparison count.  Moves from a
non-total P are the two orientations of each incomparable pair.

Candidate canonicalization: ~_bl, the greatest bisimulation of this transition
system with terminal outputs UNOBSERVED (all total orders equivalent).  This is
coarser than isomorphism (e.g. V and inverse-V merge at n=3).

Claim (proved in docs/research-state-compression.md companion note): P ~_bl Q
implies F(P) = F(Q).  The quotient recurrence on classes is exact, so the
compression is sound for computing S(n).

This script measures the number of ~_bl classes reachable from the antichain
(all labelled posets are reachable) against A001035(n) and A000112(n), and
verifies F is constant on every class.  Exact integers only.
"""

import sys
import time

sys.path.insert(0, "scripts")
from benchmark_symmetry_quotients import (  # noqa: E402
    extend,
    incomparable_pairs,
    make_refined_canon,
    quotient_classes,
)

A001035 = {0: 1, 1: 1, 2: 3, 3: 19, 4: 219, 5: 4231, 6: 130023, 7: 6129859}


def build_lts(n):
    """Return (reps, values, succ_sets, terminal) for the iso-class LTS."""
    canon = make_refined_canon(n)
    vals = quotient_classes(n)  # canon rep -> F
    reps = list(vals.keys())
    idx = {c: i for i, c in enumerate(reps)}
    succ = []
    terminal = []
    for c in reps:
        ps = incomparable_pairs(c, n)
        if not ps:
            terminal.append(True)
            succ.append(frozenset())
        else:
            terminal.append(False)
            s = set()
            for i, j in ps:
                s.add(idx[canon(extend(c, i, j))])
                s.add(idx[canon(extend(c, j, i))])
            succ.append(frozenset(s))
    return reps, vals, succ, terminal


def greatest_bisim(succ):
    """Greatest bisimulation (set-of-successors transition) via refinement.

    Refine *within* each block so the partition is monotone; comparing whole
    partitions (not block ids) avoids the id-permutation oscillation that a
    naive ``sorted(set(sig))`` relabelling produces.
    """
    n = len(succ)
    part = [frozenset(range(n))]
    while True:
        stog = {}
        for g in part:
            for i in g:
                stog[i] = g
        newpart = []
        for g in part:
            subgroups = {}
            for i in g:
                s = frozenset(stog[j] for j in succ[i])
                subgroups.setdefault(s, []).append(i)
            for v in subgroups.values():
                newpart.append(frozenset(v))
        newpart = frozenset(newpart)
        if newpart == frozenset(part):
            break
        part = list(newpart)
    block = [0] * n
    for bi, g in enumerate(part):
        for i in g:
            block[i] = bi
    return block


def main():
    print("n | iso classes (A000112) | bisim classes | A001035(n) | "
          "reduction A001035/bisim | iso/bisim | F-constant? | s")
    for n in range(2, 8):
        t0 = time.perf_counter()
        reps, vals, succ, terminal = build_lts(n)
        block = greatest_bisim(succ)
        nb = len(set(block))
        # F constant on each bisim class?
        fval = {}
        ok = True
        for i, b in enumerate(block):
            v = vals[reps[i]]
            if b in fval and fval[b] != v:
                ok = False
            fval.setdefault(b, v)
        dt = time.perf_counter() - t0
        full = A001035.get(n)
        red = full / nb if full else 0
        print(f"{n} | {len(reps)} | {nb} | {full} | {red:.2f} | "
              f"{len(reps)/nb:.2f} | {ok} | {dt:.2f}")


if __name__ == "__main__":
    main()
