# Exploration-first research program

**Active direction (2026-10-17): mathematical discovery before more Lean.**
The objective is to understand the complexity of *evaluating the optimal
sorting number* S(n), not to collect Lean proofs about comparison sorting.
Treat this document as research guidance, not a theorem-completion queue.

## What we already have

The repository contains a faithful adaptive comparison-tree model, existence
and attainment proofs, information-theoretic and insertion upper bounds,
exact kernel-checked values through n=6, and part of a minimax correspondence
in `SoringP1/Minimax.lean`. For exact provenance and current gaps, see
`kernel-results.md`. The informal partial-order recurrence has a
`2^{O(n²)}` state-enumeration bound measured in numeric n; this is not a
kernel-checked machine-time theorem.

Exact values are already known in the literature through substantially
larger n than our evaluator handles. In particular `S(7)=13`, `S(8)=16`,
and `S(12)=30` are established; `ceil(log₂(12!))=29`. See
`literature.md` and `exploration-agenda.md`. Avoid re-proving literature
facts as the default research activity.

## Independent research fronts (no fixed order)

### Structural characterization and state compression

Search for exact recurrences with a smaller state space than labelled
partial-order enumeration. Investigate symmetry quotients, canonical
representatives, decomposition, unavoidable branching configurations, and
obstructions to uniform representations. For each candidate, give a
mathematical argument for exactness, and attempt to falsify it on known cases.
Measure complexity in the *input encoding* rather than simply n.

### Hardness, certificates and structural complexity

Investigate what an efficiently checkable certificate of `S(n) ≤ k` or
`S(n) > k` would require. Explicitly test whether a proposed witness is
polynomial in unary or binary input length. Separate unrestricted
decision-tree optimisation from the fixed one-parameter family S(n).
The unary threshold language is sparse: ordinary many-one NP-hardness
would imply P=NP by Mahaney's theorem. Record limitations on proposed
reductions *before* attempting a formal proof.

### Insights from optimal comparison sorting

Read the primary literature, beginning with Ford–Johnson and proofs of
small-n optimality. Explain why the information lower bound ceases to be
tight at n=12, and test whether the known obstruction suggests a general
invariant or more compact evaluator. Distinguish adaptive decision trees,
sorting networks and partial-information sorting.

### Executable investigations

Use small Python or other transparent experiments as a falsification tool.
Benchmarks should record state counts, time, memory, symmetry reductions and
independent reference values. Do not claim a complexity class consequence
from computing finitely many S(n).

## What counts as progress

A useful research contribution has a precise question, model and encoding,
primary sources, a candidate mathematical claim/algorithm/reduction,
a written argument or reproducible experiment, a serious counterexample
attempt, and a clear statement of uncertainty. Negative results and
identified barriers are valuable. Avoid manufactured tasks that only add
routine Lean lemmas.

## Lean checkpoint, not Lean workstream

Preserve and test the existing kernel-checked model. The outstanding
`height (minimaxTree S) ≤ adv S` proof may be finished if a small and
obvious repair works; otherwise document the proof-engineering blocker and
move on. A future Lean task needs an independent mathematical justification:
a meaningful new theorem, a mature algorithm, a subtle correctness proof,
or a necessary cost-model/correspondence bridge.

The long-term objective still includes kernel checking a major result. We
do **not** assume a P/NP separation exists or can be proved with the
currently available techniques.

## References and starting note

- [Exploration agenda and complexity barriers](exploration-agenda.md)
- [Primary literature and model checks](literature.md)
- [Exact problem statement and encodings](problem.md)
- [Formalization boundary](formalization-plan.md)
- [Kernel-checked results inventory](kernel-results.md)
