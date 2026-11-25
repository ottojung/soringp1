# antonina-Pp4uCI46L6Rqfhci12VuCd-hunterian

Session: ses_e45ac9e30ffe34ZWnNDyxgazLZ
Workspace: /home/lubko/soring-fronts/additive-approximation-frontier
Created: 1794127389304; updated: 1794127957379

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 27 (msg_1ba53817e001bCBMo4vfJmgcQU)

I'll start by inspecting the current state: git status, recent commits, and durable task records, to determine what already happened before any external side effects.

## Output 42 (msg_1ba538c9f001Zff7kE3GONoGgS)

Clean worktree, on billy-dev. Now let me examine the docs and the research board (#301) to find what was already attempted.

## Output 57 (msg_1ba5396b1001fixsinEB5MfiYA)

Now let me read the board digest and the frontier ledger to see what's already been done on this front.

## Output 85 (msg_1ba53b244001s71L33UFLtf4An)

The ledger shows this front (`additive-approximation-frontier`) was launched but has no finding yet, and no board post exists (search for "additive" only returned unrelated posts). Git is clean. So no external effect has occurred beyond the durable claim; only the research remains. Let me read the key repo notes before committing to a claim.

## Output 113 (msg_1ba54a82200143MPqP5KsvvXwD)

Let me compute the information bounds against published exact values and lower bounds — this can discriminate whether the "excess 0 or 1" pattern actually persists.

## Output 146 (msg_1ba5603b2001S19qZUBQZgwWAx)

The excess `S(n) − ⌈log₂ n!⌉` is known to be 0 or 1 only for n≤22; whether it is bounded is explicitly open in the literature. Let me check for any newer primary result before fixing the claim.

## Output 201 (msg_1ba580fa1001Hj5R7Trd78dO9A)

The paper's table gives published intervals for n up to ~47. Let me extract it precisely — it may show how weak the known lower bounds are for the excess.

## Output 221 (msg_1ba58453f001K4rOKZ2DwirHWr)

The Stober–Weiß table is decisive evidence about the *lower-bound* side. Let me verify all the numerical claims (information bound, Ford–Johnson formula, published lower bounds) with a script before drawing conclusions.

## Output 232 (msg_1ba595dc80015amo0TbmSFo8Sc)

Let me check for any post-2023 improvement of sorting-number lower bounds before claiming the +1 frontier.

## Output 243 (msg_1ba59dc7b001LCGovV96yghqQm)

The numerical audit confirms the lower-bound frontier is stuck at excess +1 for all published n≤47. Now let me check how to post to board #301 correctly (and confirm no existing post to avoid duplication).

## Output 289 (msg_1ba5a4d94001jxv6MK1D50fMoL)

All claims are now verified. I'll post one concise finding to board #301 (after confirming no prior additive-approximation post exists), then leave the worktree clean.

## Output 316 (msg_1ba5b24bd001qOKedgp53gmAWW)

Post succeeded exactly once. Let me confirm the worktree remains clean and no other side effects occurred.

## Output 327 (msg_1ba5b2e1e0014irqWcS45tpkA7)

## Recovery check (done before any action)
- Host is `billy-dev`; worktree clean, no new commit, branch `billy-dev`.
- The durable ledger had `additive-approximation-frontier` in state `running` with no finding.
- Board search for `additive`, `additive-approximation`, and `bounded excess` found no prior post from this front. So the previous turn had produced no external effect beyond the durable claim.
- I completed only the research and posted **once** to #301; no repo/Lean changes. Worktree remains clean at `6a96398`.

## Mathematical finding

The front asks whether exact `S(n)` admits a uniform poly‑time approximation with additive error `O(1)` (or `O(log log n)`) instead of the known `o(n)` Sergeev excess. I attacked the claim and its natural strengthening; the honest outcome is a **reduction plus a barrier**, not a disproof of existence.

**1. The positive side is arithmetic, not algorithmic.** With `I(n)=⌈log₂ n!⌉` (poly‑time computable from `1^n`), any all‑`n` bound `S(n) ≤ I(n)+c` immediately yields a poly‑time `c`-additive approximation by outputting `I(n)`. So the O(1) goal is *implied by the open bounded‑excess conjecture* and would not require a new minimax evaluator or deciding exact `S(n)`.

**2. The negative side has no published foothold.** From Stober–Weiß 2023 (Table 7), exact values give `S(n)−I(n) ∈ {0,1}` for `n≤22`; for `23≤n≤47` **every published lower bound satisfies `L(n) ≤ I(n)+1`** (max `+1`, only at `n=28`). I verified the standard Ford–Johnson count `Σ⌈log₂(3k/4)⌉` reproduces all tabulated values; `FJ−I ≤ 3` on that range, then grows roughly `0.09n`. **No `n` has a proven excess of 2 or more.** So the falsifier “prove an infinite-family lower bound beating the Sergeev excess” is far beyond current methods — it would first need the first-ever excess‑≥2 instance.

**3. A sharpened diagonal barrier (new strengthening of Thm 6.6).** There is a nondecreasing integer `G` with `I(n) ≤ G(n) ≤ I(n)+1`, `G(n)=S(n)` for all `n≤22`, satisfying the exact insertion and merge recurrences, whose unary threshold language is **not in P** — yet `I` is still a poly‑time 1‑additive approximation of `G`. Proof: `G=I+b`, `b≤1`, with the `+1` bits placed on a positive‑density subset of the insertion‑slack set `T={n : I(n)−I(n−1)=⌈log₂n⌉−1}`, encoding a non‑P tally language; at `n∈T` the slack absorbs the bit, and merge uses `I(N) ≤ I(a)+I(c)+(N−2)` for `N≥9`. Consequently **bounded excess (even ≤1) plus matching all published values does not imply poly‑time exact computation, and an O(1)-approximation does not upgrade to a decision procedure** — so “separating exact from approximate” is realizable in this model, but it does *not* refute existence for `S`.

**4. Soundness vs completeness.** The lower side `S≥I` is sound and poly‑time; the upper side is a construction question (`FJ≈I+0.09n`, Sergeev `≈I+o(n)`). The missing near‑optimal **lower-bound certificate (completeness)**, not certificate soundness, is the real obstruction.

## Honest limits
- No O(1)- or O(log log n)-approximation was constructed; existence was **not** disproved.
- The positive direction is implied by the open bounded‑excess question; the negative direction needs unbounded (at least non-O(1)-approximable) excess.
- The literature audit is a snapshot through Stober–Weiß 2023; I found no newer exact/lower-bound tabulation.

This is a precise obstruction and a rigid no-go for upgrading approximation to exactness, not a solution of the front.

## Output 346 (msg_1ba5b9dc9001aQvaqDMtVcOn0N)

Checking durable state again before doing anything — I must not repeat the board post.

## Output 365 (msg_1ba5bb698001zBcAQD0ieKQ2tJ)

Board shows exactly one post (no duplicate), worktree clean. The ledger still records the front as `running` with no finding — that is the only apparent loose end. Let me inspect how the keeper records findings before touching shared state.

## Output 389 (msg_1ba5be79a001VCbRhFjhtdyWw1)

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
