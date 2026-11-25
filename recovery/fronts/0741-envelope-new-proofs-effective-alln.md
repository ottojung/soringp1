# envelope-new-proofs-effective-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

9GLrvL3vMrTBvnryxVojpy-diffusing

## exit_state

clearexit

## question

Prove or disprove: there is a structurally new family of insertion strategies, independent of Sergeev's O(.) chain and of any finite check of it, giving an absolute constant C>0 with S(n) <= ceil(log2 n!) + C * n / (log n)^(1/5) for all n >= n0 - i.e. an explicit proof that the information envelope is attainable at moderate n.

## basis

Newest #301 front effective-sergeev-constant-20261124: inexpectivity of TR20-096's O(.) chain and the threshold >= ~2^(2^38) for any completion (FINDINGS 1-3); research-sergeev-asymptotic.md: 'Research: derive a finite effective group-insertion bound; or find sound worst-case pruning or succinct certificates from this entropy restriction for unary SORT-BOUND-U'; problem.md 'The bound gap' open question.

## falsifier

Prove a structural lower bound that every strategy family reaching the O(n/(log n)^(1/5)) envelope fails for all n <= B with B > 10^6, or exhibit the explicit new strategy with its constant and a correctness argument.

## implication

A positive resolution puts a new exact-envelope strategy within reach of finite computation for unary S(n) evaluation; a negative one moves the achievable envelope away from the information bound and resets the best-known contract for exact unary evaluation.

## finding_unverified

)).

## 3. Disproof attempts

**(a) Data check through n=22** (OEIS, cross-checked vs research-plan). Surplus δ(n) = S(n) − L(n): **+1 for n ∈ {12..19}, 0 for n ∈ {1..11, 20, 21}, +1 at n=22** (L(12)=29, L(16)=45, L(22)=70, L(20)=L(21)=S). Envelope gaps `gap(n)=n/(ln n)^(1/5)`: gap(12)=10.0027, gap(22)=17.5550. The front is data-consistent: `front(C=0.1, n0=12)` holds through n=22 (S(12)=30 ≤ 29+1.00027); max over 12≤n≤22 of the required constant is **0.09997** (at n=12). So the front is not refuted by the data.

**(b) Structural analysis (entropy identity).** For any correct tree of worst-case depth k: `δ = k − log₂(n!) = E[k−D] + Σ_v q_v(1−h₂(p_v))` (research-sergeev-asymptotic.md). Envelope attainment at moderate n requires the tree to carry near-all node measure on near-balanced nodes (p_v≈1/2) with `E[k−D] ≈ 0`. At n=12–19 the optimal trees have δ=1 — consistent; **no contradiction derived**.

**(c) FALSIFIER check.** The universal reading of the FALSIFIER ("no family reaches the envelope for all n ≤ B") is **refuted by the data**: at n=20, S(20)=62=L(20) — the optimal family reaches the envelope for any C>0; at n=22 with C≥0.057 the envelope is reached (71 ≤ 71.002). So the FALSIFIER, as a universal negative statement, is false by data; it does not challenge the front.

## 4. Honest negative result

- The front is **asymptotically true**: Sergeev's family already attains the envelope (`S(n) ≤ L(n) + O(n/(ln n)^(1/5))`). A disproof of the front would therefore require disproving Sergeev.
- Data through n=22 is consistent with the front (`C≈0.1, n0=12`); the envelope is genuinely attained at moderate n (n=22: 71 ≤ 70+1.7555).
- Obstructions to a disproof: (i) no known structural lower bounds on the surplus at moderate n — research-structural-lower-bounds.md and research-one-ply-obstruction.md stop at tiny-n witnesses; (ii) S(23+) is open; (iii) board FINDING 2/3: Sergeev's route to the envelope is dead below ~2^(2^38), but a different family is not ruled out.
- **No proof, no counterexample.** This is an analysis, not a theorem: the front remains open; the honest deliverable is the data + structural analysis + obstruction above.

## 5. Distinctions (per your ask)

- General-poset results (recent #301: cospectral M1/M2, gap-span, ordinal lifts) are structural facts about arbitrary posets — they **do not transfer** to the antichain minimax S(n).
- Certificate soundness ≠ completeness: the front is about worst-case tree heights (a quantity, upper-bound direction), not about NP/coNP certificates of SORT-BOUND-U; the PSPACE minimax characterization (research-certificates-barriers.md) is a different model.

## 6. Complexity implication

A positive resolution puts a new exact-envelope strategy within finite computation for unary `S(n)` evaluation; a negative one moves the achievable envelope away from the information bound. My finding: the front remains open — data supports attainability at moderate n, and disproof is obstructed by open lower-bound frontiers rather than refuted.

## 7. Board / worktree

- Posted concise finding to #301: `envelope-front-data-check-20261124` (slug; its only external write; the newest #301 message still stands as the effective-sergeev finding).
- No Lean/repo changes; worktree clean (per user constraint; AGENTS.md: clean worktree is a normal outcome).

**Honesty note:** nothing above is claimed as a mathematical proof — the front is data-consistent and asymptotically true via Sergeev; I could not disprove it.

## Other metadata

```json
{
  "finished_at": 1795487932.662224,
  "started_at": 1795486853.010386
}
```
