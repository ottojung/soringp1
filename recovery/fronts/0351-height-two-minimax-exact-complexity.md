# height-two-minimax-exact-complexity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

vOgvOvT2G1AdUAKos7ua0v-manners

## exit_state

clearexit

## question

Is the exact minimax comparison number F(P) computable in deterministic polynomial time for every height-two poset P, and in particular for the height-two posets obtained from the n-element antichain by one comparison?

## basis

Board #301's staircase height-two family and all-n cover-count reachability lemma; docs/problem.md's minimax recurrence; the ledger has threshold results for width two but no exact-complexity front for height two.

## falsifier

Give an explicit infinite family of height-two posets whose exact F values encode a #P-hard counting problem, or prove that no polynomial-time algorithm can compute F on that family.

## implication

A positive answer would yield a polynomial-time algorithm for S(n), because every first comparison from the antichain produces a height-two state; a negative answer is a barrier to first-child exact recurrences but does not by itself transfer to S(n).

## finding_unverified

No extension threshold `e(P)≤T(k)` can *characterize* `F≤k` on height two: at `k=6`, `T(6)≥60` makes `Q` unsound, while `T(6)<60` fails to certify `P`. A threshold may remain a sound sufficient condition; it cannot be complete. This is the soundness/completeness gap concretely.

**4. Literature and terminology correction.**

- `#H2LE` is `#P`-complete, even for incidence posets of graphs (Dittmer–Pak, arXiv:1802.06312v1, Theorems 1.1–1.2). But by (3), counting hardness does **not** transfer to `F` through `e`, since `e(P)=e(Q)` with `F(P)≠F(Q)`.
- The Fibonacci “staircase” `W_n` cited with the width-two threshold is **width two, not height two**: `i` above `j` iff `j≤i−2` is a disjoint union of the even/odd chains, with height `≈n/2`. The height-two staircase from `docs/research-time-exponent.md` has `e=1,5,57,1145` and `F=0,3,7,11` for `m=1..4`, not Fibonacci. Width-two GPC/threshold evidence is therefore not height-two evidence.

## Failed approaches and honest limits

- Attempted a `#H2LE → F` reduction via extension thresholds; blocked by the `n=6` collision.
- Attempted to extend the collision to an infinite family by disjoint union with chains; exact minimax at `n=8` exceeded the time budget, so no all-`n` claim.
- No polynomial algorithm for all height-two `F`, no proof that none exists, and no new claim about `S(n)` beyond the identities above.
- No Lean or repository changes; the worktree remains clean at `6a96398`.

**Next decisive target:** a height-two family whose exact `F` (or decision `F≤k`) encodes a #P-/PP-hard parameter *not* reducible to `e`, or a two-way reduction showing all-height-two `F` is equivalent to `S(n)`.
## Recovery inspection result

I inspected the conversation, Git/worktree, board, and durable ledger before acting.

**Effects that actually happened (previous turn):**
- Exactly **one** board #301 comment was posted, at `2026-11-08T09:02:31Z`, author `SoringP1 frontier: height-two-minimax-exact-complexity`. I re-read it from the board and confirmed its stored body matches the prepared text (only a trailing newline was stripped).
- **No repository changes:** worktree clean at `6a96398`; no new commit, branch, stash, or Lean file.
- Verification artifacts remain outside the repo in `/tmp/opencode/` (`verify_pair.py`, `height-two-post.md`).

**Unfinished / uncertain items:**
- The durable ledger still records the front as `status: running` under agent `vOgvOvT2G1AdUAKos7ua0v-manners`, with no recorded finding or exit state. That is keeper/ledger reconciliation state, not a missing research result. I did not hand-edit operational state, to avoid a duplicate or conflicting record.
- No second height-two post exists, so I did **not** repost or repeat any external action.

**Research outcome already delivered:**
- `S(n) = 1 + F(P_n)` for the one-edge height-two family `P_n`, making that subfamily exactly equivalent to the `SORT-BOUND-U` target.
- `F(K_{m,m}) = 2S(m)`.
- Concrete height-two collision: at `n=6`, two posets both with `e=60` but `F=6` and `F=7`, blocking any extension-count threshold as an exact evaluator.
- Correction that the Fibonacci staircase `W_n` is width two, not height two.
- No poly-time algorithm, no #P-hardness proof, no complexity-class separation claimed.

No further side effects were performed. The only remaining action is operational recording of the completed front by the keeper; that record is currently still `running` and should be reconciled there rather than duplicated manually.

## Other metadata

```json
{
  "finished_at": 1794128638.4951715,
  "started_at": 1794127387.4333582
}
```
