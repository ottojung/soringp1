#!/usr/bin/env python3
"""Budgeted depth-first search for the exact sorting number S(n).

Model (see docs/problem.md, docs/upper-bound.md, docs/research-certificates-barriers.md):
  * n distinct labelled keys; a state is the strict partial order (transitive
    closure) induced by the comparisons made so far.
  * S(n) = minimum worst-case number of adaptive pairwise comparisons to sort.
  * Game G(n,k): state = transitively closed poset P; sorter picks an
    incomparable pair {x,y}; adversary answers x<y or y<x; P becomes its
    transitive closure. Sorter wins iff a total order is reached within k
    comparisons. S(n) <= k iff the sorter wins G(n,k).

This script decides the threshold question "S(n) <= k?" by a *pure* DFS
CanSort(P, d) with NO memoization and NO nonuniform advice:

    CanSort(P, d) = True                          if P is total
                 = False                         if d = 0 and P not total
                 = exists incomparable (i,j) s.t. CanSort(P+i<j, d-1)
                                              AND CanSort(P+j<i, d-1)

Correctness is by induction on d (see docs/research-budgeted-dfs.md). The DFS
is uniform, deterministic, and backtracks: it keeps only the current recursion
path on the stack, so space is O(d * n^2) bits, while the worst-case number of
calls is (2 * binom(n,2))^d = 2^{O(d log n)}.

To compute S(n) we binary-search k in [0, U(n)] with the constructive
merge-sort upper bound U(n) = n * ceil(log2(max(2,n))), giving
O(log n) DFS invocations and total deterministic time 2^{O(n log^2 n)}.

This is an experiment, not a proof. It uses no external libraries.
"""

import argparse
import random
import sys
import time

# Prototype guard only: Python's default recursion limit is 1000, which is below
# the budget depth d = U(n) for large n. The proven O(d) space bound is for the
# Turing-machine model, which uses its own explicit stack and is uniform in n;
# this limit is a bounded-prototype convenience, not part of the complexity claim.
sys.setrecursionlimit(100000)


# --------------------------------------------------------------------------
# Partial orders as tuples of successor bitmasks: succ[i] has bit j set iff
# i < j (transitively closed). Matches scripts/evaluate.py.
# --------------------------------------------------------------------------

def extend(succ, i, j):
    """Add i < j to an already transitively closed poset; return closure."""
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
        if not (succ[i] & (1 << j)) and not (succ[j] & (1 << i))
    ]


def is_total(succ, n):
    return all(
        (succ[i] >> j) & 1 or (succ[j] >> i) & 1
        for i in range(n)
        for j in range(i + 1, n)
    )


# --------------------------------------------------------------------------
# Pure budgeted DFS (no memoization, no advice). Counts every call.
# --------------------------------------------------------------------------

def can_sort(succ, n, d, counter, node_cap=None):
    """Return (result, hit_cap). result is True/False; hit_cap is True if the
    node budget was exceeded (result is then a lower-bound approximation)."""
    counter[0] += 1
    if node_cap is not None and counter[0] > node_cap:
        return None, True
    if is_total(succ, n):
        return True, False
    if d == 0:
        return False, False
    for i, j in incomparable_pairs(succ, n):
        a, cap = can_sort(extend(succ, i, j), n, d - 1, counter, node_cap)
        if cap:
            return None, True
        if a:
            b, cap = can_sort(extend(succ, j, i), n, d - 1, counter, node_cap)
            if cap:
                return None, True
            if b:
                return True, False
    return False, False


def ceil_log2(n):
    """Exact integer ceil(log2(n)) for n >= 1, no floating point."""
    if n <= 1:
        return 0
    return (n - 1).bit_length()


def merge_sort_upper_bound(n):
    """U(n) = n * ceil(log2(max(2,n))); a valid merge-sort upper bound on S(n)."""
    if n <= 1:
        return 0
    return n * ceil_log2(max(2, n))


