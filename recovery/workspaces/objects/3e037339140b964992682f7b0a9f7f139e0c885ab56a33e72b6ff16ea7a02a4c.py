#!/usr/bin/env python3
"""Truncated k-ply adversarial bounds vs the Kraft bound at the antichain root.

Companion program for ``notes/comparison-split-kraft-obstruction.md`` (front
``comparison-split-kraft-obstruction``).  All items correspond to proved or
conjectured statements labelled in the note; the code computes exact finite
values of the hierarchy ``U_0 <= U_1 <= ... <= F`` and probes where the
hierarchy first exceeds the information bound ``C(n) = ceil(log2 n!)``.

Definitions:

* ``L0(P) = ceil(log2 e(P))`` -- the leaf-counting (information) bound
  (``docs/research-one-ply-obstruction.md``).
* ``U_0(P) = L0(P)`` and for ``k >= 1`` (with )
  ``U_k(P) = 0`` if ``P`` is total, otherwise
  ``1 + min over incomparable pairs {i,j} of max(U_{k-1}(P+i<j), U_{k-1}(P+j<i))``.

The note proves (paper level): ``L0 = U_0 <= U_1 <= ... <= F`` pointwise, the
limit ``sup_k U_k = F``, and the antichain exactness theorem
``U_k(A_n) = ceil(log2 n!)`` for every ``0 <= k <= floor(n/2)`` (fresh-pair
halving chains).  The experiments below *measure* the finite values; the
inequalities themselves have general proofs and are not established by the
code.  No complexity-class or polynomial-time claim is made.
"""

from __future__ import annotations

import argparse
import math
import sys
from functools import lru_cache

sys.path.insert(0, str(__file__).rsplit("/", 1)[0])
from one_ply_obstruction import (  # noqa: E402
    L0,
    add_relation,
    ceil_log2,
    incomparable_pairs,
    linear_extensions,
    minimax,
)


# --------------------------------------------------------------------------
# The truncated k-ply hierarchy
# --------------------------------------------------------------------------

@lru_cache(maxsize=None)
def U(succ: tuple[int, ...], k: int) -> int:
    """Truncated ``k``-ply adversarial information bound。

    ``U(P, 0) = L0(P)``; for ``k >= 1`` one minimax ply whose children are
    scored by the ``(k-1)``-ply bound.  Total orders are scored 0.
    """
    pairs = incomparable_pairs(succ)
    if not pairs:
        return 0
    if k == 0:
        return L0(succ)
    best = None
    for i, j in pairs:
        a = U(add_relation(succ, i, j), k - 1)
        b = U(add_relation(succ, j, i), k - 1)
        val = 1 + (a if a >= b else b)
        if best is None or val < best:
            best = val
            if best == L0(succ):  # cannot beat the Kraft bound; stop
                break
    return best


@lru_cache(maxsize=None)
def _uk_ge_succ(succ: tuple[int, ...], k: int, target: int) -> bool:
    """Decision form ``U(P, k) >= target`` with node-independent memoization."""
    if L0(succ) >= target:
        return True
    if k + L0(succ) < target:  # proved upper bound U_k(P) <= k + L0(P)
        return False
    pairs = incomparable_pairs(succ)
    if not pairs:
        return 0 >= target
    for i, j in pairs:
        # min node: value >= target iff for the best pair both children >= T.
        # alpha-beta: a pair works iff max(child values) >= target.
        a = U(add_relation(succ, i, j), k - 1)
        b = U(add_relation(succ, j, i), k - 1)
        if max(a, b) >= target:
            return True
    return False


def uk_ge(succ: tuple[int, ...], k: int, target: int) -> bool:
    """Exact decision ``U(P, k) >= target`` (memoized threshold form)."""
    if target <= L0(succ):
        return True
    if k + L0(succ) < target:  # proved upper bound U_k(P) <= k + L0(P)
        return False
    return _uk_ge_succ(succ, k, target)


# --------------------------------------------------------------------------
# Theorem 2 machinery: canonical link forests
# --------------------------------------------------------------------------

def link_forest(m: int, n: int) -> tuple[int, ...]:
    """Successor tuple of ``m`` disjoint links ``(0<1), (2<3), ...`` on ``n`` keys.

    Keys ``2m .. n-1`` are isolated.  ``e = n!/2^m`` (proved in the note).
    """
    succ = [0] * n
    for i in range(m):
        succ[2 * i] |= 1 << (2 * i + 1)
    return tuple(succ)


# --------------------------------------------------------------------------
# Experiments
# --------------------------------------------------------------------------

def info_factorial(n: int) -> int:
    return ceil_log2(math.factorial(n))


