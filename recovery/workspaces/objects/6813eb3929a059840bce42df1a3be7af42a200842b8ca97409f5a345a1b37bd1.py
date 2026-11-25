#!/usr/bin/env python3
"""Exact arithmetic for the Ford-Johnson bound F_FJ(n) = sum_{j=1}^n ceil(log2(3j/4))
and the information bound L(n) = ceil(log2(n!)).  No floating point is used in
the integer part; a high-precision float check is used only for the asymptotic
ratio.  Artifact of the soring301 FJ-exact-barrier front (2026-11-24).
"""

import math


def fj_term(j: int) -> int:
    """ceil(log2(3j/4)) exactly: smallest r with 2^(r+2) >= 3j, i.e.
    ceil(log2(3j)) - 2 = (3j-1).bit_length() - 2."""
    return (3 * j - 1).bit_length() - 2


def F_FJ(n: int) -> int:
    return sum(fj_term(j) for j in range(1, n + 1))


def L_info(n: int) -> int:
    """ceil(log2(n!)) exactly."""
    return (math.factorial(n) - 1).bit_length()


# Exact S(n) for n=1..22, literature values (OEIS A036604; Knuth TAOCP 5.3.1;
# Wells n=12; Peczarski 2012; Stober-Weiss ALENEX 2023 for 16,17,18).
S_KNOWN = {
    1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 9: 19, 10: 22,
    11: 26, 12: 30, 13: 34, 14: 38, 15: 42, 16: 46, 17: 50, 18: 54,
    19: 58, 20: 62, 21: 66, 22: 71,
}

if __name__ == "__main__":
    print("n  F_FJ(n)  L(n)=ceil(log2 n!)  S(n)  F_FJ-S  F_FJ-L  S-L")
    for n in range(1, 23):
        F, L, S = F_FJ(n), L_info(n), S_KNOWN[n]
        print(f"{n:2d} {F:7d} {L:17d} {S:5d} {F-S:7d} {F-L:7d} {S-L:5d}")

    # first n<=22 with F_FJ(n) > S(n), if any
    bad = [n for n in range(1, 23) if F_FJ(n) > S_KNOWN[n]]
    print("first n<=22 with F_FJ(n) > S(n):", bad[0] if bad else "NONE")

    # numerical surplus ratio at larger n (float check only)
    print("\nn        F_FJ    log2(n!)   surplus   surplus/n")
    for n in [22, 32, 64, 128, 256, 1024, 4096, 16384, 65536, 262144]:
        F = F_FJ(n)
        logfact = math.lgamma(n + 1) / math.log(2)
        sur = F - logfact
        print(f"{n:6d} {F:9d} {logfact:12.3f} {sur:10.3f} {sur/n:11.5f}")

    # dyadic-block lower bound constant: 1/ln2 - 4/3
    print("\nblock constant 1/ln2 - 4/3 =", 1.0 / math.log(2) - 4.0 / 3.0)
    print("first-piece integral -int_1^{4/3} log2 x dx =",
          -( (4.0/3)*(1-math.log(4.0/3)) - 1 ) / math.log(2))
