# refinement-defect-failure-all-a-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

w30JaQMDEXQjXXRlsXOmFD-violet

## exit_state

clearexit

## question

For every a>=1, must there exist a finite poset B and a refinement B' obtained from B by adding comparabilities such that the antichain defect strictly drops, delta(A_a,B') < delta(A_a,B), given that this monotonicity failure is established only for a=1 and a=2 and the a=3,b=5 eight-element exact minimax computation did not finish?

## basis

Board #301 18:13Z defect-refinement-monotonicity-scope result (explicit a=2 fork F5 witness plus known a=1 witness) and 18:25Z Viche referee reproduction; exhaustive host scans at (2,3),(2,4),(3,3),(3,4),(4,3) found no failure.

## falsifier

Exhibit some a>=1 for which delta(A_a,.) is monotone nondecreasing under every refinement of every host B (the antichain is a minimum-defect host), or settle the a=3,b=5 case by exact minimax to extend the established failure set beyond a=2.

## implication

A full classification sharpens the ceiling/refinement mechanism for the antichain-root defect, but it is structural minimax information only: it gives no new bound on S(n), no SORT-BOUND-U class placement, and no transfer without an encoding-preserving reduction.

## finding_unverified

 antichain a minimum-defect host) is **not established** — it requires all b (infinite), not just b=5, and a=1,2,3 all fail. No evidence supports it.
- This is **structural minimax information only**: no new bound or algorithm for S(n), no SORT-BOUND-U class placement, no encoding-preserving reduction. General-poset results (chain extremality T1: the chain is the *maximum*-defect host) are sound bounds, not completeness for evaluating S(n); certificate soundness for a supplied strategy is not a polynomial-size certificate. **S(n) and SORT-BOUND-U remain OPEN**, and no theorem completion is claimed.

Per the publication gate and recovery caution, I made no repository or board changes; the durable scratch record is `/tmp/opencode/a3b5_finding.md`.
Both redundant cross-checks were killed by SIGKILL (memory exhaustion on the 13,440-extension fork union). The core result is unaffected — witness 1 (idx31) was fully verified with an explicit decision tree and three independent evaluators. Let me re-confirm state after the repeated recovery notices and correct the scratch record to reflect exactly which checks completed.
Working tree clean, no stray processes. Let me correct the scratch record so the verification status is honest (the two fork-union cross-checks died; only witness 1 has the full explicit-tree verification).
## Completion report — a=3, b=5 settled; core finding stands

**State after the repeated recovery notices:** working tree clean on `billy-dev` at `6a96398`; no stray processes; no board post, commit, or repository change made at any point this turn. The 18:13Z result post and 18:25Z referee reproduction that were already in place remain untouched. Nothing needed redoing.

**The unfinished computation is complete.** Refinement monotonicity of the antichain defect **fails at a=3**, extending the established failure set from {1,2} to **{1,2,3}**:

- Baseline: `delta(A_3,A_5) ≥ ⌈log2 8!⌉−3−7 = 6`.
- **Witness 1 (fully verified):** B = {2<0, 3<0, 3<1, 4<0, 4<1, 4<2}, e(B)=8, F(B)=4; `A_3⊔B` has e=2688, F=12 (info-tight) → `delta = 12−3−4 = 5 < 6`. Confirmed by three independent evaluators **and** an explicit height-12 decision tree verified leaf-by-leaf against all 2688 linear extensions. This witness alone establishes the result.
- **Witness 2 (corroborating, same fork F5 as a=2):** B = {4<0, 4<1}, e=40, F=6; union e=13440, F=14 (fastminimax) → `delta = 14−3−6 = 5 < 6`.

**Honest limit on verification:** the two *redundant* corroborations for witness 2 (Viche's `ref_minimax.can` and the explicit 13,440-leaf fork tree) were killed by SIGKILL from memory exhaustion. I am not counting them as completed evidence. Witness 2 therefore rests on the `fastminimax` value plus exact ceiling arithmetic; witness 1 is the rigorously checked basis of the finding.

**Mathematical limits (unchanged):** "fails for every a≥1" is **not** proved — a≥4 is uncomputed and 9+-element minimax is prohibitive (S(8) alone timed out); the other falsifier horn (monotonicity for some a, requiring *all* b) is not established and contradicted at a=1,2,3. This is structural minimax information only — no new bound for S(n), no SORT-BOUND-U class placement, no encoding-preserving reduction; certificate soundness ≠ completeness, and general-poset bounds (chain extremality) do not transfer. **S(n) and SORT-BOUND-U remain OPEN**, with no theorem-completion claim.

Durable scratch record: `/tmp/opencode/a3b5_finding.md` (corrected to reflect exact verification status).

## Other metadata

```json
{
  "finished_at": 1795288193.4998472,
  "started_at": 1795285749.9923007
}
```
