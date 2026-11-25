# optimality-verification-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

38dovV6RiaQ3rCW8ATM2Na-reassure

## exit_state

clearexit

## question

For a given adaptive comparison tree T over n labeled keys, is there an all-n polynomial-time procedure to verify that height(T) equals S(n), and can any such verifier be reduced to solving SORT-BOUND-U without knowing S(n) a priori?

## basis

AGENTS.md model notes distinguish exhibiting an optimal tree from an NP certificate; certificate soundness/completeness gap on board #301 and literature on decision-tree optimality.

## falsifier

Exhibit a uniform polynomial-time verifier V that, for all n and all correct sorting trees T, accepts iff T is height-minimal, or prove unconditionally that minimal-height testing is PSPACE-hard for uniform verifiers over all n.

## implication

If optimality verification is harder than the threshold problem, succinct certificates for S(n) cannot rely on presenting a claimed minimal tree alone and must use a different checkable invariant, reshaping the NP-membership route without implying a class separation.

## finding_unverified

ion:** The claim “can any such verifier be reduced to solving SORT-BOUND-U without knowing S(n) a priori?” is moot if no such polynomial-time verifier exists. The trivial height-based reduction (two threshold queries using h(T)) only works if V exists and we know h(T); conversely existence of such V would not obviously follow from SORT-BOUND-U alone because of size + correctness checking. But the key point is the size obstruction blocks the tree-alone route entirely.
- **Distinction from general posets:** This size obstruction is specific to the antichain/complete sorting case producing exponentially large optimal trees; it’s not a general property of all posets. Also note AGENTS.md says hardness doesn’t transfer from arbitrary posets without reduction - here the obstruction is combinatorial size, not (necessarily) PSPACE-hardness of a reduction.
- **Certificate soundness/completeness:** Completeness fails (polynomial certificate impossible due to size). Soundness is also not obviously achievable polynomially if correctness/coverage can’t be verified efficiently. This matches the board #301 certificate soundness/completeness gap exactly.

**Failed approaches / exact obstruction:**
- Trying to represent T succinctly (as a program/decision tree generator) changes the object: verifying a program generates a correct minimal-height sorting tree for all permutations is much harder than verifying a given tree. Correctness becomes a program verification property (for all inputs/permutations) - likely undecidable in general for arbitrary programs, or at least not obviously reducible to SORT-BOUND-U. Also “all-n” uniformity is problematic.
- Attempting to reduce to SORT-BOUND-U: threshold is existence of some tree of height<=k; minimality of a given T is different (universal over all trees). The two are related but not obviously polynomially equivalent without the tree. And you can’t have the tree as polynomial input.

**Honest limits:**
- I did not find a primary literature reference in the repo that states “minimal-height testing is PSPACE-hard” for the antichain sorting case; the falsifier’s PSPACE-hardness claim may or may not be true, but it’s not necessary to disprove the falsifier - the size obstruction already disproves “there is a uniform polynomial-time procedure for all correct sorting trees T”.
- No reduction giving PSPACE-hardness was constructed. The general-poset PSPACE-hardness literature exists in some forms, but AGENTS.md explicitly warns against transfer without reduction; a serious attempt to transfer would need to show the antichain case is hard via reduction, which is non-obvious and I didn’t find a clear path in the docs/literature pointers here.
- This is a combinatorial/complexity-model obstruction (input size), not a proof that SORT-BOUND-U is easier/harder than optimality testing in some other sense - just that the tree-alone verifier is impossible polynomially.

**Conclusion:** The front’s falsifier is false unconditionally because optimal sorting trees can be exponentially large, so there is no uniform polynomial-time verifier (in input length) for minimal height over all correct sorting trees T. This directly explains why exhibiting an optimal tree alone is not an NP certificate (size + verifiability), matches the certificate soundness/completeness gap on board #301, and reshapes the NP-membership route to require different checkable invariants rather than presenting a claimed minimal tree. No Lean/repo changes made.

## Other metadata

```json
{
  "finished_at": 1793404963.4171221,
  "started_at": 1793404687.6969569
}
```
