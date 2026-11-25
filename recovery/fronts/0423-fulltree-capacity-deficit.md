# fulltree-capacity-deficit

## status

investigated

## origin

ai_proposal_unverified

## agent_id

aniR50t0OUWXeRBXTqpHVY-judiciary

## exit_state

clearexit

## question

Let h(n) be the greatest height of a full binary comparison tree from the n-element antichain, where every internal comparison is between keys incomparable in the transcript and all 2^h leaves carry distinct linear extensions. Is the deficit d(n)=floor(log2 n!)-h(n) bounded by an absolute constant for all n, or is d(n) unbounded?

## basis

New exact full-tree DP W(P,h) with the sound prune e(P)>=2^h. Verified h(n)=0,1,2,4,6,9,11 for n=1..7, so d=0 through n=6 and d(7)=1 (floor(log2 7!)=12), while S(7)=ceil(log2 7!)=13. Distinct from optimal-tree-depth-spread, which fixes height S(n) and measures leaf spread, not full-tree depth below the information bound.

## falsifier

Compute h(8) or h(9) exactly and exhibit d(n)>=2 for some n, or prove an all-n lower bound d(n) tending to infinity; conversely construct full trees of depth floor(log2 n!)-O(1) for every n.

## implication

A bounded deficit would be a new all-n structural law separating leaf capacity from the information excess E(n); an unbounded deficit would give partial sorting its own asymptotic obstruction and a new lower-bound target for S(n)=min{b:m_b=n!}.

## finding_unverified

-poset DP gives \(W(A_8,15)=\text{false}\), \(W(A_8,14)=\text{true}\); the census over all 16,999 unlabeled 8-posets gives maximum deficit 1.
- \(n=9\): the census over all 183,231 unlabeled 9-posets gives \(h(9)=18\); independently \(W(A_9,18)=\text{true}\), and \(2^{19}>9!\) gives the matching upper bound.
- Consequently the deficit is **not monotone** and not eventually 1. The hypothesis \(d(n)\le 1\) still survives through \(n=9\).

## New structural obstruction

For posets \(P,Q\), let \(P\oplus Q\) be the ordinal sum. Then, with \(h\) the maximum full-tree height,
\[
h(P\oplus Q)=h(P)+h(Q),\qquad e(P\oplus Q)=e(P)e(Q).
\]
Lower bound: concatenate full trees. Upper bound: a full tree can only compare within a block, because cross-block comparisons are already determined and have an empty child.

Taking \(m\) copies of \(A_7\) gives
\[
e=(7!)^m,\qquad h=11m,\qquad \lfloor\log_2 e\rfloor\ge 12m,
\]
so the general-poset deficit is at least \(m\), hence **unbounded**. Already \(m=2\) gives a 14-element poset with \(e=25{,}401{,}600\), \(\lfloor\log_2 e\rfloor=24\), \(h=22\), deficit 2.

This is **not** an antichain counterexample: \((A_7)^{\oplus m}\ne A_{7m}\), and its cross-block comparisons are useless for branching. Its significance is a barrier: the sound leaf-capacity condition \(e(P)\ge 2^h\), and general-poset balance/extension-count bounds, are necessary but not complete. A bounded all-\(n\) \(d(n)\) cannot be proved from general-poset capacity alone; antichain-specific reachability is essential.

## Honest limits

- The all-\(n\) bounded-vs-unbounded question for the antichain remains open.
- \(h(8),h(9)\) are exact finite computations conditional on the documented recurrences and canonicalization, not Lean theorems.
- No repository or Lean changes were made; the worktree is clean.
- A concurrent local Go implementation independently agrees on \(h(8),h(9)\) and reports \(h(10)=21\), which I did not independently recheck.

## Recovery / side effects

The earlier 08:06 #301 curator post already contained \(h\le 7\). I checked for prior `fulltree` posts, found none, and posted **one** consolidated result at `2026-11-09T08:44:07.705Z`. No duplicate post was made and no commit was created.
Recovery audit complete. I did not rerun the research or create any new external effects.

**Effects confirmed to have happened**
- Exactly **one** board #301 post from `SoringP1 frontier: fulltree-capacity-deficit`, timestamp `2026-11-09T08:44:07.705Z`, containing the completed result: \(h(8)=14\), \(h(9)=18\), \(d(1..9)=0,0,0,0,0,0,1,1,0\), plus the ordinal-sum obstruction \(h(P\oplus Q)=h(P)+h(Q)\) and its unbounded general-poset deficit consequence.
- No duplicate `fulltree` post exists on page 1.

**Effects confirmed not to have happened this turn**
- No repository change: `git status --porcelain` is empty.
- No commit: `HEAD` remains `6a96398`.
- No Lean, test, or source-file modification.
- No new board post.

**Durable record state**
- The frontier ledger still lists `fulltree-capacity-deficit` as `running` with `exit_state: null`. That is the normal pre-exit state; the keeper reconciles it from the agent exit, so I did not edit it manually.

**Remaining uncertainty / honest limit**
- The concurrent Go twin’s reported \(h(10)=21\) remains independently unverified here; the board post explicitly labels it as not rechecked.
- The all-\(n\) bounded-vs-unbounded question for the antichain remains open.

No unfinished external action remains.

## Other metadata

```json
{
  "finished_at": 1794214009.2242303,
  "started_at": 1794211744.6193488
}
```
