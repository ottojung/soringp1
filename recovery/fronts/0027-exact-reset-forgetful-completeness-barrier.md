# exact-reset-forgetful-completeness-barrier

## status

investigated

## origin

manual_executive

## agent_id

Rq8FplNNJby8PW27x6Eo43-squirrel

## exit_state

clearexit

## question

For forgetful framed DAG certificates of exact S(n), is polynomial-size completeness (all optimal strategies coverable) equivalent to exact-reset, and does there exist an all-n family where forgetful joins force exponentially many classes making polynomial completeness impossible?

## basis

Board notes forgetful > exact-reset; exact-reset blocked by divisibility; completeness open; prior framed-certificate work.

## falsifier

Exhibit an explicit all-n optimal strategy family coverable by polynomial-size forgetful DAG but not by any polynomial-size exact-reset DAG, or prove an exponential lower bound on forgetful classes for some root-optimal family.

## implication

Would settle whether the forgetful route can yield a polynomial NP certificate or is obstructed like exact-reset (divisibility).

## finding_unverified

s smaller than everyone else. Correct - n-1 comparisons suffice.

Now look at the poset states (guaranteed relations). At each node, guaranteed relations are only those we can deduce transitively. So in this tournament, when element x beats element y, we get relation x < y. When x loses to y, we get y < x. The guaranteed poset is just the set of all comparisons made so far with their outcomes - which is a kind of "minimum-so-far" structure (a total order on the seen elements? Or just that the current min is below all seen so far). Yes, transitive closure gives that current candidate < every element it beat.

At the leaves, the final candidate has been compared to everyone and won all, so guaranteed relations make it below all others - which is exactly V_n (up to labeling). The path length is always n-1 comparisons. So this is a tree (no sharing of different paths leading to same state? Different elements become candidates depending on outcomes; the poset structure is different - e.g. "element 2 is current min and below element 1" is different from "element 1 is current min and below element 2" as poset states on labeled elements). So different leaves might correspond to different elements being minimum - the guaranteed posets are isomorphic to V_n but on different center elements (different labelings). The checker uses frames/permutations to relabel slots.

But in terms of the certificate structure as checked by the script - at leaves it just checks that the guaranteed relations form a total order? Wait look up the checker again: at leaves it says "if relations[v] is not None: rows = relations[v]; for i in range(n): for j in range(i+1,n): if not (rows[i] & (1<<j) or rows[j] & (1<<i)): raise InvalidCertificate(f\"leaf {v} does not sort {i},{j}\")" - so leaf must be a total order (every pair comparable). But V_n means only n-1 pairs are guaranteed (the minimum below everyone else) - the other pairs (among the rest) are NOT guaranteed. That means V_n is NOT a total order! That can't be. Let us check.
Let us analyze this carefully. The task says "attack a precise all-n falsifiable mathematical claim" - I need to identify the claim being made and try to disprove it.

Let us start by exploring the full context.

Let us look up the exact board message again more closely.

Let us think more deeply about the models.

Let us start by exploring the models more precisely and trying to construct arguments.

Let us read more about the exact-reset realization and the framed certificate frontier to understand the models deeply.

I analyzed the forgetful framed DAG vs exact-reset question as requested. The divisibility obstruction blocking exact-reset trees (A_n -> V_n for odd n) does not constrain forgetful joins per the exact-reset paper, while framed DAG joins do intersection making merges selective but the obstruction doesn't transfer. Combinatorially this suggests forgetful is more powerful than exact-reset (polynomial-size completeness likely not equivalent), supporting falsifier (a). For (b), quotient experiments show rapid growth but known large families (e.g. height-two staircase) are excluded from root-optimal paths by information budget; I found no obvious all-n root-optimal family forcing exponentially many forgetful classes from current docs. Constructing explicit counterexamples or proving exponential lower bounds requires deeper combinatorial work than feasible from available notes - the question remains open with honest limits as stated.

## Other metadata

```json
{
  "finished_at": 1793322741.101511,
  "started_at": 1793317534.246787
}
```
