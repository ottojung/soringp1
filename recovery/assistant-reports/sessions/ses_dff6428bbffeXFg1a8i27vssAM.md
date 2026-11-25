# antonina-KCeOqYisevZ75Zh6Wa6WNd-pigment

Session: ses_dff6428bbffeXFg1a8i27vssAM
Workspace: /home/lubko/soring-fronts/run-decomposition-selective-summary-size-alln
Created: 1795306542995; updated: 1795306989148

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 258 (msg_200a240bb001Kho0Ln2GwmQT7q)

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
