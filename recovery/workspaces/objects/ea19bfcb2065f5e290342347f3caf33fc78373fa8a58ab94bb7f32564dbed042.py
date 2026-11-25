#!/usr/bin/env python3
"""SoringP1 #301 - canonical height-S(n) strategy DP: n <= 6 verification.

Reference model (scripts/strategy_dag_probe.py, docs/upper-bound.md):
  State: transitively closed partial order on n labelled keys, represented
  as successor bitmasks: succ[i] has bit j set iff i < j.
  F(P) = 0                                              if P is total,
  F(P) = 1 + min_{(i,j) incomparable} max(F(P+i<j), F(P+j<i))  otherwise.
  S(n) = F(empty).

Canonical strategy (per SinglePolicyDAG in the probe): at a non-total state
P, choose the lexicographically smallest optimal pair (the first optimal
move of the probe's DAG builder).

Verification per n (0..6):
  DP  : memoized minimax via minimax_values(); check the table satisfies the
        defining recurrence on every reachable poset (self-consistency).
  DPs : simulate the canonical strategy from the empty poset (adversary
        worst case); at every visited state the canonical pair is optimal;
        walk ends at a total poset; worst-case height == F(empty).
  BF1 : naive brute force - pure tree enumeration, no memoization (n <= 5).
  BF2 : attractor fixpoint from scratch, n <= 5.
  CHK : attractor-equation consistency of the DP table vs game values.
  Cross-checks: F(empty) == KNOWN[n]; DP visits exactly the labelled posets
  on n elements (OEIS A001035).
"""

import sys
import time

sys.path.insert(0, "/home/lubko/soring301/scripts")

from strategy_dag_probe import (
    extend,
    incomparable_pairs,
    is_total,
    KNOWN,
    minimax_values,
)

A001035 = {0: 1, 1: 1, 2: 3, 3: 19, 4: 219, 5: 4231, 6: 130023}

BF_MAX_N = 5  # naive tree enumeration is exponential; DP + attractor cover n = 6


def optimal_pairs(n, P, values):
    """Incomparable pairs (i,j) at P whose branches achieve the DP value F(P)."""
    f = values[P]
    out = []
    for (i, j) in incomparable_pairs(P, n):
        a = extend(P, i, j)
        b = extend(P, j, i)
        if 1 + max(values[a], values[b]) == f:
            out.append((i, j))
    return out


def check_dp_recurrence(n, values):
    """Every reachable poset must satisfy F = 0 iff total, and
    F = 1 + min_{(i,j) incomparable} max(F(P+ij), F(P+ji))."""
    bad = []
    for P in values:
        f = values[P]
        if is_total(P, n):
            if f != 0:
                bad.append((P, f, "total but F != 0"))
            continue
        if f <= 0:
            bad.append((P, f, "non-total with F <= 0"))
            continue
        # probe: F(P) = 1 + min_{(i,j) incomparable} max(F(P+ij), F(P+ji))
        cand_max = [max(values[extend(P, i, j)], values[extend(P, j, i)])
                    for (i, j) in incomparable_pairs(P, n)]
        if not cand_max or 1 + min(cand_max) != f:
            bad.append((P, f, "non-total: F != 1+min max(children)"))
    return bad


def check_attractor_equation(n, values):
    """Attractor semantics of the DP values.

    A_0 = {total posets}; A_{d+1} = A_d U {P not in A_d : exists incomparable
    (i,j) with P+ij in A_d and P+ji in A_d}.
    Claim checked: A_d == {P : F(P) <= d} for every d = 0..S(n).
    """
    S = values[(0,) * n]
    bad = []
    A = {P for P in values if is_total(P, n)}
    for d in range(0, S + 1):
        expected = {P for P in values if values[P] <= d}
        if A != expected:
            bad.append((d, "A_d != {F <= d}", len(A), len(expected)))
            break
        # A_{d+1} = A_d U Win(A_d); Win uses only A_d (not the growing set).
        Win = set()
        for P in values:
            if P in A:
                continue
            for (i, j) in incomparable_pairs(P, n):
                if extend(P, i, j) in A and extend(P, j, i) in A:
                    Win.add(P)
                    break
        A = A | Win
    return bad


def canon_sim(n, values):
    """Simulate the canonical strategy from the empty poset (adversary picks
    the worse branch). Returns the number of steps until a total poset."""
    P = (0,) * n
    steps = 0
    empty = (0,) * n
    while not is_total(P, n):
        pairs = optimal_pairs(n, P, values)
        assert pairs, "canonical state has no optimal pair"
        m = min(pairs)  # lexicographically smallest optimal pair
        assert m in incomparable_pairs(P, n), "canonical move not incomparable"
        a = extend(P, m[0], m[1])
        b = extend(P, m[1], m[0])
        assert 1 + max(values[a], values[b]) == values[P], \
            "canonical pair not optimal"
        # adversary worst case: the branch with the larger DP value
        P = a if values[a] >= values[b] else b
        steps += 1
        if steps > 3 * values[empty] + 10:
            raise AssertionError("canonical strategy diverges")
    return steps