def compute_s_dfs(n, node_cap=None):
    """Binary search for S(n) using can_sort on the empty poset.
    Returns (value, total_calls, seconds, hit_cap). If hit_cap is True the value
    is a lower bound (unknown exact), never an exact S(n)."""
    if n <= 1:
        return 0, 1, 0.0, False
    lo, hi = 0, merge_sort_upper_bound(n)
    counter = [0]
    t0 = time.perf_counter()
    hit_cap = False
    while lo < hi:
        mid = (lo + hi) // 2
        res, cap = can_sort((0,) * n, n, mid, counter, node_cap)
        if cap:
            hit_cap = True
            break
        if res:
            hi = mid
        else:
            lo = mid + 1
    dt = time.perf_counter() - t0
    return lo, counter[0], dt, hit_cap


# --------------------------------------------------------------------------
# Memoized reference F(P) (from scripts/evaluate.py) for cross-checking.
# --------------------------------------------------------------------------

def memoized_F(n):
    """Return a dict mapping every reachable poset to its F value."""
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


# --------------------------------------------------------------------------
# Adversarial / structured posets for cross-checking can_sort(P,d) == (F(P)<=d).
# --------------------------------------------------------------------------

def antichain(n):
    return (0,) * n


def total_order(n):
    return tuple(sum(1 << j for j in range(i + 1, n)) for i in range(n))


def chain_plus_isolated(n):
    """A chain on n-1 elements plus one isolated element."""
    succ = [0] * n
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            succ[i] |= 1 << j
    return tuple(succ)


def crown(n):
    """Crown poset on n elements (n even): a_i < b_i, a_i < b_{i-1}."""
    if n % 2 != 0:
        raise ValueError("crown needs even n")
    half = n // 2
    succ = [0] * n
    for i in range(half):
        a, b = i, half + i
        succ[a] |= 1 << b
        succ[a] |= 1 << half + (i - 1) % half
    return tuple(succ)


def disjoint_chains(n, k):
    """Disjoint union of k chains as evenly sized as possible."""
    succ = [0] * n
    sizes = [n // k + (1 if i < n % k else 0) for i in range(k)]
    idx = 0
    for s in sizes:
        for a in range(idx, idx + s):
            for b in range(a + 1, idx + s):
                succ[a] |= 1 << b
        idx += s
    return tuple(succ)


def random_poset(n, p, rng):
    """Random DAG-based poset: orient i<j with prob p, take transitive closure."""
    succ = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < p:
                succ[i] |= 1 << j
    # transitive closure (Floyd-Warshall on bitmasks)
    for k in range(n):
        for i in range(n):
            if succ[i] >> k & 1:
                succ[i] |= succ[k]
    return tuple(succ)


# --------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------

def test_values(max_n=5, node_cap=5_000_000):
    """Verify S(n) via DFS binary search against known values / evaluate.py."""
    known = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10}
    print("=== Value test: S(n) via budgeted DFS binary search ===")
    print("n | U(n) | DFS result | known | calls | time(s) | status")
    ok = True
    for n in range(0, max_n + 1):
        val, calls, dt, cap = compute_s_dfs(n, node_cap)
        if cap:
            label = f">= {val} (LOWER BOUND, unknown)"
            match = val <= known[n]
        else:
            label = f"{val} (exact)"
            match = (val == known[n])
        ok = ok and match
        print(f"{n} | {merge_sort_upper_bound(n)} | {label} | {known[n]} | "
              f"{calls} | {dt:.3f} | {'OK' if match else 'FAIL'}")
    return ok


