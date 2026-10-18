#!/usr/bin/env python3
"""Disjoint-union (parallel) module reversal of the exact minimax value F.

Companion to docs/research-parallel-duality.md.

Model (docs/problem.md, docs/upper-bound.md, SoringP1/Minimax.lean): a state is
a strict partial order on the labelled keys [n], stored as successor bitmasks
(succ[i] has bit j iff i < j); the remaining minimax cost is

    F(P) = 0                                                      if P is total,
    F(P) = 1 + min_{x,y incomparable} max(F(P+x<y), F(P+y<x))      otherwise,

and S(n) = F(empty poset).  Equivalently, F(P) is the minimum height of a
decision tree identifying the unknown linear extension of P; the Lean
`adv (L(P))` is this value (A24).

Definitions (this note):

  * The *disjoint union* (parallel composition) A || B is the poset on
    |A| + |B| keys where the A-keys and B-keys keep their internal relations
    and every cross pair is incomparable.
  * A *module* S of P is a set that is uniform to the outside (Gallai
    autonomous set).  In P = A || B, A is a module, and reversing it gives
    A^op || B.

Encoding invariant (checked here, and the source of an earlier correction):
if B is encoded on its own labels 0..|B|-1, then the encoding of A || B MUST
shift B's masks left by |A|:

    succ_{A||B}[|A| + i] = succ_B[i] << |A|.

Failing to shift produces relations from B back into A, which is not a disjoint
union; an early probe did this and the resulting F values were spurious.

Main claims:

  (1) Restricted theorem (paper proof in the note): if B is self-dual up to
      relabelling (B^op ~= B), then F(A^op || B) = F(A || B).  This covers
      parallel-quotient module reversal, whose complement is an antichain and
      hence self-dual.
  (2) The general case (both A and B non-self-dual) is *unresolved*: the
      exhaustive n <= 7 checks below find no counterexample, but no proof is
      claimed.
  (3) For every pair checked: every relation of A || B lies inside A or inside
      B, and e(A || B) = binom(a+b, a) * e(A) * e(B).

No external libraries.  Deterministic.  No n >= 8 exhaustive search.
"""

import argparse
import sys
from functools import lru_cache

sys.path.insert(0, "scripts")
from benchmark_symmetry_quotients import (  # noqa: E402
    dual,
    make_refined_canon,
    quotient_classes,
)

A000112 = {0: 1, 1: 1, 2: 2, 3: 5, 4: 16, 5: 63, 6: 318, 7: 2045}


# --------------------------------------------------------------------------
# Disjoint union and its invariants.
# --------------------------------------------------------------------------

def disjoint_union(A, B):
    """Poset A || B on |A|+|B| keys; every cross pair incomparable.

    A and B are successor-bitmask tuples on their own labels.  B's masks are
    shifted left by len(A); without the shift the second block's relations
    would point back into A and the result would not be a disjoint union.
    """
    a = len(A)
    out = list(A) + [m << a for m in B]
    return tuple(out)


def dual_union(A, B):
    """(A || B)^op = A^op || B^op."""
    n = len(A) + len(B)
    return dual(disjoint_union(A, B), n)


def is_self_dual(P, n, canon=None):
    """True iff P is isomorphic to its order dual."""
    if canon is None:
        canon = make_refined_canon(n)
    return canon(P) == canon(dual(P, n))


def within_blocks(P, a, b):
    """Every relation of P = A || B (a A-keys, b B-keys) is internal.

    Returns (ok, offender) where ok is True iff no relation crosses the A/B
    boundary.  Also asserts the internal relations agree with the blocks, but
    callers pass genuine A || B so only the cross check matters.
    """
    n = a + b
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if (i < a) != (j < a) and (P[i] >> j & 1):
                return False, (i, j)
    return True, None


def linear_extensions(P):
    """Number of linear extensions e(P) by DP over down-sets."""
    n = len(P)
    preds = [0] * n
    for i in range(n):
        for j in range(n):
            if P[j] >> i & 1:
                preds[i] |= 1 << j
    full = (1 << n) - 1

    @lru_cache(maxsize=None)
    def count(done):
        if done == full:
            return 1
        total = 0
        for i in range(n):
            if done >> i & 1:
                continue
            if preds[i] & ~done:
                continue
            total += count(done | (1 << i))
        return total

    return count(0)


def e_of_class(c, ecache):
    if c not in ecache:
        ecache[c] = linear_extensions(c)
    return ecache[c]