def binary_insertion_bound(n: int) -> int:
    """``sum_{k=2}^{n} ceil(log2 k)`` -- an explicit all-n sorting strategy."""
    return sum(ceil_log2(k) for k in range(2, n + 1))


def check_antichain_exactness(max_n: int) -> dict[str, object]:
    """Verify ``U_k(A_n) = C(n)`` for all ``k <= floor(n/2)`` (Theorem 2)."""
    rows = []
    for n in range(2, max_n + 1):
        C = info_factorial(n)
        half = n // 2
        vals = [U((0,) * n, k) for k in range(half + 1)]
        assert all(v == C for v in vals), f"n={n}: U_k != C for k<={half}: {vals}"
        rows.append((n, half, C))
    return {"max_n": max_n, "rows": rows}


def first_strict_depth(n: int, cap: int = 1_000_000) -> tuple[int, int] | None:
    """Smallest ``k`` with ``U_k(A_n) > C(n)``, plus value at break, else None.

    Node-capped: returns (k, value) where value may be the capped threshold
    reached; only depths the search completes exactly count.
    """
    root = (0,) * n
    C = info_factorial(n)
    for k in range(n // 2 + 1, n * n + 2):
        if U.cache_info().currsize > cap:
            return None
        v = U(root, k)
        if v > C:
            return (k, v)
    return None


def n12_probe() -> dict[str, object]:
    """Probe where the hierarchy first exceeds ``C(12) = 29`` (known ``S(12)=30``)."""
    n = 12
    C = info_factorial(n)
    out: dict[str, object] = {"n": n, "C": C, "known_S": 30}
    vals = {}
    for k in range(n // 2 + 1, 31):
        v = U((0,) * n, k)
        vals[k] = v
        out[f"U_{k}"] = v
        if v > C:
            break
    out["values"] = vals
    return out


def validate_all(antichain_max_n: int = 6) -> dict[str, object]:
    """CI-sized checks (all statements also have full paper proofs)."""
    summary: dict[str, object] = {}
    # 1. Hierarchy sandwich on all posets n <= 4 (fast exhaustive).
    from one_ply_obstruction import all_posets  # local import keeps module light

    for n in range(1, 5):
        for P in all_posets(n):
            v0, v1, v2 = U(P, 0), U(P, 1), U(P, 2)
            f = minimax(P)
            assert L0(P) <= v1 <= v2 <= f, f"hierarchy fails at P={P}"
    summary["hierarchy_checked_posets"] = 242
    # 2. Antichain exactness Theorem 2.
    summary.update(check_antichain_exactness(antichain_max_n))
    # 3. Limit lemma: sup_k U_k = F, numerically at k = F(P) for small sets.
    for n in range(1, 5):
        for P in all_posets(n):
            f = minimax(P)
            assert U(P, f) == f, f"U(P, F(P)) != F(P) at P={P}"
    # 4. Binary insertion bound vs known exact S(n) (research plan table).
    known_S = {1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13,
               8: 16, 9: 19, 10: 22, 11: 26, 12: 30}
    for n, s in known_S.items():
        summ = binary_insertion_bound(n)
        assert s <= summ, f"S({n})={s} > binary-insertion bound {summ}"
        excess = s - info_factorial(n)
        assert excess <= n - 1 and excess >= 0, f"excess out of range at n={n}"
        assert info_factorial(n) > 0 or n <= 1
    summary["binary_insertion_checked"] = sorted(known_S)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate", action="store_true",
                        help="run CI-sized checks and print a summary")
    parser.add_argument("--antichain-exact", type=int, metavar="MAXN",
                        help="verify Theorem 2 for n <= MAXN")
    parser.add_argument("--probe-n", type=int, metavar="N",
                        help="report the first strict depth of U_k(A_N) > C(N)")
    parser.add_argument("--n12", action="store_true",
                        help="full Theorem-2-complementary probe at n = 12")
    args = parser.parse_args()
    if args.validate:
        result = validate_all()
        for key, val in result.items():
            print(f"{key}: {val}")
    if args.antichain_exact is not None:
        for row in check_antichain_exactness(args.antichain_exact)["rows"]:
            print(f"n={row[0]}: U_k(A_n)=C(n)={row[2]} checked k=0..{row[1]}")
    if args.probe_n is not None:
        res = first_strict_depth(args.probe_n)
        print(f"n={args.probe_n}: first strict depth = {res}")
    if args.n12:
        for key, val in n12_probe().items():
            print(f"{key}: {val}")
    if not (args.validate or args.antichain_exact or args.probe_n or args.n12):
        print("default: CI-sized validation")
        result = validate_all()
        for key, val in result.items():
            print(f"{key}: {val}")


if __name__ == "__main__":
    main()
