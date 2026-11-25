# antonina-pqIKsDLGmOLXoiz2EE6n1B-yielding

Session: ses_e037c301bffe90K6xunt76rfBB
Workspace: /home/lubko/soring-fronts/framed-dag-merge-insertion-nozeros-20261121
Created: 1795237859389; updated: 1795238337956

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 456 (msg_1fc8b0872001Q8xUv0QB3CublU)

Posted result to #301.

Checker verdict for the merge-sort-style (no zero-comparison) framed DAG:
- **n=5: ACCEPT, depth=8, nodes=11**
- **n=6: ACCEPT, depth=11, nodes=16**

Height comparison:
- `F_FJ(5)=7`, `F_FJ(6)=10`; merge-sort height is `8`/`11` (one more than FJ at both n).
- Trivial bound `n(n−1)/2`: `10`/`15`; merge height improves on it by 2/4.
- Node count is polynomial (`binom(n,2)+1`), and frames are prefix-determined (no value-dependent zero-comparison moves).

No repository changes were made.
