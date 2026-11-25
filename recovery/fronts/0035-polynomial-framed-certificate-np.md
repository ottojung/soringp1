# polynomial-framed-certificate-np

## status

investigated

## origin

executive_manual

## agent_id

HBWIaR5bYabCRw1bJe1ZVC-pinkish

## exit_state

clearexit

## question

For every n, does there exist a polynomial-size (in n) framed comparison DAG encoding some height-S(n) sorting strategy that is accepted by a polynomial-time soundness verifier? If not for all n, prove an infinite family with superpolynomial minimal frame size.

## basis

research-plan.md states polynomial-size permutation-framed DAG certificate completeness is open; prior unary-np-certificate-framed-dag investigated but left open.

## falsifier

Construct an infinite family of n with every height-S(n) strategy requiring framed-DAG size 2^(Omega(n^epsilon)) or prove the completeness gap is absolute for some explicit family.

## implication

A positive all-n polynomial completeness result would place SORT-BOUND-U in NP; combined with sparsity/Mahaney this gives strong constraints and a concrete upper-bound certificate.

## finding_unverified

keleton-preserving alignments, while the designer picks the **best** (min-loss) alignment. The honest lower bound requires minimizing over alignments — ideally *all* 8! relabelings. Let me brute-force the designer-optimal alignment (min over all 40320 permutations, both directions) for each pair, with memoization.
0.1s for 105 pairs × 40320 perms is impossible — and worse, the design has a **conceptual bug on my side**: applying the *same* permutation q to both states makes `e(A∩B)` permutation-invariant, so minimizing over perms is meaningless anyway. But the λ=0-everywhere result contradicts最基本的 monotonicity (`e(A∩B) ≥ max(eA,eB)` should give λ ≥ log₂(47/40) for unequal-e pairs). Let me debug one pair directly with counting.
My "permutation-invariance" reasoning was wrong — the code bug was elsewhere: `A[q[v]] & B[q[v]]` ANDs two *different* source rows; a correct relabeled intersection needs `π(A)` and `B` intersected row-wise. Also the designer has only **one** relative permutation ρ (fix B, relabel A by ρ). Let me redo this correctly: full ρ-search with a skeleton-alignment prefilter, plus a random sample over misaligned perms to make sure the prefilter isn't discarding better alignments.
Worktree clean, no external effects — the interrupted runs were pure compute. Now a key simplification emerged from re-reading the entropy identity: since the join state satisfies `Q = ρ(A) ∩ B ⊆ ρ(A)` and `⊆ B`, we always have `e(Q) ≥ max(e_A, e_B)` **regardless of alignment** ρ. With `λ_b = log₂(e(Q)/e(m_b))`, the arc whose incoming state has the *smaller* extension count is forced to pay `λ ≥ log₂(max/min)` — a permutation-independent lower bound. Let me verify this on the n=8 family cheaply (no 40320-perm search needed).
Inspected state: worktree clean, no commits/posts/edits were made by the interrupted turns — they were pure compute. Nothing to undo.

Continuing the unfinished step produced a **negative result plus one clean lemma**:

**Alignment-free lemma (correct, cheap).** At a join, `Q = ρ₁(m₁) ∩ ρ₂(m₂) ⊆ ρᵢ(mᵢ)`, and `e` is relabeling-invariant, so `e(Q) ≥ max(e(m₁),e(m₂))` for *every* choice of frames. Hence `λᵢ = log₂(e(Q)/e(mᵢ)) ≥ log₂(max(e₁,e₂)/eᵢ)`: the arc carrying the smaller extension count is forced to pay the full `log₂(max/min)` — no permutation search needed. (My earlier 40320-perm brute force was both buggy and unnecessary.)

**n=8 winning family (s=2,L=4, 15 states, k=16, log₂8!=15.299, budget 0.701 bits):**
- e-values only: 36,38,38,38,40,40,41,41,46,46,47,47,47,47 — spread factor 1.31, so forced λ is at most **0.38 bits**, under the 0.70-bit budget.
- 90/105 pairs unequal-e → forced λ min 0.031; 0 of 90 exceed budget.
- 15 equal-e pairs → lemma only gives λ≥0; identity alignment gives 0.17–0.77 bits.

**Conclusion (negative):** the entropy/forgetting identity *cannot* forbid merging winning-frontier states at the optimal budget — their extension counts are too close together. The hoped-for merge-infeasibility lower bound does not materialize, at least at n=8. This is a real obstruction to that route, not a weak test.

Two ways forward: (a) record the alignment-free lemma + this negative experiment as a short addition to `docs/research-framed-certificate-frontier.md` §4 (a barrier on the entropy route), or (b) stop here and report no result. I did not edit anything yet, pending your call — the contract discourages small-n enumeration and routine doc edits, so I'd only write it up if you consider the barrier substantive.

## Other metadata

```json
{
  "finished_at": 1793345679.084445,
  "started_at": 1793334138.6012309
}
```
