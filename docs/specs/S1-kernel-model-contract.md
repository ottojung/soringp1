# Kernel-model contract (S1, scoped draft)

**Status:** scoped draft, docs-only. Records Lean names/modules and the
exact correspondence target for any future formal translation.
No machine-time claim. Completeness of strategy programs / framed
certificates relative to this model is **OPEN** (see S2/S3/S4).

## Model modules (`SoringP1/`)

- `Model.lean`: `ComparisonTree n` (`leaf` / `compare i j yes no`),
  `ComparisonTree.height`, `ComparisonTree.run ranking`,
  `Correct tree` (`∀ ranking, run ranking tree = ranking.symm`),
  `HasBudget n k` (`∃ tree, Correct tree ∧ height tree ≤ k`),
  `S n := sInf {k | HasBudget n k}`, `hasBudget_mono`.
- `Existence.lean`: `exists_hasBudget`, `sortTree_correct`, `sortTree_height`.
- `Attainment.lean`: `hasBudget_S`, `S_le_iff : S n ≤ k ↔ HasBudget n k`,
  `S_is_minimal`, `S_le_explicit`, `exists_tree_S`.
- `Minimax.lean`: `splitPairs`, `adv`, `Sorts S T`, `adv_le_height`,
  `adv_univ_le_S`, `bestPair`, `minimaxTree`, `minimaxTree_sorts`,
  `minimaxTree_height`, `minimaxTree_spec`, `hasBudget_adv_univ`,
  `S_le_adv_univ`, **`S_eq_adv_univ (n) : S n = adv univ`**.
- Bounds/values: `LowerBound.lean` (`factorial_le_two_pow_S`),
  `Bounds.lean`, `TightBound.lean` (`S_le_tight`),
  `SmallValues*.lean` (`S 0..6` exact), `Monotone.lean` (`S_mono`).

## Correspondence target (before any translation)

Any future claim "program `p` / certificate `G` witnesses `S(n) ≤ k`"
must target **`HasBudget n k`** (equivalently `S n ≤ k` by `S_le_iff`).
Concretely: exhibit, for the given `n,k`, a `ComparisonTree n` with
`Correct` and `height ≤ k`, or equivalently discharge `HasBudget n k`.
`S_eq_adv_univ` is the mathematical bridge between `S` and `adv`;
it is **not** a Turing-machine cost theorem and does not by itself give
a program/certificate compiler.

## What is kernel-checked vs what is not

- **[kernel-checked]**: model definitions above; `S_eq_adv_univ` and the
  listed attainment/bound/value theorems (see `docs/kernel-results.md`).
- **Not kernel-checked**: any correspondence from `FO(TC)_v` program texts
  or framed DAGs to `HasBudget`/`Correct`/`height`; any uniform
  machine/resource bridge for paper `O(|φ|·N^(2v))` bounds; any all-`n`
  exact-budget compiler at `S(n)`. Those are paper-level or OPEN.

## No-machine-time rule

Do not read `adv` termination, `minimaxTree` recursion, or a passing
`lake build` as a uniform Turing-machine time bound. Per
`docs/kernel-results.md` open front 1, the `2^{O(n²)}` DP sketch and the
budgeted-DFS `2^{O(N log N)}` / `O(N log N)`-space bounds are informal
algorithm sketches with stated encoding assumptions, not kernel-checked
machine-cost theorems. The same applies to the `L^c` interpreter clock
in S2: it is a paper-model clock, not a Lean-checked cost.

## Use in gates

R3 requires naming this target (`HasBudget n k` / `S_le_iff`) before any
formal translation is attempted. R5 requires `lake build --wfail` +
`lake env leanchecker SoringP1` + axiom inspection before integrating any
Lean theorem, with no `sorry`/`admit`/`axiom`.
