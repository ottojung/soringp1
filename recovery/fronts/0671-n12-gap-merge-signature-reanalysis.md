# n12-gap-merge-signature-reanalysis

## status

blocked

## origin

executive_initiated

## agent_id

qurmJz3DFvgTG3EUnLajvF-discovery

## exit_state

failed

## question

Reproduce the Stober-Weiss n=12 non-tightness window [0.892, 0.942) with an independently written two-sided backward search and audit the bottleneck posets in it: is every reachable poset P on a height-29 optimal play a disjoint union of two chains (a Merge(a,b) substructure), or do there exist reachable bottleneck posets with non-merge structure? Exhibit a non-merge bottleneck poset, or prove that every reachable optimal-strategy bottleneck poset is merge-type.

## basis

Stober-Weiss ALENEX 2023 Table 2 (S(12) > 29; 6190 explored posets, efficiency bandwidth 0.05); docs/research-obstruction-next.md (local gap analysis and no-go section); frontier fronts sergeev-group-framed-dag and information-tightness-* (adjacent global-gap questions, do not confuse); research-n12-nontightness.md.

## falsifier

Exhibit a reachable optimal-strategy bottleneck poset P with height 29 and a comparability graph that is not a disjoint union of two chains, or prove that every reachable optimal-strategy height-29 bottleneck poset is a disjoint union of two chains.

## implication

If a non-merge bottleneck poset is reachable on an optimal play, the n=12 gap has a mechanism beyond the merge-cost theory; if only merge bottlenecks are reachable, the global non-tightness reduces to a merge-structure question and an analogous structure search at higher n is the natural next step.

## finding_unverified

Let me now look at the repo's own bidirectional method and fetch the primary source (Stober–Weiss ALENEX 2023).

## Other metadata

```json
{
  "finished_at": 1795311270.887719,
  "retry_after": 0,
  "started_at": 1795309985.1110883
}
```
