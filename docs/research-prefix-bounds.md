# Bounds for disjoint-pair prefix states

**Status:** elementary bounds; no resolution of the all-`n` identity.
The prior draft at commit `59bdbfc` (`research-prefix-equivalence.md`)
incorrectly claimed an
equivalence with Ford–Johnson optimality and an `n=47` refutation. Those
claims were invalid and are withdrawn. In particular, equality at `t=0` is
tautological and does not imply Ford–Johnson optimality.

Model: adaptive comparison sorting of `n` distinct labelled keys. Let `S(n)`
be the optimal worst-case number of comparisons and `F(P)` the minimax depth
from a poset `P` of known comparisons.

Write `A_m` for the `m`-element antichain and
`P_{n,t}=tC_2 ⊔ A_{n-2t}` for `0≤t≤floor(n/2)`, where `tC_2` is a matching of
`t` known two-element chains. Let

    M(n) = sum_{j=1..n} ceil(log_2(3j/4))

be the worst-case comparison count of Ford–Johnson / merge-insertion.

## Valid bounds

For all `n,t`,

    S(n) - t <= F(P_{n,t}) <= M(n) - t.

**Lower bound.** Prepend the `t` known pair comparisons to an optimal strategy
for `P_{n,t}`. This gives a sorter on the antichain in `t+F(P_{n,t})`
comparisons, so `S(n) <= t+F(P_{n,t})`.

**Upper bound.** Merge-insertion starts with a fixed matching of
`floor(n/2)` pair comparisons independent of their outcomes (Knuth, TAOCP 3,
§5.3.1). Relabel so the specified `t` pairs are among those initial queries.
On a compatible input, simulate merge-insertion while treating those `t`
already-known answers as free. Its total is at most `M(n)` and includes those
`t` queries, so the charged comparisons are at most `M(n)-t` on each input.

The bounds imply: when `S(n)=M(n)`, the desired identity
`F(P_{n,t})=S(n)-t` holds for every `t`. The converse does **not** follow.
For `t=0`, `P_{n,0}=A_n` and `F(P_{n,0})=S(n)` by definition, regardless of
whether `S(n)=M(n)`. For positive `t`, the interval can have slack when
`S(n)<M(n)`; neither bound determines whether `F(P_{n,t})` equals its lower
endpoint. Likewise, the fact that merge-insertion is nonoptimal at `n=47`
shows only that the upper bound is not tight there; it does not refute the
prefix identity.

Thus the finite identity through `n≤22` follows from known
`S(n)=M(n)` in that range. For `n≥23`, this bound argument alone leaves the
prefix question open. The `n=47` nonoptimality result is not a counterexample
to the prefix identity. No all-`n` result is claimed here.

## Computational check

`scripts/prefix_equivalence_check.py` computes `F(P_{n,t})` by transcript DFS
for small inputs. A completed run checked `2≤n≤5` and all `t`, with no
failures; a run toward `n=8` was terminated at the expensive `n=6,t=0`
antichain computation. This is corroboration only; the inequalities above
are the general proof.

## References

- D. E. Knuth, *The Art of Computer Programming*, vol. 3, §5.3.1 (merge-
  insertion algorithm and comparison bound).
- F. Stober and A. Weiß, “Lower Bounds for Sorting 16, 17, and 18 Elements,”
  ALENEX 2023, arXiv:2206.05597 (known optimal values through `n=22`, and
  discussion of Ford–Johnson's nonoptimality at `n=47`).
