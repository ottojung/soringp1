# antonina-9vbkeRPmx4E2KU8Bth97qn-lesions

Session: ses_e3939d4cfffe24QVrnNMFqAgRn
Workspace: /home/lubko/soring-fronts/r3-exact-minimax-20261110
Created: 1794336238406; updated: 1794345629695

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 133 (msg_1c7551a88001MLo28kB5Xe3Tfq)

**Environment / recovery checks (billy-dev, no side effects duplicated)**
- Worktree: `/home/lubko/soring-fronts/r3-exact-minimax-20261110` (git clean at `6a96398`, no uncommitted changes/untracked files).
- Read: `AGENTS.md`, `docs/research-plan.md`, `docs/problem.md`; reviewed SoringP1 #301 page 1 including 2026-11-10 `height-two-prime-excess-boundedness` post and Executive verification.
- No prior `glued-R3-exact-minimax` post found on #301 before posting; no `/tmp/opencode/r3mm` scratch existed. No repo/Lean/branch/PR changes made; scratch only in `/tmp/opencode/r3mm/`.

**Question attacked (falsifiable)**
Exact minimax `F(R_3)` for the glued height-two prime `R_t` family (or a proof `F(R_3) >= 20` / a tightened interval / a checkable failure point), using a different exact method than those reported as failed.

**Definitions / independent re-verification** [definition + experiment]
- `R_t`: minima `A={y,a_1..a_t}`, maxima `B={x,b_1,c_1,..,b_t,c_t}`; `y` below all of `B`; each `a_i` below `b_i,c_i` only; all other cross pairs missing. Height 2.
- For `t=3` (n=11): own construction + transitive closure + ideal/downset DP linear-extension count gives `e(R_3)=366240`, `C=ceil(log2 e)=19`. BFS shows comparability and incomparability graphs both connected => prime.
- Matches Exec-verified data: `t=1..3 -> e=14,1280,366240; C=4,11,19`. Known context: `F(R_1)=4`, `F(R_2)=11`, `19 <= F(R_3) <= 24`.

**Method attempted (different from reported stalled approaches)** [experiment]
- Decision/poset-state search `can_solve(P,budget)` on transitively-closed pairwise-order states (row bitmasks), not extension-subset states.
- State canonicalization over `Aut(R_3)=S_3 × C_2^3` (48 automorphisms, min-image key) for memoization.
- Pruning: fail if `budget<0` or `ceil(log2 e(P))>budget` (info bound); success if `e(P)<=1`.
- Move generation over incomparable pairs; adversary = worse child; move ordering by `max(e(child1), e(child2))` ascending.
- Exact `e(P)` per encountered state via subset ideal-DP `e(S)=Σ_{x minimal in S} e(S\{x})` (n=11, 2048 subsets) cached by state key.
- Scripts (scratch): `/tmp/opencode/r3mm/r3_solve.py`, `solve_f.py`, `solve_budget.py`.

**Exact data / results** [experiment]
- Sanity (R_2, n=8, e=1280, C=11, budget 11): solver returns `F=11` with `31,679` nodes / `31,679` memo states.
- R_3 decision probe `can_solve(R_3, 19)` (is `F(R_3) <= 19`?): 10s wall-limit run => **TIMEOUT** at `4,629` nodes, `300` (state,budget) memo entries, `8,437` distinct e-cached states; no decision reached.
- Measured blocker: per-node cost dominated by 48-way canonicalization and fresh exact `e(P)` ideal-DP evaluations on many distinct refined states (~840 e-states/s incl. overhead at this scale), with rapid state growth relative to explored nodes. Full budget-19 refutation/search (and thus exact `F`) infeasible by this method at observed scale.

**Outcome**
- No exact `F(R_3)` determined.
- No tightened interval and no checkable adversary proof of `F(R_3) >= 20` obtained.
- Checkable failure point identified: poset-state canonicalized DFS + info-bound + exact extension-count pruning stalls on `R_3` budget 19 at ~4.6k nodes/10s (8.4k e-cached states/10s), n=11, e=366240.
- **Question remains open:** `19 <= F(R_3) <= 24`.

**Board report posted (once)**
- SoringP1 #301 comment: author `SoringP1 frontier: glued-R3-exact-minimax`, created `2026-11-10T21:19:55.902Z` (id `sha256:2kG_7M7xQSmT2l4m1V9QXwko7eB0mkeJ8Qx_s4j2vDg` not separately recorded; visible as latest post in board show output).
- Report states definitions, method, exact data, limits/blocker, and that the question stays open. No theorem completion claimed.
