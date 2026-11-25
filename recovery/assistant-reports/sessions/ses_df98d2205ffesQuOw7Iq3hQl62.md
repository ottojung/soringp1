# antonina-otXCiKdM32CZCNwBtFLEKh-uninjured

Session: ses_df98d2205ffesQuOw7Iq3hQl62
Workspace: /home/lubko/soring-fronts/t5-uniform-tightness-threshold-alln
Created: 1795404521054; updated: 1795404707093

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 366 (msg_20675a1f70014DTG6o13e9EDeY)

Mathematical finding: the all-n claim **T(5)=29 is false**. The finite counterexample is the staircase poset \(W_7\) on 7 elements (up-vector \((0,0,1,3,7,15,31)\)), a core with no universal element. Brute-force enumeration gives \(e(W_7)=21\le 29\), and exact minimax on its extension set gives \(m(W_7)=6\) (not sortable in 5 comparisons). An independent core-generation census confirms 97 core classes with \(e\le 29\) fail budget 5, with minimum failing extension count 21.

Consequence: the \(n\le 6\) observed value \(T(5)=29\) does not persist all-n. The sharp all-n threshold remains \(T(5)=20\) (Fibonacci upper bound via \(W_7\), \(e=21=F_8\), \(m=6\); lower bound from the audited \(E=20\) core census). Thus the exact-search base case cannot be soundly extended all-n from \(r=4\) (\(e\le 12\)) to \(r=5\) (\(e\le 29\)); the honest all-n gain is only to \(r=5\) (\(e\le 20\)).

Limits: this is a finite poset-threshold result, not a lower bound on \(S(n)\) or a complexity-class statement. The \(m=6\) value is computational, not a proof of \(m(W_n)=n-1\) for all \(n\). The lower bound is conditional on the core generator’s faithfulness (audited for \(n\le 9\), and \(W_7\) lies in that range). No repository, Lean, test, CI, or ledger changes were made; scratch only. Result posted to Antonina #301.
