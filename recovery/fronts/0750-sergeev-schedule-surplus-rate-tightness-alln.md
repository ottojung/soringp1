# sergeev-schedule-surplus-rate-tightness-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

kvBGZM1xKXhVYSok42Bqtv-seven

## exit_state

clearexit

## question

Fix any legal parameter choice in Sergeev's TR20-096 pair-sort plus group-insertion schedule and let C_A(n) be its worst-case comparison count. Is C_A(n) - log2(n!) >= c n / (log n)^{1/5} with an explicit c > 0 for all large n, or can a refinement of the same architecture drive the schedule's surplus to o(n / (log n)^{1/5})?

## basis

Newest board #301 sergeev-framed-dag-exact-budget-alln FINDING 3 states a surplus lower bound for a fixed schedule is absent from TR20-096 and needed for its falsifier; Theorem 3 (pp.29-30) supplies only an unquantified O(n log^{-1/5} n) upper bound. I independently recomputed Lemma 4's lambda(s) = 20*2^{-s/2} + 64*2^{-s}, first below 1 at s = 10; no all-n schedule rate is claimed.

## falsifier

Exhibit a legal fixed schedule whose surplus is o(n/(log n)^{1/5}), refuting the rate lower bound; or derive explicit c > 0 and n0 certifying the Omega(n/(log n)^{1/5}) schedule bound for every n >= n0, refuting the refinement reading. Neither branch yields a claim about the optimum S(n).

## implication

An explicit schedule-level rate lower bound is the missing ingredient named in the newest #301 sergeev-framed-dag-exact-budget-alln finding: paired with any effective upper bound on S(n)'s surplus it would force that architecture's height above S(n) infinitely often; the opposite answer would weaken the barrier and improve explicit upper bounds, without placing SORT-BOUND-U in a class.

## finding_unverified

`2^{+9.4}`; at `a = 2^1000`, `−220.8` vs `2^{+182.7}`.
- The convergence condition forces **`γ < 1/6`** (bisection: `γ_max ≈ 0.130 → 0.1615` as `log₂ a` goes 100 → 1000). So this framework supports only `S(n) ≤ log₂(n!) + O(n/log^{1/6−o(1)} n)` — a *weaker* bound than 1/5. The `o(n)` headline survives (e.g. γ = 1/10 works); the specific exponent does not follow.

**Both horns fail:** (A) the paper gives only an upper bound, with no mechanism to lower-bound a fixed schedule's intrinsic loss (entropy identity bounds surplus only from above); (B) parameter tuning caps the loss exponent below 1/6 < 1/5, so it cannot produce `o(n/log^{1/5} n)`. The disjunction's premise — that `n/log^{1/5} n` is the architecture's surplus scale — is unsupported by the source.

## Honest limits
I did **not** show Theorem 3 is false, produce any new bound on `S(n)`, or refute the general `o(n)` result. Finding 1 is an algebraic discrepancy in one derivation step (verified by explicit substitution plus a log-space script); it needs independent confirmation before being treated as an erratum. No claim about `SORT-BOUND-U`'s class placement, and general-poset results / certificate soundness were kept distinct from completeness throughout.
Understood. I will not repeat the previous turn's actions. Let me first audit what actually happened — conversation record, git state, the board, and durable task records.
Git and board look consistent. Let me verify the durable ledger record and that the posted body matches my local draft exactly (intact, single post).
Audit complete. No new external actions were taken in this turn.

## What actually happened (verified)

| Effect | Status | Evidence |
|---|---|---|
| Board #301 post | **Landed exactly once** | `2026-11-24T08:19:06.825Z`, author `SoringP1 frontier: sergeev-schedule-surplus-rate-tightness-alln`; digest shows 1 unique match; posted body matches my local draft exactly (sha256 `f7c2e56f0143d99c`) |
| Repository / Lean / tests / CI | **No changes** | `billy-dev` clean, HEAD still `6a96398d…`, no stash, no worktrees |
| Durable ledger | **Untouched by me** | Front still `status: running`, `agent_id: kvBGZM1xKXhVYSok42Bqtv-seven`, `finding_len: null`, `exit_state: null` — keeper-owned fields |
| Scratch | Local only | `/tmp/opencode/sched-rate/` (paper extracts, `verify_exponent.py`, `board_post.md`, `post_result.json`) |
| Web search | No effect | Cancelled, returned no results |

## Conclusion

The previous turn **completed fully**: the research finding was delivered, the single required board report landed intact, and there were no commits, ledger edits, or other external writes. Nothing is uncertain, and there is **no unfinished process work** to continue — I will not re-post, re-commit, or modify the ledger.

The only outstanding item is the keeper's automatic ledger reconciliation on agent exit (currently `running` with no recorded finding), which is deliberately left to `research_frontier.py` rather than hand-edited, consistent with the established practice noted in prior front reports.

The mathematical outcome stands as reported: the front remains **OPEN** (both falsifier disjuncts unproved), with the substantive finding being an independently checkable exponent misestimate in Sergeev TR20-096 Theorem 2 — the error term's true exponent is `Θ(a^{1−6γ}/log a)`, not the paper's `Θ(a^{1−4γ}/(log a)²)`, so γ = 1/5 does not follow from Lemma 2 and the framework caps γ < 1/6. No claim about `S(n)` or class placement.

## Other metadata

```json
{
  "finished_at": 1795508446.1048417,
  "started_at": 1795507675.440999
}
```
