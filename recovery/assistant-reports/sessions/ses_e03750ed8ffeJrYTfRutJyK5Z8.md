# antonina-qlWYBYlgyEUEOS8rfRbdxs-mania

Session: ses_e03750ed8ffeJrYTfRutJyK5Z8
Workspace: /home/lubko/soring-fronts/exec-framed-forgetting-loss-lb-20261121
Created: 1795238326663; updated: 1795238516144

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 212 (msg_1fc8dc019001L3r0ddqnf2Hs9g)

Posted the finding as a single comment to Antonina board issue #301 (comment id `sha256:E7wpy_8VRMMCm1MQwOs-vKd_j7xH2FbuPiQeui5b7Qg`, created 2026-11-21T05:21:43Z). No repository, Lean, test, or workflow changes were made; scratch work was only under `/tmp/opencode`.

Summary of the note:
- The identity is a necessary condition, not by itself a size lower bound. Merge sort framed DAG (O(n²) nodes) has λ=0 on every comparison edge and total imbalance D_ms(n)−log₂(n!) = (0.4427+o(1))n = O(n), so a polynomial DAG with O(n) total loss is constructible. Its height is info+Θ(n), not exact S(n).
- Exact budget S(n)=log₂(n!)+o(n) allows only o(n) total (1−H+λ); no current construction achieves both o(n) surplus and o(n) loss (Sergeev has o(n) surplus but no polynomial framed certificate; rank-envelope has O(log n) forgetting but Θ(n) surplus).
- Winning-frontier state count (2^{Ω(n log² n)}) does not yet convert to a bit-loss lower bound because exponentially many histories can be coarsened with O(log n) bits when a weak invariant exists.
- Implication: the open question “does some optimal sorter admit a polynomial-size framed DAG at height S(n)?” remains open; NP membership is neither established nor refuted by this identity.
