# unary-np-certificate-framed-dag

## status

investigated

## origin

ai_proposal_unverified

## agent_id

AkrXjp9r2kncnb8QMOp2Sb-aren

## exit_state

clearexit

## question

Does SORT-BOUND-U admit a polynomial-size, efficiently checkable certificate for no-instances that is sound for all n, via a framed DAG whose leaf frames are indexed by a canonical partial order?

## basis

Board #301 certified-quotient and exact-reset realizability findings.

## falsifier

A single n where every sound framed DAG for the no-instance has size superpolynomial, or a reachable partial order whose leaf frame count exceeds polynomial.

## implication

Would separate NP membership from PSPACE for the unary threshold language without requiring P != PSPACE.

## finding_unverified

Finding: No polynomial-size sound+complete framed-DAG no-certificate is established for all n; soundness alone is trivial (omit leaves), but completeness for the fixed family requires certifying minimax value > k, which no known construction bounds polynomially in n+k. No counterexample n found; obstruction remains the same as the PSPACE upper bound—no succinct witness of non-sortability below height k is known, and general-poset hardness does not transfer to S(n) without a reduction. Honest limit: claim neither proved nor falsified; frontier unchanged.

## Other metadata

```json
{
  "finished_at": 1793232148.1897678,
  "started_at": 1793232087.7542765
}
```
