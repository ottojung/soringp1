#!/usr/bin/env python3
"""Emit per-block data (per-insertion records) for n = 2..40 and the
straggler equality counts, as reproducible artifacts."""
import csv
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from instrument import fj_sort_instr, jac, q_of, ceil_log2_frac, NMAX  # noqa

HERE = os.path.dirname(os.path.abspath(__file__))
J = jac(10000)

out_csv = os.path.join(HERE, "per_block.csv")
with open(out_csv, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["n", "mode", "i", "q", "m", "mmax", "L", "straggler",
                "cost", "p"])
    for n in range(2, NMAX + 1):
        for mode in ("actual", "worst"):
            _ch, recs, _t = fj_sort_instr(list(range(n, 0, -1)), J, mode)
            for (i, q, m, mmax, L, sg, cost, p) in recs:
                w.writerow([n, mode, i, q, m, mmax, L, int(sg), cost, p])
print("wrote", out_csv)

# per-block aggregate (worst mode) for the doc table
cnt_eq = cnt_le = 0
straggler_rows = []
for n in range(3, 401, 2):
    k = n // 2
    K = k + 1
    _ch, recs, _t = fj_sort_instr(list(range(n, 0, -1)), J, "worst")
    i, q, m, mmax, L, sg, cost, p = [r for r in recs if r[5]][0]
    bnd = ceil_log2_frac(3 * n)
    if cost == bnd:
        cnt_eq += 1
    if cost <= bnd:
        cnt_le += 1
    straggler_rows.append((n, k, K, q, J[q - 1], L, cost, bnd))
with open(os.path.join(HERE, "straggler_odd400.json"), "w") as fh:
    json.dump([list(map(int, r)) for r in straggler_rows], fh)
print(f"straggler f(L) == ceil(log2(3n/4)): {cnt_eq}/199; "
      f"<= : {cnt_le}/199 (odd n = 3..399)")
