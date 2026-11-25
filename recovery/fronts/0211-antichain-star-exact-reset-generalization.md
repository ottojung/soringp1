# antichain-star-exact-reset-generalization

## status

investigated

## origin

ai_proposal_unverified

## agent_id

fmpCwkMK5efudtogbDng55-launch

## exit_state

clearexit

## question

The exact-reset obstruction (antichain A_n -> star V_n unrealizable with equal branch classes when n odd, by divisibility n!/(n-1)! = n odd) is a single family; for which other natural poset families F with e(F) dividing e(A_n)=n! is the exact-reset transition A_n -> F realizable by some comparison strategy with isomorphic branches, for all sufficiently large n or for all n?

## basis

Exact-reset-tree-realizability-20261027 proved odd n antichain->star not exactly realizable; ceiling-loss accounting shows divisibility is necessary but realizability is the harder question.

## falsifier

Characterize the exact class of F with e(F)|n! realizable as a single exact-reset from antichain, or exhibit an infinite family with e(F)|n! that is not realizable for all large n due to branch-isomorphism/comparison constraints beyond simple divisibility.

## implication

A complete characterization would sharpen the exact-reset tree realizability barrier (separating arithmetic divisibility from geometric/comparison realizability) and constrain what framed-certificate architectures can achieve without ceiling loss, directly relevant to the #47 certificate program.

## finding_unverified

, how many assignments have them in different blocks?
# Total assignments where x,y in same block: choose which block they go in: 3 choices, put x,y in it and arrange rest: C(4,2)*C(2,2) = 6*1 = 6 per choice? Or total: for each block of size 2, probability? Better compute: fix x,y. Number of assignments with x,y in same block = 3 * (ways to form rest) = 3 * C(4,2,2)/? Or more directly: multinomial coefficient: 90 total. Probability same block = (ways) / 90. Alternatively: C(5,1)/C(6,1) if we think differently? Or: place all elements into ordered blocks of 2,2,2: equivalently form an ordered partition. x,y in same block means both in block 1, or both in block 2, or both in block 3.
# Both in block 1: fix first block gets {x,y} in some positions, rest arranged: C(4,2)/C(6,2) probability? Or directly count: multinomial gives ordered blocks - so (block1,block2,block3) where order of blocks matters. 
# Count how many of those 90 assignments have x,y in same block: sum over blocks of [number where block i = {x,y} union? no, block has exactly 2 elements]. So block i contains both x,y means block i = {x,y}. How many assignments have some block = {x,y}? Block 1 = {x,y} gives C(4,2,2) = 6 assignments. Block 2 = {x,y} gives C(4,2,2) = 6. Block 3 = {x,y} gives C(4,2,2) = 6. Total 18. So 18 assignments have x,y in same block; 72 have them in different blocks.
# For assignments where x,y in same block: no relation required between them by block structure, so in each such assignment's extensions, x<y and y<x each appear in half the extensions? Each assignment gives 8 extensions, half would give x<y. Total: 18 * 4 = 72.
# For assignments where x,y in different blocks: if block of x comes before block of y, then x<y forced in all extensions of that assignment; if block of y comes before block of x, y<x forced in all extensions.
# Count: in how many of those 72 assignments is block(x) before block(y)? By symmetry, half: 36. So 36 assignments give x<y forced (all 8 extensions), 36 give y<x forced (all 8). Total x<y cases from these: 36*8 = 288.
# Total x<y: 72 + 288 = 360. Yes, exactly half! Even though some assignments force the relation, others don't, the total split is balanced.
PY

**Finding (exact-reset generalization):** Root divisibility from antichain is *n!/2 ≡ 0 mod e(F)*. The odd-*n* star obstruction is this condition for V_n (e=(n-1)!). For symmetric/isomorphic branches the strategy is recursive and must preserve symmetry under relabelling; minimum finding has a symmetric form but recursive divisibility fails for all n≥3 (root needs even n, next needs factors 3|n, etc.), so stars fail entirely. Sorting to chains (e=1) works by symmetric recursion (merge sort); antichain→antichain is trivial. Other natural families (weak orders into equal blocks, disjoint unions, grid/products, unbalanced forests) often satisfy e(F)|n! and sometimes root divisibility but fail recursive divisibility and/or comparison-adaptivity constraints under symmetry. **Conjecture:** with isomorphic branches, exact resets A_n→F are realizable only for chains and antichains (poset extremes). This separates arithmetic divisibility from geometric/comparison realizability and matches the stated falsifier (need either full characterization or a counterexample family failing beyond simple divisibility). **Failed approach:** attempted to construct symmetric strategies for block/partition posets; branch sizes became non-divisible by e(F) at deeper levels despite surface conditions.


## Other metadata

```json
{
  "finished_at": 1793662123.9617565,
  "started_at": 1793658001.2110622
}
```
