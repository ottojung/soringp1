# A large winning frontier survives exact information pruning

**Status:** paper-level theorem with exact integer witness, independently
auditable, not Lean-checked. **Scope:** comparison-sort minimax F(P)
for a known partial order P, and S(n)=F(antichain_n). Asymptotics here
use numeric n, not the binary length of n.

## Theorem

For infinitely many n=2^(2r), let k=ceil(log₂(n!)). At a common
depth t<=k, there are at least

`2^((1/4-o(1)) n (log₂ n)^2)`

pairwise **nonisomorphic** n-element posets P such that:

1. P is reachable from the n-element antichain by exactly t legal
   comparison outcomes.
2. F(P)<=k-t: the sorter can finish within the remaining budget.

These states are genuinely winning, not merely accepted by the
information cutoff. An exact finite witness at n=1024 gives more
than 2^381 such states. The antichain root may nevertheless be losing
at budget k. This is NOT a computational time lower bound for S(n).

## 1. Layered skeleton and independent choices

Let s=2^r and n=s². Create s levels L_i={(i,x):0<=x<s},
for i=0,...,s-1. For each x and consecutive i,i+1 add edges

`(i,x) < (i+1, 2x mod s)` and
`(i,x) < (i+1, (2x+1) mod s)`.

There are t0=2s(s-1) fixed edges. Every edge increases level by
exactly one. Consequently, an edge joining *adjacent* levels
cannot be implied by a different edge or any longer path.
Each edge can be learned by a legal comparison in any order.

Exactly M=(s-1)(s²-2s) other adjacent-level pairs are absent.
Choose an arbitrary subset A of m such pairs and append all its
edges to make P_A. All edges go upward, so the construction is
consistent; all t=t0+m outcomes are legal in any order. Crucially,
the exact comparabilities across any pair of consecutive levels
are *precisely* the selected edges. Thus the `binom(M,m)` choices
produce that many distinct **labelled** reachable posets at depth t.

## 2. Perfect matching gives only s already-sorted chains

The two-edge skeleton has a *perfect matching* across each adjacent
pair of levels. For x<s/2 choose the outgoing edge to 2x; for
x>=s/2 choose the edge to (2x+1) mod s. These s destinations
are exactly the even residues and the odd residues, respectively.
Therefore this is a bijection and uses only installed edges.

Composing the matching across all s-1 interfaces partitions
the n=s² vertices into **s disjoint directed chains of length s**.
Their internal ordering is already known. The arbitrary added
edges A preserve these chains.

A tournament tree merges these s sorted chains using at most
s-1 comparisons to initialize the heads and at most r=log₂s
new comparisons after each of the first n-1 outputs, by
updating along the winner's path. Hence, constructively,

`F(P_A) <= B = (s-1) + (n-1)r`.

The earlier proof unnecessarily used rs chains; that larger
bound made the winning theorem effective only at enormous n.

## 3. Winning budget and count of isomorphism classes

Set k=ceil(log₂(n!)), and choose

`m = k - t0 - B`.

For all sufficiently large r, 0<m<M/2. By definition
t=t0+m=k-B, and therefore *every* constructed P_A satisfies
F(P_A)<=B=k-t. In particular exact linear-extension information
pruning cannot discard these states.

Every unlabelled n-element poset has at most n! labellings.
So there are at least `binom(M,m)/n!` distinct isomorphism classes.

Stirling gives k=n(2r-log₂e)+O(log n), t0=2n-2s,
B=rn+O(s+r), and M=Theta(s³). Therefore

`m=n(r-2-log₂e)+O(s+r+log n)=nr-O(n)`,
and `M/m=Theta(s/r)`. Using
`binom(M,m)>=(M/m)^m` for 1<=m<=M yields

`log₂[binom(M,m)/n!]`
`>=m log₂(M/m)-log₂(n!)`
`=n r²-O(n r log r)`
`=(1/4-o(1)) n (log₂ n)^2`.

This proves the asymptotic assertion.

## 4. Exact witness at n=1024

For r=5, s=32, n=1024, exact integer computations give:

| Symbol | Value |
|---|---:|
| k=ceil(log₂(1024!)) | 8770 |
| t0=2s(s-1) | 1984 |
| B=(s-1)+(n-1)r | 5146 |
| m=k-t0-B | 1640 |
| M=(s-1)(s²-2s) | 29760 |
| t=t0+m | 3624 |

The integer inequality

`binom(29760,1640) > 2^381 * 1024!`

is checked without floating-point approximations by
`tests/test_winning_frontier_barrier.py`. This proves the
finite claim. At r=4, this particular quotient counting
lower bound is <1, so r=5 is the first successful checked
parameter, not a statement that all the n=256 posets
are isomorphic.

## Exactly what is, and is not, ruled out

**Ruled out:** An algorithm claiming uniform time
2^(O(n log n)) that *explicitly lists every reachable
winning poset* at each relevant information-budget level,
even modulo isomorphism: this frontier is too large.

**Not ruled out:** selective DFS, df-pn, symbolic state
families, parametric sorting-certificate DAGs, algebraic
quotients stronger than relabelling, or any algorithm
computing S(n) without listing this frontier.
There is no claim of NP-hardness, PSPACE-hardness,
a P-vs-NP result, or a lower bound on the running
time of arbitrary algorithms for unary SORT-BOUND-U.

Earlier layered-skeleton research and independent reviews
are tracked in [Antonina SoringP1 #301](https://vau.place/a/antonina/?issue=301).
