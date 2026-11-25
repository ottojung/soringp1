# Exact-reset tree realizability: a branch divisibility obstruction

**Date:** 2026-10-27
**Status:** paper proof; no Lean formalization or experiment needed.

## Exact stage model

For a poset `P` on `n` labelled keys, `Ext(P)` is its set of linear
extensions and `e(P) = |Ext(P)|`. An exact reset stage from `F` to `F'` is a
comparison tree rooted at `F` such that every reachable leaf has, after its
allowed slot framing, certificate extension set exactly `Ext(F')`. A frame is
a bijective relabelling, so each reachable leaf class contains exactly
`e(F')` original input orders. Reachable leaf classes are disjoint and
partition `Ext(F)`. This is the exactness condition in the question; merely
forgetting extra leaf relations is not an exact reset.

## Counterexample family

Let `F = A_n` be the antichain. Let `F' = V_n` be the star poset with one
element `a` below each of the other `n−1` elements and no relations among
those other elements. For `n ≥ 3`, these posets are not isomorphic, and

\[
e(A_n)=n!,\qquad e(V_n)=(n-1)!,\qquad e(A_n)/e(V_n)=n.
\]

Thus the extension-count arithmetic calls for exactly `n` leaf certificate
classes, each of size `(n−1)!`; the elementary leaf-count lower bound asks for
height at least `ceil(log₂ n)`.

**Theorem (odd-order antichain-to-star reset is impossible).** For every odd
`n ≥ 3`, there is no exact reset comparison tree from `A_n` to `V_n`, at any
height.

**Proof.** A reachable leaf class has size exactly `(n−1)!`. At the root,
every comparison is between two incomparable keys. Exactly half of the `n!`
linear orders put the first key before the second, and half put them in the
opposite order. Therefore each root outcome contains `n!/2` input orders.
All descendant leaf classes under that outcome are disjoint and each has
size `(n−1)!`; consequently their union can have size only an integer
multiple of `(n−1)!`. But

\[
\frac{n!/2}{(n-1)!}=\frac n2
\]

is not an integer when `n` is odd. This contradicts the requirement that the
root outcome's orders all reach leaves. Slot framing cannot repair the
obstruction because it preserves cardinalities. The argument does not depend
on stage height or on how isomorphic sub-branches are duplicated. ∎

### Minimal instance `n=3`

Take `F=A_3` and `F'=V_3`, with relations `a<b` and `a<c`. Then
`e(F)=6`, `e(F')=2`, and the exact ratio is `3`. An exact reset would have
three leaves of two orders each. The first comparison splits the six orders
into two groups of three; neither group can be partitioned into two-order
leaf classes. So the count ratio is integral and gives the usual two-level
leaf-count lower bound, but no legal first comparison can begin an exact
reset tree.

## Consequence and limits

**Deduction:** extension-count divisibility for the whole transition is not a
sufficient realizability criterion. A necessary condition must also account
for the masses induced by the root comparison (and, recursively, by later
comparisons). This is a branch-level divisibility obstruction; it already
arises before requiring isomorphic continuation subtrees. It answers the
stated exact-transition question negatively, but is not a lower bound on
`S(n)`, does not constrain non-exact/forgetful certificate joins, and does
not characterize all realizable transitions.

The known `n=2` slot-name-swap reset is consistent: `A_2` to a two-element
chain has two singleton leaf classes, and each root outcome has size one.

**Evidence labels:** the extension counts are direct combinatorial
calculations; the odd-`n` obstruction is a paper proof from the exact-reset
definition and the balanced first comparison of the antichain. No external
sorting theorem is used.
