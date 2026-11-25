#!/usr/bin/env python3
"""Exact-integer checks for research-fj-upper-bound-proof.md."""

LIMIT = 10000


def d(j):
    t = 0
    while 4 * (1 << t) < 3 * j:
        t += 1
    return t


J = [0, 1]
while J[-1] < 2 * LIMIT + 10:
    J.append(J[-1] + 2 * J[-2])


def q(j):
    for r in range(1, len(J)):
        if J[r] >= j:
            return r
    raise AssertionError("Jacobsthal table too short")


for r in range(1, len(J)):
    assert J[r] == (2**r - (-1) ** r) // 3
    assert J[r] + J[r - 1] == 2 ** (r - 1)

B = [0]
for j in range(1, 2 * LIMIT + 2):
    B.append(B[-1] + d(j))

D = 0
U = [0] * (LIMIT + 2)
for k in range(1, LIMIT + 1):
    D += q(k) - 1
    assert D == sum(max(0, k - J[r]) for r in range(1, len(J)))
    assert d(2 * k - 1) == q(k) - 1
    assert d(2 * k) == d(k) + 1
    assert B[2 * k] - B[k] - k == D

for n in range(2, LIMIT + 1):
    k = n // 2
    U[n] = U[k] + k + sum(q(j) - 1 for j in range(1, (n + 1) // 2 + 1))
    assert U[n] == B[n]

print(f"PASS: exact integer identities and U(n)=B(n) for n<={LIMIT}")
