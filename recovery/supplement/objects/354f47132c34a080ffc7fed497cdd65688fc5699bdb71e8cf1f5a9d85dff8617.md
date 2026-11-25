# A large winning frontier survives exact information pruning

**Status:** paper-level theorem and exact integer witnesses, independently
auditable, not Lean-checked. **Model:** adaptive comparison sorting of
distinct keys, where F(P) is the minimax remaining comparison count
after learning partial order P. All asymptotics are in numeric n,
not the length of its binary encoding.

## Statement

For infinitely many n=2^(2r), with k=ceil(log₂(n!)), there exists a
common comparison depth t<=k with at least

`2^((1/4-o(1)) n (log₂ n)^2)`

pairwise **nonisomorphic** n-vertex partial orders P satisfying:

1. P is reachable from the n-antichain by exactly t legal
   comparison outcomes.
2. F(P)<=k-t: a correct sorting procedure finishes within the
   remaining comparison budget.

These states are genuinely *winning*, not merely allowed by
the linear-extension cutoff. A finite instance with **n=224**
already exhibits more than **2^39** different nonisomorphic
winning states at the same depth.

This is NOT a time lower bound for computing S(n).
A selective or symbolic algorithm need not enumerate every state;
the root antichain may itself be losing at budget k.

The same construction applies at the **exact optimal budget** `k=S(n)`.
Sergeev's `S(n)=log₂(n!)+o(n)` bound implies `S(n)=C(n)+d(n)` for an
integer `d(n)≥0` with `d(n)=o(n)`. The parameter calculation below is
unchanged for every such sublinear nonnegative surplus. Thus the large
frontier is not confined to the information budget, where the root can be
losing: at the exact optimum these states are reachable, winning, and have
the corresponding remaining budget `S(n)-t`.

## 1. The much simpler independent-edge construction

Choose integers s>=2 (number of columns) and L>=2 (number
of levels), and let n=sL. Identify vertices as

`(i,x), 0<=i<L, 0<=x<s`.

For each fixed x, place the L−1 known comparisons

`(0,x)<(1,x)<...<(L−1,x)`.

These t0=s(L−1) edges form exactly s disjoint, already-sorted
chains, each of length L. There is no need for an elaborate
high-expansion or de Bruijn skeleton.

Between each adjacent pair of levels choose any *additional*
forward pair (i,x)<(i+1,y) with x != y. There are

`M=(L−1)(s²−s)`

possible extra pairs. Choose any set A of m such pairs.

Every installed edge, initial or extra, can be learned in
arbitrary order as a legal comparison outcome: all edges
increase the level by exactly one, so a different multi-edge
path can never imply an adjacent-level relation. Edges are
consistent because all point forward. Furthermore, the
relation across adjacent levels is exactly the set of
installed edges. Thus the `binom(M,m)` choices give that
many DISTINCT LABELLED partial orders P_A, each reachable
in exactly

`t=t0+m`

comparison outcomes.

## 2. All the constructed states are winning

The s disjoint initial chains remain valid in every P_A.
A standard balanced winner tournament merges their sorted
heads with at most s−1 initial comparisons and at most
h=ceil(log₂s) comparisons to update a chain head after
each of the first n−1 outputs. Therefore

`F(P_A)<=B=(s−1)+(n−1)ceil(log₂s)`.

Now let k=ceil(log₂(n!)) and choose

`m = k−t0−B`.

Provided 0<m<=M, all constructed states are reachable at
t=t0+m=k−B and satisfy

`F(P_A)<=B=k−t`.

They survive exact information pruning, because a winning
comparison tree of height k−t has at most 2^(k−t) reachable
total-order leaves. The construction supplies much more
than information-theoretically possible states by enumeration,
not a counterexample to the information bound for sorting.

Each isomorphism class has at most n! different labellings.
Hence the count of nonisomorphic, reachable, winning P_A is at
least

`binom(M,m)/n!`.

## 3. Asymptotic lower bound

Take s=L=2^r (so n=s² and h=r).
Stirling's estimate gives

`k=n(2r−log₂e)+O(log n)`,
`t0=n−s`, `B=rn+O(s+r)`,

and therefore

`m=n(r−1−log₂e)+O(s+r+log n) = nr−O(n)`.

