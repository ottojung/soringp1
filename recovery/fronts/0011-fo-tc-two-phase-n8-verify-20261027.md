# fo-tc-two-phase-n8-verify-20261027

## status

investigated

## origin

executive_manual_dispatch

## agent_id

bPD0O9Eik4BrW4mdNrouhE-vicinity

## exit_state

succeeded

## question

Independently verify the pushed n=8 two-phase FO(TC) exact sorting witness (branch research/JTsW4AnxTLzN18IBQibXea-fo-tc-twophase-E5ZrMYvzZMAF98F5N7FYSx at 1f27d8e) with a fresh checker, then advance one barrier cell: either the n=9 two-phase extension (bounded exhaustive/memoized search with recorded space estimate) or a computed next cell of the two-phase cost/phase-count barrier as n grows.

## basis

Antonina issue JTsW4AnxTLzN18IBQibXea-fervor with pushed artifacts e3aa9a3 (n=7) and 1f27d8e (n=8) on origin; 2026-10-25 progress checkpoints; ledger fo-tc-policy-interpreter investigated; no live owner since 2026-10-27 15:58 lease release.

## falsifier

Either a verified-inconsistent n=8 witness (checker mismatch with claimed exact height or executable-cost claim), or a completed n=9 extension witness, or a precise recorded search-space estimate plus the derived next barrier cell; any outcome is falsifiable and durably committed.

## implication

Decides whether FO(TC) two-phase strategy programs can encode exact near-optimal sorters at growing n (toward the Sigma_2^P representation goal) or where the two-phase decision-rule compression must break, sharpening the known barrier for the #47 certificate program.

## finding_unverified

n=9 done: worst exactly 20 = S(8)+⌈log₂9⌉, exceeding S(9)=19 — the predicted miss, independently confirmed with zero cross-disagreements. Now recording everything in the doc:
Let me strengthen the τ(n) item — it's actually provably linear today via an elementary block-count argument plus Sergeev:
Committing granular work:
Also updating the linked durable branch (fast-forward from 1f27d8e):
Deliverables complete. Now the handoff posts — checking the Antonina CLI:
Now posting the dated handoff on the fervor issue:
Handoff posted. Now the research finding post on the board (#301):
Both deliverables are complete and posted. Summary:

**Deliverable 1 — independent verification (commit `ab0d809`)**: Wrote `scripts/twophase_independent_check.py` from scratch with my own Ford–Johnson (Jacobsthal order derived from the closed form `(2^(t+1)+(-1)^t)/3`, insertion anchors re-found by linear scan) and a different program encoding (nodes keyed by immutable transcript-prefix tuples; the constant-`Ask`/no-runtime-search property *asserted*, not assumed). Cross-implementation mode compares per-order query counts and emitted outputs against the reviewed implementation over **every** hidden order: n=5–8 all pushed claims reproduce exactly, **zero discrepancies**, Jacobsthal orders agree for k<30. One bug found was in my own first draft (missing pairwise-comparison events), never touching the pushed branch.

**Deliverable 2 — barrier cell (commit `39e27a3`)**: 
- **Proved theorem**: optimal strict two-phase worst case is *exactly* `S(n−1)+⌈log₂ n⌉`, exact-budget iff `S(n)=S(n−1)+⌈log₂ n⌉` (phase-2 threshold queries realize any n-leaf gap tree of height `⌈log₂ n⌉`).
- **New executed n=9 witness**: two-phase worst exactly **20** over all 362,880 orders (cross-checked, single core, ~5 min, <1 GB, no GPU), missing S(9)=19 — execution-backed.
- **Classification over known n≤22**: exact at {4,6,7,8,11,12,13,14,15,16,22}, misses {5,9,10,17,18,19,20,21} — non-monotone (misses 17–21, hit at 22), so finite extrapolation can't settle all-n exactness.
- **Proved deduction**: cumulative miss mass `τ(n)=T(n)−S(n) ≥ n/4 − O(n/(log n)^{1/5}) = Ω(n)` (dyadic blocks + Sergeev).

Both commits signed, pushed to `research/fo-tc-two-phase-n8-verify-20261027` and fast-forwarded the durable `research/JTsW4AnxTLzN18IBQibXea-fo-tc-twophase-E5ZrMYvzZMAF98F5N7FYSx`. Full suite (181 tests + gated n=9 slow tests) passes; worktree clean. Terminal handoff posted on issue JTsW4AnxTLzN18IBQibXea-fervor; research finding posted on board #301. Remaining open: behavior of `d(n)` beyond n=22 (first undecided cell n=23, where S(23) itself is open).

## Other metadata

```json
{
  "finished_at": 1793127559.522857,
  "started_at": 1793125908.4387977
}
```
