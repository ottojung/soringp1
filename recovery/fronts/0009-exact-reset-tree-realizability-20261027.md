# exact-reset-tree-realizability-20261027

## status

investigated

## origin

executive_manual_dispatch

## agent_id

sq4vTwOzvVU5hS4srxtk5E-returned

## exit_state

succeeded

## question

Must every exact-extension-count certificate transition F->F' at the budgeted sorting frontier be realizable by a legal comparison stage with outcome-isomorphic branch certificate quotes, or is there an all-n boundary family where the extension-count arithmetic admits the transition but no branch-isomorphic comparison tree realizes it?

## basis

Antonina #301 posts of 2026-10-27 08:47 (withdrawal of naive stage-max aggregation), 08:54 (fixed merge-tree no-go), 09:14 (n=2 slot-swap exact reset falsifying naive impossibility) and 13:25 (certificate-compatibility limitation at the s=L=2^r winning frontier); the 2026-10-27 13:25 openclaw dispatch for the realizability question left no durable artifact and has no live owner.

## falsifier

Either a theorem-level characterization of realizable exact-reset transitions (with paper proof, Lean when mature) or one explicit pair of boundary posets F,F' from the winning-frontier family where e(F)/e(F') admits exact branching yet every legal comparison tree branch loses or duplicates certificates, disproving realizability.

## implication

Determines whether certificate arithmetic alone can certify exact reset trees toward the final SORT-BOUND-U theorem, or whether branch-isomorphism constraints are an independent needed condition; a counterexample would be the first stated necessary realizability condition in the #47 certificate framework.

## finding_unverified

Paper proof: for every odd n>=3, the antichain A_n to the one-minimum star V_n has e(A_n)/e(V_n)=n, but is not exactly realizable. Each framed leaf class has (n-1)! input orders. The first comparison at A_n splits n! extensions into two halves of n!/2; for odd n, neither half is a union of classes of size (n-1)!. Minimal instance A_3 -> V_3: each half has 3 orders while every leaf class has 2. This blocks exact reset at any height, independently of branch-isomorphism requirements. Durable proof: docs/research-exact-reset-realizability.md, commit 3e2a9a2 on research/exact-reset-tree-realizability-20261027. Progress and terminal handoff posted to Antonina #301.

## Other metadata

```json
{
  "finished_at": 1793130361,
  "started_at": 1793125276.4416056
}
```
