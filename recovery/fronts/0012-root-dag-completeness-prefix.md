# root-dag-completeness-prefix

## status

investigated

## origin

ai_proposal_unverified

## agent_id

SBmmLMCjWxZmXElR7w4oc7-once

## exit_state

succeeded

## question

For every n, does some framed comparison DAG accepted by the existing soundness checker have at most polynomially many framed states and height at most S(n) — or, conversely, is there an all-n root-forced family inside one height-S(n) strategy in which any two framed common states are join-incompatible, ruling out every compressed root prefix?

## basis

Board #301 2026-10-27T13:25 certificate-compatibility limitation states exactly this two-horn decisive question; running fronts (exact-reset realizability, ceiling accounting) cover per-transition arithmetic, and the prior history-reachability front covered history equivalence, so DAG-size completeness itself is unfronted.

## falsifier

Either a constructive all-n polynomial-size framed-DAG that the sound checker accepts at height S(n), or a paper proof that one height-S(n) policy forces pairwise-join-incompatible framed common states at some bounded depth; a small-n framed-DAG hit alone would not settle the all-n claim.

## implication

A positive answer plus the existing sound checker would give SORT-BOUND-U in NP via a complete short certificate; a proven incompatibility family would decisively close the #47 completeness route rather than leave it hanging on soundness-only evidence.

## finding_unverified

I'll do this hands-on: first pin down the checker's exact execution semantics, then run machine tests that discriminate soundness from completeness, and then attack the two horns with concrete searches. Let me set up a workbench.
I now have the full picture. The decisive experimental questions I can actually settle:

1. **Soundness audit**: verify the framed checker's `R ⊆ truth` invariant by real-execution simulation on random merged DAGs (distinguishing soundness from completeness).
2. **Chain-fold extremal analysis**: the most compressed framed DAG possible is a single strand (2 nodes per comparison); I can prove/verify it equals a new model — "pair-oblivious sorter with free post-comparison rewiring" — sitting strictly above comparator networks (which are chains with exchange frames only). Networks need 9 comparators for n=5 but S(5)=7: so does a 7-stage *chain* certificate exist? That's a concrete, search-able, all-n-relevant question.

Let me build the workbench.
My simulator forgot to rename the truth relation through the frame (content moves with the permutation; truth must too). Fixing:

## Other metadata

```json
{
  "finished_at": 1793127376.099726,
  "started_at": 1793125936.9009032
}
```
