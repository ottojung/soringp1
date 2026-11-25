# antonina-TiC9RzNouEcXwVTw0hPKPk-sticks

Session: ses_e367ae8ceffeaZPgwzb0JMeJjL
Workspace: /home/lubko/soring-fronts/abc-tree-completeness-20261111
Created: 1794382305121; updated: 1794391651235

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 233 (msg_1ca1358e8001E2ivAwpQCdcJ2U)

**Recovery/audit (no duplicate external actions taken)**

- Inspected cwd: `/home/lubko/soring-fronts/abc-tree-completeness-20261111` is empty (no prior scratch artifacts), not a git repo, worktree clean in that sense.
- Inspected board state via `antonina board show --id 301 --page 1/2` and confirmed an existing post for the exact requested front:
  - **`SoringP1 frontier: antichain-reachable-abc-tree-completeness @ 2026-11-10T02:10:21.448Z`**
- This post already addresses the asked question (definitions, A/B/C at nodes, exact minimax `F(P)` vs certified height `H(P)`, exhaustive small-n results, witnesses/constructions, reachability evidence, limits, and no repo/Lean/PR changes). Because a prior turn may have already performed the external side effect, I did **not** post another comment to avoid duplication.

**What the existing #301 post reports (verified present)**

- **Question/scope:** For each `n`, is there a height-`S(n)` comparison tree from the `n`-antichain with every internal node satisfying node-local Peczarski A/B/C at that node? Falsifiable either way; exhaustive/boundary evidence over small `n`.
- **Definitions (as posted):** incomparable pair `(x,y)`, `a=e(P+xy)`, `b=e(P+yx)`; slave `z>x` incomparable with `y` or `z<y` incomparable with `x`. A: ≤1 slave and `2a>=e(P)`; B: `2a=e(P)`; C: triple `(x,y,z)` with `e(P+xy+yz) <= max{e(P+yx),e(P+zy)} <= e(P)/2`. Certified node = A/B in some orientation or C for a triple whose first comparison is the node comparison. `F(P)` exact minimax height, `H(P)` minimum height of an all-certified correct tree; `G(P)` true iff `H(P)=F(P)`.
- **Exhaustive small-n boundary (exact, as posted):**
  - `n=7`: 2045 unlabeled posets, 1 with `H>F`, `F(A_7)=H(A_7)=13`, 802 optimal-move-reachable states, 0 bad.
  - `n=8`: 16999 posets, 52 with `H>F`, `F(A_8)=H(A_8)=16`, 5102 optimal-move-reachable states, 18 bad.
  - `n=9`: 183231 posets, 839 with `H>F`, `F(A_9)=H(A_9)=19`, 33054 optimal-move-reachable states, 153 bad.
  - `F(A_n)` matches published `S(7..9)=13,16,19` (minimax check).
- **Witnesses (as posted):** certificate-starved optimal-reachable states at `n=8` (`Q8`, reached in 6 optimal comparisons, `F(Q8)=10,H(Q8)=11`) and `n=9` (`Q9`, `F=13,H=14`), with independent replay confirming no all-certified optimal continuation/tree at those states.
- **Conclusion stated:** reachability/pathwise falsifier is met at `n=8,9` (an optimal path can reach an uncertified-optimal state), but the **existential** claim (“some height-`S(n)` tree from antichain has every node A/B/C-certified”) remains **TRUE for `n<=9`** and **OPEN for all `n`**. A reachable bad state can be avoided by another optimal certified tree at tested orders.
- **Limits/honesty (as posted):** not a proof/disproof for all `n`; `n=10`/`11` exhaustive not attempted (size/cost noted); no P/NP/`SORT-BOUND-U` consequence; no succinct exact-verification scheme; GPC gives certified moves for order ≤11 states but not necessarily minimax-optimal ones; no repo/Lean/test/PR changes, scratch-only computation.

**Status**

- Required external effect (one comment to board issue #301 for this front) already exists; no unfinished posting work remains from this interrupted turn.
- I did not rerun/alter computations or create repo changes, and I did not duplicate the post. If you want, I can independently re-verify or extend the small-`n` search from scratch in this cwd and report back here (posting again only if explicitly requested, to avoid duplicate board comments).
