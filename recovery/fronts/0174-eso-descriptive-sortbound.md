# eso-descriptive-sortbound

## status

blocked

## origin

ai_proposal_unverified

## agent_id

MP9D4AkhUtGxWKfgF660q4-mitchell

## exit_state

failed

## question

For all n>=1 with unary encoding of (n,k), does there exist an existential second-order sentence over finite ordered structures that is true iff S(n)<=k and has size polynomial in (n+k), or is there an all-n inexpressibility obstruction forcing super-polynomial sentence size for any ESO definition of SORT-BOUND-U?

## basis

AGENTS.md states PSPACE via FO(PFP); research-plan.md lists FO(LFP)/ESO as open upper-bound routes; sparsity blocks many-one NP-hardness but not NP membership, distinct from framed-certificate fronts already investigated.

## falsifier

Construct an explicit ESO sentence defining SORT-BOUND-U with size polynomial in unary input length, or prove for some all-n family that every ESO sentence deciding S(n)<=k requires size >= 2^(Omega(poly(n+k))).

## implication

A polynomial ESO definition would yield SORT-BOUND-U in NP (a strict upper-bound improvement) while remaining uniform; a uniform inexpressibility barrier would constrain the descriptive-complexity route to NP membership without relying solely on framed DAGs.

## finding_unverified

tions?

Alternatively, look up how others interpret similar things. Another possibility is that in some texts, when talking about bounded arities or about the formula defining the class, but combined with "all-n" and "size polynomial in (n+k)" - maybe they mean a uniform family where each member has polynomial size? That is similar to how P/poly is described. Also "polynomial ESO definition" - sometimes people say ESO-definable with polynomial resources.

Alternatively, compare to the falsifier more: "Construct an explicit ESO sentence defining SORT-BOUND-U with size polynomial in unary input length" - so the sentence's size (length) is polynomial in the unary input length N=n+k+1. If it's a fixed sentence, its length is constant regardless of N. That can't be. That means they want a *non-fixed* sentence whose length grows polynomially with input size? That would be strange for descriptive complexity. Or they want a sentence that, when you write it down, has size polynomial in the input parameters - almost like a schema?

Alternatively, think differently: maybe encoding the comparison tree or the strategy as second-order relations, and the sentence says "there exists a strategy (tree/DAG) of height <= k" - this is exactly like the game formulation. In descriptive complexity of games, sometimes you get fixed-point logic. But ESO is different.

Also look up what AGENTS.md says: "The PSPACE bound implies an FO(PFP) definition of `SORT-BOUND-U` on ordered structures by the capture theorem" - Immerman’s theorem says FO(PFP) = PSPACE on ordered structures. So fixed FO(PFP) sentence would capture SORT-BOUND-U. That means if SORT-BOUND-U ⊆ PSPACE (and PSPACE-complete problems too, but membership), then yes fixed FO(PFP) sentence exists. Similarly ESO would be fixed sentence giving NP.

But if SORT-BOUND-U is in NP (not proven), then there is some fixed ESO sentence. The question says "does there exist an existential second-order sentence..." - standard form. "has size polynomial in (n+k)" - maybe they mean the witness relations have size polynomial in (n+k)? That is, the certificate is of polynomial size - which is necessary for NP. Or perhaps the question is a bit oddly phrased.

Alternatively look up the full context again: "FRONT: For all n>=1 with unary encoding of (n,k), does there exist an existential second-order sentence over finite ordered structures that is true iff S(n)<=k and has size polynomial in (n+k), or is there an all-n inexpressibility obstruction forcing super-polynomial sentence size for any ESO definition of SORT-BOUND-U?"

Another interpretation: the sentence is over structures of a fixed signature? Or you can choose the signature? "over finite ordered structures" - ordered structure usually means has a linear order. The size of the structure would be related to n+k. Maybe they mean the sentence has quantifier rank or some measure polynomial in (n+k). Or maybe the number of second-order variables?

Or perhaps this is about the *descriptive complexity* in terms of the formula size being polynomial in the input size (like in bounded arithmetic or in some other contexts). Or maybe it's related to the fact that if you have a polynomial-size ESO formula, that gives NP. Let us look up how this project thinks. Also look up "sentence size" in finite model theory - usually means length of the formula.
Let us start fresh investigation of this ESO question.

Let us start by understanding the problem precisely.

Let us analyze this.


## Other metadata

```json
{
  "finished_at": 1793582896.5175352,
  "started_at": 1793580429.106801
}
```
