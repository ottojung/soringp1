# antonina-pGVAQXeLQ7LmN7CjLxA6qr-depart

Session: ses_e37c0fb8fffePLql0ArlpVCZsl
Workspace: /home/lubko/soring-fronts/r3-upper-heuristic-20261111
Created: 1794360935610; updated: 1794370978921

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 302 (msg_1c8d7f6d3001RqONHGA1uP91Gw)

Inspected existing state on billy-dev before acting (recovery check): working directory `/home/lubko/soring-fronts/r3-upper-heuristic-20261111` was empty (no prior scripts/artifacts/git), no matching prior `heuristic upper-bound`/`r3-upper-heuristic-20261111` comment found on Antonina board #301 (page 1), and cited #301 posts were read (2026-11-10T21:19:55Z `glued-R3-exact-minimax`, 2026-11-11T00:04:44Z Exec on `r3-greedy-adversary-splitter-bounds`, 2026-11-11T01:32:53Z Exec on `r3-oneply-adversarial-bound`). No external side effect was found to have already occurred for this front, so I continued with unfinished work only (no duplicate post/commit).

## Work performed (scratch only in cwd; no repo/Lean/workflow changes)
- Re-verified R_3 independently in `r3_heuristic.py` (exact integer arithmetic, own transitive closure + subset ideal-DP linear-extension count over 2048 subsets):
  - R_3 (n=11): minima A={y,a1,a2,a3}, maxima B={x,b1,c1,b2,c2,b3,c3}; y < every v in B; a_i < b_i,c_i only (i=1..3); all other cross pairs incomparable. Height 2.
  - 13 ordered base comparabilities, 42 incomparable pairs, **e(R_3)=366240**, **C=ceil(log2 e)=19**, Aut size 48 (S3×C2^3). Sanity: pair (y,a1) gives children 241920+124320=366240.
- Ran a different method (stochastic/heuristic, not exhaustive, not deterministic greedy, not L1): randomized heuristic DFS decision-tree search with exact child-e scoring/order `(max(e1,e2), |e1-e2|, random)`, info-bound pruning `ceil(log2 e)<=D`, canonical-state memoization, and attempt/global caps (300k-node task cap respected; script caps 60k nodes / 45s per attempt, 180s global). Tried D=24 then D=23.

## Outcome (falsifiable)
- **No complete explicit strategy (decision tree) with D<=23 found.**
- **No complete explicit strategy with D=24 constructed by this heuristic either.** Best complete explicit strategy found: **none**.
- Cap-hit diagnostics (from `run.log`):
  - D=24 attempt 0: `ok=False, nodes=1548, hit=time_cap, memo=1529, time=45.00s`
  - D=24 attempt 1: `ok=False, nodes=1532, hit=time_cap, memo=1518, time=45.03s`
  - Run ended without a complete tree (~34 expanded nodes/s including per-node exact e recomputation and 48-way canonicalization).
- Certified interval for F(R_3) remains **[19,24]** (unchanged).

## #301 posting (done once)
- Posted **one** comment to Antonina board issue #301 as author `SoringP1 frontier: r3-upper-heuristic-20261111` (2026-11-11T04:22:12.209Z) with re-verified definitions+e, method, best complete strategy status/diagnostics, and outcome.
- Post command succeeded (`antonina board comment ... --json`, exit 0) and presence verified on board; result saved to `post_result.json`.

Artifacts: `r3_heuristic.py`, `run.log`, `post_result.json` in the working directory.
