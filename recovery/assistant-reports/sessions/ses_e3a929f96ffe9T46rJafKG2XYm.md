# antonina-KXSK51PEEcHYaVfp1oEL7I-accorded

Session: ses_e3a929f96ffe9T46rJafKG2XYm
Workspace: /home/lubko/soring-fronts/near-tight-zero-excess-adversary-memory
Created: 1794313642107; updated: 1794314718531

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 107 (msg_1c57c86e7001mnQaSrmnpcjkd3)

## Scope / recovery (billy-dev)
- Read `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/research-winning-frontier-barrier.md`, `docs/research-certificates-barriers.md`, and inspected current board/ledger state.
- Recovery check: worktree clean at `6a96398` on `billy-dev`; no commits, no repository/Lean edits. Board #301 already contains `conp-adversary-memory` (`2026-11-10T08:33:08.195Z`) with greedy counts `114/112` at `n=4`, `1164/725` at `n=5` and the near-tight `d=0` family left open; ledger front `near-tight-zero-excess-adversary-memory` is the running front for this question. I found no prior post or durable artifact for this specific front and performed **no external side effects** (no board post/commit/PR).

## Front (precise)
For zero-excess `n` with `E(n):=S(n)-C(n)=0`, i.e. `C(n)=⌈log2 n!⌉=S(n)` (known: `n<=11,20,21` per `docs/literature.md`), consider the adversary-win game `G(n,k)` at `k=S(n)-1=C(n)-1`. Let an *explicit winning adversary strategy* be a state-transition object (table/DAG/automaton over reachable game states, e.g. `(P,r)` with poset `P` and remaining budget `r`) that, for every sorter move, outputs a consistent comparison orientation and forces a non-total poset after `k` comparisons. Let `M_adv(n)` be the minimum number of distinct internal states over all such winning strategies (state-merging allowed).

Question: along the zero-excess slice, is `M_adv(n)` superpolynomial in `n`, or polynomially bounded?

## Findings (no new theorem/counterexample)

**1. Sound winning strategy exists on the whole zero-excess slice, but gives no state bound. [deduction, from definitions/information bound]**  
Since `C(n)-1 < log2 n! <= C(n)`, the standard extension-count/halving adversary (maintain the current poset `P`, answer a queried incomparable pair to keep `e(P') >= e(P)/2`, hence `e(P_t) >= n!/2^t > 1` for `t <= C(n)-1`) is *sound*: it wins `G(n,C(n)-1)`. This certifies existence of some explicit strategy when states are taken as reachable `(P,r)` (or any refinement), but it says nothing about minimality or compressibility: the number of reachable posets/behavioral states under this or any other policy is open. This is **soundness** of a strategy/certificate, not completeness/minimality.

