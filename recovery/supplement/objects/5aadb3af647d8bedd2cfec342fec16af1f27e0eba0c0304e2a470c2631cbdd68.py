#!/usr/bin/env python3
"""Exact-data probe for the sharp two-value INCREMENT DETERMINATION law.

Question (unary-only). With
    C(n) = ceil(log2 n!),
    m(n) = ceil(log2 (n+1)),
    a_n = 1 iff C(n+1) - C(n) = m(n) - 1   ("allowed" indicator),
    d(n) = S(n+1) - S(n),
is  d(n) = m(n) - a_n  for every n >= 1 ?

Since d(n) = D_{n+1} + (g(n+1) - g(n)) with D_{n+1} = C(n+1)-C(n) and
g(n) = S(n) - C(n), and m(n) - a_n = D_{n+1}, the claim is EXACTLY

    g(n+1) = g(n)  for all n  <=>  g is constant.

So the determination law is equivalent to "the excess g is constant".
It is tested here against the exact S(1..22) literature values.

Run:  python3 scripts/two_value_increment_law_probe.py
"""

from math import factorial

# Exact S(n), n = 1..22.  Provenance: Ford-Johnson/Knuth (n<=11, n=20,21),
# Wells 1965/1971 + Tao 1989 (n=12), Kasai-Sawato-Iwata 1994 and
# Peczarski 2004 (n=13,14,22), Peczarski 2007 (n=15), Stober-Weiss 2023
# (n=16,17,18), Cheng-Liu-Wang-Liu 2007 (n=19).  See #301 2026-10-21T04:43:16Z.
S = [None, 0, 1, 3, 5, 7, 10, 13, 16, 19, 22, 26, 30, 34, 38, 42, 46,
     50, 54, 58, 62, 66, 71]


def C(n: int) -> int:
    """ceil(log2 n!) exactly via bit length of n!."""
    return (factorial(n) - 1).bit_length()


def ceil_log2(x: int) -> int:
    """ceil(log2 x) for x >= 1."""
    return x.bit_length() - 1 if (x & (x - 1)) == 0 else x.bit_length()


def main() -> None:
    print("n | S(n) | C(n) | g | d(n) | m(n) | D=C(n+1)-C(n) | a_n | m-a_n | d-(m-a_n)")
    bad = []
    for n in range(1, 22):
        c = C(n)
        g = S[n] - c
        d = S[n + 1] - S[n]
        mm = ceil_log2(n + 1)
        D = C(n + 1) - C(n)
        a = 1 if D == mm - 1 else 0
        pred = mm - a
        ok = (d == pred)
        if not ok:
            bad.append((n, d, pred, g, S[n + 1] - C(n + 1)))
        print(f"{n:>2} | {S[n]:>4} | {c:>4} | {g} | {d:>4} | {mm:>4} | "
              f"{D:>14} | {a:>3} | {pred:>5} | {d - pred:>9}"
              + ("" if ok else "   <-- FAILS"))
    print()
    print("First counterexamples (n, d(n), m(n)-a_n, g(n), g(n+1)):")
    for row in bad[:5]:
        print("  n=%d: d=%d, m-a_n=%d, g(n)=%d, g(n+1)=%d" % row)
    print()
    print("Determination law d(n)=m(n)-a_n is equivalent to g constant.")
    print("g is constant on 1..22?", len({S[n] - C(n) for n in range(1, 23)}) == 1)
    print("g values:", [S[n] - C(n) for n in range(1, 23)])


if __name__ == "__main__":
    main()
