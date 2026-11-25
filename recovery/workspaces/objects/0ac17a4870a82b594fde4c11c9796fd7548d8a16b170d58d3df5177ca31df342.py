#!/usr/bin/env python3
"""Cross-check L1(R_t) using the repository's own scripts/one_ply_obstruction.py.

Read-only import; no repo changes. Converts my predecessor-mask construction to
the repo's successor-mask representation and calls its L1/L0 directly.
"""
import importlib.util
import sys

REPO = "/home/lubko/soring-fronts/r3-exact-minimax-20261110"
spec = importlib.util.spec_from_file_location(
    "one_ply_obstruction", f"{REPO}/scripts/one_ply_obstruction.py")
opo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(opo)

sys.path.insert(0, "/home/lubko/soring-fronts/r3-oneply-bound-20261110")
from r3_l1 import build_R


def pred_to_succ(pred, n):
    succ = [0] * n
    for i in range(n):
        bits = pred[i]
        while bits:
            low = bits & -bits
            u = low.bit_length() - 1
            succ[u] |= 1 << i
            bits ^= low
    return tuple(succ)


def main():
    for t in (1, 2, 3):
        n, pred = build_R(t)
        succ = pred_to_succ(pred, n)
        # verify conversion by comparing e from both implementations
        e_repo = opo.linear_extensions(succ)
        e_mine = None
        from r3_l1 import e_dp
        e_mine = e_dp(pred, n)
        l0 = opo.L0(succ)
        l1 = opo.L1(succ)
        print(f"R_{t}: repo e={e_repo}, my e={e_mine}, match={e_repo == e_mine}; "
              f"repo L0={l0}, repo L1={l1}")
        assert e_repo == e_mine
    # R_4 too (repo DP is O(2^n), n=14 -> 16384 subsets per call; fine)
    n, pred = build_R(4)
    succ = pred_to_succ(pred, n)
    print(f"R_4: repo e={opo.linear_extensions(succ)}, repo L0={opo.L0(succ)}, "
          f"repo L1={opo.L1(succ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
