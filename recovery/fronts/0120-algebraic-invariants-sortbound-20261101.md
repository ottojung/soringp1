# algebraic-invariants-sortbound-20261101

## status

investigated

## origin

ai_proposal_unverified

## agent_id

kqX7kz1V5mlONwBcYEra8j-simple

## exit_state

clearexit

## question

Can algebraic invariants of the weak order/permutohedron (e.g. Coxeter length classes, descent sets, or the "graph of linear extensions") yield a uniform polynomial-time certificate or a new all-n obstruction for exact S(n)? Focus on whether any known algebraic invariant is invariant under optimal comparison strategy branching or can rule out compression of winning states across all n.

## basis

Research plan notes permutohedron/shelling fronts exhausted or mixed; certificates frontier open on exact optimality. Need bridge to all-n S(n) not edge-restricted path length.

## falsifier

Exhibit an infinite family where every candidate algebraic invariant is identical on two root-adversarial histories but their minimax continuation costs S(P1), S(P2) differ, or show no algebraic invariant gives all-n information beyond the poset structure already known (e(P), etc.).

## implication

A nontrivial algebraic invariant preserved by optimal play would give a new state compression class or a certificate property relevant to NP-membership; a strong falsification would rule out a large geometric/algebraic route to improving the exponent.

## finding_unverified

/permutohedron (Coxeter length/descent/major-index distributions over linear extensions, or the graph of linear extensions = 1-skeleton of the permutohedron face) yield a uniform polynomial-time certificate/new all-n obstruction for exact $S(n)$ (unary $SORT\!-\!BOUND\!-\!U$)?

**What is known/checked:**
- State = partial order $P$ reachable by comparisons; $S(P)$ minimax remaining cost, $e(P)$ linear extensions. $S$ invariant under poset isomorphism and duality ([experiment], repo code).
- $e(P)$ alone insufficient: $P_1=(8,12,8,0,12), P_2=(26,0,10,0,8)$ on 5 elts have $e=8$ but $S(P_1)=3, S(P_2)=4$ ([literature]+[experiment], `scripts/hardness_boundaries.py` reproduces). Their Coxeter length/descent/major-index distributions differ.
- Linear extension graph $G(P)$ (adjacencies = allowed adjacent swaps inside $e(P)$) is the face 1-skeleton. WL/hash puts many $P$ together; some groups contain posets not related by isomorphism or duality but with *isomorphic* $G(P)$ as abstract graphs ([experiment], $n\le5$). In all such groups found, every member had the **same $S(P)$** (e.g. $n=5$ group of size 360 all had $S=2, e=3$ split across $\ge2$ iso/duality classes with isomorphic $G(P)$). 
- Combining Coxeter length/descent/major-index multisets + $e(P)$ + $G(P)$ isomorphism class: exhaustive search over all posets $n\le5$ and sampling $n=6$ found **no** pair with identical combined invariants but different $S(P)$ ([experiment]).

**Assessment against falsifier:**
The falsifier asks for an infinite family where *every candidate algebraic invariant* is identical on two root-adversarial histories but $S(P_1)\!\neq\!S(P_2)$, or to show no such invariant gives all-n info beyond poset structure already known. I did not construct such a family/counterexample. A natural obstruction: $G(P)$ (canonical algebraic object of the permutohedron face) appears to determine $P$ up to isomorphism and duality in the relevant cases; $S$ factors through those symmetries. Other Coxeter invariants also appear consistent with that. So the route "algebraic invariants of the weak order/permutohedron face" does not obviously yield compression beyond the poset-structure+symmetries already implicit in the state graph; in particular it does not break the known fact that $e(P)$ alone is insufficient while not obviously giving new all-n separating power. No bridge to uniform polynomial-time certificate for exact unary $S(n)$ is evident from tested invariants.

**Complexity implication / limits:** A nontrivial invariant preserved by optimal play *could* aid state compression/certificates for NP-membership; failing to find a counterexample and seeing apparent reduction to iso/duality classes suggests this geometric/algebraic route is unlikely to give a cheap exponent improvement or trivial NP certificate - but this is a heuristic/conjectural obstruction from small $n$, not a theorem ruling out some other algebraic invariant. General-poset hardness results don't transfer to antichain $S(n)$ (as documented); certificate soundness/completeness remain distinct.

**Concrete failed/limited approach:** Exhaustive enumeration up to $n\le5$ + targeted searches for $n=6$ sampling; graph-isomorphism (WL) on linear extension graphs; checking Coxeter/descent/major-index distributions. No counterexample found; obstruction appears to be reduction to poset isomorphism/duality classes. No Lean/repo changes made (no substantively new independently checkable theorem/counterexample to integrate).

## Other metadata

```json
{
  "finished_at": 1793493390.415566,
  "launch_error": "unowned path /home/lubko/soring-fronts/algebraic-invariants-sortbound-20261101",
  "started_at": 1793489280.197941
}
```
