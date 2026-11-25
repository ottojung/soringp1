# antonina-QYqhzIOD4HvyzMHmihugAc-distrust

Session: ses_e03b6db6dffe5Mbh12279Ybm6b
Workspace: /home/lubko/soring-fronts/framed-dag-exact-budget-n12-20261121
Created: 1795234014499; updated: 1795234407118

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 351 (msg_1fc4f12d9001j55relRbFJK5ps)

Posted the finding to Antonina board issue #301 (comment created at 2026-11-21T04:13:18Z). No repository, Lean, test, or workflow changes were made; the worktree remains clean.

Summary of the posted finding:
- **Result:** No explicit checker-verified framed DAG at budget 30 for n=12 was constructed; the question remains open for the general framed grammar. No completeness gap was demonstrated.
- **Evidence:** S(12)=30 and Ford–Johnson achieves F_FJ(12)=30, so FJ is an optimal strategy; unjoined FJ framed trees work for small n (verified n=5: 239 nodes, depth 7) but have 12! leaves at n=12; polynomial size requires the unaudited joined rank-envelope construction, whose recursive frame lifting and odd/straggler case remain unverified. The strict PRE envelope is already incomplete at n=5, but that is a barrier for that strict grammar, not the general framed grammar.
