# Documentation guide

The project studies the **uniform complexity of exact adaptive sorting numbers**.
Use this index rather than treating every historical research note as an
active task. [`AGENTS.md`](../AGENTS.md) is the current authority for
research direction and Lean policy; previous instructions in notes are
historical.

## Start here

| File | Purpose |
|---|---|
| [Problem and encoding](problem.md) | Definition of `S(n)`; active unary threshold |
| [Research plan](research-plan.md) | Proven results, limits, open complexity targets |
| [Literature](literature.md) | Original papers and model distinctions |
| [Framed certificates](research-framed-certificate-frontier.md) | Consolidated proof-carrying DAG constructions, entropy bound, what is still unproved |
| [Lean kernel inventory](kernel-results.md) | What is actually kernel checked |
| [Operations](operations.md) | Billy-only agent execution, board, keeper |

## Proven algorithmic bounds and barriers

- [Exact budgeted DFS](research-budgeted-dfs.md) — unary threshold in
  `2^{O(N log N)}` time and `O(N log N)` work space.
- [Certificate and class barriers](research-certificates-barriers.md),
  [encoding consequences](research-encoding-consequences.md), and
  [hardness boundaries](research-hardness-boundaries.md) — sparse unary
  language, advice, and transfer limitations.
- [Large winning-frontier barrier](research-winning-frontier-barrier.md)
  — counting states is not a plausible exact polynomial evaluator.
- [Sergeev's bound](research-sergeev-asymptotic.md) — the known
  `log₂(n!)+o(n)` sorting-comparison bound, not an exact evaluator.
- [Structural lower bounds](research-structural-lower-bounds.md),
  [one-ply obstructions](research-one-ply-obstruction.md), and
  [n=12 source audit](research-obstruction-next.md).

## Supporting and historical investigations

These provide examples, source audits, algorithms, or **negative**
findings. They are not independent milestones to formalize in Lean.

| Theme | Notes |
|---|---|
| Earlier certificate proposals | [strategy DAGs](research-strategy-certificates.md), [state compression](research-state-compression.md), [two-phase compositional barrier](research-fo-tc-twophase.md) |
| Exact-state decomposition and quotient | [compression](research-compression-next.md), [series decomposition](research-series-decomposition.md), [orientation modules](research-orientation-modules.md), [parallel duality](research-parallel-duality.md) |
| Research on search cost | [time exponent](research-time-exponent.md), [budget pruning](research-budget-pruning.md), [bidirectional advice](research-bidirectional-advice.md), [upper witnesses](research-upper-witnesses.md) |
| Earlier input/certificate analysis | [decision encoding](research-decision-encoding.md), [n=12 non-tightness](research-n12-nontightness.md) |

The machine-readable [research packets](research-packets.json) are for
curated Billy agents, not a list of established mathematical results.

## Active GitHub discussions

- [#47: Exact optimal framed-DAG certificates](https://github.com/ottojung/soringp1/issues/47)
- [#48: Root-specific adversarial lower-bound rule](https://github.com/ottojung/soringp1/issues/48)

Old closed pull requests and their branches are part of the provenance,
not ongoing tasks. The branch-hygiene workflow removes only branches
proved safe to retire, not unmerged experimental results.
