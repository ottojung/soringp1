# sergeev-gamma-exponent-sharpening-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

lAqVc2Ij8H3bHBfoZLfhYD-boxes

## exit_state

clearexit

## question

For Sergeev's TR20-096 container construction, Theorem 2 sets s = ceil(2 gamma log a) and states the bound P_m(a) >= 2^{a+1/2} - O(a^{-gamma} 2^a) only 'when, for example, gamma <= 1/5'. Is every gamma < 1/4 admissible, yielding S(n) <= log2(n!) + O(n / (log n)^gamma) for all n, or does some error term force a hard exponent cap at 1/5?

## basis

Primary TR20-096 p.28-29: phi > 0 requires only gamma <= 1/4 while the final bound is stated 'when, for example, gamma <= 1/5'; p.29 Corollary 2 fixes 1/5. Direct arithmetic gives 2^{-s/2} = a^{-gamma} and 2^{-2s} = a^{-4gamma}, so the exponential error term appears negligible for gamma < 1/4; this is a textual and arithmetic observation, not a proof.

## falsifier

A careful re-derivation exhibiting an error term, for instance exp(-Theta(a s^{-2} 2^{-2s})) or the lambda <= 1/50 condition, that blocks every gamma > 1/5 would refute the improvement; an explicit gamma > 1/5 derivation with all constants checked would refute the 1/5 cap.

## implication

An admissible gamma closer to 1/4 would sharpen the uniform upper envelope on the exact value S(n) and shrink the k-range a unary threshold decider must search; it is not by itself a faster evaluator or a class placement, and it would strengthen schedule-level surplus estimates used by the newest #301 framed-DAG barrier.

## finding_unverified

{−4γ}`, the exponent grows polynomially for **all γ < 1/4** — negligible, not a cap. (OCR renders this as `2^a − O(...)`, which falsely looks like a `2^a`-sized subtraction.)
- Preconditions are γ-independent: Lemma 4 needs only `s ≥ 20` (equivalently `λ ≤ 1/50` at s=20, λ(19)>0.02), achieved by `a ≥ 2^{10/γ}` for any γ>0; and `φ>0` is proved in the paper for all γ ≤ 1/4 (verified at a=100, γ=1/4). Condition (17) reduces to `2log₂m ≤ a + 2log₂a + O(1)` — γ cancels.

So the same derivation yields `P_m(a) ≥ 2^{a+1/2} − O_γ(a^{−γ}2^a)`, then `Q_{2m}(a) ≥ 2^a(1−O_γ(a^{−γ}))`, and Theorem 3's unchanged recurrence gives **`S(n) ≤ log₂(n!) + O_γ(n/(log n)^γ)` for all n and all γ<1/4**. The genuine hard cap of this argument is γ<1/4, not 1/5: for γ∈(1/4,1/3) the exponential term reverses and blocks the bound.

**Honest limits.** No explicit `C_γ, n₀` — everything remains in unquantified O(·); the crossover for the exponential term explodes as γ→1/4 (roughly `log₂ a ≈ 130, 247, 899, 11660` at γ = .2, .22, .24, .249 under one constant estimate), so nothing improves at moderate n or helps n=23. This concerns a sorting *strategy's* comparison count, not evaluating S(n): no faster evaluator, no practical k-range narrowing, no class placement. General-poset and certificate-soundness results were kept separate from completeness at the antichain root. I could not access the 2021 journal full text, so this is an independent re-derivation, not a priority claim.

**Environment:** billy-dev only, worktree clean at `6a96398`; no Lean, repo, test, CI, or ledger changes — scratch files confined to `/tmp/opencode`; the board comment is my only external write.
I'll perform a recovery audit before doing anything else. From this conversation I know a board post was made last turn, but I'll verify externally rather than trust that.
There are scratch files from ~07:35 that I did not create in this turn. Let me inspect them and check for any earlier board side effect.
## Recovery audit — complete, no action repeated

**What actually happened (verified, not assumed):**

| Effect | Status |
|---|---|
| Board #301 post, slug `sergeev-gamma-exponent-sharpening-alln` | **Exactly 1**, at `2026-11-24T08:18:05.041Z`, author `opencode[front:sergeev-gamma-exponent-sharpening-alln]`. Independent scan of all 11 board pages found no second copy and no near-duplicate phrase. |
| Git state | `billy-dev`, clean `git status --porcelain`, HEAD `6a96398`, empty stash — unchanged before and after. |
| Commits / PR / Lean / repo / test / CI / ledger writes | **None.** The ledger front entry was only read, not modified. |
| Scratch files | Mine: `/tmp/opencode/board_full.py`, `gamma_check{,2,3}.py`, `tr2096-page*.png`, `board_post.txt`, `post_result.json`. The older `board_post.md` / `board_post_result.json` (07:35) belong to the **distinct** front `succinct-adversary-copnp-sortboundu-alln`, whose post is on the board at 07:36:09Z — not my work, not touched. |

**Determination:** the only external side effect of this front was the single #301 result comment. It landed successfully and was already verified last turn; there is nothing uncertain requiring review and nothing to re-post.

**Unfinished work:** none. The commissioned question was answered (the 1/5 cap is not forced; every γ<1/4 is admissible, with the honest limits recorded in the post), the falsification attempt failed as reported, and the stop condition was reached. I will not duplicate the post, commit, or modify the ledger.

## Other metadata

```json
{
  "finished_at": 1795508407.299521,
  "started_at": 1795507673.2541192
}
```
