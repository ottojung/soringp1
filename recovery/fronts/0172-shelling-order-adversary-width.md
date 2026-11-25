# shelling-order-adversary-width

## status

blocked

## origin

ai_proposal_unverified

## agent_id

H3MNHicf461BA3ic6y7poX-wearily

## exit_state

failed

## question

Can the adversarial minimax game for sorting from the antichain root be characterized by a bounded-width shelling/linear-extension strategy for some all-n class, or does every sound adversary strategy induce shelling width Omega(n / polylog n) on an infinite all-n subfamily reachable at optimal depths?

## basis

Primary literature on shelling orders of posets and comparability graphs plus the minimax/adversary structure in docs/problem.md; separate from generic poset width to root-reachable optimal play.

## falsifier

Construct an explicit all-n adversary (or sorter) strategy achieving bounded shelling width with exact optimal play, or prove bounded shelling width forces a fixed polynomial surplus over S(n) for all large n on the antichain.

## implication

A bounded-width shelling model would constrain the alternating game structure; an all-n linear lower bound would be a barrier to certain decomposition methods without transferring arbitrary-poset shelling hardness.

## finding_unverified

ons to already-processed elements, that's similar to an "elimination order". For general graphs elimination order gives treewidth; for perfect elimination order of chordal graphs gives nice structure.

Also comparability graphs - chordal comparability graphs are exactly the interval orders of dimension at most 2. Not obviously giving shelling width. But the question says "shelling/linear-extension strategy" - linear extension is a total order extending the partial order. A shelling order might be related to an elimination ordering.

Alternatively, maybe "shelling width" is the pathwidth of the incomparability graph? Or related to interval dimension.

Alternatively, let us look up the actual combinatorial game more carefully. In the minimax game for sorting (also called the "coin identification" or just comparison sorting game), the "state graph" of partial orders with allowed comparisons gives a game tree. The adversary strategy chooses directions. There's a concept of "graph of states" and sometimes people talk about "searching number" or "pathwidth" of this state graph? Probably not exactly.

Another angle - in some papers about sorting complexity, people talk about "shelling sequences" of permutations or about the "permutohedron". Also the permutohedron has facets corresponding to comparisons and shelling orders have been studied. Maybe "shelling width" refers to some parameter of a shelling of the permutohedron?

Or perhaps related to the "number of regions" or to the "depth" in a shelling order. Let us look up permutohedron properties quickly mentally - the permutohedron $P_n$ has vertices as permutations and edges between permutations differing by adjacent transpositions; its dimension is $n-1$. Shelling orders of the permutohedron are known (e.g. by Boeckner, etc.). Also, there are connections to shelling orders and to weak Bruhat order.

Alternatively, the "shelling width" might mean the maximum size of a "shelling interval" or something similar? Or perhaps it's about the width in terms of the Hasse diagram levels?

Alternatively, let us look up the front again more: "adversarial minimax game for sorting from the antichain root be characterized by a bounded-width shelling/linear-extension strategy for some all-n class" - so the *strategy* is characterized as a shelling/linear-extension strategy of bounded width. That means the strategy follows some shelling order or linear extension order, maintaining bounded width. That fits insertion sort style strategies - you process elements in some fixed order (a linear extension in some sense, or just a fixed order), and for each new element you insert it into the sorted structure of previous elements; the "width" of the maintained sorted structure is related to how you do insertion. Or if you use binary insertion, the maintained structure is just a sorted list. But adversary playing against insertion sort?

Or alternatively, if the sorter uses a strategy based on a fixed linear extension order and bounded-width data structure, that's a restricted class of sorting algorithms. But the question says "adversarial minimax game..." so maybe characterizing the adversary's strategy?

Alternatively, "adversary strategy induces shelling width..." - so properties of the adversary's strategy induce some shelling width parameter. This is a bit cryptic. Let us look up how this might connect to known results about sorting complexity.
Let us start by reading the problem carefully and gathering context.


## Other metadata

```json
{
  "finished_at": 1793582895.955388,
  "started_at": 1793577097.0547404
}
```
