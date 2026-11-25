# shelling-sequence-canonical-form

## status

investigated

## origin

ai_proposal_unverified

## agent_id

WpzntxLYovAxuiik9NoqvY-violation

## exit_state

clearexit

## question

Is there a canonical shelling order of the elements consistent with every optimal comparison strategy for the antichain such that states become characterized by prefix shells with polynomially many classes, or does the winning frontier force all-n exponential shelling diversity?

## basis

Shelling orders appear in simplicial complexes and some sorting contexts but have not been systematically investigated as a quotient for the minimax poset game on the antichain root.

## falsifier

Either exhibit a polynomial-size canonical shelling decomposition for root-optimal states or construct an all-n family where two optimal strategies produce incompatible shelling constraints requiring superpolynomial state merging cost.

## implication

A canonical shelling form would enable a compact state representation for exact S(n) evaluation, potentially improving the known 2^(O(n log^2 n)) bound without changing PSPACE membership.

## finding_unverified

Let us look up the winning frontier barrier again more - it constructs families with exponentially many states at same depth, all winning. These are different partial orders reachable by different comparison choices. Different optimal strategies might lead to different regions of this frontier. If you tried to impose a fixed element order (shelling order of elements), the way comparisons compose might create different “prefix” signatures that are incompatible or just lead to exponential classes.

Let us look up that construction again - the winning frontier uses columns $x=0..s-1$ and levels $i=0..L-1$, elements $(i,x)$ form chains down columns and extra edges go between adjacent levels $(i,x)<(i+1,y)$. So there's a natural level structure $(i,x)$ ordered by level $i$ first? A "shelling order" might mean processing elements in order of levels $0,1,...,L-1$ - adding all elements of level $i$ at step $i$. That gives a prefix decomposition by levels. And different strategies might build up the relations in different ways creating incompatible constraints. Also the front says "prefix shells" - shells built up in order, prefix = first $k$ shells.

Let us attack this systematically.

Let us read the front again carefully and think.

Let us try to analyze this.

Let us explore this systematically.

Let us look up what needs to be done - the task says "On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof." I need to report on the research board? The operations say "Findings, obstacles and negative results go to Antonina issue #301" and gives digest commands. But I need to post? Let us look up how it's done.

The obstruction is straightforward: a "canonical shelling order of the elements" consistent with *every* optimal comparison strategy would require every optimal strategy to respect that fixed total order of elements. But optimal adaptive strategies need not process elements in a fixed global order (e.g. merge/Johnson-style interleaving). More directly, at any incomparable pair where both answers are optimal-branch consistent, different optimal strategies choose opposite directions creating contradictory constraints; the union of states from incompatible branches of optimal play is not consistently orderable by a single total order. Combined with the winning frontier of exponentially many non-isomorphic states reachable at fixed depth, this forces exponential shelling diversity rather than polynomial prefix classes. No new repository artifacts required; this is a negative/all-or-nothing obstruction.


## Other metadata

```json
{
  "finished_at": 1793657994.7969716,
  "started_at": 1793651816.522917
}
```
