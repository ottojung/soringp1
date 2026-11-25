# antonina-u8NhihEDxQTZQxTpDf1ohV-flooding

Session: ses_e0ed3d1ddffeBUtqqUqkKTb1DR
Workspace: /home/lubko/soring-fronts/t12-decide-symbolic-20261119exec
Created: 1795047566887; updated: 1795049160517

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f12c3470001ZXkRG6qTYuJNNI)

I'll start by following the FIRST instructions: reading all required documents and auditing the worktree before any external side effects.

## Output 37 (msg_1f12c478b0018RD02HEtZHRAE7)

Worktree is clean at the expected HEAD on branch `billy-dev`. Now let me inspect the board digest script and scan #301 for any prior post by my exact author string.

## Output 61 (msg_1f12c6fc4001CNGfigQD1C5g3F)

No prior post on page 1. The predecessor scanned 58 pages total, so I'll check all pages for my exact author string to rule out duplication.

## Output 72 (msg_1f12d8469001TfwoG4ngxRMAO1)

No prior post by my author string across pages 1–70 — no duplication. Let me read the full predecessor report to understand the exact engine, results, and barrier details.

## Output 83 (msg_1f12d9d73001snSiau6LrvIWGq)

No duplication and I have the full predecessor report. Let me read the relevant theoretical notes and the earlier SMT predecessor post so my angle is genuinely distinct.

## Output 106 (msg_1f12dde47001feXtj7nP9Yr5y6)

Let me check the earlier SMT predecessor post (to ensure my angle is distinct) and survey the environment (existing scratch code, available solvers/compilers).

## Output 139 (msg_1f12eec3a001yO0NuqGzypmUwe)

Interesting — there's a scratch log claiming `t(12)=18` quickly. I need to determine whether that was a sound computation or a discarded buggy run (the predecessor mentioned unsound monotonicity prunes). Let me investigate carefully.

## Output 150 (msg_1f12f0b00001tFgEWmSQeBgq1h)

The scratch `adv18.log` (23:41) predates the final corrected source (23:43/23:51) and was discarded as unsound — an important trap. Let me read the engine source to understand the unsound prune and the real barrier.

## Output 161 (msg_1f12f4750001ckxN1QD4VtcW9a)

The discarded log used an earlier unsound version (the final code's prune is different), and the final engine indeed never completed t=18. Let me check for a working compiler and measure the actual admissible frontier size, which determines feasibility.

## Output 172 (msg_1f12feb510018KMHxNpA0jTQ1L)

Working g++ toolchains exist in the Nix store. Let me set up a compiler wrapper and build a fresh frontier-enumeration engine (a distinct forward/backward DP, not the predecessor's recursive AND–OR memo).

## Output 201 (msg_1f13092dc0013OsCEeM3uJwDZ2)

Compiler works. Now let me write a fresh forward/backward frontier engine (distinct from the predecessor's recursive AND–OR memo) to measure the admissible frontier and attempt t=18.

## Output 369 (msg_1f14432100017V4bptUkx6xLBH)

**External side effects (audited):**  
- Worktree `/home/lubko/soring-fronts/t12-decide-symbolic-20261119exec` remained clean at `HEAD 6a96398d937d20977a91b9afa8619cb27feab269` (no repo/Lean/test/workflow/frontier-ledger/canonical-main changes). All scratch work was under `/tmp/opencode` only.  
- #301 duplicate scan: no prior post authored exactly `SoringP1 frontier: t12-decide-symbolic-20261119exec` before work; rechecked immediately before posting.  
- **Posted exactly once** on Antonina #301: author `SoringP1 frontier: t12-decide-symbolic-20261119exec`, created `2026-11-19T00:45:28.908Z` (verified present on page 1). No other external actions.

**Investigation summary (distinct angle: forward admissible-frontier enumeration + backward winning-set DP, not recursive memoized AND–OR):**
- **Definitions/targets [definition/literature]:** `L_0(P)=⌈log2 e(P)⌉`, `L_t(P)=1+min_{(i,j)} max(L_{t-1}(P+i<j),L_{t-1}(P+j<i))`, `C(12)=29`, `S(12)=30`, `t(12)=min{t : L_t(A_12)=30}`; barrier `L_t(A_n)=C(n)` for `2t<=n`; finite convergence gives upper bound `t(12)<=66`.
- **Independent validations [experiment/deduction]:** small-n information-tight `n=6,7,8` (`C=10,13,16`) gave `W(A_n,C(n),t)=true` for `t=1..7` with exact canonical frontier sizes reported; barrier deductions applied. For `n=12`, forward+backward verified `L_t(A_12)=29` for `t=1..10` with measured admissible canonical frontiers `S0..S10 = 1,1,2,7,27,102,456,2074,9952,49661,250310` (independent prefix check by a different algorithm; full `t<=17` spine not re-executed here beyond `t<=10` and is attributed to predecessor `t12-lookahead-strong` as cross-validated in prior executive review).
- **t=18 push / symbolic-distinct attempts [experiment/deduction]:** forward-frontier growth ratios (c=1..10) `1.00,2.00,3.50,3.86,3.78,4.47,4.55,4.80,4.99,5.04` (last-3 avg ≈4.943) extrapolate to `S11~1.24e6, S12~6.12e6, S15~7.39e8, S18~8.92e10` canonical states (~0.39 GB / ~47 GB / ~5.7 TB at ~64 B/state, rough). An extended forward run was SIGKILLed after reaching `S10`; straightforward SAT/SMT/BDD/implication encodings of the 18-ply alternation and move-orbit/automorphism strengthening face the same combinatorial winning-frontier/alternation structure (canonical isomorphism already quotiented), with no tractable completion at `t=18` within budget.

**Deliverable/result:** **Exact `t(12)` NOT decided (honest INCONCLUSIVE).** No checkable witness for `L_18(A_12)=30` (with both children certified) and no certified refutation establishing `L_18(A_12)=29`. Best supported window remains **`t(12) ∈ [18,66]`** (lower bound supported by barrier/deduction + predecessor-verified `t<=17`, independently rechecked here through `t<=10`; upper bound from finite convergence with `S(12)=30` [literature]). Precise resource-barrier/state-count and encoding-limit analysis for `t=18` included in the post.

**Scope statement:** concerns only the lookahead-hierarchy value `t(12)`; gives **no** faster algorithm for `S(n)`, **no** succinct/checkable certificate for `SORT-BOUND-U`, and **no** complexity-class result or separation (no P/NP/PSPACE implication). No theorem completion claimed for `S(n)` or `SORT-BOUND-U`.
