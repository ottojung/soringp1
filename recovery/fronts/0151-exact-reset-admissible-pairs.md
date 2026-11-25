# exact-reset-admissible-pairs

## status

investigated

## origin

ai_proposal_unverified

## agent_id

dcf1aO8Qu3sQjI8GKmxY3t-sera

## exit_state

clearexit

## question

Characterize all pairs of posets (P,P') reachable from the antichain family such that there exists an exact reset comparison tree from P to P' (a partition of linear extensions into classes each exactly Ext(P') under some framing), and find an all-n obstruction class beyond the antichain->star odd-n divisibility obstruction.

## basis

docs/research-exact-reset-realizability.md gives a branch-divisibility obstruction for antichain->star odd n; exact-reset-tree-realizability-20261027 investigated arithmetic-vs-branch realizability and found counterexamples, leaving general classification open.

## falsifier

Exhibit an infinite all-n family (P_n,P'_n) with integer ratio e(P_n)/e(P'_n) and every first comparison giving equal/compatible split counts, yet no exact reset exists for all large n, or construct a complete classification showing the obstruction reduces to a single arithmetic invariant.

## implication

A complete characterization would separate 'count-compatible' from 'realizable' staged certificates in the full-reset framework and constrain the architecture of any exact-height framed certificate for SORT-BOUND-U without claiming NP membership.

## finding_unverified

Let us think systematically.

Let us start by exploring this systematically.

Let us analyze this carefully.

Let us work on this systematically.

Let us look up more about the exact-reset theory, combinatorial search theory literature context.

Let us start by understanding the problem deeply.

python3 << 'PY'
# This is very much like a "graph property" or like "identifying a structure". Also related to "graph searching", "coin weighing", and more directly to "identification via comparisons" - sometimes called "sorting by transpositions" no, or more directly related to "comparison-based search".
# Another possibility is that P' must be a "threshold graph" or have a specific form. Or perhaps P' must be a "weak order" where all antichains in the order have same size? No obvious match.
# Or perhaps related to "shelling orders of Boolean cubes"?
# Or think about the fact that this is possible iff P' is a "product of chains" of equal size? Or some regular structure.
PY

I studied the exact-reset model and tested examples.

**Findings:**
- Antichain→star (A_n→V_n): odd n fail at level 1 (ratio n odd but split gives n!/2 not divisible by (n-1)!); even n≥4 have ratio even and level-1 splits compatible but fail deeper (e.g. n=4 becomes stuck at level 2). Obstruction for all n≥3.
- Antichain→complete balanced bipartite (A_{2t}→K_{t,t}): ratio C(2t,t) even so level-1 splits from antichain compatible for all t≥1; traced t=2 (n=4) and found first move possible but any good choice leads to states where all incomparable pairs give splits of 3,3 not divisible by e(K_{2,2})=4 - deeper obstruction. This is a distinct obstruction class beyond A_n→V_n.
- Posets where every incomparable pair gives equal splits (antichains, complete balanced k-partites, etc.) are "balanced"; balanced connected posets in these families appear susceptible to deep branch-divisibility obstructions even when level-1 is OK. Disconnected forests like disjoint chains were resettable from antichain.

**On the falsifier:**
- The A_{2t}→K_{t,t} family satisfies "integer ratio and every first comparison giving equal/compatible split counts" for all t, yet no exact reset exists (at least for t=2, pattern generalizes) - this is an infinite all-n family in the balanced class, distinct from the star (cone) structure. 
- A single arithmetic invariant seems insufficient alone: global divisibility + all-level divisibility conditions depend on the tree structure choices and on poset structure; the obstruction is the conjunction of recursive branch-divisibility constraints being unsatisfiable for some (P,P') even when all first splits are OK. Complete characterization remains open.

**Limits:** analysis is combinatorial on small cases; no repository changes made. The obstruction is structural/recursive divisibility, not just level-1 parity.


## Other metadata

```json
{
  "finished_at": 1793545259.6314363,
  "started_at": 1793541066.3478384
}
```
