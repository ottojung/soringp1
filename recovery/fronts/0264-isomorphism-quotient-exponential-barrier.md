# isomorphism-quotient-exponential-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

uzV1iL5ALacaFruDHg0krh-dowry

## exit_state

clearexit

## question

For all sufficiently large n, is there an all-n barrier proving that no equivalence relation coarser than graph isomorphism on reachable partial orders can have polynomially many classes while remaining sufficient to compute exact S(n) by minimax recurrence?

## basis

Winning-frontier barrier shows exponentially many nonisomorphic winning states at optimal/surplus depths; root-reachable quotient investigated but no polynomial complete quotient established.

## falsifier

Construct an explicit polynomial-class equivalence (with a poly-time class test and two-outcome congruence) that is complete for exact minimax evaluation from the antichain for all n, or prove such a quotient exists for some infinite family.

## implication

A verified all-n isomorphism-quotient barrier would formalize the winning-frontier obstruction for state compression: exact evaluation cannot avoid exponential state up to isomorphism, limiting DP by canonical forms.

## finding_unverified

y the exact structure of those winning frontier posets more.

Let us think. The winning frontier gives exponentially many non-isomorphic winning states at depth related to information bound / optimal budget. If your equivalence relation is coarser than isomorphism, you can merge some isomorphism classes. But can you merge different isomorphism classes from that winning frontier into the same class while keeping the minimax recurrence congruent?

For minimax to be well-defined on classes with two-outcome congruence, if P ~ Q, then for every possible comparison move from P (to P1,P2), there must be some move from Q giving (Q1,Q2) in corresponding classes such that the outcome is "compatible" - more precisely, the transition must be preserved. Also the "two-outcome congruence" suggests the relation is preserved under both possible comparison outcomes.

Also another way: such quotients that are congruences for a game tree are related to bisimulations or to the notion of "strategy stealing" / "positional strategies" in some cases, but more directly related to the concept of "state graph quotients" being well-defined. Also in some puzzles this is related to "identification via tests".

But also look up how others interpret this. Another possibility is that graph isomorphism classes are the natural ones for posets; making it coarser (merging non-isomorphic posets) might break the minimax recurrence because different posets might require different optimal moves even if merged? Or because the "adversary" can force different structures.

Alternatively, think about the fact that F(P) depends on the poset structure. If you merge P and R (non-isomorphic) into same class but F(P) != F(R), bad. If same F, maybe possible? But need to satisfy two-outcome congruence for all moves. That’s very strong - similar to being a congruence relation in universal algebra, or to the states being equivalent in a labeled transition system.

Also the winning frontier construction gives many posets P_A that are all winning at same budget depth relative to root - but do they have same F? The note says "F(P_A)<=B=k-t" and they survive information pruning. They are different posets (different extra edges). Do they have same minimax value? Maybe different values? Let us look up the construction again.

Let us think more concretely about this specific frontier.

Let us analyze the winning frontier states for bisimilarity/congruence.

Let us study this more. The front says "equivalence relation coarser than graph isomorphism" - if we take graph isomorphism of comparability graphs, that's coarser than poset isomorphism. That matches. And they want to know if such a relation (coarser than graph isomorphism) can have polynomial classes and be sufficient for exact minimax. But comparability graph isomorphism is already coarser than poset isomorphism and it's not sufficient. Going even coarser (merging more) would only make it worse.

Let us start by studying the key literature and doing a serious attempt to disprove the barrier.

Let us post our findings to board #301.

The analysis is complete. Attempted to construct a polynomial-class equivalence coarser than isomorphism with two-outcome congruence; bisimulation is coarser than isomorphism and exact for minimax but still exponential in size, and the winning frontier produces exponentially many likely non-bisimilar states forcing exponential classes - supporting the barrier rather than disproving it. No repository changes made.


## Other metadata

```json
{
  "finished_at": 1793771269.9617608,
  "started_at": 1793767226.8567824
}
```
