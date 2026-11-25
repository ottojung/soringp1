# cover-destruction-induction-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

5DcbL6YJBe6EH0JQCsqsm5-humane

## exit_state

clearexit

## question

Is the cover-destruction induction route to the (U) inequality blocked by the failure of the exact D-balanced condition at n=6,7, or does a corrected potential restore the induction for all finite posets?

## basis

Newest board #301 02:20Z upper-inequality-structural post; independent exhaustive computation over all non-total unlabeled posets of orders 5-8 finds height-two violations at n=6,7.

## falsifier

Exhibit a corrected potential D'(P) and constant C' with an induction proving F(P) <= log2 e(P) + C' D'(P) for all finite posets, or prove that every cover-destruction-based induction fails at some finite poset.

## implication

A corrected potential would revive the (U) route to a general excess inequality; a barrier would close it. Neither directly changes S(n) bounds, since (U) is weaker than Sergeev at the antichain.

## finding_unverified

every** `C′ ≥ 0`. No constant rescues the cover-destruction induction with potential `D` at this poset.

**Corrected potential.** `D′(P) = ip(P)` (number of incomparable pairs) with `C′ = 1` restores the induction for all finite posets:

`F(P) ≤ log₂ e(P) + ip(P)`.

Adding a relation makes its pair comparable and creates no new incomparable pair, so `ipᵢ ≤ ip − 1` (verified for all 250,665 pairs up to n=8). Then `F ≤ 1 + max(log₂ eᵢ + ipᵢ) ≤ 1 + log₂ M + (ip−1) = log₂ e + log₂ p + ip ≤ log₂ e + ip`, since `p = M/e ≤ 1`. This satisfies the falsifier's first disjunct.

## Why this does not revive (U)

`(U)` is `alpha ≤ C(covers+psi)`. At the antichain, `covers+psi = 2n` but `ip = C(n,2)`, so the corrected potential gives `alpha ≤ n(n−1)/2`, vastly weaker than `(U)`'s `0.273n`. Against Fredman's known `F ≤ log₂ e + 2n` (recorded in `docs/research-hardness-boundaries.md`), the corrected bound is stronger only when `ip < 2n`. So the route to `(U)` is **not** restored; only a weak general excess inequality is obtained.

## Honest limits

- The corrected-potential theorem is a short elementary induction and the inequality is weak; it may be folklore and does not imply `(U)`.
- The exact-condition failures are exact computations up to n=8, not an all-n proof.
- The n=5 obstruction kills the specific potential `D = covers+psi`, not every potential.
- This is a structural minimax statement about general finite posets. It does not change `S(n)` or `SORT-BOUND-U` bounds, and it is not a certificate soundness/completeness result.

**External effects:** one board comment posted to #301 at `2026-11-10T04:39:58Z` under `SoringP1 frontier: cover-destruction-induction-barrier` (verified unique). Worktree clean at `6a96398`; no repo, Lean, or ledger changes.
**Recovery inspection (no actions taken, no side effects repeated)**

- **Repo state:** `/home/lubko/soring-fronts/cover-destruction-induction-barrier` on `billy-dev`, clean working tree at `6a96398` (`billy-dev...origin/billy-dev`), no local diff and no untracked files.
- **Durable scratch/artifacts present:** `/tmp/opencode/cdcheck/` contains `post.md`, `report.md`, `post_result.json`, and analysis scripts (`exact.py`, `gc.py`, `cinterval2.py`, `h2fails.py`, `posets.py`, etc.). `post.md` matches the completed `cover-destruction-induction-barrier` finding (exact D-balanced condition fails from n=3; `D=covers+psi` blocked at n=5 for all `C'` by `P=(16,16,17,23,0)`; corrected potential `D'=ip, C'=1` gives `F(P) <= log2 e(P)+ip(P)` but does not revive `(U)`).
- **External side effects (based on durable records):** The board post to #301 for `cover-destruction-induction-barrier` appears to have already been recorded (summary/checkpoint states `2026-11-10T04:39:58Z`, verified unique; `post.md`/`post_result.json` exist locally). I did **not** re-post or verify against the live board API from this environment, so if absolute certainty is required that should be confirmed on Antonina/board side—but I am not duplicating the post.
- **Commits/PRs/purchases/Lean/repo changes:** none detected; nothing to commit or publish.

**Status:** front appears complete and reported; **no unfinished work identified** in this checkout from available records. Per the checkpoint, the only natural continuation would be a new investigation (e.g. whether any stronger corrected potential can recover `(U)`), but that would be a separate front/question, not continuation of an interrupted side effect. I have not started any new work.

## Other metadata

```json
{
  "finished_at": 1794285820.7608771,
  "started_at": 1794281702.4466312
}
```
