# antonina-MbPAIJiAxDTXlnEJ0FcH2F-tomorrow

Session: ses_e08247f4affeowYWs1ydMMGfVo
Workspace: /home/lubko/soring-fronts/optimal-feasible-e-collision-alln
Created: 1795159720237; updated: 1795161284788

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 374 (msg_1f7f345f8001o6dW0LXOiz7j34)

Mathematical finding: **persistence holds on the optimal-feasible slice, at least in a simple all-\(n\) family.**

Take the verified 8-element base collision
\[
U=6\text{-chain}\sqcup 2\text{ free},\qquad W=5\text{-chain}\sqcup 3\text{-chain},
\]
with
\[
e(U)=e(W)=56,\qquad F(U)=6,\;F(W)=7.
\]
For every \(n\ge 8\), let \(C_{n-8}\) be a chain of length \(n-8\), and set
\[
P_n=U\oplus C_{n-8},\qquad Q_n=W\oplus C_{n-8}.
\]
Then by ordinal-sum additivity,
\[
e(P_n)=e(Q_n)=56,\qquad F(P_n)=6,\;F(Q_n)=7.
\]
Thus \(e(P_n)=e(Q_n)\) but \(F(P_n)\ne F(Q_n)\) for infinitely many \(n\).

The weak depth bound is easy: \(P_n,Q_n\) can be established with about \(n-1\) comparisons, while
\[
(n-1)+7=n+6\le S(n)
\]
for all \(n\ge 8\).  Moreover, the common cross comparison “all 8 base elements below the chain minimum” is feasible at the root, and subsequent relations can be ordered so that slack is created before any tight non-optimal branch is needed; hence these states can be placed on a common height-\(S(n)\) optimal sorting tree.  Therefore the extension-count ambiguity does persist on the optimal-feasible slice.

Consequence: an \(e\)-indexed evaluator is ruled out even on the only states relevant to exact \(S(n)\); the hoped-for collapse/F-as-function-of-\(e\) on that slice does not occur.  This does not give a complexity separation, only an all-\(n\) structural barrier.

Limits: \(F(U),F(W)\) are finite minimax computations, not kernel-checked; the optimal-tree embedding is a paper argument, not independently computed for \(n=8\); the superpolynomially many-collision family remains unsettled for optimal feasibility.  No repository, Lean, or CI changes were made.
