# antonina-3VwjCjSKrrvcCIyUs8Dqan-rally

Session: ses_e522b1314ffem2zM2nBr34GT3b
Workspace: /home/lubko/soring-fronts/fo-tc-combined-review-20261105
Created: 1793917775156; updated: 1793917818261

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 53 (msg_1add532d90014peiPw72Aw6Nl4)

## Verdict

**The parameterized question is well-posed and appears unresolved in the primary literature I checked, but it is not presently a fresh, tractable SoringP1 result.** It is a distinct generalized-poset problem—not a new algorithm for the root value \(S(n)\)—and no known result I found establishes FPT or parameterized hardness for the exact comparison-poset minimax predicate.

This is a **literature boundary**, not a proof that no such result exists.

## Precise problem

Fix an explicit \(n\times n\) comparability-matrix encoding of a labelled poset \(P\). Let \(F(P)\) be the minimum worst-case number of adaptive pairwise comparisons needed to identify its unknown linear extension. The parameterized decision problem is

\[
\textsc{CanSort}(P,k):\quad F(P)\le k,
\]

parameterized by \(k\). The matrix encoding matters: its input length is \(\Theta(n^2+\log k)\). A sparse encoding with binary \(n\) and no explicit vertex list is a different problem.

The exact recurrence is
\[
F(P)=
\begin{cases}
0 & \text{if \(P\) has one linear extension},\\
1+\min_{\{x,y\}\text{ incomparable}}
\max\{F(P_{x<y}),F(P_{y<x})\}&\text{otherwise}.
\end{cases}
\]
A depth-\(k\) evaluation by this recurrence has up to \(n^2\) comparison choices per level: \(n^{O(k)}\), not \(f(k)\operatorname{poly}(n)\). Representing uncertainty as a set of permutations instead introduces up to \(n!\) objects; that also does not establish FPT.

## Literature boundary

- **Cardinal, Fiorini, Joret, Jungers and Munro**, *Sorting under Partial Information (without the Ellipsoid Algorithm)*, Combinatorica 33(6), 2013, [arXiv:0911.0086](https://arxiv.org/abs/0911.0086). This is the closest primary source: it studies comparison-based sorting of an explicitly given poset and gives polynomial-time strategies with comparison counts within constant factors of \(\log e(P)\). It does **not** compute the exact optimum \(F(P)\), decide \(F(P)\le k\), or give a parameterized bound.
- **Hyafil and Rivest**, *Constructing Optimal Binary Decision Trees Is NP-complete*, IPL 5(1), 1976, DOI [10.1016/0020-0190(76)90095-8](https://doi.org/10.1016/0020-0190(76)90095-8), is not a reduction for this problem: its tests are arbitrary subsets, not pairwise comparisons constrained by poset semantics.
- The project’s existing audit, [`docs/research-hardness-boundaries.md`](docs/research-hardness-boundaries.md), likewise finds no primary-source classification for exact pairwise comparison sorting on a poset. That is not an exhaustive parameterized-complexity survey, so the defensible statement is that I found **no applicable theorem**, not that the literature definitively has none.

I found no FPT theorem, W[1]-hardness theorem, or PSPACE-hardness reduction for this exact model. Any hardness result would need to encode the source instance into comparison outcomes of a poset while preserving the minimax semantics; generic decision-tree or game-solving hardness is insufficient.

## Does FPT help compute \(S(n)\)?

Only conditionally, and not automatically. For the root antichain \(A_n\), \(F(A_n)=S(n)\). If an FPT algorithm runs in \(f(k)\operatorname{poly}(n)\), applying it at the relevant threshold \(k=\Theta(n\log n)\) yields
\[
f(\Theta(n\log n))\operatorname{poly}(n),
\]
which need not improve the known \(2^{O(n\log^2 n)}\)-time root evaluator. For example, \(f(k)=2^{O(k)}\) gives \(2^{O(n\log n)}\operatorname{poly}(n)\), a genuine improvement; \(f(k)=2^{O(k\log k)}\) gives \(2^{O(n\log^2 n)}\operatorname{poly}(n)\), no asymptotic improvement; and an arbitrary computable \(f\) gives no useful root bound. An FPT result with a suitably small, explicit \(f\) could matter, but FPT alone is not enough.

**Recommendation:** do not pursue this as a root-\(S(n)\) research question without a concrete candidate parameterized algorithm or semantics-preserving reduction. As a separate generalized-poset parameterized question it is meaningful, but currently the search strategy named in the prompt does not itself supply a result or bridge to the project’s unary root objective.

## Output 72 (msg_1add59039001b24UfyxXv9Pte2)

No side effects from my prior turn: no files were written, no commits made, no external posts. The only untracked file (`docs/research-fo-tc-combined-audit-20261105.md`) is pre-existing and unrelated to my response. The answer (literature boundary + paper proof, no code/edits) is already delivered above; no further work remains.
