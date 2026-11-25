# pigeonhole-adversary-rectangle-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

VpfhfUkj6kHuE6CZrdJ25q-travels

## exit_state

clearexit

## question

For the two-party/partition model induced by splitting the unary input 1^n#1^k at some cut, does every exact rectangle cover of SORT-BOUND-U contain some rectangle that is "comparison-infeasible" in a way forcing super-polynomial cover size for all large n in the informative window?

## basis

Communication complexity rectangle bounds are standard; ledger lacks a partition/rectangle front tied to the antichain game and must distinguish soundness (feasible rectangles) from completeness (arbitrary rectangles).

## falsifier

Construct a polynomial-size rectangle cover for all-n SORT-BOUND-U (respecting the comparison/partial-order constraints) or show the comparison-feasibility obstruction is not necessary for some polynomial cover.

## implication

A Yao/rectangle lower bound that uses only the pairwise-comparison feasibility (not arbitrary posets) would give a model-theoretic barrier to certain uniform algorithms without invoking circuit lower bounds forbidden by P/poly or claiming P!=PSPACE directly.

## finding_unverified

Let us think more carefully about this front.

Let us first understand the problem better - maybe look up the winning frontier barrier again, because it talks about "rectangles" in the test.

Let us start by studying the problem more deeply and trying to model this.

Let us model this carefully.

Let us start by exploring this systematically. The user says "attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n), and try seriously to DISPROVE it." Let us think of what the most promising disproof strategy would be.

Let us also add a more detailed mathematical analysis.

I have analyzed the pigeonhole-adversary-rectangle-bound front. Let us summarize the findings clearly.

## Finding (mathematical)

**Claim attacked (front):** For the two-party/partition model induced by splitting the unary input $1^n\#1^k$ at some cut, every exact rectangle cover of $\mathrm{SORT\textrm{-}BOUND\textrm{-}U}$ contains some rectangle that is "comparison-infeasible" in a way forcing super-polynomial cover size.

**Disproof (by construction):** Take the natural partition where Alice knows $n$ (prefix $1^n$) and Bob knows $k$ (suffix $1^k$) split at the $\#$ delimiter. For each $n$, define the rectangle
$$
R_n = \{n\} \times \{k \in \mathbb{N} \mid k \ge S(n)\}.
$$
Each $R_n$ is monochromatic-1 (all pairs satisfy $S(n)\le k$), every 1-input $(n,k)\in \mathrm{SORT\textrm{-}BOUND\textrm{-}U}$ lies in $R_n$, and there are at most $O(N)$ such rectangles for inputs of total length $N$. Each rectangle is anchored to a fixed $n$ (a single sorting instance) with sufficient budget $k\ge S(n)$, so they respect comparison/partial-order constraints (all comparison-feasible). This directly satisfies the falsifier: polynomial-size rectangle cover respecting comparison/partial-order constraints exists.

**Conclusion:** The comparison-feasibility obstruction is not necessary; polynomial covers exist using only feasible rectangles. No repository changes were made (no new theorem requiring Lean, no tests/scripts added beyond a temporary analysis file). The question of whether some other partition induces an obstruction remains open in general, but the specific claim as stated is disproven for the canonical partition model. The obstruction claimed does not follow from the structure of $\mathrm{SORT\textrm{-}BOUND\textrm{-}U}$.


## Other metadata

```json
{
  "finished_at": 1793573723.5157928,
  "started_at": 1793570995.0260677
}
```
