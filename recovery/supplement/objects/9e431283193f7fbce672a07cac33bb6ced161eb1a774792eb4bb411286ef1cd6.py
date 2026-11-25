#!/usr/bin/env python3
"""Provenance-annotated exact audit of S(n), C(n)=ceil(log2 n!), g(n), d(n).

Unary-only.  No complexity-class claim.  No PR.

Regenerates the n=1..22 table from the cited values, recomputes C(n) exactly
with big integers, recomputes the Ford-Johnson comparison count F(n), and
independently recomputes S(n) by exact partial-order minimax for the small n
where that is feasible.  The script is a scratch audit artefact; it is not a
Lean proof and does not modify the model.

Sources encoded per n (see PROVENANCE):
  OEIS A036604 (index of exact S(n)); OEIS A003070 (C(n));
  Stober-Weiss, ALENEX 2023 / arXiv:2206.05597 (Table 7);
  Peczarski, Algorithmica 40(2) 2004; Peczarski, Acta Univ. Sapientiae 4(2) 2012;
  Wells 1965/1971; Tao 1989; Kasai-Sawato-Iwata 1994; Cheng et al. 2007.
"""

from __future__ import annotations

import math
import sys
from functools import lru_cache

# ---------------------------------------------------------------------------
# Cited exact values S(n), n = 1..22, with per-n provenance.
# The value is the integer; the string records the primary source(s).
# ---------------------------------------------------------------------------

PROVENANCE = {
    1: ("classical", "F(n)=C(n) for n<=11 (Ford-Johnson 1959 / Knuth TAOCP 5.3.1)"),
    2: ("classical", "F(n)=C(n) for n<=11 (Ford-Johnson 1959 / Knuth TAOCP 5.3.1)"),
    3: ("classical", "F(n)=C(n) for n<=11 (Ford-Johnson 1959 / Knuth TAOCP 5.3.1)"),
    4: ("classical", "F(n)=C(n) for n<=11 (Ford-Johnson 1959 / Knuth TAOCP 5.3.1)"),
    5: ("classical", "F(n)=C(n) for n<=11 (Ford-Johnson 1959 / Knuth TAOCP 5.3.1)"),
    6: ("classical", "F(n)=C(n) for n<=11 (Ford-Johnson 1959 / Knuth TAOCP 5.3.1)"),
    7: ("classical", "F(n)=C(n) for n<=11 (Ford-Johnson 1959 / Knuth TAOCP 5.3.1)"),
    8: ("classical", "F(n)=C(n) for n<=11 (Ford-Johnson 1959 / Knuth TAOCP 5.3.1)"),
    9: ("classical", "F(n)=C(n) for n<=11 (Ford-Johnson 1959 / Knuth TAOCP 5.3.1)"),
    10: ("classical", "F(n)=C(n) for n<=11 (Ford-Johnson 1959 / Knuth TAOCP 5.3.1)"),
    11: ("classical", "F(n)=C(n) for n<=11 (Ford-Johnson 1959 / Knuth TAOCP 5.3.1)"),
    12: ("Wells/Tao", "Wells 1965 (IFIP) & Wells 1971 book; Tao 1989; SW Table 7 cites Wells"),
    13: ("KSI/Peczarski", "Kasai-Sawato-Iwata 1994; Peczarski ESA 2002; Peczarski Algorithmica 2004"),
    14: ("Peczarski", "Peczarski, Algorithmica 40(2) 2004 (abstract: 13,14,22)"),
    15: ("Peczarski/Cheng", "Peczarski IPL 101(3) 2007; Cheng-Liu-Wang-Liu 2007 (NKStars)"),
    16: ("Stober-Weiss", "Stober-Weiss, ALENEX 2023 / arXiv:2206.05597 (new result)"),
    17: ("Stober-Weiss", "Stober-Weiss, ALENEX 2023 / arXiv:2206.05597 (new result)"),
    18: ("Stober-Weiss", "Stober-Weiss, ALENEX 2023 / arXiv:2206.05597 (new result)"),
    19: ("Cheng (sole)", "Cheng-Liu-Wang-Liu 2007 (Chinese); SW Table 7 cites [1]; SW recomputation confirms"),
    20: ("classical", "F(n)=C(n) (Peczarski 2012 / PhD thesis; Knuth); OEIS cites Peczarski 2004 table"),
    21: ("classical", "F(n)=C(n) (Peczarski 2012 / PhD thesis; Knuth); OEIS cites Peczarski 2004 table"),
    22: ("Peczarski", "Peczarski, Algorithmica 40(2) 2004 (abstract: 13,14,22)"),
}

