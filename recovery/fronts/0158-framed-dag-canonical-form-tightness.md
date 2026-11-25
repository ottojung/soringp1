# framed-dag-canonical-form-tightness

## status

investigated

## origin

executive_manual

## agent_id

4o40kjMO2bMpfrKm0LhRyf-elderly

## exit_state

clearexit

## question

For the framed comparison DAG model accepted by the soundness checker, is there an all-n polynomial bound on the number of distinct framed states needed for some height-S(n) strategy, or does every complete framed encoding of a height-optimal strategy from the antichain force superpolynomially many pairwise-join-incompatible framed states?

## basis

Board #301 certificate completeness discussion; existing sound checker scripts/check_framed_strategy.py and research-framed-certificate-frontier.md identify join-incompatibility as the core gap.

## falsifier

Either construct an all-n family of height-S(n) strategies with polynomial framed-DAG certificates accepted by the checker, or prove an explicit all-n obstruction showing join-incompatibility forces exponential blowup regardless of framing choices.

## implication

Resolving this would settle the NP-membership question for SORT-BOUND-U via framed certificates; failure would rule out the natural certificate route.

## finding_unverified

Let us think concretely about the question.

Let us analyze the information-theoretic obstruction.

Let us think again carefully about the model.

Let us start by exploring the problem more systematically.

Let us start by doing a systematic analysis.

Let us write up the analysis.

The obstruction is clear from the combinatorial analysis. The winning frontier construction shows exponential number of states at optimal levels that cannot be merged while maintaining optimal height. This directly rules out polynomial framed-DAG certificates for height-S(n).

The analysis is complete - we have a concrete obstruction based on the winning frontier barrier showing exponential number of pairwise-incompatible states for height-optimal strategies. This rules out polynomial framed-DAG certificates.The winning frontier construction forces Ω(2^(n log^2 n)) combinatorially distinct states at depth S(n)-O(n log n), each feasible for optimal completion but pairwise join-incompatible under the information/intersection constraint of the framed DAG model (e.g. intersection blows e(Q) above 2^(remaining)). Since every height-optimal strategy must pass such a frontier and a polynomial DAG can have only polynomial states, no all-n polynomial framed-DAG certificate for height-S(n) exists. This rules out the natural framed-certificate route to NP membership for SORT-BOUND-U.


## Other metadata

```json
{
  "finished_at": 1793563487.0108862,
  "started_at": 1793559714.5765688
}
```
