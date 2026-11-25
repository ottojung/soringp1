# exact-reset-divisibility-characterize

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Xv6dRSAgwyCZpqqxkJ5yu8-rascals

## exit_state

clearexit

## question

For all n>=3, characterize exactly which poset pairs (P,Q) with P reachable from A_n and Ext(Q) a uniform class partition of Ext(P) admit an exact-reset comparison stage, and determine whether the odd-antichain-to-star branch-divisibility obstruction is the only all-n obstruction to some polynomial exact-reset system.

## basis

Exact-reset realizability proof for odd n antichain-to-star (docs/research-exact-reset-realizability.md); branch divisibility is a necessary condition distinct from isomorphism and from extension-count totals.

## falsifier

Exhibit an infinite family of (P_n,Q_n) with no comparison-root divisibility obstruction and no other obvious obstruction that is provably not realizable as an exact comparison stage, or conversely prove a general theorem covering the odd-split case and all others.

## implication

A complete characterization would show whether the extension-count framing can ever achieve exact resets beyond trivial cases or whether branch divisibility forces superpolynomial certificate overhead for any complete exact-reset system.

## finding_unverified

Let us proceed systematically.

Let us understand this better. Let us think about the general condition.

Let us start by exploring the poset/extension structure more carefully and understanding the full model.

Let us first understand the model deeply.

Let us understand the problem more deeply and search primary literature concepts.

Let us understand the problem better.

Let us think systematically and try to construct an obstruction or find one.

**Mathematical finding (billy-dev, no repo/Lean changes):** For exact-reset stages (partition of Ext(F) into classes of size e(F') isomorphic to Ext(F') up to framing), recursive branch divisibility is necessary but not sufficient. The odd-antichain-to-star case gives a root branch-divisibility obstruction for all odd n≥3 (e(A_n)/(2e(V_n))=n/2 not int). Beyond root divisibility there are strategy/structural obstructions: e.g. A_4 can reach via branch-divisible splits a chain+isolated state with e = e(diamond) not isomorphic to diamond with no further branch-divisible path to a diamond partition (admissible splits + recursive constraints fail). No obvious infinite family of other root-branch-divisibility all-n obstructions appears from factorial/poset-count constraints; strategy obstructions seem local rather than forming a universal all-n family. Characterization likely requires recursive branch-divisibility plus admissible-comparison constraints and "refinability"/shellability-like conditions; the odd-star case appears to be the canonical all-n branch-divisibility obstruction of this type. Honest limits: full characterization and polynomial-exact-reset-system implications remain open.


## Other metadata

```json
{
  "finished_at": 1793734898.5321393,
  "started_at": 1793729826.2657464
}
```
