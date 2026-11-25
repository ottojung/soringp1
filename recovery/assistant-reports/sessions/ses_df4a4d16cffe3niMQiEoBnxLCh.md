# antonina-9GLrvL3vMrTBvnryxVojpy-diffusing

Session: ses_df4a4d16cffe3niMQiEoBnxLCh
Workspace: /home/lubko/soring-fronts/envelope-new-proofs-effective-alln
Created: 1795486855099; updated: 1795487878527

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20b5b4039001ysC5yPF4PoMSbd)

I'll start by studying the repository: the contract, problem statement, board #301, and literature.

## Output 25 (msg_20b5b657b001EDg6CphYjzJ3Be)

We're already on billy-dev. Now let me get the board digest for #301 and the literature/frontier docs.

## Output 40 (msg_20b5b7534001vY3KHcYKefMs3x)

The digest is truncated. Let me pull the full text of the newest #301 message (`effective-sergeev-constant-20261124`) and the other EVIDENCE files.

## Output 129 (msg_20b5be83e001liQILFvs5syaXU)

I have the full newest #301 message. Key facts so far:

- The front's question: do concrete `C>0`, `n0` extractable from Sergeev's proof satisfy `S(n) ≤ ceil(log₂n!) + C·n/(log n)^(1/5)` for all `n ≥ n0`?
- The newest finding (FINDING 2/3): Sergeev's proof is unquantified O(.) chain; the published argument's own threshold is **doubly exponential** (~2^(2^38)); the low-band 100 ≤ a < 2^38 can't be covered (FINDING 3).

Now let me study the literature and plan docs.

## Output 144 (msg_20b5d31570019bShqtVuRjzCp4)

The baseline is now clear: exact values known through n=22, and `S(n) − log₂n! = O(n/(log n)^(1/5))` is Sergeev's established bound. Let me read the bound-gap research docs and the Sergeev PDF extraction data.

## Output 167 (msg_20b5eaaab001Skx9ipXo3dGEsR)

Now let me verify Sergeev's O-chain from the local PDF extracts and fetch the OEIS tables for the known values through n=22.

## Output 198 (msg_20b5f1611001IfoFCAa4ojBbeb)

Sergeev's O-chain is verified from the primary PDF. Key parameters: Lemma 4 (s ≥ 20, λ, µ, ε), Theorem 2 (s = ⌈2γ log a⌉, "a<100 handled with unquantified O"), Corollary 2, Theorem 3. Now let me fetch the OEIS tables for S(n) through n=22 to build the empirical surplus data.

## Output 263 (msg_20b60e5d6001SJzLJrSgY2zWVe)

The literature says exact values are known through n=22 (S(16)=46, S(17)=50, S(18)=54 per Stober–Weiß). Now let me build the empirical surplus table from the OEIS data and check the front's envelope against it.

## Output 292 (msg_20b665ec7001IMk9MclnCAtlex)

Now let me compute the surplus table and envelope consistency from this data.

## Output 303 (msg_20b671697001Q9t7Sv4c4ELpVK)

The surplus data is consistent with the front. Let me verify the exact surplus values independently and check the board-posting CLI syntax (for a concise #301 finding), plus confirm a clean worktree.

## Output 318 (msg_20b68543b001NyqNPjae6HA7TD)

Surplus table verified. Now let me check the board comment CLI and record a concise #301 finding.

## Output 347 (msg_20b68ff3d001rdaTQechowXlgK)

The board finding is posted. Let me finalize the numerical checks for the report (exact C for the front under natural-log, and the falsifier data points).

## Output 376 (msg_20b699198001PLKe5kV187EWo1)

The analysis is complete and the board finding is posted. Here is the final report.

---

# Research report — envelope front (all-n, unary `S(n)`), billy-dev

## 1. Study

Read and verified on billy-dev:

- `docs/problem.md` — model: adaptive worst-case comparison trees; `S(n) = min height(T)`; `L(n) = ⌈log₂n!⌉` information bound.
- `docs/operations.md`, `docs/literature.md` — baseline: exact values known through n=22 (Stober–Weiß: `S(16)=46, S(17)=50, S(18)=54`; `S(12)=30` vs `L(12)=29`; n=23 open).
- `docs/research-plan.md` — baseline table `S(n) = L(n)` for n ≤ 11; `S(12)=30`.
- `docs/research-sergeev-asymptotic.md` — entropy identity (Sec. 2) and the Sergeev chain.
- `docs/research-structural-lower-bounds.md`, `docs/research-one-ply-obstruction.md` — the structural-lower-bound frontier (tiny-n witnesses: `Merge(2,4)` at n=6, one-ply `L1` witness at n=5).
- Newest #301 message (full text): `effective-sergeev-constant-20261124` — FINDING 2 (SGGA/proof threshold is doubly exponential, ~2^(2^38)); FINDING 3 (band 100 ≤ a < 2^38 uncovered by Lemma 4: λ(3)=15.07>1, λ(s)<1 first at s=10).
- Primary literature: ECCC TR20-096 (local PDF extracts, SHA-256 17901b39…), Theorem 2 (p.28), Corollary 2 (p.29), Theorem 3 (pp.29–30) — "S(n) = log(n!) + O(n log^{−1/5} n)".
- OEIS A036604 (S(n)), A003070 (⌈log₂n!⌉) — empirical data below.

## 2. Precise claim (the FRONT)

**Claim.** ∃C>0, ∃n₀: ∀n ≥ n₀: `S(n) ≤ ⌈log₂n!⌉ + C·n/(log n)^(1/5)`, witnessed by a family of strategies that is structurally new relative to Sergeev's O(.) chain and to any finite check of it. (log base: natural, Sergeev's convention; `C>0` absolute. The "structurally new family" part is not logically disprovable — it asks about the nature of strategies.)

**Negation (disproof target).** ∀C>0, ∀n₀ ∃n≥n₀: `S(n) > ⌈log₂n!⌉ + C·n/(log n)^(1/5)` — the true surplus exceeds the envelope infinitely often (the surplus is not O(n/(log n)^(1/5))).

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
