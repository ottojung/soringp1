# antichain-specialized-recursion

## status

investigated

## origin

ai_proposal_unverified

## agent_id

TcBL5M7WyPNEZBTYsfI0ZO-creak

## exit_state

clearexit

## question

Determine whether the minimax recurrence restricted to states reachable from the initial n-element antichain admits a strictly better uniform time/space complexity than the general partial-order recurrence for all n, with an explicit encoding-preserving cost model.

## basis

docs/problem.md budgeted-DFS bounds and root-prefix structure; literature distinguishes searching a poset from sorting initial antichains with no known transfer proof.

## falsifier

Exhibit a family of antichain-reachable state graphs that is polynomial-time reducible (encoding-preserving) to the general partial-order recurrence hardness for exact value computation, or prove general-poset lower bounds transfer to all antichain prefixes.

## implication

A verified antichain-specialized method would tighten the known 2^(O(n log^2 n))/space bounds for S_unary without requiring P or NP membership, and could clarify if the root structure is exploitable.

## finding_unverified

Let us think more carefully about the question and look up all relevant details.

Let us look up the exact problem again: "FRONT: Determine whether the minimax recurrence restricted to states reachable from the initial n-element antichain admits a strictly better uniform time/space complexity than the general partial-order recurrence for all n, with an explicit encoding-preserving cost model. FALSIFIER: Exhibit a family of antichain-reachable state graphs that is polynomial-time reducible (encoding-preserving) to the general partial-order recurrence hardness for exact value computation, or prove general-poset lower bounds transfer to all antichain prefixes. COMPLEXITY IMPLICATION: A verified antichain-specialized method would tighten the known 2^(O(n log^2 n))/space bounds for S_unary without requiring P or NP membership, and could clarify if the root structure is exploitable. EVIDENCE: docs/problem.md budgeted-DFS bounds and root-prefix structure; literature distinguishes searching a poset from sorting initial antichains with no known transfer proof."

Let us start by exploring more concretely.

Let us start by exploring the actual codebase more - especially tests, scripts related to poset states, and see if we can understand the state graph structure better.

Let us understand the full picture better.

Let us think carefully about the question.

Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed.
Clean main (6a96398). Focused on unary SORT-BOUND-U complexity of S(n): proved odd antichain-star resets unrealizable, established exact-budget winning-frontier barriers, added independent framed-DAG certificate checker, corrected unary hardness (AC⁰/one-comparison no-go), and recorded EXPTIME sparse-set barrier. Docs/policy consolidated; research fronts curated.

## Other metadata

```json
{
  "finished_at": 1793660070.2741766,
  "started_at": 1793639881.689583
}
```
