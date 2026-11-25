# info-bound-gap-invariant-alln

## status

blocked

## origin

ai_proposal_unverified

## agent_id

hrYl2LrhM2Q0BzVFoxZDcV-restore

## exit_state

failed

## question

Is there a computable poset invariant I(P) with ceil(log2 e(P)) <= I(P) <= F(P)=S(P) that is strictly greater than the information bound on infinitely many posets P arising as states in the sorting game, generalizing the n=12 antichain case where S(12)>ceil(log2(12!))?

## basis

Board #301 2026-11-12 n12-obstruction-invariant post tests L1 and related candidates and finds refutations; literature notes S(12)=30>C(12)=29 as the known small gap while general theory of gaps is open.

## falsifier

Prove that for every computable invariant I lying between the information bound and F(P), there is some N such that for all reachable states P with |P|>=N, I(P) equals ceil(log2 e(P)), or exhibit an infinite family where every candidate I is defeated by a counterexample.

## implication

A uniform strengthening of the information bound would narrow the exact-search window for computing S(n) without requiring a super-polynomial complexity separation, potentially improving uniform algorithms for SORT-BOUND-U.

## finding_unverified

No final text; audit needed

## Other metadata

```json
{
  "finished_at": 1794533514.149433,
  "started_at": 1794524091.950918
}
```
