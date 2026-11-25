# antonina-ZVPCgVwCSffNcfWPwGsDei-denser

Session: ses_e0c0ead74ffeiKm5mFerY0WEeu
Workspace: /home/lubko/soring-fronts/optimal-play-poset-quotient-growth-alln
Created: 1795094041500; updated: 1795096686450

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 663 (msg_1f419a111001fbjjfkUgI7NeO5)

Posted the report to Antonina board #301 under author `SoringP1 frontier: optimal-play-poset-quotient-growth-alln`. No repository, Lean, test, or workflow changes were made; worktree remains clean at `6a96398`.

**Finding / obstruction.** The natural dynamic-programming route to deciding whether the number of isomorphism classes of posets on some height-`S(n)` optimal play is polynomial cannot work, because the objective is the cardinality of a *union* of child class-sets, not a sum. Exact enumeration for `n≤5` (all optimal policies, all optimal comparison choices) gives true extrema

- true min: 1, 2, 4, 6, 11
- true max: 1, 2, 5, 11, 19

which differ from both the earlier undercounted quotient counts and the greedy DP counts. Thus “some play” and “every play” genuinely differ, but neither an all-`n` polynomial upper bound nor an infinite superpolynomial family is established. The winning-frontier barrier also does not force these states onto one optimal play: those states are avoidable, and counting winning states does not bound single-strategy nodes. Honest limit: the question stays open; no NP-membership consequence for `SORT-BOUND-U` follows.
