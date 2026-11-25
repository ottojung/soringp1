#!/usr/bin/env python3
"""Verify the two dyadic-block bounds used in the FJ-surplus Theta(n) proof:
 (F1) full block B_m={2^m,...,2^{m+1}-1}: S_m >= (1/ln2-4/3)*2^m - 1
 (F2) partial block prefix {2^m,...,K}, K=floor(4*2^m/3):
      >= -0.073*2^m - 1  (m>=1)
Uses exact integer F_FJ plus float log only for the *check*, not the proof.
"""
import math
from fj_exact import fj_term

def phi(j):
    return fj_term(j) - math.log2(j)

def check(m):
    a = 2**m
    K = (4*a)//3
    full = sum(phi(j) for j in range(a, 2*a))
    firstpiece = sum(phi(j) for j in range(a, K+1))
    c1 = 1/math.log(2) - 4/3
    ok1 = full >= c1*a - 1
    ok2 = firstpiece >= -0.073*a - 1
    return m, a, full, c1*a - 1, ok1, firstpiece, -0.073*a - 1, ok2

if __name__ == "__main__":
    allok = True
    for m in range(1, 21):
        r = check(m)
        allok &= r[4] and r[7]
        print(f"m={r[0]:2d} a=2^{m:<2d} full={r[2]:11.3f} bound1={r[3]:11.3f} ok={r[4]} "
              f"| first={r[5]:10.3f} bound2={r[6]:10.3f} ok={r[7]}")
    print("ALL BLOCK BOUNDS HOLD:", allok)
