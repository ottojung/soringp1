# sorting-increment-second-difference

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ozolQMXLtReLzPWVZQwLj1-following

## exit_state

clearexit

## question

Is the second difference D(n)=S(n+1)-2S(n)+S(n-1) always in {0,1} for every n>=2, so that consecutive optimal comparison-count increments can increase by at most one per step?

## basis

Exact values S(0..22) give D(n) in {0,1}; the open bounds S(23) in {75,76} and S(24) in {80,81} make D(23)=S(24)-2S(23)+71 range over {-1,0,1,2}, a decisive finite test; the ledger convexity front asks only D(n)>=0 and the increment-spectrum front bounds first differences, neither addresses the upper bound D(n)<=1.

## falsifier

Find an explicit n with D(n) outside {0,1}, in particular an increment jump D(n)>=2 or a decrease D(n)<0, certifiable from exact or tightly bounded S values, or prove such a value occurs infinitely often.

## implication

A {0,1} second-difference law would sharply constrain admissible excess fluctuations E(n)=S(n)-ceil(log2 n!) and give a new all-n structural theorem about S(n); a jump of two would refute the natural strengthening of discrete convexity and identify a concrete new obstruction.

## finding_unverified

F(n)-F(n-1)=5` for `23≤n≤42`. Since `S≤F`, induction forces

\[
S(n)=F(n)
\]

for every `23≤n≤42`:

`76,81,86,91,96,101,106,111,116,121,126,131,136,141,146,151,156,161,166,171`.

Thus any sound sorting tree beating Ford–Johnson by even one comparison anywhere in `[23,42]` refutes the law. In particular the law forces `S(28)=101`, whereas Stober–Weiss only prove `S(28)≥99`. The literature currently says Ford–Johnson is unbeaten below 47, so this is not yet a refutation.

Using also `C(45)=187` and the published `S(47)≤200`, the law forces exactly one of

\[
(S(43),S(44),S(45),S(46),S(47))
=(176,181,187,193,199)
\]

or

\[
(176,182,188,194,200).
\]

So the law excludes the currently allowed values `S(46)=192`, `S(46)=195`, `S(47)=198`, and `S(45)=189`. A certified `S(46)≤192` or `S(47)≤198` would refute it; so would `S(46)≥195` together with `S(47)≤200`. Current bounds leave this open.

**3. General-poset counterexample — but not for `S(n)`**

For ordinal sums, the exact identity `F(A⊕B)=F(A)+F(B)` holds. Let `P_j=A_j⊕A_j`, where `A_j` is the antichain. Then `F(P_j)=2S(j)`. At `j=4,5,6`, `F=10,14,20`, so the second difference is

\[
20-2\cdot 14+10=2.
\]

Hence the `{0,1}` second-difference law is **false for general posets**. This does not transfer to the antichain root, so it is not a counterexample to the sorting number itself.

**4. Soundness vs completeness**

A height-`k` decision tree is only a **sound** certificate for `S(n)≤k`; an optimal tree may have exponentially many nodes, so it is not a polynomial completeness certificate. To refute the second-difference law, a single sound tree below the predicted value suffices. To prove the law, lower bounds on the exact optimum are needed.

**5. Honest limits**

No unconditional counterexample exists in current published data. `S(23)`, `S(24)`, and the exact values in `[23,42]` remain open, and no better-than-Ford–Johnson algorithm below 47 is published. The staircase is a deduction from the law, not a proof of it.

Board #301 was updated once with this finding. No Lean or repository changes were made; the worktree remains clean at `6a96398`.
Recovery inspection complete. I did not repeat the prompt or any external action.

**Verified effects**

- **Host:** `billy-dev`.
- **Repository:** `/home/lubko/soring-fronts/sorting-increment-second-difference`.
- **Git:** branch `billy-dev`, HEAD `6a96398`, clean worktree. No commits, files, Lean changes, PRs, or other repo effects from the prior turn.
- **Board #301:** exactly one matching post exists, at `2026-11-09T21:47:40.701Z`, author `SoringP1 frontier: sorting-increment-second-difference`. It matches the prepared scratch text. No duplicate was posted and none is needed.
- **Scratch only:** `/tmp/opencode/seconds/board_post.txt`, `forced.py`, `post_result.json`. These are outside the repository.

**Unfinished / for review**

- The durable ledger entry `sorting-increment-second-difference` still shows `status: running`, with no `exit_state` or agent recorded. That transition belongs to the keeper, so I did not edit it manually.
- No other external side effects are visible; no uncertain purchases, commits, or duplicate posts were found.

The mathematical result from the previous turn remains the completed work: no unconditional disproof; corrected finite index `D(22)=S(23)-76`; conditional staircase forcing `S(n)=F(n)` for `23≤n≤42`; and the general-poset counterexample showing the law is antichain-specific. I am not rerunning that research.

## Other metadata

```json
{
  "finished_at": 1794260990.3690088,
  "started_at": 1794260185.8007507
}
```
