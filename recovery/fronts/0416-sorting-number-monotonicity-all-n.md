# sorting-number-monotonicity-all-n

## status

investigated

## origin

ai_proposal_unverified

## agent_id

EWpZebvUIvhG3lxz07kAWC-fortunes

## exit_state

clearexit

## question

Is S(n) nondecreasing in n for all n, i.e. S(n+1) >= S(n), and can an all-n proof or counterexample be given without exhaustive enumeration?

## basis

docs/problem.md defines S(n) as exact minimum worst-case comparisons; monotonicity is assumed but not proved in repository.

## falsifier

Exhibit an explicit n where an optimal (n+1)-element sorting tree has strictly smaller worst-case depth than S(n), or prove monotonicity for all n.

## implication

Monotonicity would simplify threshold languages and recurrence bounds; a counterexample would break standard S(n) interpolation assumptions.

## finding_unverified

## Finding

**Claim:** Monotonicity holds: `S(n+1) ≥ S(n)` for all `n ≥ 0`. (Equivalent to `S(n)` nondecreasing.)

**Proof (deduction, paper argument):** Let `T` be an optimal decision tree sorting `n+1` distinct keys, with worst-case depth `S(n+1)`. Given `n` keys `x_1,…,x_n`, append a sentinel key `s` that is (conceptually) larger than all of them, and run `T` on `(x_1,…,x_n, s)`. Every comparison involving `s` has a *fixed* outcome (the sentinel is always the larger element), so those branches are deterministic and add no adaptive branching. The remaining comparisons among the `x_i` form a valid (possibly redundant) adaptive comparison tree sorting the `n` keys, with worst-case depth at most the depth of `T`. Hence `S(n) ≤ S(n+1)`.

This is an embedding/restriction argument; it does not require exhaustive enumeration and gives an all-`n` proof. No counterexample exists.

**Why it matters for the central question (complexity of exact `S(n)`):** Monotonicity justifies the standard threshold-language/interpolation assumptions: `SORT-BOUND-U = {1^n # 1^k : S(n) ≤ k}` is upward-closed in `k` for fixed `n`, and binary search on `k` (used in the `SORT-BOUND-U ∈ P ⟺ S_unary ∈ FP` equivalence in `docs/problem.md`) is valid. It also supports recurrence bounds that assume `S` does not decrease.

**Limits / what this is not:** This is a classical, elementary structural observation, not a new complexity result; it does not improve uniform bounds, give certificates, or change the PSPACE upper bound. It also does not settle monotonicity of *other* natural quantities (e.g., number of optimal trees), only worst-case depth.

**No repository changes made.** A clean worktree is the appropriate outcome per AGENTS.md: this is a deduction of a known structural fact, below the publication gate.

## Other metadata

```json
{
  "finished_at": 1794187796.646554,
  "started_at": 1794187761.792523
}
```
