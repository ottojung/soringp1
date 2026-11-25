#!/usr/bin/env python3
"""Standalone capped proof-number/disproof-number search for CanSort(P,d).

Decides the same predicate as scripts/budgeted_dfs.py:can_sort without
changing semantics:

    CanSort(P,d) = True if P total
                 = False if d=0 and not total
                 = exists incomparable (i,j): CanSort(P+i<j,d-1) AND CanSort(P+j<i,d-1)

PNS mapping:
  - root over comparisons q is an OR-node (sorter chooses): proof = min over q,
    disproof = sum over q (every comparison must fail to refute).
  - each chosen comparison is an AND-node (adversary both answers): proof = sum
    of children proofs, disproof = min of children disproofs.

Cap hits are reported as unknown, never as refutation.
"""
import argparse, sys, time
sys.setrecursionlimit(100000)

# reuse helpers from budgeted_dfs
import importlib.util
spec = importlib.util.spec_from_file_location("bfd", "scripts/budgeted_dfs.py")
bfd = importlib.util.module_from_spec(spec); spec.loader.exec_module(bfd)

extend = bfd.extend
incomparable_pairs = bfd.incomparable_pairs
is_total = bfd.is_total


def pn_search(succ, n, d, cap):
    """Return (result, expansions, hit_cap). result True/False/None."""
    # node: (succ,d) ; proof/disproof numbers via DFS with transposition? None here (standalone, no memo).
    expansions = [0]
    # iterative-ish recursive
    def rec(succ, d):
        expansions[0] += 1
        if expansions[0] > cap:
            return None
        if is_total(succ, n):
            return True
        if d == 0:
            return False
        pairs = incomparable_pairs(succ, n)
        if not pairs:
            return True
        # OR over pairs: need at least one pair with both children True
        # Refutation: all pairs have a failing child
        all_fail = True
        for i, j in pairs:
            a = rec(extend(succ, i, j), d - 1)
            if a is None:
                return None
            if not a:
                # this pair's left fails -> pair fails; continue
                continue
            b = rec(extend(succ, j, i), d - 1)
            if b is None:
                return None
            if b:
                return True
            # pair failed on right
        return False
    res = rec(succ, d)
    hit = res is None
    return res, expansions[0], hit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=4)
    ap.add_argument("--d", type=int, default=None)
    ap.add_argument("--cap", type=int, default=10_000_000)
    args = ap.parse_args()
    d = args.d if args.d is not None else None
    # if no d, binary search
    if d is None:
        lo, hi = 0, bfd.merge_sort_upper_bound(args.n)
        total_exp = 0
        t0 = time.perf_counter()
        hit = False
        while lo < hi:
            mid = (lo + hi)//2
            r, e, h = pn_search((0,)*args.n, args.n, mid, args.cap)
            total_exp += e
            if h:
                hit = True; break
            if r:
                hi = mid
            else:
                lo = mid + 1
        dt = time.perf_counter()-t0
        print(f"n={args.n} result={lo}{' (LOWER BOUND, unknown)' if hit else ' (exact)'} expansions={total_exp} time={dt:.3f}s hit_cap={hit}")
    else:
        r, e, h = pn_search((0,)*args.n, args.n, d, args.cap)
        print(f"n={args.n} d={d} result={r} expansions={e} hit_cap={h}")


if __name__ == "__main__":
    main()