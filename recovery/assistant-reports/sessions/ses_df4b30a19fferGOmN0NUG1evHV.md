# antonina-rGPpU1zw1Pp0X3ZCDUIgyP-upset

Session: ses_df4b30a19fferGOmN0NUG1evHV
Workspace: /home/lubko/soring-fronts/curator
Created: 1795485922806; updated: 1795486833640

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20b4cf6b7001Dt000tJ2ov9jzI)

I'll start by exploring the repository structure, the key docs, and the current board #301 to understand the context.

## Output 29 (msg_20b4e0bb0001CCkiVU446l0jrZ)

The repo is on `main` (the host context is billy-dev). Board #301 is Antonina issue #301 on the GitHub repo. Let me get the repo remote, read the literature notes, the keeper's frontier ledger, and the board digest.

## Output 52 (msg_20b4e422c001NpXX6H7LThjLoU)

The digest shows the newest board post from today (00:47Z) about an "effective-Sergeev constant" and points to `docs/research-sergeev-asymptotic.md`. Let me get the full text of the newest #301 posts and read the newest research doc.

## Output 71 (msg_20b4e9fc8001uLOeba3bpLZBNa)

Now let me fetch the newest #301 board posts in full (filtered to the recent ones, using `gh`), to ground the attack.

## Output 86 (msg_20b4ebfb6001uwAualf0cMk3MW)

`gh` isn't authenticated, but `board_digest.py` reads board pages locally. Let me look at how it fetches pages so I can get the full newest posts.

## Output 106 (msg_20b4ef11f001eU94YOskaz0RYk)

The `execute` tool is JavaScript-based; I'll use the shell with `python3` instead.

## Output 117 (msg_20b4f15460013O1VlMYZZFKhfY)

I now have the full text of the newest board post (`effective-sergeev-constant-20261124`, 2026-11-24T00:47Z). Next: study the primary literature — the local Sergeev TR20-096 extracts — and check the recent board recency context, plus read the repo docs on surplus/lower-bound landscape to avoid duplicating existing fronts.

## Output 136 (msg_20b51767a001hEXjoMYYT4ztmY)

The landscape is clear. Now the **attack**: I'll verify the newest board post's findings against the primary literature — the local Sergeev TR20-096 text extracts. Let me locate Theorem 2, Corollary 2, Theorem 3, Lemma 4 in the extracted text.

## Output 160 (msg_20b51bc2a0012Eo8u6ntP3tA2d)

The board post's findings are confirmed by the paper text (Lemma 4's explicit constants; the "a < 100, sufficiently large hidden O" sentence at page 28; Theorem 3 at pages 29–30; the `s = ⌈2γ log a⌉` and `λ(3)≈15.07>1` arithmetic). Now let me check the durable frontier ledger and scan the board for related sergeev/surplus/envelope fronts, to make sure any new curator fronts are genuinely non-duplicates.

## Output 175 (msg_20b54fa230010nsix5ynp4HRCv)

The ledger and board contain many surplus/Sergeev-themed fronts. I must verify my proposed new fronts are genuinely non-duplicates. Let me pull the questions of the surplus/Sergeev-themed existing fronts.

## Output 186 (msg_20b55cbe9001RXlbeiEARDX6eo)

Let me scan the remaining board pages (5–9) for the surplus/Sergeev-themed fronts and check the ledger's `surplus-parameter-*` fronts, so my new fronts avoid all duplicates.

## Output 197 (msg_20b56864c001D86DMv6D8LwP9i)

Let me calibrate the new fronts against the ledger entries themselves (id + question) for the excess/surplus/Sergeev family, plus read the `exec-excess-boundedness-20261120` post fully — to be sure none of my proposed questions are duplicates.

## Output 212 (msg_20b58239a001XktRLEvoPUR53H)

I now have the complete picture. Let me check for the last few slug-collision risks on the board and ledger for my three proposed new fronts, then write the JSON deliverable.

## Output 223 (msg_20b5a1ca5001PIQgUQZKh8YkeC)

No collisions. Writing the JSON deliverable to `/home/lubko/soring-fronts/curator/frontier-candidates.json`.

## Output 243 (msg_20b5a911e001riSTjig9b7KWBG)

The JSON deliverable is written and schema-verified. Here is the attack report.

## Attack on the newest board #301 claim

**Claim (front `effective-sergeev-constant-20261124`, posted 2026-11-24T00:47Z):** "Do concrete C>0 and n0, extractable from the published proof, satisfy `S(n) <= ceil(log2 n!) + C*n/(log n)^(1/5)` for all n >= n0?"

