# antonina-49bQb8OVcjPjc104lAS3tG-domestic

Session: ses_e17966a4affeA7hVieQzpdUeWi
Workspace: /home/lubko/soring301-exec-framed-dag-n6-20261117c
Created: 1794900596258; updated: 1794900748100

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 140 (msg_1e86bb9ba001Ot11dsNPFvSeo5)

Produced and verified an explicit permutation-framed strategy DAG certificate for n=6 at exact height S(6)=10 (unshared decision tree form), saved witness/data files, and wrote `exec-report.md`.

**Key results (experiment, checker-verified):**
- **S(6) baseline:** minimax recomputation gives `S(6)=F(empty)=10` (matches known baseline in repo/docs; information lower bound `ceil(log2(6!))=10`).
- **Witness:** `witness_n6_h10_tree.json` (`{"n":6,"budget":10,...}`), unshared decision tree with identity slot permutations on all edges, no join merges.
- **Verification:** `python3 scripts/check_framed_strategy.py witness_n6_h10_tree.json` → `ACCEPT: n=6, depth=10, nodes=1439`
- **Exact counts/profile:** 1439 nodes total, 719 internal comparison nodes, 720 leaves (=6!), 1438 edges, verified depth 10, budget 10, root comparison `[0,1]`.
- **Nodes per depth:** `{0:1, 1:2, 2:4, 3:8, 4:16, 5:32, 6:64, 7:128, 8:240, 9:416, 10:528}`.
- **Structural observations:** this optimal-policy witness has `n!` distinct total-order leaves and no poset-state repetition under hash-consing for the chosen policy (`hash_cons_poset_dag_single_policy_nodes = 1439`, equal to unshared tree size). It is a concrete fixed-n exact-height witness but, as an `n!`-leaf optimal decision tree, not evidence of a polynomial-size all-n certificate at height `S(n)` (cf. polynomial-size non-optimal framed constructions in `docs/research-framed-certificate-frontier.md`).

**Durable artifacts saved (worktree):**
- `exec-report.md` — problem statement/baseline, methods/tools/commands, concrete results with evidence, verification performed, open questions and next falsifiable step.
- `witness_n6_h10_tree.json` — checked framed DAG certificate (height/budget 10).
- `witness_n6_h10_measurements.json` — exact counts/profile and structural measurements.

**Next falsifiable step (recorded in report):** attempt a join-merged/relabeled framed DAG for `n=6,k=10` (align isomorphic subproblems via permutations and intersect guarantees), verify with `scripts/check_framed_strategy.py`, and compare node count to 1439. No claim of resolution/completion of the open problem is made.
