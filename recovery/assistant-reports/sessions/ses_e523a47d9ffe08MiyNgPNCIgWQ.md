# antonina-8h8Etbxxvk3GuB3EwE71Vq-cunning

Session: ses_e523a47d9ffe08MiyNgPNCIgWQ
Workspace: /home/lubko/soring-fronts/parallel-reversal-congruence-20261106
Created: 1793916778597; updated: 1793916839460

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1adc5bdcd001itdKRD1Y5b1P7P)

I’ll inspect the research note and its cited literature first, then separate the value-identity question from the stronger transition/congruence claim. I’ll keep this within the current worktree and won’t touch board credentials or make repository changes unless the result clears the stated gate.

## Output 55 (msg_1adc600b30012tmhU7bCsYdABh)

The proposed subsequence-reversal argument does not establish the value identity: reversing the B subsequence swaps outcomes of B-internal queries, but for a cross-block query it generally changes which B elements lie before/after the queried A element. So it does not map each query’s two outcome cells to a single query partition in the other extension family. I’m now checking whether a different exact decision-tree argument works, and testing the much stronger child-transition condition directly.

## Output 71 (msg_1adc65017001MgrJRjDQNG2VHE)

The stronger congruence already fails at total size 6: take both components to be the 3-element “V” poset (one element below two incomparable elements), which is non-selfdual. The two union states have equal value (7), but their multisets of unordered successor-isomorphism-class pairs differ. I’m extracting the exact query/child witness in readable labels; this means the relation is not a DP congruence even if the value identity is true.

## Output 80 (msg_1adc67f6c001O6EbwiQcbSfNXd)

## Result

The value identity remains **unresolved**. The supplied exhaustive experiment reproduces no counterexample through total size 7: it checks 1,048 isomorphism-class pairs at size 7, with zero violations. That is bounded evidence, not an all-size proof.

The note’s proposed subsequence reversal is **not a proof**. Reversing the B subsequence can change how B-elements compare with an A-element, so it need not preserve the two outcome blocks of a cross-component query. I found no alternative paper argument or exact value counterexample.

The component-reversal relation is **not a minimax congruence**, even when the two states have equal value. A smallest witness from the exact quotient search is size 6:

- Let `V` be the 3-element poset with relations `0<1` and `0<2`; `Vᵒᵖ` has relations `1<0` and `2<0`.
- Take `P = V || V` and `Q = Vᵒᵖ || V`, using labels `0..2` and `3..5`.
- Their successor masks are `P = (0,1,1,0,8,8)` and `Q = (6,0,0,0,8,8)`.
- Exact values agree: `F(P)=F(Q)=7`.
- But their multisets of unordered pairs of child isomorphism classes differ. For example, query `{0,3}` in `P` has child classes `(0,1,1,1,9,9)` in both orientations; the corresponding query in `Q` has child classes `(0,0,0,1,1,7)` and `(0,0,3,7,15,15)`. Thus the minimax transition is not well-defined on these equivalence classes.

Consequently, this relation cannot directly provide the proposed quotient-state evaluator or an evaluator cost improvement. Equal values on these examples do not repair the failed transition condition; a different refinement or a separate proof of value invariance would be needed. No files were changed.
