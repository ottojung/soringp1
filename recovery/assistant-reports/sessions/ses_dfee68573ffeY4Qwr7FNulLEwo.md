# antonina-KZYP973Th2jAEmgqwbGHdE-delegates

Session: ses_dfee68573ffeY4Qwr7FNulLEwo
Workspace: /home/lubko/soring-fronts/uniform-extension-base-gap-growth
Created: 1795314776789; updated: 1795315447742

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 365 (msg_20123a199001nD3UYhmIhzpdN8)

**Mathematical finding: Δ(n) is unbounded.**

Using the series (ordinal) composition of a fixed 5-element poset \(P_0\) with succ-mask \((0,0,1,3,7)\), which has \(e(P_0)=8\) and \(m(P_0)=4\) (verified by independent minimax; \(\lceil\log_2 8\rceil=3\), excess \(1\)):

- For \(t\ge1\), let \(P_t\) be the ordinal sum of \(t\) copies of \(P_0\).
- Then \(e(P_t)=8^t\) and \(m(P_t)=4t\) (blocks are independent; cross-block comparisons give no information).

Take \(n_t=\min\{n:n!\ge 8^t\}\). Then \(e(P_t)\le n_t!\), so \(T(n_t)\ge 4t\). By Stirling, \(\log_2(n_t!)=3t+O(\log t)\), and standard merge sort gives \(S(n_t)\le n_t\lceil\log_2 n_t\rceil = 3t+o(t)\), while \(S(n_t)\ge \lceil\log_2 n_t!\rceil\ge 3t\). Hence \(S(n_t)=3t+o(t)\) and

\[
\Delta(n_t)=T(n_t)-S(n_t)\ge 4t-(3t+o(t))=t-o(t)\to\infty.
\]

So maximizing \(m(P)\) under an \(e(P)\le n!\) cap systematically overestimates \(S(n)\) by an unbounded amount; \(T(n)\) is not a constant-factor proxy for \(S(n)\). This is a general-poset construction reduced to the fixed antichain root via \(e(P)\le n!\) and standard sorting upper bounds; it gives no complexity-class separation for \(\mathrm{SORT\!-\!BOUND\!-\!U}\).

**Limits:** The result is an asymptotic unboundedness proof, not a finite threshold or exact rate; base case and \(t=2\) (\(e=64,m=8\)) were checked computationally, but no claim about optimal constants beyond the \(4/3\) ratio is made. No repository or Lean changes were made; worktree remains clean. The finding was posted to Antonina issue #301.