def attractor_from_scratch(n, deadline=None):
    """Independent brute force of the minimax height.

    W_0 = {total posets}; W_{d+1} = W_d U {P not in W_d : exists
    incomparable (i,j) with P+ij in W_d and P+ji in W_d}.
    Return least d such that the empty poset is in W_d.
    """
    t_start = time.time()
    empty = (0,) * n
    reach = set()
    stack = [empty]
    while stack:
        P = stack.pop()
        if P in reach:
            continue
        reach.add(P)
        for (i, j) in incomparable_pairs(P, n):
            stack.append(extend(P, i, j))
            stack.append(extend(P, j, i))
    W = {P for P in reach if is_total(P, n)}
    d = 0
    while empty not in W:
        add = set()
        for P in reach:
            if P in W:
                continue
            for (i, j) in incomparable_pairs(P, n):
                if extend(P, i, j) in W and extend(P, j, i) in W:
                    add.add(P)
                    break
        if not add:
            raise RuntimeError(f"attractor stuck at depth {d}")
        W |= add
        d += 1
        if deadline is not None and time.time() - t_start > deadline:
            return None, len(reach), f"deadline({deadline}s) at depth {d}"
    return d, len(reach), ""


def bf_tree_enum(n, P, budget, counter):
    """Pure brute force: enumerate decision trees, no memoization.
    Returns the minimal height of a correct continuation from P
    within budget, or None if none exists."""
    counter[0] += 1
    if is_total(P, n):
        return 0
    if budget <= 0:
        return None
    best = None
    for (i, j) in incomparable_pairs(P, n):
        a = bf_tree_enum(n, extend(P, i, j), budget - 1, counter)
        if a is None:
            continue
        b = bf_tree_enum(n, extend(P, j, i), budget - 1, counter)
        if b is None:
            continue
        h = 1 + max(a, b)
        if best is None or h < best:
            best = h
    return best


def bf_S(n, max_budget=None):
    empty = (0,) * n
    if max_budget is None:
        max_budget = KNOWN.get(n, 15) + 3
    for d in range(0, max_budget + 1):
        counter = [0]
        r = bf_tree_enum(n, empty, d, counter)
        if r is not None:
            return d, counter[0]
    return None, None


def main():
    t_all = time.time()
    print("SoringP1 #301: canonical height-S(n) strategy DP - verification n <= 6")
    print("reference: scripts/strategy_dag_probe.py minimax_values; KNOWN table")
    print()
    hdr = (f"{'n':>2} | {'S_dp':>4} | {'KNOWN':>5} | {'reach':>6} | "
           f"{'BF1':>4} | {'nodes':>9} | {'BF2':>4} | {'canonH':>6}")
    print(hdr)
    print("-" * len(hdr))
    for n in range(0, 7):
        t0 = time.time()
        values = minimax_values(n)
        t_dp = time.time() - t0
        empty = (0,) * n
        S_dp = values[empty]
        n_reach = len(values)

        bad = check_dp_recurrence(n, values)
        bad_chk = check_attractor_equation(n, values)
        steps = canon_sim(n, values)
        assert steps == S_dp, f"canonical height {steps} != F(empty) {S_dp}"

        if n <= BF_MAX_N:
            t0 = time.time()
            bfS, nodes = bf_S(n)
            t_bf = time.time() - t0
        else:
            bfS, nodes, t_bf = None, None, None

        t0 = time.time()
        d_attr, reach_attr, d_note = attractor_from_scratch(
            n, deadline=150 if n >= 6 else 60)
        t_attr = time.time() - t0

        line = (f"{n:>2} | {S_dp:>4} | {KNOWN.get(n, '-'):>5} | {n_reach:>6} | "
                f"{str(bfS) if bfS is not None else '-':>4} | "
                f"{str(nodes) if nodes is not None else '-':>9} | "
                f"{str(d_attr) if isinstance(d_attr, int) else '-':>4} | {steps:>6}")
        checks = []
        checks.append(f"dp_rec:{'OK' if not bad else 'BAD'}")
        checks.append(f"attr_eq:{'OK' if not bad_chk else 'BAD'}")
        if n in KNOWN:
            checks.append(f"KNOWN_ok:{KNOWN[n] == S_dp}")
        checks.append(f"reach_ok:{n_reach == A001035[n]}")
        if bfS is not None:
            checks.append(f"BF1_ok:{bfS == S_dp}")
        elif n <= BF_MAX_N:
            checks.append("BF1_failed")
        else:
            checks.append("BF1_n/a(n>5)")
        if isinstance(d_attr, int):
            checks.append(f"attractor_ok:{d_attr == S_dp}")
        elif d_attr is None:
            checks.append(f"attractor:{d_note}")
        print(line + " | " + " ".join(checks))
        print(f"    (times: DP {t_dp:.2f}s, BF1 {t_bf if t_bf is not None else 0:.2f}s,"
              f" BF2 {t_attr:.2f}s)")
    print()
    print(f"total time: {time.time() - t_all:.2f}s")


if __name__ == "__main__":
    main()
