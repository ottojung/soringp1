# exact-cert-size-exponential-if-tight

## status

investigated

## origin

ai_proposal_unverified

## agent_id

shKRvYNENUUt9y5VKZVAGu-spirited

## exit_state

clearexit

## question

For all sufficiently large n with S(n)=ceil(log2(n!)), must every sound framed comparison DAG achieving height exactly S(n) contain Omega(2^(c n log n)) distinct nodes or equivalently be exponential in input size?

## basis

Framed-certificate soundness/completeness split; tight cases rare but open (information-tightness), and state compression barriers suggest quotienting hardens under exact height constraints.

## falsifier

Construct for infinitely many tight-n an all-n uniform family of polynomial-size framed DAGs of exact height S(n) with a soundness proof and explicit join annotations.

## implication

An all-n exponential lower bound on exact-height certificates would rule out SORT-BOUND-U in NP via framed witnesses without requiring a general super-polynomial lower bound on all evaluators.

## finding_unverified

falsifier is nontrivial:**
- The falsifier asks for an *all-n uniform family* of polynomial-size framed DAGs for *infinitely many tight-n* with soundness proof and explicit join annotations. 
- Merge sort gave polynomial-size DAG but exceeded info bound for large powers of two (not tight). Ford-Johnson/insertion constructions are polynomial-size in nodes but also not achieving info bound for all tight cases; achieving exact `S(n)=ceil(log2(n!))` is much harder. 
- You might try to find special tight n where the poset states collapse (high symmetry) allowing merges with `lambda_b=0`. Or find a different certificate structure. But "infinitely many tight-n" is a strong uniform claim - and it's unknown if there are infinitely many tight n at all (pattern is irregular). Also "uniform family" means a single construction parameterized by n.
- The obstruction is not just "many states exist" but the *join constraint* of the framed model: merging is only allowed via intersection of guaranteed relations (soundness-preserving) which creates forgetting unless paths are constraint-compatible. This is stronger than just counting reachable posets.

### Concrete failed approaches / exact obstructions
- **Decision-tree sharing fails.** Hash-consing identical posets doesn't help for a single policy (tree). For all-optimal policies you get some sharing but still exponential-like growth in small n and no proof of polynomial bound; tight height constraints likely kill this sharing.
- **General poset compression fails under exact height.** Quotienting by symmetry helps for value computation but doesn't obviously help with the framed certificate's join constraints at exact optimal height.
- **Merge/insertion templates fail on exact bound.** As noted, they achieve polynomial size but exceed info bound; repairing to exact `S(n)` would require either more comparisons (violates exact height) or different structure that may lose polynomial size/shareability.

### Honest limits
- **No proof either way.** The "must be exponential" claim is a plausible obstruction (from entropy + tree distinctness + join constraints), not a theorem in the repo. The falsifier is a plausible construction attempt but would need to overcome very tight constraints.
- **Tight n are rare/sparse in pattern.** Even if infinitely many exist (open question), constructing a uniform polynomial family is nontrivial.
- **Distinction matters:** This is about *framed certificates* (this specific DAG+join model), not about all evaluators. The complexity implication in the FRONT is correct in form - exponential lower bound on this certificate class would rule out NP via framed witnesses without general super-polynomial lower bound. 
- **No repo changes suggested.** This is a mathematical analysis; no Lean/theorem proved, no code changes needed. The question is open.

**Bottom line:** The strongest obstruction is that exact information-theoretic height with framed joins requires `lambda_b=0` (no forgetting) which is incompatible with merging different comparison histories into shared nodes except in highly constrained cases; combined with tree distinctness of poset states this forces exponential size. A uniform polynomial construction for infinitely many tight n would require defeating this join constraint - a concrete obstruction, but not proven impossible. Without a new merging mechanism preserving soundness and exact height, exponential size appears necessary for this certificate model on tight cases.

## Other metadata

```json
{
  "finished_at": 1793679112.8974426,
  "started_at": 1793675708.1228762
}
```
