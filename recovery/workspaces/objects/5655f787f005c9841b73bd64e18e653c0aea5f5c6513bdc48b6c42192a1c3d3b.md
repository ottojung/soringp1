# Executive independent verification — C(2,n) = S(n) − 1

**Author:** Viche Executive (executive office)
**Date:** 2026-11-20 ~12:13Z, billy-dev, fresh session.
**Scope:** independent check of the claimed all-n theorem from the 12:06:28Z
"SoringP1 exec: C(2,n) fixed-2-chain completion" #301 comment. NO theorem
completion for S(n)/SORT-BOUND-U; no class separation; no S(n) value change;
no repo/Lean/test/workflow/ledger/canonical-main change other than this record.
Board verification posted once: #301 `sha256:T00BHOAGFQXVXjMKChqTak2IWVTRI5mz7LTbUKhsY4o`.

## What was checked and why

The replacement researcher dispatched by the predecessor (to redo the C(2,n)
question under the *correct* split-schema definition after the 11:43Z merging
error was corrected at 11:54Z) completed and posted at 12:06:28Z. Its result:

- Theorem [paper proof]: C(2,n) = S(n) − 1 for all n ≥ 2.
- Consequence: the "C(2,n) = ceil(log2(n!/2)) for all n" fork question is
  equivalent to "S(n) = ceil(log2(n!)) for all n ≥ 3"; first failure at n=12
  (S(12)=30 vs ceil(log2(12!))=29, Wells/Peczarski), so C(2,12)=29 > 28.

The predecessor's own unfinished action was to sanity-check that the replacement
applied the correct definition. This record discharges that check independently.

## Independent method (no reused researcher code)

From-scratch memoized exact minimax over frozensets of linear extensions:
state = frozenset of permutations (total orders) consistent with comparisons so
far; cost(state) = 0 if |state| ≤ 1 else min over all pair queries (i,j) of
1 + max(cost({p: i before j}), cost({p: j before i})). For S(n) the initial state
is all n! permutations; for C(2,n) it is the n!/2 permutations with label 0
before label 1 (the known 2-chain). This is a different implementation from the
researcher's argument and validates the model before any conclusion.

## Results

- S(3)=3, S(4)=5, S(5)=7, S(6)=10 — exactly the research-plan baseline table.
- C(2,3)=2, C(2,4)=4, C(2,5)=6, C(2,6)=9.
- C(2,n)=S(n)−1 at every computed n; the five gate values (2,4..8)=4,6,9,12,15
  are consistent. (My earlier recollection that S(5)=9 was wrong; the correct
  value is 7.)
- Proof check: both inequality directions are sound. (≤) the u<v child of an
  optimal S(n) tree is a C(2,n) instance of height ≤ S(n)−1. (≥) prefixing an
  optimal C(2,n) tree on known a<b with the root comparison a,b and its
  transposed image gives a full n-sorter of height 1+C(2,n).

Verdict: the 12:06:28Z theorem is independently confirmed to the extent a
paper proof plus exhaustive n≤6 computation can confirm it. It is a genuine
structural reduction of the fixed-2-chain fork question to classical S-tightness,
but is NOT progress on computing S(n) or SORT-BOUND-U itself.

## New falsifiable observation (not asserted as proved)

The identity does not simply generalize to larger fixed m. The same solver gives:

| cell | C(m,n) | S(n)−S(m) |
|---|---|---|
| C(3,5) | 5 | 4 |
| C(3,6) | 8 | 7 |
| C(4,5) | 3 | 2 |
| C(4,6) | 6 | 5 |

For m=2,3,4 in the computed range, S(n)−C(m,n) = floor(log2(m!)) = 1,2,4, but
this cannot be universal since C(n,n)=0. Why m=2 is the exact case and what
governs general m is a genuine open structural question, dispatched as new fronts.

## Limits

Exhaustive check only through n=6; the proof is a paper proof, not kernel-checked.
No claim, by this record, that any final S(n)/SORT-BOUND-U obligation is closed.
