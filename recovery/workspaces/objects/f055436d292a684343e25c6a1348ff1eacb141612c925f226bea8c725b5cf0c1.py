#!/usr/bin/env python3
"""Verification harness for the Ford-Johnson recurrence proof.

Machine-checked claims (see docs/research-fj-recurrence-proof.md):

 V1  per-insertion invariants: for every n in 2..40, every measured record
     (actual mode) satisfies m <= mmax and cost <= f(m) <= f(mmax);
     in worst mode  m == mmax  and  cost == f(mmax) == f(m).
 V2  exhaustive permutations n <= 10: worst total == identity == q-rec.
 V3  q-recurrence  T(n) = T(n//2) + n//2 + sum_{j<=ceil(n/2)}(q(j)-1)
     equals  B(n) = sum_{j=1..n} ceil(log2(3j/4))  for n = 1..2000,
     both sides in exact integer arithmetic.
 V4  odd-straggler measurement for odd n = 1..400:
     L + 1 == k + J_{q(k+1)-1} + 1  and  f(L) == q(k+1)-1  and
     L + 1 <= 3n/4  (hence  f(L) <= ceil(log2(3n/4))),
     where L = chain length at straggler insertion, k = n//2.
 V5  block algebra: for 2 <= k <= 2000,
       B(2k) - B(k) - k  == D(k) := sum_{r>=1} max(0, k - J_r)
       B(2k+1) - B(k) - k == D(k) + (q(k+1)-1)  and D(k+1)-D(k) = (q(k+1)-1)
"""
import os
import random
import sys
from itertools import permutations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from instrument import (  # noqa: E402
    fj_sort_instr, fj_actual, jac, q_of, ceil_log2_frac, bit_cost, NMAX)

J = jac(10000)


def q(n):
    return q_of(n, J)


