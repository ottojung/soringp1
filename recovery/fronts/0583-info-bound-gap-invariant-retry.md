# info-bound-gap-invariant-retry

## status

investigated

## origin

executive_blocked_front_retry

## agent_id

H0X2EVTj8GfHHwTXLkzUow-beauty

## exit_state

clearexit

## question

Is there a computable poset invariant I(P) with ceil(log2 e(P)) <= I(P) <= F(P)=S(P) that is strictly greater than the information bound on infinitely many posets P arising as states in the sorting game, generalizing the n=12 antichain case where S(12)>ceil(log2(12!))?

## basis

Board #301 2026-11-12 n12-obstruction-invariant post tests L1 and related candidates and finds refutations; literature notes S(12)=30>C(12)=29 as the known small gap while general theory of gaps is open. [EXECUTIVE RETRY 2026-11-19T19:5xZ] Fresh retry of a ledger front whose Antonina agent FAILED WITHOUT A FINAL TEXT (context/tool failure, not a mathematical resolution). FIRST read the current #301 board digest and the already-investigated adjacent fronts: antichain-root-invariant-separation, optimal-path-prefix-invariant-gap, finite-invariant-incompleteness-f, comparison-split-algebraic-invariant. Decide whether the EXACT question below is already settled by them; if so, report that precisely with evidence and STOP (do not repeat their work). Otherwise attack the exact question below. Keep scratch small; never paste large outputs or media into context; post ONE concise decisive finding/obstruction to #301.

## falsifier

Prove that for every computable invariant I lying between the information bound and F(P), there is some N such that for all reachable states P with |P|>=N, I(P) equals ceil(log2 e(P)), or exhibit an infinite family where every candidate I is defeated by a counterexample.

## implication

A uniform strengthening of the information bound would narrow the exact-search window for computing S(n) without requiring a super-polynomial complexity separation, potentially improving uniform algorithms for SORT-BOUND-U.

## finding_unverified

. Let me check the four specifically named adjacent fronts in the ledger, and locate any fuller reports in worktrees.
All four named adjacent fronts are `investigated`/`clearexit`, and the identical FRONT was already posted on #301. Let me verify posting mechanics, check no prior post by my author exists, and look for a fuller report of the barrier theorem.
I now have a complete picture. The exact FRONT was already run verbatim as `info-gap-invariant-20261119exec` and attacked by all adjacent fronts, with a consistent negative/barrier conclusion. Let me verify my worktree is clean, then post one concise decisive finding to #301.
The post succeeded. Let me verify it appears on the board and confirm the worktree remains clean.
## Done — finding reported to #301, no repository/Lean changes

**Decision: the exact FRONT is already settled by the adjacent fronts; I stopped rather than repeat their work.**

### What I verified
- On `billy-dev`, clean worktree at `6a96398`; no repo/Lean/test/ledger/main changes. All scratch in `/tmp/opencode`.
- Read `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, and scanned all 61 pages of board #301.
- The exact question was **run verbatim** as `info-gap-invariant-20261119exec` (posted #301 `2026-11-19T00:58Z`) and attacked by every adjacent front, all ledger `investigated`/`clearexit`.

### Evidence that it's settled
- **`info-gap-invariant-20261119exec`** — identical FRONT; result "(b) barrier + (c) honest inconclusive". Theorem B1: no scalar invariant `I=f(e,width,#min,#max,|Aut|)` can be both sound (`C≤I≤F`) and strict-above-`C` infinitely often (`n=6` witness pairs). A sound strict invariant exists only on decomposable states, not the antichain root.
- **`n12-obstruction-invariant`** — `L₁(A_n)=C(n)`, whole `L_k` hierarchy `=C(n)` (proved), merge-factor `B(A_n)=C(n)`, pair-split obstruction `T_J^r(A_n)≤C(A_n)`.
- **`n12-obstruction-invariant-generalization`** — reversal-defect/Fibonacci/antichain-reachability all fail; `⌈log₂ #antichains⌉` is unsound.
- **`info-bound-gap-invariant-alln`** (`exec-report.md`) — all families refuted; FJ-excess fits `n≤22` but is provably not exact (Manacher `S<FJ` for some `n≥47`; `δ_FJ=Θ(n)` vs `g=o(n)` by Sergeev). Status OPEN.
- The four named adjacent fronts are all `investigated`; their merge-family gaps are on arbitrary reachable posets, not optimal antichain paths — general-poset results don't transfer to the root.

### Honest limits (the substantive mathematical point)
- `F` itself is a computable invariant with `C≤F` and `F>C` on infinitely many reachable states, so the **literal** FRONT is trivially "yes" and the supplied **FALSIFIER is false**. The intended question is a *cheaper-than-F* strengthening — which is exactly what was refuted. Soundness (`C≤I≤F`) is cheap; completeness (lifting `A₁₂`) is not achieved.
- A general barrier for *all* computable invariants is not proved and borders the open `sup_n(S(n)−C(n))` question and ineffective Sergeev extraction. "Settled" = all natural/checkable families refuted + scalar barrier, residual open — **not a complete theorem**, and I claimed none.

**Posted:** one concise decisive finding to #301 at `2026-11-19T19:57:37Z` under author `SoringP1 frontier: info-bound-gap-invariant-retry` (verified on board). Conclusion recorded: do not re-dispatch; a new result would need a cheaper-than-F invariant lifting `A₁₂` on an infinite family, or a beyond-scalar general barrier — neither obtained here.

## Other metadata

```json
{
  "finished_at": 1795118283.0553536,
  "started_at": 1795117877.136723
}
```