**Study done:** AGENTS.md, docs/problem.md, docs/operations.md, docs/literature.md, docs/research-plan.md, docs/research-sergeev-asymptotic.md, the digest of board #301 (page 1), and the primary-literature extracts of Sergeev's ECCC TR20-096 (local text, pp. 27–30).

**Attack result — the extraction reading is refuted; the existential reading is not refuted:**

1. I verified the board's FINDINGS 1–3 against the paper text. The chain `S(n) = log n! + O(n log^(−1/5) n)` (Thm 3, pp. 29–30) is built on Thm 2 (p. 28: `P_m(a) >= 2^(a+1/2) − O(a^(−γ)·2^a)`), Cor 2 (p. 29) and Lemma 4 (p. 27, explicit constants `λ=20·2^(−s/2)+64·2^(−s)`, `µ=30·2^(−s)`, `ε=1/(25·2^s)` but requiring `s ≥ 20`). The proof of Thm 2 discards the region a<100 via the sentence: *"For a < 100, the inequality (44) holds with sufficiently large values of the constant hidden behind the symbol 'O'. Thus, we may assume a ≥ 100."* — a pure existential sentence, no numbers.
2. No extractable (C, n0): extraction would require quantifying the O-terms of the chain, i.e., re-proving the inequalities with explicit constants — new work, not extraction from the published proof. Any honest completion of the argument within its own steps hits the band wall (FINDING 3): Thm 2 is constructive (the strategy must actually insert the elements), and at γ=1/5, a=100 the proof's own constants give s=3 and `λ(3)≈15.07>1`, so `v_i<0` — the inequality is vacuous; covering `100 ≤ a < 2^38` needs new explicit strategies.
3. Even the threshold of any completion (FINDING 2): `s = ⌈2γ·log a⌉`, `s ≥ 20 ⇒ log₂ a > 19/(2γ)`: `a > 2^38` at γ=1/4, `a > 2^47.5` at γ=1/5, so the proof establishes its conclusion only for `n ≳ 2^(2^38) ≈ 10^(8.3×10^10)`. No moderate-n0 extraction exists anywhere in the argument.
4. The existential reading — `∃C,n0: S(n) ≤ ceil(log2 n!) + C·n/(log n)^(1/5)` — is **not** refuted: it follows by standard absorption from Sergeev's Thm 3 (`S(n) = log₂ n! + O(n log^(−1/5)n)`). It is a deduction, not a counterexample.

**Soundness-vs-completeness / general-poset note:** this attack studies the exact function `S(n)` directly; the recent board fronts on poset invariants (`cospectral-gap-span-alln`, `ordinal-lift-m2-conflict`, etc.) are general-poset structural results, not transferable to `S(n)` without explicit reductions — not implicated here. The inexpectivity found is about the published proof's structure (completeness of extraction), not about `S(n)` values or `SORT-BOUND-U` membership; soundness of the paper's upper bounds is untouched.

**Honest limits:** I cannot rule out a fresh proof of the envelope with extractable constants — that is exactly the new front `envelope-new-proofs-effective-alln`. I could not exhaustively re-derive Lemma 2/Thm 3 from the paper; I checked the key inexpectivity claims against the extracted text (the a<100 sentence, `λ(3)≈15.07>1`, and the threshold arithmetic `19/(2γ)`).

**No Lean, repository or board/ledger changes; nothing posted; no theorem claimed.**

## Curator deliverable

Wrote `/home/lubko/soring-fronts/curator/frontier-candidates.json` — 3 new independent all-n falsifiable fronts (schema verified: ids 6–63 lowercase chars, question ≥75, falsifier ≥40, implication ≥40, basis ≥35; no duplicates of board #301 posts or the 739-entry durable ledger):

- **`surplus-lower-bound-omega-alln`** — is the surplus `S(n) − ceil(log2 n!)` at least `Omega(n/(log n)^(1/5))` (or is the envelope refutable)? Distinct from the board's upper-bound excess fronts (`excess-two-alln`, `branch-mass-telescoping-o-n-excess`).
- **`envelope-new-proofs-effective-alln`** — a structurally new envelope-achieving strategy family with effective constants, independent of Sergeev's O(.) chain.
- **`surplus-linear-dichotomy-alln`** — is the surplus `Omega(n)` (linear) or `o(n)`? Distinct from `haeubler-heapsort-antichain-excess` (a specific source family).
