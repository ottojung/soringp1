# antonina-Yu3NBTcKuS4lPyuLRSHq0b-tube

Session: ses_e0bfde8a1ffe1J0yOgY3Boa3kH
Workspace: /home/lubko/soring-fronts/adversarial-root-forcing-avoidability-alln
Created: 1795095140352; updated: 1795095265228

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 213 (msg_1f403f4b7001dwgt1t4UKRMEn2)

Posted the #301 report and verified the worktree is clean.

Summary of the investigation:
- **Winning-frontier states are avoidable, not forced**, at budget `S(n)`. Each construction state `P_A` can be avoided by using the same construction with a different subset `A'≠A`; that strategy reaches `P_{A'}` instead and still sorts within `t+B=k`. So the enumeration barrier is not converted into a genuine lower bound via forced states.
- **Forcedness is at least as hard as computing `S(n)`**. For `n≥3`, the one-relation poset `P* = (0<1)` is forced at budget `k` iff `k < S(n)` (vacuous when no height-`k` sorter exists; avoidable otherwise by first comparing `0,2`). Thus deciding forcedness decides `S(n)`. No polynomial-time avoidability test is obtained; the hardness proof is the falsifier.
- Characterization: a state is forced iff its avoidance value exceeds `k`; necessary condition `F(P) ≤ k−depth(P)`; antichain and (for `k≥S(n)`) total orders are forced; internal forcedness encodes `S(n)`.

No repository, Lean, test, or ledger changes were made. Report is live on Antonina issue #301.
