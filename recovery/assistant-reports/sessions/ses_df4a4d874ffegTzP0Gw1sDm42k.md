# antonina-KJi4d28E3Vbq1JQNr8DYAu-starry

Session: ses_df4a4d874ffegTzP0Gw1sDm42k
Workspace: /home/lubko/soring-fronts/surplus-lower-bound-omega-alln
Created: 1795486853164; updated: 1795489025314

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20b5b3710001rt1m52AB0qjDK3)

I'll start by exploring the repository structure and the key documents, including the research board #301.

## Output 42 (msg_20b5b93a0001o8xj5lOtdahPAm)

The shell tool seems to be failing. Let me test basic commands to diagnose.

## Output 61 (msg_20b5ba5f200133P72fA9sCdQvA)

`execute` is a JS runtime for MCP tools; the right tool for shell commands is `shell`. Let me use it now.

## Output 76 (msg_20b5bd368001CY2wCOB0kXn90A)

The shell tool works now. I'm on `billy-dev`. Let me read the board digest, the literature, and the key research docs.

## Output 99 (msg_20b5be28b001AiOlG1gffGX6de)

Good — I'm on `billy-dev`, clean worktree at `6a96398`. I've read the problem, operations, Sergeev's asymptotic doc, and the n=12 nontightness note. Now let me look at the literature index, related research notes, and the board's excess fronts mentioned in the prompt.

## Output 122 (msg_20b5eacef001TX2T9KolptLm3K)

Let me check the other `~/soring-fronts/` directories (L-* fronts), search the board for the "excess-two-alln" and "branch-mass-telescoping" fronts the prompt mentions, and grep the durable ledger.

## Output 141 (msg_20b5ee0c2001JUoIoksJITR6Ns)

The durable ledger holds many relevant past fronts. Let me extract the ledger entries for the surplus/excess/tightness questions, and locate the board store to search for the "excess-two-alln" and "branch-mass-telescoping" fronts.

## Output 156 (msg_20b5f56bf001FV88gaPvwjGulW)

I now have the full picture of the target front: `surplus-lower-bound-omega-alln` (status running) — exactly the user's question. Prior fronts on the same questions exist (`branch-mass-telescoping-o-n-excess`, `surplus-linear-dichotomy-alln`, Fredman fronts with conflicting claims, `excess-two-realization-alln`, `dyadic-*` fronts). Since prior agents made *conflicting* claims about Fredman's bound, I need the primary literature. Let me:

1. grep the repo for Fredman references and inspect `scripts/evaluate.py` to compute exact `S(n)` and `C(n)` values for small `n`.
2. Web-search Fredman's bound and the Hauser/Haubel (?) heapsort excess paper.
3. Fetch Sergeev's ECCC TR20-096 text around pp.29–30.

## Output 179 (msg_20b6003d6001sdg4bQ11Cy66w3)

Web search is unavailable (`cancelled`). I'll rely on the local repo's primary literature notes + webfetch. Let me read the repo's Fredman/Sergeev references and compute the surplus table with `evaluate.py`.

## Output 202 (msg_20b61df6e001rplw1oANhWQulK)

`evaluate.py` is too slow for n=13, and `webfetch` can't handle the PDF. Let me check whether the shell has network access, search the host for local copies of the primary texts, grep the repo for all Fredman references, and compute the surplus table for n ≤ 11.

## Output 225 (msg_20b640c91001sw6uNohoFC9Hf4)

No network access (curl timed out). I'll rely on repo-local primary evidence. Key facts so far: `S(n)=C(n)` for n ≤ 11 and n = 20, 21 (per `certificates-barriers.md`); literature: `S(12)=30`, `S(13)=34`, `S(16)=46`, `S(17)=50`, `S(18)=54`, `S(28)≥99`. Let me compute `C(n)` for the literature range, scan all repo Fredman/surplus references, and find the two board fronts the user mentioned (`excess-two-alln`, `branch-mass-telescoping-o-n-excess`).

## Output 248 (msg_20b660464001ofws4r7DgUPxWc)

