# sparse-pspace-ph-level

## status

investigated

## origin

ai_proposal_unverified

## agent_id

o07ZAabNZmJFfJUCHPIpFc-tribute

## exit_state

clearexit

## question

For the sparse unary language SORT-BOUND-U in PSPACE (by ATM alternation), is there a fixed level k of the polynomial hierarchy with SORT-BOUND-U in Sigma_k^P, or can it be shown to require arbitrarily high fixed alternation levels for all polynomial-time reductions from complete problems?

## basis

Claim A gives APTIME=PSPACE for SORT-BOUND-U; sparsity is established and gives P/poly; Karp-Lipton/Ogiwara-Watanabe give PH collapses for sparse NP/PH, but position of sparse PSPACE in PH is underexplored.

## falsifier

Construct a polynomial-time reduction from some QBF_k-complete language to SORT-BOUND-U for all fixed k, or prove SORT-BOUND-U in Sigma_k^P for some fixed k using its sparsity and the minimax game structure.

## implication

Pinning the PH level would clarify whether the alternating comparison game collapses below PSPACE or is a genuine sparse PSPACE instance, without relying on P/poly circuit lower bounds.

## finding_unverified

 number of alternations can be up to polynomial (equal to time for some constructions). But Σ_k^P is polynomial time with at most k alternations starting with existential.

So being in PSPACE (APTIME) means there is some polynomial time bound and some number of alternations (bounded by the time). It doesn't mean fixed k - it means polynomially many alternations. That matches - QBF with polynomially many alternations is PSPACE-complete.

So the question is: can we bound the number of alternations by a fixed constant k (independent of n,k) for SORT-BOUND-U? That would mean SORT-BOUND-U ∈ Σ_k^P ⊆ PH. Or do we need arbitrarily many alternations as function of input size, meaning it's outside every fixed level of PH (and since in PSPACE, this would mean PH != PSPACE)?

Also combined with sparsity - if it were in some fixed level of PH, that would create a contradiction with sparsity under some hardness assumptions? Or is there a collapse theorem?

Also the falsifier says "Construct a polynomial-time reduction from some QBF_k-complete language to SORT-BOUND-U for all fixed k" - that would mean SORT-BOUND-U is hard for every fixed level of PH, hence not contained in any fixed level (and also would mean PH ⊆ P^SORT-BOUND-U; but SORT-BOUND-U is sparse in PSPACE - combined maybe get collapses). Or "prove SORT-BOUND-U in Sigma_k^P for some fixed k using its sparsity and the minimax game structure."

Also Karp-Lipton is about NP ⊆ P/poly => PH collapse. Ogiwara-Watanabe is about sparse sets and bounded truth-table reductions giving collapses. Also for higher levels, if a Σ_k^P-hard set is sparse, maybe get collapses?

Or another fact: if a sparse language is in Σ_k^P, is there a collapse? Not obviously. Or if it's PSPACE-complete and sparse, maybe different story.
Let us start by examining the full picture more systematically.

Let us analyze this carefully.

Let us analyze this systematically.

**Mathematical finding (attempt to disprove PH-hardness):**

**Claim attacked:** SORT-BOUND-U is PH-hard (reduces QBF_k to it for all fixed k). 

**Structural obstruction (deduction):** The comparison game is ∃ (sorter picks incomparable pair) vs ∀ (adversary answers consistently with some total order), states are partial orders. Encoding arbitrary QBF_k (boolean formulas with k alternations) requires simulating arbitrary boolean constraints; the pairwise-comparison model + adversary constrained to linear extensions is highly restrictive. The project repeatedly emphasizes hardness does not transfer from arbitrary tests/posets to the antichain/sorting case (Hyafil–Rivest/Laber–Nogueira use arbitrary tests; general poset hardness doesn’t transfer). No obvious reduction exists and the structure blocks it.

**Alternation/level analysis:** The direct ATM needs O(k) rounds = polynomial alternations as function of input budget k ("polynomially many alternations supplied by the unary horizon", Claim A), so fixed-level PH membership would require collapsing unbounded alternations. Sparsity gives P/poly but census argument to reach P^NP needs NP-membership (not established). 

**Conclusion:** PH-hardness appears structurally obstructed (failed approach). PH-membership is not ruled in by sparsity; combined with polynomial alternation depth, the most consistent picture is SORT-BOUND-U in PSPACE \ PH (genuine sparse PSPACE instance outside PH) — though this remains open without PSPACE-hardness or a PH upper bound. The question’s position remains underexplored as noted.


## Other metadata

```json
{
  "finished_at": 1793522126.600781,
  "started_at": 1793518828.4965878
}
```
