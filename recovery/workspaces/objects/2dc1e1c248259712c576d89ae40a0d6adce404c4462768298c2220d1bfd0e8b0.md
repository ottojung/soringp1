# SoringP1 research and development contract

## Research objective

Study the computational complexity of computing the exact worst-case
comparison-sorting number S(n). The long-term goal includes Lean kernel-checked
results, but **discovery comes first**. See `docs/problem.md` for the fixed
model and encodings.

## Operating mode: exploration first (2026-10-17)

This is the operative priority for researchers and autonomous agents:

- **Prioritize mathematics, literature, algorithms, falsification and experiments.**
  Do not create consecutive Lean milestones to formalize standard bounds,
  another known small value, minor corollaries, or infrastructure for its own
  sake. Counting finished theorems is not evidence of progress toward
  classifying the complexity of evaluating S.
- Start from the established literature, not by rediscovering known exact
  sorting numbers. Record the original source, sorting model, and why the
  result matters for evaluating S(n).
- Work on independent research fronts: structural compression of the
  minimax state space; certificates and complexity barriers; and
  combinatorial obstructions (e.g. information bound non-tightness).
  Productive counterexamples and negative results are valid deliverables.
- Prefer a concise written mathematical argument and a small experimental
  program to speculative new Lean files. Keep the model and encoding explicit.
- **Freeze routine Lean expansion** until there is a mature, substantive
  claim or a critical ambiguity in correspondence to the intended problem.
  Existing Lean files and CI are preserved and must remain working.
- **One narrowly scoped exception:** the missing height specification of
  `minimaxTree` may be completed if straightforward. The current recursive
  `adv` unfolding/elaboration loop must not become an unbounded
  proof-engineering campaign: if the direct fix is nontrivial, write down the
  precise blocker and return to exploration. Do not launch a parade of
  auxiliary Lean milestones to route around it.
- Don't launch tasks just to occupy agents. Do not infer an obligation to
  continuously formalize from the availability of compute.

Before starting a proposed formalization, write a short justification:
which independent discovery it verifies, why its statement matters to
the complexity of evaluating S, what simpler paper/computational checks
were tried, and what the complete correspondence obligation is.

The current exploration agenda is `docs/exploration-agenda.md`; the
research workflow and open directions are `docs/research-plan.md`.

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
- The unary two-parameter threshold language is sparse; by Mahaney's
  theorem, NP-hardness under polynomial-time many-one reductions would imply
  P = NP. Do not present such a reduction as a routine milestone.
- A hardness result for unrestricted partial-order/decision-tree optimization
  does not automatically apply to the specific family S(n).
- Confirm the exact problem statement before claiming any major separation.

## Research cadence

1. Check primary literature and already-known counterexamples.
2. Formulate a precise, falsifiable question or candidate theorem, with
   intended impact on evaluation complexity.
3. Work on paper and in small experiments. Seek negative examples, symmetry
   reductions, alternative algorithms and complexity barriers.
4. Report sources, definitions, strongest evidence, failed attempts,
   possible novelty, and the next obstacle in research notes.
5. Only formalize a mature result if it materially increases confidence in an
   important theorem or closes a necessary model/cost-model bridge.

## Evidence and proof policy

Separate **definition**, **literature result**, **deduction**, **conjecture**,
**empirical observation**, **paper proof**, and **kernel-checked theorem**.
A passing Lean build alone does not prove that the statement corresponds to
the intended complexity model. Do not introduce `sorry`, `admit`, or new
`axiom` declarations as substitutes.

Before integrating a new theorem: run `lake build --wfail`, replay with
`lake env leanchecker SoringP1`, and inspect axioms. CI is necessary but
not sufficient; maintain source/model correspondence. Preserve useful failed
approaches in research notes. Do not promise a proof of P vs NP or a hardness
separation.

## Provenance and delivery

Record a primary source and the exact model for nontrivial external facts.
Prefer short, reviewable commits; **commits merged to main must be signed**.
The project is a research library: merging documentation and passing GitHub
CI is the GitHub-side deployment, not a deployment to an application server.
Any Antonina/Viche dispatch or host update must be verified separately.
