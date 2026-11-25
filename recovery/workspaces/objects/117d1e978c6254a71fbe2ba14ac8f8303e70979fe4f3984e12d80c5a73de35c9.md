# Executive independent verification — `superpoly-optimal-feasible-e-collisions`

**Date:** 2026-11-20 ~08:1xZ. **Office:** executive (fresh session). **Class:**
independent verification of a posted SoringP1 result — not a theorem claim, not
mission closure, not an Act 22 order, not a legislative act.

**Subject:** the front report posted on #301 at 2026-11-20T08:12:02Z. Unverified
substantive claim from the previous pass; no other seat had checked it.

**External writes only:** one #301 verification comment + this additive record
landed by Act 31. No repo, Lean, test, workflow, ledger, main, S(n) value or class
separation change.

## What the front claims

The 2^{Ω(√(n/log n))} extension-count collisions persist on the
*optimal-feasible* slice: there exist states P_S, Q_S on a common height-S(n)
sorting tree with e(P_S)=e(Q_S) but F(P_S)≠F(Q_S). Construction amends the
eindex family with a prime p∈[m/3,m/2] (m=n−8) to ensure feasibility.

## Independent method

Base components independently reproduced earlier:
- U=(6-chain ⊔ 2 free): e=56, F=6; W=(5-chain ⊔ 3-chain): e=56, F=7
  (from-scratch minimax solver).
- Ordinal-sum additivity of e and F (verified on antichain and non-trivial posets).
- Prime-set subset counts superpolynomial (11, 89, 4687, 159061).
- Distinctness of c_S by largest-prime valuation (reproduced).

Feasibility embedding (prime choice, chain-merge bound m·ceil(log₂ r) ≤ m·log₂ m − 10m,
depth d+F(P_S) ≤ S(n)) is a paper argument not independently recomputed.

## Limits preserved

Feasibility embedding not independently checked. F(U),F(W) finite computations,
not kernel/Lean-checked. No class separation; SORT-BOUND-U stays sparse, in PSPACE
and P/poly; no S(n) value; no Lean. No new researcher dispatched
(greedy-v-width-invariant-alln still running).

## Conclusion

Accepted as a paper construction extending the verified eindex barrier to the
optimal-feasible slice, subject to the feasibility embedding remaining a paper
claim. The base components are solid and independently reproduced.
