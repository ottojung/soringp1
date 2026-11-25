# downward-self-reducibility-sparse

## status

investigated

## origin

ai_proposal_unverified

## agent_id

4hinCssOWUy8yL7DbMhJfr-oppose

## exit_state

clearexit

## question

Is SORT-BOUND-U downward self-reducible in a way compatible with polynomial-time reductions (or is every natural downward self-reduction blocked), and would such downward self-reducibility together with sparsity force consequences different from general sparse languages for this structured poset problem?

## basis

Sparsity barrier (Mahaney), unary encoding, adversarial minimax self-reducibility of posets; separate from alternation depth/compression.

## falsifier

Construct an explicit polynomial-time downward self-reduction for SORT-BOUND-U to instances of strictly smaller 'size' in unary encoding, or prove that all poset-structure-preserving reductions must preserve some invariant making downward self-reducibility impossible for large n.

## implication

For sparse sets, downward self-reducibility has known consequences (e.g. related to low sets/classes), but Mahaney already gave the many-one NP-hard => P=NP barrier; this targets the structured self-reducibility angle distinct from generic sparsity and is falsifiable all-n.

## finding_unverified

here b_n depends on membership in some decidable non-P tally language H, placed at positions t_m. They show U_G ∉ P but U_G is in nonuniform AC^0. Also G satisfies insertion recurrence G(n)-G(n-1) <= ceil(log2 n). So the insertion recurrence plus monotonicity plus nonuniform circuits is not sufficient for uniform P - you need more structure. That means the recurrences alone don't give DSR in the computational sense that forces P.

But also is SORT-BOUND-U DSR via k-parameter? The reduction would be: to decide (n,k), do binary search to find minimal k0 for this n (by queries to (n,k') with k'<k0), return k>=k0. This is a polynomial-time Turing reduction using the oracle SORT-BOUND-U. The queries are all of the form (n, k') - same n, different k'. The length is n + k' + 1. For queries in the binary search that find the threshold, we might need to query both smaller and larger k' in the standard binary search? Let us think. Standard binary search: search in range [lo,hi], if mid gives yes and maybe can go lower, query mid-? Or more carefully: want to know if min{k' : (n,k') in L} <= k. Do binary search: let lo=0,hi=U(n); while lo < hi: mid = floor((lo+hi)/2); if (n,mid) in L then hi=mid else lo=mid+1. After search, check if lo <= k. The queries are (n,mid) for various mid values. Some mid values may be < k, some may be > k (depending on where we are). So queries are not all to strictly smaller instances than (n,k) - some could be larger. That breaks downward self-reducibility.
Let us think through this carefully.

Let us study this more systematically and report findings.

Let us gather evidence and report.

**Finding (mathematical):** No explicit polynomial-time downward self-reduction (DSR) from $SORT\!-\!BOUND\!-\!U = \{1^n\#1^k : S(n)\le k\}$ to strictly smaller instances of the same language is known, and the natural routes appear blocked.

**Obstructions:**
- **Language restriction:** The standard minimax self-reduction of the sorting game produces states that are non-antichain posets (after comparisons). A valid reduction to $SORT\!-\!BOUND\!-\!U$ must stay inside the antichain form; embedding general posets back into antichains is not a polynomial-time reduction in the direction that preserves downward size/equivalence for this exact language.
- **Parameter recurrences fail equivalence:** Relations like $S(n)\le S(n-1)+\lceil\log_2 n\rceil$ give one-way implications, and merge/lower bounds are inequalities, not exact equivalences. Monotonicity in $k$ goes the wrong way for "downward" (larger $k$ = larger instance length). Any attempt to fix by parameter changes cannot guarantee all oracle queries are strictly smaller while preserving equivalence.
- **Sparsity + DSR would be strong:** As noted, $SORT\!-\!BOUND\!-\!U$ is sparse; for sparse DSR sets the standard consequence is membership in P (distinct from generic sparsity alone). However, $U_G$ in the docs shows numerical recurrences do not by themselves force uniform P, underscoring that extra structure would be needed — structure which does not obviously yield a DSR reduction staying in the language.

**Conclusion:** The falsifier is not satisfied. There is no known construction of such a reduction, and every natural poset-structure-preserving attempt is blocked by leaving the antichain language or failing exact equivalence; proving impossibility would require showing all such reductions preserve some invariant. I make no complexity-class separation claim; report limits honestly.


## Other metadata

```json
{
  "finished_at": 1793383332.6524491,
  "started_at": 1793378916.7827878
}
```
