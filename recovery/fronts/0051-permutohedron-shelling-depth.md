# permutohedron-shelling-depth

## status

investigated

## origin

ai_proposal_unverified

## agent_id

3qGfZgiDLhhaNkJzl3f2KT-rubles

## exit_state

clearexit

## question

Is the minimum worst-case depth of any shelling order of the n-permutohedron equal to S(n) for all n>=1, and does that combinatorial identity create a new all-n invariant separating it from arbitrary partial orders?

## basis

Permutohedron faces correspond to partial orders and linear extensions are shelling orders; need to check exact correspondence between comparison cost and shelling move complexity.

## falsifier

Find n where some shelling order gives strictly fewer comparisons than optimal comparison sort, or show the identity fails for some n or that shelling complexity has different asymptotics.

## implication

A tight identity would allow importing geometric/shelling theory to S(n); failure would clarify why combinatorial geometry doesn't directly transfer.

## finding_unverified

lar to the "poset sorting" or to the number of linear extensions / the 1/3-2/3 conjecture which is about finding good comparisons to identify a linear extension quickly.

Also the "shelling move complexity" - in shelling a complex, when you add a facet, you glue it along its intersection with the union of previous facets; the "complexity" might relate to how complicated this intersection is. Or perhaps the number of moves.

But the question says "minimum worst-case depth of any shelling order of the n-permutohedron equal to S(n)". So depth of the shelling order (the order itself) equals S(n). That is, if you have a shelling order $\sigma_1, ..., \sigma_m$ of facets of the $n$-permutohedron, its depth is S(n)? That doesn't make obvious sense dimensionally.

Or perhaps the "depth" as in the shelling depth of the complex? Or maybe in this specific context they mean the length/depth as the number of steps? Or perhaps a translation issue and it means "minimum worst-case length" or "height"?

Alternatively, looking up how "depth" is used. Another possibility is that the "depth" refers to the depth of a vertex in the shelling order, and the worst-case depth equals S(n). Unclear. But the falsifier is very explicit about comparisons - "some shelling order gives strictly fewer comparisons than optimal comparison sort" - so "comparisons" is the unit being counted, same as in comparison sort. That means "depth" here is being used to mean the number of comparisons (the depth of the decision tree/comparison count). That is plausible in some texts.
Let us write up the analysis.

**FINDING (falsification):** The identity fails. For the n-permutohedron, shelling orders of the associated Coxeter/permutohedron complex correspond to maximal chains in the weak Bruhat order (edge moves = adjacent transpositions), so their worst-case "depth" in move-count is $h(W_n)=\binom{n}{2}=\Theta(n^2)$. Comparison sorting allows arbitrary pairwise comparisons (not restricted to adjacent swaps), giving $S(n)=\log_2(n!)+o(n\log n)=\Theta(n\log n)$. Equality fails for all $n\ge4$ ($\binom{n}{2}>S(n)$) and asymptotically. The move model (adjacent transpositions/shelling chain length) is the adjacent-swap model, not the arbitrary-comparison model; information-theoretic bound requires $\Omega(n\log n)$ anyway but the edge-restricted shelling gives quadratic depth. Also no special all-n invariant separating from general posets emerges because the geometric identity doesn't hold. Distinction: general poset linear-extension identification relates to $e(P)$ (1/3–2/3 gives $O(\log e(P))$), but transferring shelling-chain depth (edge moves) to arbitrary-comparison cost is false. 
**OBSTRUCTION:** If "depth" means comparison count in the arbitrary-comparison model, you cannot achieve $O(n\log n)$ by restricting to adjacent-transposition shelling moves; conversely the identity requires equating restricted-move shelling depth to unrestricted-comparison $S(n)$ which is false. No obvious bridge from edge-restricted shelling complexity to $S(n)$ without changing the move model.
**HONEST LIMITS:** Didn't construct an explicit counterexample script or new theorem; this is a standard combinatorial disjunction (weak Bruhat order height vs decision-tree depth / adjacent swaps vs arbitrary comparisons). The question's exact "shelling move complexity" definition might have a non-obvious correspondence, but the natural geometric correspondence gives the falsification above. No repo changes made.

## Other metadata

```json
{
  "finished_at": 1793356325.825689,
  "started_at": 1793354052.0966132
}
```
