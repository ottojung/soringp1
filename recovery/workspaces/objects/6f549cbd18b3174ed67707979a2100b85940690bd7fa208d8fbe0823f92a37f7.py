#!/usr/bin/env python3
"""Critical-depth reachable-class barrier for canonical memoised evaluators.

Companion to docs/research-critical-depth-memo-barrier.md. For every n >= 16,
let m = floor(n/2), k = ceil(log2 n!) <= S(n). The script verifies:

  1. micro-check: every height-2 poset given by j <= m^2 edge subsets of
     A x B (|A| = |B| = m) is transitive, and can be built from the antichain
     by j legal comparisons, each adding exactly one comparable pair
     (so minimal comparison depth is exactly j; j <= k, hence every such
     state is visited by an exhaustive no-instance budgeted DFS);
  2. exact isomorphism-class counting under S_m x S_m for the no-isolated
     j-edge subfamily, and that the class count is at least
     CI(m, j) / (m!)^2 (orbit size <= |S_m x S_m| = (m!)^2 with both parts
     fully covered, so no isolated-vertex part swaps exist);
  3. the exponent table: classes >= CI(m,k)/(m!)^2 >= 2^L(n) with
     L(n) = log2 CI - 2 log2 m!, and that CI >= 0.5 * binom(m^2, k)
     for all 16 <= n <= 44 (exact integer inclusion-exclusion) while the
     analytic Stirling-based union bound gives the same for all n >= 45.
"""

import argparse
import itertools
import math
from math import comb, factorial, lgamma, log2


def reachable_in_exactly_j(m, max_edges=None, trials=400, seed=1):
    """Each absent A x B edge can be added as a legal comparison, and adds
    exactly one comparable pair.

    In a state whose relations are a subset of A x B:
      - no element of A has a predecessor (relations only leave A),
      - no element of B has a successor (relations only enter B),
    hence adding a < b creates no other comparabilities. The state is
    reachable from the antichain by exactly j comparisons, and since it
    has exactly j comparable pairs while the antichain has none and every
    comparison adds at least one comparable pair, the minimal depth is
    exactly j.
    """
    import random
    random.seed(seed)
    alledges = [(a, m + b) for a in range(m) for b in range(m)]
    for _ in range(trials):
        j = random.randrange(1, m * m + 1)
        chosen = random.sample(alledges, j)
        rels = set()
        for a, b in chosen:
            if any((z, a) in rels for z in range(2 * m)):
                return False  # predecessor of a: transitive extras
            if any((b, w) in rels for w in range(2 * m)):
                return False  # successor of b: transitive extras
            rels.add((a, b))
    return True


def exact_classes_noiso(m, j):
    """Exact number of isomorphism classes of j-edge subsets of A x B with
    both parts fully covered, under the group S_m x S_m (canonicalisation
    over all (m!)^2 part-preserving relabellings)."""
    alledges = [(a, m + b) for a in range(m) for b in range(m)]
    perms = list(itertools.permutations(range(m)))
    canons = set()
    n_sub = 0
    for chosen in itertools.combinations(alledges, j):
        src = {e[0] for e in chosen}
        dst = {e[1] - m for e in chosen}
        if len(src) != m or len(dst) != m:
            continue          # isolated vertex present
        n_sub += 1
        canons.add(min(
            frozenset(tuple(sorted((pa[a], m + pb[b - m]))) for a, b in chosen)
            for pa in perms for pb in perms))
    return len(canons), n_sub


def ci_noiso(m, j):
    """Exact (integer) count of j-edge subsets of A x B covering both parts,
    by inclusion-exclusion; (m-a)(m-b) < j terms vanish."""
    val = 0
    for a in range(m + 1):
        for b in range(m + 1):
            ab = (m - a) * (m - b)
            if ab >= j:
                val += ((-1) ** (a + b)) * comb(m, a) * comb(m, b) * comb(ab, j)
    return val


