# framed-dag-completeness-tight

## status

investigated

## origin

executive_commissioned

## agent_id

slcHUXpswNMBj3Iujj5TrA-outskirts

## exit_state

clearexit

## question

Prove or disprove that every height-S(n) adaptive strategy has a polynomial-size permutation-framed DAG witness at budget S(n), or characterize which n/families fail completeness.

## basis

Framed grammar is sound and checkable in polynomial time; NP membership remains open.

## falsifier

Exhibit a family of optimal strategies at height S(n) where join/intersection in the framed grammar necessarily loses information causing exponential blowup or incompleteness.

## implication

Completeness => SORT-BOUND-U in NP; incompleteness gives a certificate complexity gap.

## finding_unverified

or *exact* class resets due to branch divisibility (mass split), but framed DAG uses *forgetful* intersections (only guaranteed relations) so it does not require equal leaf classes — this obstruction does not constrain non-exact/forgetful joins. (docs/research-exact-reset-realizability.md)
- **Winning frontier:** 2^(Ω(n log^2 n)) nonisomorphic winning states exist at depths around S(n) (barrier to enumerating states), but that’s a frontier/state-space barrier, not a proof that every optimal adaptive strategy lacks a polynomial-size framed DAG witness.

**Potential obstruction relevant to the falsifier (adaptive strategies):**
- **Join/intersection information loss:** intersection keeps only relations true in *all* incoming paths (after possibly different edge permutations). Permutations give relabeling flexibility, but disjunctive correlations present in some branches but not all can be lost at joins. For an *arbitrary* adaptive strategy, can we always find *some* other framed DAG (possibly different structure/choices) of polynomial size that is accepted at height S(n)? Or is there some family of optimal strategies where maintaining correctness+optimal height forces either (a) exponential blowup to avoid bad joins, or (b) incompleteness if you join?
- **Local compression failure:** research packets note “Root-optimal conditional compression…” with “The n=6 DAG counterexample defeats naive local repairs.” That suggests for some optimal strategy at n=6, naive local normalization/compression fails; whether this scales to an all-n exponential family or is fixable by global reorganization remains unproven. (docs/research-packets.json across fronts)
- **Single-policy sharing:** for one optimal policy, hash-consing identical poset states gives little sharing for small n (DAG(1) size ~ tree size), suggesting the strategy structure may not create many merge points; compression would need to rely on framed-DAG joins with permutations/intersections, not just identical states.

**Concrete failed approach / exact obstruction (current state):**
No all-n theorem or explicit infinite family is established in the reviewed material that *necessarily* forces exponential blowup or incompleteness for every polynomial attempt to witness some optimal adaptive strategy via framed-DAG joins. The network example doesn’t transfer. The exact-reset divisibility obstruction doesn’t apply to forgetful joins. The n=6 “naive local repairs defeated” is noted but not documented as a proven all-n counterexample in the accessible docs.

**Honest limits:**
- **Completeness is open.** NP membership of SORT-BOUND-U would follow from all-n polynomial-size framed DAG completeness; conversely incompleteness would give a certificate complexity gap, but neither is proved.
- **Distinction critical:** soundness ≠ completeness; general-poset hardness (e.g. Parberry/coNP for network verification) doesn’t imply obstruction for a *single optimal adaptive sorter* per n.
- **Falsifier not discharged.** A serious attempt would need either (1) a theorem showing some optimal-strategy family is not representable by any polynomial framed DAG (incompleteness) or (2) a proof that all representations require exponential size (blowup), accounting for permutations and the ability to choose a different DAG structure (not just compress a given tree). The intersection+permutation model is subtle; current literature points to barriers/obstructions but not a completed all-n disproof of the front claim.


## Other metadata

```json
{
  "finished_at": 1793729668.3077178
}
```
