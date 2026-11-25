#!/usr/bin/env python3
"""Size of explicit NO certificates for S(n) > k (unary SORT-BOUND-U).

Scratch experiment for research/unary-conp-nocert-20261020.  Model (from
docs/problem.md, docs/research-certificates-barriers.md):

  SORT-BOUND-U = {1^n # 1^k : S(n) <= k}, unary input length N = n+k+1.
  State = transitively closed strict partial order on [n] (successor bitmasks).
  F(P) = 0 if total, else 1 + min over incomparable {i,j}
         max(F(P+i<j), F(P+j<i));  F(antichain_n) = S(n).

A *NO certificate* for (n,k) (an adversary policy / barrier) is an explicit
closed adversary-strategy DAG:

  S  = finite set of NON-TOTAL posets containing the antichain A_n;
  sigma(P,{x,y}) = chosen outcome child (total, or non-total in S)
                   for every P in S and every incomparable pair {x,y};
  S closed: every non-total child is in S;
  rank R(P) = 0 if total, else 1 + min_{pairs} R(sigma(P,pair));
  certificate valid  <=>  R(A_n) > k.

Verification of an explicit (S,sigma) is O(|S| * n^2 * poly(n)).  The
question is whether a winning certificate with |S| = poly(N) can exist.

This script computes, for small n and k = S(n)-1 (the hardest NO instance):
  * |reach| = size of the closure S under the *optimal* adversary
    sigma(P,pair) = argmax_o F(P_o)  (the unique optimal policy up to ties);
  * |reach_e| = closure under the *information* adversary argmax_o e(P_o);
  * the number of labelled posets with F(P) > j for j = 0..S(n)-1;
  * the number of labelled posets with comparison-depth <= d (d = S(n)-1);
  * the "forced" sorter-reachable count (all posets reachable under *any*
    adversary policy within k steps), a lower bound on |S| for any explicit
    certificate, computed as the set of posets with cover-count <= k.

No complexity-class claim is made here.
"""

from __future__ import annotations

import sys
from functools import lru_cache


# ---------------------------------------------------------------- poset utils

def add_relation(succ, i, j):
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(len(succ)):
        if x == i or (succ[x] >> i) & 1:
            out[x] |= new_greater
    return tuple(out)


def incomparable_pairs(succ):
    n = len(succ)
    return [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if not (succ[i] >> j) & 1 and not (succ[j] >> i) & 1
    ]


def is_total(succ):
    return not incomparable_pairs(succ)


@lru_cache(maxsize=None)
def linear_extensions(succ):
    n = len(succ)
    full = (1 << n) - 1
    dp = [0] * (1 << n)
    dp[0] = 1
    for S in range(1, 1 << n):
        total = 0
        m = S
        while m:
            x = (m & -m).bit_length() - 1
            m &= m - 1
            if succ[x] & (S ^ (1 << x)) == 0:
                total += dp[S ^ (1 << x)]
        dp[S] = total
    return dp[full]


def all_posets(n):
    start = (0,) * n
    seen = {start}
    stack = [start]
    while stack:
        s = stack.pop()
        for i, j in incomparable_pairs(s):
            for t in (add_relation(s, i, j), add_relation(s, j, i)):
                if t not in seen:
                    seen.add(t)
                    stack.append(t)
    return seen


@lru_cache(maxsize=None)
def minimax(succ):
    pairs = incomparable_pairs(succ)
    if not pairs:
        return 0
    return 1 + min(
        max(minimax(add_relation(succ, i, j)), minimax(add_relation(succ, j, i)))
        for i, j in pairs
    )


# ------------------------------------------------------- adversary policies

def policy_closure(n, key):
    """Closure S of A_n under the adversary policy argmax_o key(P_o).

    key(P) is a numeric "value"; ties broken by (key, succ) deterministically.
    Returns (S, rank_root) where rank is computed on the closed set.
    """
    A = (0,) * n
    S = set()
    frontier = [A]
    parent_children = {}  # P -> list of chosen children
    while frontier:
        P = frontier.pop()
        if P in S or is_total(P):
            continue
        S.add(P)
        kids = []
        for i, j in incomparable_pairs(P):
            a = add_relation(P, i, j)
            b = add_relation(P, j, i)
            # choose outcome maximising key (adversary keeps the harder side)
            if (key(a), a) >= (key(b), b):
                kid = a
            else:
                kid = b
            kids.append(kid)
            if not is_total(kid) and kid not in S:
                frontier.append(kid)
        parent_children[P] = kids

    # rank by DP (S closed under chosen children)
    rank = {}

    def R(P):
        if is_total(P):
            return 0
        if P in rank:
            return rank[P]
        rank[P] = 1  # placeholder to break cycles (none should occur)
        best = None
        for kid in parent_children[P]:
            v = R(kid)
            if best is None or v < best:
                best = v
        rank[P] = 1 + (best if best is not None else 0)
        return rank[P]

    root_rank = R(A)
    return S, root_rank


def forced_reachable_count(n, k):
    """Number of posets reachable from A_n by <= k comparisons under ANY
    adversary policy = number of posets whose transitive reduction (cover
    count) is <= k.  This is a lower bound on |S| for any explicit NO
    certificate that must contain the sorter-reachable states.

    NOTE: the sorter cannot force an arbitrary cover set (the adversary picks
    outcomes), so this is an upper bound on the *forced* reachable set in the
    game; we report it as the "static" bound and discuss the gap in the note.
    """
    cnt = 0
    for P in all_posets(n):
        if cover_count(P) <= k:
            cnt += 1
    return cnt


def cover_count(succ):
    """Number of cover relations (transitive-reduction edges)."""
    n = len(succ)
    c = 0
    for i in range(n):
        for j in range(n):
            if (succ[i] >> j) & 1:
                # is (i,j) a cover? no k with i<k<j
                if succ[i] & (succ[j] | (1 << j)):
                    # there is an intermediate k
                    mid = succ[i] & ~(1 << j)
                    # intermediate if some k with i<k and k<j
                    if any((succ[i] >> kk) & 1 and (succ[kk] >> j) & 1
                           for kk in range(n)):
                        continue
                c += 1
    return c


def main():
    maxn = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print(f"{'n':>3} {'S(n)':>5} {'k':>5} {'|reach_F|':>10} "
          f"{'|reach_e|':>10} {'forced<=k':>10} {'#F>k':>8} {'N':>5}")
    for n in range(2, maxn + 1):
        posets = all_posets(n)
        S_n = minimax((0,) * n)
        k = S_n - 1
        SF, rF = policy_closure(n, minimax)
        SE, rE = policy_closure(n, linear_extensions)
        forced = forced_reachable_count(n, k)
        fgt = sum(1 for P in posets if minimax(P) > k)
        N = n + k + 1
        print(f"{n:>3} {S_n:>5} {k:>5} {len(SF):>10} {len(SE):>10} "
              f"{forced:>10} {fgt:>8} {N:>5}")
        # sanity: rank root should equal S(n)
        assert rF == S_n, (n, rF, S_n)


if __name__ == "__main__":
    main()
