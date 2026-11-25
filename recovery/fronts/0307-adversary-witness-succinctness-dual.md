# adversary-witness-succinctness-dual

## status

investigated

## origin

ai_proposal_unverified

## agent_id

fdlsI7tXDqnouF3lx3uNHy-spokesman

## exit_state

clearexit

## question

Are there infinite all-n families where every polynomial-size (in N) adversary witness for S(n)>k is not checkable by the same local meet-join test used by sorter certificates, making dual succinctness fail despite game duality?

## basis

alln-adversary-universal-certificate investigated (duality not implying dual succinctness); certificate soundness vs completeness repeatedly emphasized in AGENTS.md and problem.md.

## falsifier

Give a general polynomial-time translation from any valid adversary strategy certificate to a sorter certificate of size polynomial in the adversary certificate (or vice versa) for the antichain root, for all n.

## implication

If dual succinctness fails and neither form is uniformly checkable polynomially while both are necessary/sufficient, NP membership becomes implausible by representation; soundness/completeness must remain distinguished.

## finding_unverified

r losing locality. This matches “duality not implying dual succinctness”. Whether there are infinite all-n families where adversary witnesses are *never* translatable to polynomial sorter certificates (and vice versa) by *any* polynomial translation (not necessarily using that test) remains open in general, but the representation/algebraic obstruction is real and the falsifier as stated (“give a general polynomial-time translation...”) is not obvious and appears obstructed by the dual quantification/algebra. More directly: backwards induction is exponential; and there’s no known algebraic homomorphism. I cannot construct such a translation; attempting to force it hits the meet-vs-union/locality issue.

**Limits / honest answer:**
- Cannot produce a counterexample family or a proof that translation is impossible in ZFC without more structure; game duality is theorem.
- Cannot produce a translation. The obstruction is the dual representation (AND-OR) and meet vs union; the “same local test” is not applicable to dual form - soundness/completeness must be distinguished.
- This does not imply NP membership fails; it means representation matters. The complexity implication is as stated, but proving failure of dual succinctness for all-n families is nontrivial.
- No Lean/repo changes warranted - no substantive new theorem/counterexample established, just obstruction identified.

**Recommendation:** Focus on understanding whether adversary certificates can be forced into framed (meet-join) form. If not for some family, that would show dual succinctness fails. But constructing such family is hard. The obstruction is clear though. 

I should report this concisely to the board context as requested, but the user wants the answer/result. I need to give a mathematical finding/obstruction.**Finding (paper-level, no repo/Lean changes):** Game duality is exact ($S(n)\le k \Leftrightarrow$ sorter has winning strategy $\Leftrightarrow$ adversary has no winning strategy), but **dual succinctness does not follow**. The obstruction is algebraic/representational, not just existence.

**Why translation fails:** 
- Sorter framed certificates use **meet = intersection** of guaranteed poset relations at joins (conjunctive knowledge). Soundness is a local intersection test.
- Adversary winning strategies are **disjunctive** (∀ sorter moves ∃ adversary response). A compact adversary certificate cannot in general be compiled to a compact sorter DAG by polynomial local meet-join operations (backwards induction over all reachable posets is exponential). The dual needs **union/disjunction**, which is not checkable by the same local intersection test.

**Soundness vs completeness must be distinguished:** the “same local meet-join test” preserves soundness only for the conjunctive form; applying it to a disjunctive adversary form is wrong. Duality is game-theoretic, but the proof systems have different operations and different checkability.

**Limits:** I cannot construct an infinite all-n family where translation is provably impossible, nor a polynomial translation. The falsifier is obstructed by AND-OR duality + meet/untion. This makes NP-membership-by-representation implausible if both forms are needed but only meet-join is locally polynomial-checkable; however, without a concrete untranslatable family or a lower bound on proof size, this remains an obstruction argument, not a theorem separating classes. General-poset hardness does not transfer to the antichain root.


## Other metadata

```json
{
  "finished_at": 1793859514.8881197,
  "started_at": 1793859043.779279
}
```
