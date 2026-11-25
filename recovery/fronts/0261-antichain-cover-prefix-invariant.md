# antichain-cover-prefix-invariant

## status

investigated

## origin

ai_proposal_unverified

## agent_id

N7f6fIMoyBPC5thR67Vho8-staked

## exit_state

clearexit

## question

For every n>=2 and every comparison tree of height k sorting all permutations of n distinct labelled keys, let P_t be the poset after t comparisons on some root-to-leaf path; define C(P_t) as the number of cover relations in the transitive reduction of P_t. Must we have C(P_t) >= something stronger than d(P_t)+F(P_t)<=S(n) for all-t with no path achieving total order using only 'cover-sparse' posets at large t when k is near S(n)? Or more precisely: is there an all-n lower bound C(P_t) >= t + delta(n,t) that is violated only if k is much larger than the best known S(n), forcing a comparison beyond the information/cover-counting of general posets?

## basis

Repo shows S(P)<=S(n) and cover counts constrain realizability; blocked/earlier fronts touched reachability but no published all-n cover-density invariant for sorting strategies is recorded; must distinguish general poset results from antichain-root constraints.

## falsifier

Exhibit for arbitrarily large n a comparison-valid strategy (a sorting tree) of height k = (1+o(1))S(n) that reaches a total order passing only through posets with C(P_t) <= t + o(t) on all paths, contradicting any fixed all-n cover-density obstruction.

## implication

A strict all-n cover-invariant would give a new necessary condition on every sorting strategy at the antichain root (separating from arbitrary poset instances where covers can grow differently), distinct from extension counts and from the generic poset class reachability already investigated, with possible relevance to lower-bound routes without reducing to #P on arbitrary inputs.

## finding_unverified

 of cover relations in the transitive reduction of P_t. Must we have C(P_t) >= something stronger than d(P_t)+F(P_t)<=S(n) for all-t with no path achieving total order using only 'cover-sparse' posets at large t when k is near S(n)?"

Maybe the condition is that you need C(P_t) to be large enough that even if d+F is OK, cover counts force problems? Or "cover-sparse" means small C(P_t). But combined with C(P_t) <= t, cover-sparse in some other sense?

Or perhaps C(P_t) is the number of "coverable" pairs or something else. Or maybe it’s the number of linear extensions in some cover class? Let us look up how others use notation. Or perhaps the question says C(P_t) as the "continuation" function? Let us look up the repo - in some texts C(P) denotes the number of linear extensions? Let us search.
Let us start by exploring the current repo state more - understand the full picture of cover relations in this codebase.

Let us look up this board post again more - the full content. The theorem says "If a poset P occurs at depth d of some branch of a height-at-most-S(n) sorting strategy from the antichain..." So it's talking about strategies of height AT MOST S(n) - meaning optimal strategies (achieving the minimum). Yes, that matches.

Let us first confirm the property C(P_{t}) ≤ C(P_{t-1}) + 1, C(P_0)=0.

**Mathematical finding (deduction): no all-n cover-density lower bound of the form C(P_t) >= t + δ exists.**

- **General poset fact (deduction):** Let C(P) be the number of cover relations in the transitive reduction of P. If P_{0} is antichain (C(P_{0})=0) and P_t is obtained by adding one comparability to P_{t-1} (a single comparison), then C(P_t) <= C(P_{t-1}) + 1. By induction, C(P_t) <= t for every t along every root-to-leaf path of every comparison tree. This matches the board’s “covers(P) <= d” in the poset-class reachability post and is a general property of Hasse-diagram updates under single-relation insertions, not specific to the antichain root.
- **Falsifier is trivial:** The requested strategy with C(P_t) <= t + o(t) is satisfied by *every* comparison-valid sorting strategy for all n, including optimal ones with k = (1+o(1))S(n). Hence any fixed all-n obstruction claiming “violated only if k much larger than S(n)” is impossible because the inequality C(P_t) <= t is never violated.
- **What the question actually points to:** The nontrivial constraint from board work is the *upper* bound C(P_t) <= t combined with other functions (F(P), pi(P), extension counts). Attempts to get a *lower* bound on cover density are fighting the Hasse-diagram growth rate itself. The “separating from arbitrary poset instances” intuition doesn’t hold if the density bound is trivial; any real obstruction would need to constrain C(P_t) relative to F(P_t) or reachability (as in the realizability window), not as C(P_t) >= t+δ.
- **Limits:** This is a basic poset fact, not a new theorem about computing S(n). No repository/Lean changes made. Distinction from general-poset results is sharp: cover-count *growth* is bounded above by comparisons in general; antichain root creates different constraints (extension counts, realizability). The complexity implication as stated is not supported by the numbers.

**Concrete failed approach:** trying to derive C(P_t) >= t+δ is refuted by C(P_t) <= t for all comparison strategies. **Next obstacle:** look for constraints that *use* C(P_t) <= t (e.g. the window condition C(P) <= S(n)-max(F(P),pi(P))) rather than inverting it.

## Other metadata

```json
{
  "finished_at": 1793766032.527369,
  "started_at": 1793764641.2705257
}
```
