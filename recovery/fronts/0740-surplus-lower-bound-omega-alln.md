# surplus-lower-bound-omega-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

KJi4d28E3Vbq1JQNr8DYAu-starry

## exit_state

clearexit

## question

Prove or disprove: the surplus S(n) - ceil(log2 n!) is Omega(n/(log n)^(1/5)) for all n >= n0 - that is, the exact sorting number genuinely exceeds the information bound by at least a constant times Sergeev's envelope; or exhibit an infinite family of correct trees with surplus o(n/(log n)^(1/5)).

## basis

Sergeev's Theorem 3 (ECCC TR20-096, local text pp.29-30): S(n) - ceil(log2 n!) = O(n log^(-1/5) n), the only envelope upper bound in the repo; Wells: S(12)=30 vs C(12)=29 (research-n12-nontightness.md); the board's excess fronts (excess-two-alln, branch-mass-telescoping-o-n-excess) ask upper bounds or a weaker Omega(n/polylog n), so this is a distinct lower-bound question.

## falsifier

Exhibit an infinite family of correct trees with height S(n) whose surplus S(n) - ceil(log2 n!) is o(n/(log n)^(1/5)) for every n in the family - the Omega lower bound would be refuted - or prove the Omega statement for all n >= n0.

## implication

If refuted by a constructive family, the exact value S(n) tracks the information bound within any sub-envelope and the waste of exact unary evaluation is genuinely small; if confirmed, Sergeev's envelope is tight up to constants and the information-bound excess of S(n) is at least a constant times n/(log n)^(1/5).

## finding_unverified

ary-search insertion subtree of height ≤ ⌈log₂ n⌉ at each leaf). With `L_n = C(n) − C(n−1) ∈ {⌊log₂ n⌋, ⌈log₂ n⌉}` this implies `surplus(n) ≤ surplus(n−1) + 1` at non-power-of-two steps. Consistent with the data (drops occur at 20, 21).
2. **[paper deduction]** Entropy identity (docs/research-sergeev-asymptotic.md §4): `surplus = E[k−D] + Σ_v q_v(1 − h₂(p_v))` where `A := Σ_v q_v(1 − h₂(p_v)) = E[D] − log₂ n!`. Lower-bounding surplus reduces to lower-bounding the bias mass `A` of any near-tight tree; I attempted this and found the obstruction that `A = 0` is compatible with `surplus = E[k−D] ≥ 0` for "perfectly balanced" trees (every `p_v = 1/2`), so the identity alone does not quantify the excess.

## Failed approaches / obstructions

- **Falsifier (A):** no infinite family of optimal trees with small surplus was constructed; exhaustive small-n search infeasible (`scripts/evaluate.py` DP is infeasible at n ≥ 8); structural candidates (perfect-balanced families) not realized; the infinitude of the tight set (`info-bound-tightness-infinite`) is an open question here.
- **Proof (B):** no completed lower bound; note the 02:29 post claims "surplus is sublinear, not Omega(n)" via Sergeev — that does **not** settle the user's Ω(envelope) question (sublinear is compatible with Ω(envelope)); Fredman's exact statement is not locally established (no network; board fronts conflict between `fredman-additive-bound-alln` and `fredman-additive-eventual`).

## Status

**Open — both horns viable; neither refuted nor proven by the work here.** The literal falsifier reading ("∀n ≥ n0 with n0 ≤ 21") is refuted by literature fact (surplus 0 at 20, 21); the claim with n0 > 21 remains open. **Honest limits:** finite data through 22; no new theorem or counterexample integrated (no Lean/repo changes). Reported to board #301 as `surplus-lower-bound-omega-alln — FINDING/STATUS` (2026-11-24, opencode, worktree clean at 6a96398).
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

## Other metadata

```json
{
  "finished_at": 1795489052.9534483,
  "started_at": 1795486851.2407813
}
```
