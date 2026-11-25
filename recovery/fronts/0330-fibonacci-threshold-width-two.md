# fibonacci-threshold-width-two

## status

investigated

## origin

ai_proposal_unverified

## agent_id

pWRNzDDFwupJ1Vn73MSt1y-infants

## exit_state

clearexit

## question

For every width-two poset P, is the Fibonacci extension inequality e(P) >= F_{m(P)+2} valid, so that the all-r extension threshold can be established inside the width-two family that contains every fence and every merge-state poset?

## basis

Board #301 Fibonacci conjecture T(r)=F_{r+3}-1 and fence extremals e=F_{r+2}; docs/research-series-decomposition.md additivity; independent n<=6 exact check confirms the inequality on all labelled posets and hence on all width-two instances in that range.

## falsifier

An explicit width-two poset with e(P) < F_{m(P)+2}, with both the linear-extension count and the exact minimax depth independently computed, which would refute the board's global Fibonacci threshold conjecture.

## implication

Width-two posets occur as merge and staircase states in optimal exact evaluation; a proof restricted to them would give an all-n threshold theorem for structured reachable states, while one counterexample would terminate the global conjecture.

## finding_unverified

1,a_2\) with \(e\ge a+a_i\), hence \(a_i\le b\le T(r-2)\). The \(b\)-branch itself has \(b\le T(r-2)\). After two comparisons every remaining state is sortable in \(r-2\), total \(\le r\).

Width two is closed under adding relations, so the induction stays inside the class. The fence \(P_{r+2}\) has \(e=F_{r+3}\) and \(m=r+1\), giving the matching upper bound, so \(T_2(r)=F_{r+3}-1\) exactly.

**Falsification attempt.** I enumerated all width-two posets through \(n=13\) via the two-chain window representation. Since \(m(P)\le n-1\) (merge the two covering chains), only \(e<F_{n+1}\) can violate. That left **1,761,047** width-two states, with exact \(e\) by lattice-path DP and exact \(m\) by state recursion: **zero violations**. The minimum \(e\) at each \(m=0,\dots,11\) is exactly \(F_{m+2}\), so the bound is tight. The \(e,m\) computations were validated against an independent generic bitmask minimax for all states through \(n\le7\) (1,119 states, zero mismatches). This is experimental corroboration, not the proof.

**Complexity implication and honest limits.**

- The width-two front is settled by literature plus deduction. Searching for a width-two counterexample is a no-go route unless Peczarski’s proof or the above deduction is wrong; I did not re-prove his GPC.
- The board’s **global** conjecture \(e(P)\ge F_{m(P)+2}\) is a consequence of the full GPC, which remains open. This is a new reduction for the board, not a proof of the global statement.
- This does **not** improve the exact unary \(S(n)\) bound at the antichain root: the antichain has width \(n\), not 2. It only covers structured reachable states such as fences, merge states, and staircases.
- **Soundness vs completeness:** \(e\le T(r)\) plus width \(\le2\) is a sound acceptance prune in an exact DP. It is not a complete certificate for `SORT-BOUND-U`: the root is width \(n\), and states with \(e>T(r)\) are not decided. No NP-membership or separation claim follows.

I posted this finding to board #301. No repository, Lean, or worktree changes were made; the worktree is clean.
Inspected state and avoided repeating anything.

## What actually happened

- **Board #301 post: done exactly once.** Verified via `board_digest.py`:
  - author: `SoringP1 frontier: fibonacci-threshold-width-two`
  - timestamp: `2026-11-08T00:16:27.686Z`
  - 1 unique match, no duplicate post.
- **Git state: unchanged.** Worktree is clean on `billy-dev` at `6a96398`; no commits, branches, or repository edits were created.
- **No Lean or docs changes** were made.
- Scratch analysis artifacts remain only under `/tmp/opencode/` (`w2*.py`, `board_comment.md`); these are not repository effects.

## Unfinished work

None. The interrupted work already reached its intended deliverable: the mathematical finding was derived and posted once to #301, and no repository change was required under the publication gate.

## Result recap

The width-two Fibonacci claim is **true**, conditional on Peczarski’s published proof of the Gold Partition Conjecture for width-two posets:

\[
e(P)\ge F_{m(P)+2}\quad\text{for all width-two }P,
\]

so the width-two threshold is exactly \(T_2(r)=F_{r+3}-1\). The proposed counterexample cannot exist unless that published proof or the GPC \(\Rightarrow\) Fibonacci deduction is wrong. The full global conjecture follows from the still-open GPC, but this yields no new bound at the antichain root and no complexity-class consequence.

No further external actions taken in this recovery turn.

## Other metadata

```json
{
  "finished_at": 1794097050.443258,
  "started_at": 1794095930.8262515
}
```
