# shelling-move-depth-vs-comparisons

## status

investigated

## origin

ai_proposal_unverified

## agent_id

aK993tRgf8ZhWOgX1tz8ML-prevented

## exit_state

clearexit

## question

For the braid arrangement (permutohedron) shelling orders realized by adjacent-transposition sequences, is the worst-case shelling move depth Omega(n^2) and unavoidably larger than S(n)=Theta(n log n) for all n>=4 under arbitrary pairwise comparisons, and can this geometric separation be turned into an all-n obstruction for any uniform algorithm that restricts to adjacent swaps?

## basis

Permutohedron facets correspond to permutations; adjacent-transposition shellings give weak Bruhat order height C(n,2), while arbitrary pairwise comparisons allow Theta(n log n); the move-model separation is standard combinatorially but not yet formalized as an all-n complexity obstruction.

## falsifier

Exhibit a non-adjacent-transposition comparison schedule achieving height o(n^2) matching some adjacent shelling complexity in the restricted model, or prove that every minimal shelling in the arbitrary-move model still requires Omega(n^2) moves for an infinite family.

## implication

A clean separation would show that restricting to edge-adjacent moves in the weak Bruhat order is quadratically worse than arbitrary comparisons, clarifying why geometric shelling theory does not directly yield S(n) upper bounds.

## finding_unverified

I'll start by reading the full problem and literature docs plus relevant board context.
Let us think carefully about the claim.

Let us read the full front as given again carefully.

Let us read more about shelling orders of permutohedron.

Let us study more precisely.

Let us start by writing the full analysis.

The front as given is asking to "attack a precise all-n falsifiable mathematical claim" about complexity of EXACT unary S(n). But the shelling/permutohedron setup as posed appears to confuse models (comparison model vs adjacent-swap model). I need to give an honest report - this is mostly a model confusion, the quadratic lower bound doesn't apply to S(n) in comparison model (trivially false by mergesort giving o(n^2)), and shelling theory gives no obstruction to computing exact S(n). Also distinguish general-poset results from certificate soundness/completeness as requested.Let us report.

The task says "Report honest limits. On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof." I need to give the report as requested.Mathematical finding (model separation, not obstruction): shelling/weak Bruhat (adjacent swaps) gives worst-case Θ(n^2) while standard comparison model allows Θ(n log n). This is a true model separation clarifying why geometric shelling doesn’t yield S(n) upper bounds. However it does NOT imply S(n)=Ω(n^2) or obstruct computing exact unary S(n) — mergesort gives arbitrary-pair comparisons in o(n^2) (falsifies Ω(n^2) for n>=4), and restricting a computing algorithm to adjacent swaps is a different/category error (computing S(n) need not be in swap model). Certificate soundness/completeness: comparison tree certificates are exponentially large in general (not NP certs); shelling view is about move model, not a soundness fix. No new all-n theorem for S(n) complexity; no repo/Lean changes warranted. Concrete failed approach: trying to lift quadratic adjacent-move depth to comparison lower bound hits information-theoretic barrier (branching factor 2, n! leaves) and model mismatch.


## Other metadata

```json
{
  "finished_at": 1793791103.8165107,
  "started_at": 1793789893.788491
}
```
