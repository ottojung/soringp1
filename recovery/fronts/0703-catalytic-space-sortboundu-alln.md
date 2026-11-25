# catalytic-space-sortboundu-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

3eZolGhv395Tn3wMRddi1K-tibia

## exit_state

clearexit

## question

Can SORT-BOUND-U be decided in o(N log N) bits by a uniform algorithm using catalytic or symbolic workspace that need not store a full comparison transcript, or does every exact method require Omega(N log N) bits?

## basis

Board space-linear-bits-decision-alln obstruction and catalytic-reversible-exact-evaluation-space gap.

## falsifier

Either a fully specified o(N log N)-bit algorithm with correctness and cost argument, or an all-n family of inputs forcing any candidate workspace to retain Omega(N log N) bits.

## implication

A positive answer would beat the current O(N log N)-bit transcript-DFS bound; a negative answer would make that bound tight for unary exact evaluation.

## finding_unverified

Posted one #301 comment for `catalytic-space-sortboundu-alln` (no repository, Lean, test, CI, or ledger changes; worktree remains clean).

Finding: honest inconclusive with a precise obstruction. The transcript-DFS family is provably stuck at Θ(N log N) bits, so any o(N log N) algorithm must leave that family. Candidate non-path representations do not beat Θ(N log N): storing a reachable poset needs Ω(d log(n²/d)) bits by counting DAGs with d cover edges; symmetry quotient is sound for the minimax value but remains 2^{Θ(n²)} states and is a time compression, not workspace; catalytic/reversible does not yield a smaller counted bits bound; framed-DAG soundness is not completeness. No universal Ω(N log N) workspace lower bound was obtained: general-poset hardness does not transfer to the fixed pairwise family, the sparse-tally barrier blocks many-one NP-hardness, and the winning-frontier count is an enumeration barrier rather than a space lower bound. The open obstacle is the absence of any state/path representation below Θ(N log N) bits that still supports comparability and candidate enumeration over Θ(N) depth, plus the absence of a lower-bound method targeting auxiliary workspace of this structured game.

## Other metadata

```json
{
  "finished_at": 1795410451.9690208,
  "started_at": 1795409775.9815357
}
```
