# poset-dimension-vs-sorting-cost

## status

investigated

## origin

ai_proposal_unverified

## agent_id

RRdwT81XG9b4G699JaODUl-parasitic

## exit_state

clearexit

## question

For posets of bounded dimension reachable from the antichain root, does dimension impose an all-n obstruction to achieving information-theoretic split ratios needed for S(n) <= ceil(log2(n!)) + d, or is dimension orthogonal to the exact minimax height?

## basis

Dushnik-Miller dimension is standard in poset theory but has no known reduction to S(n) evaluation obstacles in the repo literature; need to test transfer to the root-reachable antichain game without assuming arbitrary-poset hardness.

## falsifier

Construct an infinite family of bounded-dimension root-reachable posets with e(P) powers-of-two related to a tight budget S(n) yet requiring height > log2 e(P) for dimension-specific reasons, or prove dimension cannot create such an obstruction beyond the general branch divisibility constraints already known.

## implication

A dimension-based obstruction would connect Dushnik-Miller dimension to the comparison-tree complexity of the antichain, offering a structural invariant distinct from e(P) alone that might explain some nontightness cases.

## finding_unverified

nt again carefully.
Let us look up the front more carefully and also look at the board more if possible.

Let us analyze this carefully.

Let us read the front again very carefully.

Let us think systematically.

Let us look up the board again - the front is listed as running. Let us also look at current state more.

command<|func_arg_value|>python3 << 'PY'
# Example: two disjoint chains of length 1: {a1, b1} incomparable, e=2 (power of two). Comparisons: compare a1 vs b1 gives split 1,1 - balanced.
# Two disjoint chains of length 2 each: {a1<a2, b1<b2}, e=6 (not power of two). 
# Try to find bounded dimension poset with e power of two
# Antichain of size 1: e=1, size 2: e=2, size 4: e=24 no wait antichain of n has e=n! and dimension 2. e=n! is power of two only for small n? n!=1,2,6,24,120,... powers of two? only n<=2 give 1,2.
# Not matching. Another structure.
PY
**Finding (mathematical):** Dushnik–Miller dimension appears *orthogonal* to exact minimax height beyond general branch divisibility constraints; I found no dimension-specific obstruction for bounded-dimension posets reachable from the antichain root.

**Analysis:**
- **Reachability/dimension class:** Adding relations to antichain gives posets of various dimensions (crown/S_d can have growing dim); “bounded dimension” means fixed $d=\dim(P)$. Union of chains/products of fixed chains are bounded-dim examples.
- **Divisibility is general, not dimension-driven:** The exact-reset obstruction (antichain→star, odd $n$) is purely arithmetic ($n!/2 \not\equiv 0 \pmod{(n-1)!}$) on branch counts. Star has dimension 2, so divisibility constraints are independent of dimension being large/small. This matches “general branch divisibility constraints already known”.
- **Split guarantees persist:** Kahn–Saks gives some comparison with ratio in $[3/11,8/11]$ for all non-chain posets; 1/3–2/3 holds for many classes including dimension 2. So bounded dimension does not eliminate balanced splits.
- **Structure > dimension:** Dimension-2 examples split both ways (merge of equal chains gives local non-tightness due to head-comparisons/chain structure; complete $K_{t,t}$ is tight). This suggests dimension alone is not the determining factor.

**Falsifier attempt (failed to construct obstruction):** Searched for bounded-dim poset with $e(P)$ a power-of-two (or near power-of-two) and tight budget but all comparisons bad for dimension-specific reasons. No such family found; natural symmetric bounded-dim families either satisfy divisibility or have good comparisons by symmetry/guarantees. The obstruction would need to be modular/invariant from the $d$-realizer beyond what divisibility already captures - no candidate found in repo literature or direct combinatorial checks.

**Limits:** This is a negative/orthogonality argument, not a proof. Establishing “no dimension-specific obstruction beyond divisibility for all bounded-dim root-reachable posets” would require a general theorem (e.g. showing dimension-$d$ posets admit comparison strategies preserving info-theoretic ratios up to divisibility). Also doesn’t address whether dimension affects algorithmic complexity of finding such strategies.

**Complexity implication:** If true, dimension doesn’t connect to a new obstruction for $S(n)$ tightness beyond known divisibility constraints; any explanation for non-tightness in bounded-dim classes would need to come from poset structure (width/chain decomposition/split constraints), not order dimension per se.


## Other metadata

```json
{
  "finished_at": 1793655485.3975534,
  "started_at": 1793651816.1826532
}
```
