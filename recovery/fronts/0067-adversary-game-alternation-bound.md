# adversary-game-alternation-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

FvfrDPAKjEJa3x1fY6B9kq-resigned

## exit_state

clearexit

## question

For the natural minimax game for S(n) with alternation depth equal to the decision depth, does there exist an all-n strategy-compression that reduces alternation to O(log n) blocks without exponential certificate blowup?

## basis

Claim A gives polynomial alternation ATM; PH fixed-level membership remains open and no compression obstruction has been established as an all-n theorem.

## falsifier

Prove an all-n lower bound showing that any strategy representation achieving fixed or logarithmic alternation blocks requires super-polynomial size or is unsound for some optimal adversary policy.

## implication

Logarithmic alternation would place SORT-BOUND-U in a lower class within PSPACE (closer to PH), while a strong compression obstruction would delimit PH-membership routes without yielding P!=PSPACE.

## finding_unverified

 k" - it's deterministic, no alternation. That doesn't fit.

Alternatively, if you don't have the full DAG but some compressed representation, maybe you need to verify it with alternation?

Alternatively, let us look up the board #301 again - the user said "study AGENTS.md, docs/problem.md and current board #301" and gave this task. But I'm doing this as an agent now - maybe this is the task I need to solve? Let us look up the current front on board #301 more. The front in the ledger says "adversary-game-alternation-bound" is currently running with agent FvfrDPAKjEJa3x1fY6B9kq-resigned. But the user says "FRONT: ..." which matches exactly that front. So maybe I'm supposed to work on this front right now? Let us read the full task again carefully.

The user says: "On billy-dev ONLY, study AGENTS.md, docs/problem.md and current board #301. Study the primary literature, attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n), and try seriously to DISPROVE it. Distinguish general-poset results and certificate SOUNDNESS from completeness. Do not create Lean or repository changes without a genuinely substantive, independently checkable new theorem or counterexample. Report honest limits. 
FRONT: For the natural minimax game for S(n) with alternation depth equal to the decision depth, does there exist an all-n strategy-compression that reduces alternation to O(log n) blocks without exponential certificate blowup?
FALSIFIER: Prove an all-n lower bound showing that any strategy representation achieving fixed or logarithmic alternation blocks requires super-polynomial size or is unsound for some optimal adversary policy.
COMPLEXITY IMPLICATION: Logarithmic alternation would place SORT-BOUND-U in a lower class within PSPACE (closer to PH), while a strong compression obstruction would delimit PH-membership routes without yielding P!=PSPACE.
EVIDENCE: Claim A gives polynomial alternation ATM; PH fixed-level membership remains open and no compression obstruction has been established as an all-n theorem.
If resuming after an infrastructure failure, inspect earlier work and avoid repeating side effects or claims. 
On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof." 

This reads like instructions for the task - I need to do this research. Let us proceed.
Let us analyze this carefully.

Let us look up the literature more. Maybe related to "round elimination", "strategy compression", or to the fact that for some games you can reduce rounds. Or perhaps related to the "alternating complexity" and "block complexity".

Let us look up what others have done - the ledger says agent FvfrDPAKjEJa3x1fY6B9kq-resigned is running on this front. But maybe I need to do it myself now. Let us think deeply about the question.

Let us analyze this systematically.

Let us start by exploring this systematically.

The analysis suggests the falsifier's claim is likely true: the combination of (a) no state-sharing for single optimal policies (distinct poset states per node, tree of size 2n!-1) and (b) exponentially many winning states in the frontier barrier makes polynomial-size strategy representations with few alternation blocks infeasible for completeness/soundness. However, the exact mapping between "alternation blocks" and these structures needs formalization, and no complete proof was achieved. No repo or Lean changes were made per the publication gate.

## Other metadata

```json
{
  "finished_at": 1793384335.5168588,
  "started_at": 1793376302.047521
}
```
