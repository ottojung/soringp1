# antonina-HdY7T0bWjLBecJR95VWf7B-mistaking

Session: ses_e473b3b1bffe9X3FYoxoVS9JpW
Workspace: /home/lubko/soring-fronts/unary-evaluator-space-nlogn
Created: 1794101265719; updated: 1794101280416

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 28 (msg_1b8c4cd35001rp31L2R0wH0WGm)

## Result: INCONCLUSIVE (no construction found) — missing lemma identified

### 1. Reconstructed established bound
From `docs/problem.md` + `research-budgeted-dfs.md` §5.2/§5.3:

- Space accounting for transcript-only DFS: `O((d+n) log(n+2))` bits, with `d` = budget.
- For the **numeric function** `S_unary(1^n)`: binary search over `k ∈ [0, U(n)]`, `U(n)=O(n log n)`, so each deciding call uses `d=O(n log n)`. Total work-tape: `O(n log n · log n) = O(n log² n)` bits. Dominant term = **stack/transcript length `d` frames × `O(log n)` bits per frame** = `O(n log² n)`. The `+n log n` reachability workspace is lower order.
- For the **threshold** decision with supplied `k`: `O((k+n) log n)` bits, i.e. `O(N log N)` for input length `N=n+k+1`.

### 2. Attempted construction for O(n log n)
Candidates considered:
- **Iterative deepening / bounded DFS with recomputation**: depth still `d=O(n log n)` comparisons; without storing the path, each node cannot be resumed after a child returns, so the path must be reconstructed — requiring either storing it or re-searching, which doesn't reduce worst-case space below `O(d log n)`.
- **Savitch-style reachability** (§5.2, §11): removes the `+n log n` workspace term (reachability in `O(log² n)` space) but leaves the `O(d log n)` transcript stack untouched. Still `O(n log² n)`.
- **Compressing the transcript**: a comparison path is an acyclic digraph on `n` vertices with `d=O(n log n)` edges; general graph compression cannot losslessly represent an arbitrary such transcript in `O(n log n)` bits (information-theoretic: `d` independent labels ≈ `d log n` bits lower bound for *this* representation). No canonical/quotient form is known that decides the game without the path.

Feasibility test for small `n≤8`: the existing `scripts/transcript_dfs.py` already realizes the minimal transcript-only accounting and records max stored path length = depth. Measured peak path length = `d+1` frames for `n≤5, d≤5`, confirming the `O(d log n)` term is intrinsic to this DFS; no implementation achieves `O(n log n)` bits for `n` with `d=Θ(n log n)`.

### 3. Conclusion
No construction achieving `O(n log n)` bits (uniform, for `S_unary`) was found. A lower bound `Ω(n log² n)` is **not** established — the obstruction is not proven intrinsic to the game, only to the transcript-DFS method. Mark **INCONCLUSIVE**.

**Precise missing lemma:** A proof (or refutation) that the minimax game `G(n,k)` can be decided in space `o(k log n)` bits, i.e. without retaining an `Ω(k)`-length comparison transcript — equivalently, a space-efficient (non-memoized) characterization of poset states reachable within `k` comparisons that avoids storing the generating edges. Until such a lemma exists, the `O(n log² n)` upper bound stands and no improvement to `O(n log n)` is justified. (Consistent with §13 of `research-budgeted-dfs.md`, which flags `o(n log² n)` space as open.)
