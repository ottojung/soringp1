#!/usr/bin/env python3
"""Test the potential/Lyapunov certificate framework for unary SORT-BOUND-U.

A descent potential Phi: Posets -> N is a YES-certificate primitive:
  - Phi(total order) = 0
  - for every non-total P, some incomparable pair {x,y} has
    max(Phi(P+x<y), Phi(P+y<x)) <= Phi(P) - 1   (the "descent" property)
  - Phi(antichain) <= k
Following the descent comparisons yields a sorting strategy of height <= Phi(antichain),
so Phi(antichain) >= S(n) for any descent potential, with equality iff Phi = F (the
minimax value).  Hence a descent potential with Phi(antichain) <= k exists  <=>  S(n) <= k.

This script tests, for small n, three candidate potentials:
  Phi_0(P) = #incomparable pairs          (poly-time, descent, loose)
  Phi_1(P) = ceil(log2 e(P))              (the information bound; NOT always descent)
  F(P)     = minimax value                 (tight descent potential; exponential)
and verifies the minimality F <= Phi_0.
"""

from __future__ import annotations

import math
import sys
from functools import lru_cache


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


def predecessors(succ):
    n = len(succ)
    pred = [0] * n
    for i in range(n):
        for j in range(n):
            if (succ[i] >> j) & 1:
                pred[j] |= 1 << i
    return pred


@lru_cache(maxsize=None)
def linear_extensions(succ):
    n = len(succ)
    pred = predecessors(succ)
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


@lru_cache(maxsize=None)
def minimax(succ):
    pairs = incomparable_pairs(succ)
    if not pairs:
        return 0
    return 1 + min(
        max(minimax(add_relation(succ, i, j)), minimax(add_relation(succ, j, i)))
        for i, j in pairs
    )


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


def phi0(succ):
    return len(incomparable_pairs(succ))


def phi1(succ):
    e = linear_extensions(succ)
    return (e - 1).bit_length()  # ceil(log2 e) for e >= 1


def is_descent_potential(n, phi):
    """Check descent for every non-total poset.  Returns (ok, num_failures, witness)."""
    failures = 0
    witness = None
    for P in all_posets(n):
        if not incomparable_pairs(P):
            continue
        v = phi(P)
        ok = False
        for i, j in incomparable_pairs(P):
            a = add_relation(P, i, j)
            b = add_relation(P, j, i)
            if max(phi(a), phi(b)) <= v - 1:
                ok = True
                break
        if not ok:
            failures += 1
            if witness is None:
                witness = P
    return failures == 0, failures, witness


def main():
    ns = [int(x) for x in sys.argv[1:]] or [5]
    for n in ns:
        print(f"\n===== n = {n} =====")
        empty = (0,) * n
        S_n = minimax(empty)
        print(f"S(n) = F(antichain) = {S_n}")
        print(f"Phi_0(antichain) = {phi0(empty)}  (= n(n-1)/2 = {n*(n-1)//2})")
        print(f"Phi_1(antichain) = {phi1(empty)}  (= ceil(log2 n!) = {(math.factorial(n)-1).bit_length()})")

        # Descent tests
        for name, phi in [("Phi_0 (#incomparable)", phi0), ("Phi_1 (ceil log2 e)", phi1), ("F (minimax)", minimax)]:
            ok, fails, wit = is_descent_potential(n, phi)
            status = "DESCENT OK" if ok else f"NOT descent ({fails} failures)"
            print(f"  {name:24s}: {status}")
            if not ok and wit is not None:
                print(f"      smallest witness succ = {wit}, e = {linear_extensions(wit)}, F = {minimax(wit)}, Phi_1 = {phi1(wit)}")

        # Minimality: F <= Phi_0 everywhere?
        leq = all(minimax(P) <= phi0(P) for P in all_posets(n))
        print(f"  F <= Phi_0 everywhere: {leq}")
        # Info bound: Phi_1 <= F everywhere?
        ib = all(phi1(P) <= minimax(P) for P in all_posets(n))
        print(f"  Phi_1 <= F everywhere (info bound): {ib}")


if __name__ == "__main__":
    main()
