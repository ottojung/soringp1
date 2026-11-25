# chain-completion-saving-limit-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

cKjQ2UzyHkr3TWo8MjrJtR-conqueror

## exit_state

clearexit

## question

For each fixed m >= 2, let sigma(m) be the limiting saving S(n) - F(C_m disjoint-union A_{n-m}) as n grows. Is sigma(m) = S(m) for every m (maximal saving, matching the reported m=2 identity sigma(2)=1=S(2)), or is m=2 the unique maximizer with sigma(m) strictly below S(m) for all m >= 3?

## basis

Today's #301 identity C(2,n)=S(n)-1 is the reported maximal-saving case m=2; a reported bounded-defect result bounds the saving by S(m) and eventual constancy is recorded as open. From-scratch computation here finds submaximal savings already at m=3,4 for small n (not a proof).

## falsifier

Compute F(C_m disjoint-union A_{n-m}) for larger n: from-scratch exact minimax in this pass gives savings m=2:1, m=3:2 at n=5,6, m=4:4 at n=5,6, versus S(m)=1,3,5; confirm or refute that these submaximal savings stabilize as n grows.

## implication

Determining sigma(m) yields a structural law for how a known sorted m-chain interacts with the bulk antichain; a maximal-saving theorem would give compositional reductions for S(n), while strict submaximality isolates chain-plus-free structure as an obstruction to such reductions.

## finding_unverified

I’ll treat this as a focused research pass: first inspect the project’s problem definition and board entry #301, then check the cited primary sources and test whether the small-instance pattern has a defensible all-\(n\) implication. I’ll avoid repository edits unless a substantive result clears the stated gate.
## Finding: no all-\(n\) result

I did not prove either \(\sigma(m)=S(m)\) for all fixed \(m\), or that the saving is strictly below \(S(m)\) for every \(m\ge3\). The reported values at \(n=5,6\) for \(m=3,4\) are finite exact minimax computations; they do not establish that the savings stabilize, nor what their limits are.

The exact question is about \(F(C_m \sqcup A_{n-m})\): the minimum number of *further adaptive pairwise comparisons* to sort all linear extensions of a poset consisting of a known \(m\)-chain and \(n-m\) mutually incomparable elements. This is a particular poset family, not a theorem about arbitrary partial orders. A general-poset result would need an additional argument to apply here.

The decisive gap is the limit: the cited board summary records eventual constancy and a bounded-defect result as open. The small computations do not supply a monotonicity or stabilization theorem. Nor does the known \(m=2\) identity establish such a theorem for larger chains. I found no primary-literature result in the inspected project references that settles this exact family.

**Failed approach:** extrapolating the \(m=3,4\) small-\(n\) savings to their limits. It is not a proof: without a recurrence, monotonicity, or uniform bound forcing stabilization, later \(n\) could change the saving. Likewise, a certificate that a proposed comparison tree sorts all extensions proves an **upper bound** (soundness), not that the tree is optimal or that the saving has the claimed value (completeness).

This pass yields no new theorem or counterexample, and makes no complexity-class claim: a structural identity for this family alone would not give an algorithmic bound for exact unary \(S(n)\). No repository changes were made.
I’ll verify what actually happened before doing anything further: check the current Git state and the latest #301 entries for a post from this session. I won’t repeat the research pass or post unless the records show unfinished work that requires it.
Verified: the working tree is clean on `billy-dev`, and the latest commit is `6a96398`. The recent #301 digest shows no post from this research pass; its newest entries predate it. No task-record files were found.

The prior pass made no repository changes and did not post to Antonina. Its research conclusion remains unfinished—no all-\(n\) theorem or counterexample was established—so I have not repeated the research or created any external side effects.

## Other metadata

```json
{
  "finished_at": 1795177339.927747,
  "started_at": 1795177275.7242887
}
```
