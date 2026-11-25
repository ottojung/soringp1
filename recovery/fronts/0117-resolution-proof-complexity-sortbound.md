# resolution-proof-complexity-sortbound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

GlgTBIvovv6QZym9HO8X4j-manor

## exit_state

clearexit

## question

For fixed encodings, is there an infinite family of CNFs encoding 'S(n) > k_n' (from a canonical all-n reduction of the minimax/AND-OR game to SAT) that require superpolynomial resolution proof size for all choices related to k_n = S(n)?

## basis

AND-OR/minimax game structure is standardly reducible to SAT; proof-complexity lower bounds are orthogonal to Mahaney/sparsity and not obviously covered by existing alternation/certificate fronts in the ledger.

## falsifier

Exhibit a polynomial-size resolution refutation for some canonical all-n CNF family encoding S(n)>S(n)-1 (a nontrivial lower bound instance) or prove bounded-width resolution suffices uniformly, contradicting a superpolynomial lower bound claim.

## implication

Superpolynomial resolution lower bounds for such canonical CNFs would imply that naive CDCL-style searches cannot refute optimality trivially, but do not by themselves place SORT-BOUND-U below NP or give a uniform algorithmic separation without further transfer.

## finding_unverified

and PSPACE/EXPSPACE bounds, but no Tseitin encoding of this exact game into CNF is present. Any claim about resolution complexity must pin down the encoding (Tseitin over ATM? over the recurrence? over poset constraints?). Different encodings can have very different proof complexities (even equivalent formulas). The front says "canonical all-n reduction" but doesn't specify it - that's a critical ambiguity.
2. **Restriction to comparison tests is essential but easy to lose**. If someone does a naive reduction treating "queries" as arbitrary or treats posets too generally, they might import Hyafil–Rivest style hardness which doesn't transfer (and the sparsity/Mahaney context already warns about transfer). Conversely, exploiting the comparison structure might make proofs easier.
3. **The formula would need to encode poset consistency/transitive closure and all permutations**. Transitive closure is a common source of complexity in encodings; doing it compactly is delicate. Also the "state graph" is the Hasse diagram of weak order restricted to order ideals - highly structured.
4. **Resolution lower bounds typically need either (a) expansion/pigeonhole-like structure, or (b) width+size tradeoffs, or (c) specific hard combinatorial objects.** The sorting game doesn't obviously produce a bipartite expander-like constraint system; it's more like a "searching with lies"? No. Or like "graph searching number"? Or more directly like a "coin weighing" with comparison tests gives a decision tree - but the adversarial strategy is different.

### Honest limits / what I can conclude
- **Cannot produce a polynomial-size resolution refutation now**. Constructing one for a general canonical encoding of S(n)>S(n)-1 is a nontrivial proof-complexity task requiring a precise encoding + proof; I don't have the encoding specified or the machinery to write such a proof.
- **Cannot rule out superpolynomial lower bounds** either. The structure is a kind of "AND-OR game" on a large state graph - AND-OR tree formulas can be hard for resolution in some forms, but with DAGs/memoization and this specific structure it's unclear. Also the restriction to comparison tests might help or hurt.
- **Key distinction (as requested)**: general-poset results don't transfer to S(n) (fixed test set). Certificate *soundness* vs *completeness* is critical - a short resolution refutation would be a sound proof of optimality (a lower bound certificate) but the existence of such refutations for all n,k near S(n) is different from NP-completeness of the decision problem.
- **Complexity implication is careful**: even if such CNFs had superpolynomial resolution lower bounds, that means CDCL won't refute optimality trivially - which matches "naive search is hard" - but as stated, doesn't place SORT-BOUND-U below NP without transfer; also SORT-BOUND-U is sparse in unary so many-one NP-hardness would collapse P=NP anyway (Mahaney). This is orthogonal to sparsity.

**Bottom line:** No concrete polynomial-size resolution refutation found. No explicit superpolynomial lower bound proved. The main obstruction is lack of a single agreed canonical polynomial-size CNF encoding for this comparison game; without pinning down encoding + doing proof-complexity analysis against comparison-test structure (not arbitrary tests), the question is underspecified. I cannot claim either horn. No repository/Lean changes made. This matches "honest limits" - a clean negative/inconclusive result on this precise front.

## Other metadata

```json
{
  "finished_at": 1793488658.9078655,
  "started_at": 1793487080.2885637
}
```
