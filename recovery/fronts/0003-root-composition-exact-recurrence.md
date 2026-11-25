# root-composition-exact-recurrence

## status

investigated

## origin

reviewed_seed

## agent_id

OchERapJ6Ncb667p8f9GhX-radiantly

## exit_state

succeeded

## question

Seek a compositional exact recurrence for optimal sorting from chain or ordinal-product interfaces that preserves the adversarial root and both sibling branches, not merely the post-transcript minimax F(P).

## basis

docs/problem.md, established root-prefix sibling obstruction and prior failed naive direct-sum transfer in the research ledger.

## falsifier

Supply a small but extensible family in which all candidate interface summaries agree but the exact antichain root optimum differs, or show an explicit sibling-incompatibility obstruction.

## implication

A uniform polynomial-state exact root recurrence would improve the time bound for computing S(n) and perhaps place SORT-BOUND-U in P.

## finding_unverified

**Result: a candidate local-interface summary fails for correlated transcript sets, but I found no root-level counterexample or recurrence.**

I tested a summary that keeps each block’s feasible local orders and exact local comparison/budget profile, but forgets how the blocks are correlated. For blocks \(A=\{0,1\}\) and \(B=\{2,3\}\), let \(X=\{0123,1032\}\). Each block’s projection has both possible orders, with local value 1 and a 1/1 split. Yet the joint value is 1: comparing 0 and 1 also determines the order in \(B\). For the independent product \(Y=L(A)\times L(B)\), the same local summaries have joint value 2, by deterministic direct-sum.

This is a concrete **deduction** that separate local profiles lose cross-block correlation and cannot compose correctly for arbitrary transcript subsets. Jain–Klauck–Sántha’s direct-sum theorem applies to the independent product case; it does not justify composition under arbitrary cross-block comparisons.

**Limit:** \(X\) is not shown to be the linear extensions of a poset reachable from the antichain root. So this does not establish a sibling-incompatibility obstruction for the root recurrence, a complexity improvement, or a result about certificate completeness. The antichain-root question remains open.

I posted the scoped finding to Antonina **#301**. No repository or Lean changes were made.

## Other metadata

```json
{
  "failure_kind": "transient_backend_unavailable",
  "finished_at": 1792795805.4304683,
  "launch_error": "antonina: agent OchERapJ6Ncb667p8f9GhX-radiantly is still running; use --steer to redirect it\n",
  "retry_after": 0,
  "started_at": 1792795713.3093727,
  "transient_failures": 7
}
```
