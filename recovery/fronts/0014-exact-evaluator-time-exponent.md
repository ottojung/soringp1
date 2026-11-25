# exact-evaluator-time-exponent

## status

investigated

## origin

ai_proposal_unverified

## agent_id

XQbdqk22VYjiZwy2bHYrBQ-doubt

## exit_state

succeeded

## question

Can the exact numeric evaluator S_unary(1^n) be improved from the known 2^{O(n log^2 n)} time to 2^{O(n log n)} or 2^{O(n)} uniformly in n via a memoization or interface-summary tradeoff that provably recomputes or stores everything it needs, or is there an all-n state family forcing every such evaluator to keep an Omega(n^2)-bit seed table?

## basis

docs/research-budgeted-dfs.md section 5.3 threshold bound and the compress-exact-space-evaluator finding that naive canonical reconstruction already blew up to 2^{O(k^2 log n)}, plus docs/research-time-exponent.md showing orbit pruning alone is insufficient; no prior front targets time rather than space.

## falsifier

Either a fully specified algorithm with a correctness and cost paper argument reaching 2^{O(n log n)} or 2^{O(n)} on 1^n, or an explicit all-n family of reachable framed states such that any candidate interface summary agreed on by all of them still yields a different exact antichain-root value, breaking the proposed memoization.

## implication

Any improvement directly lowers the known uniform time envelope for computing the exact function S(n), and a forced-state family would rule out an entire memoization-prune family of evaluators without touching the transcript-DFS upper bound.

## finding_unverified

Now the test file:
Test bugs of mine (offset in brute-force check, and the peaked binomial makes consecutive n share values). Fixing:
All tests pass. Now the research note:
One real subtlety caught: if `S(n) = ⌈log₂ n!⌉` exactly (tight, e.g. n ≤ 6 empirically), threshold k = that value is a *yes*-instance with short-circuiting. Fix: use budget `k = ⌈log₂ n!⌉ − 1`, which is always a no-instance since `S(n) ≥ ℓ(n)` strict above `ℓ−1`. Updating code and note:
One final strengthening — the visit-count statement is unconditional even under key collisions. Adding it:
Final soundness pass done (orbits, budgets, Stirling constants all check). Sharpening one doc claim, then commit:
Now board posting per `docs/operations.md`:
Done. Mathematical finding and honest limits:

**Result (new, all-n, paper proof + experiments, commit `f9d444a`):**
For `m = ⌊n/2⌋`, every j-edge height-2 subset poset on `A ⊔ B` is reachable from the antichain in **exactly j** comparisons (A→B-only relations give no implications and exactly one new comparable pair per step) — fixing the gap in `research-time-exponent.md`, whose staircase posets need Θ(n²) comparisons and are never visited by a budget-critical search. With the guaranteed no-instance budget `k = ⌈log₂ n!⌉ − 1 ≤ S(n)−1`, an exhaustive threshold DFS (memoised or not) must visit ≥ `CI(m, min(k,⌊m²/2⌋))/(m!)²` pairwise non-isomorphic states (exact inclusion–exclusion, verified by big-integer counts `n ≤ 88` and an analytic union bound valid for all `n ≥ 5`), whose count is `2^{Θ(n log²n)} = 2^{ω(n log n)}` (L(1024) ≈ 47 663 bits vs n log₂ n = 10 240).

**Consequences:** every evaluator in the canonical-memoisation family (exhaustive game-tree threshold recursion, isomorphism-class memo keys) takes ≥ `2^{Θ(n log²n)}` time on this input — the family cannot reach `2^{O(n log n)}` or `2^{O(n)}`, and the §5.3 threshold bound `2^{O(N log N)}` is exponent-tight within it (`L/(N log N) → 1`).

**Not proved:** forced state identity here is Θ(n log²n) bits, *not* Ω(n²) bits — the front's Ω(n²)-bit forced-seed hypothesis is neither proven nor refuted. This constrains *completeness* of state identity only; a coarser sound interface summary (bisimulation-style congruence over critical-depth reachable states) evades the bound and remains the open route. No Lean changes; note + probe script + 8 tests (`docs/research-critical-depth-memo-barrier.md`), board #301 updated.

## Other metadata

```json
{
  "finished_at": 1793127559.7946813,
  "started_at": 1793125938.6720185
}
```
