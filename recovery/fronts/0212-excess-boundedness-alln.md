# excess-boundedness-alln

## status

blocked

## origin

ai_proposal_unverified

## agent_id

ZUXz9lJCh2L32e4P7lRTRu-anything

## exit_state

failed

## question

Is the information-theoretic excess D(n)=S(n)-⌈log2(n!)⌉ bounded above by some constant C for all sufficiently large n, or does sup_n D(n)=+∞ under the exact adaptive comparison model?

## basis

Known values show D(1..11)=0, D(12..19)=1, larger later; Sergeev gives D(n)=o(n) but boundedness is listed as open in research-certificates-barriers.md.

## falsifier

Prove sup_n D(n) <= C for some fixed C (bounded excess) using known split properties, or construct an infinite family with D(n) -> +∞ arbitrarily slowly while preserving exact S(n) values.

## implication

Bounded excess would mean the search for optimal strategies is always within constant additive overhead of the information bound, constraining the effective budget window for exact unary evaluation; unbounded excess would mean the gap is intrinsic and grows without fixed constant.

## finding_unverified

xcess over the information-theoretic lower bound (which is already tight asymptotically) would mean S(n) = log2(n!) + O(1). That would be incredibly tight. That seems very unlikely to be true for all large n given the combinatorial constraints of comparison trees.

Compare to Huffman coding - you can achieve entropy + 1 bit. But here the "codebook" structure is more constrained (it's a sorting network/comparison tree structure, not arbitrary prefix codes). Also sorting requires being able to sort any permutation - it's a kind of universal sorting.

Also for universal traversal sequences or other things constraints apply. Or more directly, comparison trees are a restricted class of decision trees (only certain tests allowed depending on history). That restriction might make the excess unbounded?

And unrestricted tests would give excess 0 in terms of information bound? No wait - if you could do arbitrary tests (not just comparisons), you could just ask yes/no questions to identify the permutation directly and you'd need ceil(log2(n!)) tests, achieving the information bound exactly (up to ceiling). But comparisons are restricted tests - you can only ask "is x_i < x_j?" and the allowed comparisons depend on what you've learned so far? Or in general the test set is fixed structure. So the restriction of the test model (comparisons vs arbitrary tests) causes the excess. And for restricted tests, is the excess bounded?

But for arbitrary tests the model is different (not comparison-based sorting). The question says "under the exact adaptive comparison model" so comparisons are the tests. In that restricted model, is there unbounded excess over the information bound?

Also looking up Hyafil–Rivest result - they showed that constructing optimal decision trees (minimizing height) is NP-complete for arbitrary tests. But for comparison tests it's a different setting. Also Laber–Nogueira showed hardness of approximation.

But bounded excess - another way: there's a concept in some contexts called "information-theoretic bound is tight" meaning the excess is bounded. Or not. Let us look up the one-ply obstruction again more - it shows that locally you can have gaps. And they generalize to all larger n by suffix extension. But does that create unbounded excess at the root?

The witness W gave L1(W)=4 vs L0(W)=3 (excess +1 in the one-ply bound), and F(W)=4. So at n=5, the actual excess D(5)=S(5)-ceil(log2(5!))=7-7=0 if I look up my earlier calculation - wait wait, let us compute again carefully.

For n=5: log2(5!) = log2(120) ~ 6.9069, ceil is 7. S(5)=7 (from known values I showed earlier). So D(5)=0. But the witness W in the one-ply obstruction note has e(W)=8, L0(W)=3, and F(W)=4. And they say "e(P_t)=8, L0(P_t)=3, L1(P_t)=4, F(P_t)=4" for P_t = W ⊕ C_t. So for P_t on 5+t elements, e(P_t)=8, log2(e(P_t))~3, ceil is 3, so information bound gives L0=3, but actual F(P_t)=4. That means excess of +1 relative to the information bound on that specific poset state. But how does this relate to sorting all permutations of n elements (the antichain)?

The antichain on n elements has e = n! all permutations. The poset W is some intermediate state reachable during sorting - it's not the initial antichain. So local excess on some reachable poset is different from global excess on the initial antichain. The question is about global excess D(n)=S(n)-ceil(log2(n!)) for the full sorting problem on n elements.
Let us examine the split structure and known results more.


## Other metadata

```json
{
  "finished_at": 1793669310.728534,
  "started_at": 1793663279.517062
}
```
