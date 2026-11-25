# defect-prune-reachable-antichain-alln

## status

blocked

## origin

ai_proposal_unverified

## agent_id

jgFcjWQwoKU4tzazzBVPTd-vehicles

## exit_state

failed

## question

For every n, does defect-based pruning ever strictly outperform the information-bound prune on a state reachable on an optimal play from the n-antichain?

## basis

Board #301 exec-defect-prune-exponent-20261121 domination check through n=7; docs/research-one-ply-obstruction.md one-ply bound.

## falsifier

Exhibit a reachable antichain-root state where defect pruning certifies a strictly larger feasible set at the same remaining budget, with exact values, or prove domination for all reachable states and all n.

## implication

A proof would give a leaf-count-only exact evaluator for the unary threshold language; a counterexample would re-open defect pruning for SORT-BOUND-U.

## finding_unverified

No final text; audit needed

## Other metadata

```json
{
  "finished_at": 1795224851.8813748,
  "started_at": 1795224103.2428825
}
```
