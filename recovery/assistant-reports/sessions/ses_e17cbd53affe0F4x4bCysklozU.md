# antonina-JScpyjeRH9n286J4mNRy2K-openshaw

Session: ses_e17cbd53affe0F4x4bCysklozU
Workspace: /home/lubko/soring301-exec-framed-dag-n11-20261117
Created: 1794897095557; updated: 1794897708701

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 145 (msg_1e83d4916001HD35kjf5A9DZ18)

Inspected the worktree first (clean git state, no existing `exec-report.md` or `*witness*n11*` artifacts) and continued only unfinished work; no commits or external actions were taken.

## Durable deliverables (this worktree)
- [`exec-report.md`](exec-report.md): problem statement and `S(11)` baseline, methods/tools/commands, concrete results/obstruction with evidence, verification performed, open questions and next falsifiable step.
- [`witness_bubble_n11.json`](witness_bubble_n11.json): explicit framed strategy DAG certificate (bubble/compare-exchange path form), saved.
- [`probe_max5.txt`](probe_max5.txt): `strategy_dag_probe.py --max-n 5` output, saved.

## Key results (precise)
- **`S(11)` baseline (literature/arithmetic context, not newly proved here):** `ceil(log2(11!)) = ceil(25.2504927...) = 26`, and Ford–Johnson bound `F_FJ(11)=∑_{j=1}^{11} ceil(log2(3j/4)) = 26`, consistent with equality of optimal comparison counts with the information bound through `n=11` as cited in `docs/literature.md`.
- **Exact-height-26 framed DAG witness for `n=11`: not produced/verified.** No explicit, checker-accepted permutation-framed strategy DAG certificate of height `26` was constructed.
- **Best verified framed witness found:** `witness_bubble_n11.json` (`n=11`, `budget=55`).
  - Checker: `python3 scripts/check_framed_strategy.py witness_bubble_n11.json` → `ACCEPT: n=11, depth=55, nodes=56`
  - Profile: **56 nodes, 55 edges/comparisons on the path, depth 55** (path-shaped). Nodes are `O(n^2)` in form but depth is non-optimal (>> 26 and above the `~n log2 n` scale for this instance), so this certifies correctness at budget 55, not optimality.
- **Obstruction/evidence:** a 26-comparison optimum at the info floor (`F_FJ(11)=S(11)`) is plausible as a strategy but does not yield an explicit framed certificate; completing/auditing the recursive Ford–Johnson rank-envelope frame/join construction (§3 of `docs/research-framed-certificate-frontier.md`) was not done here (permutation/anchor/boundary bookkeeping blocker). `probe_max5.txt` shows poset/minimax DAG growth for small `n` (e.g. `n=5`: unshared-all 26541, DAG(all) 1551, quotient(all) 19), evidencing naive enumeration infeasibility though in a different representation than framed certificates.

## Verification performed
- `witness_bubble_n11.json`: **ACCEPT** by `scripts/check_framed_strategy.py` (`n=11, depth=55, nodes=56`).
- Local arithmetic: `11! = 39,916,800`, `log2(11!) ≈ 25.2504927`, `ceil=26`, `F_FJ(11)=26`.
- Probe regenerated to `probe_max5.txt` (`strategy_dag_probe.py --max-n 5`, exit 0). `S(11)=26` itself was **not** kernel-checked/re-proved here (literature/derived baseline).

See [`exec-report.md`](exec-report.md) for full commands, tables/observations, and the concrete next falsifiable step (implement/check a Ford–Johnson framed DAG generator for `n=11` against the soundness checker, or isolate and verify a minimal insertion/join sub-certificate to localize the ambiguity).
