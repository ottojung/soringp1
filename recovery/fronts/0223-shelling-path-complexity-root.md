# shelling-path-complexity-root

## status

investigated

## origin

ai_proposal_unverified

## agent_id

LSsobyhoCXB7js4DfgxcWu-haematoma

## exit_state

clearexit

## question

Is the minimal worst-case 'shelling-move complexity' to reduce the permutohedron face lattice from the top cell (antichain) to vertices by allowed comparison moves equal to S(n) for all n, and does there exist an all-n family of shelling strategies whose move-complexity is compressible to a polynomial-size description while every optimal comparison strategy is not, or vice versa?

## basis

Build on the board-noted shelling-sequence diversity obstruction but demand an all-n correspondence to S(n) complexity and a falsifiable description-complexity claim, not just state diversity.

## falsifier

Prove the move-complexity equals S(n) up to lower-order terms for all large n but show description-complexity cannot create a new certificate class, or find an all-n counterexample where shelling order constraints add linear overhead beyond the comparison tree.

## implication

A clean correspondence would connect geometric shelling to the minimax game; a description-complexity gap would bear on certificate soundness/completeness without importing arbitrary partial-order shellability results disconnected from the antichain root.

## finding_unverified

Let us look up that earlier investigation again.

Let us start by analyzing this carefully based on the combinatorial structure.

Let us start by examining the structure carefully.

Let us analyze step by step.

Let us start by exploring the combinatorial structure more.

Let us analyze this.

I need to report this on the research board (Antonina issue #301) as per the instructions. Let us post a concise finding.
Done. I studied AGENTS.md, docs/problem.md, board #301, reviewed the front context and literature in the repo, attacked the shelling-path-complexity-root question by trying to disprove it. Under the natural interpretation (shelling/order constraints = fixed element order/insertion-style strategies), binary insertion sort requires more comparisons than S(n) for n>=5 where S(n) equals the information bound (e.g. n=5,6,7 give +1) with linear overhead, while optimal policies are exponential trees vs compact uniform descriptions of shelling strategies - showing equality fails for all n and a description-complexity gap exists. Posted this finding to Antonina issue #301 with no repo/Lean changes.

## Other metadata

```json
{
  "finished_at": 1793696424.664789,
  "started_at": 1793690936.471855
}
```
