# witness-verification-minimax-separation-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

yBTH6ifbGUoXWcAMOslvYy-necrosed

## exit_state

clearexit

## question

For all n and every n-element poset P given explicitly by a polynomial-size transitive reduction, is the decision F(P) <= k solvable in time poly(n) times 2^{O(k - log2 e(P))}, so that the information slack k - log2 e(P) uniformly controls the cost of verifying a minimax value on explicit posets, or does an all-n family defeat every slack-parameterized budgeted search?

## basis

Antonina #301 (2026-11-20) contains two independent but INCONCLUSIVE F computations for an n=9 witness that stalled with plain memoized minimax; an information-pruned budgeted search here returned F(P)=12 and F(Q)=11 for that same witness in seconds. No ledger front parameterizes exact minimax verification cost by information slack on explicit posets.

## falsifier

Exhibit an all-n family of explicit posets P_n and budgets k_n with small slack k_n - log2 e(P_n) = O(log n) for which every information-pruned or budgeted minimax search still requires 2^{Omega(n)} time, or prove a uniform slack-parameterized upper bound.

## implication

A uniform slack-parameterized bound would give a cheap, sound value-checker for explicit posets and sharpen the budgeted-DFS engine behind SORT-BOUND-U upper bounds; a counterexample would show extension-count slack alone cannot control minimax verification cost.

## finding_unverified

I’ll first inspect the current worktree, Git state, and any durable records for this task so I can distinguish completed work from anything interrupted. I won’t repost or make repository changes.
The workspace is on `billy-dev`, branch `billy-dev`, and the Git tree is clean; I found no durable result or repository artifact for this specific slack-parameterized question. I’m checking the current #301 digest and the repository’s literature/algorithm notes next.
**No all-\(n\) theorem or counterexample was established.** I made no repository changes and did not post to #301: the current board already records the two independent, inconclusive plain-minimax computations and the later information-pruned \(n=9\) results \(F(P)=12\), \(F(Q)=11\). Repeating those results would not advance this question.

The main obstacle is that the proposed runtime needs a sharper specification before it is falsifiable. For arbitrary budgets, \(k-\log_2 e(P)\) can be negative—for example, \(k=0\) on an antichain—so \(2^{O(k-\log_2 e(P))}\) does not define the usual nonnegative parameterized runtime bound. A meaningful version should specify a promise such as \(k\ge\lceil\log_2 e(P)\rceil\), or define a nonnegative slack and state how instances below the information bound are handled. Also, “every information-pruned or budgeted minimax search requires exponential time” is not an algorithm-independent lower-bound statement unless the search model is defined.

The literature reviewed here does not settle the repaired claim. Cardinal et al.’s polynomial-time results for sorting under partial information give comparison-efficient strategies, not exact minimax-value verification. The repository’s boundary audit likewise warns against transferring general-poset complexity results to the antichain problem \(S(n)\). The reported \(n=9\) computation is useful experimental evidence about one instance, not evidence for an all-\(n\) bound or lower bound.

**Unresolved:** whether a properly specified, uniform slack-parameterized exact verifier exists for explicit posets, or whether a family defeats a clearly defined search procedure. I did not infer a result about computing \(S(n)\) from the general-poset question.
The prior turn recorded no post or repository edits. I’ll verify the current Git state and the latest durable #301 entries once more, then report only whether anything remains unfinished.
**Recovery audit:** the worktree is clean on `billy-dev` at `6a96398`; there are no untracked files. The current #301 digest shows no post about the slack-parameterized front, and the durable scratch report confirms no repository edits or board post for that work. No external side effect needs repeating.

The mathematical investigation remains **unfinished**: no all-\(n\) upper bound or counterexample was established. One record discrepancy is worth flagging: the board reports the information-pruned search returned \(F(P)=12\), \(F(Q)=11\), while `/tmp/opencode/report.md` records a separate verification attempt that confirmed \(e(P)=e(Q)=1512\) but could not reproduce either \(F\)-value. Treat the values as reported, not independently verified. No follow-up action was taken.

## Other metadata

```json
{
  "finished_at": 1795171161.7976775,
  "started_at": 1795170583.8675582
}
```
