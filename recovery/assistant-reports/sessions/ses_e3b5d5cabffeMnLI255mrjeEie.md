# antonina-5wANF2bJcAnHOnOgTl9RLB-body

Session: ses_e3b5d5cabffeMnLI255mrjeEie
Workspace: /home/lubko/soring-fronts/optimal-play-state-fraction-lower-bound
Created: 1794300355477; updated: 1794300723496

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 100 (msg_1c4a72a4d001aUth002V30aALE)

## Scope and sources (studied)
- **Contract/model**: `AGENTS.md`, `docs/problem.md`. Fixed object: `S(n)` = minimax height of deterministic adaptive comparison sorting of `n` distinct labelled keys; unary threshold `SORT-BOUND-U={1^n#1^k : S(n)<=k}`; `SORT-BOUND-U ∈ PSPACE` (`docs/research-certificates-barriers.md`, Claim A, deduction from `APTIME=PSPACE`). Unary lower bounds `∉P/∉NP` would imply `P!=PSPACE/NP!=PSPACE` (`problem.md`), so unconditional super-polynomial unary lower bounds are out of scope; the frontier is upper bounds/certificates/barriers/structure.
- **Prior local results**: `docs/research-certificates-barriers.md` §8 identifies the *optimal-play state count* as the next experiment; `docs/research-strategy-certificates.md` and `scripts/strategy_dag_probe.py` compute the same object as `DAG(all)` for `n<=6` (all-optimal, hash-consed, both adversary outcomes kept).
- **Board #301 (via digest)**: recent fronts/corrections checked (`certificate-starvation-propagation-alln` 07:04Z, etc.); I do not duplicate them. The prompt’s evidence states “optimal-play reachable states propagate through n=10” and gives the `n=0..7` counts below.

## Precise claim attacked (definition-level restatement)
Let `G(n)` be the comparison game (`docs/problem.md` / `research-certificates-barriers.md`): states are transitively closed labelled partial orders on `[n]`, root = antichain `∅`, `F(P)=0` if total else `F(P)=1+min_{x||y} max(F(P+x<y),F(P+y<x))`, `S(n)=F(∅)`. A sorter move `(x,y)` at `P` is **optimal** iff `1+max(F(P+x<y),F(P+y<x))=F(P)`. Define
`Opt(n) = { P : P` is reachable from `∅` by a path whose every sorter move is optimal`}` (hash-consed states; **both** adversary outcomes of each chosen optimal move included, since the adversary may answer either way in a play following that optimal sorter choice). This is exactly the node set of the all-optimal strategy DAG (`DAG(all)` in `research-strategy-certificates.md` / `strategy_dag_probe.py`), i.e. “states lying on some height-`S(n)` optimal play”.

**Front claim (all-`n`)**: `|Opt(n)| >= c * A001035(n)` for some constant `c>0` and all `n>=4`, hence `|Opt(n)| = 2^{Theta(n^2)}` (Kleitman–Rothschild: `log2 A001035(n)=n^2/4+3n/2+O(log n)`, literature).  
**Falsifier sought**: an infinite family with `|Opt(n)| = o(A001035(n))` (e.g. polynomial, or ratio -> 0).

## Evidence base (experiment/literature, as given or reproduced in-repo)
- `A001035(0..7)=1,1,3,19,219,4231,130023,6129859`.
- Prompt/independent billy-dev computation: `|Opt(0..7)|=1,3,19,181,1551,65551,2769663`, ratios for `n=4..7` = `181/219≈82.6%`, `1551/4231≈36.7%`, `65551/130023≈50.4%`, `2769663/6129859≈45.2%` (matches `DAG(all)` for `n<=6` in `research-strategy-certificates.md`).
- Board evidence cited by prompt: propagation through `n=10` (07:04Z front). I did not independently recompute `n=8..10` here (full minimax over millions of labelled posets is nontrivial in this environment; a direct `n<=7` script I attempted did not finish within the tool timeout, and I avoid duplicating the board’s reported computation).

These finite data do **not** discriminate `Theta(A001035(n))` from `o(A001035(n))` (no monotone decay, but `n<=10` is tiny relative to the `2^{Theta(n^2)}` scale).

## Falsification attempts (serious) and why they fail / remain inconclusive

### 1. Single-policy upper bound — **fails to falsify the union** (deduction)
A *single* optimal sorter policy is a deterministic strategy tree: it has exactly `n!` leaves and `2n!-1` nodes (`research-strategy-certificates.md` Thm 2.1/Obs 2.5, deduction+experiment `n<=6`). Distinct nodes of a reduced comparison tree correspond to distinct labelled posets, so hash-consing gives no saving for one policy and that policy contributes at most `2n!-1 = 2^{Theta(n log n)}` **distinct** states (`log2(2*6!)≈10.49` vs `log2 A001035(6)≈22.5`; asymptotically `n! = o(A001035(n))`).
However, `Opt(n)` is the **union** over all optimal sorter policies (and all their adversary outcomes). A constant-fraction lower bound is not ruled out by the smallness of any one policy; conversely, an `o(A001035(n))` upper bound would require showing the union over *all* optimal choices remains `2^{o(n^2)}`. I found no argument forcing the union to be `2^{o(n^2)}`.

