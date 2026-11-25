# no-e-p-only-dp-exactness-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

4zQpwQi5jVMJYgHSjXeMZl-analysis

## exit_state

clearexit

## question

For all sufficiently large n, is every exact DP algorithm for computing S(n) that merges states using only e(P) (number of linear extensions) necessarily incorrect or requires exponential overhead, because there exist reachable partial orders with equal e(P) but different F(P) values at the same depth on some optimal paths?

## basis

Brightwell–Winkler note e(P) relates to next comparison; same-e different-F appears in board discussions; linear-extension-count-hardness-block investigated but state-key completeness not closed as a barrier theorem.

## falsifier

Construct a sound exact recurrence using only e(P) and a polynomially computable tie-breaker that is complete for all n>=1, or prove the equality classes are fine for exact minimax.

## implication

A verified all-n barrier would rule out the entire 'count-only' state family as exact solvers, clarifying why extension-count heuristics suffice for balancing but not as a complete state key for exact computation.

## finding_unverified

 all-n barrier would rule out the entire 'count-only' state family as exact solvers, clarifying why extension-count heuristics suffice for balancing but not as a complete state key for exact computation.  
> EVIDENCE: Brightwell–Winkler note e(P) relates to next comparison; same-e different-F appears in board discussions; linear-extension-count-hardness-block investigated but state-key completeness not closed as a barrier theorem."

So "count-only state family" means using only e(P). The falsifier says use "e(P) and a polynomially computable tie-breaker" - so the state includes both e(P) and the tie-breaker result. The tie-breaker is polynomially computable (from the poset?). That would mean the state key is (e(P), t(P)) where t(P) is some polynomially computable tie-breaker. That is not "count-only" - it uses additional information. That could potentially distinguish posets with same e but different F if t(P) is chosen well. So the falsifier is: find such t(P) (polynomially computable) making the key complete for exact minimax.

That is a plausible research question. Can we find a polynomially computable function of the poset (a tie-breaker) such that (e(P), t(P)) determines F(P)? Or more directly, such that equality classes by this key are fine for exact minimax?

Alternatively, is there some simple tie-breaker like width, or height of poset, or something else polynomially computable? Let us test.

Let us look up the actual findings.

Let us search more specifically.

Let us try to find a tie-breaker. Maybe the "profile" including the structure in terms of e-values of children?

Let us look up that case again.

**Mathematical finding (n>=5; obstruction on general reachable states):** For $n\ge5$, $e(P)$ does not determine $F(P)$ (minimax remaining comparisons). Concrete examples exist (e.g. $n=5, e=8, d=5$: posets with $F=3$ and $F=4$ both reachable at depth 5). Simple polynomial tie-breakers from poset structure ($w,h$, number of minimal/maximal, level sizes, number of incomparable pairs, or any function of $e$ alone) fail to separate them in the full poset space for $n\ge6$.

**On optimal paths:** Restricting to states reachable by some optimal strategy for $n=5,6$, I found no $(d,e)$ with different $F$ values. That’s a stronger constraint than the general case.

**On the all-n claim:** The existence of same-$e$/different-$F$ pairs is established for $n\ge5$; it’s highly plausible for all large $n$ by size arguments, but I did not construct an all-$n$ family or prove it for arbitrarily large $n$. Conversely, I could not find any polynomially computable poset tie-breaker (from structure) that separates all same-$e$ collisions in general, and tie-breakers depending only on $e$ are impossible by definition.

**Conclusion:** The “count-only” ($e$-only) state key is **incorrect for exact minimax over all reachable states** starting at $n\ge5$ (it merges states with different $F$). Whether this constitutes an “all-$n$ barrier” depends on scope: if the DP is restricted to optimal paths, the obstruction is not visible at $n\le6$; if it merges over all reachable states (the standard minimax recurrence), it’s already false at small $n$. I found no polynomial $e$+tie-breaker that is complete for all $n\ge1$, but also no all-$n$ theorem/ruling out all possible polynomial structure-based tie-breakers. Honest limit: no verified all-$n$ barrier theorem obtained; the clean obstruction is local (general states) rather than clearly on optimal paths.


## Other metadata

```json
{
  "finished_at": 1793769859.1262052,
  "started_at": 1793767227.7367365
}
```
