# adversary-turing-pnp-reduction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ErXBh7a0PXMEQ8zrOnxtKP-absurd

## exit_state

clearexit

## question

Is SORT-BOUND-U decidable by a deterministic polynomial-time Turing machine with an NP oracle (in P^NP) for all n,k, without assuming membership in NP or coNP a priori, via an adaptive strategy that queries a suitable NP oracle about the comparison game?

## basis

docs/problem.md establishes PSPACE membership and sparsity barriers but leaves NP/coNP open; board #301 investigated NP-certificate soundness/completeness and coNP adversary certificates separately without settling Turing-reduction class membership; AGENTS.md treats class placement as a potential upper-bound result.

## falsifier

Show that no polynomial-time oracle machine making poly(N) queries to any NP language can decide {1^n # 1^k : S(n)>k} uniformly for all large n with the correct threshold, or construct an all-n adversary/strategy argument showing the minimax value requires a stronger query hierarchy than P^NP.

## implication

Membership in P^NP would be a concrete class upper bound below PSPACE distinct from NP/coNP; a separation from P^NP would be a stronger structural result than sparsity-based NP-hardness obstructions and would clarify where SORT-BOUND-U sits relative to the polynomial hierarchy.

## finding_unverified

Let us look at the board, literature, and the DFS/upper bound docs.
Let us look at certificates/barriers and the optimal-tree-np-certificate front finding if available.

Let us write up the analysis.

Let us look up the exact class relationships - but better to reason directly.

**Finding (paper proof):**

**Claim attacked:** SORT-BOUND-U ∈ P^NP (poly-time TM with NP oracle, adaptive queries) for all n,k without assuming NP/coNP a priori.

**Why naive binary search fails ([deduction], literature):**
- S(n)≤k ⇔ ∃ comparison tree of height ≤k sorting n elements. Tree has ≥n! leaves and 2n!−1 nodes in reduced form (problem.md §5.1) — exponential in input length N=n+k+1. No polynomial witness; verifying “sorts all permutations” by enumerating n! is exponential. So “∃ tree of height k” is not obviously in NP.
- Binary search needs an oracle for that predicate; if predicate not in NP, P^oracle is not the question.

**Game/alternation view ([deduction], Chandra–Kozen–Stockmeyer):**
- W(∅_n,k): sorter vs adversary on poset states (AND-OR game), k = O(n log n) moves. Direct oracle queries give Σ_k^P alternation; k(n) polynomial => in PH, above P^NP (P^NP = Θ_2^P ⊊ Σ_2^P ∩ Π_2^P in general). So hierarchy level grows with k(n).
- General AND-OR reachability is PSPACE-complete; our graph is the poset-refinement (permutohedron face) DAG — highly structured but exponential states.

**Sparsity/barriers ([literature]):**
- SORT-BOUND-U sparse. Mahaney/Fortune/Ogiwara–Watanabe forbid many-one/btt NP-hardness unless P=NP; Karp–Lipton gives PH collapse for Turing to sparse. These constrain *hardness*, not *upper bounds*. P^NP can contain sparse languages; a sparse set being in P^NP is not ruled out by these theorems.

**Assessment:**
1. **No obvious P^NP algorithm.** The natural collapse (tree-existence as NP) fails due to exponential certificate size. Alternation collapse to 2 queries is not apparent from poset structure.
2. **No known reduction showing P^NP-hardness.** SORT-BOUND-U is a tally/threshold of a single function S(n); standard P^NP-complete problems are more general. Also sparsity + tally structure is restrictive.
3. **Obstruction is structural, not a standard theorem.** To *disprove* P^NP membership for all n would likely require showing the k(n)-level AND-OR game on poset graph is not “Θ_2^P-evaluable” — i.e. the structure doesn’t collapse polynomial alternation. This is reminiscent of “game complexity” separations but proving it unconditionally is hard; also relates to whether poset games have special strategy complexity.

**Concrete failed approach / exact obstruction:** The front as stated conflates “exists polynomial witness” (NP) with “P^NP”. The real question is alternation depth. Without a theorem that poset refinement games collapse PH to Θ_2^P, P^NP membership is unsubstantiated. Conversely, without a reduction from a Θ_2^P-complete problem to this sparse tally language, separation is unsubstantiated. **Neither direction is established by known results in the repo/literature.** The most precise obstruction: exponential tree size + k(n)-alternating game => no obvious Θ_2^P evaluation; sparsity blocks standard completeness routes. This is a genuine open structural question, not resolvable by the cited barriers alone.

**Limits:** No counterexample found; no proof found. Cannot claim membership or separation. No repo changes proposed (would need substantive independently checkable theorem).

## Other metadata

```json
{
  "finished_at": 1793716348.2080286,
  "started_at": 1793715478.861563
}
```
