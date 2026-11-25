# antonina-m5j7KxHtfYs5D7qhMhhaZC-keep

Session: ses_e3fb07087ffed89GuO1tGQJBGE
Workspace: /home/lubko/soring-fronts/fixed-pattern-defect-eventual-constancy
Created: 1794227802192; updated: 1794230746740

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 494 (msg_1c07b87e6001ahbGwyMiSdyewl)

**Verdict: no counterexample and no proof of eventual constancy. I found a precise obstruction: the information-rounding part of `D_Q(n)` oscillates infinitely for every `Q` with a non-integral information defect, but deciding whether `D_Q` itself oscillates reduces to an open correlation with the sorting-number excess `E(n)=S(n)-ceil(log2 n!)`.**

No repository or Lean changes were made. Work is in `/tmp/opencode/fp/` (`FINDINGS.md`, `chain.go`, `chain_free_dp.py`).

## 1. The exact decomposition

For fixed `Q`, `q=|Q|`, `e_Q=#Ext(Q)`, `P_n=Q ⊔ A_{n-q}`:

```
e(P_n) = e_Q · n!/q!
C(n)   = ceil(log2 n!)
C_P(n) = ceil(log2 e(P_n))
E(n)   = S(n)-C(n)
δ_Q(n) = F(P_n)-C_P(n) ≥ 0
```

Then exactly:

```
D_Q(n) = S(n)-F(P_n)
       = E(n) + [C(n)-C_P(n)] - δ_Q(n).
```

Write `α_Q=log2(q!/e_Q)=k+β`. For `β>0` and `n≥3`:

```
C(n)-C_P(n) = k + 1_{ {log2 n!} < β }.
```

## 2. A paper-checkable leading-bit lemma

Let `x_n={log2 n!}` and `d_n={log2 n}`. Since intervals `(2^{m+a},2^{m+b})` contain integers for large `m`, `{d_n}` is dense in `[0,1]`, and

```
x_{n+1} = { x_n + d_{n+1} }.
```

**Lemma.** For every `β∈(0,1)`, `x_n<β` infinitely often and `x_n>β` infinitely often.

Sketch: if `x_n` stayed below `β`, an increment in `(max(0,β-x_n),1-x_n)` pushes it above without wrapping. If it stayed above `β`, for `β>1/2` an increment in `(1-β,β)` wraps it below; for small `β`, two consecutive increments do the same. Density of `{log2 n}` supplies such indices arbitrarily late.

Therefore, for every `Q` with non-integral `α_Q`, the term `C(n)-C_P(n)` is **not eventually constant**: it alternates between two consecutive integers `k` and `k+1` infinitely often.

## 3. Why this does not disprove eventual constancy

Boundedness only gives `0≤D_Q(n)≤S(q)`. Rearranging the identity:

```
δ_Q(n)-E(n) = [C(n)-C_P(n)] - D_Q(n).
```

So a proof that `D_Q` is eventually constant would force `δ_Q(n)-E(n)` to alternate in lockstep with the leading bits of `n!`, between two consecutive values. That is an exact correlation between the fixed-pattern information defect `δ_Q` and the global sorting excess `E`, not a consequence of boundedness. Conversely, the oscillating information term alone is absorbed by `δ_Q-E`.

## 4. Concrete `Q=C3` reduction

Here `q=3`, `e_Q=1`, `α=log2 6=2.585`, `β=log2(3/2)`.

| `n` | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|
| `F(C3⊔A_{n-3})` | 0 | 2 | 5 | 8 | 10 | 13 | 17 |
| `S(n)` | 3 | 5 | 7 | 10 | 13 | 16 | 19 |
| `D_C3(n)` | 3 | 3 | 2 | 2 | 3 | 3 | 2 |
| `C-C_P` | 3 | 3 | 2 | 3 | 3 | 3 | 3 |
| `δ` | 0 | 0 | 0 | 1 | 0 | 0 | 1 |

On `E=0` points: high-side points (`x_n>β`) satisfy `D=2-δ≤2`; low-side points satisfy `D=3-δ≤3`. The dips at `n=6,9` are exactly `δ=1`.

If `D_C3` were eventually `c`, then on the infinite high-side and low-side sets one would need

```
δ(n)-E(n) = 2-c   (high side),
δ(n)-E(n) = 3-c   (low side).
```

For example, `c=3` would force `E(n)≥1` at every sufficiently large high-side `n`; `c=2` would force `δ` to alternate `0,1` with the leading-bit side.

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

## Output 566 (msg_1c07c59cc001yz53qSIkhOFYaA)

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