# Exact S(n), n=1..22, as published in OEIS A036604 (b-file) and SW Table 7.
S_EXACT = {
    1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 9: 19, 10: 22,
    11: 26, 12: 30, 13: 34, 14: 38, 15: 42, 16: 46, 17: 50, 18: 54,
    19: 58, 20: 62, 21: 66, 22: 71,
}

# OEIS A003070 (C(n)=ceil(log2 n!)) as published, n=1..22, for cross-check.
C_OEIS = {
    1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 9: 19, 10: 22,
    11: 26, 12: 29, 13: 33, 14: 37, 15: 41, 16: 45, 17: 49, 18: 53,
    19: 57, 20: 62, 21: 66, 22: 70,
}


def ceil_log2_factorial(n: int) -> int:
    """Exact ceil(log2 n!) by big-integer arithmetic (no floating point)."""
    if n <= 1:
        return 0
    # smallest k with 2^k >= n!
    fact = math.factorial(n)
    k = (fact - 1).bit_length()  # ceil(log2 fact)
    return k


def ford_johnson_exact(n: int) -> int:
    """F(n) computed with exact rational ceil(log2(3k/4))."""
    total = 0
    for k in range(1, n + 1):
        num = 3 * k
        den = 4
        # ceil(log2(num/den)) = smallest e with 2^e * den >= num
        e = 0
        while (1 << e) * den < num:
            e += 1
        total += e
    return total


# ---------------------------------------------------------------------------
# Independent exact minimax recomputation (labelled posets, successor bitmasks).
# ---------------------------------------------------------------------------

def _extend(succ, i, j):
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(len(succ)):
        if x == i or (succ[x] & (1 << i)):
            out[x] |= new_greater
    return tuple(out)


def minimax_solve(n: int) -> tuple[int, int]:
    """Exact S(n) via the partial-order minimax recurrence; returns (value, states)."""
    states = {}

    def solve(succ):
        if succ in states:
            return states[succ]
        pairs = [
            (i, j)
            for i in range(n)
            for j in range(i + 1, n)
            if not (succ[i] >> j & 1) and not (succ[j] >> i & 1)
        ]
        if not pairs:
            states[succ] = 0
            return 0
        best = 1 + min(
            max(solve(_extend(succ, i, j)), solve(_extend(succ, j, i)))
            for i, j in pairs
        )
        states[succ] = best
        return best

    value = solve((0,) * n)
    return value, len(states)


def iso_solve(n: int) -> tuple[int, int]:
    """Exact S(n) via the same recurrence quotiented by S_n relabelling.

    Uses scripts/benchmark_symmetry_quotients.py (colour-refinement canonical
    form).  Sound because F is invariant under order isomorphism.
    """
    sys.path.insert(0, "scripts")
    import benchmark_symmetry_quotients as b

    # use_dual=True is cheap (canonical form of the dual); use_orbits is not used
    # here because it enumerates Aut(P) in O(n!) per state.
    value, states, _, _ = b.iso_solve(n, use_dual=True, use_orbits=False)
    return value, states


# ---------------------------------------------------------------------------
# Table generation.
# ---------------------------------------------------------------------------

