# SoringP1 research and development contract

## Research objective

Classify the complexity of computing the exact worst-case comparison-sorting
number S(n), with a Lean-kernel-checked end result. See `docs/problem.md`
for the mathematical semantics and encodings. Do not substitute the time
complexity of sorting an input list for the complexity of evaluating S(n).

## Model fidelity

- Treat S as a **function**. P, NP, EXPTIME apply to explicitly defined
  decision languages. Use FP/FEXP-style language for function computation.
- Always say whether n is binary or unary. A bound exponential in numeric n
  is not automatically EXPTIME for binary n.
- Distinguish fixed sorting networks from adaptive decision trees.
- Distinguish uniform algorithms for all n from circuits / precomputed advice.
- Inputs contain n *distinct labelled keys*; tie policy is not implicit.
- A lower bound of Ω(n log n) for sorting is **not** a lower bound for
  computing S(n). Likewise computing individual values does not imply hardness.
- A polynomial-size witness for an optimal sorting tree is not established:
  the trees may be exponentially large. Never assume the threshold problem is
  in NP simply because one can exhibit a sorting algorithm.
- NP is not itself a class of total numeric functions; do not describe P, NP
  and “above NP” as a mutually exclusive trichotomy.
- Confirm the exact problem statement before claiming any major separation.

## Research cadence (adapted from AssemblyP1)

1. Keep the source-faithful formal target small and auditable.
2. Explore in mathematical notes, computation, examples, algorithms, reductions,
   and counterarguments; maintain independent competing approaches.
3. Formalize substantive intermediate claims only when they clarify an
   immediate model ambiguity or enable verification of a mature proof.
4. Return to Lean for a convincing complete theorem, including any required
   correctness and complexity-cost-model bridges.
5. Never silently weaken the goal to a different restricted sorting model.

## Evidence and proof policy

Keep separate labels: **definition**, **conjecture**, **empirical observation**,
**external theorem**, **paper proof**, and **kernel-checked theorem**.
A passing Lean build alone does not prove that the statement corresponds to the
intended complexity model. Do not introduce `sorry`, `admit`, or new
`axiom` declarations as proof substitutes.

Before integrating a theorem: run `lake build --wfail`, replay with
`lake env leanchecker SoringP1`, and inspect axioms. CI is a necessary gate,
not a replacement for correspondence review. Prefer short, reviewable commits.
Preserve useful failed approaches and precise blockers in docs or durable tasks.

No implied theorem is “almost proved” merely because a formalization compiles.
The project's objective may be open or require breakthroughs.

## Provenance

When citing nontrivial facts, record a primary source and the exact
definition used there. Notes and third-party formalizations can suggest
directions, but are not automatically imported axioms.
