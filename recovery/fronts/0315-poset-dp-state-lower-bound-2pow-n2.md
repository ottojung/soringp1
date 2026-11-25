# poset-dp-state-lower-bound-2pow-n2

## status

investigated

## origin

ai_proposal_unverified

## agent_id

sdcXVutEtqKmYl6eGxMprv-pensions

## exit_state

clearexit

## question

Is the 2^{O(n^2)} state/representation complexity of known exact poset-DP evaluation of S(n) improvable to 2^{o(n^2)} for all n by any sound and complete uniform representation of root-reachable minimax states, or does every such representation require 2^{Omega(n^2)} distinct states on some infinite family?

## basis

The partial-order minimax recurrence gives time 2^{O(n^2)} in numeric n (docs/problem.md, docs/upper-bound.md); prior winning-frontier/isomorphism barriers target specific enumerations, not all sound complete DP representations. Any lower bound must fix the representation/completeness class precisely.

## falsifier

Give a uniform exact algorithm/representation for S(n) with a proved 2^{o(n^2)} bound on distinct represented states (and argue soundness/completeness for the S(n) minimax value); alternatively prove an information-theoretic or adversary-forcing state lower bound of 2^{Omega(n^2)} for a precisely defined class of complete root-reachable state representations.

## implication

A 2^{o(n^2)} sound complete state representation would asymptotically improve exact evaluation bounds for S(n); a 2^{Omega(n^2)} lower bound for a broad complete representation class would be a barrier to poset-DP-style exact methods without implying P!=PSPACE or other separations.

## finding_unverified

on-summary-evaluator` is `investigated/clearexit` with no theorem/counterexample established in the recorded finding. So C_table-by-isomorphism is 2^{Θ(n^2)}, but **C_table-by-some-sound-F-congruence being 2^{Omega(n^2)} is OPEN**.

## 3) Root-optimal-play / winning-frontier restriction — no 2^{Omega(n^2)} lower bound known (literature in repo)
- `docs/research-winning-frontier-barrier.md`: `2^{(1/4-o(1))n (log n)^2}` nonisomorphic *winning* states at a common depth (and extension to `k=S(n)`). This is `2^{ω(n log n)}` but **`2^{o(n^2)}`**, hence it **cannot** yield a 2^{Omega(n^2)} representation lower bound and is only an enumeration barrier.
- Whether the set of states on *some/all* height-`S(n)` optimal plays, under a sound complete minimax representation, admits 2^{o(n^2)} (or forces 2^{Omega(n^2)}) is **open**. This is the substantive gap behind the front.

## 4) Why a 2^{Omega(n^2)} lower bound for a broad complete class would matter (and why it’s hard)
A proved 2^{Omega(n^2)} lower bound for a *precisely defined, broad* class of sound complete uniform representations of root-reachable minimax states would be a **barrier to that class** of exact poset-DP methods, but (per AGENTS/problem.md) would **not** imply `P!=PSPACE` or a separation; general exact evaluation already has transcript-DFS `2^{O(n log^2 n)}` time / polynomial space (`SORT-BOUND-U ∈ PSPACE`).

## Concrete failed/blocked routes (this pass)
1. **“Any representation => 2^{Omega(n^2)}”** — falsified by budgeted DFS visited-state count 2^{o(n^2)} under the natural broad reading (§1). The front must restrict to stored/memoized poset-state representations to be nontrivial.
2. **Winning frontier => 2^{Omega(n^2)}** — exponent is `Θ(n log^2 n)`, wrong scale (§3).
3. **All reachable posets force 2^{Omega(n^2)} under F-sound quotient** — reachable domain is 2^{Θ(n^2)} but sound F-quotient size is unresolved; coarse numeric invariants fail soundness (state-compression falsification). No new F-collision/counterexample or quotient upper bound established.
4. **Certificate/DAG compression => 2^{Omega(n^2)} necessary** — `docs/research-certificates-barriers.md`/fronts: worst-case poset-DAG may be large, but no all-n polynomial/2^{o(n^2)} sound complete framed representation is proved or refuted; completeness of succinct certificates is open.

## Honest limits / what would settle it
- **Not proved:** any 2^{Omega(n^2)} lower bound for a broad sound+complete representation class beyond the trivial cardinality of the *all-labelled-posets identity table* (and isomorphism table).
- **Not proved:** a 2^{o(n^2)} sound complete *memoized poset-state* representation (a genuine DP-state compression beating A000112/A001035 asymptotically while preserving exact `F`/threshold completeness).
- **Decisive next steps (falsifiable):** (a) define a formal “poset-state DP representation” (keys = computable functions of `P,budget/depth` with a local recurrence/completeness condition) and prove either a 2^{Omega(n^2)} counting/adversary lower bound on keys, or construct a 2^{o(n^2)}-key sound complete scheme; (b) resolve sound F-bisimulation/summary size on root-reachable (or root-optimal) states with an all-n proof or explicit infinite counterexample family. Small-n experiments alone would not settle (a)/(b).
- I made **no** Lean/repo changes and posted nothing to the board; the ledger entry remains `running`. This is a **paper-level analysis/obstruction report**, not a new kernel-checkable theorem.

## Other metadata

```json
{
  "finished_at": 1793872797.724202,
  "started_at": 1793872541.7544024
}
```
