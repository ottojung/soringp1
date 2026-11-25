# antonina-7onhWKuxrJVJ0Q2ZSdiegv-caprice

Session: ses_e5291e5a0ffe3uTogJjG86TGkW
Workspace: /home/lubko/soring-fronts/fo-tc-varying-block-program-20261105
Created: 1793911036514; updated: 1793911063414

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ad6e1a7f001m0Zq2F3NdhICvx)

I’ll trace the existing DFS argument and compare it against the budgeted-DFS note, then account explicitly for configuration storage, counters, cursors, and time overhead. I’ll keep this analysis-only and won’t edit the repository.

## Output 23 (msg_1ad6e2b4e001rve8RbomnimHVi)

**Yes.** Replacing the per-query BFS workspace with deterministic Savitch reachability gives the DFS a sharper *parameterized space* bound:
\[
O\!\bigl(k\log(n+2)+\log^2(n+2)\bigr)
\]
work bits for `CanSort(P,k)` on an explicit `n`-element poset, plus the read-only input head position if `P` is input-encoded. This is below \(O((k+n)\log n)\) when \(k=o(n)\), but **does not improve the worst-case unary space bound**: the nontrivial threshold range includes \(k=\Theta(n\log n)\), where the transcript alone costs \(O(n\log^2 n)\) bits.

### Accounting

At a DFS node, store the path transcript once, not once per frame. Each path comparison contributes two labels, or \(O(\log(n+2))\) bits; each active frame needs a candidate-pair cursor, branch/return flags, and a remaining-budget counter, also \(O(\log(n+2))\) bits. With at most \(k+1\) frames, stack and transcript together use \(O(k\log(n+2))\) bits. The root pair-enumeration cursor and all scalar counters are covered by this bound (or by an additive \(O(\log n)\) for the degenerate \(k=0\) case).

To test whether \(y\) is reachable from \(x\) in the transcript graph, use Savitch’s directed reachability algorithm on \(n\) vertices. Its recursion depth is \(O(\log n)\); each level stores a midpoint vertex and bounded-length/path-length control, \(O(\log n)\) bits. Thus one reachability query uses \(O(\log^2(n+2))\) bits. Queries are sequential: totality checks, pair enumeration, and return-from-child checks reuse the same workspace. No closure matrix, visited vector, queue, or incomparable-pair list is retained across frames. Peak space is therefore the sum, not a product:
\[
O(k\log(n+2)) + O(\log^2(n+2))
= O(k\log(n+2)+\log^2(n+2)).
\]
For \(n\le 1\), or \(k=0\), handle the trivial cases directly; they do not change the bound.

A “succinct closure” does not improve this accounting by itself: a closure representation that supports exact comparability still needs a query procedure, whose workspace must be counted. The transcript plus Savitch reachability already supplies such a representation without storing the closure.

### Time cost

Let \(B=\binom n2\). The DFS makes at most \((2B)^k\) recursive calls. At each call, a conservative implementation may test all \(B\) pairs, and each test performs up to two reachability queries; totality testing performs \(O(n^2)\) more. Savitch reachability on an \(n\)-vertex graph can be implemented in time \(n^{O(\log n)}=2^{O(\log^2 n)}\), with polynomial factors for transcript-edge lookup. Consequently a conservative overall bound is
\[
(2B)^k\cdot 2^{O(\log^2 n)}\operatorname{poly}(n+k)
=2^{O(k\log(n+2)+\log^2(n+2))}\operatorname{poly}(n+k).
\]
Relative to BFS-based DFS, this adds at most a quasipolynomial-in-\(n\) factor per node, \(2^{O(\log^2 n)}\). It is absorbed by the existing \(2^{O(k\log n)}\) node-count exponent when \(k\ge \Omega(\log n)\). For smaller \(k\), it is safer to retain the displayed additive \(\log^2 n\) term rather than claim the same time bound. This is a space-for-time tradeoff, not a time improvement.

### Useful regime and limitations

For a concrete regime, if \(k\le n^{1/2}\), the Savitch version uses
\[
O(n^{1/2}\log n+\log^2 n)
\]
bits instead of the BFS-based \(O(n\log n)\) bound for an individual `CanSort` call. That is an asymptotic reduction in this parameter range. On unary threshold inputs, however, \(k\) is part of the input and can be as large as the sorting upper bound \(U(n)=\Theta(n\log n)\) on nontrivial instances. The transcript then dominates, giving \(O(n\log^2 n)\) bits, exactly the established worst-case upper bound. The general input-length bound remains within polynomial space, and no complexity-class improvement follows.

This is a deduction from the established DFS accounting in `docs/research-budgeted-dfs.md` §§5.2–5.3, not a new claim about the minimax game or unary worst-case space. The note already explicitly flags Savitch reachability as a way to remove the BFS `+n` term at quasi-polynomial query-time cost (§11); the parameterized statement above makes that consequence explicit while preserving the transcript term. No repository changes were made.