Surplus data so far (literature): `S(n)=C(n)` for n≤11, n=20, 21; +1 at 12–13, 16–18, 22; S(28)≥99 (C(28)=98). So surplus is 0 for small n — but that's finite. I need to understand **Fredman's actual result** (no network here) — let me search board history and exec worktrees for Fredman analysis, and run the surplus table for n=2..11.

## Output 267 (msg_20b71fbbc001qe93SNxQjtCvC4)

Let me resolve the precise model definition — I need the Lean definition of the sorting tree (the entropy identity I plan to use depends on it), then run a quick surplus-table computation.

## Output 287 (msg_20b746f6a001Ki4WKviOV0rlDj)

The Lean model confirms the combinatorial content I need: leaves ↔ permutations (bijective), so `S(n) = min{height: tree sorts all n! permutations}` and the note's entropy identity applies. Now let me verify the `C(n)` table, then attempt the mathematical attack on the claim `surplus = Ω(n/(log n)^(1/5))`.

## Output 302 (msg_20b76633f001y4gf2ZlBgWcK3R)

Let me read the project's research plan doc and survey all "surplus/excess" mentions across the repo for existing analyses.

## Output 317 (msg_20b77891e001i7xDFF0zZNOStM)

Now let me check the Antonina CLI's board-post mechanism (AGENTS.md requires reporting findings on board #301) before writing the research report.

## Output 337 (msg_20b78a768001KMsbtkH7OU2gPm)

Let me do a recovery audit for this front's slug on the board, then post the research result.

## Output 388 (msg_20b79e73c001M3u1pntNoH0lrr)

This is a key discovery — there are two recent opencode posts (02:29 and 02:35) on the surplus question, including a claim "Front attacked: claim REFUTED: surplus is sublinear, not Omega(n)" and a data check. Let me read them in full.

## Output 403 (msg_20b7a30de001xnHexO7BhVu0Vk)

I now have the full board picture. Two recent posts (02:29, 02:35 today) — one claims "claim REFUTED: surplus is sublinear, not Omega(n)" (Sergeev Theorem 3), the other a data check ("surplus ∈ {0,+1} for n≤22"). Neither directly settles the user's Ω(n/(log n)^(1/5)) claim. Let me post a finding/status to board #301 per AGENTS.md, then report.

## Output 423 (msg_20b7b9311001enVVbk2eH90Pa3)

The board post is recorded (`surplus-lower-bound-omega-alln — FINDING/STATUS`, 2026-11-24T02:56Z, opencode). Here is the research report:

---

## Claim attacked (all-n)

`surplus(n) = S(n) − ⌈log₂ n!⌉` is `Ω(n/(log n)^(1/5))` for all `n ≥ n0` — i.e. the exact sorting number genuinely exceeds the information bound by at least a constant times Sergeev's envelope. Falsifier: infinite family of optimal trees with `surplus = o(n/(log n)^(1/5))`.

## Studies done (billy-dev)

AGENTS.md, problem.md, operations.md, board #301 (recent posts; excess fronts `excess-two-alln`, `branch-mass-telescoping-o-n-excess`; today's 02:29/02:35 posts), literature.md, Fredman cites (research-certificates-barriers.md, research-hardness-boundaries.md, research-series-decomposition.md), Sergeev ECCC TR20-096 (Theorem 3: the envelope upper bound `S(n) − C(n) = O(n/(log n)^(1/5))`), research-plan.md, research-n12-nontightness.md, research-structural-lower-bounds.md, OEIS A036604/A003070.

## Data (experiment; `C(n) = ⌈log₂ n!⌉`)

`surplus = 0` for n ≤ 11 and at n = 20, 21 (certificates-barriers.md); `+1` at 12–13, 16–18, 22 (excess-sequence-structure front), 28 (S(28) ≥ 99 → surplus ≥ +1). So the known tight set is finite — infinitude is exactly the open question `info-bound-tightness-infinite`. The 02:35 data check agrees: surplus ∈ {0, +1} through n = 22, while envelope(22) ≈ 16.3.

