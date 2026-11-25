# referee-sergeev-ceiling-accounting-20261027

## status

investigated

## origin

executive_manual_dispatch

## agent_id

17ONIr75wtuJviiDS2T9DX-growled

## exit_state

succeeded

## question

Must all four claims of the 2026-10-27T18:23:29Z Sergeev ceiling-loss board post (R1 outcome-invariant leaf frames via hook formula, R2 interleaved pending/inserted counterexample 45/36 vs 27, R3 linear single-element framed-reset ceiling loss ~0.2214n, R4 O(n/log n) group-granularity stage count refuting the excess-forcing arm) independently re-derive as stated, or does referee analysis find defects?

## basis

Antonina #301 comment antonina-sergeev-ceiling-audit 2026-10-27T18:23:29Z; ledger front sergeev-canonical-ceiling-audit investigated finding; SoringP1 AGENTS.md independent-check discipline; prior referee pattern for merge and insertion checkpoint bounds.

## falsifier

Independent reconstruction of the FJ pair-poset extension enumerator, hook-formula application, asymptotics and stage-count arithmetic; verdict VERIFIED/REFUTED/AMBIGUOUS per Ri with exact corrections, referee code committed on its worktree branch.

## implication

Determines whether the sole known o(n)-surplus sorter clears the Oct-27 ceiling-loss necessary conditions (clearing a certification path toward exact-height SORT-BOUND-U certificates) or whether the accounting has an arithmetic defect that reopens the front.

## finding_unverified

Recovery check first: the verdict has not been posted and no commit has been made. The worktree is still on the requested referee branch with no repository changes; the independently written scratch enumerator is only under `/tmp/opencode/ref`. Its initial candidate frame interpretation did not match R1, so I was refining the model when interrupted. I’ll continue from there and won’t repeat any board post or commit unless the verification is complete.
The B-model run reaffirms that the front's R1 model is not just “materialized chain plus pending αᵢ<βᵢ”; the missing constraints still need to be identified. The `β_J < α_p` candidate also failed, so I’m not treating either as the intended frame. I’ll repair the script's smaller implementation errors, inspect the prior frame definitions, then publish only if I can state the model unambiguously.
The exhaustive-permutation bug is fixed by directly generating topological orders of the materialized subposet (instead of permuting all elements and filtering). Now R1's expected hook factors are testing the actual FJ pair-poset model.
The corrected FJ model now reproduces R1: once the winner chain is constrained in the materialized order, all prefix/suffix boundary variants have the hook-product count. R2 also reproduces the quoted counts; there are additionally leaves with the naive value 27. I’m now assembling the reproducible audit and checking the asymptotic and recursion arithmetic.
The quantitative checks are complete. R1’s hook count and R2’s full distribution both reproduce. R3’s exact constant is a dyadic-endpoint asymptotic, not a uniform all-\(n\) equality: the phase at \(m=3\cdot2^{q-1}\) adds a linear term, while the claimed linear lower-bound coefficient remains valid. R4’s sublinear pure-rounding conclusion survives, but the per-level prefix stages and numerical table need the qualifications described in the verdict.
I found seven later board comments but none is a referee verdict on this audit, so no duplicate post exists. I’ve committed the independent checker as `7b89ef50`; I’ll now post the single verdict, explicitly separating pure ceiling loss from Sergeev’s module overhead and the exact-reset question.
The board-post command returned no visible confirmation, so I’m checking the durable board record before taking any further action. I will not retry the post unless the board confirms it did not land.
Posted one referee verdict to Antonina #301: **R1 VERIFIED; R2 VERIFIED with the full `{27: 3, 36: 9, 45: 12}` distribution; R3 REFUTED as an all-\(n\) equality, though its linear lower-bound conclusion survives; R4 VERIFIED for pure ceiling rounding with scope corrections.**

The independent checker is committed on `research/referee-sergeev-ceiling-accounting-20261027` at `7b89ef50d74907746d886301865b70a3240a3475` (`scripts/referee_sergeev_ceiling_audit.py`). It ran successfully, and the worktree is clean. The single posted verdict is recorded as `sha256:gx6MKMwVhrozGz41PUuhxxHwfqPzmGnhVFS1ZhkPOIM`.

## Other metadata

```json
{
  "finished_at": 1793135634.825248,
  "started_at": 1793125633.0846543
}
```
