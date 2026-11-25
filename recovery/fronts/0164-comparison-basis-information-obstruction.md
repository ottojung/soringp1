# comparison-basis-information-obstruction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

dYR9lh2DmbNgJZKPRpDMeN-camel

## exit_state

clearexit

## question

For all sufficiently large n where n! is not a power of two, is there an all-n combinatorial obstruction (beyond simple integer rounding of log2(n!)) forcing S(n) >= ceil(log2(n!)) + 1 due to the comparison (pairwise test) basis constraints on the state graph, independent of specific poset structure counts?

## basis

S(12)=30 > ceil(log2(12!))=29 shows information bound not tight; decision trees have both Kraft constraint and comparison constraints; distinction between general tests and pairwise comparisons not fully characterized for all-n.

## falsifier

Exhibit an infinite family or a general construction showing a comparison-based decision tree can achieve height exactly ceil(log2(n!)) for all n in that class despite n! not power-of-two, or prove the comparison basis imposes no additional all-n lower bound beyond the Kraft/information bound.

## implication

A positive all-n obstruction would give a structural lower bound beyond counting linear extensions and could help explain excess; a negative result would clarify the boundary between information theory and the restricted test set.

## finding_unverified

basis forces excess>=1 for all large n in that class - so no more cases like 20,21 where tightness returns? Or is there some general obstruction?

Also look up the docs again: "S(n) = ⌈log₂ n!⌉ for n ≤ 11 and n = 20, 21" - so tightness appears again at 20,21. That suggests there is NO all-n obstruction forcing excess>=1 for all large n; tightness can return. That would mean the falsifier is easy to satisfy in the sense that the claim is false? Or we need to be more precise.

Also another angle: the Kraft inequality gives a condition, but also for comparison trees there are stronger conditions (e.g. the "graph of splits" has structure). But are there theorems like "for sorting, if n! not power of two then S(n) >= ceil(log2 n!) + 1 for all n > 11"? Let us check values again carefully.
n=12: 30>=30 yes. n=13: 34>=34 yes. n=14 probably >=37 yes. n=15>=41, n=16>=45. n=20,21: tight so equal (excess 0) even though n! not power of two? Check n=20: 20! is large, log2(20!) is about 42.3366*? Compute roughly: log10(20!)~18.386, so log2 = log10(20!)/log10(2)~18.386/0.30103~61.08, ceil is 62. Is 20! power of two? No, has odd factors. And docs say S(20)=ceil(log2 20!) so tight. Yes, excess 0 despite n! not power of two. That directly contradicts "for all sufficiently large n where n! is not a power of two, there is an all-n obstruction forcing S(n) >= ceil(log2(n!)) + 1". The falsifier holds - we have counterexamples at 20,21.
But the question says "attack a precise all-n falsifiable mathematical claim..." so maybe the task is to show this claim is false by pointing to 20,21? But we need to be thorough and cite literature properly.

Also the user says "try seriously to DISPROVE it" - so probably disprove it. Let us be precise.

Let us investigate systematically.

I'll study the literature and known values to give a precise mathematical answer.

Let us write up the analysis.

The claim is refuted by known exact values - S(20)=⌈log2 20!⌉ and S(21)=⌈log2 21!⌉ despite 20!, 21! not being powers of two. The comparison basis imposes structural constraints causing sporadic non-tightness (n=12,13,14,...), but there is no all-n obstruction forcing +1 for every sufficiently large n in that class; tightness returns irregularly. This matches the literature in the repo.
**Finding (disproof):** The all-n claim is false. Known exact values give S(20)=⌈log2 20!⌉ and S(21)=⌈log2 21!⌉ with 20!,21! not powers of two (docs/research-certificates-barriers.md:125), so no universal obstruction forces +1 for all large n in that class—tightness recurs irregularly.

**Mechanism:** Comparison basis restricts allowed splits (not every partition realizable), producing sporadic non-tightness (e.g. n=12 via split-structure/Peczarski–Wells) where *all* trees fall short; but structure/symmetry allows achieving the information bound for other n despite non-power-of-two n!. Also monotonicity in e(P) fails and same e can have different m(P), so no scalar "rounding+comparison" all-n invariant applies.

**Distinction:** Information bound is necessary (sound). Tightness = some comparison tree hits Kraft bound for that n (completeness to bound holds there). The obstruction is state-graph/split-structure dependent, not a general theorem over all sufficiently large n with n!∤2^p.

**Evidence:** repo literature + computed ceil(log2 n!); no new Lean/repo changes (no substantive independently checkable new theorem/counterexample beyond citing established values). Analysis written to ANALYSIS.md.


## Other metadata

```json
{
  "finished_at": 1793563210.359139,
  "started_at": 1793561675.2097697
}
```
