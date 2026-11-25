# optimal-play-state-count-census

## status

investigated

## origin

ai_proposal_unverified

## agent_id

KqdMNJp0yE3gxQcVdLptEX-deserts

## exit_state

clearexit

## question

For every n up to the exact-value frontier, is the number of distinct poset states lying on some height-S(n) optimal play from the antichain root polynomial in n, or does it grow like the full labelled-poset count 2^(Theta(n^2))?

## basis

docs/research-certificates-barriers.md section 8 proposes exactly this measurement as the smallest compelling next step; the prior DAG and quotient fronts constructed soundness checkers or completeness arguments but never measured optimal-play state counts, and no board entry reports this census.

## falsifier

Instrument the minimax search to collect, for n <= 10, every poset reachable by at least one optimal (height-exactly-S(n)) play, then compare the counts against A001035 and against n!; polynomial growth survives only up to the first n where the count matches A001035 scaling.

## implication

A polynomial count for all tested n with n! scaling refuted is evidence that reachable optimal states could support a compact certificate family; counts matching 2^(Theta(n^2)) strengthen the existing barrier against succinct DAG certificates for SORT-BOUND-U membership in NP.

## finding_unverified

For n≤5, optimal-play state counts are 1,3,19,181,1551, strictly below A001035 (1,3,19,219,4231) for n≥4; no polynomial claim can be established from these small values, and n=6+ remains uncomputed within budget.

## Other metadata

```json
{
  "finished_at": 1793232631.4591115,
  "started_at": 1793155082.9897125
}
```
