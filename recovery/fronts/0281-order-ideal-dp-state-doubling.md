# order-ideal-dp-state-doubling

## status

investigated

## origin

ai_proposal_unverified

## agent_id

JGBIsRni0F6NDYOhSaX9i2-availing

## exit_state

clearexit

## question

For the poset DP over order ideals used to compute F(P)=S(P) (sometimes called the 'minimum path length' or 'poset game tree' DP), does the number of reachable order ideals grow as 2^(Omega(n^2)) for some infinite family reachable from the antichain under optimal play, forcing any memoization over all order ideals to be exponential even with isomorphism quotients removed?

## basis

The number of order ideals is equal to the number of linear extensions in some cases? No - order ideals in the poset of linear extensions? Or more directly, the 'state graph' of partial orders by adding order constraints relates to order ideals in the distributive lattice of order ideals of P; the DP over all subsets is exponential but the 'down-set' (order ideal) formulation gives states as order ideals of the current poset.

## falsifier

Find an infinite family reachable on optimal paths with O(2^(c n log n)) order ideals for fixed c or better, or show order-ideal state graphs can be compressed below 2^(Omega(n^2)) for all root-reachable families.

## implication

A proof of 2^(Omega(n^2)) order ideals on optimal paths would give a structural explanation for the exponential state count and constrain exact DP approaches without relying solely on linear extension counts.

## finding_unverified

atical fact - "the state graph of partial orders by adding order constraints relates to order ideals in the distributive lattice of order ideals of P". So starting from some P, adding order constraints gives larger (in some sense) partial orders. The set of all partial orders extending P forms an order ideal in some lattice? Or forms a distributive lattice isomorphic to J(Q) for some Q?

Alternatively, every finite distributive lattice is isomorphic to J(P) for a unique finite poset P. Also, the lattice of all order ideals of a poset is distributive. Maybe they're saying the state graph is related to order ideals of J(P) - getting into higher levels.

Alternatively, this could be referring to the fact that counting linear extensions or doing certain DP can be related to order polynomials and to order ideals. Or perhaps to the "zeta polynomial".

Alternatively, let us look up standard results about the complexity of computing S(n). The poset DP (also called "graph of states" or "minimax path length" in some puzzles, sometimes called "coin weighing" or more directly related to "identification via comparison") - another name is "the minimum comparison tree" and the state graph is the poset of partial orders under refinement. Also in some sources this is called the "poset game" or "sorting game".

Alternatively, maybe "order ideals" is being used to mean the "ideals" (maximal in some sense?) or perhaps it's a mistranslation. Or perhaps they mean "order types" or "order ideals" as in the states are ideals in the decision tree order?

Alternatively, let us look up the board #301 context again from the task more - the user says "study AGENTS.md, docs/problem.md and current board #301". Let us look up more of board #301 if possible? The digest showed recent messages, but maybe there's more specific discussion. Also let us look in the repo for any recent files or notes about this specific front.
Let us look up this front's mathematical content from first principles.

Let us search for "minimum path length" in combinatorics of sorting more specifically.

Let us write a precise analysis.

Let us proceed.

Let us start by exploring the codebase to understand the full picture of the poset DP.

Let us look up common results about state counts in sorting algorithms. Also the winning frontier barrier showed 2^((1/4-o(1)) n (log n)^2) states at a level - which is super-polynomial but smaller than 2^(n^2). The total poset states are 2^(Theta(n^2)). The question says "order ideals" specifically - maybe they mean something like "ideals" in the sense of "maximal elements" or perhaps it's referring to down-sets in a different context.

Reported honest limits and analyzed both interpretations. The most decisive mathematical point is that if "order ideals" means order ideals of the current poset P (linear-extensions-style DP), then N(P) ≤ 2^n and decreases as relations are added from the antichain, so it cannot grow as 2^(Ω(n^2)) - a direct contradiction of the claim. If "order ideals" instead means the poset states themselves (terminology misuse), then the question is about restricting to optimal-play paths with isomorphism quotients removed; Kleitman–Rothschild gives 2^(Θ(n^2)) for all posets and quotienting doesn't change exponent, but it's unclear whether all those states are actually reachable under minimax optimal play - this remains unresolved. No repo/Lean changes made as no substantive independently-checkable theorem or counterexample was established.

## Other metadata

```json
{
  "finished_at": 1793795397.0729384,
  "started_at": 1793789895.2924604
}
```
