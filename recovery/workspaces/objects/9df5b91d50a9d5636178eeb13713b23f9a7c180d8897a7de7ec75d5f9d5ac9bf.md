# SoringP1 research contract

This is the single current contract for people and agents working in this
repository. It replaces the earlier stack of dated directives; their history
is in `git log`. Where another document disagrees with this one, this one wins.

Operational details (host, Antonina, the research board, the agent pool
keeper) live in [docs/operations.md](docs/operations.md).

## Objective

Change what is known about the **uniform complexity of computing the exact
sorting number `S(n)`**: the minimum worst-case number of adaptive pairwise
comparisons needed to sort `n` distinct labelled keys. The fixed model and
encodings are in [docs/problem.md](docs/problem.md). Discovery comes first;
Lean is for checking mature results, not for generating activity.

## Scope: unary encoding

The active target is the unary threshold language

    SORT-BOUND-U = { 1^n # 1^k : S(n) <= k }

and its function counterpart `S_unary(1^n)`. Measure resources against the
actual input length `N = n + k + 1` (or `N = n` for the function).

The binary encoding (`SORT-BOUND-B`, `S_binary`) remains defined in
`problem.md` and its established bounds are kept, but there is no binary
workstream. Opening one requires an explicit decision by the project owner.

## What can and cannot be achieved

Read the "Realistic outcomes" section of `problem.md` before choosing a
question. In short: `SORT-BOUND-U ∈ PSPACE` is proved here, so showing
`SORT-BOUND-U ∉ P` would prove `P ≠ PSPACE`, and showing `∉ NP` would prove
`NP ≠ PSPACE`. As a tally language it is also trivially in `P/poly`, so
circuit lower-bound methods cannot help. Do not spend research time on
unconditional super-polynomial lower bounds for the unary language. The
productive frontier is **upper bounds** (faster or more space-efficient exact
evaluation, succinct certificates), **barriers** that rule out whole
families of methods, and **structural theorems** about the minimax game.

## How research works

1. Start from one sharp, falsifiable all-`n` question whose answer would
   change what we know about evaluating `S(n)`. State that consequence.
2. Read the primary literature first; the sorting-number literature is
   extensive (see [docs/literature.md](docs/literature.md)). Do not
   rediscover known exact values or known barriers.
3. Try hard to refute the idea: a paper argument first, a small experiment
   only when it discriminates between hypotheses.
4. Report the result, including negative or inconclusive outcomes, as a
   concise update on the research board (see `docs/operations.md`). No
   branch, PR, note, test or Lean file is required. A clean worktree is a
   normal outcome.
5. If a line of attack has no plausible bridge back to `S(n)` (for example,
   it only concerns arbitrary partial orders), say so and stop.

Avoid: repeating prior negative findings, endless small-instance
enumeration, generic partial-order complexity with no reduction back to the
antichain root, and routine formalization.

Agent count, PR count, CI passes and Lean file count are **not** measures
of progress. The questions that are: what new claim about computing `S(n)`
can we defend, which hypothesis was ruled out, and what is the next decisive
obstacle?

## Publication gate

Bring work into the repository (note, script, test, Lean) only for:

- a demonstrably improved uniform bound or algorithm for `S(n)`;
- a rigorous, encoding-preserving reduction or barrier theorem;
- a substantive certificate, recurrence or structural theorem about `S(n)`;
- a decisive no-go result excluding a major route; or
- a necessary fix to model fidelity.

Before integrating, provide an independent paper argument, primary sources,
a serious falsification attempt, and a short explanation of why the result
matters for the central question. Then use minimal tests and review.

## Lean policy

The existing Lean library is maintained and must keep building. Do not add
consecutive milestones for standard bounds, further small values, minor
corollaries or infrastructure. Before starting a new formalization, write a
short justification: which independently established result it verifies,
why the statement matters for evaluating `S(n)`, which paper and
computational checks were already done, and what the full correspondence
obligation is. The minimax correspondence (`minimaxTree_height`,
`S_eq_adv_univ`) is complete; do not reopen it.

## Model fidelity

- Treat `S` as a **function**. P, NP, EXPTIME apply to explicitly defined
  decision languages; use FP/FPSPACE-style language for function
  computation. NP is not a class of numeric functions, and "P, NP, above NP"
  is not a trichotomy.
- Always state the encoding of `n`. A bound exponential in numeric `n` is
  not EXPTIME in the binary input length.
- Distinguish adaptive decision trees from sorting networks, and uniform
  algorithms from circuits or precomputed advice.
- Inputs are `n` distinct labelled keys; no tie policy is implied.
- An Ω(n log n) sorting lower bound is not a lower bound for computing
  `S(n)`; computing individual values does not imply hardness.
- An optimal sorting tree may be exponentially large, so exhibiting one is
  not an NP certificate.
- `SORT-BOUND-U` is sparse: many-one NP-hardness would imply P = NP
  (Mahaney), and it cannot be many-one EXPTIME-hard.
- Hardness of optimization over arbitrary partial orders does not transfer
  to the fixed family `S(n)` without a reduction.

## Evidence and proof

Label claims as **definition**, **literature**, **deduction**,
**conjecture**, **experiment**, **paper proof** or **kernel-checked**. A
passing Lean build does not by itself show that a statement matches the
intended model. Never use `sorry`, `admit` or new `axiom` declarations.

Before integrating a Lean theorem, run `lake build --wfail`, replay with
`lake env leanchecker SoringP1`, and inspect axioms. Record a primary source
and the exact model for every nontrivial external fact. Preserve useful
failed approaches.

## Delivery

Prefer short, reviewable commits; commits merged to `main` must be signed.
Merging to `main` with passing CI is the whole deployment: this is a
research library with no application server. Changes to the agent pool on
the execution host are a separate operational step (see
`docs/operations.md`).
