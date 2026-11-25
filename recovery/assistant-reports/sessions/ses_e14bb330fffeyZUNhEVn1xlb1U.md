# antonina-b2eYL2icDOZAJVwp9Ui6Mf-distrust

Session: ses_e14bb330fffeyZUNhEVn1xlb1U
Workspace: /home/lubko/soring-fronts/uniform-polytime-e-oracle-s-reduction-bridge
Created: 1794948517163; updated: 1794948662942

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 87 (msg_1eb45c51a001zGTFHvH4gXZmi8)

## Scope and sources (studied)

- **Contract/model:** `AGENTS.md`, `docs/problem.md` (unary target `SORT-BOUND-U = {1^n#1^k : S(n) ≤ k}`, `S_unary(1^n)`; adaptive comparison-tree minimax `S(n)=F(A_n)` with `F(P)=0` if total else `1+min_{x∥y} max(F(P|x<y),F(P|y<x))`, `S_eq_adv_univ`; inputs n distinct labelled keys; `N=n+k+1`; known `SORT-BOUND-U ∈ PSPACE/EXPTIME`-time bounds discussed in docs; no unconditional super-polynomial uniform lower bound for unary in scope). `docs/literature.md` (exact values/barriers, model caveats). `docs/operations.md` (board #301 context).
- **Board #301 (via `/home/lubko/soring301/scripts/board_digest.py --recent 7` and `--contains "linear-extension oracle necessity"`):** prior 2026-11-17T03:23:08Z post “SoringP1 frontier: linear-extension oracle necessity” reports exhaustive cheap-invariant collision tests over all labelled posets n=3..6 (130,023 at n=6) with *no theorem*; motivates a sharper all-n uniform e-oracle-reduction question. No posted theorem/counterexample for the present front was found in the sampled digest.
- **Repo evidence consulted:** `docs/research-state-compression.md` (reachable states = all labelled posets, `F` invariant under relabelling; **(a)** linear-extension count `e(P)` does **not** preserve `F`: explicit n=5 witness with `e(P)=e(Q)=8` but `F(P)=3, F(Q)=4`; balanced-greedy/leaf-count surrogates not complete), `docs/research-hardness-boundaries.md` (general-poset `GEN-SORT` model/encoding care; Hyafil–Rivest 1976 is arbitrary-subset tests, not pairwise comparisons; Cardinal et al. 2013 give constant-factor/`O(log e(P))` comparison strategies, not exact `S(P)`/threshold decision; unary sparsity/Mahaney barriers apply to `SORT-BOUND-U`, not to dense `GEN-SORT`).

Labels below: **[definition/model]**, **[literature]**, **[deduction]**, **[experiment/indexed repo evidence]**, **[obstruction/limit]**, **[open]**.

## Front (restated, all n)

**Claim C (to test/refute):** There is a uniform algorithm which, on input `1^n`, computes `S(n)` for all `n>=1` by making only `poly(n)` calls to an oracle returning `e(P)=` the number of linear extensions of a poset `P`, where every queried `P` is generated adaptively from the antichain `A_n`, each queried `P` is describable in `poly(n)` bits, and all non-oracle work is `poly(n)`.

**Target falsifier:** an infinite family of `n` and a theorem showing every correct uniform method of this form needs, for all constants `c`, `ω(n^c)` e-queries on infinitely many `n`, or `ω(n^c)`-bit descriptions, or `ω(n^c)` external work tied to the reduction.

## Precise model audit (necessary before any transfer)

- **[definition/model]** `e(P)` is the exact linear-extension count of the queried poset. States reachable by adaptive comparisons from `A_n` are exactly partial orders on the same `n` labelled keys (every labelled poset is reachable by adding consistent relations; cf. `research-state-compression.md` Finding 1 **[deduction+experiment]**). Hence any such `P` has an explicit representation (e.g. `n×n` relation/comparability matrix or Hasse/transitive closure) of size `O(n^2)` bits: **the “superpolynomial description complexity” branch is not a viable falsifier for n-element states** (it would require querying objects not encodable over the fixed n keys, contrary to “generated adaptively from the antichain”).
- **[deduction]** Therefore a refutation must come from **query complexity** (number of e-calls) and/or **external computation**, not per-query bit-length of n-element posets.
- **[literature/model]** Brightwell–Winkler (1991, counting linear extensions is #P-complete for general posets; standard, see `docs/literature.md`/boundaries context) implies an e-oracle on general poset instances is polynomially equivalent in power to a #P oracle under polynomial-time Turing reductions. **But** this is a *general-poset* hardness fact about the oracle function, not a lower bound on using e to compute the *specific* antichain value `S(n)=F(A_n)`; it cannot by itself refute C and must not be conflated with hardness of `SORT-BOUND-U`. Likewise **[literature, boundaries]** Cardinal et al. 2013 give polynomial-time constant-factor/`O(log e(P))` comparison strategies under partial information, not exact `S(P)` nor an exact e-oracle decision procedure for `S(n)≤k` (sound/efficient approximation ≠ completeness for the exact minimax threshold).
- **[definition/model]** `S(n)` is a minimax *height* (adversarial/worst-case) over comparison choices, not determined by `e(A_n)=n!` alone except via bounds `⌈log2 n!⌉ ≤ S(n)`; exact evaluation requires certifying the best comparison tree height, not merely an extension count of the root.

## Serious attempt to DISPROVE C

### 1) Insufficiency of pointwise `e` (sound negative evidence, not a refutation)
- **[experiment/indexed repo evidence, deduction]** `e(P)` alone does not determine `F(P)`: there exist posets with identical `e` but different remaining minimax cost (n=5 witness, `e=8`, `F=3` vs `4`, `research-state-compression.md` (a)). Also greedy balancing by `e`/leaf count fails to be exact-optimal in general (fails at n=9 for the balanced-greedy class there). **Consequence:** any correct e-oracle method for *exact* `S(n)` cannot be a nonadaptive function of `e(A_n)` nor a local `e`-only surrogate; it must exploit *adaptive* queries and/or global structure. **Limit:** this does **not** refute C, because C allows adaptive queries of `e` on *any* generated posets (children/grandchildren etc.), and adaptive access to a rich #P-equivalent oracle may, in principle, convey far more than isolated counts.

### 2) Information/game-tree pressure (heuristic, no theorem)
- **[deduction/obstruction, heuristic]** Naive minimax evaluation of `F(A_n)` depends on the full comparison game; the reachable/state structure is exponential-scale in relevant parameters (`A001035(n)=2^{Θ(n^2)}` labelled posets total for n elements; optimal strategies relate to large trees/certificates in general), and `F` is sensitive to structure not captured by `e` pointwise. This motivates suspecting superpolynomially many *relevant* states/queries may be unavoidable for infinitely many n. **Limit:** this is not a lower bound. With poly(n) non-oracle work per query, an algorithm could in principle (a) query only a polynomially-small, cleverly chosen adaptive set, or (b) extract a succinct minimax witness via algebraic/global properties of `e(·)` over queried posets. No counting/adversary argument found that forces `ω(n^c)` e-queries for all correct uniform methods.

### 3) Reduction/complexity consequences (bars to an easy “yes”, not a disproof)
- **[deduction]** A uniform poly(n)-query, poly(n)-work e-oracle algorithm on input `1^n` would place `S_unary` in `FP` relative to the e-oracle; since `e` is #P-complete for general posets **[literature]**, this is morally an `FP^{#P}`-style upper-bound route (a concrete strong consequence for `SORT-BOUND-U`, consistent with Toda’s theorem context `PH ⊆ P^{#P}` but only as an inclusion landscape, not used as a premise here). **[obstruction/limit]** Conversely, *proving* C false in the strong asymptotic form (superpolynomial e-queries/work for infinitely many n, for all correct uniform reductions) would separate this exact antichain-evaluation task from efficient `P^{#P}/e`-oracle computation in that query/work sense—a separation far beyond current techniques and in tension with the “no unconditional super-polynomial uniform lower bound for unary is in scope” reality of `docs/problem.md` (and would likely subsume major open questions depending on the precise relativized claim). I found no unconditional route to such a separation.

### 4) Exhaustive/small-n search for a concrete uniform failure
- **[open/limit]** No concrete `n` or infinite family was identified for which *all* correct uniform adaptive e-oracle reductions provably fail the polynomial bounds. Small-n collision/non-determination evidence (above) rules out naive surrogates but not all adaptive strategies; prior board collision tests reported no theorem. A genuine falsifier here would require an all-correct-methods argument, not a single algorithm’s failure.

## Finding (mathematical, honest)

- **No disproof, no counterexample, and no new theorem found** for front C. The claim remains **[open]**.
- **Established negatives relevant to C (not sufficient to refute it):** (i) `e(P)` is not a complete invariant for `F(P)` pointwise, so e-only local/surrogate completeness fails **[experiment/indexed+d eduction]**; (ii) per-queried description complexity is automatically `poly(n)` for antichain-generated n-element posets, eliminating one stated falsifier branch **[deduction]**; (iii) general-poset approximation/hardness results (Cardinal et al. exactness gap; Hyafil–Rivest wrong test model; #LE general hardness) do not transfer to an all-n antichain e-oracle reduction without a new argument **[literature/model]**.
- **Exact obstruction:** refuting C requires, for infinitely many `n`, a uniform lower bound against *every* correct adaptive e-query method (superpolynomial queries or external work). Given `e`’s #P-completeness as an oracle primitive and the absence of any known technique for unconditional super-polynomial uniform lower bounds on this unary/PSPACE-landscape evaluation task, producing such a theorem appears out of reach of current methods; I do not claim it impossible, only that no independently checkable argument (paper-level or computationally decisive for all methods) was obtained. A **positive** resolution would be a substantive `FP^{e}`/oracle-route upper bound for exact `S_unary` and would require exhibiting/verifying a correct poly-query adaptive reduction (soundness and completeness for the minimax value), which was also not found.

## Concrete failed approaches / non-starters (to avoid repetition)

- Treating a single-poset `e(P)` collision or a failing heuristic (e.g. balanced-by-e, cheap invariants) as a refutation of all adaptive e-oracle reductions (confuses surrogate incompleteness with oracle lower bounds).
- Inferring a bound on C from Hyafil–Rivest (arbitrary subset tests) or from constant-factor approximation under partial information (Cardinal et al.) as if they decided exact `S(n)` (model/certificate-completeness mismatch).
- Using Brightwell–Winkler #P-completeness of `e` as a hardness proof for `SORT-BOUND-U` or as a query lower bound for computing `F(A_n)` (wrong direction/target).
- Targeting “superpolynomial description of queried `P`” for n-key states (vacuous under the stated generation model).
- Small-n exhaustive enumeration alone as an all-n/infinite-family falsifier without a theorem covering all correct uniform methods.

## Complexity implication (as stated, conditional)

- **If C were proved (yes):** a concrete `e`-oracle (hence #P-oracle-strength, by general #LE completeness) route toward polynomial-time exact evaluation of `S_unary` / strong uniform upper bounds for `SORT-BOUND-U` (subject to the exact oracle model). 
- **If a rigorous no/barrier of the stated strength were proved:** exact `S(n)` would be separated from efficient adaptive `e(P)`-oracle search/reduction in that form, sharpening limits of extension-count-driven methods beyond collision/no-theorem evidence. No such barrier is established here.
