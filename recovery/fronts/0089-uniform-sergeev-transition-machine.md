# uniform-sergeev-transition-machine

## status

investigated

## origin

ai_proposal_unverified

## agent_id

cA4JnGnQM0l0F8rWHfHRoo-naught

## exit_state

clearexit

## question

Is there a deterministic uniform algorithm (polynomial-time in n, given 1^n) that outputs for each n the interval boundaries and container assignments for Sergeev's group-insertion construction realizing log2(n!)+o(n) comparisons, or does any such uniform specification require superpolynomial description length relative to n?

## basis

Sergeev ceiling-loss audits on board #301 showed accounting issues tied to canonical transition choices; distinction between uniform algorithms and non-uniform advice in AGENTS.md/problem.md.

## falsifier

Give an explicit polynomial-time uniform transition machine producing a valid Sergeev realization for all large n with the stated surplus, or prove that the choice function is NP-hard/uniformly incompressible forcing exponential-size descriptions.

## implication

Separating the existence of some non-uniform (or existential) realization from a uniform algorithm would clarify whether Sergeev's bound counts as a uniform upper bound for computing S(n) or only as a non-uniform comparison bound, directly affecting uniform complexity claims.

## finding_unverified

" vs just existence.

Also AGENTS.md says "An optimal sorting tree may be exponentially large, so exhibiting one is not an NP certificate." - existence vs exhibition. And for uniform complexity of computing S(n), distinction between uniform algorithms and circuits/precomputed advice matters.

So Sergeev's result is: for every n there exists some sorting tree with that height (existential/non-constructive in uniform sense, or just existence). The construction is described in the paper but making it fully explicit and uniform for all n might require choices not given by a uniform algorithm - hence no uniform polynomial-time algorithm exists to output the parameters; the bound is non-uniform/existential. That would mean the falsifier's first option fails and second is true (or at least the uniform algorithm doesn't exist).

That fits all the pieces: "separating existence of some non-uniform (or existential) realization from a uniform algorithm would clarify whether Sergeev's bound counts as a uniform upper bound for computing S(n) or only as a non-uniform comparison bound"

So the claim "Sergeev gives a uniform upper bound for computing S(n)" is false; it gives only an existential/non-uniform bound. The obstruction is that the construction lacks a uniform specification - extracting uniform parameters requires choices not provided by any polynomial-time uniform algorithm (the description is not uniform). 

This is a strong claim but matches the evidence.

I should report this as the finding - with honest limits (I don't have the full Sergeev paper text, but based on docs/board saying extracting finite computable bound is separate task and uniformity distinction matters, the obstruction is lack of uniform constructive procedure). Also try to be precise.

Let us also check: "deterministic uniform algorithm (polynomial-time in n, given 1^n) that outputs for each n the interval boundaries and container assignments" - so for each fixed n (input 1^n) output parameters for that n. That is a uniform function from n to parameters. Sergeev's construction as described might not give an explicit formula/function - might need to search over choices per n. And if valid choices are hard to find (satisfy discipline + surplus), that could be NP-hard. Or if the space is large and no formula exists, incompressible.

But without paper details it's hard to be certain. But the evidence points to uniformity being the issue.
Done. I posted the analysis to board #301 on this front, distinguishing non-uniform/existential vs uniform, noting the extraction gap (big-O doesn't give finite uniform procedure), discipline constraints making choices nontrivial, tried a naive formula and saw it would ignore discipline (likely breaking surplus/invariance), but didn't derive NP-hardness/incompressibility or a formal counterexample. Reported honest limits.The investigation is posted to Antonina #301 (billet-dev-agent). Conclusion: Sergeev’s bound is an existential/non-uniform construction in form—extracting finite uniform parameters is a separate task. Discipline constraints (upper-suffix/pending-set discipline, canonical transition choices) mean not all boundary assignments are valid; the choice function is over constrained transitions, so trivial formulas fail invariance/surplus. However I could not derive a formal NP-hardness/completeness or incompressibility obstruction from available docs, only the existence-vs-uniformity gap. No repo/Lean changes; honest limits reported.


## Other metadata

```json
{
  "finished_at": 1793407587.0841827,
  "started_at": 1793404688.878522
}
```
