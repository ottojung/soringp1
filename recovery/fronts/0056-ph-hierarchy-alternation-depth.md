# ph-hierarchy-alternation-depth

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ZQMHYDs6rMtpG8j0SY3jYQ-malleolus

## exit_state

clearexit

## question

For unary SORT-BOUND-U, does every polynomial-time alternating Turing machine deciding it require alternation depth omega(log N) on infinitely many input lengths N, or is there a fixed constant k with SORT-BOUND-U in Sigma_k^P union Pi_k^P?

## basis

ATM gives O(k*n^2) steps with 2*O(k) alternations on unary inputs (Claim A); no published result fixes alternation depth to constant level despite PSPACE membership.

## falsifier

Either construct a Sigma_k^P machine for fixed k deciding all large inputs, or prove an all-n alternation lower bound exceeding any fixed k for the natural game (contradicting fixed-level PH membership).

## implication

A fixed-level PH membership would imply PH != PSPACE; conversely a superconstant alternation lower bound would be strong evidence against PH collapse relative to PSPACE and separate from NP/coNP boundaries.

## finding_unverified

 intermediate class.

But the question as posed is very specific about alternation depth / fixed level of PH. Let us think of the structure again. For the ATM of Claim A with polynomially many rounds, you need polynomial alternations. To get into fixed level of PH, you need to be able to do it with a constant number of alternation blocks. Is there a known method to compute the sorting number with bounded alternation?

Alternatively, consider the following: you can do a binary search on k (the budget) - is SORT-BOUND-U in NP if we have a good certificate? If we can verify "S(n) ≤ k" in polynomial time with some witness, then yes. Or if we can do it with constant alternation, that gives Σ_k^P.

Alternatively, is there a polynomial-size certificate for S(n) ≤ k? Claim C says "No polynomial-size certificate is known for either S(n) ≤ k or S(n) > k" and "The tree witness is not polynomial". But "not known" doesn't mean it doesn't exist. And membership in NP would mean there IS some polynomial-size certificate.

Similarly for coNP. The question is asking if it's in some fixed level of PH (so NP, coNP, Σ_2^P, etc.). That is a very strong structure question.
Let us start by exploring the alternation structure more deeply and looking up what is known.

Let us start by systematically examining the evidence.

Let us start by exploring the question systematically.

I studied AGENTS.md, docs/problem.md, the board #301 context, and the primary complexity literature in the repo (certificates/barriers/encoding/hardness/winning frontier). 

**Question:** For unary SORT-BOUND-U, does every polynomial-time ATM need alternation depth ω(log N), or is there fixed k with SORT-BOUND-U ∈ Σ_k^P ∪ Π_k^P (PH)?

**Findings:**
- Natural game G(n,k): sorter (∃) picks pairs, adversary (∀) chooses directions, k rounds ⇒ ~2k alternations. For unary informative inputs k = Θ(n log n), N = n+k+1 so alternations are Θ(N) (polynomial). Claim A gives SORT-BOUND-U ∈ PSPACE via this ATM.
- Barriers: SORT-BOUND-U is sparse and not EXPTIME-hard (hence not PSPACE-hard) under many-one reductions (Berman–Hartmanis/Mahaney). In P/log nonuniformly. GEN-SORT PSPACE-completeness is open.
- Certificates: merge sort admits polynomial framed certificates for its bound; optimal S(n)-strategies have no known polynomial certificate. Framed DAGs use intersection/meet which loses disjunctive correlations (obstruction for some adaptive strategies); winning frontier shows exponentially many winning states but compression not obviously ruled out. NP/coNP membership open.
- Alternation: If fixed-level PH membership holds, that's fixed alternations (good). If polynomial alternations are necessary for the natural game and no compression exists, that would place it outside PH but inside PSPACE (if PSPACE-hard under stronger reductions) or just in PSPACE without PH collapse - but no lower bound is known.

**Conclusion (honest):** Genuinely open. The move-by-move game gives polynomial alternations; fixed alternation would require a succinct compressed strategy with no known obstruction-evading representation, while fixed-level PH is not obviously ruled out by sparsity/barriers. No all-n theorem or counterexample is established here. No Lean/repo changes made (no substantive independently checkable new result). The decisive next step would be either a polynomial certificate system for optimal sorting (proving PH membership) or a game-theoretic alternation lower bound (disproving it). Neither is achieved.

## Other metadata

```json
{
  "finished_at": 1793371238.7373805,
  "started_at": 1793365314.6284888
}
```