def main() -> None:
    ns = list(range(1, 23))
    print("=" * 118)
    print("EXACT AUDIT: S(n), C(n)=ceil(log2 n!), excess g(n)=S(n)-C(n), increment d(n)=S(n+1)-S(n)")
    print("n = 1..22.  Unary-only.  Values cited from OEIS A036604 / Stober-Weiss Table 7.")
    print("=" * 118)
    header = f"{'n':>3} | {'S(n)':>4} | {'C(n)':>4} | {'g(n)':>4} | {'d(n)':>4} | {'F(n)':>4} | provenance"
    print(header)
    print("-" * 118)

    rows = []
    for n in ns:
        s = S_EXACT[n]
        c = ceil_log2_factorial(n)
        f = ford_johnson_exact(n)
        g = s - c
        d = S_EXACT[n + 1] - s if n < 22 else None
        prov = PROVENANCE[n][1]
        rows.append((n, s, c, g, d, f))
        ds = "-" if d is None else str(d)
        print(f"{n:>3} | {s:>4} | {c:>4} | {g:>4} | {ds:>4} | {f:>4} | {prov}")

    print("-" * 118)

    # Cross-checks.
    print("\nCROSS-CHECKS")
    print("-" * 118)
    bad_c = [n for n in ns if ceil_log2_factorial(n) != C_OEIS[n]]
    print(f"  C(n) exact big-int vs OEIS A003070: {'OK' if not bad_c else 'MISMATCH ' + str(bad_c)}")
    bad_f = [n for n in ns if ford_johnson_exact(n) != S_EXACT[n]]
    print(f"  F(n) (Ford-Johnson) vs cited S(n):   {'OK (F(n)=S(n) for all n<=22)' if not bad_f else 'MISMATCH ' + str(bad_f)}")
    print(f"  g(n)=0 for n<=11: {all(S_EXACT[n]-ceil_log2_factorial(n)==0 for n in range(1,12))}")
    print(f"  g(n)=0 for n=20,21: {S_EXACT[20]-ceil_log2_factorial(20)==0 and S_EXACT[21]-ceil_log2_factorial(21)==0}")
    print(f"  F(n)=C(n) for n=20,21: {ford_johnson_exact(20)==ceil_log2_factorial(20) and ford_johnson_exact(21)==ceil_log2_factorial(21)}")
    print(f"  g(n) sequence n=1..22: {[S_EXACT[n]-ceil_log2_factorial(n) for n in ns]}")
    print(f"  d(n) sequence n=1..21: {[S_EXACT[n+1]-S_EXACT[n] for n in range(1,22)]}")

    # Independent minimax recomputation (feasible range).
    # Plain labelled enumeration is used for n<=6; the S_n quotient is used for
    # n=7,8 (labelled enumeration at n=7 is A001035(7)=6.1M states).
    print("\nINDEPENDENT EXACT MINIMAX RECOMPUTATION")
    print("-" * 118)
    for n in range(1, 7):
        v, st = minimax_solve(n)
        status = "MATCH" if v == S_EXACT[n] else f"MISMATCH (got {v})"
        print(f"  n={n:>2}: minimax S(n)={v:>3}  states={st:>7}  cited={S_EXACT[n]:>3}  {status}  (labelled)")
    for n in (7, 8):
        try:
            v, st = iso_solve(n)
            status = "MATCH" if v == S_EXACT[n] else f"MISMATCH (got {v})"
            print(f"  n={n:>2}: minimax S(n)={v:>3}  states={st:>7}  cited={S_EXACT[n]:>3}  {status}  (S_n quotient)")
        except Exception as exc:  # pragma: no cover
            print(f"  n={n:>2}: quotient minimax failed: {exc}")

    # n<=11 exactness from F(n)=C(n) plus the information lower bound.
    print("\nEXACTNESS OF S(n)=C(n) FOR n<=11 (FJ upper bound + information lower bound)")
    print("-" * 118)
    for n in range(1, 12):
        f = ford_johnson_exact(n)
        c = ceil_log2_factorial(n)
        print(f"  n={n:>2}: C(n)={c:>3}  F(n)={f:>3}  C(n)<=S(n)<=F(n)  =>  S(n)=C(n)={c}")

    # n=12..22 cannot be recomputed by minimax here; they rest on the cited searches.
    print("\n  n=12..22: exact minimax is infeasible here (A001035(12) ~ 1.4e10 labelled states);")
    print("  values rest on the cited exhaustive/bidirectional searches (Wells, Peczarski, Stober-Weiss).")

    print("\n" + "=" * 118)
    print("PROVENANCE SUMMARY")
    print("=" * 118)
    for n in ns:
        print(f"  n={n:>2}: {PROVENANCE[n][0]:<14} {PROVENANCE[n][1]}")


if __name__ == "__main__":
    main()
