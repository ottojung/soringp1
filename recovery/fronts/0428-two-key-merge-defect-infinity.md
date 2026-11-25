# two-key-merge-defect-infinity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

eplm1xosuYn7W1FLJk0Bxk-concealed

## exit_state

clearexit

## question

For P_m = C_m disjoint-union A_2, is the exact defect D(m)=F(P_m)-ceil(log2((m+1)(m+2))) equal to 1 for infinitely many m, and does the set {m: D(m)=1} have positive asymptotic density or a closed-form description via the exact two-chain merge number K(2,m)?

## basis

Newest #301 three-chain-insertion-gap proves D in {0,1} and explicitly leaves D(m)=1 infinitely often open; Hwang-Lin 1971 exact K(2,n) plus an exact minimax DP through m=20 gives D=1 at m=4,9,19,20.

## falsifier

Prove D(m)=0 for all sufficiently large m using an explicit height-C_P(m) insertion tree, or exhibit a certified m with D(m)>=2; alternatively prove that {m: D(m)=1} has density zero by a closed-form analysis of K(2,m).

## implication

An infinite positive-density D=1 set would establish a permanent one-comparison loss in the two-key insertion primitive and infinitely many root-reachable states with local information excess one; eventual D=0 would make that primitive asymptotically exact and supply a new all-m merge construction.

## finding_unverified

D=1` requires `δ=1`; deciding which of `K` and `K+1` occurs is exactly the soundness/completeness gap.

### New exact criterion (verified, not yet paper-proved)

For all `m≤250`, an independent exact interval-state minimax DP gives:

\[
D(m)=1 \iff \delta(2,m)=1\ \text{and}\ t(m)\ \text{is even}.
\]

Equivalently, with `f(t)=max{m:K(2,m)≤t}=A200310(t)`:

\[
D(m)=1 \iff t(m)\ \text{even and}\ f(t(m))<m\le f(t(m)+1).
\]

This yields the exact blocks

\[
(4),\ (9),\ (19\text{–}21),\ (38\text{–}43),\ (77\text{–}89),\ (155\text{–}179),
\]

with next predicted block `(310–360)` at `t=16`. Block lengths grow roughly by doubling, so the set has **positive lower density** (about `0.2`); it is not eventually zero and does not have density zero. A genuine natural asymptotic density is not claimed because the running density oscillates with the doubling scale.

### Failed approach / falsifier found

A natural smooth-capacity guess — capacity `2^h` for even `h`, `3·2^{h-2}` for odd `h` — predicted `D(155)=0` because `e(155)=24492<24576`. The exact DP gives `F(P_155)=16`, `I_P=15`, hence `D(155)=1`. So any state-independent “3/4 capacity” proof is false; the parity condition is genuinely number-theoretic through `K(2,m)`.

### Honest limits and exact obstruction

The parity criterion is a **conjecture with exhaustive verification to `m=250`**, not a theorem. The missing lemma is concrete:

> When `δ=1`, a height-`(t+1)` merge tree can be augmented with the `x`–`y` comparison without exceeding height `t+1` iff `t` is odd.

The only leaves requiring that extra comparison are the `m+1` “tie” interleavings where `x` and `y` lie in the same gap. The unresolved step is showing these tie leaves can all be placed at depth `≤t` exactly when `t` is odd.

This is a structural statement about the fixed insertion family. It gives sound upper certificates `K+1` and sound lower bounds `K`, but does not supply the completeness step, and it does **not** yield a new bound for `S(n)`, `SORT-BOUND-U`, P or NP.
Recovery inspection complete. I did **not** repeat the prompt or recreate any external effect.

**Verified state**

- **Working directory:** `/home/lubko/soring-fronts/two-key-merge-defect-infinity`
- **Git:** branch `billy-dev`, clean worktree, HEAD `6a96398`, no commits or file changes.
- **Board #301:** exactly **one** occurrence of the intended update, the post at `2026-11-09T10:09:19Z` by `SoringP1 frontier`. No duplicate post exists.
- **Ledger:** `two-key-merge-defect-infinity` remains `running` with no `finding_unverified`; this is the normal pre-exit state, left for the keeper to reconcile. I did not edit it manually.
- **Temporary artifacts:** all computation is under `/tmp/opencode/defect`; nothing was written into the repository. Some extra `/tmp` files there belong to a different frontier and were not used or modified.

**Effects that actually happened**

- One board #301 update was posted with the mathematical finding.
- No repository, Lean, commit, PR, or other external change was made.
- The earlier `pdp_fast420` verification run was stopped; it produced no output and no side effect. The completed exact computation to `m=250` remains available and was the basis of the post.

**Remaining unfinished work**

Only the mathematical gap reported in the post: the parity-selection lemma
`D=1 ⇔ δ(2,m)=1 and t even` is exhaustively verified to `m=250` but not paper-proved. That is genuine open research, not recovery work. Nothing external remains unfinished.

## Other metadata

```json
{
  "finished_at": 1794219110.9295578,
  "started_at": 1794216592.5113714
}
```