## Mathematical findings

1. **[deduction]** Insertion gives `S(n) ≤ S(n−1) + ⌈log₂ n⌉` (Lean-model construction: extend optimal tree for n−1 with a binary-search insertion subtree of height ≤ ⌈log₂ n⌉ at each leaf). With `L_n = C(n) − C(n−1) ∈ {⌊log₂ n⌋, ⌈log₂ n⌉}` this implies `surplus(n) ≤ surplus(n−1) + 1` at non-power-of-two steps. Consistent with the data (drops occur at 20, 21).
2. **[paper deduction]** Entropy identity (docs/research-sergeev-asymptotic.md §4): `surplus = E[k−D] + Σ_v q_v(1 − h₂(p_v))` where `A := Σ_v q_v(1 − h₂(p_v)) = E[D] − log₂ n!`. Lower-bounding surplus reduces to lower-bounding the bias mass `A` of any near-tight tree; I attempted this and found the obstruction that `A = 0` is compatible with `surplus = E[k−D] ≥ 0` for "perfectly balanced" trees (every `p_v = 1/2`), so the identity alone does not quantify the excess.

## Failed approaches / obstructions

- **Falsifier (A):** no infinite family of optimal trees with small surplus was constructed; exhaustive small-n search infeasible (`scripts/evaluate.py` DP is infeasible at n ≥ 8); structural candidates (perfect-balanced families) not realized; the infinitude of the tight set (`info-bound-tightness-infinite`) is an open question here.
- **Proof (B):** no completed lower bound; note the 02:29 post claims "surplus is sublinear, not Omega(n)" via Sergeev — that does **not** settle the user's Ω(envelope) question (sublinear is compatible with Ω(envelope)); Fredman's exact statement is not locally established (no network; board fronts conflict between `fredman-additive-bound-alln` and `fredman-additive-eventual`).

## Status

**Open — both horns viable; neither refuted nor proven by the work here.** The literal falsifier reading ("∀n ≥ n0 with n0 ≤ 21") is refuted by literature fact (surplus 0 at 20, 21); the claim with n0 > 21 remains open. **Honest limits:** finite data through 22; no new theorem or counterexample integrated (no Lean/repo changes). Reported to board #301 as `surplus-lower-bound-omega-alln — FINDING/STATUS` (2026-11-24, opencode, worktree clean at 6a96398).

## Output 474 (msg_20b7c2b7200190EUC7ASKkkdeq)

## Recovery audit (post-backend-failure)

**What actually happened (verified):**

- **Git state**: worktree clean at `6a96398` (no commits, no untracked changes). Confirmed.
- **Board #301**: my finding post landed and is verified present:
  `surplus-lower-bound-omega-alln — FINDING/STATUS` (2026-11-24T02:56:28Z, opencode). No duplicate post made.
- **Durable ledger** (`~/.local/state/soringp1/frontier-ledger.json`): front `surplus-lower-bound-omega-alln` is still `status: running`, `finished_at: None`, `finding_unverified` empty. The board post is the durable finding; ledger reconciliation to `investigated` is handled by the keeper (`research_frontier.py`/`agent_pool_keeper.py`) based on the Antonina agent's exit state — **not** something I should force from here, to avoid side effects.
- **Scratch**: only `/tmp/opencode` artifacts (digests, board text); no repo/Lean/test/CI changes were made.

**Unfinished work (intentionally left to the keeper):** ledger status transition from `running` → `investigated` with `finding_unverified` populated. I did not edit the ledger manually because (a) that's the keeper's reconcile step, and (b) the recovery instruction is to report rather than guess.

**No external actions were duplicated.** The board post happened exactly once and was verified.

**Net result of this investigation**: the claim `surplus(n) = Ω(n/(log n)^(1/5))` remains OPEN — no proof or falsifier produced; findings posted to #301 (02:56Z). If the keeper needs the finding text, it's on the board. I will not re-post or re-run the keeper.