**2. The fixed-order (oblivious) adversary is not a winning strategy. [deduction; consistent with #301 08:33Z]**  
If the adversary answers every query according to one fixed total order `π`, then the sorter (knowing the strategy/value of the game, as usual in minimax analysis) can force the path consistent with `π` and identify/sort that fixed order in `S(n)` comparisons of an optimal tree — but more directly, because `π` is fixed, a comparison sequence of length `n-1` following a chain consistent with `π` makes the poset total against that strategy; for relevant `n>=4`, `n-1 < C(n)-1`. Hence any winning adversary must be adaptive/query-dependent, and “state = constant” is impossible; the question is genuinely about adaptive memory.

**3. Primary obstruction to an all-`n`/infinite-family answer: the zero-excess index set is not known infinite. [literature/obstruction]**  
The slice is exactly `{n : S(n)=⌈log2 n!⌉}`. Known values give membership for `n<=11,20,21` and non-membership where checked otherwise (`docs/literature.md`, `docs/problem.md`), but it is open whether this set is infinite, finite, or has any asymptotic density (tied to infinitude of information-tight `S(n)=C(n)`). Therefore the falsifier branch “exhibit an **infinite** zero-excess family with superpolynomial minimal adversary memory” cannot be discharged (positively or negatively) without first settling an open infinitude/exactness question about `S(n)` itself; the complementary branch “polynomial-size explicit optimal adversary for **all such `n`**” is only finitely instantiated by current knowledge.

**4. Finite/empirical status gives no growth discrimination. [experiment, from #301]**  
#301 reports greedy upper bounds (not minima) `114/112` states at `n=4` and `1164/725` at `n=5`, with exact minima open for `n>=4` and larger `n` infeasible without stronger (symmetry-reduced/compiled) minimization. This does not witness superpolynomial growth and does not witness a polynomial minimum (upper bounds are heuristic; lower bounds/minimality unproven). In particular, these counts concern general small `n` game instances there; they do not isolate a proved asymptotic behavior on the zero-excess slice.

**5. Why counting/barrier results do not settle `M_adv(n)`. [deduction; model-fidelity]**  
- Large reachable/winning-frontier or poset counts (A001035, `2^{Θ(n^2)}`) and winning-frontier enumeration barriers exclude *listing* all states, but a *selective* adversary strategy may visit far fewer; a lower bound on `M_adv(n)` would require showing every winning strategy’s reachable/behavioral closure is large (a completeness/exhaustivity claim about strategies), which is stronger than frontier existence.  
- Conversely, a compact *description* of a strategy is not the same as a small explicit state table unless the table itself is small and checkable. A “succinct” rule whose induced reachable-state graph is superpolynomial does not give a polynomial explicit-table certificate.  
- General-poset hardness does not transfer to the fixed antichain root `A_n` without a reduction. Soundness of a proposed table is locally checkable given the table; completeness (that it wins for all sorter plays, and/or is minimal) is the hard global property.

## Concrete failed/incomplete approach
- **Attempt:** use a fixed or obliviously structured adversary (constant/low-memory template independent of adaptive history) to obtain a polynomial-state winning strategy on zero-excess `n`.  
- **Why it fails/inconclusive:** fixed-order strategies lose (point 2). Any winning strategy must maintain enough adaptive uncertainty to survive `C(n)-1` sorter-chosen comparisons; I found no construction proving this can be done with `poly(n)` distinct explicit states for all (or infinitely many) zero-excess `n`, and no argument forcing superpolynomially many. The attempt yields only the sound-but-unbounded halving adversary (point 1).

## Exact obstruction (decisive gap)
A resolution needs one of: (a) a proof that the zero-excess set is infinite together with either a uniform `poly(n)` explicit winning strategy on an infinite subset (upper bound) or a strategy-agnostic superpolynomial lower bound on reachable/behavioral states for every winning adversary on that subset; or (b) for the known finite slice, exact minimization certifying `M_adv(n)` (open per #301 even at `n=4`). The core technical gap is **selective vs exhaustive**: current barriers control existence/counts of states, not the minimum over all winning adversary policies, and no invariant is known that both (i) is preserved by some winning adversary against all sorter moves at budget `C(n)-1` and (ii) has polynomially many classes (nor one proved to require superpolynomial classes).

## Complexity implication (careful)
- A proved superpolynomial lower bound on `M_adv(n)` (minimum over winning strategies) on an infinite zero-excess family would rule out explicit-table/DFA-style adversary certificates of polynomial size on that family (a barrier to that *certificate format*), but by itself is not a separation from P/NP/PSPACE and does not rule out non-tabular succinct proofs.  
- A polynomial-size explicit, efficiently checkable winning-adversary strategy for the relevant no-instances would be a candidate compact coNP-style witness for those instances; on the zero-excess slice `k=C(n)-1` this is trivial as a lower-bound statement (`S(n)>=C(n)`), so complexity significance would require extension beyond this slice or to informative `k`.

**Status:** open/no resolution. No repository, Lean, commit, or board changes made.
