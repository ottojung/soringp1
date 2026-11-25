# antonina-UAx7txWqiOjMUzJBxVusO7-wronged

Session: ses_e07ffedc1ffeu8g2FcMD4BZs7z
Workspace: /home/lubko/soring-fronts/superpoly-optimal-feasible-e-collisions
Created: 1795162116779; updated: 1795162336488

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 257 (msg_1f8035bdd001SqdG78sOve6hT6)

Mathematical finding: **YES** — the \(2^{\Omega(\sqrt{n/\log n})}\) extension-count collisions do persist on the optimal-feasible slice for all sufficiently large \(n\).

Construction: amend the eindex family by forcing one large prime component \(p\) with \(m/3 \le p \le m/2\) (\(m=n-8\)) in each prime set \(S\), plus an arbitrary subset \(T\) of smaller primes with sum \(\le m-p\). Set \(C_S\) to the disjoint union of a chain of length \(p\), chains for \(T\), and free elements; then \(P_S=U\oplus C_S\), \(Q_S=W\oplus C_S\) with \(U=6\)-chain \(\sqcup\) 2 free and \(W=5\)-chain \(\sqcup\) 3-chain. We still have \(e(P_S)=e(Q_S)\) but \(F(P_S)=6+F(C_S)\neq 7+F(C_S)=F(Q_S)\). The number of admissible \(T\) is \(\exp(\Omega(\sqrt{m/\log m}))\), so superpolynomially many ambiguous \(e\)-values remain. The large prime makes the information deficit \(D=\log_2(p!)\ge 9m\), and merging the \(O(\sqrt{m/\log m})\) chains costs at most \(\frac12 m\log_2 m+O(m\log\log m)\le m\log_2 m-10m\). With Ford–Johnson, \(S(n)\le \log_2 n!+O(\log n)\), so \(d+F(P_S)\le S(n)\); single bad outcomes are one inversion or one chain split, also within budget. Thus these states lie on a common height-\(S(n)\) optimal tree.

Consequence: \(e\)-indexed dynamic programming over optimal continuations has superpolynomial ambiguity; a polynomial-size exception set cannot rescue an \(e\)-keyed exact evaluator.

Honest limits: feasibility embedding is a paper argument; \(F(U),F(W)\) and additivity are finite/paper-checked, not kernel-checked; the construction needs \(n\) large enough for the prime choice and the merge-cost inequality. No complexity separation, no new \(S(n)\) value, and no repository/Lean changes were made. The result has been posted to Antonina board #301.
