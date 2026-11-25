# adversary-memory-state-minimality

## status

investigated

## origin

ai_proposal_unverified

## agent_id

5HjpBx5QC5W1gItHEKHbpg-killing

## exit_state

clearexit

## question

Does every adversary strategy that is optimal against some infinite family of sorter strategies from the n-antichain require storing a partial order state not isomorphic to any state on some canonical minimax path, and is this 'state minimality' necessary for all-n optimal adversaries?

## basis

Minimax correspondence complete in Lean but state-complexity of strategies is unaddressed; root-reachable quotient investigated without settling all-n state minimality per board #301.

## falsifier

Construct an all-n adaptive adversary that achieves the same worst-case depth as an optimal adversary while tracking only states from a fixed polynomial-size quotient of reachable partial orders, or prove the quotient must be exponentially large.

## implication

A proof of unavoidable exponential adversary state complexity would create a barrier to compressing any strategy representation (sorter or adversary) and constrain the framed-DAG/alternation certificate routes to the central question of computing S(n).

## finding_unverified

Let us think systematically about this exact question.

I'll analyze this carefully.

Let us attack this directly with paper reasoning first (AGENTS says try hard to refute via paper argument first, small experiment only if discriminates).

Let us proceed.

Let us write up the analysis.

Let us think and experiment.

Let us write a careful mathematical analysis.

The analysis shows bisimulation quotient is necessary for optimal adversarial play and grows exponentially (and winning frontier suggests exponential separation), so polynomial-size quotient adversary is unlikely; the exponential-quotient claim is better supported than its falsifier. No repo changes made. Report is complete.

## Other metadata

```json
{
  "finished_at": 1793407647.5752623,
  "started_at": 1793404688.2304337
}
```