### 2. “Both adversary outcomes” inflation / closure — **argues against easy falsification, not a proof** (deduction)
For every optimal move kept, *both* children `P+x<y`, `P+y<x` are in `Opt(n)` (adversary may select either). Thus `Opt(n)` is not a single path but a union of full-outcome subtrees of optimal sorter choices. At depth 1 the root is symmetric, so every incomparable pair is an optimal first comparison and `Opt(n)` contains **all** `n(n-1)` one-comparison labelled posets. This “adversary-closure” makes exclusion harder: a poset is excluded only if *every* comparison path to it contains some sorter-suboptimal move. But this does not yield a constant-fraction lower bound for large `n`, because paths have length `<=S(n)=O(n log n)` while the space has `2^{Theta(n^2)}` states.

### 3. Structural confinement of optimal play (width/dimension/balance/poset class) — **no confinement found; not a disproof** (failed approach)
I looked for a structural invariant preserved along all optimal moves that would restrict states to a class with `o(A001035(n))` members (e.g. bounded width/height/dimension, series-parallel/interval, or a Kahn–Saks-style extension-balance class). 
- Balance of linear extensions is the right heuristic for *sorting a fixed poset* (Kahn–Saks/Fredman, literature) but optimal minimax height `F` is not determined by `e(P)` alone (see `research-state-compression.md` falsification: different `F` possible in related settings; more directly, Brightwell–Winkler note counting `e(P)` is #P-complete and only suggests a greedy route, not that `F`-optimal play preserves a countable balance invariant). No theorem is known making `F`-optimal moves stay inside any asymptotically sparse labelled-poset family.
- Hardness/structure results over **arbitrary** posets do not transfer to the fixed root/antichain family without a reduction (`AGENTS.md` model fidelity). 
Result: no falsifying family produced.

### 4. Direct exclusion/witness construction — **local exclusions exist, infinite-family amplification not achieved** (deduction + experiment)
`|Opt(n)| < A001035(n)` for `n>=4` in the known data (e.g. `38` excluded at `n=4`), so some labelled posets are unreachable without a sorter-suboptimal step; the “>= constant fraction” claim is not vacuously equivalent to “all posets”. But I did not obtain a characterization of excluded posets stable in `n`, nor a counting argument showing excluded mass becomes `1-o(1)` of `A001035(n)`. Producing an explicit infinite family inside `A001035(n) \ Opt(n)` (or proving its density -> 1) remains open.

## Mathematical finding (honest)
- **Status of the front claim (`|Opt(n)| >= c*A001035(n)` all `n>=4`)**: **OPEN**. I did **not** prove it and I did **not** disprove it.
- **Falsification outcome**: **no infinite family with `|Opt(n)|=o(A001035(n))` found**. The most plausible disproof routes checked here fail to close: a single optimal policy is only `2^{Theta(n log n)} = o(A001035(n))` (deduction) but the adversary-closed union over all optimal policies is empirically a large fraction for `n<=7` and can in principle be as large as `A001035(n)`; I identified no sparse poset class forced by `F`-optimality.
- **Tension/obstruction (exact)**: any all-`n` **positive** theorem must explain how `O(n log n)` comparison steps, even with union over all optimal sorter choices and both adversary outcomes, cover `2^{Theta(n^2)}` labelled posets up to a constant factor; any all-`n` **negative** (falsifying) theorem must exhibit a structural/counting restriction making the optimal-move union `2^{o(n^2)}`. The gap between the per-policy size `2^{Theta(n log n)}` and the full space `2^{Theta(n^2)}` is the core quantitative obstacle, and current methods (small-`n` enumeration, symmetry/quotients as in local notes, general-poset heuristics) do not bridge it in either direction.

## Complexity implication (conditional, per front)
- If true (`|Opt(n)|=2^{Theta(n^2)}`): a strong barrier to state-graph/DAG exact evaluators and to naive succinct witnesses based on enumerating optimal-play states for `SORT-BOUND-U` (deduction, consistent with `research-certificates-barriers.md`/`research-strategy-certificates.md`).
- If false in the strong form `|Opt(n)|=2^{o(n^2)}` (or stronger): it would revive—but not by itself establish—the possibility of a smaller optimal-play state graph; a polynomial or otherwise succinct *checkable* certificate for `SORT-BOUND-U` would still require an explicit representation and a verifier, and is a separate open problem.

## Limits / non-claims
- No new theorem, no counterexample family, no Lean/repository changes; finite data (`n<=10` as reported) are **not** asymptotic evidence. I did not recompute `n=8..10` and I do not claim completeness/correctness of board counts beyond citing them as reported evidence. General-poset results were not transferred to `S(n)`. Distinguishing “certificate/state-graph size” from actual uniform complexity of `SORT-BOUND-U` remains essential (`SORT-BOUND-U ∈ PSPACE` is known; membership in NP/coNP is open).
