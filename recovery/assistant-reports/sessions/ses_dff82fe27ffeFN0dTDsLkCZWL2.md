# antonina-GpgBkjCvumGT92hcAulo73-puffs

Session: ses_dff82fe27ffeFN0dTDsLkCZWL2
Workspace: /home/lubko/soring-fronts/binary-minimax-additive-constant-alln
Created: 1795304522218; updated: 1795306238565

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_2008471db001mkaUacnDs43tBS)

I'll start by carefully inspecting the current state — since the previous turn may have performed side effects, I need to understand what actually happened before doing anything.

## Output 32 (msg_200848709001V5yYPqOfk6I0F2)

I'm on `billy-dev` (correct host), single worktree, clean status. Let me gather the board digest, the problem/literature docs, and the ledger state for this specific front.

## Output 55 (msg_20084a09b001DW6lHvnG0HlpuZ)

Let me read the full board messages about the binary-rate result and check for any existing scratch work or ledger entry for this specific front (in case the interrupted turn left something).

## Output 74 (msg_20084bd68001zaCsx7vSLUADRx)

There's a **ledger entry** for this exact front, plus prior scratch. I must determine whether the interrupted turn already posted a result to #301. Let me check the ledger and search the board specifically for this front's tag.

## Output 89 (msg_20084e19c00133JHWUiSchjkS6)

The board has **zero posts** for this front (`additive-constant` → 0 matches), so no result was posted by the interrupted turn. Let me inspect the ledger entry and the prior scratch files that define B(n) and the known result.

## Output 121 (msg_200850b3e001esPLCqmg8vm2Y7)

The board has no post for this front, and the ledger shows it as `running` (launched ~23:42Z) with no result. So nothing was posted by the interrupted turn; I'll continue the unfinished mathematical work.

Let me now understand the mathematical structure deeply. First, let me verify the known values and try to extend the exact computation.

## Output 136 (msg_200887c0d001zWn5GNcaz2HXUf)

Let me run the exact minimax solver for larger n in the background while I research the literature and develop the theory.

## Output 178 (msg_2008cb0c5001Tmt4DWgJISftgl)

Let me try the literature search again with different phrasing, and check the solver progress.

## Output 221 (msg_2008fef74001iDWa3tSlfMaBvM)

Let me try fetching a search page directly and check the solver.

## Output 236 (msg_2009093e4001Tw6eDd1uDBzcPa)

I need to test a potential construction rigorously. Let me write code to check an "interior recursion + endpoint reading" algorithm and verify the model.

## Output 247 (msg_20091b3af001J7FDdQsp4LYSeG)

I've developed a concrete lower-bound argument. Let me verify it computationally before committing to it.

## Output 265 (msg_20094ed00001utPmL4Ga271PgF)

The lower bound is verified. Let me check the posting mechanism and the current board state before posting, and confirm no new posts about this front arrived.

## Output 280 (msg_2009537d3001Nll6jLOJMro2I0)

I have a rigorous lower bound. Let me write it up carefully and post to board #301 (the only external side effect, as required by the contract).

## Output 307 (msg_20095e76a0013L9rJltsZRb1Di)

The post succeeded. Let me verify it appears on the board and confirm no duplicate.

## Output 327 (msg_200963259001wDXTMB7xgq6CBd)

Let me check how prior researchers recorded findings in the ledger, to decide whether a status update is appropriate.

## Output 347 (msg_200966f11001DXzqWuaOiB13Xl)

I'll record the finding in the durable ledger (standard completion record, not a repository change), being careful to preserve all other entries.

## Output 383 (msg_20096dad2001aw6WRAg66L2XLW)

## Result

**The bounded-additive-constant horn is false: `B(n) − n → ∞`, growing like `⌈log₂ n⌉`.**

### Theorem (proved, paper proof + computational check)
For all `n ≥ 3`:

\[
(n-2) + \lceil \log_2 n\rceil \;\le\; B(n) \;\le\; (n-1) + \lceil \log_2(n-1)\rceil .
\]

