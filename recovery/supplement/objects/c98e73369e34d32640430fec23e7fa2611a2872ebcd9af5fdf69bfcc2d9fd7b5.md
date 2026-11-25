# Sergeev's sublinear excess bound

**Primary theorem, not Lean-checked here.** Igor S. Sergeev,
*On the asymptotic complexity of sorting*, ECCC TR20-096 (2020),
[original](https://eccc.weizmann.ac.il/report/2020/096/download),
Theorem 3 (page 29):

`S(n) = log₂(n!) + O(n/(log n)^(1/5))`.

This is obtained by a group-insertion *sorting algorithm*. Together
with the information lower bound `L(n)=⌈log₂(n!)⌉`, it implies

`0 ≤ S(n)−L(n) = O(n/(log n)^(1/5)) = o(n)`.

The journal version is Sergeev, *On the Upper Bound of the Complexity
of Sorting* (2021), DOI 10.1134/S0965542521020111.

**Crucial limitations:** This bounds the comparisons made while
sorting, NOT the computation time needed to evaluate exact `S(n)`.
The asymptotic big-O alone does not supply explicit constants or a
finite computable upper-bound function for every input. Extracting
such a bound from the constructive group-insertion proof is a
separate task. Ford–Johnson remains an explicit finite upper bound.

## A structural entropy identity (paper deduction)

Choose a random uniformly distributed input permutation in any
correct deterministic sorting decision tree of worst-case depth `k`.
For each internal node `v`, let `q_v` be its reach probability
and `p_v` the fraction of reachable permutations giving one outcome.
Set `h₂(p)=−p log₂ p−(1−p) log₂(1−p)`; let `D` be the
random depth of the output leaf.

Since the output leaf uniquely identifies the permutation,
entropy chain rule and node-visit counting give

`log₂(n!) = Σ_v q_v h₂(p_v)`, `E[D] = Σ_v q_v`.

Therefore, exactly,

`k−log₂(n!) = E[k−D] + Σ_v q_v(1−h₂(p_v))`.

For fixed `δ∈(0,1/2)`, the **expected** number of comparisons
whose conditional outcome probability has bias at least `δ` is at
most `(k−log₂(n!))/(1−h₂(1/2+δ))`. Moreover, using
binary Pinsker,

`E[Σ_(v visited) (p_v−1/2)²] ≤ (ln 2)/2 · (k−log₂(n!))`.

Sergeev supplies a correct sorting tree with
`k−log₂(n!)=O(n/(log n)^(1/5))`. Hence it makes only
`o(n)` comparisons of fixed conditional bias **in expectation**
on a random input. This is NOT a bound for every adversarial
branch and NOT a hardness or algorithmic classification result.

**Research:** derive a finite effective group-insertion bound; or
find sound worst-case pruning or succinct certificates from this
entropy restriction for unary `SORT-BOUND-U`.
