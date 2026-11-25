# antonina-IwlXeAJd54JYpMDbKPZVdZ-repaired

Session: ses_e17cdfad5ffenufQqhXAtYfGmI
Workspace: /home/lubko/soring301-exec-framed-dag-n9-20261117
Created: 1794896954672; updated: 1794897695425

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 187 (msg_1e83d1a77001QqpkUiZte4XCX5)

Inspected existing state first (recovery): clean git worktree, no prior `exec-report.md` or n=9 framed witness files, recent commits unchanged — no evidence of prior external side effects from the interrupted turn, so no actions were duplicated.

**Durable deliverables added**
- `exec-report.md`: problem statement and `S(9)=19` baseline (repo/literature-cited, not re-proved), methods/commands, concrete results, verification, obstruction/evidence, and next falsifiable steps. Distinguishes verified facts from cited/conjectural items.
- `witness_bubble_n9.json`: explicit permutation-framed strategy DAG certificate for `n=9` (triangular bubble, budget 36).

**Work performed (verified)**
- Reviewed `docs/research-framed-certificate-frontier.md`, `scripts/check_framed_strategy.py`, `scripts/strategy_dag_probe.py`, `scripts/generate_optimal_tree.py`, `scripts/evaluate.py`, `scripts/upper_witness.py`, and relevant tests/docs for baseline (`S(9)=19`, `M(9)=19`).
- Checked/constructed framed witnesses with the repo soundness checker:
  - `python3 scripts/check_framed_strategy.py --bubble 4` → `ACCEPT: n=4, depth=6, nodes=7`
  - `python3 scripts/check_framed_strategy.py --bubble 9` → `ACCEPT: n=9, depth=36, nodes=37`
  - Generated & saved `witness_bubble_n9.json` via `triangular_bubble_certificate(9)`; rechecked: `python3 scripts/check_framed_strategy.py witness_bubble_n9.json` → `ACCEPT: n=9, depth=36, nodes=37`
- Structural context: `python3 scripts/strategy_dag_probe.py --max-n 4` (poset minimax/hash-consed DAG sizes/quotients for n≤4; different representation than framed slot certificates).
- `python3 scripts/upper_witness.py` (no args) exceeded 120s timeout and was not required; interface inspected (`--help`).

**Outcome**
- **Exact-height-19 framed DAG witness for `n=9`: not produced/verified.** Smallest constructed and checker-verified framed witness here is bubble at **depth 36, 37 nodes** (36 compare nodes + 1 leaf, path DAG, 72 edge records), saved as `witness_bubble_n9.json`.
- Report documents evidenced obstruction: merge-sort framed route is polynomial-envelope (`O(n^2)` nodes, `O(n log n)` path) but ~20 comparisons for `n=9` (not exact); Ford–Johnson gives `M(9)=19` but complete recursive framed embedding/permutations/odd-case needs audit and no checked generator/certificate exists here; lifting a known optimal `n=9` strategy into sound joined framed format not completed. No exhaustive framed-DAG search attempted (resource/representation limits noted).
- Next falsifiable steps in `exec-report.md`: implement/audit framed merge-sort and/or Ford–Johnson generators for `n=9` and verify with `check_framed_strategy.py`, or lift a known optimal `n=9` strategy into framed-certificate form and measure nodes/edges/depth/profile.
