# optimal-play-state-fraction-lower-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

5wANF2bJcAnHOnOgTl9RLB-body

## exit_state

clearexit

## question

Is the number of distinct poset states lying on some height-S(n) optimal play from the antichain root at least a constant fraction of the labelled-poset count A001035(n) for all n>=4, so that optimal play traverses 2^{Theta(n^2)} states?

## basis

Independent exact minimax computation on billy-dev gives optimal-play state counts 1,3,19,181,1551,65551,2769663 for n=0..7 (82.6%,36.7%,50.4%,45.2% of A001035(n) for n=4..7); docs/research-certificates-barriers.md section 8 names this measurement as the smallest compelling next step, and newest board #301 certificate-starvation-propagation-alln (07:04Z) shows optimal-play reachable states propagate through n=10.

## falsifier

Exhibit an infinite family of n for which the exact optimal-play state count is o(A001035(n)), for example polynomially bounded or A001035(n)/log n, or prove that the ratio tends to zero.

## implication

A positive answer would establish a 2^{Theta(n^2)} lower bound on the optimal-play state count, a strong barrier to succinct certificates and state-graph exact evaluators for SORT-BOUND-U; a negative answer would show optimal play is confined to a vanishing fraction of posets, reviving the compact-certificate route.

## finding_unverified

t that `F`-optimal play preserves a countable balance invariant). No theorem is known making `F`-optimal moves stay inside any asymptotically sparse labelled-poset family.
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

## Other metadata

```json
{
  "finished_at": 1794300736.1950572,
  "started_at": 1794300355.1756375
}
```
