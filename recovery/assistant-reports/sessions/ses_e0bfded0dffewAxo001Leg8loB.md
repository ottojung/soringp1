# antonina-wyPcV8hoFEvZg3NKLyvBvU-musician

Session: ses_e0bfded0dffewAxo001Leg8loB
Workspace: /home/lubko/soring-fronts/effective-sergeev-finite-constant-alln
Created: 1795095139248; updated: 1795095285016

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 295 (msg_1f4044466001RXU45jg2uUJ8Q4)

Reported on Antonina issue #301 as a single deliverable. Outcome: **no** — an effective finite `(C,n0)` cannot be read off from Sergeev's published proof as written. The obstruction is the non-effective parameter regime in Lemma 4: the construction requires `s = ceil((2/5) log a) ≥ 20`, forcing `a` (hence `n`) to be at least double-exponential, while the hidden constants in Theorem 2/Corollary 2 and Theorem 3's group parameters (`n0=n/log n`, `m≈√n/log n`, insertion block lengths `ρ_t`) remain untracked. For `n=23`, `a≈2.2` and `s≈1`, far outside the validated regime. The current explicit finite upper bound remains Ford–Johnson: `S(23) ≤ 76`, with information lower bound `C(23)=75`, so the search window stays `[75, 76]`. No repository/Lean/test changes; worktree clean. NO theorem completion claimed for `S(n)`/`SORT-BOUND-U`.
