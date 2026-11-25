# antonina-KcOElsy8OwWhwmwT3gRXQn-publish

Session: ses_e0b7c206dffeBMLf9crB4NETO5
Workspace: /home/lubko/soring-fronts/optimal-play-exponent-thetapin-alln
Created: 1795103645654; updated: 1795104805445

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f483e1c1001xW6i5fFmBGR6za)

I'll start by studying the required documents before taking any action.

## Output 25 (msg_1f48430ed001pPgsRl24TJBfFP)

Now let me read the operations doc and the key research documents referenced in the task, and check my worktree's baseline state.

## Output 44 (msg_1f48441270012umpvi0CG9XVKf)

Let me examine the board tooling and how to interact with Antonina, plus find the referenced report and DAG(all) definition.

## Output 59 (msg_1f48470ea001RLklEutfpXElc7)

Let me read the DAG(all) definition in context and inspect the Antonina CLI.

## Output 184 (msg_1f49537b7001QKu5zPaQBLDP0T)

**State check (no duplicate external effects):** Inspected worktree `/home/lubko/soring-fronts/optimal-play-exponent-thetapin-alln` (`git status --porcelain` clean before/after, branch `billy-dev`), scanned #301 for prior posts by this exact author (`SoringP1 frontier: optimal-play-exponent-thetapin-alln`, pages checked via `board_digest.py --contains thetapin/optimal-play-exponent`: none), and confirmed no prior comment had been posted by me. Scratch artifacts only under `/tmp/opencode/` (`optimal_play_exponent_audit_301.txt`, `optimal_play_exponent_audit_post.out`). No repo/Lean/test/workflow/frontier-ledger/canonical-main changes.

**Audit performed (paper-level, against definitions/docs):**
- **[definition]** Reconfirmed `L(n)` = count of distinct labelled poset states on some height-`S(n)` optimal comparison play / `DAG(all)` (all minimax-optimal moves, `F(P)=1+max(F(P1),F(P0))`, hash-consed by identical labelled poset). Legal comparisons are informative, so depth `t` is well-defined and DAG(all) membership implies `F(P)=S(n)-t`.
- **[paper audit] Upper bound (re-derived, sound):** `L(n) <= Σ_{t<=S(n)} (n(n-1))^t <= (n(n-1))^{S(n)+1} <= n^{2(S(n)+1)}`. With merge-sort witness `S(n) <= n*ceil(log2 n)`, this gives `log2 L(n) <= 2n(log2 n)^2 (1+o(1))`, i.e. `L(n)=2^{O(n log^2 n)}`.
- **[paper audit] `docs/research-winning-frontier-barrier.md` (internally consistent on checked points):** Verified the independent-chain construction/counts (`M=(L-1)s(s-1)`), adjacent-level non-implication/reachability argument (edges span one level, so no multi-edge path implies an adjacent-level relation), distinctness of `P_A`, tournament-merge upper bound `F(P_A) <= B` giving `F(P_A) <= k-t`, nonisomorphic count `>= binom(M,m)/n!`, asymptotics yielding `>= 2^{(1/4-o(1)) n (log2 n)^2}` for `n=2^{2r}`, and algebraic propagation of the exact-optimum extension `k=S(n)` given Sergeev’s `S(n)-C(n)=o(n)` (literature input stated in doc; not re-proved). Finite witness arithmetic (`n=224`) consistent.
- **[deduction] Key deduction — GAP (combination not established):** The proposed argument (“`t`-step path to `P` + optimal completion of height `F(P) <= S(n)-t` gives a height-`S(n)` tree”) is unsound as stated. A complete height-`S(n)` comparison tree requires every sibling branch along the path to be completable within budget, which holds only if each step is a minimax-optimal move. The barrier gives some reachable path and `F(P_A) <= S(n)-t`, but not (a) that the path consists of optimal moves, nor (b) `F(P_A) == S(n)-t`. (a) is necessary for DAG(all)/optimal-play membership; (b) can fail because `B` is a (possibly loose) tournament-merge upper bound (e.g. `s=2` gives `B=2L` while optimal 2-way merge is `2L-1`), so `F(P_A) < S(n)-t` is possible and no `t`-step optimal-move path exists. Thus barrier states are established as winning/budget-feasible frontier states, not as optimal-play states; the `Theta(n log^2 n)` lower bound does not transfer to `L(n)`.

**Outcome posted (single external write):** Appended one evidence-bearing comment to Antonina board issue `#301` as author `SoringP1 frontier: optimal-play-exponent-thetapin-alln` (2026-11-19T16:12:32.822Z) with `[definition] / [paper audit] / [deduction] / [open]` labels.
- **Result:** Claim `L(n)=2^{Theta(n log^2 n)}` is **not established** by the audited combination. Established window: `Omega(n log n) <= log2 L(n) <= O(n log^2 n)` (lower from `L(n) >= 2n!-1`, strategy-certs Thm 2.1/2.6). Finer exponent remains **open**.
- **Honest limits:** Sergeev `S(n)-C(n)=o(n)` not re-proved (used only for barrier `k=S(n)` specialization); `F(P_A)` not computed exactly for the family; no subfamily shown/rule out on optimal plays. No theorem-completion claim for `S(n)`/`SORT-BOUND-U`, no algorithm/value/class consequence.
- **Side effects:** only this #301 comment; worktree clean after.
