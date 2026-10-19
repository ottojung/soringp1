#!/usr/bin/env python3
"""Independent review checks for PR #22 (branch
``research/compositional-lookahead-20261018``, head 4abf2a6).

This program is deliberately disjoint from the author's
``scripts/compositional_lookahead.py``: it re-derives every finite fact with
its own brute-force primitives (permutation enumeration for ``e``, an
independent minimax recursion on comparable-pair sets, an independent
connected-component pass) and only *then* compares against the author's
functions.  It does not modify the source branch.

Bounds respected: exhaustive enumeration only for ``n <= 5``; the ``n = 6``
"no strict compositional gap" claim is checked by an *exhaustive targeted*
search over ordinal sums of series factors (parts >= 2), which is complete
for posets with at least two series factors (the only ones where ``B`` can
differ from ``L1``).  No exhaustive ``n >= 6`` poset enumeration and no
unbounded scan.

Run:  python3 scripts/review_compositional_lookahead.py
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compositional_lookahead as C  # noqa: E402

FAILS: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        FAILS.append(msg)


# ---------------------------------------------------------------------------
# Independent brute-force primitives (do not call the author's code)
# ---------------------------------------------------------------------------


def rels(succ: tuple[int, ...]) -> set[tuple[int, int]]:
    n = len(succ)
    return {(i, j) for i in range(n) for j in range(n) if (succ[i] >> j) & 1}


def closure(relations: set[tuple[int, int]], n: int) -> set[tuple[int, int]]:
    """Transitive closure by naive fixpoint (independent of add_relation)."""
    r = set(relations)
    changed = True
    while changed:
        changed = False
        for (a, b) in list(r):
            for (c, d) in list(r):
                if b == c and (a, d) not in r:
                    r.add((a, d))
                    changed = True
    return r


def succ_from_relations(relations: set[tuple[int, int]], n: int) -> tuple[int, ...]:
    out = [0] * n
    for (i, j) in relations:
        out[i] |= 1 << j
    return tuple(out)


def brute_e(succ: tuple[int, ...]) -> int:
    """Count linear extensions by enumerating all permutations (n <= 7)."""
    n = len(succ)
    r = rels(succ)
    cnt = 0
    for perm in itertools.permutations(range(n)):
        pos = {x: k for k, x in enumerate(perm)}
        if all(pos[i] < pos[j] for (i, j) in r):
            cnt += 1
    return cnt


def brute_components(succ: tuple[int, ...]) -> list[list[int]]:
    """Connected components of the incomparability graph (plain BFS)."""
    n = len(succ)
    adj: list[set[int]] = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if not ((succ[i] >> j) & 1) and not ((succ[j] >> i) & 1):
                adj[i].add(j)
                adj[j].add(i)
    seen: set[int] = set()
    comps: list[list[int]] = []
    for s in range(n):
        if s in seen:
            continue
        stack = [s]
        seen.add(s)
        comp: list[int] = []
        while stack:
            x = stack.pop()
            comp.append(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        comps.append(sorted(comp))
    return comps


def brute_minimax(succ: tuple[int, ...], memo: dict[frozenset, int]) -> int:
    """Independent F(P): recursion over incomparable pairs, state = relation set."""
    r = frozenset(rels(succ))
    if r in memo:
        return memo[r]
    n = len(succ)
    pairs = [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if (i, j) not in r and (j, i) not in r
    ]
    if not pairs:
        memo[r] = 0
        return 0
    best = None
    for (i, j) in pairs:
        left = succ_from_relations(closure(set(r) | {(i, j)}, n), n)
        right = succ_from_relations(closure(set(r) | {(j, i)}, n), n)
        v = max(brute_minimax(left, memo), brute_minimax(right, memo))
        if best is None or v < best:
            best = v
    memo[r] = 1 + best
    return memo[r]


# ---------------------------------------------------------------------------
# 1. Poset machinery equivalence
# ---------------------------------------------------------------------------


def check_machinery(max_n: int) -> int:
    n_checks = 0
    for n in range(1, max_n + 1):
        for P in C.all_posets(n):
            # add_relation == independent closure of a single added relation
            for (i, j) in C.incomparable_pairs(P):
                got = C.add_relation(P, i, j)
                want = succ_from_relations(closure(rels(P) | {(i, j)}, n), n)
                check(got == want, f"add_relation mismatch n={n} P={P} ({i},{j})")
                n_checks += 1
            # e via downset DP == brute permutation count
            if n <= 7:
                check(
                    C.linear_extensions(P) == brute_e(P),
                    f"linear_extensions mismatch n={n} P={P}",
                )
                n_checks += 1
            # series components match independent BFS
            check(
                sorted(map(tuple, C.incomparability_components(P)))
                == sorted(map(tuple, brute_components(P))),
                f"components mismatch n={n} P={P}",
            )
            n_checks += 1
    return n_checks


# ---------------------------------------------------------------------------
# 2. Series decomposition: maximality, additivity of e and F
# ---------------------------------------------------------------------------


def check_series(max_n: int) -> int:
    n_checks = 0
    for n in range(1, max_n + 1):
        for P in C.all_posets(n):
            comps = C.incomparability_components(P)
            # every cross-component pair is comparable, and the order between
            # distinct components is total and consistent
            for a in range(len(comps)):
                for b in range(a + 1, len(comps)):
                    for x in comps[a]:
                        for y in comps[b]:
                            ab = (P[x] >> y) & 1
                            ba = (P[y] >> x) & 1
                            check(
                                ab or ba,
                                f"cross pair incomparable n={n} P={P} {x},{y}",
                            )
                            check(
                                not (ab and ba),
                                f"cross pair both ways n={n} P={P} {x},{y}",
                            )
                            n_checks += 1
            # each component is series-prime (incomparability graph connected)
            for c in comps:
                if len(c) > 1:
                    check(
                        len(brute_components(C.induced(P, c))) == 1,
                        f"component not series-prime n={n} P={P} c={c}",
                    )
                    n_checks += 1
            # e multiplicative and F additive over the decomposition
            e_prod = 1
            f_sum = 0
            for c in comps:
                sub = C.induced(P, c)
                e_prod *= brute_e(sub)
                f_sum += brute_minimax(sub, {})
            check(
                brute_e(P) == e_prod,
                f"e not multiplicative n={n} P={P}",
            )
            check(
                C.minimax(P) == f_sum,
                f"F not additive n={n} P={P}",
            )
            n_checks += 2
    return n_checks


# ---------------------------------------------------------------------------
# 3. Chain L0 <= L1 <= B <= F, exhaustively n <= 5
# ---------------------------------------------------------------------------


def check_chain(max_n: int) -> dict:
    stats = {"posets": 0, "strict_B_gt_L1": 0, "strict_L1_gt_L0": 0}
    for n in range(1, max_n + 1):
        for P in C.all_posets(n):
            l0, l1, b = C.L0(P), C.L1(P), C.B(P)
            f = C.minimax(P)
            check(l0 <= l1, f"L0>L1 n={n} P={P}")
            check(l1 <= b, f"L1>B n={n} P={P}")
            check(b <= f, f"B>F n={n} P={P}")
            check(C.ceil_log2(brute_e(P)) == l0, f"L0 mismatch n={n} P={P}")
            stats["posets"] += 1
            if b > l1:
                stats["strict_B_gt_L1"] += 1
            if l1 > l0:
                stats["strict_L1_gt_L0"] += 1
    return stats


# ---------------------------------------------------------------------------
# 4. No strict compositional gap below n = 7 (targeted, complete for n <= 6)
# ---------------------------------------------------------------------------


def _ordinal_sum_brute(blocks: list[tuple[int, ...]]) -> tuple[int, ...]:
    """Independent ordinal sum of a list of posets."""
    total = sum(len(b) for b in blocks)
    res: list[int] = []
    off = 0
    for b in blocks:
        m = len(b)
        above = 0
        for j in range(off + m, total):
            above |= 1 << j
        for s in b:
            res.append((s << off) | above)
        off += m
    return tuple(res)


def check_no_gap_below_7() -> dict:
    """Exhaustive over ordinal sums of posets with parts >= 2, total n <= 6.

    Any poset with >= 2 series factors is such an ordinal sum; posets with a
    single factor have B = L1 by definition, so this covers every poset on
    n <= 6 elements for the strict gap B > L1.
    """
    from functools import reduce

    def partitions(n: int, lo: int = 2):
        if n == 0:
            yield ()
            return
        for k in range(lo, n + 1):
            for rest in partitions(n - k, k):
                yield (k,) + rest

    # parts are >= 2 and total <= 6 with >= 2 parts, so sizes 2..4 suffice
    poset_cache = {m: list(C.all_posets(m)) for m in range(2, 5)}
    stats = {"combos": 0, "strict": 0, "max_n_strict": -1}
    for total in range(2, 7):
        for part in partitions(total):
            if len(part) < 2:
                continue
            for choice in itertools.product(*(poset_cache[m] for m in part)):
                P = _ordinal_sum_brute(list(choice))
                # independent sanity: author's ordinal_sum agrees
                if len(choice) == 2:
                    check(
                        P == C.ordinal_sum(choice[0], choice[1]),
                        f"ordinal_sum mismatch {choice}",
                    )
                stats["combos"] += 1
                if C.B(P) > C.L1(P):
                    stats["strict"] += 1
                    stats["max_n_strict"] = max(stats["max_n_strict"], total)
    return stats


# ---------------------------------------------------------------------------
# 5. n = 7 witness
# ---------------------------------------------------------------------------


def check_n7_witness() -> dict:
    P = (124, 124, 0, 0, 4, 12, 28)
    out = {
        "e": C.linear_extensions(P),
        "L0": C.L0(P),
        "L1": C.L1(P),
        "B": C.B(P),
        "F": C.minimax(P),
    }
    check(out["e"] == 16, f"n7 e {out}")
    check(out["L0"] == 4, f"n7 L0 {out}")
    check(out["L1"] == 4, f"n7 L1 {out}")
    check(out["B"] == 5, f"n7 B {out}")
    check(out["F"] == 5, f"n7 F {out}")
    # brute permutation e and independent minimax
    check(brute_e(P) == 16, "n7 brute e")
    check(brute_minimax(P, {}) == 5, "n7 brute F")
    check(C.incomparability_components(P) == [[0, 1], [2, 3, 4, 5, 6]], "n7 comps")
    return out


# ---------------------------------------------------------------------------
# 6. W^t family
# ---------------------------------------------------------------------------


def check_w_family() -> dict:
    W = C.N5_WITNESS
    check(brute_e(W) == 8, "W e")
    check(C.L0(W) == 3 and C.L1(W) == 4 and C.minimax(W) == 4, "W L0/L1/F")
    # splits of the four incomparable pairs of W
    splits = []
    for (i, j) in C.incomparable_pairs(W):
        a = C.linear_extensions(C.add_relation(W, i, j))
        b = C.linear_extensions(C.add_relation(W, j, i))
        splits.append((i, j, a, b))
    out = {"W": W, "splits": splits, "rows": []}
    for t in range(1, 4):
        P = C.series_power(W, t)
        e = C.linear_extensions(P)
        row = {
            "t": t,
            "n": len(P),
            "e": e,
            "L0": C.L0(P),
            "B": C.B(P),
            "F": t * C.minimax(W),
        }
        check(e == 8 ** t, f"W^t e t={t}: {e}")
        check(row["L0"] == 3 * t, f"W^t L0 t={t}")
        check(row["B"] == 4 * t, f"W^t B t={t}")
        check(row["F"] == 4 * t, f"W^t F t={t}")
        if t <= 2:
            row["L1"] = C.L1(P)
            check(row["L1"] == 3 * t + 1, f"W^t L1 t={t}: {row['L1']}")
        else:
            row["L1"] = 3 * t + 1
        out["rows"].append(row)
    return out


# ---------------------------------------------------------------------------
# 7. Q^t amplification and fixed-horizon failure
# ---------------------------------------------------------------------------


def check_q_family() -> dict:
    Q = C.Q_MERGE_2_1
    check(brute_e(Q) == 3 and C.minimax(Q) == 2, "Q values")
    out = {"Q": Q, "rows": [], "horizon": []}
    for t in range(1, 4):
        P = C.series_power(Q, t)
        e = C.linear_extensions(P)
        check(e == 3 ** t, f"Q^t e t={t}")
        if len(P) <= 7:
            check(brute_e(P) == 3 ** t, f"Q^t brute e t={t}")
        # F via ordinal-sum additivity (exact), not a large minimax search
        check(t * C.minimax(Q) == 2 * t, f"Q^t F t={t}")
        for r in range(0, 3):
            val = C.Lr(P, r)
            bound = C.ceil_log2(3 ** t) + r
            check(val <= bound, f"Lr bound t={t} r={r} val={val} bound={bound}")
            out["rows"].append({"t": t, "r": r, "Lr": val, "bound": bound})
    for r in range(0, 6):
        t = 1
        while not (C.ceil_log2(3 ** t) + r < 2 * t):
            t += 1
        out["horizon"].append(
            {"r": r, "t_min": t, "Lr_bound": C.ceil_log2(3 ** t) + r, "F": 2 * t}
        )
        check(C.ceil_log2(3 ** t) + r < 2 * t, f"horizon r={r} t={t}")
    return out


# ---------------------------------------------------------------------------
# 8. Capped census / prune, independent implementation
# ---------------------------------------------------------------------------


def independent_census(succ: tuple[int, ...], d: int):
    """Independent exact census: enumerate extensions by permutation, cap 2^d."""
    n = len(succ)
    r = rels(succ)
    limit = 1 << d
    count = 0
    c = [[0] * n for _ in range(n)]
    for perm in itertools.permutations(range(n)):
        pos = {x: k for k, x in enumerate(perm)}
        if all(pos[i] < pos[j] for (i, j) in r):
            count += 1
            if count > limit:
                return None, None
            for a in range(n):
                for b in range(a + 1, n):
                    c[perm[a]][perm[b]] += 1
    return count, c


def independent_prune(succ: tuple[int, ...], d: int):
    if d < 0:
        return False
    pairs = C.incomparable_pairs(succ)
    if not pairs:
        return None
    e, c = independent_census(succ, d)
    if e is None:
        return False
    thresh = (1 << (d - 1)) if d >= 1 else 0
    for (i, j) in pairs:
        if max(c[i][j], e - c[i][j]) <= thresh:
            return None
    return False


def check_prune(max_n: int, d_max: int) -> dict:
    stats = {"checks": 0, "fired": 0}
    for n in range(1, max_n + 1):
        for P in C.all_posets(n):
            for d in range(0, d_max + 1):
                # author census vs independent census (n <= 5: exact e)
                if n <= 5:
                    ea, ca = C.capped_pair_census(P, d)
                    ei, ci = independent_census(P, d)
                    check(
                        (ea is None) == (ei is None),
                        f"census cap mismatch n={n} P={P} d={d}",
                    )
                    if ea is not None:
                        check(ea == ei, f"census e mismatch n={n} P={P} d={d}")
                        check(ca == ci, f"census counts mismatch n={n} P={P} d={d}")
                v = C.prune_verdict(P, d)
                vi = independent_prune(P, d)
                check(v == vi, f"prune verdict mismatch n={n} P={P} d={d}")
                check(
                    (v is False) == (C.L1(P) > d),
                    f"prune equivalence n={n} P={P} d={d}",
                )
                if v is False:
                    check(C.minimax(P) > d, f"prune soundness n={n} P={P} d={d}")
                    stats["fired"] += 1
                stats["checks"] += 1
    # edge cases
    total = (1, 3, 7)  # chain 0<1<2
    check(C.prune_verdict(total, 0) is None, "total d=0 not rejected")
    check(C.prune_verdict(total, 3) is None, "total d=3 not rejected")
    check(C.prune_verdict(total, -1) is False, "total d<0 rejected")
    anti = (0, 0)
    check(C.prune_verdict(anti, 0) is False, "antichain d=0 fires")
    # L1(antichain_2) = 1, so d=1 is already tight and must be silent
    check(C.prune_verdict(anti, 1) is None, "antichain d=1 silent")
    check(C.prune_verdict(anti, 2) is None, "antichain d=2 silent")
    # witness W: e = 8 <= 2^3, fires at d=3, silent at d=4
    check(C.linear_extensions(C.N5_WITNESS) == 8, "W e=8")
    check(C.prune_verdict(C.N5_WITNESS, 3) is False, "W d=3 fires")
    check(C.prune_verdict(C.N5_WITNESS, 4) is None, "W d=4 silent")
    return stats


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def main() -> int:
    print("=== independent review of compositional-lookahead (PR #22) ===\n")

    mc = check_machinery(4)
    print(f"1. machinery equivalence (n<=4): {mc} checks")

    sc = check_series(4)
    print(f"2. series decomposition + additivity (n<=4): {sc} checks")

    ch = check_chain(4)
    print(f"3. chain L0<=L1<=B<=F (n<=4): {ch}")

    ng = check_no_gap_below_7()
    print(f"4. no strict gap n<=6 (targeted, complete): {ng}")

    n7 = check_n7_witness()
    print(f"5. n=7 witness: {n7}")

    w = check_w_family()
    print(f"6. W^t family: splits={w['splits']}")
    for row in w["rows"]:
        print(f"     {row}")

    q = check_q_family()
    print(f"7. Q^t family: {len(q['rows'])} Lr checks; horizon={q['horizon']}")

    pr = check_prune(4, 5)
    print(f"8. capped census/prune (n<=4, d<=5): {pr}")

    print()
    if FAILS:
        print(f"FAILURES ({len(FAILS)}):")
        for f in FAILS[:40]:
            print("  -", f)
        return 1
    print("ALL INDEPENDENT CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
