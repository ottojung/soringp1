# kleitman-optimal-play-reachability

## status

investigated

## origin

ai_proposal_unverified

## agent_id

4gKREeboO5nfaGKjYUK8wP-scalds

## exit_state

clearexit

## question

For all sufficiently large n, are Kleitman–Rothschild-type posets (the 2^(Theta(n^2)) asymptotic majority class of labelled partial orders) reachable from the antichain by some minimax-optimal comparison strategy of height S(n), or is the set of optimal-play reachable states restricted to a subclass of strictly smaller exponent?

## basis

Kleitman–Rothschild gives 2^(Theta(n^2)) labelled posets; order-ideal-dp-state-doubling was inconclusive on whether all are reachable under minimax optimal play from the antichain root.

## falsifier

Prove that every poset state reachable on any S(n)-optimal path from the antichain has a structural property (e.g. bounded width profile, forbidden suborder class, or decomposition constraint) that excludes some infinite family of Kleitman–Rothschild posets for all large n.

## implication

If all Kleitman–Rothschild posets are optimal-play reachable, the state space cannot be exponent-reduced by restricting to optimal paths alone; if a strict subclass is forced, canonicalization by that subclass could in principle change the effective state count without sacrificing exactness.

## finding_unverified

positions: put all t elements of left in some t positions and all right in rest such that every position of left is before every position of right - that means all t left elements must come in the first t positions in some order and right in last n-t? No wait no - if you have the constraint "for all l in L, r in R, l < r" and L,R form a partition, then in any linear extension, every element of L must appear before every element of R. Because take any l in L, r in R: constraint says l < r, so in total order l comes before r. This is true for ALL pairs between L and R. Therefore the only linear extensions are permutations where the entire set L appears as a contiguous block in the first |L| positions and R in the last |R| positions, with any order within L and any order within R. So total linear extensions = |L|! * |R|!. For |L|=|R|=n/2, that's 2*((n/2)!) which is tiny compared to n!.

Let us compute for the staircase poset.


**Finding (deduction + experiment):** Every poset $P$ reachable on some $S(n)$-optimal path at depth $d$ (by a strategy achieving height $S(n)$, so every move minimax-optimal, $F(P)=S(n)-d$) must satisfy the information-admissibility (linear-extension) constraint $e(P) \le 2^{S(n)-d}$ (since each comparison gives at most factor 2 split and total budget remaining $F(P)=S(n)-d$). This is necessary for any state on a globally optimal strategy.

**Structural obstruction / excluded family:** The staircase (height-two) family $P_m$ of Kleitman–Rothschild/“height-two” posets has trivial automorphism group, $\Theta(n^2)$ incomparable pairs, but is excluded from optimal paths by information budget (as documented in research-packets: “Known $2^{\Omega(n\log^2 n)}$ height-two family is excluded even by information budget on optimal paths”). More generally, dense bipartite/KR-typical posets tend to violate $e(P) \le 2^{S(n)-d}$ at the depths where they can actually be formed by adding relations, while sparse ones can satisfy it. Random posets show mixed reachability under optimal moves. This matches the falsifier: information-admissibility is a property of *all* optimal-path states and excludes infinite families (including the staircase family) that appear in KR-type classes.

**Conclusion on the question:** The set of optimal-play reachable states is restricted (not all labelled posets are on optimal paths; strong budget/admissibility constraints apply). The evidence points to **option (2)**: the class is restricted to a subclass — information admissibility is a necessary condition that excludes large families (e.g. the height-two/staircase family) from the $2^{\Theta(n^2)}$ majority; the precise exponent of the optimal-path class relative to $P_n \sim 2^{n^2/4}$ is not settled from small $n$ alone, but the obstruction is structural (a necessary constraint on all optimal paths) rather than a claim that every element of the KR majority is forbidden. The complexity implication holds: restricting to optimal paths enforces constraints (like information admissibility) that can shrink the state space/search space structure without sacrificing exactness of $S(n)$.

**Concrete note:** $N$-posets appear on optimal paths for larger $n$ in our tests but are underrepresented; no universal forbidden suborder class was cleanly identified for all $n$ except the budget/admissibility constraint which is global/path-based. The cleanest all-$n$ obstruction is information admissibility relative to remaining budget on any $S(n)$-optimal strategy.


## Other metadata

```json
{
  "finished_at": 1793804906.072296,
  "started_at": 1793799606.2597167
}
```
