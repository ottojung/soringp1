# antonina-IQZTUlvnXYivIXPDihm8HJ-cleanse

Session: ses_e0c2d2a57ffeGp7pc0OvLzZu8Y
Workspace: /home/lubko/soring-fronts/exponent-shrink-20261119
Created: 1795092043229; updated: 1795092092738

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 87 (msg_1f3d379bd001SRH8wjB4F14aR8)

# #301 report — shrinking the exponent for evaluating S(n)

**Outcome: (b) for the known decomposition family; (c) precise obstruction for going further.** No algorithm achieving `2^{O(n log n)}` is found. No repo changes; worktree clean.

## Tags and claims

- **[literature]** Budgeted DFS gives `S(n)` in `2^{O(n log² n)}` time, `O(n log² n)` bits; winning-frontier barrier gives `2^{Θ(n log² n)}` nonisomorphic winning states at one depth, including at budget `S(n)` (Sergeev surplus `d(n)=o(n)`).
- **[deduction]** The DFS exponent comes from branching `Θ(n²)` (incomparable pairs) × depth `Θ(n log n)` (budget). Reducing to `2^{O(n log n)}` requires either depth reduction to `O(n)` or branching reduction to `O(1)` under an exactness-preserving compression.
- **[deduction]** No known exactness-preserving decomposition reduces the dominant state count:
  - Ordinal sums are exact but the root antichain is series-prime; decomposable fraction decreases (`67%→47%` for `n=2..5`), and component states are *added* memo entries (research-series-decomposition.md).
  - Modular/prime quotients: interval/series/parallel reversals are sound, but prime-quotient reversal fails at `n=7` (8 violations); modular decomposition tree up to reversal does **not** determine `F` (research-orientation-modules.md).
  - Duality (`S_n × Z_2`) is exact but a constant factor (~2); comparability graph fails both value invariance (`n=7`) and transition well-definedness (`n=5`) (research-compression-next.md).
  - Parallel (disjoint-union) composition is not additive for `F` (research-parallel-duality.md).
- **[deduction]** The winning-frontier construction is itself a family of series-prime/prime-quotient posets (chains with forward cross edges) with `Θ(n log n)` independent choices among `Θ(n^{3/2})` slots; its `2^{Θ(n log² n)}` distinct states are not compressible by any of the above quotients, and each is reachable within `S(n)` comparisons.
- **[conjecture/open]** A `2^{O(n log n)}` method would need a new exact invariant strictly between the full poset and the (failed) comparability-graph/module/ordinal-sum invariants, compressing the prime-quotient frontier states. No such invariant is known; the certificate question (polynomial-size framed DAG) is the adjacent open route, and would be a stronger (NP) result if resolved.

## Precise obstruction

The `2^{O(n log² n)}` exponent is not an artifact of the DFS: the number of distinct reachable states at a single depth is already `2^{Θ(n log² n)}`, and every known exact decomposition/symmetry leaves a `2^{Θ(n log² n)}`-sized set of inequivalent prime/series-prime states. Beating the exponent therefore requires a new structural theorem, not canonicalization or pruning within the known family. A general time lower bound for *arbitrary* (non-enumerative) methods remains open and would need a communication/decision-tree argument not currently available.

## Consequence for central question

No change to known upper bound: `S(n)` computable in `2^{O(n log² n)}` time, `O(n log² n)` bits; no class separation or NP/coNP consequence. Next decisive obstacle: find (or rule out) an exact invariant compressing the prime-quotient frontier states, or resolve the polynomial-size framed-certificate completeness question.
