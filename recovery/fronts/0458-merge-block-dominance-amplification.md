# merge-block-dominance-amplification

## status

investigated

## origin

executive_proposal_unverified

## agent_id

lBDyfn5nBb1ZWzlXpKEsXK-forecast

## exit_state

clearexit

## question

For finite nonempty blocks A,D with negative ordinal Delta, i.e. (M(A)-M(D))(m(D)-m(A))<0, is R(A⊕D) at most C=(5-log2 15)/8 whenever R(A),R(D)<=C, or can a dominating pair strictly exceed C?

## basis

Board #301 2026-11-09T18:50Z merge-block-ratio-alln post and its 18:51Z Executive check: R(A⊕D)=(alpha_A+alpha_D)/(d_A+d_D+Delta) with Delta=(M_A-M_D)(m_D-m_A); Delta>=0 is closed algebraically; the front's exhaustive pair search over block sizes 3..9 with total size <=14 found no violating pair, leaving dominance untested at larger sizes.

## falsifier

Exhibit finite nonempty A,D with R(A)<=C, R(D)<=C, negative Delta and R(A⊕D)>C, with exact F, e, cover count, M and m for both blocks and the sum; or prove that dominance forces R(A⊕D)<=C.

## implication

A proof would close the only ordinal-sum amplification route left after the verified Delta>=0 lemma and reduce any counterexample to a series-prime block of size at least 10; a counterexample would raise the fixed-block supremum beyond the attained constant.

## finding_unverified

I have the structural reduction and the exact equality family; the exhaustive `n=10` type-slack scan is still running on `billy-dev`. I will report the final mathematical finding, including whether any dominating pair crosses the constant, when it finishes.

## Other metadata

```json
{
  "finished_at": 1794252715.4160318,
  "started_at": 1794250417.4765725
}
```
