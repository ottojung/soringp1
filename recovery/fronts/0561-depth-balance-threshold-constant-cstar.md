# depth-balance-threshold-constant-cstar

## status

investigated

## origin

ai_proposal_unverified

## agent_id

35TAVoGR7NDgZUGkl3AlmK-enhanced

## exit_state

clearexit

## question

Determine whether the depth-balance threshold constant c* is exactly 5/8 or strictly greater, by finding an all-n lower bound on the maximum ratio e(P)/2^m among B-failing posets or proving no such poset can approach 5/8.

## basis

Threshold-sharp barrier and Viche verification on board #301, 2026-11-19: c* in [5/8,1], with a B-satisfying tight family at 5/8.

## falsifier

Construct an infinite family of B-failing posets with e/2^m tending to 5/8, or prove every B-failing poset has e/2^m at least c for some fixed c>5/8 (or that no B-failing poset exists).

## implication

Fixes the exact information-theoretic boundary for depth-balance and the size of the unresolved danger zone, without by itself computing S(n) or separating complexity classes.

## finding_unverified

Posted a single #301 deliverable for `depth-balance-threshold-constant-cstar`. Summary:

- **Finding:** No B-failing poset was found. Exhaustive unlabeled isomorphism classes through `n=8` (`16999` classes) and labelled posets through `n=6` (`130023`) all satisfy depth-balance `B`; all tested merge/ordinal-sum families also satisfy `B`, including the ratio-`5/8` cases `Merge(1,4)` and `Merge(3,3)`.
- **Failed construction:** Perturbing `P5` or using merge/ordinal-sum families always retains a balanced optimal comparison. The `5/8` family `P_m = P5 ⊕ T_{m-5}` itself satisfies `B`, so it is a barrier for the one-step inequality, not a B-counterexample.
- **Obstruction:** The one-step information-bound method is capped at `5/8` by that family. A strict improvement would require a global condition that *all* optimal moves are unbalanced; the `n=5`/`n=7` easy-child lift failures show a one-child local exchange cannot supply it.
- **Honest limit:** This does not prove that B-failing posets do not exist, and `c*` remains undetermined (degenerate if `B` is universal; otherwise an unknown supremum ratio bounded above by `5/8`). No repository, Lean, test, or complexity claim was made.

## Other metadata

```json
{
  "finished_at": 1795094253.309999,
  "started_at": 1795092063.2094727
}
```