Also M=(s−1)s(s−1)=Theta(s³) and M/m=Theta(s/r),
so for all sufficiently large r we have 0<m<M/2.
The elementary estimate `binom(M,m)>=(M/m)^m` yields

`log₂[binom(M,m)/n!]`
`>=m log₂(M/m)−log₂(n!)`
`=n r²−O(n r log r)`
`=(1/4−o(1)) n (log₂ n)²`.

This proves the theorem. It strengthens the earlier
unpublished two-edge, rs-chain construction in two ways:
the chain count is s rather than rs, and *one known edge*
per column and level interface suffices, freeing a larger
number of budgeted independent extra comparisons.

### 3.1 Extension to sublinear budget surplus, including `S(n)`

Let `k=C(n)+d(n)` where `d(n)` is a nonnegative integer and
`d(n)=o(n)`, and continue to take `s=L=2^r` and `n=s^2`. Keep
`t0=s(L-1)`, `B=(s-1)+(n-1)r`, and `M=(L-1)(s^2-s)`, but set
`m=k-t0-B`. Stirling's estimate gives

`m=nr-n log₂(e)-n+d(n)+O(s+r+log n)=nr-O(n)+o(n)=Θ(n log n)`.

Consequently `0<m<M/2` for all sufficiently large r, since
`M=Θ(n^(3/2))`. The same independent-edge family has
`binom(M,m)` different labelled posets, each reachable at
`t=t0+m=k-B` legal comparisons and sortable in at most
`B=k-t` further comparisons. Distinct labelled posets differ on
an adjacent-level relation, and each isomorphism class has at most
`n!` labelings. Therefore

`log₂[binom(M,m)/n!] ≥ m log₂(M/m)-log₂(n!)`
`= (1/4-o(1)) n (log₂ n)^2`.

The `d(n)=o(n)` increment changes only lower-order terms: here
`log₂(M/m)=Θ(log n)`, so it contributes `o(n log n)`, below the
leading `n(log n)^2` term. This specializes to `k=S(n)` because
`C(n)≤S(n)` and Sergeev, *On the asymptotic complexity of sorting*,
ECCC TR20-096 (2020), Theorem 3, gives
`S(n)=log₂(n!)+O(n/(log n)^(1/5))`; hence `S(n)-C(n)=o(n)`.
This use of Sergeev is asymptotic and supplies no effective finite
threshold. The conclusion remains an enumeration barrier only, not a
general running-time lower bound.

## 4. Exact finite witness with only 224 elements

Take s=16 columns and L=14 levels. Then n=224 and
h=ceil(log₂16)=4. Exact integer arithmetic gives:

| Quantity | Exact value |
|---|---:|
| k=ceil(log₂(224!)) | 1431 |
| t0=s(L−1) | 208 |
| B=(s−1)+(n−1)h | 907 |
| m=k−t0−B | 316 |
| M=(L−1)(s²−s) | 3120 |
| t=t0+m | 524 |

The exact integer inequality

`binom(3120,316)>2^39 * 224!`

is certified by `tests/test_winning_frontier_barrier.py`,
so **more than 2^39** pairwise nonisomorphic reachable
states are each sortable within their remaining **907**
comparisons.

A symmetric check with s=L=16 (n=256) is even stronger
in count: k=1684, t0=240, B=1035, m=409, M=3600, and

`binom(3600,409)>2^148 * 256!`.

We have not proved that 224 is the smallest n for which
*any possible* winning-frontier construction works.
It is a readily checked witness from this simple
rectangular-chain family.

## What this theorem excludes (and does not)

**Excluded:** any purported uniform 2^(O(n log n))
algorithm whose method necessarily outputs **all**
reachable winning partial orders at the information
budget, even when identified up to isomorphism.
Such an enumerated frontier has
2^(Omega(n (log n)²)) separate states.

**Not excluded:** selective minimax search, proof-number
search, stronger state compression, parametric DAG
sorting certificates, algebraic recurrences, or any
method evaluating S(n) without listing the full
frontier. The theorem does not establish a space
lower bound for arbitrary solvers, NP/PSPACE hardness,
or any classification of unary SORT-BOUND-U.

Original and subsequent independent math audits are
tracked on [Antonina SoringP1 #301](https://vau.place/a/antonina/?issue=301).