def test_boundary(max_n=5, node_cap=20_000_000):
    """Verify can_sort(empty, S(n))=True and can_sort(empty, S(n)-1)=False."""
    known = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10}
    print("\n=== Boundary test: can_sort(empty, S(n)) / can_sort(empty, S(n)-1) ===")
    print("n | S(n) | can_sort(S(n)) | can_sort(S(n)-1) | calls | time(s) | hit_cap")
    ok = True
    for n in range(2, max_n + 1):
        s = known[n]
        c1 = [0]
        t0 = time.perf_counter()
        r1, cap1 = can_sort((0,) * n, n, s, c1, node_cap)
        dt1 = time.perf_counter() - t0
        c2 = [0]
        t0 = time.perf_counter()
        r2, cap2 = can_sort((0,) * n, n, s - 1, c2, node_cap)
        dt2 = time.perf_counter() - t0
        match = (r1 is True) and (r2 is False) and not cap1 and not cap2
        ok = ok and match
        print(f"{n} | {s} | {r1} | {r2} | {c1[0]+c2[0]} | "
              f"{dt1+dt2:.3f} | {cap1 or cap2} | {'OK' if match else 'FAIL'}")
    return ok


def test_adversarial(max_n=5, node_cap=2_000_000):
    """Cross-check can_sort(P,d) == (F(P) <= d) on structured/random posets."""
    print("\n=== Adversarial poset test: can_sort(P,d) == (F(P) <= d) ===")
    rng = random.Random(20261018)
    ok = True
    total_checks = 0
    for n in range(2, max_n + 1):
        F = memoized_F(n)
        posets = {
            "antichain": antichain(n),
            "total": total_order(n),
            "chain+iso": chain_plus_isolated(n),
            "2-chains": disjoint_chains(n, 2),
            "crown": crown(n) if n % 2 == 0 else None,
        }
        for name, P in posets.items():
            if P is None:
                continue
            fval = F[P]
            for d in range(0, min(fval + 2, merge_sort_upper_bound(n) + 1)):
                counter = [0]
                res, cap = can_sort(P, n, d, counter, node_cap)
                expected = (fval <= d)
                total_checks += 1
                if cap or res != expected:
                    ok = False
                    print(f"  FAIL n={n} {name} d={d}: got {res} (cap={cap}), "
                          f"expected {expected}, F={fval}")
        # random posets
        for _ in range(6):
            P = random_poset(n, rng.choice([0.2, 0.4, 0.6]), rng)
            fval = F[P]
            for d in range(0, min(fval + 2, merge_sort_upper_bound(n) + 1)):
                counter = [0]
                res, cap = can_sort(P, n, d, counter, node_cap)
                expected = (fval <= d)
                total_checks += 1
                if cap or res != expected:
                    ok = False
                    print(f"  FAIL n={n} random d={d}: got {res} (cap={cap}), "
                          f"expected {expected}, F={fval}")
    print(f"  {total_checks} checks across structured and random posets: "
          f"{'ALL OK' if ok else 'FAILURES'}")
    return ok


def measure_call_counts():
    """Measure worst-case call counts for the empty poset at small budgets."""
    print("\n=== Call-count measurement: can_sort(antichain, d) ===")
    print("n | d | binom(n,2) | 2*binom | calls | time(s) | result")
    for n in range(2, 6):
        B = n * (n - 1) // 2
        for d in range(0, min(6, merge_sort_upper_bound(n) + 1)):
            counter = [0]
            t0 = time.perf_counter()
            res, cap = can_sort((0,) * n, n, d, counter, 50_000_000)
            dt = time.perf_counter() - t0
            print(f"{n} | {d} | {B} | {2*B} | {counter[0]} | {dt:.3f} | {res}"
                  f"{' (cap)' if cap else ''}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-n", type=int, default=5)
    ap.add_argument("--node-cap", type=int, default=20_000_000)
    ap.add_argument("--skip-measure", action="store_true")
    args = ap.parse_args()

    ok = True
    ok &= test_values(args.max_n, args.node_cap)
    ok &= test_boundary(args.max_n, args.node_cap)
    ok &= test_adversarial(args.max_n, args.node_cap)
    if not args.skip_measure:
        measure_call_counts()
    print("\n" + ("ALL TESTS PASSED" if ok else "SOME TESTS FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
