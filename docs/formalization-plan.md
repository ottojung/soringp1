# Formalization boundary — exploration is the default

**Decision (2026-10-17): pause routine expansion of the Lean library.**
The goal is to discover a substantial result about evaluating S(n), then
formally check it. Formalization is not an independent measure of progress.

## Existing boundary: preserve, don't duplicate

The repository already kernel-checks a faithful adaptive comparison-tree
model, feasibility/attainment of S, bounds, monotonicity, and exact small
values through n=6. The minimax module now proves `S_eq_adv_univ`, including
correctness and the height bound for the constructed `minimaxTree` (A24).
See `kernel-results.md` for the precise inventory. Existing CI and checked
proof objects stay intact.

## Active boundary: exploration

Prefer primary literature, pencil-and-paper arguments, candidate structural
recurrences, complexity theory, counterexamples and small reproducible
experiments. Document deductions and failed approaches in
`exploration-agenda.md` and further research notes.

Routine proofs of familiar inequalities, further isolated small-n instances,
and nonessential helper-lemma chains are **not** active milestones.
Do not create new Lean tasks without a demonstrated research need.

## Former minimax exception — completed

The bounded minimax height attempt succeeded in A24. The Lean kernel checks
`minimaxTree_height` and `S_eq_adv_univ`. This closes the correctness
correspondence; it does **not** establish an efficient uniform algorithm to
evaluate `S(n)` and does not authorize routine follow-on formalization.

## Return to Lean for mature results

A proposed theorem should be supported by an independent mathematical
argument or algorithm, an explicit claimed novelty/usefulness, an audited
model and input encoding, and a concrete explanation of the value added by
kernel checking. Then prove any necessary correctness and machine-cost
bridges. Never confuse a Lean termination proof, a computable recurrence,
or finite tests with a Turing-machine time bound.

Verification remains `lake build --wfail` and
`lake env leanchecker SoringP1`, plus axiom and correspondence review.
