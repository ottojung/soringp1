# soringp1

**SoringP1** studies the computational complexity of the *sorting numbers*: the function
\(S(n)\) giving the minimum worst-case number of pairwise comparisons required
to sort \(n\) distinct labelled items with a deterministic adaptive comparison
algorithm.

The long-term goal is a **Lean kernel-checked classification** of the complexity
of evaluating \(S\), including whether efficient algorithms or unconditional
lower bounds are possible. This is a research goal, **not a claimed theorem**.

## What exactly is being classified?

Complexity classes require a representation of the input. We study both:

- **Unary parameterization**: compute \(S(n)\) on input \(1^n\), returning a
  binary integer. Here a dynamic program over partial orders gives a
  \(2^{O(n^2)}\)-time upper bound, placing the associated threshold language
  in **EXPTIME**.
- **Binary parameterization**: compute \(S(n)\) on the binary representation
  of \(n\). The same algorithm gives a **double-exponential** upper bound
  in the bit length; an EXPTIME bound does *not* follow.

The canonical decision language for discussing P, NP, and EXPTIME is
\(\mathrm{SORT\text{-}BOUND}_{\mathrm{unary}}
 = \{(1^n,1^k) : S(n)\le k\}\).
NP does not directly classify a numeric function; its membership for this
language is a research question, not an assumption. See
[the problem statement](docs/problem.md) for exact definitions and caveats.

## Active direction: exploration before further formalization

As of October 17, 2026, **mathematical exploration is the default**. The
Lean foundation remains checked and maintained, but routine lemmas and
known small-instance results are no longer the research queue. The priority
is to find and falsify structural hypotheses, understand established
sorting-number literature, improve exact algorithms, and study realistic
complexity-class and certificate barriers. Return to Lean for a mature,
substantive discovery or an essential correctness/cost-model bridge.

- [Exploration agenda, known results and sparsity barrier](docs/exploration-agenda.md)
- [Problem statement and encodings](docs/problem.md)
- [Research directions and milestones](docs/research-plan.md)
- [Lean formalization boundary](docs/formalization-plan.md)
- [Research and evidence workflow](AGENTS.md)
- [Lean model](SoringP1/Model.lean)

The [development contract](AGENTS.md) makes this priority explicit for agents.
The outstanding minimax correspondence may be finished if straightforward;
otherwise document the Lean blocker and redirect effort toward research.

## Build

The Lean/Mathlib toolchain is pinned to the same version as the
AssemblyP1 bootstrap:

```sh
lake exe cache get
lake build --wfail
lake env leanchecker SoringP1
```

CI builds and kernel-replays the existing proof modules. **No P/NP
separation is proved yet.** This research repository has no application
server to deploy: merging to `main` publishes the research instructions;
Viche/Antonina worker scheduling is a separate operational change.
