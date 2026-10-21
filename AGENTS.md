# SoringP1 research and development contract

## Binding execution host (2026-10-21)
All SoringP1 Antonina/Viche agents, worktrees, manual development, and experiments run **only on `billy-dev`**, following the founder's migration from `phoebe-dev`. Old host references in historical research notes do not authorize work elsewhere. GitHub-hosted Actions CI, PR review, and hosting remain expressly permitted, including Lean verification. Preserve existing agent identities and research history across host migrations.

## Research objective

Study the computational complexity of computing the exact worst-case
comparison-sorting number S(n). The long-term goal includes Lean kernel-checked
results, but **discovery comes first**. See `docs/problem.md` for the fixed
model and encodings.

## Binding unary-first research priority (2026-10-19)

**Work exclusively on the unary-encoded problem first.** The active target
is `SORT-BOUND-U = {1^n # 1^k : S(n) <= k}`, equivalently uniform
evaluation of `S(n)` on input `1^n`. The resource input length is
`N=n+k+1` for the threshold language, and `N=n` for the function.
All live research packets, literature investigation, complexity-class
claims, descriptive-logic formulae, and agent assignments must explicitly
target the unary encoding and its uniform complexity.

**Defer binary-encoded `SORT-BOUND-B` and `S_binary` research until
the unary research objective is fully completed.** Do not run a parallel
binary-complexity workstream, pursue binary EXPSPACE/EXPTIME improvements,
or reopen binary work because a unary attack stalls or an agent becomes
idle. The existing binary definitions and established bounds remain as
historical mathematical context, not active tasks. Any future transition
requires completion of the unary agenda and explicit founder direction.
This directive supersedes older wording presenting both encodings as
equally active research priorities.

Maintain five **independent unary-focused** research agents on
`billy-dev` under the parallelism directive below. Diversify among
unary exact threshold algorithms, near-tight bound-gap tests, structural
obstructions and recurrences, sparse-language reductions and certificate
barriers, and descriptive complexity (ordered FO(LFP)/ESO/FO(PFP) and
EXPTIME logics). In descriptive complexity, distinguish the existence
of a defining formula by a capture theorem from constructing and
validating an explicit formula for this specific language. Do not claim
P/NP membership, hardness, or a separation without a proof.

## Binding research parallelism directive (2026-10-19)

**Target five simultaneously active SoringP1 research agents** while the
problem remains open and actionable. This is a **repository-wide steady-state
target, not a hard cap or a mandatory floor**. Check the current SoringP1 pool at
the start of each orchestration pass; launch a topologically independent batch
to reach a target of five, and replenish completed, failed or stalled agents in
the same pass. Do not leave useful workers idle while the orchestrator
personally pursues substantial research. Agents belonging to other projects
do not count toward the SoringP1 target.

**Explore a wide frontier.** If fewer than five obvious tasks exist, actively
generate distinct high-value research packets: alternative algorithms and
representations, complexity reductions, certificates, counterexample hunts,
primary-source audits, independent mathematical checks, and scaffold problems
whose implications for computing S(n) are explicit. Research packets need not
have pre-existing GitHub issues, PRs, branches or deliverable quotas. Give each
agent one falsifiable objective, non-goals, assumptions, evidence expectations,
and a durable handoff. Use independent worktrees for any write-capable agents.
Do not create duplicate prompts or fabricated milestones merely to fill slots.

**Schedule by mathematical dependencies, not by guessed resource capacity.**
Do not delay launches because of estimates of host load, memory, CPU, or model
cost; runtime execution management is separate from research orchestration.
Concrete provider failures, unavailable tools, and genuine dependency
collisions are to be reported and recovered from, not converted into an
unwritten concurrency cap. All SoringP1 agents and commands run on
`billy-dev` only. The orchestrator retains independent verification and
merging responsibility. Count of agents is an operational obligation, not
mathematical evidence of progress.

