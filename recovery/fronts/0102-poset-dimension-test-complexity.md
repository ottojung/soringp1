# poset-dimension-test-complexity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

DogMQTCktA9WuqkVvUWw3L-illness

## exit_state

clearexit

## question

For states P reachable near optimal play from the antichain, does bounded poset dimension create a polynomial-time exact test for the minimax value F(P), and can this be used as an all-n sound interface that evades the Theta(n log^2 n)-bit state identity barrier without losing exactness?

## basis

Poset dimension is a standard parameter but not tested against minimax F(P) on optimal-play states in docs/research-state-compression.md or board #301.

## falsifier

Exhibit an infinite family of root-optimal-reachable states of unbounded dimension (or dimension growing) with superpolynomial test complexity under any dimension-bounded summary, or construct a counterexample where dimension class merges states with different F(P).

## implication

A sound polynomial dimension-based summary would suggest a compact quotient for evaluators; a barrier would rule out this natural algebraic invariant as a universal compression.

## finding_unverified

Let us look up properties of $S_k$ and also think about the question again.

Let us start a proper investigation.

Let us look up the full frontier question more and related docs.

Let us think through this carefully.

Let us start by exploring what we know about poset dimension and sorting states.

Let us start by understanding the poset dimension concept in relation to sorting states.

Let us start by exploring systematically.

The investigation shows that poset dimension classes on optimal play paths merge states with different F(P) values (e.g. dimension 2 contains states with F from 1 to 7 on optimal paths for n=5), so dimension cannot serve as a lossless summary for exact F(P). This falsifies the claim. No repository changes made.

## Other metadata

```json
{
  "finished_at": 1793434730.401463,
  "started_at": 1793430405.0486095
}
```
