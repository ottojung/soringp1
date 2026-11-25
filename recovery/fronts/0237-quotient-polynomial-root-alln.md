# quotient-polynomial-root-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

YOHHexjWQWBq2wfNCJ1LB1-cardiac

## exit_state

clearexit

## question

Does there exist an all-n equivalence relation on antichain-root comparison histories that is checkably congruent under both outcomes, closed under the minimax recurrence, has polynomially many classes in n, and is coarser than full poset isomorphism?

## basis

Root-reachable-certified-quotient investigated but lacked a specified invariant; state explosion is the main obstacle to efficient exact evaluation (docs/problem.md, board #301).

## falsifier

Prove no such nontrivial quotient exists for all large n (an all-n state-merging obstruction), or construct one with explicit class representatives and a polynomial-time membership test usable in the recurrence.

## implication

A polynomial exact quotient would yield a polynomial-state recurrence for S(n) and a natural polynomial-size certificate class; a general obstruction would explain the exponential state graph and constrain NP-certificate routes for SORT-BOUND-U.

## finding_unverified

No final text; audit needed

## Other metadata

```json
{
  "finished_at": 1793711721.0213065,
  "started_at": 1793711059.7805827
}
```
