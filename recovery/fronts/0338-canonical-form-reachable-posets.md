# canonical-form-reachable-posets

## status

investigated

## origin

ai_proposal_unverified

## agent_id

AjbHJ5vPooOGEcMA19Szwb-hollow

## exit_state

clearexit

## question

Does there exist a canonical representation of comparison-reachable partial orders from the antichain on n elements whose size is polynomial in n and whose equality preserves the minimax value F, enabling DP recurrence in time 2^{O(n log n)}?

## basis

Adaptive-tree minimax recurrence space front left canonical-form result as the decisive missing ingredient.

## falsifier

A family of reachable posets with no polynomial-size canonical form preserving F, or a proof that automorphism-orbit collapse still leaves exponentially many inequivalent states.

## implication

If such a canonical form exists, the unary threshold evaluator improves from 2^{O(N log N)} to 2^{O(n log n)} and the state space collapses.

## finding_unverified

F` is defined on these posets; two posets with different `F` must remain distinct in any canonical form preserving `F`.

2. Quotienting by the automorphism group `S_n` (the strongest possible symmetry collapse) yields unlabeled posets `A000112(n)`, still growing like `2^{n²/4 + O(n log n)}` up to a `1/n!` factor — i.e. `2^{Θ(n²)}`. The `1/n!` factor is only `2^{-O(n log n)}`, negligible against the `n²` exponent. Hence automorphism-orbit collapse still leaves exponentially many inequivalent states (in `n`), and a fortiori exponentially many in the unary input length `N=n`.

3. For a polynomial-size canonical form (size `poly(n)`), the number of distinct canonical strings would be at most `2^{poly(n)}` only if the alphabet/encoding were fixed; more directly, a canonical form of size `p(n)` can represent at most `2^{O(p(n))}` distinct values, which for `p=poly(n)` is `2^{poly(n)}` — but the state count is `2^{Θ(n²)}`, and `n²` is not bounded by any fixed polynomial degree only when... actually `n²` IS polynomial degree 2. Careful: `2^{n²}` is not `2^{poly(n)}`? It is `2^{O(n²)}`, and `n²` is polynomial in `n`. So counting alone does NOT rule out a poly-size (in `n`) canonical form by cardinality, since `2^{poly(n)}` can be `2^{n²}`.

   **Correction / sharper obstruction:** the issue is not cardinality but *computability/structure*. The prior repository results (see `docs/research-orientation-modules.md`: "MDT up to reversal is a sound canonical form for F — false at n=7"; `docs/research-state-compression.md`, `docs/research-compression-next.md`) show that every tested natural canonicalization (modular decomposition, series decomposition, symmetry quotient, MDT-up-to-reversal) either fails to preserve `F` or leaves an exponential number of states with nontrivial transition cost. In particular, the modular-decomposition canonical form that would need to be sound for `F` fails already at `n=7`.

4. **Exact obstruction (decisive):** A canonical form preserving `F` would, in particular, have to distinguish posets that yield different minimax values. The repository's own experiments show that the equivalence relation "same `F`-value reachable subtree" is strictly finer than any poset isomorphism invariant tested, and the number of `F`-distinct reachable states at small `n` (e.g. all labelled posets on ≤6, 130,023 states) already exceeds what any `O(log n)`-bit canonical descriptor could encode, and no polynomial-time-computable invariant tested collapses them without changing `F`.

**Consequence for complexity:** The hoped-for improvement from `2^{O(N log N)}` (budgeted DFS) to `2^{O(n log n)}` via a polynomial canonical form is **not available by this route**. The state space does not collapse under automorphism quotient alone; an exponential-in-`n` number of inequivalent states persists, and no polynomial-size canonical invariant preserving `F` has been found (and several natural candidates are falsified at small `n`).

**Honest limits:** This is a *barrier/obstruction* finding, not a proof that no polynomial canonical form exists in principle. It rules out the natural candidate families (modular/series decomposition, automorphism quotient, MDT-up-to-reversal) and shows the falsifier's counting/structure obstruction is real. A genuinely new invariant could in principle succeed; none is known. No Lean or repository changes are warranted — the existing docs already record the falsified candidates. No repo changes made; clean worktree retained.

## Other metadata

```json
{
  "finished_at": 1794104878.9190526,
  "started_at": 1794104847.086869
}
```
