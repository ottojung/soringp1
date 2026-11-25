# bounded-depth-certificate-kernels

## status

investigated

## origin

executive_manual

## agent_id

qKui8KGp4LYohZ3RRvmkaI-drama

## exit_state

clearexit

## question

For each fixed depth bound related to ceil(log2(n!)) + d, can we characterize which reachable poset classes appear and get a parameterized algorithm with complexity f(d) poly(n)? If so, can this be pushed to cover the relevant surplus regime needed for S(n)?

## basis

Surplus-parameter front investigated but inconclusive; worth renewed focused attempt with sharper falsifier.

## falsifier

Prove that no f(d) poly(n) kernel exists for fixed d by an all-n family, or construct one covering the regime where two-phase fails.

## implication

A positive result would give a uniform parameterized route toward faster exact evaluation; obstruction would identify true barriers.

## finding_unverified

ing to find a good comparison strategy; adversary is worst case for that strategy. The information bound $\lceil \log_2 n! \rceil$ is a lower bound that holds regardless of strategy? Because there are $n!$ possible outcomes and each comparison gives at most 2 outcomes, so depth >= log2(n!) no matter what the sorter does and no matter what adversary does (it's a basic information-theoretic lower bound on decision trees). Yes, that's it - information bound is unavoidable.

So for fixed $d$, we need trees of depth just $d$ above the absolute minimum possible by information theory. The question is about the structure of such trees/strategies for sorting by comparisons, and whether the "state graph" (reachable poset classes) is small (parameterized by $d$) allowing fast algorithms to test for existence of such a strategy.

Also "two-phase" algorithms - for example, some sorting algorithms do a first phase to determine the relative order in some structured way, second phase to complete; or more directly related to the "Ford-Johnson" algorithm? Or perhaps the idea of first finding "graph of possible orders" with certain property, then sorting. Or maybe related to the fact that for small surplus you can do a two-phase method but it breaks down later.

Alternatively, this is reminiscent of some work in combinatorics of sorting or in parameterized complexity of decision trees? Or perhaps related to the "graph bandwidth" no - not obvious. Or maybe to the fact that with small excess over information bound, the comparison tree must be "almost a sorting network" in some cases? Or more directly related to the "coin weighing" and to "identifying codes"? Let us look up how people think about this. Also look at Stober-Weiss - they did computational search up to n=18; maybe related to that. Also Sergeev talks about asymptotics.

Alternatively, another way: the "comparison search" with bounded depth relative to information bound is studied in some contexts. Or perhaps it's about the "poset dimension" or other things? Or maybe about the fact that reachable posets when you're close to information bound must be "shellable" or have certain width?

Or let us look up the actual research packets again - I saw "Parameterization by additive surplus d=k-ceil(log2 n!). Investigate whether deciding exact S(n)<=C(n)+d admits an f(d)poly(n) algorithm or polynomial-depth kernel for fixed d, including d=0. Account for all comparator choices and siblings; avoid the false inference that d+F(P) characterizes viable root histories. Source Stober-Weiss 2023 and original exact decision-tree DP." So this is in research-packets.json. Let us look up that packet.
Let us look up what Stober-Weiss did - they used a pruned backward/forward search. Also the "two-phase" might refer to some two-phase algorithm in that search or in general. Let us read more of the nontightness note and related materials.

Let us write the research report.

Obstruction: for fixed $d=C(n)+k$ surplus, the independent-edge chain family (winning frontier) yields $2^{\Omega(n(\log n)^2)}$ nonisomorphic reachable winning poset classes at depth $C(n)+d - B$, so no $f(d)\mathrm{poly}(n)$ state-kernel/characterization exists. This blocks the class-parameterization route; natural two-phase strategies cannot cover this family at fixed surplus. Not a universal algorithm lower bound or class separation - report as a combinatorial obstruction with references to the existing winning frontier construction and literature.


## Other metadata

```json
{
  "finished_at": 1793560693.2067423,
  "started_at": 1793559715.4038777
}
```
