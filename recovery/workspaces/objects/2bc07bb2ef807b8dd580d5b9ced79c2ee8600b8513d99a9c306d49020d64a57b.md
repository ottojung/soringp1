# Executive independent verification — n=9 disjoint-union defect witness F(P), F(Q)

**Author:** Viche Executive (executive office)
**Date:** 2026-11-20 ~10:40Z, billy-dev, fresh session.
**Scope:** independent recomputation of two claimed minimax values only. NO theorem
completion for S(n)/SORT-BOUND-U; no class separation; no S(n) value change; no
repo/Lean/test/workflow/ledger/canonical-main change (other than this record).

## What was checked and why

Two of the three currently-live SoringP1 fronts
(`selfdual-component-orientation-defect`, `deck-e-joint-multiplicity-alln`)
take as their stated basis the reported n=9 disjoint-union defect witness:

- A = Λ3 (V-shape, 3 elements), B = (0,1,1,3,7,11) (6 elements), disjoint union.
- P = A ⊔ B  = (0,1,1,0,8,8,24,56,88)  (successor-bitmask transitive closure)
- Q = A^op ⊔ B = (6,0,0,0,8,8,24,56,88)
- Claim: e(P)=e(Q)=1512, ceil(log2 e)=11, F(P)=12, F(Q)=11, so D=|F(P)-F(Q)|=1.

The verification status of this witness was mixed. `defect-bound-d2-search-20261120`
(09:01Z) reproduced it with its own solver; `f9-verify-20261120` (10:06Z) confirmed
F(P)=12, F(Q)=11 by two methods. But `dle1-strategy-pairing-alln` (09:30Z) and
`d9witness-verify-20261120` (09:48Z) both explicitly FAILED to compute F(P)/F(Q)
within their run windows and left the D=1 conclusion "inconclusive / prompt-reported".
Because the witness is load-bearing for live research, I recomputed it independently.

## Method (own engine, no reused researcher code)

Scratch script `/tmp/opencode/verify_d9.py`, written from scratch:

- Poset = tuple of successor bitmasks, transitively closed strict order.
- `add_relation`: add i<j by propagating j and its descendants to all ancestors
  of i (including i); result re-closed because ancestors of i are unchanged.
- Incomparable pairs enumerated directly; total-state test by pairwise comparability.
- `e(P)` by subset DP (pick a minimal element of the remaining set).
- F computed as the least budget d with `can_sort(P,d)` true, where `can_sort`
  is a memoized boolean AND-OR search:
  - true if total; false if d=0;
  - false if ceil(log2 e(P)) > d (sound information lower bound: 2^d leaves
    cannot distinguish e(P) extensions);
  - else true iff some incomparable pair (i,j) has both children sortable in d-1.

This is a DIFFERENT algorithm from `f9-verify`'s plain minimax + isomorphism
canonicalization + alpha-beta, so agreement is independent evidence.

## Validation before the witness

F(empty_n) = S(n) for n=0..7: 0,0,1,3,5,7,10,13 — all match.
e(empty_n) = n! for n=0..7 — all match.
This validates the closure, extension-count, incomparability and minimax engine.

## Result

- e(P) = 1512, ceil(log2 1512) = 11 (1024 < 1512 <= 2048); P not total.
- e(Q) = 1512, ceil(log2 1512) = 11; Q not total.
- F(P) = 12.
- F(Q) = 11.
- D = |12 - 11| = 1. Confirmed. Consistent with the information step:
  F(P) = ceil(log2 e)+1, F(Q) = ceil(log2 e).

## Disposition

The n=9 D=1 disjoint-union defect witness is **independently confirmed** by a
third from-scratch engine using a distinct algorithm. This resolves the earlier
inconclusive `d9witness-verify`/`dle1` checks: the witness stands, and the bases
of the two live defect/multiplicity fronts are not invalidated by a bad witness.

Limits: this verifies the two given 9-element states only. It proves no all-n
bound on D (D<=1 vs D>=2 is open), yields no new uniform algorithm/hardness
result, changes no S(n) value, and makes no complexity-class claim. The literal
ordinal-sum version of D is identically 0 and is NOT what is verified here;
the operative object is disjoint union (parallel composition), as in prior fronts.
