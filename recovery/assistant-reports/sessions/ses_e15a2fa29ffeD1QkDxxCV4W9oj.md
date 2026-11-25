# antonina-4R5SbTztJGUrkRfTBohulE-occupied

Session: ses_e15a2fa29ffeD1QkDxxCV4W9oj
Workspace: /home/lubko/soring301-exec-optplay-dag-width-20261117d
Created: 1794933327401; updated: 1794933426032

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 69 (msg_1ea5e61b0001MXivAYPS5Jb4dZ)

Wrote `exec-report.md` in `/home/lubko/soring301-exec-optplay-dag-width-20261117d`.

The report addresses the requested falsifiable question on the number/width of states on optimal (height-`S(n)`) plays/DAGs (union/layer-width sense, distinct from all reachable/all winning states), with:
- **Precise definitions**: reachable/budget-winning states, optimal height-`S(n)` play/path, single-policy vs optimal-play-union DAG, depth/layer, and width (`w`, `w_~`, `W`, `W_~`) as functions of `n/N`.
- **Argument/evidence**: synthesis of `docs/research-winning-frontier-barrier.md` (superpolynomial optimal-play frontier at exact budget via Sergeev’s asymptotic surplus, `2^{(1/4-o(1)) n (log n)^2}` nonisomorphic states at some depth, infinitely often; finite `n=224` witness) and small-`n` optimal-union evidence from `docs/research-strategy-certificates.md`/`scripts/strategy_dag_probe.py` (`n<=6`, noting limits).
- **Falsification/limits**: what bound would refute the claim, finite-threshold/asymptotic caveat for `k=S(n)`, model sensitivity (union/frontier vs single policy, not a time/space lower bound), and remaining open quantitative gaps.
- **Consequence**: framed-DAG/NP certificate plausibility—explicit frontier/state-layer enumeration is ruled out for polynomial size, while a sound but compressive/non-enumerative polynomial framed certificate at height `S(n)` remains open but constrained.

No repo-wide edits, Lean work, PRs, or comments were made.
