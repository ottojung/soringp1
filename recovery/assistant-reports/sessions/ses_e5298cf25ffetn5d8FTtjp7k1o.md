# antonina-IliEBZOWJIgNLYkHrmFooc-wonderful

Session: ses_e5298cf25ffetn5d8FTtjp7k1o
Workspace: /home/lubko/soring-fronts/bidirectional-symmetry-analysis-20261024
Created: 1793910583623; updated: 1793910620048

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 70 (msg_1ad679f98001oQoH8gP6DzaXxx)

**Result: the standard ordinal-sum recurrence is exact, but it does not compose through the antichain root.** For full product states, \(F(A\oplus B)=F(A)+F(B)\): cross-block comparisons are already determined, and the remaining sorting tasks are independent. This is an exact recurrence for those states, not a root-composition method for \(S(n)\).

A tempting extension—summarize each block by its standalone \(F\)-value and compose those summaries across root comparisons—fails even for two 2-element antichains. Their ordinal sum has \(F=2\). Comparing the bottom element of each block splits the six extensions into two three-extension siblings, each with \(F=2\). But comparing the bottom element of the first block with the top element of the second instead gives siblings of sizes 5 and 1, with \(F=3\) and \(0\). Thus equal-size blocks and the same standalone block values do not determine the root comparison’s sibling costs.

This is an exact small obstruction to a **scalar block-value interface**, not a proof that every richer interface fails. The ordinal-sum theorem’s product invariant is lost once a root comparison correlates the blocks; any viable compositional state must retain enough cross-interface order information to represent both outcomes while ensuring a globally consistent strategy. I found no justified state bound or arithmetic-cost analysis that would support a uniform complexity improvement. No files were changed.
