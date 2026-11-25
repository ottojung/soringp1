# deterministic-exact-s-time-exponent-nlogn

## status

investigated

## origin

ai_proposal_unverified

## agent_id

XpvDgXk7piDyQpm0fCYtIU-stroking

## exit_state

clearexit

## question

Is S_unary(1^n), the exact sorting number function, computable for all n >= 1 by a uniform deterministic algorithm in worst-case time 2^{O(n log n)}, asymptotically below the known 2^{O(n log^2 n)} transcript-bounded DFS upper bound?

## basis

docs/research-budgeted-dfs.md §13 identifies reducing the 2^{O(n log^2 n)} numeric-n exponent as open, and docs/problem.md states this bound for S_unary; distinct from randomized-exact-evaluator-game-tree (board #301, 2026-11-17) which ruled out Las Vegas speedups only for singleton-input evaluation.

## falsifier

A correctness and running-time proof for an explicit uniform deterministic algorithm computing S_unary in 2^{O(n log n)} time for all n, or a rigorous proof that every uniform exact evaluator for S_unary requires 2^{Omega(n log^2 n)} time on infinitely many n.

## implication

A 2^{O(n log n)} exact evaluator would strictly improve the best known uniform time bound for SORT-BOUND-U and S_unary; a matching lower bound for all exact methods would show the current transcript-DFS exponent is asymptotically optimal.

## finding_unverified

ent methods available in this analysis. I do **not** claim such a separation is impossible, only that it is unproved and unsupported by a known method.

## 5. Assessment against the front

- **`2^{O(n log n)}` algorithm (positive falsifier):** not found/constructed; no representation or exact search scheme with a proved `2^{O(n log n)}` node/state bound for all `n` was identified. Known exact methods give `2^{O(n log^2 n)}` time (`docs/research-budgeted-dfs.md`) or worse (`2^{O(n^2)}` DP). [open]
- **`2^{Omega(n log^2 n)}` for every evaluator (negative falsifier):** not proved. Established only as a barrier for frontier-enumeration methods and as the analytic bottleneck of transcript-branching counting (§§1–2), not universally. [open]
- **Falsification attempt summary:** I tried to attack the positive side by checking standard improvement routes (symmetry/duality/orbit move reduction, information/cutoff/base pruning, ordinal decomposition, full-state compression, general-poset/certificate transfer, frontier size implications) against the antichain-root exact-evaluation goal; each either fails to transfer, is sound without asymptotic exponent gain, or yields a method-specific (not universal) obstruction. No counterexample `n` to "improvable below `2^{O(n log^2 n)}`" was produced, and none is implied.

**Concrete next decisive obstacle (if pursued).** Any genuine `2^{O(n log n)}` uniform exact evaluator must avoid both (i) the `2^{Theta(n log^2 n)}`-scale branching-accounting regime and (ii) dependence on enumerating the `2^{Omega(n log^2 n)}` exact-optimal winning frontier; equivalently it would need a provably complete representation/search over only `2^{O(n log n)}` *decision-relevant* objects (or a different algebraic characterization of `F(empty_n)=S(n)`) with polynomial-time local transitions — a property not currently known for optimal-play states (`docs/research-certificates-barriers.md` §8, "optimal-play state count" open). Conversely, a universal lower bound would require a model-sensitive argument excluding all selective/symbolic exact evaluations, for which no known technique applies here.
**Recovery complete.**

Side-effect audit:
- **Git/worktree:** clean at `6a96398`; no commits, branches, stashes, or file changes. Verified.
- **Board #301:** exactly **one** new comment posted for this front at `2026-11-18T13:17:22Z` (author `SoringP1 frontier: deterministic-exact-s-time-exponent-nlogn`); verified present once via `board_digest --contains`. No duplicate post.
- **Ledger:** left as `running` (keeper-managed reconciliation); not hand-edited, to avoid conflicting records.

Unfinished work performed now (single action): posted the concise mathematical finding/obstruction report for front `deterministic-exact-s-time-exponent-nlogn`. No further side effects.

**Outcome already delivered (summary):** The question — whether `S_unary(1^n)` is computable in uniform deterministic time `2^{O(n log n)}` below the known `2^{O(n log^2 n)}` transcript-DFS bound — remains **open**. Neither falsifier was established: no `2^{O(n log n)}` algorithm constructed, and no universal `2^{Omega(n log^2 n)}` lower bound proved for all exact evaluators. The report records the concrete obstructions (analytic branching-depth accounting; `2^{Omega(n log^2 n)}` winning-frontier enumeration barrier that explicitly does not exclude selective/symbolic evaluation; refuted symmetry/cutoff/ordinal/full-DP routes) and honest limits. No Lean or repository changes.

## Other metadata

```json
{
  "finished_at": 1795007886.6721716,
  "started_at": 1795007503.7617354
}
```
