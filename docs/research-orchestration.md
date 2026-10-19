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
* Threshold search in the `O(n)` interval between information
  and Ford-Johnson comparison bounds: reduce the **cost of a
  threshold decision**, not merely the number of candidates.
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
or old task assignments override this research scope. The obligation
to maintain ten active independent SoringP1 agents remains binding:
broaden the **unary** question portfolio instead of launching binary
fallback investigations.

## Parallelism is the default

Keep **at least ten simultaneously active SoringP1 research agents**
repository-wide whenever the complexity of S(n) remains open and research is
actionable. Ten is a minimum, not a cap. Count live SoringP1 workers (not Viche
or other-project agents), dispatch distinct independent packets to reach ten,
and replenish completions and failures during the same orchestration pass.
Use Antonina on **phoebe-dev only**. Do not serialize independent questions,
ration dispatches against guesses about RAM/CPU, or wait for a PR to merge
before launching unrelated work. Runtime resource management and actual
provider errors belong to the execution layer, not research prioritization.

If the apparent frontier has fewer than ten entries, diversify it before
accepting idle workers. Generate new representations, structural conjectures,
adversarial constructions, algorithms, complexity reductions, certificate
formalisms, source/model checks, cheap discriminating computations and scaffold
problems. Avoid near-identical "solve S(n)" prompts and artificial deliverables.

## Orchestrator's loop

1. Recover main/PR status, Antonina #301, the existing agent pool, completed
   research, outstanding mathematical assumptions, and any failed approaches.
2. Reconstruct the live portfolio of *materially different* approaches. A
   packet may exist without any corresponding GitHub issue or branch.
3. Select and dispatch enough independent, high-value packets to maintain at
   least ten concurrent SoringP1 research agents; retain separate worktrees
   for agents that may write files.
4. Every packet identifies a precise question, potential consequence for the
   **uniform computation of S(n)**, permitted assumptions, non-goals,
   falsification/evidence tasks and concise handoff conditions.
5. Collect results without waiting for all workers. When one ends or fails,
   reconcile its specific claims and replenish the portfolio and pool in the
   same pass. Retry transient infrastructure failures without mistaking them
   for mathematical refutations.
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

Ten agents is an execution policy, not evidence of a theorem. Do not treat
bounded experiments or agreement among agents as a proof. Separate
literature facts, conjectures, experiments, human proofs and Lean
kernel-checked statements. Do not infer the hardness of fixed S(n) from
hardness of arbitrary-poset optimization. The orchestrator retains final
mathematical review and integration responsibility.

This document and AGENTS.md supersede historical instructions that might
limit SoringP1 to fewer than ten active agents, forbid generating new frontier
packets, require an issue before dispatch, or turn host-load guesses into
research scheduling policy.
