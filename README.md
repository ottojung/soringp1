# soringp1

**SoringP1** studies the computational complexity of the *sorting numbers*: the function
\(S(n)\) giving the minimum worst-case number of pairwise comparisons required
to sort \(n\) distinct labelled items with a deterministic adaptive comparison
algorithm.

The long-term goal is a **Lean kernel-checked classification** of the complexity
of evaluating \(S\), including whether efficient algorithms or unconditional
lower bounds are possible. This is a research goal, **not a claimed theorem**.

## What exactly is being classified?

**Current binding research scope: unary first (October 19, 2026).**
All active work and a target of five concurrent independent research agents
focus on `SORT-BOUND-U` and `S_unary`. Binary versions below remain
mathematically defined and their previously proved bounds are preserved
for reference, but **no new binary research proceeds until unary work
is complete and the founder directs the transition**. See
[unary-first research orchestration](docs/research-orchestration.md).

Complexity classes require a representation of the input. We define both
variants below for completeness, but only the unary encoding is an active
research target:

- **Unary parameterization**: compute \(S(n)\) on input \(1^n\), returning a
  binary integer. A dynamic program over partial orders gives a
  \(2^{O(n^2)}\)-time upper bound (**EXPTIME**); a tighter game/ATM
  formulation improves this to **PSPACE** (see the research notes below).
- **Binary parameterization**: compute \(S(n)\) on the binary representation
  of \(n\). The dynamic-program algorithm gives a **double-exponential**
  upper bound in the bit length; the game/ATM formulation improves this to
  **EXPSPACE**.

The canonical decision language for discussing P, NP, and EXPTIME is
\(\mathrm{SORT\text{-}BOUND}_{\mathrm{unary}}
 = \{(1^n,1^k) : S(n)\le k\}\).
NP does not directly classify a numeric function; its membership for this
language is a research question, not an assumption. See
[the problem statement](docs/problem.md) for exact definitions and caveats.

**Known asymptotic comparison-count bound (not an evaluator):**
Sergeev proved `S(n)−log₂(n!)=O(n/(log n)^(1/5))=o(n)`,
improving the classical linear Ford–Johnson gap. It does not
compute exact `S(n)` or give an explicit finite numeric bound
without instantiating constants. See [primary-source research
note](docs/research-sergeev-asymptotic.md).

## Active direction: complexity-first theory with broad parallel exploration

**October 18, 2026 pivot:** The active goal is to change what we know about
the *uniform complexity of evaluating S(n)*. Research agents are free to
spend time on open-ended arguments, hypotheses and primary literature,
including approaches that fail. A routine partial-order counterexample,
small-n test, research note, PR or Lean lemma is **not** a milestone.
Aim for **five concurrent SoringP1 research agents** on independent
questions via Antonina on **phoebe-dev**, under the binding
[research orchestration](docs/research-orchestration.md) policy.
Agent count is not evidence of a breakthrough; diversify exploratory packets
rather than generating filler PRs. Agents report findings and obstacles
briefly to Antonina issue #301 without a mandatory commit; only mature
results important to the central question go through review/publication. Existing research remains archived.


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

### Research deliverables (exploration-first, 2026-10-17)

These are research notes (not Lean theorems), each with a companion program:

- [Structural compression of the minimax state space](docs/research-state-compression.md)
  — `scripts/state_compression.py`. Reachable states are exactly the labelled
  posets (OEIS A001035); the `S_n` symmetry quotient is exact and recomputes
  `S(8)=16`, `S(9)=19`; falsifies linear-extension-count and balanced-greedy
  compression.
- [Succinct certificates and complexity barriers](docs/research-certificates-barriers.md).
  Improves the upper bounds to `SORT-BOUND-U ∈ PSPACE`, `SORT-BOUND-B ∈ EXPSPACE`
  (game/ATM + `APTIME = PSPACE`); the unary language is sparse (Mahaney), the
  binary one is not; a **reduced** explicit sorting-tree witness has
  `2·n! − 1` nodes and is not polynomial-sized in the input. This does
  **not** rule out a different polynomial-size NP certificate.
- [Why the information bound is not tight at n = 12](docs/research-n12-nontightness.md)
  — `scripts/nontightness_experiments.py`. Audits Wells/Peczarski/Stober–Weiß;
  the efficiency pruning is equivalent to leaf counting; five scalar invariants
  are falsified with smallest witnesses (same-`e` at `n = 5`, non-monotonicity
  at `n = 6`, merge family `Merge(2,4)`).
- [Budgeted DFS for exact S(n)](docs/research-budgeted-dfs.md)
  — `scripts/budgeted_dfs.py`, `scripts/transcript_dfs.py`. Pure budgeted DFS
  `CanSort(P,d)` (no memoization, no advice) decides `S(n) ≤ k`; deterministic
  time `2^{O(n log² n)}` in numeric `n`, improving the recorded `2^{O(n²)}` DP
  bound. The transcript-only implementation decides comparability by graph
  reachability and uses `O(n log² n)` bits of work space (vs `O(n³ log n)` for
  a matrix-per-frame version); this also gives a sublinear-space upper bound
  `O(√N log² N)` for dense-matrix `GEN-SORT` (`N = Ω(n²)`).
  For unary `SORT-BOUND-U` with actual word length `N=n+k+1`,
  budget-specific DFS gives the sharper **deterministic time
  `2^{O(N log N)}` and work space `O(N log N)` bits** (see §5.3 of
  the DFS note). All are upper bounds only, not class separations.
- [Sound pruning and move reduction for the budgeted DFS](docs/research-budget-pruning.md)
  — `scripts/budgeted_pruning_experiments.py`. Provably sound, poly-space
  pruning: the poset-level information cutoff `e(P) > 2^d`, the Hanamura–Iwata
  `e ≤ 7` acceptance base, and `Aut(P)` move orbits (both outcomes retained).
  Cuts the `S(5)` binary search `261,662 → 750` calls (349×) and preserves
  `S(0..5)`; ordinal-sum allocation is exact but does not reduce no-memoization
  calls (negative result). No asymptotic exponent improvement; the cutoff stops
  helping exactly at the `n = 12` information-bound gap.
- [Hardness boundaries between generalized and antichain sorting](docs/research-hardness-boundaries.md)
  — `scripts/hardness_boundaries.py`. Compares generalized `CanSort(P,k)` with
  the antichain `S(n) ≤ k`; the containment reduction is polynomial only under
  the unary encoding; audits Hyafil–Rivest (arbitrary subset tests) and Cardinal
  et al. (constant-factor approximation, not exact); `e(P)` does not determine
  `S(P)` (smallest witness `n = 5`, `e = 8`, `S = 3` vs `4`). No NP-hardness
  or separation is claimed.

The reference minimax evaluator is `scripts/evaluate.py` (exact for small `n`).

The [development contract](AGENTS.md) makes this priority explicit for agents.
The minimax correspondence `S_eq_adv_univ` is now kernel-checked (A24).
The remaining open problem is the uniform complexity of evaluating it;
further routine Lean milestones are not the priority.

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
