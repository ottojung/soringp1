#!/usr/bin/env python3
"""Check F(t C_2 + A_{n-2t}) against the valid bounds M(n)-t and S(n)-t.

See docs/research-prefix-bounds.md. The theorem there proves

    S(n) - t <= F(P_{n,t}) <= M(n) - t,

When S(n)=M(n), the bounds coincide. The converse is not established by those
bounds: in particular t=0 gives F(A_n)=S(n) tautologically. This script
evaluates F(P_{n,t}) exactly (transcript DFS) for small n and all t, and
prints the quantities side by side. It is a finite check, not an all-n proof.

Usage: python3 scripts/prefix_equivalence_check.py [max_n]
"""

import argparse
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from transcript_dfs import can_sort  # noqa: E402


def merge_insertion_bound(n):
    """M(n) = sum_{j=1..n} ceil(log2(3j/4)), computed with integers."""
    total = 0
    for j in range(1, n + 1):
        num, den = 3 * j, 4
        k = 0
        while (1 << k) * den < num:
            k += 1
        total += k
    return total


def exact_f_for_prefix(n, t):
    """Exact F(P_{n,t}) by increasing the budget until the DFS succeeds."""
    transcript = [(2 * i, 2 * i + 1) for i in range(t)]
    budget = 0
    limit = merge_insertion_bound(n) + 1
    while not can_sort(transcript, n, budget):
        budget += 1
        if budget > limit:
            raise RuntimeError("budget exceeded M(n)+1")
    return budget


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("max_n", nargs="?", type=int, default=8)
    args = parser.parse_args()

    # Exact S(n) for the established range; values through 22 are recorded in
    # docs/research-plan.md and docs/literature.md.
    known_s = {1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 9: 19,
               10: 22, 11: 26, 12: 30, 13: 34, 14: 38, 15: 42, 16: 46,
               17: 50, 18: 54, 19: 58, 20: 62, 21: 66, 22: 71}

    failures = 0
    for n in range(2, args.max_n + 1):
        m = merge_insertion_bound(n)
        for t in range(0, n // 2 + 1):
            start = time.time()
            f = exact_f_for_prefix(n, t)
            elapsed = time.time() - start
            s = known_s.get(n)
            # Unknown lower endpoint is reported as unknown, not as passing.
            ok_upper = f <= m - t
            ok_lower = None if s is None else (f >= s - t)
            tight = (s is not None) and f == m - t == s - t
            if not ok_upper or ok_lower is False:
                failures += 1
            print(
                "n=%2d t=%2d F=%3d M-t=%3d S-t=%s upper=%s lower=%s tight=%s (%.1fs)"
                % (
                    n,
                    t,
                    f,
                    m - t,
                    "-" if s is None else s - t,
                    ok_upper,
                    "unknown" if ok_lower is None else ok_lower,
                    tight,
                    elapsed,
                ),
                flush=True,
            )
    print("BOUND FAILURES:", failures)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
