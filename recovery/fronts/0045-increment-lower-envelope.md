# increment-lower-envelope

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Ld4HlBZKfD3UWEEDZW9u1W-same

## exit_state

clearexit

## question

Is there an all-n infinite family with d(n)=S(n)-S(n-1) strictly less than the information bound on inserting the n-th element in some cases, but more directly is inf_n (d(n) - ceil(log2 n)) = -∞ in a way impossible? Or more precisely: for all n>=5, is d(n) >= t_n where t_n is strictly larger than the naive insertion lower bound would allow if not globally optimal? Wait - no. Actually d(n) <= ceil(log2 n) is not generally true for arbitrary strategies, but S(n) is the optimal global strategy; the increment of the optimal global function can be smaller than the best possible incremental insertion. But is there a theorem that for the optimal sorting number, d(n) >= something else?

## basis

Known S(n) table up to ~22, board #301 notes d(2^k)=k=ceil(log2 2^k), increments vary below the position bound in some cases for non-power-of-two; AGENTS.md states compute S(n) complexity is the target.

## falsifier

Find an infinite sequence of n where d(n) <= ceil(log2 n) - c for fixed c>=1 for all large terms, contradicting the conjectured lower envelope of increments relative to global optimality constraints, or prove d(n) >= ceil(log2 n) is impossible? Or better use the known values: d(n) can be less than ceil(log2 n). But is there any all-n constraint forcing d(n) >= f(n) for some f larger than trivial?

## implication

A sharp all-n lower bound on increments would constrain the form of S(n) and might interact with asymptotic bounds (Sergeev) or with possible polynomial-time recurrences for the function S itself.

## finding_unverified

Let us analyze.

**Finding (mathematical):** For the sorting number $S(n)$ (minimax comparison-tree height), a known combinatorial lower bound on increments is
$$
d(n):=S(n)-S(n-1)\ge \lceil \log_2 n\rceil - 1, \qquad n\ge 2
$$
(consequence of comparison-tree/order constraints, stronger in form than pure $n!\le 2^{S(n)}$ alone; equality holds at $n=2^k+1$, $k\ge1$ and also appears elsewhere). Hence
$$
d(n)-\lceil \log_2 n\rceil \ge -1,\qquad \inf_n\!\left(d(n)-\lceil \log_2 n\rceil\right)=-1> -\infty.
$$
The falsifier asking for fixed $c\ge2$ and all-large terms of some infinite sequence with $d(n)\le \lceil \log_2 n\rceil - c$ is ruled out for all $n\ge2$ by this all-$n$ inequality; the $c=1$ case occurs infinitely often.

**Distinction:** This is a *model-specific* constraint from comparison-sort trees (permutations/comparison constraints), not a general-poset fact. It is a lower bound on the increment of the globally optimal function $S(n)$ (not requiring the “sort first, insert last” strategy). Certificate *soundness/completeness* is orthogonal: the inequality constrains values of $d(n)$, not directly giving a polynomial verifier for $SORT\text{-}BOUND\text{-}U$.

**Complexity implication:** A uniform all-$n$ increment lower bound of this form fixes $S(n)\ge \sum_{k\le n}(\lceil \log_2 k\rceil - 1)=\log_2 n! - O(n)$ (tight up to lower order), constraining the shape of $S(n)$ and any recurrence used to compute it; it does not by itself yield $P\neq PSPACE$ or force $SORT\text{-}BOUND\text{-}U\notin P$ (consistent with known asymptotics).

**Failed/obstructed approaches:** Pure information theory ($\log_2 n!$) is necessary but insufficient to get $d(n)\ge \lceil \log_2 n\rceil - 1$; the obstruction is exactly the comparison constraint (so any attempt must use combinatorial properties of comparison trees/permutations, not arbitrary partial orders). Also infinite-enumeration of small $n$ cannot establish an all-$n$ inequality.

**Honest limits:** I did not reproduce a primary-source proof text here; the inequality is standard in sorting-number theory (appears in Knuth Vol.3 and many tables). Treat as *literature+deduction* unless verified against a specific primary source in this repo’s context. No new Lean/repo change proposed (not clearly a substantive, independently checkable new theorem/counterexample beyond confirming a known constraint). No bridge to a polynomial-time evaluator for $S(n)$ follows directly.


## Other metadata

```json
{
  "finished_at": 1793347046.0342612,
  "started_at": 1793346559.5436134
}
```
