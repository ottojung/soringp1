#!/usr/bin/env python3
"""Independent referee for paired vs unpaired bisimulation on the exact
minimax sorting LTS.

Model (docs/problem.md, docs/research-state-compression.md):
  States are isomorphism classes of labelled strict partial orders on [n].
  From a non-total poset P, each incomparable pair {x,y} is a sorter action
  with the two adversarial successors P+x<y and P+y<x.  Total orders are
  terminal and unobserved (all equivalent).

Unpaired signature (the earlier heuristic):
    sig_u(P) = { block(child) : child is any successor of any action }
  = the union of the individual child classes.  This discards which two
  children came from the same action.

Paired signature (correct action-preserving):
    sig_p(P) = { {block(P+x<y), block(P+y<x)} : {x,y} incomparable }
  = the set of unordered pairs of child classes, one pair per action.

Both are computed as greatest fixpoints over partitions of the iso-class LTS.
F is checked to be constant on every paired class (soundness) and on every
unpaired class (falsification probe).

Exact integers only.
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


def build_lts(n):
    """Return (reps, values, actions, terminal).

    actions[c] = tuple of (child_index, child_index) for each incomparable pair.
    """
    canon = make_refined_canon(n)
    vals = quotient_classes(n)
    reps = list(vals.keys())
    idx = {c: i for i, c in enumerate(reps)}
    actions = []
    terminal = []
    for c in reps:
        ps = incomparable_pairs(c, n)
        if not ps:
            terminal.append(True)
            actions.append(())
        else:
            terminal.append(False)
            acts = []
            for i, j in ps:
                acts.append((idx[canon(extend(c, i, j))],
                             idx[canon(extend(c, j, i))]))
            actions.append(tuple(acts))
    return reps, vals, actions, terminal


def greatest_bisim(actions, paired):
    """Greatest fixpoint over partitions.

    paired=True  -> signature is the set of unordered pairs of child blocks.
    paired=False -> signature is the set of individual child blocks (union).
    """
    n = len(actions)
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
                if paired:
                    s = frozenset(
                        frozenset((stog[a], stog[b])) for a, b in actions[i]
                    )
                else:
                    s = frozenset(
                        stog[a] for ab in actions[i] for a in ab
                    )
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


def check(block, reps, vals):
    fval = {}
    ok = True
    for i, b in enumerate(block):
        v = vals[reps[i]]
        if b in fval and fval[b] != v:
            ok = False
        fval.setdefault(b, v)
    return ok


def main():
    ns = [int(a) for a in sys.argv[1:]] or list(range(2, 9))
    print("n | iso | paired | unpaired | paired=unpaired | F paired | F unpaired | s")
    for n in ns:
        t0 = time.perf_counter()
        reps, vals, actions, term = build_lts(n)
        bp = greatest_bisim(actions, True)
        bu = greatest_bisim(actions, False)
        np_, nu = len(set(bp)), len(set(bu))
        # partition equality: compare block ids via canonical relabeling
        cp, cu = {}, {}
        for i in range(len(reps)):
            cp.setdefault(bp[i], len(cp))
            cu.setdefault(bu[i], len(cu))
        same = all(cp[bp[i]] == cu[bu[i]] for i in range(len(reps)))
        fp = check(bp, reps, vals)
        fu = check(bu, reps, vals)
        dt = time.perf_counter() - t0
        print(f"{n} | {len(reps)} | {np_} | {nu} | {same} | {fp} | {fu} | {dt:.2f}")


if __name__ == "__main__":
    main()
