# sparse-optimal-comparison-graph-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

XEodjvpgTdo5n7Kd0uW0yG-chaos

## exit_state

clearexit

## question

In the fixed adaptive pairwise-comparison model of docs/problem.md, let g(n) be the minimum number of distinct key-pairs that any height-S(n) correct sorting tree on n labelled keys may compare anywhere over its whole leaf set. Is there a fixed constant c with g(n) <= c*n*log n for all n (so some optimal strategy uses a sparse comparison graph), or does every height-S(n) tree compare Omega(n^2) distinct pairs for infinitely many n?

## basis

docs/problem.md fixed pairwise model and the board #301 evaluator-exponent frontier; an independent audit of all 687 ledger fronts found no restricted-edge-set or comparison-graph-sparsity front (nearest restrict test type or bound graph entropy, not a sparse allowed-pair set).

## falsifier

For one n, exhaustively certify with a faithful minimax solver that no height-S(n) tree uses fewer than c*n*log n distinct pairs, or construct for all n a poly-time-buildable sparse graph G_n and certify that the restricted-comparison optimum S_{G_n}(n) equals S(n).

## implication

A uniformly constructible sparse optimal comparison graph would cut root minimax branching from Theta(n^2) candidate pairs to O(n log n), a concrete route to shrinking the 2^{O(n log^2 n)} exact-evaluation exponent; a dense lower bound rules out that sparsification route.

## finding_unverified

inear extension of `Q`. At the antichain root every pair qualifies (hence `K_n`); from a chain, none do. This is a statement about the antichain root of `S(n)`, not a general-poset hardness result.
- **Soundness ≠ completeness.** Checking consecutive pairs of a *claimed* order (n−1 comparisons) is a cheap verification certificate that presupposes the answer; it does not produce a tree that *discovers* the order. Framed-DAG/succinct certificates therefore say nothing about the tree's global edge set.
- **Complexity implication.** The proposed exponent-shrinking route (cut root branching from Θ(n²) to O(n log n) allowed pairs) is **dead**: no sparse allowed-pair set can sort at all. This rules out exactly that route; it yields no new bound for `S(n)` and does not affect symmetry-quotient, compression, or certificate approaches.

## Honest limits
- The theorem is elementary and classical (standard exercise; exchange argument appears in StackOverflow Q251068); I claim **no novelty and no new complexity theorem** for `S(n)` or `SORT-BOUND-U`. The front's dense horn is true but degenerate: the stronger statement holds for *every* correct tree, not just optimal ones.
- Serious falsification attempts: merge-insertion graph (binary-insertion pivots cover the whole chain over all inputs ⇒ dense), general-poset reductions (no bridge back to `S(n)`), and direct refutation of the theorem (blocked by adjacency). `websearch` was repeatedly cancelled; I used `docs/literature.md` plus a direct fetch of the comparison-sort model/value table.

**External writes:** exactly one board comment on Antonina #301 at 07:28Z (verified: 1 unique match). No Lean, repository, ledger, test, or CI changes; worktree remains clean.
Understood. I will not repeat the post. Let me re-inspect the actual state to confirm what happened in the previous turn and whether anything remains unfinished.
Confirmed. Let me do one final check for any newer board instruction directed at this front that would constitute unfinished work.
## Inspection result: work already complete — no action taken this turn

**Effects that actually happened in the previous turn (verified, not assumed):**
- **Exactly one external write:** a board comment on Antonina #301 at `2026-11-22T07:28:01.784Z`, authored `SoringP1 researcher: sparse-optimal-comparison-graph-alln`. The query for that front id returns **1 unique match** — no duplicate.
- **Scratch only:** `/tmp/opencode/sparse_g.py`, `sparse_post.md`, `sparse_post_result.json` (plus empty stderr).
- **No other side effects:** git tree clean on `billy-dev` at `6a96398` (HEAD unchanged, no commits, no repo/Lean/test/CI changes). Ledger front `sparse-optimal-comparison-graph-alln` remains `running` with `finding=None` — untouched, as with the other fronts' reports.

**Unfinished work:** none. The previous turn completed the research task: it proved the decisive all-n theorem (every correct comparison tree compares all `C(n,2)` pairs, so `g(n)=Θ(n²)` and the sparse-allowed-pair route is impossible), ran the exhaustive small-n falsification checks, and posted the result with honest limits. The newest board message is that very post; there is no follow-up request directed at this front.

I have therefore **not** re-posted, not touched the ledger, and not created any commit or repository change. Nothing is uncertain enough to require review. If you want the ledger front flipped to `investigated`, that is a deliberate new action — say so and I will do it once.

## Other metadata

```json
{
  "finished_at": 1795332527.01165,
  "started_at": 1795331706.469409
}
```
