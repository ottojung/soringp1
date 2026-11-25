# antonina-6eKyptaZcXXrdc0ccRulkq-inflamed

Session: ses_e17b213c8ffeRgxh6oXszmZQRU
Workspace: /home/lubko/soring301-exec-framed-dag-n8-20261117b
Created: 1794898783318; updated: 1794899519374

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 221 (msg_1e858e280001KHmiIRT1Wakgva)

## Status (recovery check)
- Inspected worktree/git/durable records before acting: clean git state (`git status` empty), recent commits unrelated, no pre-existing `exec-report.md` or witness/data artifacts found. No prior external side effects detected; no actions duplicated.

## Work completed
- Read and used relevant materials: `AGENTS.md`, `docs/problem.md`, `docs/research-framed-certificate-frontier.md`, `scripts/check_framed_strategy.py`, `scripts/strategy_dag_probe.py`, `scripts/generate_optimal_tree.py`, `scripts/transcript_dfs.py`, `scripts/budgeted_dfs.py`.
- Established/verifed baselines: `S(8)=16` (literature baseline per `docs/problem.md`), `ceil(log2(8!))=16`, `F_FJ(8)=16` (computed), bubble framed witness `n=8` accepted at depth 28.
- Attempted exact-height-16 framed DAG witness construction: direct optimal-strategy extraction for `n=8` was not completed with available scripts/prototypes (naive subset/permutation approaches infeasible here; unguided budgeted/transcript DFS not run to completion at `n=8,k=16`). **No explicit checker-accepted height-16 framed DAG witness produced.**
- Constructed and verified a concrete best-effort framed certificate: top-down balanced merge-sort decision tree for `n=8` (identity permutation frames), checker-accepted.

## Verified concrete results
- `witnesses/mergesort_n8_framed_height17.json`: **ACCEPT** (`n=8, depth=17, nodes=80639`, budget 17). Structure: 40320 leaves, 40319 internal, 80638 edges, max in-degree 1, 0 join nodes (full binary decision tree, no sharing). Depth is 1 above `S(8)=16` (and below `O(n log n)=24` path envelope) but node count is far above `O(n^2)=64` (~`2*8!-1`).
- `witnesses/bubble_n8_framed_height28.json`: **ACCEPT** (`n=8, depth=28, nodes=29`) baseline (single compare-exchange path).

## Obstruction / evidence (precise)
- Exact-height-16 framed DAG witness for `n=8` remains unconstructed/unverified in this worktree. Evidence: `F_FJ(8)=S(8)=16` and `ceil(log2(8!))=16` make height 16 necessary and suggest Ford–Johnson is comparison-optimal for `n=8`, but `docs/research-framed-certificate-frontier.md` only states a *plausible* (not audited/all-n-verified) polynomial framed certificate for the FJ upper bound requiring checked recursive frame construction/joins; this run did not produce that explicit encoding. Gap documented as a verified +1-comparison witness (height 17) vs exact 16.

## Durable deliverables in worktree
- `exec-report.md` — problem statement & `S(8)` baseline, methods/tools/commands, concrete results/witness/obstruction with evidence, verification performed, open questions/next falsifiable step.
- `witnesses/mergesort_n8_framed_height17.json`
- `witnesses/bubble_n8_framed_height28.json`

## Next falsifiable step
Explicitly encode and checker-verify a standard Ford–Johnson (merge-insertion) framed strategy for `n=8` (recursive winner frames, loser-slot/rank-envelope tracking, Jacobsthal insertion order, odd case). Falsifiable outcomes: `ACCEPT` at depth 16 (exact witness) or a specific `REJECT`/local invariant-height failure identifying the obstruction in that encoding. Also measure hash-cons/join compression of any obtained height-16/17 tree under the framed meet invariant.
