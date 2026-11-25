# additive-approximation-frontier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Pp4uCI46L6Rqfhci12VuCd-hunterian

## exit_state

clearexit

## question

Can S(n) be computed uniformly in polynomial time with additive error O(1), or even O(log log n), rather than merely with the known o(n) error inherited from Sergeev's upper bound?

## basis

Published exact values S(1..22) have information excess 0 or 1; Sergeev gives S(n)=log2(n!)+o(n); docs/problem.md lists no approximation result and the ledger has no additive-approximation front.

## falsifier

Construct a uniform polynomial-time algorithm with additive error O(1), or prove an infinite-family lower bound showing that no uniform polynomial-time approximation can beat the Sergeev excess.

## implication

An O(1)-error algorithm would give the first polynomial-time near-exact evaluator without deciding exact S(n); a matching lower bound would show the Sergeev excess is algorithmically necessary and separate exact from approximate evaluation.

## finding_unverified

e recurrences, whose unary threshold language is **not in P** — yet `I` is still a poly‑time 1‑additive approximation of `G`. Proof: `G=I+b`, `b≤1`, with the `+1` bits placed on a positive‑density subset of the insertion‑slack set `T={n : I(n)−I(n−1)=⌈log₂n⌉−1}`, encoding a non‑P tally language; at `n∈T` the slack absorbs the bit, and merge uses `I(N) ≤ I(a)+I(c)+(N−2)` for `N≥9`. Consequently **bounded excess (even ≤1) plus matching all published values does not imply poly‑time exact computation, and an O(1)-approximation does not upgrade to a decision procedure** — so “separating exact from approximate” is realizable in this model, but it does *not* refute existence for `S`.

**4. Soundness vs completeness.** The lower side `S≥I` is sound and poly‑time; the upper side is a construction question (`FJ≈I+0.09n`, Sergeev `≈I+o(n)`). The missing near‑optimal **lower-bound certificate (completeness)**, not certificate soundness, is the real obstruction.

## Honest limits
- No O(1)- or O(log log n)-approximation was constructed; existence was **not** disproved.
- The positive direction is implied by the open bounded‑excess question; the negative direction needs unbounded (at least non-O(1)-approximable) excess.
- The literature audit is a snapshot through Stober–Weiß 2023; I found no newer exact/lower-bound tabulation.

This is a precise obstruction and a rigid no-go for upgrading approximation to exactness, not a solution of the front.
Checking durable state again before doing anything — I must not repeat the board post.
Board shows exactly one post (no duplicate), worktree clean. The ledger still records the front as `running` with no finding — that is the only apparent loose end. Let me inspect how the keeper records findings before touching shared state.
## State inspection (no action repeated)

- **Host:** `billy-dev`.
- **Git:** worktree clean, still at `6a96398`; no commits or file changes, no Lean touched.
- **Board #301:** the finding is present **exactly once** (`2026-11-08T08:51:28Z`, author `SoringP1 frontier: additive-approximation-frontier`). No second post exists, and I did not post again.
- **Durable ledger:** `additive-approximation-frontier` is still `status: running`, `exit_state: null`, `finding_unverified: null`.

That ledger state is **expected, not a lost update**: `research_frontier.py::reconcile()` deliberately skips any front whose `agent_id` is still in the active set, and only writes `exit_state` / `finding_unverified` / `status: investigated` after the agent reaches `clearexit`, `failed`, `stopped`, or `killed`. This session is still active, so the keeper has not yet reconciled it. I did **not** hand-edit the shared ledger, because that would race the keeper and could be overwritten.

## Unfinished work

None that is safe or non-duplicative:
- The research and single board report are complete.
- The ledger transition is automatic on agent exit; touching it manually is not justified and is the only “uncertain” state, so I am reporting it for review rather than guessing.

## Result already recorded

The finding posted to #301 stands: the O(1)-approximation front reduces the positive direction to the open bounded-excess question (output `I(n)=⌈log₂n!⌉`), no published lower bound through `n≤47` even reaches excess 2, and a sharpened diagonal shows bounded excess/agreement with all 22 exact values does not imply poly-time exact computation. Existence of an `O(1)`- or `O(log log n)`-approximation was **not** disproved.

## Other metadata

```json
{
  "finished_at": 1794127980.5751493,
  "started_at": 1794127388.2548149
}
```
