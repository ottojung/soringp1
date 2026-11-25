# uniform-extension-base-gap-growth

## status

investigated

## origin

ai_proposal_unverified

## agent_id

KZYP973Th2jAEmgqwbGHdE-delegates

## exit_state

clearexit

## question

Let T(n) = max{ m(P) : P any finite poset with e(P) <= n! } and define Delta(n) = T(n) - S(n) >= 0. We verified Delta(5) >= 1 while Delta(6) = 0 when the maximum is restricted to posets of at most 6 elements. Is Delta(n) bounded by an absolute constant for all n, or does T(n) - S(n) grow without bound as n increases?

## basis

Verified 6-element witness e=120=5!, m=8>S(5)=7 by three independent methods plus exhaustive check that Delta(6)=0 up to 6 elements; literature good-comparison bounds of Kahn-Saks and Cardinal et al.; distinct from the ledger's m(P)-log2 e(P) excess-boundedness fronts because T(n) is a maximum at fixed extension count n! compared with the specific antichain value S(n).

## falsifier

Find any n with T(n) >= S(n)+2 via a bounded search over 7- or 8-element posets with e <= n! (for instance 7! = 5040), or prove a uniform upper bound m(P) <= log2 e(P) + c for all posets with e <= n!, which would force Delta(n) = O(1) for every n.

## implication

An unbounded gap would show that maximizing m under an e <= n! cap systematically overestimates S(n), ruling that quantity out as an exact evaluator; an O(1) gap would make it only a constant-factor approximation, still giving no P, NP or PSPACE placement for SORT-BOUND-U.

## finding_unverified

**Mathematical finding: Δ(n) is unbounded.**

Using the series (ordinal) composition of a fixed 5-element poset \(P_0\) with succ-mask \((0,0,1,3,7)\), which has \(e(P_0)=8\) and \(m(P_0)=4\) (verified by independent minimax; \(\lceil\log_2 8\rceil=3\), excess \(1\)):

- For \(t\ge1\), let \(P_t\) be the ordinal sum of \(t\) copies of \(P_0\).
- Then \(e(P_t)=8^t\) and \(m(P_t)=4t\) (blocks are independent; cross-block comparisons give no information).

Take \(n_t=\min\{n:n!\ge 8^t\}\). Then \(e(P_t)\le n_t!\), so \(T(n_t)\ge 4t\). By Stirling, \(\log_2(n_t!)=3t+O(\log t)\), and standard merge sort gives \(S(n_t)\le n_t\lceil\log_2 n_t\rceil = 3t+o(t)\), while \(S(n_t)\ge \lceil\log_2 n_t!\rceil\ge 3t\). Hence \(S(n_t)=3t+o(t)\) and

\[
\Delta(n_t)=T(n_t)-S(n_t)\ge 4t-(3t+o(t))=t-o(t)\to\infty.
\]

So maximizing \(m(P)\) under an \(e(P)\le n!\) cap systematically overestimates \(S(n)\) by an unbounded amount; \(T(n)\) is not a constant-factor proxy for \(S(n)\). This is a general-poset construction reduced to the fixed antichain root via \(e(P)\le n!\) and standard sorting upper bounds; it gives no complexity-class separation for \(\mathrm{SORT\!-\!BOUND\!-\!U}\).

**Limits:** The result is an asymptotic unboundedness proof, not a finite threshold or exact rate; base case and \(t=2\) (\(e=64,m=8\)) were checked computationally, but no claim about optimal constants beyond the \(4/3\) ratio is made. No repository or Lean changes were made; worktree remains clean. The finding was posted to Antonina issue #301.

## Other metadata

```json
{
  "finished_at": 1795315455.7390807,
  "started_at": 1795314776.3799102
}
```
