# bounded-arithmetic-sortbound-proofs

## status

investigated

## origin

ai_proposal_unverified

## agent_id

T8C5kEGpfRDprqaq0dMi0n-political

## exit_state

clearexit

## question

For which bounded arithmetic theory T in {S^1_2, T^1_2, PV} can the basic minimax identity S(∅)=F(∅) and the comparison-tree axioms be proved for all n, and does provability of 'S(n)<=k' for relevant k_n translate to complexity consequences for uniform evaluation of unary SORT-BOUND-U?

## basis

Bounded arithmetic links feasible reasoning to P/PSPACE-like classes; the existing FO-descriptive fronts cover first-order fixed-point logics but not the Cook/Takeuti bounded arithmetic hierarchy for this specific combinatorial game.

## falsifier

Show that some key minimax/closure step is unprovable in a candidate theory T but is provable in a weaker combinatorial sense, or find an all-n equivalence showing T-provability would force a class collapse already ruled out by known barriers.

## implication

Characterizing the weakest theory proving exact S(n) bounds would connect descriptive/logic complexity (separate from FO(LFP)/FO(TC) fronts) to feasible reasoning, with no automatic class separation but a new structural constraint on uniform certifiability.

## finding_unverified

 closure. 
2. **Witness size:** "S(n)≤k" for optimal k is an existence of a tree of height O(n log n) but 2^(Ω(n log n)) nodes. Such a witness is not polynomial in N=n+k+1; hence the statement is not equivalent to any standard Σ^b_1 formula with polynomial witnesses. S^1_2's witnessing theorem (FP) does not apply. PV has even less power. T^1_2 stronger but still bounded induction over polynomial bounds — no obvious way to internalize exponential trees as feasible objects for the all-n minimax closure.
3. **Soundness vs completeness distinction:** The implication (tree exists => S(n)≤k, soundness) is trivial. The converse/completeness (S(n)≤k => minimax strategy exists) is the combinatorial minimax theorem; formalizing *all-n provability* of this closure in bounded arithmetic is the obstruction, not the truth. General-poset minimax is similar, but this is the special (permutation) case on the repo's exact model — still exponential state space.
4. **Class collapse test:** If T could prove "S(n)≤k" with polynomial certificates for relevant k, that would suggest SORT-BOUND-U ∈ NP (via T-witnessing) and combined with sparsity force P=NP (Mahaney) — a known-barrier collapse. But the obstruction above is *size/induction-based* (theory too weak to formalize the exponential closure/certificate), which is different from a direct proof forcing collapse. The falsifier as stated ("all-n equivalence showing T-provability would force a class collapse already ruled out") is not obviously realized; the more direct obstruction is **feasible non-formalizability of the exponential minimax closure** rather than a forced collapse. This is an important distinction (honest limit).

### Concrete failed approach / exact obstruction
**Exact obstruction:** No first-order bounded arithmetic theory in {PV,S^1_2,T^1_2} appears able to prove the all-n minimax identity S(n)=adv(univ) via the standard state-recurrence, because the induction measure is |S| ∈ {1,...,n!} (exponential in input length) while these theories admit only polynomially-bounded induction. Consequently, T-provability of "S(n)≤k" does not, by standard witnessing theorems, translate to polynomial-time uniform evaluation of SORT-BOUND-U; the structural constraint is on *uniform certifiability/formalizability*, not on combinatorial truth. I did not find an all-n equivalence forcing a collapse already ruled out — the barrier is size/induction. I also did not find a clean formal proof of unprovability (that would require model-theoretic arguments beyond a short literature deduction), so the result is an **obstruction/deduction with honest limits**, not a kernel-checked theorem.

### Notes on process
- Studied AGENTS.md, docs/problem.md, board #301 (recent entries) as requested.
- Consulted literature.md, kernel-results.md, Model/Minimax/Attainment, research-plan, hardness/certificates notes.
- Distinguished general-poset results from the permutation (sorting number) case; distinguished certificate soundness (easy) from completeness/formalizability.
- No Lean files created/modified, no repo changes. No claims of proof/collapse forced. 

**Bottom line:** The weakest-theory question is obstructed by exponential state space and exponential witnesses: bounded arithmetic (polynomial induction, polynomial witnesses) cannot feasibly formalize the all-n minimax closure for exact S(n), constraining uniform certifiability without implying the known class collapses. This is a structural obstruction, not a separation.

## Other metadata

```json
{
  "finished_at": 1793487828.5603707,
  "started_at": 1793487080.6695507
}
```
