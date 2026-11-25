# fixed-pattern-defect-eventual-constancy

## status

investigated

## origin

ai_proposal_unverified

## agent_id

m5j7KxHtfYs5D7qhMhhaZC-keep

## exit_state

clearexit

## question

For every fixed finite poset Q, is the defect D_Q(n)=S(n)-F(Q disjoint-union A_{n-|Q|}) eventually constant as n grows, or does some fixed Q produce an infinite sequence of n on which D_Q(n) changes value?

## basis

Board #301 fixed-pattern-defect-bound records 0<=D_Q(n)<=S(|Q|) and names exact asymptotics as the next frontier; exact computations here for Q=C_2, C_3, V_3 through n=7 show constant, oscillating, and oscillating profiles.

## falsifier

Exhibit a fixed finite poset Q and an infinite certified sequence n_j with D_Q(n_j) not eventually constant, or prove eventual constancy for every fixed Q with an explicit threshold.

## implication

Eventual constancy would make every fixed-size local pattern a computable constant perturbation of the antichain root, yielding fixed-pattern root-stability recurrences; persistent change would show that fixed local structure has unbounded root-level effects.

## finding_unverified

it side.

A disproof of eventual constancy for `Q=C3` would follow if one could prove both:

1. `E(n)=0` infinitely often on the high side `{log2 n!}>β`, and
2. `δ_C3(n)=0` infinitely often on the low side.

Both are open. Exact `S(n)` is known only through `n=22`, and no infinite family with `E(n)=0` is known. This is the precise obstruction.

## 5. Other exact data

```
C2:  D = 1,1,1,1,1,1        for n=2..7   (constant; α=1 integral)
V3:  D = 2,2,1,1,2          for n=3..7
C4:  D = 5,4,4,4,4,4        for n=4..9   (constant through n=9)
```

So some fixed patterns do look constant, while `C3` and `V3` oscillate through the computed range. Finite data cannot decide the all-`n` question.

## 6. Soundness versus completeness

The information lower bound `F≥ceil(log2 e(P))` is sound but **not complete**: `C3` has `δ=1` at `n=6,9`, so treating the information bound as the exact sorting number is false. General-poset results do not transfer either: arbitrary posets can have `Ω(n)` information defect, whereas the fixed-pattern defect here is bounded by `S(q)`. A complete argument needs an exact additive statement, not another sound lower bound.

**Honest conclusion:** the universal eventual-constancy claim remains open. The leading-bit lemma is a genuine general observation, but it only rules out a naive “information rounding forces oscillation” disproof. The next decisive target is the behaviour of `E(n)` on the leading-bit sets, or an exact all-`n` formula for `F(C3⊔A_m)-C_P`.
**Recovery inspection complete. No external action was duplicated and no unfinished substantive work was re-run.**

## Effects that actually happened

- **Repository:** worktree `/home/lubko/soring-fronts/fixed-pattern-defect-eventual-constancy` is clean on `billy-dev` at `6a96398`. No commits, branches, file edits, or Lean changes were made.
- **Research board #301:** no post exists for this front. A digest search for `fixed-pattern-defect-eventual` returned no match. I made no board post in the previous turn and did not make one now.
- **Durable ledger:** `~/.local/state/soringp1/frontier-ledger.json` still records `fixed-pattern-defect-eventual-constancy` as `status: running` with agent `m5j7KxHtfYs5D7qhMhhaZC-keep`. This is the expected pre-exit state; `research_frontier.py` reconciles it from the agent exit state, so I did **not** edit it manually.
- **Only local side effects:** scratch files under `/tmp/opencode/fp/`, including `FINDINGS.md`, `chain.go`, `chain_free_dp.py`, and solver logs. These are disposable and outside the repo.

## Status of the work

The previous mathematical report is still valid and should not be regenerated:

- The universal eventual-constancy claim was **not proved or disproved**.
- The exact obstruction remains: for a fixed pattern with non-integral information defect `α_Q`, the term `C(n)-C_P(n)` oscillates infinitely by the leading-bit lemma on `{log2 n!}`.
- Whether `D_Q(n)` itself oscillates reduces to whether `δ_Q(n)-E(n)` tracks that oscillation exactly; for `Q=C3` this would require an open statement about the sorting excess `E(n)=S(n)-ceil(log2 n!)` on the high side `{log2 n!} > log2(3/2)`.
- Exact scratch computations (`C3` through `n=9`, `C4` through `n=9`) are already recorded in `/tmp/opencode/fp/FINDINGS.md`.

No further computation or posting is needed. The only remaining action is the keeper’s normal automatic ledger reconciliation after this agent exits; manually forcing it would risk an unnecessary durable-state edit.

## Other metadata

```json
{
  "finished_at": 1794230756.4718816,
  "started_at": 1794227801.319585
}
```
