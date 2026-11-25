# antonina-2FpYojc5Ycrz2tBJZwWIVm-pedicle

Session: ses_e1896d3dcffeLdP92zEvvkpA0v
Workspace: /home/lubko/soring301-exec-computable-entropy-balance-surrogates-20261117
Created: 1794883791942; updated: 1794884442945

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 336 (msg_1e7730bb6001Rbg53mkuRVeeSB)

Task complete.

**Summary of what was done:**

- **Audit:** Clean worktree on `exec/computable-entropy-balance-surrogates-20261117`, HEAD `6a96398`. No prior post by this front (scanned all pages of #301). No duplicate side effects.
- **Research:** Investigated whether a polynomial-time approximate balancing oracle (Bubley–Dyer FPRAS for `e(P)`, or Haeupler et al. partial-information sorting) can certify the exact threshold `S(n) ≤ k`.
- **Independent checks re-run this worktree:**
  - `P1=(8,12,8,0,12)`: `e=8, F=3`; `P2=(26,0,10,0,8)`: `e=8, F=4` (same `e`, different `F`).
  - `Merge(2,4)`: `e=15, info=4, F=5` (exact `e` still below true optimum).
  - `S(12)=30` vs `ceil(log2 12!)=29` (literature datum).
- **Conclusion (non-certification):** Approximation yields only near-optimal upper bounds. Even exact `e(P)` does not determine `S(P)`; balancing slack is `Θ(n)` while Sergeev's gap is `o(n)`. Conditional completeness theorem stated: would require split error `δ=o(1/log n)` *and* additive slack `A=o(n/(log n)^{1/5})` simultaneously — not achieved by Kahn–Saks (constant `δ`) or Cardinal et al. (additive constant blows up as `δ→0`). FPRAS error is controllable but cannot fix the structural slack. No NP membership claimed from an approximate oracle.
- **Deliverables:** `exec-report.md` written locally; concise summary posted to Antonina #301 (author `SoringP1 frontier: computable-entropy-balance-surrogates`) — no duplicate. No Lean/repo/PR changes.
