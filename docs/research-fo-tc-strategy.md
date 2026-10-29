# FO(TC) strategy programs for exact optimal sorting

Model: a strategy program is a finite FO(TC) program over structures with state predicates. Each comparison is a charged oracle query `cmp(a,b)` with branch on outcome. Mutable knowledge stores relative order facts. Termination requires a total order. Worst-case comparison budget k.

Soundness/time: fixed interpreter evaluates in polynomial combined time when program size and n are inputs; data complexity alone insufficient. Restrict to bounded-variable arity to keep combined polynomial.

Completeness (conditional): conjecture that S(n)-optimal adaptive comparison strategies have poly(n+k)-size programs with poly(n+k) runtime. Not proved. No NP/Sigma_2^P claim without completeness.

Next experiment: implement interpreter + encode insertion/merge sort; test small n.
