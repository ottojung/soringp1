# antonina-B0I088iLIJeCzEL2bam8PS-correctly

Session: ses_e159f4186ffeiH9Kh2ya5bXhxf
Workspace: /home/lubko/soring301-exec-series-parallel-alln-20261117e
Created: 1794933571261; updated: 1794933663576

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 65 (msg_1ea61f6e5001nsqqHsZfdgusig)

Wrote `exec-report.md` in `/home/lubko/soring301-exec-series-parallel-alln-20261117e`.

**Summary of findings (all `n`, exact `F(P)` / `S(n)=F(∅_n)`):**
- **Series/ordinal-sum (`A ⊕ B`) — exact but no provable asymptotic gain for `S(n)`:** `F(A⊕B)=F(A)+F(B)` holds (deduction/literature context in `docs/research-series-decomposition.md`, Jain–Klauck–Sántha direct-sum specialization) and is poly-time detectable, but (1) the root antichain `∅_n` is series-prime/incomparability-connected so the identity cannot decompose `S(n)`, (2) every labelled poset remains reachable (`2^{Θ(n^2)}` state space) with a series-prime core that must still be handled, and (3) decomposition adds component memo states rather than shrinking stored state count. Finite evidence (`scripts/series_decomposition_probe.py`, `n≤5`, exhaustive poset checks `n≤4`) preserves `S(n)` but shows states `3→4, 19→23, 219→230, 4231→4381` despite fewer expansions; decomposable fraction decreases `67%→47%` (`n=2..5`). A correlated-subset counterexample (`F(L(P))=2, F(S)=1, F(S_A)+F(S_B)=2`) bounds exactness to true poset products.
- **Parallel/disjoint-union (`A ∥ B`) — obstruction, no exact evaluation recurrence:** `F` is not additive (`F(a∥b)=1 ≠ 0`) and comparisons interleave, so no general series-parallel/minimax merge recurrence for `F` is known; `∅_n` factors as a disjoint union but `S(n)` does not split. Related parallel-module reversals give exact symmetries only in restricted/unresolved forms (`docs/research-parallel-duality.md`, `docs/research-orientation-modules.md`) and no asymptotic state/exponent reduction.
- **Consequence:** Exact series/parallel decomposition, as established, does not yield a provable asymptotic reduction in reachable state space or evaluation exponent for computing `S(n)`/`SORT-BOUND-U`; it provides structural shortcuts/identities but does not move the exponent frontier. Any future decomposition claim needs an all-`n` `F`-correct recurrence plus an asymptotic bound against the poset-DP baseline and falsification on known values/counterexamples.

No repo-wide edits, Lean, PRs, or comments were made (only `exec-report.md` added).
