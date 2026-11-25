# optfeasible-state-multiplicity-per-ef-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ewllPxEuDtK1EmuMI4bKv2-reacted

## exit_state

clearexit

## question

For all sufficiently large n, does the optimal-feasible slice (states reachable within S(n) comparisons from the n-antichain on a height-S(n) sorting tree) contain superpolynomially many states sharing both the same extension count e(P) and the same minimax value F(P)?

## basis

Prior optimal-feasible e-collision construction yields 2^{Omega(sqrt(n/log n))} states per e but only two F-values; distinct F-values per e are bounded by S(n)+1=O(n log n); state multiplicity per (e,F) remains open.

## falsifier

Exhibit an infinite family of n with superpolynomially many optimal-feasible states sharing one (e,F) pair but not isomorphic, or prove every (e,F) pair has only polynomially many optimal-feasible states.

## implication

Superpolynomial multiplicity would show an e-and-F-keyed exact dynamic program has superpolynomial ambiguity on the only states relevant to S(n); a polynomial bound would leave compact e+F indexing viable.

## finding_unverified

gle external write)

- **Posted:** Antonina board #301 comment as `SoringP1 frontier: optimal-feasible-state-multiplicity-per-ef-alln` (JSON redirected to `/tmp/opencode/mult/comment301.json`, exit 0). No other external side effects (no commits, PRs, Lean/repo edits, no duplicate posts).
- **Environment/state checked:** billy-dev, sourced `/home/lubko/.profile`; studied `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, and board #301 (recent posts incl. `superpoly-optimal-feasible-e-collisions` 2026-11-20T08:12:02Z / exec verification and `minimax-multiplicity-per-extension-count-optfeasible-alln` 08:47:55Z). Worktree clean at `6a96398`.
- **Front attacked (all-n, falsifiable):** optimal-feasible slice multiplicity per `(e(P),F(P))` (states reachable within `S(n)` comparisons from `A_n` on a height-`S(n)` sorting tree). Falsifier: superpolynomially many pairwise nonisomorphic optimal-feasible states sharing one `(e,F)` vs polynomial bound per pair. Complexity implication reported only as an `(e,F)`-keyed exact-DP ambiguity/barrier (no class-separation claim).

## Mathematical finding (partial / negative; no theorem completion)
- **Definitions/solver (scratch `/tmp/opencode/mult`, from scratch):** transitively closed poset states (bitmasks), `e(P)` via subset-DP linear-extension count, `F(P)` via memoized unrestricted minimax `F(P)=0` if total else `1+min_{(a,b)} max(F(P|a<b),F(P|b<a))`, BFS minimal-depth reachability `d_min` from `A_n`, optimal-feasible filter `d_min(P)+F(P) <= S(n)`, unlabelled canonicalization by min-over-permutations.
- **Search performed:**
  - Exhaustive all posets `n<=5`: unlabelled isomorphism types per `(e,F)` max = 1,1,2,3,7 for `n=1..5`.
  - Optimal-feasible slice `n<=5` (`S=0,1,3,5,7`): reachable 1,3,19,219,4231 states, groups 1,2,4,8,14, max unlabelled types per `(e,F)` = 1,1,2,3,4.
  - Disjoint-union-of-chains family (partitions of `m`, `e = m! / Π L_i!`): factorial-product `e`-collisions enumerated for `m<=12` (e.g. `m=7` prod 24: `[4,1,1,1],[3,2,2]`; multiple groups up to 3-way at `m=12`). Computed `F`: `[4,1,1,1]` gives `n=7,e=210,F=9` vs `[3,2,2]` gives `n=7,e=210,F=8` (same `e`, different `F`, no `(e,F)` collision). Partial `m=7` minimax (completed through `[2,2,2,1]`) showed no `(e,F)` collision among completed cases.
- **Result:** No `(e,F)`-collision found in computed cases. The prior 08:12Z optimal-feasible `e`-collision construction gives `2^{Ω(sqrt(n/log n))}` states per `e` but split across different `F` values with distinct index sets yielding distinct `e`, so it provides multiplicity 1 per `(e,F)` (removes that direct source, not a bound). **No theorem, no infinite `(e,F)`-collision family, no polynomial upper bound.**

## Exact obstruction / honest limits
- The all-`n` question remains open: neither superpolynomial `(e,F)` multiplicity on the optimal-feasible slice nor a polynomial bound was established.
- **Limits:** exact minimax `F` too costly for larger chain-union collision groups (timed out/killed for `m>=10`/some `m=7` tails) and exhaustive optimal-feasible enumeration stopped at `n=5`; search covered only all posets `n<=5` and chain unions (not a systematic large-`n` optimal-feasible/optimal-tree search). Small-`n` data show tiny multiplicities but no growth argument; equal `e` did not force equal `F` in tested chain collisions, but no general separation/identification principle was proved. No claim on `SORT-BOUND-U` membership or complexity-class separation.

## Other metadata

```json
{
  "finished_at": 1795167383.4567065,
  "started_at": 1795166016.63771
}
```
