# linear-extension-sampling-lower-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

0UEGVs5RxXQ2WpEeVaYPHV-mist

## exit_state

clearexit

## question

Does approximate uniform sampling of linear extensions of states on any optimal sorting strategy require super-polynomial time for all-n, creating a barrier to certain randomized certificate approaches?

## basis

Brightwell–Winkler show counting linear extensions is #P-complete in general; transfer to antichain-reachable states is nontrivial and must be all-n.

## falsifier

Give a polynomial-time approximate uniform sampler for all states reachable by some optimal strategy for all n, or prove it would imply collapse of counting classes.

## implication

If sampling is hard, randomized polynomial-size certificates appear unlikely; this distinguishes counting complexity from decision complexity without claiming #P-hardness of S(n) directly.

## finding_unverified

Let us look up the frontier and literature.
Let us proceed.

Let us start by exploring the codebase more for how optimal strategies/states are modeled, and also look up Brightwell–Winkler construction details if possible from docs.

Let us look up how "states on optimal strategies" are characterized.

Let us write up the analysis.

The task says "on billy-dev ONLY" and to report to board #301 etc. But I need to follow the exact instructions - report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof. I should report honestly as above. The instructions say "Report honest limits" and "Do not create Lean or repository changes without a genuinely substantive..." - so probably just report findings. Let us also add precise citations.The FRONT claim is falsified. Bubley–Dyer give a polynomial-time (FPRAS) approximate uniform sampler for linear extensions of *all* finite posets; "states on some optimal sorting strategy" form a subset, so easiness transfers. Brightwell–Winkler is exact counting (#P-complete), but approximate sampling/counting is easy. The alleged barrier disappears. No obstruction found for all-n; complexity distinction is exact vs approximate, not a source of super-polynomial barrier here.


## Other metadata

```json
{
  "finished_at": 1793355204.1732328,
  "started_at": 1793354053.5373342
}
```