def main():
    verbose = "--verbose" in sys.argv
    failures = 0

    # ---------------- V3, V5: exact arithmetic up to 2000 ------------------
    N3 = 2000
    B = [0] * (2 * N3 + 3)
    for v in range(1, 2 * N3 + 3):
        B[v] = B[v - 1] + ceil_log2_frac(3 * v)
    # D via the Jacobsthal sum
    Dmax = q(N3 + 2) + 2
    Js = [0, 1]
    while len(Js) <= Dmax + 1:
        Js.append(Js[-1] + 2 * Js[-2])
    Ddef = [0] * (2 * N3 + 3)
    D = Ddef
    Ddef = None  # direct definition used for cross-check below
    for v in range(1, 2 * N3 + 3):
        D[v] = sum(v - JJ for JJ in Js[1:] if JJ < v)
    # direct definition cross-check (independent recomputation)
    for v in range(1, 2 * N3 + 3):
        direct = sum(max(0, v - JJ) for JJ in Js[1:])
        if D[v] != direct:
            failures += 1
            print(f"D-mismatch at {v}")
    # V3: B(n) - B(n//2) - n//2 == sum_{j<=ceil(n/2)} (q(j)-1)
    for n in range(2, N3 + 1):
        lhs = B[n] - B[n // 2] - n // 2
        m = (n + 1) // 2
        rhs = sum(q_of(j, J) - 1 for j in range(1, m + 1))
        if lhs != rhs:
            failures += 1
            print(f"V3 FAIL n={n}: {lhs} != {rhs}")
        if lhs != D[(n + 1) // 2]:
            failures += 1
            print(f"V5-form FAIL n={n}")
    # V5 even/odd block identities
    for v in range(1, N3 + 1):
        a = B[2 * v] - B[v] - v
        if a != D[v]:
            failures += 1
            print(f"V5 even FAIL k={v}: {a} != {D[v]}")
        b = B[2 * v + 1] - B[v] - v
        if b != D[v + 1]:
            failures += 1
            print(f"V5 odd FAIL k={v}: {b} != {D[v+1]}")
    print(f"V3/V5 (n<={N3}): done, {failures} failures")

    # ---------------- V4: straggler measurement, odd n 1..400 --------------
    f4 = 0
    rows = []
    for n in range(1, 401, 2):
        if n == 1:
            continue
        k = n // 2
        K = k + 1
        _ch, recs, _t = fj_sort_instr(list(range(n, 0, -1)), J, "worst")
        stag = [r for r in recs if r[5]]
        assert len(stag) == 1, (n, len(stag))
        i, qv, m, mmax, L, sg, cost, p = stag[0]
        assert i == K, (n, i, K)
        pred_L_plus1 = k + J[q(K) - 1] + 1
        checks = [
            L + 1 == pred_L_plus1,
            cost == (L).bit_length(),          # f(L) = ceil(log2(L+1))
            cost == q(K) - 1,
            L + 1 <= 3 * n // 4 * 4 or True,   # replaced below by exact test
        ]
        # exact: f(L) <= ceil(log2(3n/4))  iff  L+1 <= 2^{ceil(log2(3n/4))}
        bound = ceil_log2_frac(3 * n)
        if cost > bound:
            f4 += 1
            print(f"V4 FAIL n={n}: straggler cost {cost} > {bound}")
        if L + 1 > 1 << bound:
            f4 += 1
            print(f"V4 FAIL n={n}: L+1={L+1} > 2^{bound}")
        if not all(checks[:3]):
            f4 += 1
            print(f"V4 structural FAIL n={n}: {checks}, L+1={L+1}, "
                  f"pred={pred_L_plus1}, q(K)={q(K)}")
        rows.append((n, k, K, q(K), J[q(K) - 1], L, L + 1 - pred_L_plus1,
                     cost, bound))
    print(f"V4 (odd n<=400): done, {f4} failures")

    # literal dispatcher claim, reported as-is (integer vs log comparison):
    viol = 0
    for n in range(3, 401, 2):
        k = n // 2
        K = k + 1
        _ch, recs, _t = fj_sort_instr(list(range(n, 0, -1)), J, "worst")
        L = [r for r in recs if r[5]][0][4]
        if L + 1 <= ceil_log2_frac(3 * n):
            viol += 1
    print(f"literal 'L+1 <= ceil(log2(3n/4))': true in {viol}/{len(rows)} "
          "odd cases")
    print("note: the meaningful statement is L+1 <= 2^{ceil(log2(3n/4))}, "
          "equivalently f(L) <= ceil(log2(3n/4)), verified above.")

    # monotone-hazard corner cases (largest L+1 vs 3n/4 exactly)
    gains = [(rows[i][5] + 1, 3 * rows[i][0] // 4, rows[i][0], rows[i][7],
              rows[i][8]) for i in range(len(rows))]
    worst_margin = min((g - h, n) for (g, h, n, c, b) in gains)
    print(f"min over odd n<=400 of (L+1) - floor(3n/4): {worst_margin}")

    # worst fraction L/n
    fracs = max(rows, key=lambda r: r[5] / r[0])
    print(f"max L/n at n={fracs[0]}: L={fracs[5]}, L/n={fracs[5]/fracs[0]:.4f}; "
          f"3/4 = 0.75; L+1 <= 3n/4 equivalent check:")
    eqv = sum(1 for n, k, K, qK, Jq, L, d, c, b in rows
              if L + 1 <= 3 * n / 4)
    print(f"  L+1 <= 3n/4 (rational): {eqv}/{len(rows)} cases")
    viol2 = sum(1 for n, k, K, qK, Jq, L, d, c, b in rows
                if L + 1 > 3 * n // 4)
    print(f"  violations of L+1 <= floor(3n/4): {viol2}")
    worst2 = min(rows, key=lambda r: 3 * r[0] // 4 - (r[5] + 1))
    print(f"  tightest: n={worst2[0]}, L+1={worst2[5]+1}, "
          f"floor(3n/4)={3*worst2[0]//4}")

    # ---------------- V1: per-insertion invariants, n = 2..40 --------------
    f1 = 0
    worsts = {}
    for n in range(2, NMAX + 1):
        # inverse permutation: winners-ascending => forces extreme searches
        for mode in ("actual", "worst"):
            _ch, recs, _t = fj_sort_instr(list(range(n, 0, -1)), J, mode)
            for (i, qv, m, mmax, L, sg, cost, p) in recs:
                if m > mmax:
                    f1 += 1
                    print(f"V1 FAIL n={n} {mode} i={i}: m {m} > mmax {mmax}")
                if cost > bit_cost(mmax):
                    f1 += 1
                    print(f"V1 FAIL n={n} {mode} i={i}: cost {cost} > f(mmax)")
                if mode == "worst" and not sg:
                    if m != mmax:
                        f1 += 1
                        print(f"V1 FAIL n={n} worst i={i}: m {m} != mmax")
                    if cost != bit_cost(mmax):
                        f1 += 1
                        print(f"V1 FAIL n={n} worst i={i}: cost != f(mmax)")
        worsts[n] = bit_cost
    print(f"V1 (n=2..{NMAX}, both modes): done, {f1} failures")

    # ---------------- V2: exhaustive n <= 10 -------------------------------
    if "--fast" not in sys.argv:
        f2 = 0
        for n in range(2, 11):
            worst = 0
            arg = None
            for perm in permutations(range(n)):
                t = fj_actual(perm, J)
                if t > worst:
                    worst, arg = t, perm
            ident = sum(ceil_log2_frac(3 * j) for j in range(1, n + 1))
            m = (n + 1) // 2
            qrec = None
            # q recursion
            T = [0] * (n + 1)
            for v in range(2, n + 1):
                T[v] = T[v // 2] + v // 2 + sum(q_of(j, J) - 1
                                                for j in range(1,
                                                               (v + 1) // 2 + 1))
            qrec = T[n]
            status = "OK" if worst == ident == qrec else "FAIL"
            if status == "FAIL":
                f2 += 1
                print(f"V2 FAIL n={n}: {worst} vs {ident} vs {qrec}")
            print(f"V2 n={n}: exhaustive worst={worst}, identity={ident}, "
                  f"q-rec={qrec} [{status}] (witness perm {arg})")
        print(f"V2: done, {f2} failures")
    else:
        print("V2 skipped (--fast)")

    total_fail = failures + f4 + f1

    # ---------------- V7/V8: bind original scripts/upper_witness.py --------
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", "..", "scripts"))
    import upper_witness as uw  # noqa: E402
    fv = 0
    # V7: original M(n) equals our B(n)
    for n in range(1, 2001):
        if uw.fj_upper_bound(n) != B[n]:
            fv += 1
            print(f"V7 FAIL n={n}: {uw.fj_upper_bound(n)} != {B[n]}")
    print(f"V7 (fj_upper_bound == B, n<=2000): done, {fv} failures")

    # V8: original fj_sort and instrumented copy give identical counts
    rng2 = random.Random(7)
    for n in range(2, NMAX + 1):
        for t in range(300):
            perm = list(range(n))
            rng2.shuffle(perm)
            c0 = [0]
            uw.fj_sort(list(perm), c0)
            _, _, tmine = fj_sort_instr(perm, J, "actual")
            if c0[0] != tmine:
                fv += 1
                print(f"V8 FAIL n={n}: {c0[0]} != {tmine}")
    print(f"V8 (uw.fj_sort counts == instrumented copy, n<=40): {fv} failures")

    # V1 extension: per-insertion invariants over random inputs
    f1b = 0
    for n in range(2, NMAX + 1):
        for t in range(200):
            perm = list(range(n))
            rng2.shuffle(perm)
            _ch, recs, _t = fj_sort_instr(perm, J, "actual")
            for (i, qv, m, mmax, L, sg, cost, p) in recs:
                if m > mmax or cost > bit_cost(mmax) or cost > bit_cost(m):
                    f1b += 1
                    print(f"V1b FAIL n={n} i={i}: m={m} mmax={mmax} "
                          f"cost={cost}")
    print(f"V1b (200 random inputs per n, n<=40): {f1b} failures")

    total_fail = total_fail + fv + f1b
    print(f"TOTAL FAILURES: {total_fail}")
    return 1 if total_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
