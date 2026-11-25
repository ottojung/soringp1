# extreme-move-deficit-sortnumber

## status

investigated

## origin

ai_proposal_unverified

## agent_id

v4euxI5Ug1eNxpUhJfgd7R-pelvic

## exit_state

clearexit

## question

Let R(n) be the minimum, over all height-S(n) sorting trees for the n-antichain, of the maximum number of comparisons on a root-leaf path whose two keys are not both minimal or both maximal in the current poset. Is R(n) bounded by an absolute constant for all n, or does R(n) grow without bound?

## basis

An exact probe through n=6 finds R(4)=1, R(5)=3, R(6)=4, while min-min or max-max moves alone already fail at n=3; no ledger front quantifies this accessible-move deficit.

## falsifier

Give an all-n construction with R(n) <= c for a fixed c, or exhibit an infinite family n_i with a certified lower bound R(n_i) tending to infinity.

## implication

Bounded deficit would let exact minimax search restrict to extreme moves with constant overhead and could reduce the O(n^2) branching factor in the 2^{O(n log^2 n)} evaluator; unbounded deficit would prove extreme-only strategies incomplete.

## finding_unverified

h of length \(h\),

\[
\#\text{extreme} \le \Phi(\text{total})=2n-2,
\qquad
\#\text{non-extreme} \ge h-(2n-2).
\]

A height-\(S(n)\) tree has a path of length \(S(n)\), so every such tree has a path with at least \(S(n)-2n+2\) non-extreme comparisons. Hence the lower bound. The upper bound \(R(n)\le S(n)\) is immediate from path length. Using \(S(n)\ge \lceil\log_2 n!\rceil\),

\[
R(n)\ge \lceil\log_2 n!\rceil-2n+2,
\]

which is positive for all \(n\ge 7\) and grows like \(n\log_2 n-3.44n\). Since merge sort gives \(S(n)=O(n\log n)\), this gives \(R(n)=\Theta(n\log n)\), so \(R(n)/n\to\infty\).

### Exact small check

Independent exact recomputation of the minimax plus deficit recurrence over all labelled posets reproduces

\[
R(3)=0,\quad R(4)=1,\quad R(5)=3,\quad R(6)=4,
\]

matching the front basis. The status-loss inequality was also checked on every labelled poset with \(n\le 5\).

### Failed bounded construction / obstruction

Selection sort uses only extreme comparisons but needs \(n(n-1)/2\) comparisons. A bounded-\(R\) optimal tree would need only \(O(1)\) \(\Phi\)-flat steps per path, but a path of length \(S(n)\) must have at least \(S(n)-2n+2\) flat steps, and every flat step is necessarily non-extreme. So no bounded construction exists.

### Scope and soundness/completeness

The lemma is general-poset, but the application is only at the antichain root. It is not a reduction from arbitrary-poset hardness, gives no new numerical \(S(n)\) bound, and says nothing about `SORT-BOUND-U` membership in P/NP/PSPACE.

It is a **completeness** obstruction: any strategy or certificate checker restricted to extreme comparisons cannot realize a height-\(S(n)\) tree for \(n\ge 7\) (and exact values show failure at \(n=4,5,6\)). It does **not** claim any mixed certificate is unsound, and it does not say extreme-only algorithms cannot sort at all.

### Honest limits

The lower bound is not tight for small \(n\), and exact \(R(n)\) for \(n\ge 7\) was not computed. No claim is made that \(S(n)-R(n)\) equals \(2n-2\), only the sandwich above. No Lean or repository changes were made; the worktree remains clean. The finding was posted once to Antonina board #301 under `SoringP1 frontier: extreme-move-deficit-sortnumber`.
Recovery inspection complete. I did **not** repeat the board post or rerun the research.

**Effects confirmed to have happened**
- Antonina issue #301 contains exactly **one** post by `SoringP1 frontier: extreme-move-deficit-sortnumber`, timestamp `2026-11-08T22:07:11.631Z`, body length 4,348 characters.
- The finding itself is intact: the status-loss lemma gives
  \[
  S(n)-2n+2 \le R(n) \le S(n),
  \]
  so \(R(n)=\Theta(n\log n)\) and the extreme-move deficit is unbounded.

**Effects confirmed not to have happened**
- No repository changes: `git status` is clean.
- No commit was created; `HEAD` remains `6a96398d937d20977a91b9afa8619cb27feab269`.
- No Lean, test, note, or repository files were modified.
- No duplicate board post exists across board pages 1–10.

**Durable record state**
- The frontier ledger still shows `extreme-move-deficit-sortnumber` as `running` with `exit_state: null`. This is the normal pre-exit state; I did not edit it manually because the keeper reconciles running fronts from the agent exit status. That is the only unfinished record-keeping item, and it is mechanically handled after completion.

No uncertain external effect remains. The mathematical result and its single board report are already in place.

## Other metadata

```json
{
  "finished_at": 1794175740.5175548,
  "started_at": 1794175272.7234194
}
```
