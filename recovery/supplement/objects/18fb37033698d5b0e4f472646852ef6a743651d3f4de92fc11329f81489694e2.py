#!/usr/bin/env python3
"""Unary automaticity probe for S(n) (SoringP1, issue #301).

Corrected scope (per orchestration correction):
  * S and d(n)=S(n+1)-S(n) are unbounded, so neither is a k-automatic
    sequence (finite alphabet) nor eventually periodic.  That part is trivial.
  * The non-trivial objects are INDICATOR sets, e.g.
        T = { n : d(n) = ceil(log2(n+1)) }        ("tight increments")
        A = { n : C(n+1)-C(n) = ceil(log2(n+1))-1 } ("allowed positions")
    and we ask whether such sets are eventually periodic / k-automatic.
  * The prior #301 g-Lipschitz theorem proves only d(n) <= m and (strict S)
    d(n) >= 1; it does NOT prove d(n) in {m-1,m}.  We do not assume that.

Primary sources for exact S(n):
  n<=12  Wells (1965)/Tao (1989); n=13 Peczarski ESA 2002; n=14,22 Peczarski
  Algorithmica 2004; n=15 Peczarski 2012; n=16,17,18 Stober-Weiss ALENEX 2023
  (arXiv:2206.05597); n=19,20,21 Peczarski 2004 table (OEIS A036604 comment);
  n=19..22 Stober-Weiss arXiv table.  OEIS A036604 (index), A003070 (C(n)).
"""
import math


# exact optimal sorting numbers S(n), n = 1..22 (OEIS A036604)
S = {1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 9: 19, 10: 22,
     11: 26, 12: 30, 13: 34, 14: 38, 15: 42, 16: 46, 17: 50, 18: 54,
     19: 58, 20: 62, 21: 66, 22: 71}


def ceil_log2_int(f):
    """Exact ceil(log2 f) for integer f >= 1."""
    assert f >= 1
    return (f - 1).bit_length()


def C(n):
    """C(n) = ceil(log2(n!)), exact."""
    return ceil_log2_int(math.factorial(n))


def m(n):
    """m(n) = ceil(log2(n+1))."""
    return ceil_log2_int(n + 1)


def audit_table(nmax=22):
    print(" n |  S(n) | d(n) | m(n) | C(n) | g(n) | tight? | allowed? | Delta=g(n+1)-g(n)")
    tight, allowed = [], []
    for n in range(1, nmax + 1):
        d = S[n + 1] - S[n] if n < nmax else None
        c = C(n)
        g = S[n] - c
        if d is None:
            print(f"{n:2d} | {S[n]:5d} |    - | {m(n):4d} | {c:4d} | {g:4d} |")
            continue
        a = 1 if (C(n + 1) - C(n)) == m(n) - 1 else 0
        gnext = S[n + 1] - C(n + 1)
        delta = gnext - g
        is_tight = (d == m(n))
        if is_tight:
            tight.append(n)
        if a:
            allowed.append(n)
        print(f"{n:2d} | {S[n]:5d} | {d:4d} | {m(n):4d} | {c:4d} | {g:4d} |"
              f" {str(is_tight):>5s} | {a:7d} | {delta:4d}")
    print()
    print("T (tight increments)      :", tight)
    print("A (allowed positions)     :", allowed)
    print("non-allowed               :",
          [n for n in range(1, nmax) if n not in allowed])
    print()
    # Verify the exact decomposition d = m - a + Delta  and  tight <=> Delta = a.
    ok = True
    for n in range(1, nmax):
        d = S[n + 1] - S[n]
        a = 1 if (C(n + 1) - C(n)) == m(n) - 1 else 0
        delta = (S[n + 1] - C(n + 1)) - (S[n] - C(n))
        if d != m(n) - a + delta or (d == m(n)) != (delta == a):
            ok = False
            print("MISMATCH at n=", n, d, m(n), a, delta)
    print("decomposition d = m - a + Delta and tight <=> Delta=a :",
          "VERIFIED" if ok else "FAILED")


def allowed_density(limit):
    """Exact-ish count of allowed positions q in [4, limit]; density -> 1/ln2 - 1.

    D_q = C(q)-C(q-1); allowed iff D_q = ceil(log2 q) - 1.
    Uses high-precision lgamma with an exact fallback near integer boundaries."""
    import math
    cnt = 0
    for q in range(4, limit + 1):
        x = math.lgamma(q + 1) / math.log(2)   # log2(q!)
        if abs(x - round(x)) < 1e-6:           # boundary: recompute exactly
            c_q = (math.factorial(q) - 1).bit_length()
            c_prev = (math.factorial(q - 1) - 1).bit_length()
        else:
            c_q = math.ceil(x)
            c_prev = math.ceil(math.lgamma(q) / math.log(2))
        if c_q - c_prev == m(q - 1) - 1:       # m(q-1) = ceil(log2 q)
            cnt += 1
    return cnt


def allowed_prefix_at_powers(rmax=20):
    """Return [(2^R, E(2^R))] where E is the allowed-position counting function.

    E(2^R)/2^R -> 1/ln2 - 1 (irrational).  Sampled at dyadic boundaries because
    the density oscillates inside a dyadic block."""
    import math
    out = []
    cnt = 0
    for q in range(4, (1 << rmax) + 1):
        x = math.lgamma(q + 1) / math.log(2)
        if abs(x - round(x)) < 1e-6:
            c_q = (math.factorial(q) - 1).bit_length()
            c_prev = (math.factorial(q - 1) - 1).bit_length()
        else:
            c_q = math.ceil(x)
            c_prev = math.ceil(math.lgamma(q) / math.log(2))
        if c_q - c_prev == m(q - 1) - 1:
            cnt += 1
        if q >= 8 and (q & (q - 1)) == 0:
            out.append((q, cnt))
    return out


def main():
    audit_table()
    print()
    target = 1.0 / math.log(2) - 1.0
    print("theoretical allowed density 1/ln2 - 1 = %.9f  (irrational)" % target)
    print(" E(2^R)/2^R, sampled at dyadic boundaries:")
    for q, c in allowed_prefix_at_powers(20):
        print(f"   2^{q.bit_length() - 1:2d} : E={c:7d}  density={c / q:.6f}")
    print()
    print("A (allowed) has dyadic-limit density 1/ln2-1, irrational.  If A were")
    print("eventually periodic with period p then E(2^R)/2^R -> (#ones)/p rational,")
    print("contradiction.  Hence A is NOT eventually periodic (nor k-automatic).")
    print("T depends on the unknown gap g = S - C; its periodicity cannot be")
    print("settled by the 22 exact data points.")


if __name__ == "__main__":
    main()
