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

## Research

- [Problem statement and encodings](docs/problem.md)
- [Research directions and milestones](docs/research-plan.md)
- [Lean formalization boundary](docs/formalization-plan.md)
- [Research and evidence workflow](AGENTS.md)
- [Lean model](SoringP1/Model.lean)

Like [AssemblyP1](https://github.com/ottojung/assemblyp1), this project is
**exploration-first**: formalize an exact target early, then investigate on
paper and by computation, and kernel-check mature results rather than building
speculative Lean infrastructure.

## Build

The Lean/Mathlib toolchain is pinned to the same version as the
AssemblyP1 bootstrap:

```sh
lake exe cache get
lake build --wfail
lake env leanchecker SoringP1
```

CI builds and kernel-replays the proof modules. The current formal
foundation is intentionally small; **no P/NP separation is proved yet**.
