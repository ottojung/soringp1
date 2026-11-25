# antonina-SOKHOeY9jVEGGBzOSfCYav-mare

Session: ses_e49aa89e0ffeIlG26OZ2dYtjhX
Workspace: /home/lubko/soring-fronts/exec-winning-frontier-sparse-interface-20261107
Created: 1794060416601; updated: 1794060489342

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 27 (msg_1b655947a0019yfbU57RYEqHvj)

## Result: the bounded-degree version loses the required entropy

**Rebuttal.** Under the construction in §§1–3.1, restricting the additional edges to any per-interface bounded-degree family necessarily removes the \(n\log^2 n\) exponent. This is an obstruction to that sparse-family construction, not to every possible structured construction.

Take \(n=s^2\), \(L=s\), with \(s\) disjoint vertical chains, as in the document. Let \(G_i\) be the added bipartite graph between levels \(i\) and \(i+1\), excluding the \(s\) chain edges. There are \(q=s(s-1)\) eligible edges per interface and \(s-1\) interfaces. The budget parameter is
\[
m=k-t_0-B=nr-O(n)+d(n)=\Theta(n\log n),
\]
where \(r=\log_2s\), \(t_0=n-s\), \(B=(s-1)+(n-1)r\), and \(d(n)=0\) for \(k=C(n)\), or \(d(n)=S(n)-C(n)=o(n)\) by Sergeev for \(k=S(n)\).

For a fixed maximum degree \(\Delta=O(1)\), each interface graph has at most \(\Delta s\) edges. Thus the entire family has at most
\[
\sum_{j\le \Delta s(s-1)}\binom{(s-1)s(s-1)}j
\]
choices, whose logarithm is \(O(n\log s)=O(n\log n)\): there are \(s-1\) interfaces, \(O(s^2)\) choices per interface, and at most \(2^{O(s\log s)}\) bounded-degree graphs per interface. More precisely, the per-interface count is at most \(\sum_{j\le\Delta s}\binom{s(s-1)}j=2^{O(s\log s)}\), yielding the stated bound after multiplying over interfaces.

This estimate already counts **all** such graphs, not just those with exactly \(m\) edges, so it remains an upper bound after imposing \(\sum_i |E(G_i)|=m\). If \(m>\Delta s(s-1)=O(n)\), the family is empty; if feasible, its labelled-state count is at most \(2^{O(n\log n)}\). Quotienting by isomorphism cannot increase the count. Consequently it cannot yield \(2^{\Omega(n\log^2 n)}\) nonisomorphic states. The required \(m=\Theta(n\log n)\) edges are compatible with bounded degree only when \(\Delta\) grows at least \(\Omega(\log n)\); that is no longer a constant-degree sparse family, and this counting obstruction does not settle it.

For comparison, the unrestricted construction has \(M=(s-1)(s^2-s)=\Theta(n^{3/2})\) candidates and
\[
\log_2\binom{M}{m}\ \ge\ m\log_2(M/m)
=\left(\tfrac14-o(1)\right)n(\log_2n)^2.
\]
Subtracting \(\log_2(n!)=O(n\log n)\) for the at-most-\(n!\) labelings of an isomorphism class leaves the same leading exponent. The sparse-family upper bound is therefore genuinely too small, even before the isomorphism quotient.

**Reachability and winning conditions.** In the independent-edge construction, each installed comparison goes forward exactly one level. No alternate multi-edge path can imply an adjacent-level relation, so none of the added edges is already implied; all \(t=t_0+m=k-B\) outcomes are legal and the resulting posets are distinct as labelled states. The \(s\) disjoint sorted chains permit a balanced-head merge in at most \(B=(s-1)+(n-1)\lceil\log_2s\rceil\) comparisons, so every state is winning with the remaining budget \(k-t=B\). These arguments apply at \(C(n)\) and \(S(n)\); Sergeev’s asymptotic bound gives \(S(n)-C(n)=o(n)\), not an effective finite threshold.

**Scope.** This does not produce a new barrier for bounded-degree families; it rules out using those families within this chain-based counting argument to recover the dense construction’s superpolynomial-in-input-size frontier count. The existing dense result only excludes enumeration strategies that must output the *entire* information-budget winning frontier, even up to isomorphism. It neither rules out selective or compressed search nor gives a time lower bound. There is no established bridge here to #47/#48 or to improved exact evaluation: generic graph counting cannot supply such a reduction or evaluator. **Stopping point:** the bounded-degree restriction loses the needed entropy; no broader claim about expanding or logarithmic-degree families follows from this count.

## Output 127 (msg_1b656675f00151LuhWAN6F4Q6k)

State check complete. Here is what actually happened and what was (not) done:

## Durable state

- **Worktree** `…/exec-winning-frontier-sparse-interface-20261107` on branch `research/exec-winning-frontier-sparse-interface-20261107`, base `c865b239`: **clean**, no uncommitted files, no new commits. The sparse-analysis task required no repo edits, and none were made.
- **Issue 301 board**: last message (as of `updatedAt` 14:07:16) is the assignment of this very front to this worktree; **no outcome or comment has been posted** for it — and the task explicitly forbade board posting, so none is due.
- No purchases, commits, merges, CI pushes or other external side effects are traceable to the previous turn. The prior turn was analysis-only: reads of `docs/research-winning-frontier-barrier.md` (all side effects = none), `docs/literature.md`, and a cancelled web search for Sergeev TR20-096 (search failed; the citation in the note's §3.1 was used as recorded there).

## Unfinished work

The only deliverable was the rebuttal/analysis, which was completed and remains uncontaminated by side effects — nothing to redo and nothing to undo. Restating the conclusion compactly:

**Result: bounded-degree sparse restriction does not preserve the barrier.** For `n=s²`, `M=(s−1)(s²−s)=Θ(n^{3/2})` candidate edges, budget `m=Θ(n log n)`. A per-interface bounded-degree family admits at most `∑_{j≤Δs} binom{s(s−1)}{j} = 2^{O(s log s)}` graphs per interface, hence `2^{O(n log s)} = 2^{O(n log n)}` labelled posets total, versus the needed `binom(M,m) ≥ 2^{(1/4−o(1))n (log₂ n)²}`. Even unquotiented (so `n!` isomorphism merging is irrelevant), the sparse family undercounts by the whole `n log²n` exponent. Compatibility requires `Δ = Ω(log n)`, i.e., not a constant-degree family — the degree-constraint arithmetic forces entropy loss. Reachability/winning arguments are unaffected but moot without the entropy. So: **a concrete obstruction to the sparse variant of this construction, not a new barrier for sparse liftings in general and no bridge to #47/#48 or improved exact evaluation.** Per the stop rule (no nontrivial new consequence beyond the arithmetic obstruction), no publication-gate artifact was produced — consistent with the instruction.

No further action needed; the worktree and board need no cleanup.
