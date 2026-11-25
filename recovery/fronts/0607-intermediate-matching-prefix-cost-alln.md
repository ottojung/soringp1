# intermediate-matching-prefix-cost-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

3TxLOR9zl1nnMLJEWTkabZ-soften

## exit_state

clearexit

## question

For every n >= 2 and every 1 <= k <= floor(n/2), is the exact minimax value F(k disjoint 2-chains disjoint-union A_{n-2k}) equal to S(n) - k, i.e. can any k pairwise-disjoint opening comparisons always be front-loaded at cost exactly k, not only at the full matching prefix k = floor(n/2)?

## basis

Today's #301 post reports an all-n identity C(2,n)=S(n)-1 (paper-level), the k=1 case; the matching-prefix normal form is reported open from n=23. From-scratch exact minimax (this pass) confirms equality for all n<=6 and every k, which supports but cannot prove the all-n claim.

## falsifier

A from-scratch exact minimax computation finding any n,k with F(k*C2 disjoint-union A_{n-2k}) != S(n)-k, or showing the value depends on k non-linearly; today's reported identity C(2,n)=S(n)-1 supplies only the k=1 base case and does not settle intermediate k.

## implication

A uniform equality would give a prefix-front-loading normal form reducing S(n) to intermediate matching-prefix families and opening a faster exact evaluator; a counterexample at some intermediate k would also refute the reported full matching-prefix normal form at that n.

## finding_unverified

I’ll first verify this is the designated `billy-dev` environment and inspect the specified contract/problem/board entry, then pursue the intermediate-prefix claim against the primary literature and existing computation without modifying the repository.
**No new theorem or counterexample found.** The proposed equality remains unresolved beyond the reported small cases and the `k=1` identity.

For the exact adaptive minimax value `F(P)`, there is a simple lower bound:
\[
F(kC_2 \sqcup A_{n-2k}) \ge S(n)-k.
\]
Compare the `k` disjoint pairs first, in `k` comparisons. Whichever outcomes occur, the remaining state is isomorphic to the stated matching-prefix poset. Completing its optimal strategy would sort all inputs, so `S(n) ≤ k + F`.

The hard direction is the matching upper bound. The `k=1` argument uses symmetry of an optimal root comparison; it does not establish that an optimal strategy can begin with an arbitrary prescribed set of `k` disjoint comparisons. I found no primary-literature result that supplies this step. Results about general poset minimax values would not suffice without a transfer to this specific family.

The equality would be a **completeness** claim about the prescribed prefix’s ability to attain the lower bound—not merely **soundness** of a strategy that sorts after opening those pairs. Neither the lower bound nor a certificate for one strategy proves that completeness claim.

The reported from-scratch computation through `n≤6` is supporting finite evidence, not an all-`n` argument. I did not extend it or find a falsifying instance. No repository changes, Lean work, or board post were warranted.

## Other metadata

```json
{
  "finished_at": 1795177339.8456447,
  "started_at": 1795177275.2925735
}
```
