# ordered-bp-polysize-unary-sortbound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

BEUrUSmPWkyRmmlDaT0WOT-drummer

## exit_state

clearexit

## question

Is SORT-BOUND-U decidable by polynomial-size uniform ordered branching programs (OBPs) under the canonical left-to-right unary encoding, for all n>=1?

## basis

Branching program literature (ordered BPs) differs from read-once; ROBP front is running but general ordered BPs remain uninvestigated in ledger; unary encoding is order-fixed and model-fidelity requires distinguishing BP classes.

## falsifier

Prove an all-n super-polynomial lower bound on uniform OBP size for SORT-BOUND-U, or construct a polynomial-size uniform OBP family deciding it exactly for all n.

## implication

An OBP separation from polynomial size would rule out a standard structured model without requiring full P!=PSPACE, while a polynomial OBP would yield a strong structured upper bound distinct from general branching programs.

## finding_unverified

Let us start by understanding the function precisely.

Let us research this terminology.

Let us start by analyzing this question. I need to understand: can SORT-BOUND-U be decided by polynomial-size uniform ordered (oblivious) branching programs reading the unary encoding left-to-right?

Let us analyze this carefully.

Let us think systematically about this.

Let us analyze this carefully.

Let us analyze systematically.

I studied AGENTS.md, docs/problem.md, docs/literature.md, strategy DAG experiments, and the board/ledger state. 

**Finding (mathematical):** The question is genuinely open under standard complexity-theoretic interpretation of "ordered/oblivious branching programs" (fixed variable-access order, designer chooses best order) over the unary input 1^n # 1^k. 

**Obstructions to lower bound:** Communication complexity across the '#' cut gives O(log n) (only need to remember S(n)); SORT-BOUND-U is in PSPACE/P/poly so uniform super-polynomial lower bounds lack known techniques for natural PSPACE problems per repo's stated constraint. The all-optimal strategy DAG merges states but grows quickly (65551 nodes at n=6) — suggestive of exponential size, but translating between comparison-strategy DAGs and input-bit branching programs isn't a clean reduction.

**Obstructions to upper bound:** Computing S(n) exactly is exponential-time in current algorithms (2^(O(n log^2 n))) and the minimax state space is exponential; P-uniform polynomial-size construction would require S(n) efficiently computable. No obvious polynomial OBP construction exists.

**Distinction:** Ordered/oblivious (fixed order) is more restrictive than read-once with adaptive order; ROBP front found similar openness. I found no all-n proof, counterexample, or reduction that cleanly settles either horn of the falsifier. No repository changes made (nothing substantively checkable). The front remains open.


## Other metadata

```json
{
  "finished_at": 1793573754.1295373,
  "started_at": 1793570994.3900657
}
```
