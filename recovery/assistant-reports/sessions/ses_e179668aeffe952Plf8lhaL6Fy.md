# antonina-xQ0GCMBRygn0grP9GcVFEh-polls

Session: ses_e179668aeffe952Plf8lhaL6Fy
Workspace: /home/lubko/soring301-exec-framed-dag-n14-20261117c
Created: 1794900596625; updated: 1794900846119

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 188 (msg_1e86d3d3f001JvpeSHBUclCsPx)

## Done
- Wrote `exec-report.md` with: problem statement and `S(14)` baseline (literature/index + `ceil(log2(14!))=37`, `M_FJ(14)=38`), methods/commands/tools, concrete results, verification, and open/next falsifiable steps.
- Constructed and saved a **verified framed DAG witness** (sound, non-optimal): `witnesses/bubble_n14_framed.json` (`n=14`, budget/depth `91`, nodes `92`, edges `182`, path-comparisons `91`). Verified with `scripts/check_framed_strategy.py` → `ACCEPT: n=14, depth=91, nodes=92`.
- Saved measurements/baseline: `data/n14_framed_witness_results.json` (`"height_37": false`, includes S(14) baseline and witness profile).
- Ran strategy-DAG scaling probe: `data/strategy_dag_probe_max5.txt` (`--max-n 5`, `RC=0`); `--max-n 6` attempt timed out at 120s leaving `data/strategy_dag_probe_max6.txt` empty.

## Outcome (precise)
- **No explicit/checkable permutation-framed strategy DAG certificate of exact height 37 for n=14 was constructed or verified** in this run. Best verified framed DAG witness here is the triangular-bubble certificate at height 91 (accepted by the soundness checker) with exact counts above.
- Reported evidenced obstruction/context (not a proof of nonexistence): lack of in-repo optimal/FJ framed generator, explicit generators not reaching 37 (`M_FJ(14)=38`, bubble 91), and single-policy optimal-tree size `2*n!-1` explosion (probe data; ~1.74×10^11 nodes extrapolated at n=14) vs open all-n polynomial-size framed completeness at exact `S(n)`. Next falsifiable step is to implement/check a stronger framed generator (e.g. framed merge-insertion/merge-sort per `docs/research-framed-certificate-frontier.md`) for a certified depth-37-or-smallest witness at n=14.