# --------------------------------------------------------------------------
# Exhaustive check over isomorphism classes.
# --------------------------------------------------------------------------

def verify(n, check_e=True, verbose=False):
    """Exhaustive over all isomorphism classes A, B with |A|+|B| = n.

    Returns a stats dict.  For every pair checks:
      * encoding invariants (within-block relations, e identity);
      * the restricted theorem (B self-dual => F(A^op||B) = F(A||B));
      * the general (unproven) equalities F(A^op||B) = F(A||B) = F(A||B^op),
        recorded as evidence, not as a theorem.
    """
    canon = make_refined_canon(n)
    classes = quotient_classes(n)
    F = classes  # canonical rep -> F value
    ecache = {}
    by_size = {k: list(quotient_classes(k).keys()) for k in range(n + 1)}

    stats = {
        "n": n,
        "pairs": 0,
        "restricted_pairs": 0,
        "restricted_violations": 0,
        "restricted_examples": [],
        "general_violations": 0,
        "general_examples": [],
        "e_violations": 0,
        "block_violations": 0,
        "block_examples": [],
        "e_examples": [],
    }

    for a in range(1, n):
        b = n - a
        for A in by_size[a]:
            for B in by_size[b]:
                stats["pairs"] += 1
                P = disjoint_union(A, B)
                ok, off = within_blocks(P, a, b)
                if not ok:
                    stats["block_violations"] += 1
                    stats["block_examples"].append((A, B, off))
                    continue
                cP = canon(P)
                fP = F[cP]
                Q = disjoint_union(dual(A, a), B)
                fQ = F[canon(Q)]
                R = disjoint_union(A, dual(B, b))
                fR = F[canon(R)]

                # e identity e(A||B) = C(a+b,a) e(A) e(B)
                if check_e:
                    lhs = linear_extensions(P)
                    rhs = _binom(n, a) * e_of_class(A, ecache) \
                        * e_of_class(B, ecache)
                    if lhs != rhs:
                        stats["e_violations"] += 1
                        stats["e_examples"].append((A, B, lhs, rhs))

                if is_self_dual(B, b, make_refined_canon(b)):
                    stats["restricted_pairs"] += 1
                    if fQ != fP:
                        stats["restricted_violations"] += 1
                        stats["restricted_examples"].append((A, B, fP, fQ))

                if fQ != fP or fR != fP:
                    stats["general_violations"] += 1
                    stats["general_examples"].append(
                        (A, B, fP, fQ, fR))

                if verbose and stats["general_violations"] and \
                        len(stats["general_examples"]) <= 3:
                    print(f"   general witness: A={A} B={B} "
                          f"F={fP} F(A^op||B)={fQ} F(A||B^op)={fR}")
    return stats


def _binom(n, k):
    if k < 0 or k > n:
        return 0
    num = den = 1
    for t in range(k):
        num *= n - t
        den *= t + 1
    return num // den


# --------------------------------------------------------------------------
# Driver.
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--max-n", type=int, default=6,
                    help="largest total size to check (default 6; 7 uses the "
                         "iso quotient, a few MB)")
    ap.add_argument("--no-e", action="store_true",
                    help="skip the linear-extension identity checks")
    ap.add_argument("--n7", action="store_true",
                    help="also run n=7 (default is n<=6)")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    nmax = 7 if args.n7 else args.max_n
    print("Disjoint-union reversal of F (exhaustive over isomorphism classes)")
    print("n | pairs | restricted pairs | restricted violations "
          "| general violations | e violations | block violations")
    for n in range(2, nmax + 1):
        st = verify(n, check_e=not args.no_e, verbose=args.verbose)
        print(f"{n} | {st['pairs']} | {st['restricted_pairs']} "
              f"| {st['restricted_violations']} "
              f"| {st['general_violations']} "
              f"| {st['e_violations']} | {st['block_violations']}")
        if st["restricted_examples"]:
            print("   restricted witnesses:",
                  st["restricted_examples"][:3])
        if st["general_examples"]:
            for A, B, fP, fQ, fR in st["general_examples"][:3]:
                print(f"   general witness: A={A} B={B} "
                      f"F={fP} F(A^op||B)={fQ} F(A||B^op)={fR}")
        if st["e_examples"]:
            print("   e witnesses:", st["e_examples"][:3])
        if st["block_examples"]:
            print("   block witnesses:", st["block_examples"][:3])
    print()
    print("Reference iso-class counts:",
          {k: A000112[k] for k in range(nmax + 1)})


if __name__ == "__main__":
    main()
