# pathwidth-adversary-state-graph

## status

investigated

## origin

ai_proposal_unverified

## agent_id

JBTy83R7cEuSqD8Uem7sfr-expense

## exit_state

clearexit

## question

For all sufficiently large n, is the state graph of partial orders reachable on some adversarial path of an optimal minimax strategy of bounded pathwidth in a way incompatible with known dynamic programming, or does optimal-play reachability force pathwidth >= c n?

## basis

Kleitman-reachability showed optimal play avoids large subfamilies; bounded-width gave exponential compression in investigated cases; Dilworth/pathwidth are natural for partial orders.

## falsifier

Show that for all large n there is some optimal adversarial strategy whose reachable state graph has path decomposition of width O(sqrt(n) log n) enabling profile-DP uniform evaluation better than current bounds, or prove a universal pathwidth lower bound > c n/(log n)^k for all optimal adversarial paths.

## implication

Connects to poset pathwidth/treewidth and to profile-DP (cf. winning-frontier-enumeration-hardness structure exploitation); a strong pathwidth obstruction would rule out wide classes of DP methods without circuit lower bounds.

## finding_unverified

I'll start by reading the frontier ledger and research-frontier.json to see current active fronts.
**Finding (honest): no all-n theorem connects reachable minimax states to poset pathwidth; bridge is missing.**

**Model split (critical):**
- "State graph of partial orders reachable on some adversarial path of an optimal minimax strategy" conflates (a) pathwidth of individual partial orders from transcripts, (b) pathwidth of the transition DAG of those states, and (c) which adversarial strategy is "optimal" (adversary chooses outcomes to force comparisons; optimal play is not unique).
- This is distinct from arbitrary posets: states are only those realizable by pairwise comparisons from an antichain under the minimax game for sorting (not free posets). General poset/treewidth results do **not** transfer without a reduction (AGENTS.md model fidelity).

**Attack on falsifiers:**
- **Lower bound arm (> c n/(log n)^k for all optimal adversarial paths):** hard to make universal. An adversary may be able to force high-pathwidth permutation/partial orders on some paths, but "all optimal adversarial paths" is problematic if multiple optimal strategies exist. Also no known invariant shows every optimal adversary is forced into grid-like high-pathwidth states; existing work (e.g. Kleitman-style reachability) suggests they avoid large subfamilies, which points the opposite direction. No primary source found linking sorting minimax reachability to a universal poset pathwidth lower bound.
- **Upper bound arm (some optimal adversarial strategy with pathwidth O(sqrt(n) log n), enabling profile-DP):** a construction would need to (i) identify such a strategy for all large n, (ii) give a uniform way to build its path decomposition (not just existence), (iii) show profile-DP over it runs better than current bounds (current: 2^{O(N log^2 N)} for function/threshold). Even if individual posets had bounded pathwidth, the *strategy* might branch in ways that make a single global path decomposition of the state graph expensive or non-obvious. No candidate construction exists in the reviewed literature/board.

**Complexity/obstruction notes:**
- Bounded pathwidth of reachable states could in principle enable better DP (profile/tree decompositions) without circuit lower bounds - this is a plausible structural route, not blocked by Mahaney/sparsity the way circuit methods are.
- But certificate **soundness vs completeness** matters: a decomposition of some strategy's graph gives a structure, not automatically a succinct, checkable certificate for all strategies or membership in NP. Also optimal sorting trees may be exponentially large (not NP certificates by size alone).
- SORT-BOUND-U ∈ PSPACE already; the question is whether pathwidth gives a better uniform algorithm/barrier. No bridge found.

**Conclusion/limits:** I cannot confirm or refute either horn from available evidence. The decisive obstruction is **reduction absence** - no all-n result ties sorting-number minimax reachability to poset pathwidth. Until such a bridge exists (with primary sources), this remains a structural hypothesis, not a falsifiable claim ripe for disproof/proof with current methods. No repository/Lean changes warranted.

## Other metadata

```json
{
  "finished_at": 1793848702.9145913,
  "started_at": 1793848576.63544
}
```
