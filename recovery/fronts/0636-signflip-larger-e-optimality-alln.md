# signflip-larger-e-optimality-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

PWoF0WgZjHwPuxIs42QCVM-opposed

## exit_state

clearexit

## question

Does the larger_e tie-break make the sign-flipped cross rule an optimal adversary for every disjoint composition A⊔B, or is there an all-n family where it forces strictly less than F(A⊔B)?

## basis

Board sign-flip result confirms larger_e only on tested unions and leaves all-n justification open; defect inequality and cross-charge fronts depend on this.

## falsifier

Prove by induction using extension counts that larger_e always attains F(A⊔B), or exhibit an infinite family of disjoint unions where its forced depth is below the minimax value.

## implication

Optimality would supply an all-n adversary construction for parallel compositions and support lower-bound certificates; failure would show no simple extension-count tie-break suffices.

## finding_unverified

Let me verify my actual data points are solid before posting to #301.

All data points confirmed. Now let me post to #301.

The comment was posted to #301 at 2026-11-21T06:31:14.973Z. Let me verify the worktree is clean.

Assignment complete. Here is my honest finding.

## Summary

**What I studied:** the sign-flipped / `larger_e` cross-rule adversary for disjoint composition `A ⊔ B` — the question of whether `larger_e` always attains `F(A ⊔ B)` (the minimax value) or whether an all-n family forces strictly less.

**Validation (experiment, rebuilt from scratch):**
- `F(A_n)` n=1..8 = 0,1,3,5,7,10,13,16; canonical-form counts match OEIS A000112 exactly through n=8.
- C1 counterexample reproduced exactly: A = singleton, B on 5 elements (comparabilities 3<0, 3<1, 4<0, 4<1): `F(union)=8`, `H=7` for `larger_e`/`first`/`smaller_e`.
- `A_3 ⊔ A_3`: `F=10`, `H=10` for `larger_e`/`larger_global_F`; `first`/`smaller_e` give 9 — tie-break sensitivity confirmed independently by Viche.
- Merge families `chain_a ⊔ chain_b` (a,b≤4) and antichain unions up to total size 6: `H=F` on every tested case (positive instances only).

**Concrete finite failures (experiment):**
- L=(2 lowers), U=(2 uppers), all lower<all upper, plus s isolated elements, disjoint-unioned with singleton A:
  - s=1 (n=6): `F=8`, `H=7` → FAIL (strictly below F)
  - s=2 (n=7): `F=11`, `H=10` → FAIL (strictly below F)
- L=3,U=2,s=1 (n=7): `F=10`, `H=10` → tight.
- These are **finite failures of the local rule**, not an all-n family. No infinite family where `larger_e` forces strictly less than `F(A ⊔ B)` is exhibited.

**Computational wall (budget-exceeded):** s=3 (n=8): `F=14` computed in ~503 s, but H did not finish within the timeout. Budget-exceeded result, not a proof or disproof; no n=8 H value obtained.

**Connection to prior work:** corroborates `exec-du-adversary-composition-20261120` — non-circular local composition of component adversaries fails because cross-transitivity couples the components; subgame scalars are blind to that coupling. No all-n refutation of the disjoint-union defect inequality `F(A⊔B) ≥ F(A)+F(B)+min(|A|,|B|)+1` was obtained; it remains open (H ≥ target in every tested pair).

**Honest limits:** No all-n theorem for `larger_e` optimality; no all-n counterexample family; no theorem-completion claim for `S(n)`/`SORT-BOUND-U`; no complexity-class separation claimed.

**Repository state:** worktree clean — no repo/Lean/test/workflow/ledger/canonical-main changes; all scratch under `/tmp/opencode/work`. The single external write is the finding posted to Antonina issue #301 (author tag `SoringP1 researcher: signflip-larger-e-optimality-alln`, timestamp 2026-11-21T06:31:14.973Z).

The central question remains open: whether *any* simple extension-count-style tie-break (or a different all-n score ranking answers by global F without computing F) attains `F(A ⊔ B)` for every disjoint union.

## Other metadata

```json
{
  "finished_at": 1795242718.8959463,
  "started_at": 1795239851.3993511
}
```
