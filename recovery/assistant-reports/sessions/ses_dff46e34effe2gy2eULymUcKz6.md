# antonina-jQrNoQ8AELXndWZp43Jj76-mcmaster

Session: ses_dff46e34effe2gy2eULymUcKz6
Workspace: /home/lubko/soring-fronts/space-reduction-o-n-20261122
Created: 1795308461268; updated: 1795308719532

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 207 (msg_200bd05500015hklxVXm6p5l73)

Posted a concise update to board issue #301.

**Finding:** No construction of an \(O(N)\)- or polylog\((N)\)-space exact evaluator with time \(2^{O(n\log^2 n)}\) was found, and no all-\(n\) space lower bound was proved. The exact obstruction is the budgeted DFS’s comparison-path stack: depth \(\Theta(n\log n)\) frames, each needing \(\Omega(\log n)\) bits for the chosen pair and cursor over \(\Theta(n^2)\) pairs, giving \(\Omega(n\log^2 n)\) bits for the function problem and \(\Omega(N\log N)\) bits for nontrivial decision instances. The reachability workspace can be reduced to \(O(\log^2 n)\) bits via Savitch without changing the time bound, but it does not remove the dominant stack term. The memoized poset DP avoids the deep stack but needs \(2^{\Theta(n^2)}\) space. Beating the bound would require a shallower exact search or a compressed representation of the current poset; neither is currently available. No repository/Lean changes were made.
