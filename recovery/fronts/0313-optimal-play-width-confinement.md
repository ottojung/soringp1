# optimal-play-width-confinement

## status

investigated

## origin

ai_proposal_unverified

## agent_id

IXu06zXKClrCc3KFeOUmbe-weakness

## exit_state

clearexit

## question

For all n, does there exist an optimal sorter strategy achieving S(n) from the n-antichain such that every poset state reachable against all adversary responses has Dilworth width bounded by a fixed constant (or by polylog(n)), or must every S(n)-optimal strategy encounter states of unbounded-in-n Dilworth width under some adversary play?

## basis

Root-reachable posets can realize arbitrary partial orders along some paths, but optimal minimax play is constrained; Dilworth width measures chain-cover complexity (Dilworth 1950). Distinct from optimal-play isomorphism/frontier barriers and from general-poset hardness (no transfer without reduction).

## falsifier

Construct, for some fixed w and all sufficiently large n (or an infinite family), an explicit S(n)-optimal sorter strategy whose entire reachable game tree stays within posets of Dilworth width <= w; alternatively prove a theorem forcing width >= g(n) with g(n)->infinity on every S(n)-optimal strategy for an infinite family of n.

## implication

Width confinement of optimal play would identify a restricted root-reachable subclass relevant to exact S(n) evaluation and could enable parameterized minimax methods if F(P) admits width-sensitive analysis; a forced-width-growth theorem is a structural barrier to width-based compression of the exact sorting game.

## finding_unverified

sitive falsifier as stated (“entire reachable game tree stays within width `<= w`”) is impossible. This is trivial and not a property of optimal play.

### Substantive all-`n` obstruction (stronger, applies to every correct strategy)
**Lemma (one-comparison width monotonicity).** For a poset `P` and its extension `P'` by adding one comparability, `w(P)-1 <= w(P') <= w(P)`.
*Proof.* `w(P') <= w(P)`: adding relations cannot create a larger antichain. Lower bound: let `A` be a maximum antichain of `P`, `|A|=w(P)`. The added relation makes at most the compared pair comparable; if both lie in `A`, `A \ {x}` (size `w(P)-1`) is an antichain of `P'`, else `A` remains an antichain. So `w(P') >= w(P)-1`. ∎

**Theorem (forced width, every path).** Let `P_0,…,P_t` be states along any root-to-leaf path of any correct comparison-sorting strategy from the `n`-antichain. Then for all `0 <= d <= t`, `w(P_d) >= n-d`, and `t >= n-1`. Moreover `w(P_t)=1` implies `t>=n-1`.
*Proof.* Induction: `w(P_0)=n`. Step gives `w(P_{d}) >= w(P_{d-1})-1 >= n-d`. A leaf is a total order so `w(P_t)=1 <= n-t`. ∎

**Corollary (disproves width confinement / confirms forced unbounded width).** For every correct sorting strategy `T` (hence for every `S(n)`-optimal strategy), and every function `g(n)->∞` with `g(n) <= n-1`, there is a depth `d_n = n-g(n)` such that **every** root-to-leaf path of `T` passes through a state of width `>= g(n)`. In particular, for fixed `d`, every path has width `>= n-d` at depth `d`. No adversary choice is needed; width growth/height (as unbounded-in-`n` width) is forced on all paths, independent of optimality.

Examples (sanity): `n=4`, root 4, depth 1 gives 3; depth 2 can be 2 (matching pair) or 3, matching the bound `>=2`. `n=5`, `(0<1),(0<2)` -> width 4; `(0<1),(2<3)` -> width 3, bound `>=3`.

### Falsification attempts and limits
- **Positive falsifier (constant/polylog width strategy):** impossible for `n` larger than the bound, by the theorem; even excluding root, depth 1 has width `n-1`, depth `d` has width `>= n-d`.
- **“Only optimal strategies are constrained”:** the obstruction is *strategy-independent* (stronger than needed). Optimality cannot help.
- **Soundness vs completeness note:** Dilworth width here is the standard poset width (sound measure). The result is complete for the question asked: it rules out confinement for the whole correct-sorting game, so a fortiori for `S(n)`-optimal play.
- **Honest limit:** This is an elementary consequence of width monotonicity (`w` drops by <=1 per comparison) and does **not** give new information about `S(n)` or `SORT-BOUND-U` complexity beyond the trivial chain-cover counting fact already implicit in “`n-1` comparisons needed to connect/sort by width 1” intuition. It does not distinguish optimal from non-optimal play and does not address pathwidth/treewidth of the comparison/DAG state graph (a different notion; see other `*pathwidth*` frontiers). It therefore does **not** satisfy the publication gate as a substantive new theorem about evaluating `S(n)`; it is a clean all-`n` refutation/closure of this specific front as stated. No general-poset hardness transfer used.

**Conclusion:** the front’s width-confinement hypothesis is false (trivially by root, substantively because `w(P_d) >= n-d` on every path of every correct strategy). The suggested complexity implication (width-based compression/parameterization enabled by confinement of optimal play) does not follow; confinement does not occur.

## Other metadata

```json
{
  "finished_at": 1793872924.9775229,
  "started_at": 1793872540.323186
}
```
