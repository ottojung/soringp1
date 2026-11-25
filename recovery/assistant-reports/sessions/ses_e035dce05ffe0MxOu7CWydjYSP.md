# antonina-JtbvFo2nhW5jaOQmyKnR27-blockhead

Session: ses_e035dce05ffe0MxOu7CWydjYSP
Workspace: /home/lubko/soring-fronts/framed-dag-exact-budget-hybrid-alln
Created: 1795239850496; updated: 1795240324246

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 550 (msg_1fca962520013khk4EonjQ6xjC)

Posted to Antonina #301 (2026-11-21T05:52 UTC). No repository, Lean, test, or CI changes.

**Finding.** The hybrid route is refuted for exact budgets:

- Weak (polynomial) rank-envelope windows give height \(W_{\text{weak}}(n) > F_{\text{FJ}}(n) \ge S(n)\) for all \(n\ge 5\) (e.g. \(n=5\): 10 vs 7; \(n=12\): 39 vs 30), so they cannot certify the exact budget.
- Exact budget therefore requires exact insertion positions. In the Ford–Johnson schedule the first insertion is a zero-comparison prepend for a value-dependent subset of inputs (72/120 permutations at \(n=5\)), and that prepend’s applicability depends on value state, not the outcome prefix. A shared edge would need two incompatible frames; splitting gives exponential blowup.
- Merge-sort-style insertion avoids zeros but has height 8 at \(n=5\), above \(S(5)=7\).

Thus lifting the accepted merge-sort framed DAG through rank-envelope insertions cannot yield a polynomial-size, prefix-determined exact-budget certificate; the zero-comparison/value-dependent-frame obstruction is unavoidable for exact budgets in this family. This does **not** prove \(\text{SORT-BOUND-U}\notin\text{NP}\) or exclude other constructions. SORT-BOUND-U NP membership remains open.
