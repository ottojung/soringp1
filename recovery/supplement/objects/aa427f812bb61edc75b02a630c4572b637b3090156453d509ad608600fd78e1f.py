#!/usr/bin/env python3
"""Succinct-strategy size experiments for the unary antichain S(n) problem.

Model (docs/problem.md, docs/research-strategy-certificates.md):
  State = transitively closed poset on n labelled keys, succ[i] bit j iff i<j.
  F(P) = 0 if P total, else 1 + min_{x||y} max(F(P+x<y), F(P+y<x)).
  S(n) = F(empty antichain).

A *single-policy quotient DAG* is the DAG over S_n-isomorphism classes
(canonical posets) reachable by one optimal strategy.  Its size is the
number of distinct canonical states visited.  This is the natural measure
of a succinct strategy: an iso-equivariant strategy is a function on
canonical states, and a relabeling map recovers the concrete labels.

We compute, for n=1..8:
  * S(n) and the rigorous lower bound S(n)+1 on quotient-DAG size;
  * the greedy-argmin quotient-DAG size (first optimal move in canonical order);
  * the greedy-maximin / random-tie-break range;
  * the labelled single-policy DAG size 2*n!-1 for comparison.

No external libraries.  No proof is claimed beyond the deductions labelled.
"""

import argparse
import itertools
import random
import sys


def extend(succ, i, j):
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
        if not (succ[i] >> j & 1) and not (succ[j] >> i & 1)
    ]


def is_total(succ, n):
    return not incomparable_pairs(succ, n)


# --------------------------------------------------------------------------
# Canonical form under S_n: 2-dim colour refinement, then lexicographically
# least encoding over relabellings preserving colours.
# --------------------------------------------------------------------------

def refine_colors(succ, n):
    color = [bin(succ[i]).count("1") for i in range(n)]
    while True:
        sig = []
        for i in range(n):
            down = tuple(sorted(color[j] for j in range(n) if succ[i] >> j & 1))
            up = tuple(sorted(color[j] for j in range(n) if succ[j] >> i & 1))
            sig.append((color[i], down, up))
        order = {v: k for k, v in enumerate(sorted(set(sig)))}
        comp = [order[v] for v in sig]
        if comp == color:
            return color
        color = comp


def _encode(succ, perm, n):
    new = []
    for a in range(n):
        bits = succ[perm[a]]
        m = 0
        for b in range(n):
            if bits >> perm[b] & 1:
                m |= 1 << b
        new.append(m)
    return tuple(new)


def make_refined_canon(n):
    cache = {}

    def canon(succ):
        if succ in cache:
            return cache[succ]
        color = refine_colors(succ, n)
        groups = {}
        for i, c in enumerate(color):
            groups.setdefault(c, []).append(i)
        gs = [groups[c] for c in sorted(groups)]
        best = None
        for combo in itertools.product(*(itertools.permutations(g) for g in gs)):
            perm = [x for p in combo for x in p]
            e = _encode(succ, perm, n)
            if best is None or e < best:
                best = e
        cache[succ] = best
        return best

    return canon


# --------------------------------------------------------------------------
# Exact F on canonical states (S_n quotient DP).
# --------------------------------------------------------------------------

def solve_canonical(n):
    canon = make_refined_canon(n)
    vals = {}

    def solve(c):
        if c in vals:
            return vals[c]
        ps = incomparable_pairs(c, n)
        if not ps:
            vals[c] = 0
            return 0
        best = 1 + min(
            max(solve(canon(extend(c, i, j))), solve(canon(extend(c, j, i))))
            for i, j in ps
        )
        vals[c] = best
        return best

    solve(canon((0,) * n))
    return canon, vals


def optimal_children(canon, vals, c, n):
    """All (pair, yes, no) edges that are optimal at canonical state c."""
    f = vals[c]
    out = []
    for (i, j) in incomparable_pairs(c, n):
        a = canon(extend(c, i, j))
        b = canon(extend(c, j, i))
        if 1 + max(vals[a], vals[b]) == f:
            out.append(((i, j), a, b))
    return out


def quotient_dag_size(canon, vals, n, tie="first", rng=None):
    """Number of distinct canonical states visited by one optimal strategy."""
    root = canon((0,) * n)
    seen = set()
    stack = [root]
    while stack:
        c = stack.pop()
        if c in seen:
            continue
        seen.add(c)
        if is_total(c, n):
            continue
        moves = optimal_children(canon, vals, c, n)
        if rng is not None:
            rng.shuffle(moves)
        if tie == "last":
            moves = list(reversed(moves))
        _, a, b = moves[0]
        stack.append(a)
        stack.append(b)
    return len(seen)


def exact_min_quotient_dag_size(canon, vals, n, upper_bound=None):
    """Exhaustively minimize canonical-state count over optimal policies.

    This is an exact search only for small n. A policy assigns one optimal
    move to each reachable isomorphism class. The recursion processes the
    largest remaining F-value first; every transition strictly lowers F, so
    once a class is processed no later choice can add a predecessor to it.
    `memo` identifies equal partial reachable/assigned policy states.
    """
    root = canon((0,) * n)
    if upper_bound is None:
        upper_bound = quotient_dag_size(canon, vals, n)
    best = [upper_bound]
    memo = set()

    def search(reachable, chosen):
        if len(reachable) >= best[0]:
            return
        pending = [c for c in reachable
                   if not is_total(c, n) and c not in chosen]
        if not pending:
            best[0] = min(best[0], len(reachable))
            return

        # Since F drops strictly on each edge, all possible predecessors of
        # the selected maximum-F state have already been assigned.
        c = max(pending, key=lambda state: vals[state])
        key = (frozenset(reachable), frozenset(chosen.items()))
        if key in memo:
            return
        memo.add(key)

        for move in optimal_children(canon, vals, c, n):
            _, a, b = move
            search(reachable | {a, b}, {**chosen, c: move})

    search({root}, {})
    return best[0], len(memo)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--max-n", type=int, default=7)
    ap.add_argument("--trials", type=int, default=20)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--exact-through", type=int, default=0,
                    help="also exhaustively minimize quotient DAG for n up to this value")
    args = ap.parse_args()

    rng = random.Random(args.seed)
    print("n | S(n) | lower S(n)+1 | greedy(1st) | greedy(last) | "
          f"random[{args.trials}] min-max | 2*n!-1 (labelled tree)")
    print("-" * 110)
    for n in range(1, args.max_n + 1):
        canon, vals = solve_canonical(n)
        s = vals[canon((0,) * n)]
        q_first = quotient_dag_size(canon, vals, n, tie="first")
        q_last = quotient_dag_size(canon, vals, n, tie="last")
        qs = [quotient_dag_size(canon, vals, n, tie="rand", rng=rng)
              for _ in range(args.trials)]
        import math
        tree = 2 * math.factorial(n) - 1
        print(f"{n} | {s} | {s + 1} | {q_first} | {q_last} | "
              f"{min(qs)}-{max(qs)} | {tree}")
        if args.exact_through and n <= args.exact_through:
            exact, states = exact_min_quotient_dag_size(
                canon, vals, n, upper_bound=min([q_first, q_last] + qs))
            print(f"  exact quotient minimum={exact} (search states={states})")


if __name__ == "__main__":
    main()