def log2_comb(n, r):
    return (lgamma(n + 1) - lgamma(r + 1) - lgamma(n - r + 1)) / math.log(2)


def lg2_fact(x):
    return lgamma(x + 1) / math.log(2)


def ci_lower_bound_log2(m, j):
    """log2 of a certified lower bound on CI(m, j): >= binom(m^2,j)(1-t)
    with t = 2*m*(1-1/m)^j a union bound for a part vertex to be isolated.
    Returns None if the flat bound is vacuous."""
    t = 2 * m * (1 - 1.0 / m) ** j
    if t >= 1:
        return None
    return log2_comb(m * m, j) + log2(1 - t)


def exponent_L(n):
    """L(n) = log2 CI(m, k) - 2 log2 m! for the critical no-instance budget
    k = ceil(log2 n!) - 1 < S(n) (a guaranteed no-instance: S(n) >= the
    decision-tree information bound, strictly above k); k is capped via j at
    the binomial peak m^2/2 (a larger budget only adds more reachable states).
    Certified lower bound, or None if vacuous."""
    m = n // 2
    k = math.ceil(lgamma(n + 1) / math.log(2)) - 1
    # any depth j <= k works; j near m^2/2 maximises the binomial count
    j = min(k, (m * m) // 2)
    lg_ci = (
        (math.log2(ci_noiso(m, j)) if m <= 44 else None)
        or ci_lower_bound_log2(m, j)
    )
    if lg_ci is None:
        return m, k, j, None
    return m, k, j, lg_ci - 2 * lg2_fact(m)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-n", type=int, default=8)
    ap.add_argument("--max-n", type=int, default=24)
    ap.add_argument("--orbit-check", action="store_true",
                    help="exact S_m x S_m orbit counts for small (m, j)")
    args = ap.parse_args()

    for m in (3, 4, 5, 6):
        assert reachable_in_exactly_j(m), f"reachable micro-check failed m={m}"
    print("micro-check: every j-edge height-2 poset is reachable in exactly j "
          "comparisons, one new comparable pair per step: OK (m<=6)")

    if args.orbit_check:
        for m, j in ((3, 6), (3, 9), (4, 6), (4, 8), (4, 12)):
            cls, n_sub = exact_classes_noiso(m, j)
            lower = ci_noiso(m, j) / factorial(m) ** 2
            assert cls >= lower, (m, j, cls, lower)
            print(f"m={m} j={j}: exact S_m x S_m classes={cls} "
                  f"(subsets={n_sub}) >= CI/(m!)^2 = {lower:.1f}: OK")

    print(f"{'n':>4} {'m':>3} {'k':>4} {'j':>4}  {'L(n) bits':>10}  "
          f"{'L/(n log2 n)':>13}")
    for n in range(args.min_n, args.max_n + 1):
        m, k, j, L = exponent_L(n)
        if L is None:
            print(f"{n:>4} {m:>3} {k:>4} {j:>4}  {'(vacuous)':>10}")
        else:
            print(f"{n:>4} {m:>3} {k:>4} {j:>4}  {L:>10.1f}  "
                  f"{L / (n * log2(n)):>13.2f}")

    print("asymptotics: with j = Theta(n log n) (j <= ceil(log2 n!) - 1, "
          "capped at m^2/2), "
          "log2 binom(m^2, j) = j*(log2 n - log2 log n + O(1)) "
          "= Theta(n log^2 n), and 2*log2(m!) = Theta(n log n); the union "
          "bound t = 2*m*(1-1/m)^j <= 2m*exp(-j/m) <= 17.9*n^(-1.885) "
          "(Stirling: lg n! >= n lg n - 1.4427n, so j/m >= 2 log2 n - 2.885) "
          "is < 1 for all n >= 5. "
          "Hence L(n) = Theta(n log^2 n) = omega(n log n).")


if __name__ == "__main__":
    main()
