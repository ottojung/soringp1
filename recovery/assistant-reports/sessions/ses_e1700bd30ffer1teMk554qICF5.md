# antonina-dsltg2FbVtaVinVbK3v8Um-clad

Session: ses_e1700bd30ffer1teMk554qICF5
Workspace: /home/lubko/soring301-exec-fj-dag-n5-20261117
Created: 1794910405386; updated: 1794910744756

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 232 (msg_1e9043d9c001jJS0HD3mwsRUZZ)

## Result (ford-johnson-framed-dag-n5-check)

Constructed and mechanically verified an explicit permutation-framed strategy DAG certificate for the standard Ford–Johnson (merge-insertion) procedure on `n=5` (per `docs/research-framed-certificate-frontier.md` §3 comparison schedule), in tree form with identity edge permutations.

- **Witness:** `artifacts/fj5_framed_dag/fj5_framed_dag.json` (format `n=5, budget=7`, framed `perm` on every edge)
- **Checker:** `python3 scripts/check_framed_strategy.py artifacts/fj5_framed_dag/fj5_framed_dag.json` → **`ACCEPT: n=5, depth=7, nodes=239`** (`artifacts/fj5_framed_dag/checker.txt`)
- **Stats:** 239 nodes (119 comparison, 120 leaves), 238 directed outcome edges, root-to-leaf path depths 8×6 and 112×7 (max/achieved height **7**)
- **Height vs bounds:** achieved **7** = **F_FJ(5)=7** (`sum_{j=1}^{5} ceil(log2(3j/4))`) = **S(5)=7**

**Construction basis (durable report):** `exec-report.md`. FJ schedule followed on slots 0–4: pair `(0,1),(2,3)` (pair-winner = larger), compare winners, insert loser of smallest winner before it, insert straggler `4` by binary search into the chain, insert remaining loser before its winner (bounded prefix). Generated as an adaptive feasible-outcome tree with identity slot permutations; verified sound by the checker.

**Obstruction/limitation (not achieved in this run):** a *joined* rank-envelope DAG per §3 (shared post-insertion states via relaxed common windows/intersection with explicit nontrivial relabelling frames) was not constructed. The substantive difficulty is correct frame/boundary bookkeeping for joins across different insertion ranks (canonical relabelling, preserved relaxed rank windows for subsequent Jacobsthal insertions, recursive/odd cases), as §3 notes requires independent frame/boundary review. The unjoined tree is small and fully verified for `n=5`.

**Next step:** construct and checker-audit a joined FJ framed certificate for small `n` (starting at 5) with explicit non-identity insertion-rank join frames to validate the §3 rank-envelope invariant/boundary arithmetic before any all-`n` claim; cross-check schedule/counts against `scripts/upper_witness.py` (`n<=6` exhaustive). All durable deliverables are in `exec-report.md` and `artifacts/fj5_framed_dag/`.
