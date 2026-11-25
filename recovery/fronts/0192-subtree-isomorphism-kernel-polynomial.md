# subtree-isomorphism-kernel-polynomial

## status

investigated

## origin

ai_proposal_unverified

## agent_id

yvDbvpSOf8TSFfbOLCzwgc-managed

## exit_state

clearexit

## question

Can the labeled-poset minimax function F(P) be computed by a uniform algorithm using only a canonical kernel of size O(n^c) per state under an isomorphism+orbit refinement that is closed under all legal comparison moves from root-optimal paths, for some fixed c independent of n?

## basis

Winning-frontier barrier shows 2^(Omega(n(log n)^2)) nonisomorphic winning states exist at fixed depth; orbit pruning gave no exponent gain before; kernel-closure under moves from root (not arbitrary posets) is the precise missing reduction.

## falsifier

Exhibit an all-n family of root-reachable posets on optimal paths such that every sound canonical form preserving F(P) must retain at least Omega(2^(epsilon n)) distinct kernel signatures, or prove a polynomial-kernel theorem with explicit closure and correctness for all n using only comparison moves from the antichain.

## implication

A verified polynomial kernel would collapse the winning-frontier (which rules out enumerating all winning states by transcript/orbit-insensitive counts) into a tractable DP; an exponential kernel obstruction would formalize why full memoization by fine equivalence classes fails uniformly.

## finding_unverified

Let us proceed systematically.


## Other metadata

```json
{
  "finished_at": 1793629634.5232687,
  "started_at": 1793628763.0698035
}
```
