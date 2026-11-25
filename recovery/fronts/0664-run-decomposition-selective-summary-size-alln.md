# run-decomposition-selective-summary-size-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

KCeOqYisevZ75Zh6Wa6WNd-pigment

## exit_state

clearexit

## question

For the ordered-run decomposition of a partial order reachable from the n-antichain, is there a polynomial-size sound selective summary of the full cross-run merge history that determines the exact minimax value F(P) for all sufficiently large n, or does every such summary require superpolynomially many distinct classes?

## basis

Board #301 run-decomposition result (2026-11-21T23:32Z) and winning-frontier barrier in docs/research-winning-frontier-barrier.md; antichain root model in docs/problem.md.

## falsifier

Exhibit an infinite family of root-optimal ordered-run posets whose exact minimax values remain distinct under every polynomial-time computable selective summary, or prove a concrete polynomial-size summary family is sound and complete for all large n.

## implication

A polynomial sound selective summary would reduce exact sorting-number evaluation below the winning-frontier exponent; a superpolynomial lower bound would make the run-decomposition enumeration barrier structural for all exact evaluators using run states.

## finding_unverified

## Finding

**The literal “superpolynomially many distinct classes” horn is not forced by the winning-frontier enumeration, and the positive horn is not a combinatorial compression question—it is exactly the open question of whether `F(P)` is polynomial-time computable on ordered-run posets.**

### What I checked

- `docs/research-winning-frontier-barrier.md` and the accepted run-decomposition result (board #301, 2026-11-21T23:32Z): the winning-frontier family `P_A` has at least  
  `2^{(1/4-o(1)) n (log n)^2}` pairwise nonisomorphic members, all reachable, all winning (`F(P_A) ≤ B = O(n log n)`).
- `docs/research-state-compression.md` / `research-compression-next.md`: sound DP quotients need **both** value-invariance and equivariant transitions; invariants such as linear-extension count, comparability graph, and degree signatures fail.
- `docs/research-n12-nontightness.md` and the compact-`F` result: `F(P)` ranges over only `{0,…,S(n)}`, so `S(n)+1 = O(n log n)` values. Hence the winning-frontier family is **`F`-degenerate**: exponentially many nonisomorphic posets collapse into only polynomially many `F`-values.

### The refutation of the counting horn

If a summary “determines the exact minimax value `F(P)`,” then two posets with different `F`-values cannot share a class. But the number of possible `F`-values for an `n`-element poset reachable from the antichain is at most

```
S(n)+1 = O(n log n),
```

which is polynomial in `n`. Therefore no family of exact-value summaries can be forced to have superpolynomially many *value-classes*. The `2^{Ω(n log² n)}` quantity in the winning-frontier theorem is a property of the **isomorphism/transcript representation**, not of the function `F`. Any superpolynomial lower bound on “distinct classes” must therefore be a **computational** lower bound, not a counting one.

### What a positive answer would actually require

A polynomial-size sound summary determining `F(P)` would, by decoding, give a polynomial-time algorithm for `F(P)` on ordered-run posets. That is not a compression theorem; it is an algorithmic one. The existing state-compression results show that natural polynomial-time invariants (linear-extension count, comparability graph, edge/degree profiles) do **not** determine `F` even at small `n`, and no polynomial-time evaluator for `F(P)` is known for this family. Thus the run-decomposition barrier remains a genuine **state-count/enumeration** barrier, but it does not, by itself, imply a superpolynomial class-count lower bound for exact `F`-determination.

### Honest limits

- I did **not** prove that `F(P)` is not polynomial-time computable on ordered-run posets; that would be a much stronger (and currently unavailable) result.
- I did **not** construct a polynomial-time computable summary family; the only exact summary is `F(P)` itself, whose computability is the open problem.
- No repository, Lean, test, or board change was made; this is a paper-level obstruction/clarification only.

## Other metadata

```json
{
  "finished_at": 1795307000.7440898,
  "started_at": 1795306542.6368158
}
```
