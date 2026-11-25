# antonina-KO0RYwGgDxmUjIV2Qvb4uH-macerated

Session: ses_e1493a546ffeM7qUC9V0hmRzzX
Workspace: /home/lubko/soring301-exec-sergeev-effective-window-20261117h
Created: 1794951109329; updated: 1794951758607

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 286 (msg_1eb75c44a001c0r3MBxNDeZozw)

**Result: second branch — precise blocker decomposition and no-go for extraction from the published proof.** No explicit polynomial-time `W(n)` can be read off from Sergeev’s proof as written.

### Conclusion
- **[literature]** Sergeev (ECCC TR20-096, Theorem 3) proves `S(n)=log₂(n!)+O(n/(log n)^{1/5})`, hence some finite window exists in principle.
- **[paper audit]** The published proof does **not** supply the constants or finite thresholds needed for an all-`n` inequality `S(n) ≤ C(n)+W(n)` with explicit computable `W(n)`.
- **[deduction]** Therefore the requested extraction route is blocked at the level of the published proof; obtaining an explicit window requires a new constant-tracking reanalysis or a different construction.

### Blocker decomposition

1. **Untracked constants.**
   - **[paper audit]** The `1/5` exponent enters through `s = ceil((2/5) log a)` with Lemma 4 requiring `s ≥ 20`.
   - This forces `a ≥ e^{47.5}` (depending on log base), and since `a ≈ log₂ n`, any extraction following the published construction has threshold at least `N ≥ 2^{2^{47.5}}`.
   - **[paper audit]** Theorem 2/Corollary 2 and Theorem 3 contain `O(·)` terms (`O(a^{-1/5}2^a)`, `O(n log^{-1/5}n)`) whose constants are not tracked.
   - **[paper audit]** The recurrence `s(n) ≤ s(n/2)+O(n log^{-1/5}n)` hides the constant; unrolling gives only an existential `O(n log^{-1/5}n)` bound, not an explicit `C`.

2. **Hidden branches.**
   - **[paper audit]** Theorem 1 splits the parameter `τ` into an interval `[143/126, 235/126]` and handles the complement by “direct calculation” without an explicit finite verification bound.
   - **[paper audit]** The final group insertion has cases `k ≤ n₀`, `n₀ < k < n/2-m`, `k ≥ n/2-m`, and a short last group; their constants are not made explicit.
   - **[paper audit]** The `a < 100` branch is dismissed with “sufficiently large constants” and no values.

3. **Asymptotic vs finite gap.**
   - **[deduction]** The proof gives an eventual bound, not a uniform finite inequality. The hidden constant in the `O` and the base case of the recurrence are unspecified, so no explicit `N` or `C` can be stated.
   - **[experiment]** For `n ≤ 22`, the gaps `δ = S(n)-⌈log₂(n!)⌉` are at most `1`, binding at `n = 12,13,...,19,22`; all satisfy `δ ≤ 0.108·n/(log₂ n)^{1/5}` (with slack huge for `C=1`). Thus small `n` cannot falsify a reasonable constant and does not illuminate the asymptotic regime.
   - **[deduction]** The `n=12` gap is a separate local combinatorial phenomenon, not an instance of Sergeev’s asymptotic excess (which is `≈ 9–10` at `n=12` and not in force until astronomically large `n`).

### What this does and does not imply
- **[deduction]** A weaker polynomial window such as `W(n)=n` is available from standard weaker bounds, but that is not an extraction of Sergeev’s sharper `n/(log n)^{1/5}` exponent or constant.
- **[deduction]** The blocker is an audit obstruction in the published proof, not a proof that no effective bound exists in principle. A full constant-tracking reanalysis, or a small-`s` construction, would be new work.
- **[model note]** No complexity-class consequence is claimed; this concerns soundness/effectivity of an upper bound, not hardness of computing `S(n)`.

### Delivery status
- No explicit `(N,C,W)` is provided.
- No repository, Lean, test, branch, or PR changes were made.
- No board post was added: the equivalent audit obstruction is already recorded on #301 as `effective-sergeev-bound-finite-extraction`; this conclusion is a direct corollary for the `W(n)` formulation, not a separate material claim.
