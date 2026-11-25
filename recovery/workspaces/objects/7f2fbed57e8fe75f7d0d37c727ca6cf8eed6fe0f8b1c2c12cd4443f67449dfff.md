# Research plan

What is known, what is realistically open, and how Lean fits in. This is
guidance for choosing questions, not a task queue. The rules for doing the
research are in [AGENTS.md](../AGENTS.md); the machinery is in
[operations.md](operations.md).

## Baseline: known values

`S(n)` has been studied extensively. For `1 ≤ n ≤ 11` the Ford–Johnson
upper bound meets the information lower bound `C(n) = ⌈log₂ n!⌉`:

| n    | 1 | 2 | 3 | 4 | 5 | 6  | 7  | 8  | 9  | 10 | 11 | 12 |
|------|---|---|---|---|---|----|----|----|----|----|----|----|
| S(n) | 0 | 1 | 3 | 5 | 7 | 10 | 13 | 16 | 19 | 22 | 26 | 30 |

At `n = 12`, `C(12) = 29` but `S(12) = 30` (Wells). Exact values are known
for every `n ≤ 22`; the last three to be settled were `S(16) = 46`,
`S(17) = 50`, `S(18) = 54` (Stober–Weiß 2023, by exhaustive bidirectional
search taking days of computation each). `n = 23` is open. Asymptotically,
`S(n) − log₂ n! = O(n / (log n)^{1/5})` (Sergeev). Sources and model notes
are in [literature.md](literature.md). These are adaptive worst-case
comparison counts, not sorting-network sizes. Do not re-derive them as
research.

## Baseline: what this project has established

Upper bounds (numeric `n`; unary input length `N = n + k + 1`):

| Result | Status | Where |
|---|---|---|
| `S(n) ≤ k` decidable by memoized poset DP in `2^{O(n²)}` time | paper sketch | [upper-bound.md](upper-bound.md) |
| `SORT-BOUND-U ∈ PSPACE`, `SORT-BOUND-B ∈ EXPSPACE` (game / alternating TM) | paper proof | [research-certificates-barriers.md](research-certificates-barriers.md) |
| Budgeted DFS: `2^{O(n log² n)}` time, `O(n log² n)` bits; unary threshold in `2^{O(N log N)}` time, `O(N log N)` space | paper proof + code | [research-budgeted-dfs.md](research-budgeted-dfs.md) |
| Sound pruning (information cutoff, Aut(P) move orbits); no exponent gain | experiment | [research-budget-pruning.md](research-budget-pruning.md) |

Barriers and structural facts:

| Result | Status | Where |
|---|---|---|
| `SORT-BOUND-U` is sparse: many-one NP-hardness ⇒ P = NP; not many-one EXPTIME-hard | literature + deduction | [research-hardness-boundaries.md](research-hardness-boundaries.md), [research-encoding-consequences.md](research-encoding-consequences.md) |
| `2^{(1/4−o(1)) n log² n}` nonisomorphic winning states at one depth: enumerating winning states cannot beat the DFS exponent by more than a constant factor | paper theorem | [research-winning-frontier-barrier.md](research-winning-frontier-barrier.md) |
| An explicit sorting-tree witness has `2·n! − 1` nodes, so it is not an NP certificate | deduction | [research-certificates-barriers.md](research-certificates-barriers.md) |
| `e(P)` (linear extensions) does not determine the minimax value; five scalar invariants falsified | experiment | [research-n12-nontightness.md](research-n12-nontightness.md), [research-hardness-boundaries.md](research-hardness-boundaries.md) |
| Ordinal-sum decomposition is exact but does not shrink the state space | deduction + experiment | [research-series-decomposition.md](research-series-decomposition.md) |

Lean-checked results are listed in [kernel-results.md](kernel-results.md).

## Realistic targets

See "Realistic outcomes" in [problem.md](problem.md). In short:
unconditional super-polynomial lower bounds for the unary problem are
equivalent to known open separations (`P ≠ PSPACE`, `NP ≠ PSPACE`), so they
are out of scope. The open, plausibly reachable questions are on the
upper-bound and barrier side.

## Open questions

**Shrinking the exponent.** Is `S(n)` computable in `2^{O(n log n)}` time,
or `2^{O(n)}`? The winning-frontier barrier says any such method must avoid
enumerating transcripts or winning states. Decomposition, symmetry and
duality notes (`research-compression-next.md`, `research-parallel-duality.md`,
`research-orientation-modules.md`, `research-series-decomposition.md`) are
starting points; each so far gives exactness without a state-count gain.

**Certificates.** Can a height-`S(n)` strategy always be encoded as a
polynomial-size permutation-framed DAG? A polynomial-time verifier exists,
and constructive polynomial graphs cover merge sort and rank-envelope
insertion procedures, but **optimal-size completeness is open**. Read
[the consolidated certificate frontier](research-framed-certificate-frontier.md)
for proved boundaries and paper-level constructions awaiting audit;
[older strategy experiments](research-strategy-certificates.md) are supporting
history. Membership in NP or coNP would be a genuine upper-bound result.

**Space.** Can the `O(N log N)` work space be reduced, for example to
`O(N)` or polylogarithmic in `N`?

**The bound gap.** Can an effective finite version of Sergeev's bound be
extracted, narrowing the threshold window that an exact algorithm must
search? Can the `n = 12` obstruction be explained by an invariant that
generalizes? See `research-sergeev-asymptotic.md`,
`research-one-ply-obstruction.md`, `research-structural-lower-bounds.md`.

**Descriptive complexity.** The PSPACE bound implies an FO(PFP) definition
of `SORT-BOUND-U` on ordered structures by the capture theorem; building
and validating an explicit formula is separate work. An FO(LFP) (P) or
ESO (NP) definition would be a new upper bound. Do not infer a
smaller-class definition from a compact-looking informal recursion.

For each candidate: give an argument for exactness, measure cost against
the unary input length, and try to falsify it on known values.

## Lean

The library kernel-checks a faithful adaptive comparison-tree model,
existence and attainment of `S`, the information bound, `S(n) ≤ n(n−1)/2`,
monotonicity, exact values for `n ≤ 6`, and the minimax correspondence
`S_eq_adv_univ` (see [kernel-results.md](kernel-results.md)). Routine
expansion is paused. A new formalization needs the justification described
in `AGENTS.md`. When a mature result is ready, prove the correctness and
machine-cost bridges it needs; a Lean termination proof, a computable
recurrence or finite tests are not a Turing-machine time bound.

Verification: `lake build --wfail`, `lake env leanchecker SoringP1`, and
an axiom and correspondence review.
