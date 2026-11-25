# antonina-hsKGNF50s1tgFjipe837bx-suture

Session: ses_e037c0facfferF1drwU4uyCqsh
Workspace: /home/lubko/soring-fronts/framed-dag-lowerbound-omega-n-20261121
Created: 1795237867658; updated: 1795238049256

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 239 (msg_1fc86a6ea001b8D5W8x9nI7I1P)

Posted the result to Antonina issue #301 (comment at 2026-11-21T05:14:01Z). No repository changes were made.

Summary of what was recorded:

- **Result type:** obstruction to the simple counting lower bound, not a proof.
- The number of distinct insertion positions does not by itself force exponential framed-DAG nodes: FJ’s weak-window rank-envelope handles exponentially many histories with O(n²) nodes and only O(log n) total forgetting.
- Eliminating the constant-factor (4/3) slack in FJ’s insertion intervals requires exact/value-dependent insertion ranks; exact-position sharing fails at n=5 because zero-comparison insertions attach slot moves whose correctness depends on value state before the edge, forcing incompatible frames on shared edges.
- The argument does not cover non-insertion architectures (e.g., Sergeev’s coupled containers), so a universal Ω(n) surplus lower bound for all polynomial-size framed DAGs remains open. Next obstacle identified: either exhibit a polynomial frame scheme for Sergeev’s containers or prove any sound join collapses value-dependent ranks/container parameters.
