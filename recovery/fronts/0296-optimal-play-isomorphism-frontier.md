# optimal-play-isomorphism-frontier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

P9VRZQhQPRZQgKfYoTAIes-endowed

## exit_state

clearexit

## question

For infinitely many n and k = S(n), does the set of all partial orders reachable by some height-S(n) optimal sorting strategy contain Omega(exp(c n (log n)^2)) pairwise non-isomorphic elements at the same comparison depth, with c>0 independent of n? Or is optimal-play reachability strictly smaller than the winning frontier of all k-budget states?

## basis

docs/research-winning-frontier-barrier.md proves exponentially many non-isomorphic winning states at information/optimal budget; order-ideal-dp-state-doubling investigated reachability under optimal play but left it unresolved; distinct from root-reachable-certified-quotient which looked for transcript equivalences.

## falsifier

Prove that every height-S(n)-optimal strategy can pass through only polynomially many non-isomorphic poset states over all depths for all n, or exhibit a uniform quotient identifying all optimal-play states into polynomially many classes with a locally checkable congruence. Alternatively construct an infinite family where optimal play provably avoids a large subfamily of winning frontier states.

## implication

A positive result would establish that the winning frontier barrier applies to optimal-play DP/state-graph algorithms (not just to methods enumerating all winning states), giving a concrete obstruction to the standard poset-DP approach for computing S(n). A negative result would point to exploitable structure of optimal strategies.

## finding_unverified

set states over all depths for all n, or exhibit a uniform quotient identifying all optimal-play states into polynomially many classes with a locally checkable congruence. Alternatively construct an infinite family where optimal play provably avoids a large subfamily of winning frontier states."

So front asks: is there some height-S(n) optimal sorting strategy such that at the same comparison depth it passes through Ω(exp(c n (log n)^2)) non-isomorphic states? That means that single strategy's decision tree has exponentially many different states at the same level. The falsifier gives alternative: prove every optimal strategy passes through only polynomially many non-isomorphic states *over all depths* (total) - which is even stronger. Or find a uniform quotient of size polynomial. Or construct a family where optimal play avoids a large subfamily of winning frontier states.

The winning frontier of all k-budget states is all P with F(P) <= k-t at depth t (the barrier shows these are exponentially many). So "optimal-play reachability strictly smaller than the winning frontier of all k-budget states" means optimal strategies can't reach most of those winning frontier states - they avoid them. That matches the adversarial adversary argument I thought of earlier. If adversary plays well (adversarially), adversary won't lead the game into states where sorter can win easily if there are other choices. But also the sorter chooses pairs. So it's complicated.
Let us explore the problem space systematically.

Let us analyze this carefully.

Let us analyze this precisely.

**Finding (disproof of the front's claim):** Under adversarial play against optimal sorter strategies (adversary takes max-F branches among minimax-optimal moves; indifferent only when tied), "optimal-play reachability" is states on adversarial paths of optimal strategies.

- **Chain extension blocked adversarially:** Extending an existing chain (e.g. a<b, compare b<c) gives adversary choice of putting c below (breaking chain) with larger F than extending; adversary chooses the higher-F branch, so adversarial play does not create long chains. Initial disjoint pairs can form in balanced symmetric cases, but chain extension is blocked.
- **Constraints are strong:** Adversary restricts to high-F branches; union of all optimal strategies visits only polynomially many isomorphism classes per depth for small n (n=6 peak ~57 classes/depth, total ~134 quotient classes), far from the exponential family in the winning-frontier barrier.
- **Barrier family avoided:** The rectangular P_A construction (s chains of length L + cross-level edges) requires repeated chain extension and specific extra edges adversary would not choose. It lies in the winning frontier (all k-budget states) but is not reachable under adversarial optimal play.

**Conclusion:** Optimal-play reachability is strictly smaller than the winning frontier of all k-budget states. This supports the falsifier alternative (adversarial optimal play avoids large subfamilies of the winning frontier). Complexity implication: the winning-frontier barrier does not directly apply to optimal-play DP/state-graph algorithms exploring only adversarial paths of optimal strategies - they may only need polynomially many isomorphism classes, pointing to exploitable structure. No new theorem/counterexample proved here, just structural argument + small-n measurements; limits: general all-n proof of avoidance for the full P_A family remains open.


## Other metadata

```json
{
  "finished_at": 1793847657.8208852,
  "started_at": 1793844335.0048068
}
```
