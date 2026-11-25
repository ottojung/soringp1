# winning-frontier-peak-two-thirds-s-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

skrYTuDxcloSGx1QXzJALy-economic

## exit_state

clearexit

## question

For all n, if W_t(n) counts nonisomorphic posets reachable from the n-antichain in exactly t comparisons with F(P) <= S(n)-t, is the maximum of W_t(n) over t attained at t = floor(2*S(n)/3)?

## basis

Board #301 winning-frontier-peak refutation W values for n<=5; docs/research-winning-frontier-barrier.md; meet-in-the-middle frontier analysis.

## falsifier

Compute W_t(n) for n=6 or larger and find a peak t differing from floor(2*S(n)/3); the n<=5 data have peaks at t=2,3,4 for S=3,5,7.

## implication

The peak location determines the largest meet-in-the-middle frontier size for exact evaluators; a predictable peak would guide bidirectional search, while a mismatch exposes new growth in the winning frontier.

## finding_unverified

M came from holding ~6M tuple-keyed states plus all layers at once. Before deciding on n=7, let me do a robustness check on the n=6 result: compare the "exact-depth" reachability semantics (reference, no dedup) against "minimum-depth" semantics, to confirm the peak location is not an artifact of the interpretation.
Important robustness finding: under **minimum-depth** reachability semantics, n=6 peaks at t=5 (≠ floor(2S/3)=6), while the reference **exact-depth** semantics peaks at t=6. The two agree for n≤5 but diverge at n=6. Let me verify no board post was already made for this front (to avoid duplicating an external side effect during recovery).
No existing board post for this front — no external side effects occurred. Let me check the board post command syntax (without posting yet), then decide.
I have a substantive, reproducible finding. The research contract mandates reporting to board #301, and I've verified no post exists for this front, so posting once is safe (no duplication). Let me compose and post a concise update.
The board post succeeded (visible once at `id sha256:sRmq...`, no stderr). Let me confirm it appears exactly once and the worktree is still clean.
Done. Here is the honest outcome.

## What I did (billy-dev, no repo changes)

Studied `AGENTS.md`, `docs/problem.md`, board #301, and the winning-frontier barrier note. I built an independent W_t enumerator (`/tmp/opencode/w6.py`) that reproduces the established n≤5 data **exactly** (`W=[1,1,3,1]`, `[1,1,4,6,4,1,0]`, `[1,1,2,6,17,11,5,1,0,0,0]`), then computed n=6, and stress-tested the definition. I caught and fixed a canon bug (it initially missed relations like `2<0` stored in `succ[2]`'s bit 0). One board post to #301 (verified single), clean worktree, no commits/Lean.

## Mathematical finding

**The claim is NOT falsified at n=6 under the intended semantics.** With S(6)=10, floor(2·10/3)=6:

- Exact-depth semantics (the `w_t_check.py` reading that produced the motivating peaks 2,3,4):
  W₆ = `[1,1,2,7,27,76,84,49,19,6,1,0,…]`, max **84 uniquely at t=6**. So the peak sequence extends 2,3,4 → **2,3,4,6**, matching floor(2S/3) at every tested n. This is the first new confirmation beyond the supplied data.

## Concrete obstruction / sensitivity

**The all-n claim is not robust to the meaning of "reachable in exactly t comparisons."** Under the alternative minimum-depth reading (each poset counted only at its first reachable depth), n=6 peaks at **t=5** (W=`[1,1,2,7,26,66,42,11,1,0]`, max 66), which would **falsify** floor(2S/3)=6. The n≤5 data hold under *both* readings, so they cannot disambiguate it — the claim's truth at the first new test case hinges on this definitional choice.

**n=7 is computationally blocked here:** 6,129,859 labelled posets; the naive full-minimax enumeration was OOM-killed by SIGKILL; even with 11 GB the scaled estimate is ~2–3 h. No falsification obtained at n≥7.

## Honest limits

- No structural reason for exactly 2/3 was found; floor(2S/3) merely coincides with ≈0.6·S at small S. The barrier note exhibits huge frontiers near t≈0.37·S for large n, hinting the true peak may drift — but I have no method to locate argmax W_t for large n, so this is speculation, not a result.
- This is an experiment/obstruction, **not a theorem and not a counterexample** to the claim as posed. Under the reference semantics the claim survives n=3–6; it remains unproven. The next decisive obstacle is computing argmax W_t for n≥7 without full poset enumeration.

## Other metadata

```json
{
  "finished_at": 1795320326.9163666,
  "started_at": 1795318828.0809815
}
```
