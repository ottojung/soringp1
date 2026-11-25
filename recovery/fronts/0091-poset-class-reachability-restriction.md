# poset-class-reachability-restriction

## status

blocked

## origin

ai_proposal_unverified

## agent_id

czhUM6B0vTNA1lx05Ovhj1-assertion

## exit_state

failed

## question

Is there a nontrivial all-n property (other than being partial orders) that every poset reachable on some height-S(n) optimal strategy from an antichain must satisfy, and does that property place those posets outside the class that would enable a trivial poly-time counting/certificate transfer?

## basis

Hardness of arbitrary partial orders need not transfer to fixed antichain root; need all-n structural restriction on optimal-play reachable posets.

## falsifier

Show that for all large n the posets on height-optimal plays generate a class that is #P-hard to count over or are universal, or exhibit an explicit restriction that blocks all known transfers and is stable for all n.

## implication

A provable restriction would distinguish 'general poset' hardness from the antichain-root game (matching AGENTS.md); no restriction would leave general-poset barriers as plausible only if they survive universality.

## finding_unverified

imal strategy from an antichain must satisfy" - so fix some optimal strategy T (optimal = achieves S(n)). Consider all possible adversarial answer sequences when playing against T starting from antichain. Each such sequence leads to some poset state P at some depth. The question says "poset reachable on some height-S(n) optimal strategy" - so P is reachable on (by playing) some height-S(n) optimal strategy. That means there exists some optimal strategy T and some adversarial play against T reaching P. That is almost the same as saying "reachable by some sequence of comparisons with adversarial answers" but the path is constrained to follow some optimal strategy? Wait - but if T is optimal, T chooses pairs to achieve height S(n). The adversary chooses answers. So states reachable on strategy T are exactly states in the decision tree of T. So union over all optimal strategies T of all states in tree(T). That’s a big union - could include almost anything? Probably less restricted.

Or perhaps the other way around - posets that appear on *any* optimal strategy's play? Let us read again carefully:
> "Is there a nontrivial all-n property (other than being partial orders) that every poset reachable on some height-S(n) optimal strategy from an antichain must satisfy, and does that property place those posets outside the class that would enable a trivial poly-time counting/certificate transfer?"

The phrasing is a bit ambiguous, but "reachable on some height-S(n) optimal strategy" - like "reachable on some route" or "reachable via some strategy". Another reading: every poset reachable on some height-S(n) optimal strategy (i.e. reachable by any height-optimal strategy) must satisfy... That would mean all posets on all optimal strategies. That seems more interesting. Let us look up how others interpret similar phrasing in this repo. Also look up the full question again more.

Let us start by exploring more of the codebase to understand the full picture, especially related to optimal strategies and poset classes.

Let us understand this better - need to distinguish different notions of reachability.

Let us start by exploring the model more deeply - understanding what posets can actually appear in optimal strategies.

Let us think. Also look up the "antichain-root game" - in the game, sorter wants to sort fast (achieve small height), adversary wants to force more comparisons. An optimal strategy for sorter is a strategy achieving height S(n). States reachable in plays of that strategy are states in its decision tree. The question says "reachable on some height-S(n) optimal strategy" - if we say "on X" meaning "using X" or "in the context of X". Also in common language sometimes ambiguous. But "every poset reachable on some height-S(n) optimal strategy" - if there exists some optimal strategy and we look at posets reachable on it, then "every poset reachable on some optimal strategy" is a bit strange. Better to read as: is there a property that every poset reachable (on some height-S(n) optimal strategy) from an antichain must satisfy? Or perhaps it means: for every poset reachable on *any* height-S(n) optimal strategy from an antichain, ... That is plausible. Also the falsifier says "posets on height-optimal plays generate a class that is #P-hard to count over or are universal" - "plays" of height-optimal strategies (optimal = achieving S(n)). So union over all optimal strategies of all their play states. That fits.

Let us explore systematically.


## Other metadata

```json
{
  "finished_at": 1793410056.5814495,
  "started_at": 1793406919.4389102
}
```
