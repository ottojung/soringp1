# antonina-CZ8czjMqjSAIy9MyEm8KqO-ashburton

Session: ses_df36e5a77ffeu3FCt3EBAxVPT7
Workspace: /home/lubko/soring-fronts/curator
Created: 1795507201825; updated: 1795507650208

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20c91a7ad001nSyBzWqCUQ9CBx)

I'll start by understanding the repository state and the documents I need to study.

## Output 21 (msg_20c91c770001BAZnL33aeNXwMT)

I'm currently on `main`, but the task requires operating on `billy-dev` only. Let me check branches and switch.

## Output 32 (msg_20c91dde8001QABumIqhtgrjZ9)

There's no local `billy-dev` branch visible. Let me look more broadly — perhaps it's a separate worktree or needs fetching.

## Output 73 (msg_20c923a08001G23zyUjD4OP7B1)

Let me read the key documents and find how the board works, plus identify the billy-dev commit.

## Output 96 (msg_20c9250f4001VgZSbqx8atT1SD)

`billy-dev` is the execution **host** (per operations.md), not a git branch — let me confirm the hostname and read the newest board #301 digest.

## Output 111 (msg_20c927552001Xdf8Q5jDYOzhqh)

I'm on host `billy-dev` — confirmed. The two newest board messages are key. Let me get their full text and check available tooling.

## Output 147 (msg_20c92b58b001BJWz99hwZQEFhn)

Let me extract the full text of just the two newest messages (they were truncated).

## Output 158 (msg_20c92d0460014oLY4hs2QPxkr4)

Let me check the full frontier ledger to avoid duplicate investigations, then examine the certificate grammar and key research notes.

## Output 178 (msg_20c9307f3001PITsSsnKx0F48C)

I now have the board context. Let me study the certificate grammar and the key research notes to ground a genuinely new direction.

## Output 202 (msg_20c939434001sbrpSDkloMhkna)

Let me inspect the full questions of potentially overlapping frontier entries before committing to a new direction.

## Output 213 (msg_20c93f50b001fKF8LL0bzdhYxj)

Let me scan the full recent board page for all of today's results, then look for genuinely unclaimed angles.

## Output 278 (msg_20c96373d001VEHdAw97ExXdCs)

Let me verify key numbers from the newest board independently and inspect the Sergeev source text to formulate a precise new question.

## Output 327 (msg_20c96d888001WHmrcTx1N8o5N2)

Let me try a genuine disproof attempt: examine whether Sergeev's own derivation permits a better exponent than 1/5.

## Output 347 (msg_20c97328d001WX0VA40wiBSs1h)

Let me verify the γ-parameter constraints more carefully before finalizing the question.

## Output 358 (msg_20c9793430014p0agXplSCVw7Q)

Let me do a final duplicate check on the board for my two candidate slugs, then write the JSON.

## Output 369 (msg_20c97cc9c001EMc2JXSPeJwRGs)

I have two genuinely new, non-duplicate directions grounded in the newest board and primary text. Let me write the curator output and validate it.

## Output 405 (msg_20c9855f5001ezSG18PnucrQoB)

Done. I studied `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, the newest board #301 (the two 07:36Z fronts plus the 00:47Z effective-Sergeev result), and the primary ECCC TR20-096 text. I checked all 748 ledger entries and the 25 previously investigated slugs before proposing anything.

**Disproof attempt (honest outcome).** I attacked the implicit claim that the exponent 1/5 in Sergeev's bound is forced by his method. Re-reading Theorem 2 (p.28–29): `s = ⌈2γ log a⌉` needs only `γ ≤ 1/4` for `φ > 0`, and the final bound is stated *"when, for example, γ ≤ 1/5"*; my arithmetic gives `2^{−s/2}=a^{−γ}` and `2^{−2s}=a^{−4γ}`, so the `exp(−Θ(a s⁻² 2^{−2s}))` term looks negligible for `γ < 1/4`. This **suggests** the cap is not 1/5, but I did not re-derive the proof — no proof or refutation is claimed. I also independently reproduced Lemma 4's `λ(s)=20·2^{−s/2}+64·2^{−s}` first dropping below 1 at `s=10`, matching the board. A second attack on the framed-DAG checker's meet-invariant yielded only a small soundness/completeness observation with no bridge back to `S(n)`, so I stopped that line.

**What I wrote** to `/home/lubko/soring-fronts/curator/frontier-candidates.json` — two new, non-duplicate fronts:
- `sergeev-gamma-exponent-sharpening-alln` — is every `γ < 1/4` admissible in TR20-096?
- `sergeev-schedule-surplus-rate-tightness-alln` — the schedule-level surplus rate lower bound the newest board says is missing for its falsifier.

Both are labelled with the text/arithmetic basis, not as proofs.

**Limits.** No theorem, no counterexample, no value of `S(n)`, no improved algorithm, no class placement — `SORT-BOUND-U` and `S(n)` remain open. General-poset findings and certificate *soundness* were kept strictly separate from completeness. No Lean, source, test, CI, ledger or board changes; worktree clean at `f89f6d0` on host `billy-dev`, with only the required curator JSON untracked.
