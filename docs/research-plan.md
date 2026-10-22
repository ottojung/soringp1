# Exploration-first research program

**Binding pivot (2026-10-18): pursue mathematical discovery about the
complexity of `S(n)` before publishing any new artifacts.**
The objective is to understand the complexity of *evaluating the optimal
sorting number* S(n), not to collect Lean proofs about comparison sorting.
Treat this document as research guidance, **not** a theorem/PR queue.
**Binding 2026-10-19 scope: unary only until fully completed.** The only
active encoding is `SORT-BOUND-U={1^n # 1^k:S(n)<=k}`, with
`S_unary(1^n)` its function counterpart. All active
agents must contribute to this unary research program. Binary encodings
are definitions/background only and must not generate separate
investigations before the unary goal is complete and the founder
authorizes a scope transition. See `AGENTS.md` and
[research orchestration](research-orchestration.md).

Do not produce a research note, script, test, or Lean statement merely
because an agent completed a work session; a concise result or obstacle
in Antonina issue #301 is the default.

## What we already have

The repository contains a faithful adaptive comparison-tree model, existence
and attainment proofs, information-theoretic and insertion upper bounds,
exact kernel-checked values through n=6, and the complete minimax correspondence
`S_eq_adv_univ` in `SoringP1/Minimax.lean`. For exact provenance and current gaps, see
`kernel-results.md`. The informal partial-order recurrence has a
`2^{O(n²)}` state-enumeration bound measured in numeric n; this is not a
kernel-checked machine-time theorem.

Exact values are already known in the literature through substantially
larger n than our evaluator handles. In particular `S(7)=13`, `S(8)=16`,
and `S(12)=30` are established; `ceil(log₂(12!))=29`. See
`literature.md` and `exploration-agenda.md`. Avoid re-proving literature
facts as the default research activity.

## High-risk questions bearing directly on S(n)

**Priority is the one-parameter problem `S(n)`, not incremental bounds for
arbitrary `F(P)`.** The latter matter only if they bridge to an asymptotic
algorithm, valid reduction, succinct representation or substantial no-go
theorem for the special input family.

Research should spend time on uncertain attempts, not merely polished
corollaries. The binding repository-wide orchestration policy requires distinct,
falsifiable, complexity-relevant investigations while maintaining a minimum of five running agents, with no maximum; subsections are not a mandatory task queue.
See [research orchestration](research-orchestration.md).

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
polynomial in the **unary** input length `N=n+k+1`. Separate unrestricted
decision-tree optimisation from the fixed one-parameter family S(n).
The unary threshold language is sparse: ordinary many-one NP-hardness
would imply P=NP by Mahaney's theorem. Record limitations on proposed
reductions *before* attempting a formal proof.

### Descriptive complexity of the unary threshold language

In addition to quantitative bounds, pursue **unary descriptive
complexity**. On appropriately ordered finite input structures, test
explicit logical definitions of `SORT-BOUND-U` in FO(PFP) (capturing
PSPACE), in a logic capturing EXPTIME, and the genuinely open smaller
descriptions FO(LFP) (P) and existential second-order logic (NP).
The already established unary PSPACE upper bound implies existence
of an FO(PFP) definition via the capture theorem; building an explicit
faithful formula remains a separate research problem. Do not infer a
smaller-class definition from a compact-looking informal recursion.

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

Progress requires a **material update to what is known or plausibly
possible about evaluating S(n)**: a new uniform bound/algorithm, a valid
complexity reduction or barrier, a global structural theorem with a
credible complexity consequence, or a serious falsification of a major
route. Investigations may leave only a compact comment with sources, the
sharpest argument, disproof attempts and open obstacle. A polished PR,
test file, research note, or increased agent count is **not itself mathematical
progress**. Active research must have a distinct falsifiable question
with a credible complexity consequence; there is a minimum of five active agents and no maximum.
Avoid repetitive paperwork or routine formalization. Do not turn every
small poset observation into a follow-up research task.

## Lean checkpoint, not Lean workstream

Preserve and test the existing kernel-checked model. The earlier minimax height proof is now complete in the kernel-checked
`minimaxTree_height` / `S_eq_adv_univ` results. Do not reopen it. A future Lean task needs an independent mathematical justification:
a meaningful new theorem, a mature algorithm, a subtle correctness proof,
or a necessary cost-model/correspondence bridge.

The long-term objective still includes kernel checking a major result. We
do **not** assume a P/NP separation exists or can be proved with the
currently available techniques.

## Parallel research discipline

Run independent SoringP1 agents on `billy-dev` for distinct, promising
mathematical questions. Replenish only when the next investigation has
a falsifiable objective and potential complexity consequence. Do not use
the number of open issues, host-load guesses, or absence of obvious new Lean
work as a reason to serialize exploration. The orchestrator reconciles claims,
reviews evidence and signs off on integrations; see
[research orchestration](research-orchestration.md).

## References and starting note

- [Exploration agenda and complexity barriers](exploration-agenda.md)
- [Primary literature and model checks](literature.md)
- [Exact problem statement and encodings](problem.md)
- [Formalization boundary](formalization-plan.md)
- [Kernel-checked results inventory](kernel-results.md)
