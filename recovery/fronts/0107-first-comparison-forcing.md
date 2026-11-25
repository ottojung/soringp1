# first-comparison-forcing

## status

investigated

## origin

ai_proposal_unverified

## agent_id

nqXgIKMR2pYsqNw8ZJxCUe-studies

## exit_state

clearexit

## question

Is there an infinite family of n such that every optimal strategy for sorting n elements must begin with a comparison of the same 'type' up to relabeling, or is the first move always free?

## basis

Minimax game structure is in scope; no existing front in the ledger investigates first-move uniqueness/forcing across all n. Bridges to state canonicalization without requiring NP-hardness.

## falsifier

Prove that for infinitely many n there are at least two non-isomorphic optimal first moves, or prove for all sufficiently large n the first move is unique up to relabeling.

## implication

Strong symmetry/uniqueness of optimal minimax strategies would constrain the state space structure; lack of uniqueness would mean the strategy space remains rich and harder to canonically compress.

## finding_unverified

or all large n (contradicting "always free").

#### Mathematical analysis (paper deduction)
Model: minimax F on posets, S(n)=F(antichain P0^n). Optimal strategy = decision tree of height S(n).

- Initial state P0^n is the empty partial order on labelled elements; Aut(P0^n)=S_n acts transitively on all unordered pairs.
- For any two pairs e1=(x,y), e2=(z,w), there is g in S_n with g(e1)=e2, hence g maps state P0^n union {x<y} to P0^n union {z<w} isomorphically. Only 1 isomorphism class of first-move results.
- F depends only on isomorphism class of state: S(n)=1 + max(F(Q_n), F(Q_n))=1+F(Q_n) where Q_n is that class, regardless of which pair chosen. Therefore *every* possible first pairwise comparison appears in some optimal strategy, and all first moves are pairwise-isomorphic up to relabeling.

Thus for all n>=2: exactly 1 isomorphism class of first moves total (and a fortiori of optimal first moves). Clause (b) is true for all sufficiently large n (all n>=2). Clause (a) is false for all n>=2.

#### Distinction (posets vs S(n), soundness/completeness)
- General poset minimax can have non-isomorphic optimal moves from asymmetric posets (this is standard). The nontriviality fails here because the root is the fully symmetric antichain (the sorting "root" class). No reduction from arbitrary posets is needed or implicated.
- "Certificate soundness vs completeness": irrelevant to trivial symmetry of the move type; a certificate for S(n) is not the same as forcing a first comparison.
- State canonicalization: the symmetry is exactly what hash-consing/quotienting by isomorphism exploits at root (trivial). No compression constraint is removed by "freedom" here - freedom is only relabeling freedom which is already identified.

#### Failed approaches / obstructions
1. Tried to find any n where pair types differ - impossible by S_n transitivity. No experiment could create different pair types.
2. Considered "type" as imbalance/strategy shape after first move - the question states "begin with a comparison of the same 'type' up to relabeling"; "begin with a comparison" means the first comparison action/type, not downstream. Shifting to downstream is not the falsifier as stated.
3. Looked for literature mentions of forced first moves in optimal sorting trees - known optimal trees differ, but first move is always a pair (isomorphic). No source claims non-isomorphic first move types exist; symmetry is trivial.

#### Honest limits
- This is a basic symmetry fact, not a deep theorem. It does not affect the uniform complexity of S(n) directly.
- The complexity implication given ("strategy space remains rich and harder to canonically compress") is the opposite of what holds at root (root is maximally symmetric). Richness appears later at asymmetric poset classes, not at the first move.
- No new theorem/counterexample to add to repo; no Lean change warranted. The claim is essentially decided by symmetry.

#### Conclusion
For all n>=2 the first move is unique up to relabeling (all pairs isomorphic). The "always free" in the sense of choosing different move-types does not occur; freedom is only labeling. Clause (b) of the falsifier holds for all n>=2. No infinite family with non-isomorphic optimal first moves exists. This is a deduction from symmetry of the antichain, not from experiment. The front as stated has trivial answer; the interesting question would be about non-root states or about some other notion of "type". No obstruction found except triviality.

## Other metadata

```json
{
  "finished_at": 1793442385.6887856,
  "started_at": 1793441858.7982564
}
```
