# transit-closure-update-amortized-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

QwdGnou2ijUniTLGXKHAMK-sinewy

## exit_state

clearexit

## question

For uniform exact minimax evaluators maintaining transitive closure of partial orders under pairwise comparisons, is there an all-n family of reachable states where any pointer/bitmask scheme must perform Omega(n^2 / something) amortized updates per comparison making 2^(O(n log^2 n)) total impossible to beat below a higher exponent?

## basis

Many exact evaluators maintain reachability/TC; general dynamic TC is hard, but this is a very restricted incremental/dynamic class (only comparisons, DAGs of dimension<=2 in some cases, special structure).

## falsifier

Give a uniform dynamic transitive-closure data structure specialized to this comparison-game poset class achieving total update cost o(n^2) per level on that all-n family and preserving exact F(P) values.

## implication

A proven amortized TC-update barrier would separate the data-structure cost of the minimax recurrence from its graph-theoretic form, constraining uniform evaluators without invoking circuit lower bounds.

## finding_unverified

 comparisons, is there an all-n family of reachable states where any pointer/bitmask scheme must perform Omega(n^2 / something) amortized updates per comparison making 2^(O(n log^2 n)) total impossible to beat below a higher exponent?  
> FALSIFIER: Give a uniform dynamic transitive-closure data structure specialized to this comparison-game poset class achieving total update cost o(n^2) per level on that all-n family and preserving exact F(P) values.  
> COMPLEXITY IMPLICATION: A proven amortized TC-update barrier would separate the data-structure cost of the minimax recurrence from its graph-theoretic form, constraining uniform evaluators without invoking circuit lower bounds.  
> EVIDENCE: Many exact evaluators maintain reachability/TC; general dynamic TC is hard, but this is a very restricted incremental/dynamic class (only comparisons, DAGs of dimension<=2 in some cases, special structure)."

So this is asking to attack this specific front. The previous findings showed that for transitive-closure-subquadratic-alln-barrier, someone claimed Italiano gives O(n) per insertion and refuted the barrier. But for THIS front (transitive-closure-update-cost-barrier), the finding says "the information-theoretic lower bound requires Omega(n^2/w)=Omega(n^2/log n) bit operations per update in the RAM model for dense adversarial partial orders - the bitmask method achieves this. However, this is not an unconditional proof of the stronger Omega(n^2/polylog n) claim..." So the finding is saying it's open - they couldn't prove or disprove it strongly. The front is still "investigated" status. The instruction says "On billy-dev ONLY, study AGENTS.md, docs/problem.md and current board #301. Study the primary literature, attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n), and try seriously to DISPROVE it." So I need to attack THIS claim (the transitive-closure-update-cost-barrier front) and try to DISPROVE it - i.e. find the falsifier (give such a data structure).

Let us report the findings.

**Mathematical finding (disproof attempt):** In the standard RAM model with word size w = Θ(log n), the simple bitmask method (budgeted_dfs extend) achieves O(n^2/w) = O(n^2/log n) per update = o(n^2); Italiano’s incremental TC gives better amortized bounds. With undo/persistent backtracking this is asymptotically unchanged. The comparison-game class (DAGs, incremental, only edge insertions) is easier than general dynamic TC, not harder. No unconditional lower bound forces Omega(n^2/polylog n) in this model; the falsifier (uniform method with o(n^2) update cost per level) is satisfied by existing representations.

**Failed/obstructed approaches / limits:** Distinction between pointer/bitmask schemes is model-sensitive (log n factor disappears without bitwise packing). The stated complexity implication (barrier affecting the 2^(O(n log^2 n)) exponent) is weak because tree branching/depth, not polynomial per-node TC costs, dominate that exponent. If the claim assumes a restricted machine model (e.g. pointer machine counting pointer operations) where bitwise packing gives no advantage, the question becomes model-dependent and I cannot derive an all-n obstruction from first principles without committing to that model. No theorem or counterexample was proved here; repo changes are unwarranted. The front remains open in a model-restricted sense, but in the model implicit in the repo’s complexity accounting the lower bound is false.

## Other metadata

```json
{
  "finished_at": 1793804496.8982189,
  "started_at": 1793801913.3039024
}
```
