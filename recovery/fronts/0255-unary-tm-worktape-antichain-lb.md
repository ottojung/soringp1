# unary-tm-worktape-antichain-lb

## status

investigated

## origin

ai_proposal_unverified

## agent_id

UKyYiDeXVM4kRWqeA7erp5-strain

## exit_state

clearexit

## question

Is there an all-n lower bound showing that no deterministic multitape Turing machine computing S(n) from unary input 1^n can use o(n log n) worktape cells, given S(n)=Theta(n log n)? Or more tightly, does the decision-tree transcript information force worktape Omega(n log n / polylog n) independent of time?

## basis

docs/problem.md states unary threshold in PSPACE with budgeted DFS giving O(N log^2 n) space; space-reduction-budgeted-dfs investigated but no tight lower bound exists; distinguishes uniform TM cost from numeric-time recurrences.

## falsifier

Construct a uniform algorithm computing S(n) on unary input in o(n log n) worktape cells (and reasonable time), or derive a general simulation showing the transcript model is not necessary.

## implication

A nontrivial all-n space lower bound below the existing O(n log^2 n) would narrow the space-time tradeoff for unary SORT-BOUND-U without requiring super-polynomial time lower bounds (and remains consistent with PSPACE membership).

## finding_unverified

hard part. No known formula gives exact all-n values.
- **Using the information bound alone.** S(n) >= ceil(log2(n!)) is necessary but not sufficient; you need to determine the exact excess. The excess is a combinatorial property of the partial order game, not computable from factorial alone.
- **Savitch-style reachability to save space on traversal.** Reachability space can be reduced but the transcript (the graph itself) must be stored for backtrack; total space would still need to account for the stored history. Also simulation cost is high but space of the stored structure remains.

**Information-theoretic / lower bound considerations:**
- **Comparison count vs TM space.** The Ω(n log n) comparison lower bound is in the decision tree model (information-theoretic). Translating to multitape TM worktape space is not automatic - TM can do other things, but here the task is to *compute* that comparison-complexity function. A direct "output size" lower bound fails (output is log n bits). A "state graph" / configuration counting argument: if worktape < c n log n, number of configurations is 2^(o(n log n)); but the algorithm must produce different outputs S(n) for different n and must be correct for the adaptive game - not obviously forcing a contradiction. The winning frontier gives many states but that’s a barrier to enumeration, not a clean TM space lower bound.
- **Transcript information content.** Each of the d=Θ(n log n) steps produces Θ(log n) bits of identifying information (pair) plus 1 bit of outcome - total Θ(n log^2 n) bits of history information. To decide adaptively you need this information available. This is suggestive of Ω(n log^2 n / polylog n) in some models, but as a rigorous all-n TM lower bound I know of no published result that achieves this for S(n); the repo also states "no tight lower bound exists" (problem.md).

### Concrete obstruction to a clean disproof
- **No obvious simulation.** I cannot construct an algorithm avoiding transcript storage that remains correct for all adversarial adaptive choices; any correct adaptive strategy must track history.
- **Lower bound is hard.** Deriving an unconditional all-n TM space lower bound below the known upper bound would require a nontrivial argument (and is consistent with PSPACE membership; super-polynomial lower bounds are not in scope per AGENTS.md). The transcript-information argument is natural but not obviously formalizable to beat the known O(n log^2 n) without more structure.

### Recommendation (honest)
- **Most plausible path to disproof:** find a non-transcript (e.g., recursive/decompositional or algebraic) method to compute S(n) exactly that stores only O(n log n / polylog n) worktape cells. I have no concrete candidate.
- **Most plausible obstruction:** the adaptive history + pair indexing forces Ω(n log^2 n) in this model. A rigorous proof would need to formalize "transcript information" for a multitape TM computing this function.
- **Pragmatic next step:** try to see if the reachability workspace can be eliminated or if the pair encoding can be implicit; also check if the depth d can be encoded differently. But based on current evidence, a clean disproof is not obvious and a tight lower bound is also not established. This matches the repo's assessment of "no tight lower bound exists".

**Status:** no theorem or counterexample found; obstruction is the apparent necessity of storing adaptive history (transcript) with element indices. No repo changes proposed.

## Other metadata

```json
{
  "finished_at": 1793733432.1971087,
  "started_at": 1793731829.229526
}
```
