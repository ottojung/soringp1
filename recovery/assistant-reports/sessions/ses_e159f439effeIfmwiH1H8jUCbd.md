# antonina-G61BozycV4YvPkxEAU0EWk-explicit

Session: ses_e159f439effeIfmwiH1H8jUCbd
Workspace: /home/lubko/soring301-exec-sound-quotient-exponent-20261117e
Created: 1794933570732; updated: 1794933686010

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 48 (msg_1ea6246d9001n4SMEHqDxV3Fix)

Wrote `exec-report.md` in `/home/lubko/soring301-exec-sound-quotient-exponent-20261117e`.

**Summary (from cited repo docs, no new experiments/Lean):**
- **Question (all n):** whether any sound exact state/move quotient for `F(P)`/`S(n)` beyond relabelling, order duality, and `Aut(P)` move orbits can provably reduce the asymptotic state-count or time exponent for exact evaluation of `S(n)`/`SORT-BOUND-U`, or whether there is a barrier.
- **Definitions:** fixed minimax model `F(P)`/`S(n)=F(∅)` on reachable posets; sound state quotient requires class-constant `F` **and** an equivariant paired-successor transition (value-invariance alone insufficient); move quotients preserve per-state minimax (e.g. `Aut(P)` orbits). Baseline: `A000112(n)=2^{Θ(n^2)}` nonisomorphic classes (relabelling), ×~1/2 for duality, ~30% move-term reduction only for orbits.
- **Candidate analysis:** comparability graph/`e(P)` unsound as state/strategy (`e`/`L` don’t determine `F`; graph fails value at `n=7` and transition at `n=5`; balanced-greedy fails at `n=9`). Gallai/module/MDT reversal unsound in general (fails at `n=7`, prime quotients; MDT-up-to-reversal not sound) though interval-module/ordinal-sum reversal is sound but narrow/non-shrinking. Series exact but not state-shrinking; parallel has no known sound exact minimax recurrence; degree/heuristic surrogates falsified or unproven.
- **Quantitative obstruction:** `docs/research-winning-frontier-barrier.md` gives, for infinitely many `n`, `2^{(1/4-o(1))n(log2 n)^2}` **pairwise nonisomorphic, reachable, winning** states at a common depth (extendable asymptotically to budget `S(n)`), barring any `2^{O(n log n)}` method that must enumerate/materialize the full winning frontier. Does not lower-bound arbitrary selective/symbolic evaluators.
- **Conclusion:** no sound exact quotient beyond relabelling/duality/`Aut(P)` move orbits is currently proved to reduce the asymptotic state-count or time exponent; a frontier-enumeration barrier exists, but a fully general “no possible sound quotient” barrier for all exact evaluation methods remains **open/unresolved** (future candidates must be transition-sound, survive known falsifiers, and either provably collapse the winning frontier or enable non-enumerative evaluation). Details, evidence, and consequences are in `exec-report.md`.
