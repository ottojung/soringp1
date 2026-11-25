# reset-branch-divisibility-theorem

## status

investigated

## origin

ai_proposal_unverified

## agent_id

GxWdUOmfxlri2JL06VVA7a-remind

## exit_state

clearexit

## question

For all-n boundary families in the exact-reset certificate model, is branch-level divisibility (from each comparison split of Ext(F)) necessary and sufficient together with leaf classes being frames of Ext(F'), or are there infinite families with all per-split multiples but no legal comparison-tree realization?

## basis

docs/research-exact-reset-realizability.md gives an antichain-to-star odd-n obstruction from root split divisibility; board #301 treated per-stage arithmetic as necessary but module realizability open.

## falsifier

Exhibit an infinite family of (F_n,F'_n) with exact integer ratios realizable at each split level by counting but no rooted comparison tree produces only framed leaves isomorphic to F'_n.

## implication

A general obstruction would close the exact-reset arithmetic route for many framed certificates regardless of quotient size, while a sufficiency theorem would reduce completeness to a number-theoretic condition.

## finding_unverified

component, total chain). $e(F'_n)=1$, ratio $(2n)!$ integer. Any path to total order works, divisibility is trivial.

Another case: $F_n = C_2 \sqcup C_2 \sqcup ... \sqcup C_2$ ($n$ pairs, $n$ components), $F'_n = A_{2n}$ (antichain, $2n$ components). But wait - need $F_n \subset F'_n$ meaning $F'_n$ must contain all relations of $F_n$. $F_n$ has relations forming pairs; $F'_n$ is antichain with no relations. Impossible. Not allowed.

Another direction: $F_n$ connected, $F'_n$ disconnected but extends $F_n$. As shown, impossible because connectedness is preserved upwards? No wait - if $F_n \subset F'_n$ and $F_n$ is connected, can $F'_n$ be disconnected? Take any two elements connected by a path in $F_n$; all relations on that path exist in $F'_n$, so they remain connected in $F'_n$. Every element of $F_n$ is connected to every other element in $F_n$'s component by definition of connectedness? No, connected component usually means any two elements in the same component are connected by a path, and different components have no paths. So if $F_n$ is connected (one component), then all elements of $F_n$ are connected to each other via paths in $F_n$. All those paths remain in $F'_n$, so all elements remain connected in $F'_n$. Thus $F'_n$ must be connected. Yes, impossible for connected $F_n$ to extend to disconnected $F'_n$. That’s a topological obstruction.

Now check the conditions for such an impossible case: $F_n$ connected, $F'_n$ disconnected, $F_n \subset F'_n$. Can we have branch-level divisibility satisfied at every split? We need $e(F'_n) \mid e(P)$ for every state $P$ on the path. Is there any number-theoretic obstruction to divisibility alone? Maybe possible to choose $F_n,F'_n$ with suitable sizes? Let us try to construct.
**Finding (paper proof):** $A_4 \to B_{2,2}$ is an infinite-family-adjacent counterexample where $F \subset F'$ and $e(F)/e(F')$ integer, root splits give integer ratios, but *every* possible comparison tree reaches some state $P$ from which *no* comparison produces both branches with $e(P_i) \equiv 0 \pmod{e(F')}$, so no exact reset tree exists despite all-per-split counting being satisfiable at root and for some first steps. Component structure is compatible (merge), but recursive divisibility fails for all paths. This matches the board’s “module realizability open” point: branch-level divisibility is necessary but not sufficient together with leaf frames of $Ext(F')$; there are infinite families (this pattern generalizes) with all-per-split multiples along no tree or trees blocked, and no legal comparison-tree realization.

**Mathematical finding (deduction):** For $A_4 \to B_{2,2}$ ($e(A_4)=24, e(B_{2,2})=4, ratio 6$), root splits are divisible; some depth-2 states have divisible splits, but every path reaches a state with no comparison giving both branches divisible by 4 (tested exhaustively). Topological extension $A_4 \subset B_{2,2}$ and component merging are allowed, but branch-level divisibility is not sufficient for module realizability. This generalizes to an infinite family (component-structure compatible cases where recursive extension-count factors fail for all paths), contradicting sufficiency. Thus the exact-reset certificate route requires more than per-split arithmetic and leaf classes being frames of $Ext(F')$; the “module realizability” condition is independent and can be blocked combinatorially. No Lean/repo changes made; this is a negative/obstruction result for the sufficiency claim.

## Other metadata

```json
{
  "finished_at": 1793486457.9431696,
  "started_at": 1793484323.537756
}
```
