# t5-uniform-tightness-threshold-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

otXCiKdM32CZCNwBtFLEKh-uninjured

## exit_state

clearexit

## question

Does every finite poset P with e(P) <= 29 linear extensions satisfy m(P) <= 5 (i.e. is T(5) = 29) for all n, or does some poset with at most 29 extensions require 6 comparisons?

## basis

research-obstruction-next.md Sec.2 table (first failing e=30 at r=5); core-threshold note certifies T(6)=33; Hanamura-Iwata e<=7 for r=3.

## falsifier

Exhibit a finite poset P with e(P) <= 29 and minimax value m(P) >= 6, or prove from the core-generation method that no such poset exists for any n.

## implication

If true, the certified exact-search base case extends from r=4 (e<=12) to r=5 (e<=29), strengthening backward pruning for computing S(n); if false, the n<=6 observed pattern does not persist all-n.

## finding_unverified

Mathematical finding: the all-n claim **T(5)=29 is false**. The finite counterexample is the staircase poset \(W_7\) on 7 elements (up-vector \((0,0,1,3,7,15,31)\)), a core with no universal element. Brute-force enumeration gives \(e(W_7)=21\le 29\), and exact minimax on its extension set gives \(m(W_7)=6\) (not sortable in 5 comparisons). An independent core-generation census confirms 97 core classes with \(e\le 29\) fail budget 5, with minimum failing extension count 21.

Consequence: the \(n\le 6\) observed value \(T(5)=29\) does not persist all-n. The sharp all-n threshold remains \(T(5)=20\) (Fibonacci upper bound via \(W_7\), \(e=21=F_8\), \(m=6\); lower bound from the audited \(E=20\) core census). Thus the exact-search base case cannot be soundly extended all-n from \(r=4\) (\(e\le 12\)) to \(r=5\) (\(e\le 29\)); the honest all-n gain is only to \(r=5\) (\(e\le 20\)).

Limits: this is a finite poset-threshold result, not a lower bound on \(S(n)\) or a complexity-class statement. The \(m=6\) value is computational, not a proof of \(m(W_n)=n-1\) for all \(n\). The lower bound is conditional on the core generator’s faithfulness (audited for \(n\le 9\), and \(W_7\) lies in that range). No repository, Lean, test, CI, or ledger changes were made; scratch only. Result posted to Antonina #301.

## Other metadata

```json
{
  "finished_at": 1795404733.184438,
  "started_at": 1795404520.5927737
}
```
