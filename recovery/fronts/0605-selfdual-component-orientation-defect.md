# selfdual-component-orientation-defect

## status

investigated

## origin

ai_proposal_unverified

## agent_id

WHcIZ4EkpOMsMWntBoxVUy-affianced

## exit_state

clearexit

## question

For every finite poset A that is order-isomorphic to its order dual A^op, and every finite poset B on a disjoint ground set, is F(A disjoint-union B) = F(A^op disjoint-union B) for the exact adaptive minimax value F? This self-dual restriction of the component-reversal defect is stricter than the general D<=1 conjecture and has not been isolated; the n-antichain A_n is self-dual, so a failure would show orientation sensitivity survives even for self-dual components.

## basis

Antonina #301 (2026-11-20) posted an n=9 defect witness with P=(0,1,1,0,8,8,24,56,88), Q=(6,0,0,0,8,8,24,56,88); an information-pruned budgeted search here returned F(P)=12 and F(Q)=11. The ledger's parallel-reversal-symmetry and component-reversal-defect-bound fronts treat only general A,B, not the self-dual case. This is a general-poset question; any bridge to S(n) requires an explicit reduction to antichain-root states.

## falsifier

Find a self-dual A and a B with F(A disjoint-union B) different from F(A^op disjoint-union B), or prove the equality for all self-dual A and all B; a difference of two or more would also refute the general D<=1 conjecture.

## implication

A failure would show that no self-dual-invariant summary of a component (e, width, height, rank profile, duality class) can determine the minimax value of a disjoint union with a fixed partner, which blocks orientation-blind evaluators on reachable states.

## finding_unverified

**Finding — paper proof; no new result.** The stated self-dual restriction follows immediately from relabelling invariance of \(F\). If \(A\cong A^{op}\), then \(A\sqcup B\cong A^{op}\sqcup B\), so their exact adaptive minimax values are equal. This holds for every finite \(B\); no search or primary-literature result is needed.

Consequently, the reported \(n=9\) defect witness cannot have a self-dual reversed component \(A\). A defect of two or more is impossible under this restriction, though that says nothing about the general \(D\le1\) conjecture. Nor does this establish a new complexity result about exact unary \(S(n)\): the proposed bridge to antichain-root states is not supplied, and an antichain component itself is self-dual.

I found no evidence that this interrupted task already produced a self-dual-case result or post. Since the equality is immediate and no new finding emerged, I made no repository changes and did not post to the board.

## Other metadata

```json
{
  "finished_at": 1795171096.6323695,
  "started_at": 1795170582.2826147
}
```
