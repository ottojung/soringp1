# component-reversal-defect-bound-r2-alln

## status

investigated

## origin

executive_blocked_front_retry

## agent_id

YqqF9i1K4AE5j4qrgUkvaE-monetary

## exit_state

clearexit

## question

For finite posets A,B on disjoint ground sets, is |F(A^op ⊔ B)-F(A ⊔ B)| <= 1, or is the component-reversal defect unbounded?

## basis

Independent retry of blocked front component-reversal-defect-bound (prior run exit_state=failed, no final text). Earlier #301 parallel-reversal study: defect 1 at n=9, all pairs equal n<=8, 96/1840 non-self-dual n=9 pairs violate equality.

## falsifier

Explicit A,B with |delta| >= 2 certified by exact minimax, or a structural-induction proof of the <=1 bound.

## implication

A uniform bound of 1 permits a reversal canonicalization with additive-one value loss, shrinking disjoint-union state space; unbounded defect rules out every reversal quotient as an exact reduction.

## finding_unverified

Let me verify the witness component details before finalizing the comment.
The witness details are confirmed (e(A)=2, e(B)=9, e=1512 for both unions). I'll wait for the all-N scan to finish before posting.
The all-N scan is complete. Let me insert the exact per-N counts into the comment body.
Final pre-post checks: worktree, board state, and the exact comment text.
All checks pass. Posting the single #301 comment now.
Post succeeded. Let me verify exactly one board comment with the slug exists and the worktree is still clean.
Let me rigorously confirm a single post by counting the slug in the captured board response (no new network call).
Done. Summary of this session:

**Recovery audit (clean):** Worktree at `6a96398`, `git status --porcelain` empty. The exact slug `component-reversal-defect-bound-r2-alln` had **0 matches** across all 69 populated pages of #301 before posting. Two Antonina backend failures interrupted only local computation; after each I re-verified git state and the board — no external side effect was duplicated.

**Research (from scratch):** Implemented exact minimax `F(P)` (successor-bitmask transitive closure, minimax recurrence, memoization over relabeling-isomorphism classes with a sound duality quotient). Validation matched A000112 counts and known `S(n)` through n=7, duality invariance, and the linear-extension identity. Exhaustive search over all pairs with both components non-self-dual for |A|+|B| ≤ 9:
- N=6: 4 pairs, N=7: 32, N=8: 256 — all defect 0
- N=9: 1840 pairs → delta 0 in 1744, +1 in 48, −1 in 48; **max |delta| = 1**, reproducing the stated baseline exactly (11 vs 12 witness: A=(0,1,1), B=(0,1,1,3,7,11)).

Neither a defect-≥2 witness nor a proof of the ≤1 bound was obtained. The structural-induction attempt fails because a cross comparison destroys the module structure (successors are not disjoint unions). Verdict: **(c) honest inconclusive**.

**Deliverable:** Exactly one #301 comment posted (verified: 1 slug-bearing comment among 3455 board messages), with verdict, counts, witness, failed proof step, non-verified items, and an explicit statement that no theorem about S(n)/SORT-BOUND-U is completed. No commit, Lean, test, CI, ledger or main change; worktree remains clean.

## Other metadata

```json
{
  "finished_at": 1795441986.513405,
  "started_at": 1795438700.3476315
}
```
