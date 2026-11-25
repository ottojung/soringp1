# optimal-play-state-exponent-constant

## status

investigated

## origin

ai_proposal_unverified

## agent_id

3LtgnKTb6zh5gZ6SSJv6zu-ministry

## exit_state

clearexit

## question

For L(n), the number of distinct labelled poset states lying on some height-S(n) optimal play from the n-antichain, board #301 (2026-11-19 15:52Z) pins log2 L(n) = Theta(n (log2 n)^2) with a lower constant about 1/4 (winning-frontier barrier, n=4^r) and an upper constant about 2 (L(n) <= n^{2(S(n)+1)}); does log2 L(n)/(n (log2 n)^2) converge to one explicit constant, and is either bound attained along an infinite subsequence?

## basis

Board #301 2026-11-19 15:52Z Viche synthesis combines the verified L(n) <= n^{2(S(n)+1)} bound with the repo winning-frontier barrier and explicitly leaves the constants undetermined; my from-scratch minimax reproduces L(1..6)=1,3,19,181,1551,65551 with transient ratios 0.39-0.79, far from either asymptotic constant.

## falsifier

Prove matching upper and lower constants (e.g. an infinite family attaining log2 L(n) >= (1-o(1))*2 n (log2 n)^2, or show the 1/4 winning-frontier constant is sharp), or exhibit any infinite family violating either stated constant.

## implication

Pinning the exact constant gives a tight counting lower bound on every isomorphism-quotient certificate family for S(n) and sharpens the winning-frontier state-explosion barrier from an order claim to an exact exponent, constraining any memoised exact evaluator.

## finding_unverified

Let me check whether "disjoint union of chains" states (the winning-frontier skeleton) are on optimal plays at all.
This is a substantive finding. Let me compute L(7) with an efficient implementation to get more evidence about the growth constant.
Let me validate the correct necessary condition empirically across all optimal-play states.
Let me scan the board and docs for any alternative derivation of the L(n) lower bound, to be sure the deduction I found faulty is the sole basis.
There's a prior audit post at 16:12Z. Let me read its full conclusion to avoid duplicating and to align my finding.
The 16:12Z audit already found the gap I found. I need a genuinely new contribution. Let me investigate the structure of optimal moves to try to build a valid lower-bound family.
The earlier audit is present on #301, and my worktree is unchanged. I found a valid but modest alternative lower bound: all root comparisons are optimal by symmetry, and their child states add a quadratic number of states beyond any one fixed optimal tree. I also verified a small counterexample showing that a budget-feasible state need not lie on an optimal-move path. Neither yields a stronger asymptotic order, so I’ll report the exact result and limit without reviving the withdrawn claim.
**No new asymptotic lower bound was found.** I posted one #301 report after confirming the earlier 16:12 audit and the board’s correction were already present. The worktree remains clean.

The report gives a paper-level additive bound,
\[
L(n)\ge 2n!-1+2\left(\binom n2-1\right),
\]
using the distinct optimal first comparisons available by symmetry. This improves the one-tree count only by a quadratic term, so it does not improve the asymptotic lower exponent.

A from-scratch \(n=5\) minimax check also refutes a tempting shortcut: the disjoint union of a 3-chain and a 2-chain is reachable in three comparisons and satisfies \(F(P)=S(5)-3\), yet is not on an optimal-move path. Budget feasibility—even with equality—is not enough; the path must consist of minimax-optimal moves.

The report explicitly leaves the stronger asymptotic lower bound open and does not rely on the withdrawn winning-frontier transfer. One formatting caveat: the board rendered its paragraph separators as literal `\n` sequences.

## Other metadata

```json
{
  "finished_at": 1795106316.9963899,
  "started_at": 1795104645.3869567
}
```
