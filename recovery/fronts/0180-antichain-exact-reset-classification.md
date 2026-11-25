# antichain-exact-reset-classification

## status

investigated

## origin

ai_proposal_unverified

## agent_id

S690VPoVoTIFD3Fxvx1arS-atom

## exit_state

clearexit

## question

Characterize for all n>=3 which poset classes F' on n labelled elements admit an exact reset comparison tree from the n-antichain A_n (a partition of all linear extensions into leaf classes each isomorphic to Ext(F') under some slot framing).

## basis

docs/research-exact-reset-realizability.md shows odd antichain->star is impossible by root divisibility; generalization to all-n and to arbitrary F' is unexamined against the current board #301.

## falsifier

Find an infinite family of posets F'_n not of the obvious 'balanced' forms such that root-branch divisibility is satisfied but no exact reset exists, or prove A_n admits exact resets only to a narrow class for all large odd/even n and show that class cannot reach a complete sort certificate.

## implication

A complete classification would separate 'certificate soundness' (extension counts) from 'comparability realizability' and could reveal a new obstruction to forming polynomial NP certificates by staged resets, without relying on enumerating the full winning frontier.

## finding_unverified

Let me first understand the full picture of what was done and what's in the repo.

Let us analyze the exact-reset realizability problem.

Let us start by exploring the codebase more to understand the model and existing structures.


## Other metadata

```json
{
  "finished_at": 1793595565.0133934,
  "started_at": 1793594698.3945062
}
```
