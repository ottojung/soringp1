#!/usr/bin/env python3
"""Enumerate isomorphism classes of posets with e(P) <= E and |P| <= N, then check
that every *core* (no element comparable with all others) has minimax depth <= R.

Usage: python3 run_core_sets.py E N R [--quiet]

The core reduction (docs/research-core-reduction.md) says T(R) >= E iff every core
with e <= E has minimax depth <= R, so `E N R` with N >= E certifies T(R) >= E when
no bad core is reported.

e(P) never decreases when an element is adjoined, so pruning branches with e > E is
sound and complete for this task.
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core_sets as cs


def main(argv):
    if len(argv) < 4:
        print(__doc__)
        return 2
    E, N, R = int(argv[1]), int(argv[2]), int(argv[3])
    quiet = '--quiet' in argv[4:]
    t0 = time.time()

    def report(n, count, start):
        if not quiet:
            print('n=%2d classes=%6d  [%.1fs]' % (n, count, time.time() - start), flush=True)

    levels = cs.enumerate_levels(E, N, t0, report)
    worst = []
    total = 0
    if not quiet:
        print('--- core check ---', flush=True)
    for n in sorted(levels):
        if n < 2:
            continue
        cores = [(up, ex) for (up, ex) in levels[n].values() if cs.is_core(up, n)]
        mx = 0
        for up, ex in cores:
            m = cs.minimax(ex)
            mx = max(mx, m)
            if m > R:
                worst.append((n, len(ex), m, up))
        total += len(cores)
        if not quiet:
            print('n=%2d classes=%6d cores=%5d max_m=%d' % (n, len(levels[n]), len(cores), mx), flush=True)
    print('E=%d N=%d R=%d total_cores=%d bad_cores=%d elapsed=%.1fs'
          % (E, N, R, total, len(worst), time.time() - t0))
    for bad in worst[:10]:
        print('  BAD n=%d e=%d m=%d up=%r' % bad)
    return 0 if not worst else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
