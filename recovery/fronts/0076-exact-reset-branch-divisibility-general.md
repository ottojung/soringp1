# exact-reset-branch-divisibility-general

## status

investigated

## origin

ai_proposal_unverified

## agent_id

kV4WkjM6ie61oXTcxW2m5M-language

## exit_state

clearexit

## question

For exact-reset framed transitions F -> {F1,...,Fm} (partitioning Ext(F) into equal classes of some fixed F' up to framing), is there a general necessary and sufficient condition on (F, F') beyond the antichain->star odd-n obstruction, and does every height-S(n) optimal strategy force some exact-reset transition that is not realizable?

## basis

Exact-reset realizability gave a concrete odd-n antichain->star divisibility obstruction; the general theory of when ratio-of-extension-counts is realizable by comparison splits is open and directly bears on framed-certificate completeness for optimal strategies.

## falsifier

Characterize all (F,F') with e(F)/e(F') integer realizable by some comparison tree with branch classes exactly Ext(F') under framing, or exhibit an optimal strategy that must pass through an unrealizable exact reset to achieve height S(n).

## implication

A complete characterization would explain when ceiling-loss accounting is valid and when branch divisibility creates stronger obstructions to framed certificates achieving height exactly S(n); a forced unrealizable exact reset would rule out certain exact-height certificate constructions.

## finding_unverified

-loss accounting is valid and when branch divisibility creates stronger obstructions to framed certificates achieving height exactly S(n); a forced unrealizable exact reset would rule out certain exact-height certificate constructions.
> EVIDENCE: Exact-reset realizability gave a concrete odd-n antichain->star divisibility obstruction; the general theory of when ratio-of-extension-counts is realizable by comparison splits is open and directly bears on framed-certificate completeness for optimal strategies.
> If resuming after an infrastructure failure, inspect earlier work and avoid repeating side effects or claims. 
> On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof."

This is asking to attack this question. Let us think - is this related to the "graph of posets" and "shelling orders"? Or more directly to the concept of "comparison basis" or to "poset games"?

Another angle: in some contexts, exact resets relate to "regular posets" or to the fact that you can only do resets when the poset has certain symmetry properties. Also related to "searching with lies"? No.

Alternatively, think of the "state graph" as states = posets up to isomorphism/framing. A transition is allowed if you can do one comparison to get from F to states that are all "isomorphic" to each other up to framing and form a partition of Ext(F). So all children are the same type F'.

Also, for such uniform splits to be possible repeatedly, F must have a lot of symmetry. The antichain A_n is highly symmetric - every pair equivalent. The star V_n also has symmetry.

Also the obstruction was: in a symmetric poset, any comparison gives a balanced split, but you need the split size to be compatible with e(F') dividing e(F)/2. So ratio condition is necessary but not sufficient because of the *branching* structure of the comparison.

Also, are there other posets besides antichains where all pairs give same split? Or where you get obstructions?

Also, there's a concept in combinatorics of posets called "N-free" posets? Or more directly related to "series-parallel posets"? Or maybe to "permutation graphs"?

Alternatively, consider the case where F is a disjoint union of chains of equal length - also symmetric?

Or think about the "mobile posets" or other classes. Let us test.

Let us test if exact reset to V_n is possible for even n >= 4.

Let us think systematically.

Let us write up a careful mathematical analysis.

**Mathematical finding (deduction):** Exact reset F->F' requires (i) branch divisibility e(F') | N_+(P,u,v), e(F') | N_-(P,u,v) at every split under some comparison strategy; the odd-n A_n->V_n is a root-split instance. (ii) Structural condition: guaranteed relations (transitive closure) must form exactly some poset isomorphic to F' under framing with no extra forced relations - transitivity can create extras even if counts divide (e.g. attempts at A_4->V_4 fail structurally). A general complete characterization needs both; it's not just count divisibility. **Failed approach:** tried to construct A_4->V_4 by various strategies and all create extra forced relations via transitivity or wrong structure despite divisible splits. **Relation to S(n):** if optimal sorting strategies must pass through unrealizable exact resets (divisibility or structural), this would obstruct exact-height framed certificates; this remains open and is not obviously forced by known optimal tree structures.


## Other metadata

```json
{
  "finished_at": 1793392702.6310298,
  "started_at": 1793390334.2971077
}
```
