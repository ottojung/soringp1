# Formalization plan

Inspired by AssemblyP1's exploration-first methodology.

**Boundary A (initial bootstrap).** Give a faithful sorting decision-tree
model and make feasible budgets and the minimum value meaningful.
The initial Lean model already has the basic tree, interpreter, correctness
predicate, feasibility predicate, and minimization specification.
**Status: largely complete.** Existence (`exists_hasBudget`), attainment and
minimality (`hasBudget_S`, `S_le_iff`, `S_is_minimal`), the information lower
bound (`n! ≤ 2^(S n)`), and small reference instances (`S(0..3) = 0,0,1,3`)
are kernel-checked. See `docs/kernel-results.md` for the exact theorem
inventory and the remaining open fronts (tight upper bound, `S 4`, a checked
executable evaluator, and the machine-model/complexity bridge).

**Exploration (default).** Prefer informal mathematical arguments, executable
experiments, adversarial examples, and connections to optimal decision-tree
theory. In particular, search for a *structural characterization* of S(n)
that avoids enumerating partial orders. Do not expand Lean code merely to
record unproven heuristic ideas.

**Boundary B (mature results).** Formalize a complete algorithm/complexity
bound or lower-bound reduction once a coherent independent proof exists.
Prove the complexity class encoding and machine-model bridge; do not leave
resource bounds as comments attached to a function definition.

**Verification.** Build all Lean modules, kernel replay them, and audit axioms.
A theorem of a surrogate problem is not automatically a theorem about S.
