# antonina-AyMoZjTtymrpmSR7gZ3Vnu-announced

Session: ses_e10e94c99ffez4xStuoM0dZzGr
Workspace: /home/lubko/soring-fronts/framed-dag-completeness-alln-20261118
Created: 1795012604827; updated: 1795013414144

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 290 (msg_1ef22f63c001AHAOGCqlwyvgCf)

Posted one concise report to Antonina issue #301 as author `SoringP1 frontier: framed-dag-completeness-alln` (message `sha256:yM1H…`, 2026-11-18T14:49:22Z). Verified exactly one post by that author; no duplicate side effects. Worktree remains clean at `6a96398` (no repo/Lean/test/PR changes).

Summary of the report's substance:
- **Soundness vs. completeness distinguished**: the framed-DAG grammar (comparison arcs with explicit slot permutations, joins intersect guaranteed relations, terminal totals, height ≤ k) is sound and polynomial-time checkable; soundness alone places SORT-BOUND-U in NEXP, not NP.
- **No all-n polynomial construction for an optimal family**: known polynomial framed DAGs (merge sort O(n²) nodes; Ford–Johnson rank-envelope O(n²) query nodes) are suboptimal (merge sort exceeds log₂ n! by (log₂ e−1)n; FJ bound ≠ S(n) for all n).
- **No exponential-frame obstruction proved**: single-policy DAGs are trees (2n!−1 nodes, no hash-consing); all-optimal DAG counts grow (19→65551 for n=3..6) consistently with super-polynomial but n≤6 too small; S_n quotient compresses but also grows (1,2,5,12,19,134). The winning-frontier barrier (2^(¼−o(1)) n log² n states) is an enumeration barrier, not a proof of incompressibility under intersection+permutation merges; forgetful joins can collapse exponential history classes with tiny information loss in structured cases. No formal merge/equivalence condition exists to settle either direction.
- **Conclusion**: completeness remains open; no NP/coNP membership claimed; next obstacle is a canonical merge condition tested against the winning frontier, or an all-n optimal family with provably cheap merges.
