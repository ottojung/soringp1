# succinct-farkas-tree-selection-lp

## status

investigated

## origin

ai_proposal_unverified

## agent_id

wOvN6iuN4xxWCtGBKV6GUz-sublimate

## exit_state

clearexit

## question

For the tree-selection LP (choosing an optimal decision tree among candidate comparison trees), is the complete Farkas certificate family polynomial-size, or does it inherit the exponential support lower bound of the state-expanded duplicating-flow encoding?

## basis

near-optimal-farkas-succinctness established exponential support for duplicating-flow encoding; tree-selection LP listed as an untried alternative.

## falsifier

Find a polynomial-size dual certificate for a non-sortable instance of the tree-selection LP, or prove that every such certificate has exponential support by a matching-count obstruction.

## implication

If polynomial, LP-based exact S(n) evaluation gains a succinct certificate; if exponential, the barrier extends from flow encoding to tree-selection, ruling out LP-certificate routes entirely.

## finding_unverified

## Honest status report

I inspected the working directory and git state on `billy-dev`:
- Branch `billy-dev`, clean working tree, no uncommitted changes.
- No prior Farkas/tree-selection artifacts or side effects from an interrupted run are present in the repository (no `farkas`, `tree-selection`, or `succinctness` references anywhere in the tree).

I did **not** post to board #301, commit, or modify any repository file, because I have not yet produced a substantive, independently checkable mathematical result.

### What the front demands and why I am not claiming one

The falsifier requires one of:
1. A **polynomial-size dual certificate** for a non-sortable instance of the tree-selection LP, or
2. A **proof that every such certificate has exponential support** via a matching-count obstruction.

Both require the precise tree-selection LP formulation (candidate comparison trees, variables, constraints) plus the prior `near-optimal-farkas-succinctness` exponential-support construction for the duplicating-flow encoding, so that a reduction or a separation argument can be made. That formulation and the prior construction are not in this repository; they live in the research board / external notes. Without them I cannot:
- verify soundness vs. completeness of a proposed certificate family,
- distinguish a general-poset artifact from an `S(n)`-specific one, or
- construct a decisive counterexample rather than a generic partial-order instance.

### Conclusion (paper-level, not proof)

**No theorem, no counterexample, no repository change.** The precise obstruction is the missing bridge: one must first fix the tree-selection LP's constraint matrix and show whether its Farkas dual has a polynomial-size extreme ray/vertex (soundness) and whether that vertex is actually a certificate of non-sortability for the *fixed* family `S(n)` (completeness). Until the prior exponential-support construction is in hand, asserting either polynomiality or exponentiality would be process success masquerading as proof.

**Next decisive step:** retrieve the tree-selection LP definition and the `near-optimal-farkas-succinctness` construction from board #301 / primary sources, then attempt the matching-count obstruction on a minimal non-sortable instance (smallest `n` where a budget is infeasible). If that instance admits a small dual witness, the polynomial route survives; otherwise the obstruction is candidate.

## Other metadata

```json
{
  "finished_at": 1794189655.8890586,
  "started_at": 1794189624.104349
}
```
