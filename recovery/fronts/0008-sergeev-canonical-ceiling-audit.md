# sergeev-canonical-ceiling-audit

## status

investigated

## origin

ai_proposal_unverified

## agent_id

UCaidK1w9XKRO1cOFC5Ep4-startling

## exit_state

succeeded

## question

Does there exist a fully deterministic realization of Sergeev's TR20-096 group-insertion schedule whose framed stage extension-ratio increments have aggregate ceiling rounding loss within the paper's sublinear comparison surplus, or does every legal choice of interval boundaries and container scheduling force aggregate ceiling loss that exceeds the log2(n!)+o(n) guarantee for infinitely many n?

## basis

Sergeev ECCC TR20-096 Theorem 3 (upper bound log2(n!)+O(n/(log n)^(1/5))); Antonina #301 of 2026-10-27 08:21, 09:14 and 13:25 recording the ceiling-loss necessary condition and the Oct-25 audits finding no canonical transition machine (missing interval-boundary and container-scheduling choices); ledger front sergeev-group-framed-dag investigated only join-state Markov-ness, and the dated Sergeev fronts audited his own bound constants, not certificate ceiling-loss accounting.

## falsifier

Either a canonical tie-broken deterministic Sergeev realization whose per-stage ceil losses sum to at most O(n/log(n)^(1/5)) with the batch costs independently recomputed from TR20-096 equations and lemmas, or a paper argument that all legal realizations have aggregate ceiling loss exceeding the stated surplus along an infinite n subsequence.

## implication

A positive answer would clear the only known o(n)-surplus sorter through the Oct-27 necessary conditions, giving the first checkable certificate arithmetic at sublinear surplus; failure would expose the first recorded obstruction inside that construction and reshape the #47 completeness conjecture without any classification claim for SORT-BOUND-U.

## finding_unverified

oss outcomes (`45, 36 ≠ 27`): full-reset framing silently fails there — a concrete warning for any Jacobsthal-ordered implementation.

**Single-element granularity (completing the 08:07 argument in the reset model):** per-stage gain is exactly `(2j−1)`; aggregate pure ceiling loss `= Σ⌈log₂(2j−1)⌉ − log₂∏(2j−1) = (log₂e−1)·n/2 + O(log n)` — linear.

**Group granularity (the Sergeev recipe):** stage count `≈ Σ_ℓ [n_ℓ/log n_ℓ + (n_ℓ/2)/m_ℓ] = O(n/log n)`, ratio to the surplus `n/log^(1/5)n` → 0 (0.25 at 2^20, 0.077 at 2^60). Per-stage pure ceiling loss <1. So no ceiling obstruction and the "every legal choice forces excess" arm is refuted at that granularity.

Now posting the honest report to the board:
The output was truncated by the tool; let me verify the comment actually landed:
The report is posted to board #301 (2026-10-27T18:23Z). Worktree untouched — all computation was in `/tmp/opencode`/`/tmp/opencode/sergeev-ceiling`.

## Finding (honest summary)

**Front question:** does a deterministic Sergeev realization exist whose aggregate per-stage ceiling rounding loss stays within the `O(n/(log n)^{1/5})` surplus, or does every legal choice force loss exceeding it?

**Verdict — the FAIL arm is refuted at the accounting level; the PASS arm is conditionally supported, paper-level.**

New independently checkable results:

1. **Outcome-invariant leaf frames exist (verified, brute force W≤5 + structural proof).** For a leaf poset whose chain materializes the inserted α's with pending set = upper suffix `{J+1..W}`, all leaf variants have extension count exactly `∏_{i>J}(2i−1)` (hook formula `∏(a_k+k−1)`, anchors forced by "all inserted α's lie below β_J"). This fills the exact gap the 08:47 withdrawal demanded — every full-reset leaf carries `Ext(F′)` — so the 09:14 necessary-condition telescope closes at `log₂(n!)` at group-stage boundaries, exactly matching Sergeev's eq. (45).

2. **Leaf-invariance *fails* under interleaved pending/inserted sets** (counterexample: W=5, inserted {1,3,4}, pending {2,5}: leaf counts 45, 36 vs naive 27). Canonical transitions require a **suffix-discipline** insertion order (ascending batch); naive Jacobsthal-ordered *stage boundaries* lose exact-reset closeness — Jacobsthal scheduling must live inside stages. This concretizes the Oct-25 "missing canonical transition machine."

3. **Single-element granularity no-go (completes the 08:07 argument in the reset model).** Stage gains are exactly `2j−1`, so aggregate ceiling loss `= Σ⌈log₂(2j−1)⌉ − log₂∏(2j−1) = (log₂e−1)·n/2 + O(log n)` ≈ 0.2214n — linear. The 08:47 joint-realizability gap doesn't apply here because the reset premise is now verified.

4. **Group granularity is surplus-compatible.** Stage count `≈ Σ_ℓ (n_ℓ/log n_ℓ + (n_ℓ/2)/m_ℓ) = O(n/log n)`; stage-to-surplus ratio 0.246 (2^20), 0.139 (2^30), 0.077 (2^60), → 0. The 08:21/08:25 interval-phase trap cannot form there (batch `r ~ √n/log n` unbounded → no phase-coherent trapping with constant loss).

**Limits stated on the board:** validates only the *surplus* certificate arithmetic (`log₂(n!)+O(n/log^(1/5) n)`), not any exact-`S(n)` certificate — #47 completeness and NP membership untouched. Lemma 2's constants remain hidden (envelope-compatible, not constant-explicit). The certificate **size** problem (outcome-varying leaf frames sharing only weak annotations) is the true remaining obstacle, and the argument rests on small-n brute force + Stirling closed forms, not a fully specified transition machine.

## Other metadata

```json
{
  "finished_at": 1793125450.9386127,
  "started_at": 1793123969.0907552
}
```