The upper bound is the existing #301 construction. The **lower bound is new here**. It follows that `B(n) − n = ⌈log₂ n⌉ − 2 + ε(n)` with `ε(n) ∈ {0,1}`; for `n = 2ᵏ+1` the bounds coincide and `B(n) = n + ⌈log₂ n⌉ − 2` exactly.

### Proof of the lower bound
Adversary answers **YES** to the first `n−2` comparisons. A YES to `(i,j)`, `i<j`, imposes `xᵢ ≤ xⱼ`; all relations go from smaller to larger index, so the constraint set is a **subposet of the natural order** (crucially, *not* a general poset).

**Lemma:** with `k` such relations, the number `u(P)` of consistent bit-vectors satisfies `u(P) ≥ (k+2)·2^{n−k−1}`. The relation graph is a forest; a tree component on `s` vertices has `≥ s+1` up-sets (leaf deletion + induction), and splitting `k` across components only increases the product, with equality for a chain. Verified exhaustively for `n ≤ 7`.

The number of distinct output-classes is `c(P) = u(P) − s + 1 ≥ u(P) − n` (the `≤ n+1` suffix up-sets collapse to the identity class). At `k = n−2`: `c ≥ 2n − n = n`. From there the adversary keeps the larger class-branch, so `cⱼ ≥ n/2ʲ`; reaching one class needs `j ≥ ⌈log₂ n⌉` more comparisons. Total `≥ (n−2) + ⌈log₂ n⌉`. ∎

### Falsification attempts
I tried and rejected `n + O(1)` constructions: right-anchor scan `(i,n)`, left-anchor scan `(1,j)`, interior recursion + endpoint reading, and crossing-pair scans. Each fails when `x₁=0, xₙ=1` with an interior monotone segment — a monotone segment of length `m` inside a non-identity string needs `⌈log₂ m⌉` comparisons to locate its boundary, and these accumulate to `log₂ n`. This is why the bounded-constant route genuinely fails.

### Honest limits
- The **literal falsifier** `B(n) ≥ n + ⌈log₂ n⌉` is impossible (upper bound `≤ n + ⌈log₂ n⌉ − 1`), but the unboundedness it was meant to test is settled YES.
- The exact `ε(n) ∈ {0,1}` for general `n` remains open (e.g. `B(12) ∈ {14,15}`; my exact minimax run was still pending when stopped).
- This is a **restricted-family value theorem**: the Lemma is specific to subposets of the index order, and the adversary/counting argument certifies *soundness* of the lower bound — it is not a certificate-completeness result and yields **no SORT-BOUND-U placement**.

### Side effects (audit)
No repository/Lean/CI/branch changes, no commits. The interrupted turn had left **no** #301 post (verified twice before acting, and once after). My only external writes are: **one** #301 comment (`binary-minimax-additive-constant-alln`, 00:09:02Z, verified exactly once on the board) and the standard ledger entry update to `investigated`.

## Output 404 (msg_2009719f1001yjNNs1qAnUD0Ss)

No further action taken — the previous turn’s effects are already present and I did not duplicate them.

**Verified state (read-only):**
- Board #301: exactly **1** post tagged `binary-minimax-additive-constant-alln` (2026-11-22T00:09:02Z). No duplicate.
- Ledger `~/.local/state/soringp1/frontier-ledger.json`: front `binary-minimax-additive-constant-alln` is `investigated` (finished_at 1795306204.2) with the finding recorded.
- Git: `billy-dev` at `6a96398`, worktree clean; no commits/branches/PRs/Lean changes.

**Completed finding (already posted):** for `n ≥ 3`, `(n-2)+⌈log₂ n⌉ ≤ B(n) ≤ (n-1)+⌈log₂(n-1)⌉`, so `B(n)-n = ⌈log₂ n⌉ - 2 + ε(n)`, `ε(n)∈{0,1}`; `B(n)-n → ∞`. Bounded additive constant is refuted (restricted binary-order universe only; no SORT-BOUND-U consequence). The exact `ε(n)` in general and the exact `B(12)` remain open.
