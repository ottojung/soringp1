#!/usr/bin/env python3
"""Exact-integer corroboration of the F-J algebra through k=10000."""

def d(j: int) -> int:
    t = 0
    while 4 * (1 << t) < 3 * j:
        t += 1
    return t


J = [0, 1]
while J[-1] < 20002:
    J.append(J[-1] + 2 * J[-2])


def q(j: int) -> int:
    return next(r for r in range(1, len(J)) if J[r] >= j)


B = [0]
for j in range(1, 20001):
    B.append(B[-1] + d(j))

D = 0
for k in range(1, 10001):
    D += q(k) - 1
    assert B[2 * k] - B[k] - k == D, f"(E) fails at k={k}"

for k in range(10001):
    assert d(2 * k + 1) == q(k + 1) - 1, f"odd identity fails at k={k}"

print("PASS: (E) for 1 <= k <= 10000; odd identity for 0 <= k <= 10000")
