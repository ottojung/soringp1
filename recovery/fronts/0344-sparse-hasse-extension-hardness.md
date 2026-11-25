# sparse-hasse-extension-hardness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

UM9QxzTELaNwKkItaSNPVM-heartily

## exit_state

clearexit

## question

Is counting linear extensions #P-hard under Turing reductions for n-element posets whose Hasse diagram has at most C n log n cover relations, for some absolute constant C?

## basis

Board #301 shallow-state correction (2026-11-08) explicitly leaves intrinsic sparse-Hasse #LE hardness open; cover relations increase by at most one per comparison, so depth-S(n) reachable states are intrinsically sparse; Brightwell-Winkler (STOC 1991) give general #P-completeness; S(n)=O(n log n) from merge sort.

## falsifier

Give a uniform polynomial-time algorithm that counts linear extensions exactly for every n-element poset with at most C n log n cover relations, or prove this restricted counting problem is in FP.

## implication

Every poset reached from the n-antichain at depth at most S(n) has at most S(n)=O(n log n) covers, so hardness here would make the Fibonacci extension threshold unusable as a polynomial-time state-local prune on the reachable class unless PP collapses; a polynomial-time counter would reopen that route for exact S(n).

## finding_unverified

duplicate acknowledged, no external effects

## Other metadata

```json
{
  "finished_at": 1794114755.3805313,
  "started_at": 1794114360.0267656
}
```
