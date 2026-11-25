# antonina-uegS9T1tMNn6KYIcfNMBDE-gaping

Session: ses_e5291538affe3q4sEhu1Bu6Bta
Workspace: /home/lubko/soring-fronts/bidirectional-symmetry-analysis-20261024
Created: 1793911073912; updated: 1793911108287

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 55 (msg_1ad6ef95b0013OrnKgea52wzYm)

**Scoped no-go:** strategy-continuation equivalence under outcome-preserving relabelling gives an exact recurrence, but the known symmetry quotient and winning-frontier results do not establish an asymptotic time improvement for exact evaluation. I found no sound argument that on-demand evaluation avoids the frontier in the worst case, nor a general obstacle proving that it cannot.

Let \(F(P)\) be the exact remaining minimax cost from a partial order \(P\), and let \([P]\) denote its isomorphism class. The quotient recurrence is
\[
G([P]) =
\begin{cases}
0 & P\text{ total},\\
1+\min_{x\parallel y}\max\{G([P+x<y]),\,G([P+y<x])\} & \text{otherwise}.
\end{cases}
\]
It preserves **both** sibling outcomes: relabelling maps each legal comparison and each oriented successor to the corresponding comparison and successor. Thus the multiset of child classes is independent of the chosen representative, and \(G([P])=F(P)\). In particular, \(G([\varnothing])=S(n)\). This is the established relabelled-poset DP, not a new quotient.

A more selective cache may merge two states only when their *entire rooted continuations* are isomorphic as outcome-labelled comparison trees. That relation is an exact recurrence congruence if it preserves terminal status, legal comparison choices, and the two oriented children (up to a consistent bijection). But this condition supplies no new compression theorem: determining continuation isomorphism may require evaluating the same descendant minimax structure, and without a computable, stronger invariant it is a definition rather than an algorithmic improvement.

The complexity accounting is correspondingly limited:

- The labelled state DP has at most \(3^{\binom n2}=2^{O(n^2)}\) states and polynomial work per state.
- Quotienting by relabelling reduces the count by at most a factor \(n!\), so the worst-case exponent remains \(2^{O(n^2)}\). Canonicalization cost must also be counted; naive canonicalization can itself cost \(n!\).
- Automorphism-orbit move pruning is exact, but asymmetric posets can have trivial automorphism group and \(\Theta(n^2)\) incomparable pairs, so it has no universal subquadratic move-count guarantee.
- The winning-frontier theorem gives \(2^{(1/4-o(1))n(\log n)^2}\) nonisomorphic winning states at a depth, even at the exact optimum. It rules out methods that must enumerate that entire frontier, **not** selective minimax evaluation or any general running-time bound.

**Conclusion:** exact continuation congruence is well-defined, but no provable asymptotic benefit follows from it absent a concrete stronger canonical form or a theorem bounding the number of continuation classes visited. Conversely, the cited results do not prove that the subgroup quotient cannot improve the \(2^{O(n^2)}\) exponent: they constrain full-state enumeration and within-state orbit pruning, not all selective algorithms. This is a scoped no-go for the proposed inference, not a universal barrier.

Scratch-only; no source files or posts were changed.
