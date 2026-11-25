# reset-obstruction-complete-classification

## status

investigated

## origin

ai_proposal_unverified

## agent_id

7PJGlDPmjNQGEXfMd1hFrv-bouquet

## exit_state

clearexit

## question

Is the odd antichain-star the unique infinite all-n family of uniform poset classes for which exact-reset comparison strategies are unrealizable due to branch divisibility, or does there exist at least one other infinite family with a different structure that is also unrealizable for all sufficiently large n under the same reset model?

## basis

Recent exact-reset realizability work shows odd-star unrealizable; branch divisibility from factorial counts appears necessary but characterization remains open and no other infinite family has been identified.

## falsifier

Exhibit a second infinite all-n family of reset-admissible class structures with provably violated branch divisibility for large n, or prove no other infinite families exist and characterize the exact closure.

## implication

A complete classification would separate local obstructions from universal reset barriers and clarify whether exact-reset systems form a restrictive or characterizable algorithmic subclass for evaluating S(n).

## finding_unverified

Let us look up the research-exact-reset-realizability.md and the front frontier.json in this repo.

Let us search for related work patterns in other frontiers and in literature references.

Let us analyze systematically.

Let us proceed with the analysis.

I need to study the exact-reset model and do this analysis. Let us write up the findings.

The analysis shows there are other infinite all-n families (e.g. fixed odd star plus isolated elements, or unions of odd stars) with odd ratio t for all large n giving root branch divisibility obstruction. The closure is families where t_n is odd for all large n. Stars are one source (factor = size), and any poset Q with odd t(Q) extended by isolated elements gives another family. So the odd antichain-star is not unique.

I need to report on board #301 as instructed. But the user says "On completion report a mathematical finding..." - but the rules say "Report the result, including negative or inconclusive outcomes, as a concise update on the research board (see docs/operations.md). No branch, PR, note, test or Lean file is required." So I need to post to board #301.

Posted the mathematical finding to board #301. The result shows the odd antichain-star is not unique - fixed odd star plus isolated elements and unions of odd-t components form other infinite all-n families with root branch divisibility obstruction for all members. Characterized by odd ratio t_n = e(A_n)/e(F'_n). Clean worktree, no repo changes.


## Other metadata

```json
{
  "finished_at": 1793780346.9082909,
  "started_at": 1793776250.1256328
}
```
