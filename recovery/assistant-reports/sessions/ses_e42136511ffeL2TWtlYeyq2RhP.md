# antonina-EWpZebvUIvhG3lxz07kAWC-fortunes

Session: ses_e42136511ffeL2TWtlYeyq2RhP
Workspace: /home/lubko/soring-fronts/sorting-number-monotonicity-all-n
Created: 1794187762676; updated: 1794187773497

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 19 (msg_1bdeca357001wqQnXHD9v0yrXa)

## Finding

**Claim:** Monotonicity holds: `S(n+1) ≥ S(n)` for all `n ≥ 0`. (Equivalent to `S(n)` nondecreasing.)

**Proof (deduction, paper argument):** Let `T` be an optimal decision tree sorting `n+1` distinct keys, with worst-case depth `S(n+1)`. Given `n` keys `x_1,…,x_n`, append a sentinel key `s` that is (conceptually) larger than all of them, and run `T` on `(x_1,…,x_n, s)`. Every comparison involving `s` has a *fixed* outcome (the sentinel is always the larger element), so those branches are deterministic and add no adaptive branching. The remaining comparisons among the `x_i` form a valid (possibly redundant) adaptive comparison tree sorting the `n` keys, with worst-case depth at most the depth of `T`. Hence `S(n) ≤ S(n+1)`.

This is an embedding/restriction argument; it does not require exhaustive enumeration and gives an all-`n` proof. No counterexample exists.

**Why it matters for the central question (complexity of exact `S(n)`):** Monotonicity justifies the standard threshold-language/interpolation assumptions: `SORT-BOUND-U = {1^n # 1^k : S(n) ≤ k}` is upward-closed in `k` for fixed `n`, and binary search on `k` (used in the `SORT-BOUND-U ∈ P ⟺ S_unary ∈ FP` equivalence in `docs/problem.md`) is valid. It also supports recurrence bounds that assume `S` does not decrease.

**Limits / what this is not:** This is a classical, elementary structural observation, not a new complexity result; it does not improve uniform bounds, give certificates, or change the PSPACE upper bound. It also does not settle monotonicity of *other* natural quantities (e.g., number of optimal trees), only worst-case depth.

**No repository changes made.** A clean worktree is the appropriate outcome per AGENTS.md: this is a deduction of a known structural fact, below the publication gate.
