# antonina-cQD2z0rdyD7HU4iTOC7Svw-tetanic

Session: ses_e145f9602ffenzkoGVST1M9I7a
Workspace: /home/lubko/soring301-exec-adversary-nontight-20261117b
Created: 1794954521115; updated: 1794957210664

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 558 (msg_1ebc9490f001gfCM73KCh7xLoA)

Final state achieved — report below.

## What happened this run (continuing the interrupted thread)

1. **Recovery audit:** worktree clean, HEAD `6a96398`, detached; no lingering processes; no prior #301 post by the front `SoringP1 frontier: adversary-forced-nontightness` existed (latest posts at that point: executive dispatch 22:29Z, framed-dag 22:39Z, sergeev-grammar 22:39Z, catalytic-space-barrier 22:48Z). No side effects had been duplicated or repeated.
2. **Read:** `AGENTS.md`, `docs/research-plan.md`, `docs/problem.md`, `docs/research-n12-nontightness.md`, `docs/research-winning-frontier-barrier.md`, plus the board #301 thread (pages/comments) and the prior `adversary-forced-winning-frontier-states` post (22:14Z).
3. **Investigated the sharp question** ("must every height-S(n) optimal tree hit a reachable state with `F(P) > ceil(log2 e(P))`?") using the repo engine (`scripts/nontightness_experiments.py`) plus scratch search (`/tmp/opencode/nontight_force2.py`: `CanSort(P,d)` with information prune, `alltight(P,b)`).

## Findings

- Known data: `S(n)=C(n)` for `n<=11, 20, 21`; `S(n) > C(n)` for `n=12..19, 22` → forcing is trivially at the antichain root (depth 0) exactly for those nine `n`.
- **Hard result (refutation, small n):** for every root-tight `n` with a computable exact minimax search, an **all-tight height-S(n) optimal tree exists** for `n = 1..7`; for `n = 5,6,7` it was built and exhaustively verified over all `n!` permutations (worst case = `S(n)`, all reachable states tight by construction).
- **Consequence:** non-tightness is **not** forced for those root-tight instances; the only forced instances found are the root-excess ones (`n=12..19,22`).
- **Open:** all-tight existence for `n = 8, 20, 21` (n=8 run was stopped inconclusive / still too expensive; n=20,21 are the root-tight boundary ≥12).

## Deliverable status (exact)

- **Posted to board #301** via `antonina board comment --id 301 --author "SoringP1 frontier: adversary-forced-nontightness" ... --json` → **SUCCESSFUL** (comment id `sha256:Z8eKGO6YxWB9eZqRrCSCcNgrOdyQ7Yxfk3uOUM0nXHY`, created `2026-11-17T23:13:03.123Z`, no duplicate).
- **Exec report** written to `/home/lubko/soring301-exec-adversary-nontight-20261117b/exec-report.md` (untracked; repo otherwise untouched, HEAD still `6a96398`).

**Stop condition:** not met in the (a) all-tight-for-n≥12 or (b) all-n-forcing sense; **(c) hard data for n≤22 plus precise obstruction** delivered (all-tight exists for root-tight n≤7, impossible where root excess, open deeper). Honest limits: no theorem claimed, no complexity-class implication, small-n only.
