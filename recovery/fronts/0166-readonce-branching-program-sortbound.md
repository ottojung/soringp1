# readonce-branching-program-sortbound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

nHth8ohf7P3tgpjj2auwy8-braunau

## exit_state

clearexit

## question

Is SORT-BOUND-U computable by polynomial-size uniform read-once branching programs (ROBP) over the unary input representation, and can the comparison-adversary structure of the antichain give an all-n exponential ROBP lower bound or a polynomial upper bound?

## basis

SORT-BOUND-U is in PSPACE and P/poly; branching program/ROBP complexity is unexamined in repo fronts and does not obviously collide with the sparsity/circuit-lower-bound P/poly barrier in the same way as general nonuniform circuits.

## falsifier

Prove a super-polynomial uniform ROBP lower bound for SORT-BOUND-U for all large n, or construct a polynomial-size uniform ROBP family recognizing SORT-BOUND-U.

## implication

ROBP lower bounds are often tractable and would separate SORT-BOUND-U from restricted classes without requiring a full P!=PSPACE proof; a polynomial ROBP would be a strong structural upper bound for exact sorting-number evaluation.

## finding_unverified

PLEXITY IMPLICATION: ROBP lower bounds are often tractable and would separate SORT-BOUND-U from restricted classes without requiring a full P!=PSPACE proof; a polynomial ROBP would be a strong structural upper bound for exact sorting-number evaluation. EVIDENCE: SORT-BOUND-U is in PSPACE and P/poly; branching program/ROBP complexity is unexamined in repo fronts and does not obviously collide with the sparsity/circuit-lower-bound P/poly barrier in the same way as general nonuniform circuits."

This reads like a research front/problem statement that was just given to me. The instruction says "On billy-dev ONLY, study AGENTS.md..." - this is the task. I need to execute this research.

Let us think more precisely about the ROBP structure.

Let us look up standard results about ROBP/lower bounds and also think again carefully.

Let us analyze carefully.

Let us analyze the ROBP question systematically.

Let us write up a detailed analysis and see if we can find a real obstruction.

I studied AGENTS.md, docs/problem.md, docs/literature.md, the strategy DAG experiments, and the board/ledger state. The ROBP question splits cleanly.

**Analysis (all-n, falsifiable):**

- **Input/structure:** SORT-BOUND-U = {1^n # 1^k | S(n)≤k} read left-to-right. A read-once BP can count prefix 1's (to get n) and suffix 1's (to get k), but must test S(n)≤k. The natural cut after '#' gives communication matrix of threshold rows with different thresholds S(n); deterministic communication complexity is O(log n), so standard communication complexity gives no exponential lower bound.
- **Uniformity obstruction:** a polynomial-time uniform family would need to construct B_m knowing S(n) for all n≤m-1. Computing S(n) exactly is exponential-time (minimax/budgeted DFS) and not known in P; also values unknown for n≥23. But the constructor builds the BP structure, not necessarily computes values on-the-fly - and for each fixed m one could in principle hardcode S(n) if known. The real blocker is likely not "can't know values" but "can't compute efficiently / BP can't encode exponential computation".
- **ROBP restriction is the key:** polynomial-size ROBPs are strictly weaker than general polynomial-size BPs and incomparable in some ways to P/poly barriers (sparsity doesn't block). The repo notes "branching program / DAG strategy" as an open candidate witness (research-encoding-consequences.md:495) and strategy DAG experiments show exponential growth of optimal-strategy DAGs; framed certificates distinguish soundness from completeness. However, translating strategy-DAG size to ROBP lower bounds requires care - ROBP reads (n,k), not permutations.
- **No obvious exponential lower bound:** no standard fooling set/communication complexity argument gives super-polynomial lower bound for this specific structure. Constructing a polynomial-size uniform ROBP also seems nontrivial given S(n) complexity, but not obviously impossible.

**Honest conclusion:** The question is genuinely open. A polynomial upper bound would need either S(n)∈P or a very clever uniform ROBP construction; an exponential lower bound would require a ROBP-specific lower-bound technique exploiting the minimax/adversary structure of sorting from the antichain. I found no all-n proof either way, no counterexample, and no way to cleanly reduce general-poset hardness to this fixed antichain family without more structure. No repository changes made (nothing substantive independently checkable). The front remains open.


## Other metadata

```json
{
  "finished_at": 1793571547.6343434,
  "started_at": 1793567593.3608155
}
```
