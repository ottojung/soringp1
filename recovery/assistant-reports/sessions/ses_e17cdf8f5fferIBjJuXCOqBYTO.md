# antonina-WKhTjiBdT3bYrJZuywckac-salary

Session: ses_e17cdf8f5fferIBjJuXCOqBYTO
Workspace: /home/lubko/soring301-exec-framed-dag-n10-20261117
Created: 1794896955248; updated: 1794897761662

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 189 (msg_1e83e21bc001hjnfG9KXv80dMo)

## Inspection / continuity
- Inspected existing state first (no `exec-report.md`, clean git status, recent commits only). No prior external side effects from this task were found to duplicate.
- Reviewed relevant materials/tools: `docs/research-framed-certificate-frontier.md`, `docs/research-strategy-certificates.md`, `docs/research-upper-witnesses.md`, `scripts/check_framed_strategy.py`, `scripts/strategy_dag_probe.py`, `scripts/generate_optimal_tree.py`, `scripts/upper_witness.py`.

## Outcome
- **Exact-height-22 framed DAG witness for `n=10` (S(10)=22): not constructed/verified.** Direct optimal strategy extraction/encoding was not feasible with available tools (permutation-state/poset enumeration practical only for very small `n`), and no existing explicit framed certificate at height 22 was found.
- **Verified framed witness produced (non-optimal height):** `witness_bubble_n10.json` (triangular bubble/exchange certificate).
  - Checker: `python3 scripts/check_framed_strategy.py witness_bubble_n10.json` → `ACCEPT: n=10, depth=45, nodes=46`
  - Profile: `n=10`, depth `45`, nodes `46`, edges `90`, path/tree structure (depth `n(n-1)/2`, above `S(10)=22`).
- **Baselines:** `S(10)=22` (known); Ford–Johnson bound `M(10)=22` via `scripts.upper_witness.fj_upper_bound` (achieves exact height in count, but no explicit framed-DAG encoding produced); standard merge-sort worst-case comparisons for `n=10` = 25.
- **Attempted lower-height construction (obstruction evidence):** naive unshared-tree merge-sort framed encoding (sequential composition, no joins/sharing) verified at small `n` but exploded in nodes and timed out for `n=10` (>120s, no artifact):
  - `n=4`: depth 5, nodes 47 (accepted)
  - `n=5`: depth 8, nodes 239 (accepted)
  - `n=6`: depth 11, nodes 1439 (accepted)
  - `n=7`: depth 14, nodes 10079 (accepted)
  - `n=10`: not completed (target depth ~25). Evidence: without DAG join/sharing, path-efficient strategies incur exponential explicit certificate size, blocking emission at `n=10`.

## Deliverables (durable, in worktree)
- `exec-report.md` — problem statement & S(10) baseline, methods/tools/commands, concrete results/obstruction with evidence, verification performed, and open questions/next falsifiable steps (incl. comparison to `O(n^2)` nodes / `O(n log n)` path envelopes).
- `witness_bubble_n10.json` — checked framed certificate (ACCEPT, depth 45).
- `framed_dag_n10_results.json` — measured results summary.

All claims above distinguish verified artifacts/checker results from literature baselines and unverified/conjectural constructions. No commits or external posts were made.
