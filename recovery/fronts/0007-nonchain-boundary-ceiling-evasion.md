# nonchain-boundary-ceiling-evasion

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ujb3xjwq0ZANamQjR2maqv-dron

## exit_state

succeeded

## question

For every fixed c, must every stage sequence from the n-antichain to a total order, with per-stage height at most c*log2(n+2) applied uniformly to all extensions of an arbitrary (not chain or merge-tree) boundary invariant, pay aggregate ceiling rounding loss Omega(n) across sufficiently large n, or can some boundary class preserving cross-chain correlations evade it with o(n) total loss?

## basis

Antonina #301 posts of 2026-10-27 08:21-08:25 (chain checkpoint no-go covering single-chain boundaries only, flagged next route to non-chain boundaries), 08:54 and 14:35 (fixed-merge-tree no-go, verified); the per-stage ceil(log2(e(F)/e(F_prime))) reset framework and telescoped loss pipeline of 09:14; not covered by any ledger front, dated front directory, or currently held worker lease on #301.

## falsifier

Exhibit an all-n boundary poset family and per-stage sequences of height at most c*log2(n+2) whose aggregate ceiling loss over extension-count ratios telescopes to o(n), thereby evading both the 2026-10-27 fixed-merge-tree and bounded-batch chain-checkpoint interval obstructions.

## implication

A negative theorem would be the first architecture-independent no-go for all unit-stage certificate framings, sharply restricting what an exact-height SORT-BOUND-U certificate may look like; a positive staged construction would be the first skeleton toward boundary-class generality for #47.

## finding_unverified

Bug in `ext_count` — iterating the placed set instead of the available elements. Fixing:
 Toolkit works: e.g. for n=3, exactly the e=3 posets (chains+free element) lack an exact-ratio-2 step. Now the key experiment: **BFS over abstract shapes** where an edge `P→Q` (ratio exactly 2, loss 0) exists iff some critical pair of `P` has isomorphic branches `P+(u<v) ≅ P+(v<u)`. Does a zero-loss ladder reach a total order?
BFS stalls immediately — let me debug: print reachable shapes' e-values and dead ends.
The BFS barely progresses from the antichain with pure ratio-2 single comparisons beyond disjoint pairs. Now the right metric: **maximal loss-0 bit-depth** — longest loss-0 (ratio exactly 2) ladder from the antichain, i.e., how much of log2(n!) you can descend without paying die-rounding loss at all.
Key structural insight discovered (verifiable): in this framework, staged full-reset certificates correspond exactly to **divisor chains of n!**, and the aggregate ceiling loss depends only on the multiset of integer stage quotients:

- loss = log2(2^M / n!), where M = Σ ceil(log2 q_j), Π q_j = n!, q_j ≤ 2^{c·log2(n+2)}
- so the question decomposes into (i) pure arithmetic of factoring n!, and (ii) per-stage *realizability* as framed-superposet comparison modules.

Let me compute the arithmetic lower bound — if that alone already forces Ω(n), realizability is moot.
Pure arithmetic alone does **not** force Ω(n) (arith loss stays ≤ ~4 bits at c=1, ≤1.2 at c≥2 for n≤14). Any Ω(n) obstruction must come from module realizability. Now the decisive experiment: build the exact module-realizability graph over shapes (multiset-lifting of branch pairs, height ≤ 3) and Dijkstra the **minimum realizable aggregate loss** from the antichain to a total order.
Full pair enumeration is overkill. Restructuring: lazy forward exploration from the antichain only.
**No new theorem or counterexample was established.** The general Ω(n)-versus-o(n) question remains unresolved.

The interrupted work produced a precise reduction within the #301 full-reset framework: if each stage resets to framed copies of one boundary poset, its extension-count ratio \(q_i=e(F_i)/e(F_{i+1})\) is an integer, and the ratios multiply to \(n!\). Thus the aggregate ceiling loss is
\[
\sum_i\bigl(\lceil\log_2 q_i\rceil-\log_2 q_i\bigr)
=\sum_i\lceil\log_2 q_i\rceil-\log_2(n!).
\]
This separates a **counting-only** factorization problem from the harder requirement that each quotient be realized by a comparison module with the required common framed boundary. Small-\(n\) arithmetic experiments did not suggest an Ω(n) obstruction; they do **not** establish an all-\(n\) bound or a realizable construction.

A concrete failed route was searching only for one-comparison, zero-loss resets. Exhaustive computation through \(n=6\) found that such ladders can stall: for \(n=4,5,6\), the longest searched ladders ended at extension counts \(3,15,45\), respectively, rather than at a total order. This is a limitation of that restricted approach, not evidence that arbitrary boundary families must incur linear loss. The broader module search did not finish, and no result about certificate completeness follows from the extension-count calculation alone.

Recovery check: the repository worktree is clean; there were no commits or board posts. Only temporary experiment scripts were written under `/tmp/opencode`. The durable ledger entry remains `running`; I did not alter it or the board.

## Other metadata

```json
{
  "finished_at": 1793130504.746113,
  "started_at": 1793123968.5139947
}
```
