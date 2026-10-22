# SoringP1 research orchestration

This is SoringP1's operational adaptation of the exploration portfolio and
parallel worker principles inherited from AssemblyP1. The binding authority
is [AGENTS.md](../AGENTS.md).

## Binding scope: unary before binary

**All active research is unary-first until the unary classification
program is complete.** The target is
`SORT-BOUND-U={1^n # 1^k : S(n)<=k}` and its equivalent uniform
function problem `S_unary(1^n)`. For complexity statements, account for
the actual unary word input length `N=n+k+1`. Binary-encoded input
remains only in background definitions and previous established
results; there must be **no live binary work packets or binary
research agents** until the unary objective is resolved and the
founder authorizes broadening the scope. If an existing agent was
assigned binary work, steer it to a distinct unary line immediately.

The unary portfolio includes:
* Threshold search: the explicit finite Ford–Johnson gap is `O(n)`,
  but Sergeev's group-insertion theorem bounds the *true*
  asymptotic excess by `O(n/(log n)^(1/5))`. Investigate
  whether an effective finite upper bound can be extracted, and
  reduce the **cost of threshold tests** rather than merely
  their number. See [Sergeev research note](research-sergeev-asymptotic.md).
* Ordered-finite-structure descriptive complexity: FO(LFP) (P),
  existential second-order logic (NP), FO(PFP) (PSPACE), and an
  EXPTIME-capturing logic such as SO(LFP). The PSPACE upper bound
  already implies existence of a defining FO(PFP) sentence
  by the capture theorem; challenge agents to construct
  explicit formulae and verify their sorting-game semantics. See
  [Immerman's descriptive complexity references](https://people.cs.umass.edu/~immerman/descriptive_complexity.html)
  for the standard capture theorems. Take ordered finite input
  structures and well-formed unary words seriously.
* Unary-uniform algorithms and parameterizations, structural
  recurrences, information/pruning obstructions, certificate designs,
  sparse-language complexity barriers, and independent source audits.

Do not let apparent binary completeness, binary-specific techniques,
or old task assignments override this research scope. Do not launch binary
fallback investigations merely to create activity. Broaden the unary frontier
only where there is a distinct testable question.

## Parallelism follows the mathematical frontier

Launch independent SoringP1 researchers only for concrete, falsifiable
questions with a plausible bridge to the **uniform complexity of S(n)**.
The minimum is **five concurrently running agents, with no maximum**. Restore the minimum promptly after any completion or failure.
Run additional agents whenever genuinely distinct research questions exist. Do not spawn work just to
saturate an agent pool, and do not formalize routine intermediate results.

Use Antonina on **billy-dev only**. Do not serialize genuinely independent
questions or invent arbitrary resource-based concurrency ceilings. Actual
execution errors remain an execution concern, not a reason to degrade
the mathematical research standard.

## Orchestrator's loop

1. Recover main/PR status, Antonina #301, the existing agent pool, completed
   research, outstanding mathematical assumptions, and any failed approaches.
2. Reconstruct the live portfolio of *materially different* approaches. A
   packet may exist without any corresponding GitHub issue or branch.
3. Select and dispatch only packets with distinct, falsifiable goals and an
   explicit consequence for the complexity problem; retain separate worktrees
   for agents that may write files.
4. Every packet identifies a precise question, potential consequence for the
   **uniform computation of S(n)**, permitted assumptions, non-goals,
   falsification/evidence tasks and concise handoff conditions.
5. Collect results without waiting for all workers. When one ends or fails,
   reconcile its specific claims and replace it only if a new, nonredundant
   and well-motivated mathematical question is available. Retry transient
   infrastructure failures without mistaking them for mathematical refutations.
6. Compare conflicting claims proposition by proposition; an independent
   review or a bounded counterexample search is more useful than voting.
7. Record meaningful source facts, counterexamples, conjectures, proofs and
   mathematical obstacles durably (normally Antonina #301); reserve signed
   commits/PRs and Lean work for the existing exceptional publication gate.

## Independent research packet families

Work should span distinct questions, such as: tightness and size of the gap
between computable lower and upper bounds; algorithms avoiding exhaustive
enumeration of winning partial-order states; structural classification and
compression without counting every isomorphism class; lower-bound mechanisms
and n=12 obstructions; threshold certificates and exact verification cost;
encoding-faithful reductions for fixed-antichain S(n); additive/multiplicative
recurrences and subproblem composition; outside-literature/model audits;
independent falsification of central arguments; and algorithmic time/space
bounds measured against unary input length. These are examples, **not**
a cap, an exclusive list or a compulsory fixed one-agent-per-topic mapping.

## Non-negotiable distinctions

Agent count is never a substitute for a mathematical breakthrough. Do not treat
bounded experiments or agreement among agents as a proof. Separate
literature facts, conjectures, experiments, human proofs and Lean
kernel-checked statements. Do not infer the hardness of fixed S(n) from
hardness of arbitrary-poset optimization. The orchestrator retains final
mathematical review and integration responsibility.

This document and AGENTS.md supersede historical headcount targets and
procedural requirements that create work without a plausible complexity payoff.
