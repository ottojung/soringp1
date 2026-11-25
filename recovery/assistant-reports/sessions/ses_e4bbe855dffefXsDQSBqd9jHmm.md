# antonina-wnRpYGQzwE6S8ocEnNDz4j-asylum

Session: ses_e4bbe855dffefXsDQSBqd9jHmm
Workspace: /home/lubko/soring-fronts/exec-root-potential-audit-20261107
Created: 1794025552602; updated: 1794025604345

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b4417ca0001KHuj47Wqm98gNU)

I’ll inspect the existing issue/front notes and exact minimax tooling first, then test only a sharply specified root-potential candidate against the stated path-versus-reachable-poset distinction. I won’t edit or publish anything.

## Output 121 (msg_1b441fae8001d9tqU9pnf5zHOB)

## Audit result

**No root-reachable potential argument producing an unbounded sublinear gap was established.** The sharpest general identity is an exact telescoping identity for an adversary’s path, but its surplus is bounded above by the *sorting strategy’s height above* \(\log_2(n!)\). By itself it cannot give a stronger lower bound on \(S(n)\). An arbitrary reachable poset with large \(F(P)\), or even a path chosen against one strategy, does not establish a path forced against every height-\(k\) root strategy.

### Exact path identity

Let \(P_0\) be the \(n\)-element antichain. At a state \(P_i\), let \(m_i=e(P_i)\) count its linear extensions. For a queried incomparable pair, let the two child extension counts be \(m_i^+\) and \(m_i^-\). Choose a child with the larger count, breaking ties arbitrarily, and write \(q_i=m_{i+1}/m_i\). Along this path, define local surplus
\[
\delta_i=1+\log_2 q_i.
\]
This is nonnegative because \(q_i\ge \tfrac12\). If the path ends at a total order after \(D\) comparisons, then
\[
\sum_{i=0}^{D-1}\delta_i
=D+\log_2\frac{e(P_D)}{e(P_0)}
=D-\log_2(n!).
\]
This follows by telescoping \(\log_2 m_{i+1}-\log_2 m_i=\log_2 q_i\). In particular, for a fixed height-\(k\) sorter this adversary path has cumulative surplus at most \(k-\log_2(n!)\).

That is an exact **path identity**, not a lower bound on \(S(n)\): the path length is at most the chosen sorter’s height, and the identity supplies no positive lower bound on the path surplus that holds against every root strategy. The identity also does not imply that any selected intermediate poset is reachable under every such strategy.

### Potential candidates and obstruction

- **Extension count \(e(P)\):** yields the usual leaf-count/information bound. The adversary makes each step retain at least half the extensions, giving the identity above, but no additional uniform surplus lower bound.
- **One-ply minimax \(F(P)\):** is an exact *remaining* worst-case value. A state with large \(F(P)\) is relevant only if the root strategy can be forced to reach it with enough depth remaining. Reachability under some strategy is insufficient.
- **Combinations:** a potential combining these quantities would need to prove a root-level, strategy-independent forcing statement—not merely certify a bad reachable state or a path against a particular strategy. No such statement emerged from this audit.

The known Sergeev upper bound \(S(n)-\log_2(n!)=O(n/(\log n)^{1/5})\) is compatible with the path identity: it bounds the adversary path’s surplus *from above* for a sorter supplied by that construction. It does not rule out a smaller lower bound, but any proposed forced surplus must also be consistent with this sublinear upper bound.

### Scope and prior work

The exact-value tooling in this checkout covers \(n\le6\); literature records \(S(7)=13\), but this audit did not produce a new \(n\le7\) minimax counterexample. Thus this is an obstruction to the proposed inference, not a computational disproof of every possible refined potential.

The comparison with the named fronts is structural: the prior root-adversary, amplification, entropy-deficit, and telescoping investigations already flag the gap between local/path facts and root forcing. The framed-certificate note’s annotation-majority identity is for a walk through a certificate’s annotations; it is **not** a theorem about the larger-child adversary against every root sorter. This audit does not upgrade it to one. Issue #48’s comment 6350140834 was not independently retrieved here, so I cannot claim a comment-by-comment comparison.

**Conclusion:** the concrete larger-extension-child surplus has a clean exact lemma, but is unsuitable on its own for proving an unbounded sublinear lower gap \(S(n)-\lceil\log_2(n!)\rceil\). The missing ingredient is a root-forcing theorem that survives minimization over all sorting strategies.
