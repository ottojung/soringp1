# soringp1

**SoringP1** studies the computational complexity of the *sorting numbers*:
the function \(S(n)\) giving the minimum worst-case number of pairwise
comparisons needed to sort \(n\) distinct labelled items with a
deterministic adaptive comparison algorithm.

The question is how hard it is to **compute** \(S(n)\), not how hard it is
to sort. The long-term goal is a Lean kernel-checked result about that
complexity. This is a research goal, not a claimed theorem; no P/NP or
other separation is proved.

## Project status: suspended

Research was suspended on 2026-11-24. No new investigations or automated
research agents are authorized by the historical notes. The accumulated
research is now preserved on this default branch.

**Research website:** [Explore the live SoringP1 research library](https://ottojung.github.io/soringp1/).
The website source and local preview instructions are in [site/README.md](site/README.md).

**Start with the [research archive](recovery/README.md)**:

| What you want | Where to start |
|---|---|
| What was actually learned | [Research synthesis](recovery/SYNTHESIS.md) |
| Theorems, computations, conditional results, barriers | [Results and evidence register](recovery/RESULTS.md) |
| Conjectures, unsolved questions, failed approaches | [Open questions](recovery/OPEN-QUESTIONS.md) and [corrections](recovery/CORRECTIONS.md) |
| Every research direction and original evidence | [Complete topic and source catalogue](recovery/catalog/README.md) |
| Search the archive on a clone | [Search and integrity tools](recovery/tools/README.md) |
| Kernel-checked Lean theorems | [Formal theorem inventory](docs/kernel-results.md) |

The archive keeps historical reports and experimental code separate from
the maintained Lean library. A research agent's reported conclusion is
not a certified theorem.

## The problem

Complexity classes need an input encoding. The historical research focused on the unary
one:

\[
\mathrm{SORT\text{-}BOUND\text{-}U} = \{\,1^n \# 1^k : S(n) \le k\,\}
\]

with input length \(N = n + k + 1\), and the function \(S_{\mathrm{unary}}(1^n)\).
A binary encoding is defined for precision but was not an active research stream.
See [docs/problem.md](docs/problem.md) for exact definitions and for which
outcomes are realistically reachable.

## Where things stand

- **Upper bounds.** `SORT-BOUND-U ∈ PSPACE`. A budgeted depth-first search
  decides it in `2^{O(N log N)}` time and `O(N log N)` space, improving the
  `2^{O(n²)}` partial-order dynamic program.
- **Barriers.** The unary language is sparse, so many-one NP-hardness would
  imply P = NP, and it cannot be many-one EXPTIME-hard. There are
  `2^{(1/4−o(1)) n log² n}` distinct winning states at a single depth, so
  any method that enumerates winning states cannot beat the search exponent
  by more than a constant factor.
- **Lower bounds are out of reach.** Since the language is in PSPACE,
  proving it is not in P would prove P ≠ PSPACE.
- **Lean.** A faithful comparison-tree model, existence and attainment of
  \(S\), the information bound, monotonicity, exact values for
  \(n \le 6\), and the equivalence of \(S\) with the partial-order minimax
  value are kernel-checked with no `sorry` or custom axioms.
- **Literature.** Exact values are known for \(n \le 22\);
  \(S(12) = 30\) is the first value above \(\lceil \log_2 n! \rceil\), and
  \(S(n) - \log_2 n! = o(n)\) (Sergeev).

The full table of results, with status and links to the research notes,
is in [docs/research-plan.md](docs/research-plan.md).

## Documents

| Document | Contents |
|---|---|
| [AGENTS.md](AGENTS.md) | Research contract: scope, method, publication gate, Lean policy, model fidelity |
| [docs/problem.md](docs/problem.md) | Exact definitions, encodings, established facts, realistic outcomes |
| [docs/research-plan.md](docs/research-plan.md) | Known values, results so far, open questions |
| [docs/README.md](docs/README.md) | Short index of active vs historical research notes |
| [docs/research-framed-certificate-frontier.md](docs/research-framed-certificate-frontier.md) | Current proof-carrying certificate results, caveats, exact-completeness problem |
| [docs/kernel-results.md](docs/kernel-results.md) | Inventory of Lean-checked theorems |
| [docs/literature.md](docs/literature.md) | Primary sources |
| [docs/operations.md](docs/operations.md) | Execution host, research board, agent pool keeper |
| `docs/research-*.md` | Individual research notes, each with its status and companion script |

## Code

- `SoringP1/` — Lean 4 + Mathlib library (model in [`Model.lean`](SoringP1/Model.lean)).
- `scripts/` — reference evaluator (`evaluate.py`), research experiments,
  and operational tools (`agent_pool_keeper.py`, `board_digest.py`).
- `tests/` — Python regression tests: `python3 -m unittest discover -s tests`.

## Build

The Lean/Mathlib toolchain is pinned to the same version as AssemblyP1:

```sh
lake exe cache get
lake build --wfail
lake env leanchecker SoringP1
```

CI runs the Python tests on every change and rebuilds and kernel-replays
the Lean library whenever Lean-relevant files change. Merging to `main` is
the whole deployment; updating the agent pool on the execution host is a
separate step (see [docs/operations.md](docs/operations.md)).