This directive **supersedes every earlier statement in this repository**
that could discourage useful saturation, impose a smaller pool, turn agent
availability into a reason to pause, or require work to originate in an issue.
The complexity-first publication gate remains: broad parallel exploration
does not mean producing PRs or Lean files for every investigation. Operational
details: [research orchestration](docs/research-orchestration.md).

## Binding reset: complexity-first research, not artifact production (2026-10-18)

**This section supersedes any older instructions that imply a required
research note, script, test, Lean proof, agent run, or PR per investigation.**
The expected result of most investigations is **increased understanding**,
including a falsified attractive conjecture, a precise obstruction, or an
honest inconclusive finding. A clean worktree and no PR are normal outcomes.
This does not suspend the five-agent research target or justify
leaving the frontier idle.

The sole research objective is a significant theorem about the **uniform
complexity of computing the special one-parameter function `S(n)`** or its
carefully encoded threshold language. Optimizing `F(P)` for arbitrary
partial orders is supporting research, not an end in itself: **before**
spending time on it, identify a plausible bridge to a uniform bound,
certificate, hardness reduction, exact structural characterization, or
fundamental obstacle for `S(n)`. If that bridge fails, say so and stop
that line instead of polishing supporting lemmas.

**New default for every research agent:**
1. Begin with one sharp question and at least one plausible line of
   attack that would change our view of `S(n)` if it succeeded.
2. Read relevant *primary literature*, carefully distinguish models,
   and try hard to disprove the idea (paper argument first, a small
   experiment only if it discriminates between hypotheses).
3. Explore multiple genuinely different hypotheses if needed; accept
   uncertainty and negative findings. Do not stop reasoning at the
   first small lemma, counterexample, or successful test.
4. Report substantive changes of knowledge, key references, failed
   attempts and the next decisive obstacle in **Antonina issue #301**.
   A concise research update is sufficient; **no mandatory artifact**.
5. Do **not** automatically create a branch, PR, new test suite,
   documentation page, GitHub issue or Lean milestone. Scratch experiments
   can remain local on Billy. Replenish the active research pool with
   independent, evidence-seeking packets, not routine artifact-production tasks.

**Exceptional publication gate.** Seek integration only for a meaningful
theoretical breakthrough about `S(n)`; a demonstrably improved uniform
asymptotic bound; a rigorous encoding-preserving hardness reduction;
a substantive, independently justified certificate/recurrence theorem;
a decisive no-go theorem excluding a major route; or a necessary fix to
model fidelity. First provide an independent paper argument, original
sources, a serious falsification attempt, and a short explanation of
**why this changes the central complexity question**. Then use minimal
tests and peer review; a PR is optional, not the reward or goal.
Formalize in Lean only when kernel checking would genuinely validate
such a mature result or a critical model/cost correspondence.

**Research scorecard:** What new claim about computing `S(n)` can we
defend? Which hypothesis was ruled out? Did a bound, algorithm, or valid
reduction change? What decisive question comes next? Counts of active
agents, PRs, CI passes, solved local poset examples and Lean files do
**not** measure mathematical progress. Nevertheless, maintain the binding
five-agent target: broaden independent research directions when a particular
route ends, rather than letting the pool drain or substituting routine
formalization. Document actual mathematical blockers without inventing
filler tasks.

The current open PR backlog is archival research, not a research
milestone. Triage once for correctness and relevance, then merge
substantive results or defer/close minor experiments with rationale.
Do not create derivative paperwork to 'finish' the backlog.

## Historical exploration-first guidance (2026-10-17)

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
- **The former narrowly scoped height exception is already completed:**
  `minimaxTree_height` and `S_eq_adv_univ` are kernel checked. Do not
  reopen that proof-engineering stream.
- Keep a target of five independent SoringP1 investigations live; diversify
  questions rather than duplicating tasks. Do not infer an obligation to
  formalize from the availability of agents.

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
