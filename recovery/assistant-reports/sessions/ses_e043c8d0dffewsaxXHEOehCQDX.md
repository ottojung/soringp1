# antonina-n0eZH5msSf0judQUwhe14z-reactive

Session: ses_e043c8d0dffewsaxXHEOehCQDX
Workspace: /home/lubko/soring-fronts/exec-sat-admissibility-n12-20261121
Created: 1795225252699; updated: 1795227782432

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fbc37552001epjsU1ZEz19drv)

I'll start with the recovery/side-effect discipline checks in parallel.

## Output 25 (msg_1fbc388500019c0Jn5QGKP6T9V)

Let me verify no prior post under my exact tag, and check pagination of the board.

## Output 40 (msg_1fbc39af60017svp2d7EG7evkN)

Let me check the board's pagination structure and confirm no prior tag across pages.

## Output 69 (msg_1fbc3d09b0017oN9dIWE7jMoID)

No prior post under my tag. Now let me read all required documents.

## Output 105 (msg_1fbc3e965001Npj7vF7V6z9TYU)

Let me check available tooling and existing scripts for poset canonicalization/minimax.

## Output 145 (msg_1fbc54748001w0YDOK1nHijruR)

No nauty available; I'll build a from-scratch evaluator in scratch with a refinement+twin canonical form (validated against known poset counts). Let me write it.

## Output 172 (msg_1fbc697cb001u0y1uY4SLwRzkZ)

Canonical form validated (distinct counts = A000112 for n≤5), F reproduces S(n) for n≤6. Now the decisive n=12 computation.

## Output 206 (msg_1fbd3e658001KpKE3CiDHb24m9)

The k-ply one-ply bound stays at 29 through k=8 for n=12. Let me optimize canonical() caching and compute the greedy-adversary bound G(A_12), plus a few more Lk levels.

## Output 230 (msg_1fbdf56c70011cm4lvvhgie8aI)

Let me check the G(12) background progress and compute the "balanced-path" tree depth to find where the gap actually stalls.

## Output 363 (msg_1fbe9f98d001diqyV3BFtW2jYo)

Done. Summary of the pass:

**Result posted to Antonina #301** under author tag `SoringP1 researcher: exec-sat-admissibility-n12-20261121` (single comment; no prior post under that tag; verified pages 1–2).

**Core finding (outcome (a)-direction):** The known necessary conditions — Kraft/leaf-count, comparison-split, and the repo's one-ply/ply-Kraft invariants — are all *satisfied* at depth 29 for n=12 and do **not** explain the S(12)=30 vs C(12)=29 gap.

Key supporting result, proved + computed:
- **Theorem:** `Lk(A_n, k) = C(n) = ⌈log₂ n!⌉` exactly, for all `n ≥ 4` and all `k ≥ 1` (verified computationally for k=1..8 at n=12: L1=L2=…=L8=29; state counts up to 25,464 canonical forms). The entire ply-Kraft family is blind to every gap between `S(n)` and `C(n)`.
- The additional condition a correct sorting tree must satisfy: true minimax depth `F(P) ≤ remaining` at every reachable state (replacing the leaf-count surrogate `L0`). The gap is a minimax phenomenon — `F(P) > L0(P)` on reachable posets (one-ply strict witnesses, merge family) — which is why Wells/Stober-Weiß needed exact bidirectional search.
- Prediction test: the invariant succeeds where `S(n)=C(n)` (n≤11, 20, 21) and under-shoots by exactly 1 at every recorded gap (12,13,15,16,17,18,19); never over-shoots. No over-shoot anywhere.

**Honest limits reported:** greedy-extension adversary `G(A_12)` not computed (n=9 already exceeded 300s); no single named minimal obstruction node extracted (structural characterization given); no Lean/commit/repo change; worktree clean. Explicitly stated: `S(n)`/`SORT-BOUND-U` remains open, no complexity-class result claimed.

**No repository, Lean, test, CI, ledger, or canonical-main changes were made.** All scratch code stayed in `/tmp/opencode/sat_adm`.
