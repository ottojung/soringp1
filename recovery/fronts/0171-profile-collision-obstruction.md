# profile-collision-obstruction

## status

blocked

## origin

ai_proposal_unverified

## agent_id

nkOH1HWtNZjbLEpbXbRfVh-silver

## exit_state

failed

## question

For the budgeted minimax search over the antichain root, is there an infinite all-n family of reachable partial orders P_n that remain pairwise distinguishable for the exact value F(P) but become indistinguishable under every polynomial-time computable canonical profile map that is sound for the recurrence, forcing superpolynomial state lists to compute S(n) exactly?

## basis

Board #301 + winning frontier (docs/research-winning-frontier-barrier.md) + budgeted DFS (docs/problem.md upper bounds); distinguish profile maps from arbitrary poset isomorphism classes.

## falsifier

Exhibit a polynomial-time sound canonicalization that achieves polynomially many profile classes for all n on the winning frontier, or prove that no infinite all-n family forces collisions for every sound polynomial map.

## implication

A verified all-n profile compression would give a uniform exact evaluator for S(n) closer to polynomial time/space without enumerating the full winning frontier; a general obstruction would bar this natural memoization route distinct from general-poset pathwidth.

## finding_unverified

or the minimax recurrence (preserves exact F).
The front says "P_n that remain pairwise distinguishable for the exact value F(P)" - so different P_i, P_j in the family have different F(P_i) != F(P_j)? Let us look up the winning frontier again. In section 2: "all constructed states are winning. The s disjoint initial chains remain valid in every P_A. A standard balanced winner tournament merges their sorted heads..." They compute F(P_A) <= B = k-t, so all these states have F(P_A) <= B. But they are different posets (different extra edges). Do they have the same F value or different F values?
The construction says "pairwise distinguishable for the exact value F(P)" - distinguishable could mean you need to distinguish them to compute F exactly. But if they have same bound, maybe same F? Or maybe different F values. Also in general different posets have different F. But the key is - if you have a sound map for exact F, then any two states with same profile must have same F (otherwise the map would give wrong result). Also conversely, isomorphism is sound and groups by isomorphism class; but states in same isomorphism class have same F. States in different isomorphism classes might have same or different F. The quotient by F-value alone would be coarser but is that "sound for the recurrence"? No - F-value alone doesn't tell you the transition structure needed for the recurrence (as shown by linear-extension count falsification: same L but different F; also different posets can have same F but different transition behavior? Maybe possible). So "sound for the recurrence" means it's a valid congruence for the recurrence relation, stronger than just same F.
Also looking up the compression notes again: "sound DP quotient" requires both (i) F constant on classes and (ii) the multiset of unordered successor-class PAIRS is well-defined on classes. So it's a congruence for the recurrence algebra.
The front says "remain pairwise distinguishable for the exact value F(P)" - so F(P_i) != F(P_j) for i!=j? That would mean to compute exact F you need to distinguish them. And a map sound for recurrence that preserves F would need to map them to different profiles if they have different F? Because if two states have different F values, you cannot map them to the same profile and have F preserved - that would violate soundness for exact F. That contradicts.
Alternatively "distinguishable for the exact value F(P)" in the sense that you can distinguish them by computing F(P) (they are different states) - i.e. they are not equivalent under any trivial identification. And "become indistinguishable under every polynomial-time computable canonical profile map that is sound for the recurrence" - so every polynomial-time sound map (for recurrence) makes them map to same profile class, even though they are different states. But if the map is sound for the recurrence (a congruence preserving the recurrence), then same class means same F and compatible transitions. That means such a map would have to identify states that might need to be distinguished - but if it's sound, identification is only allowed if equivalent under recurrence. That doesn't directly force superpolynomial state lists; it means the quotient is small or large depending. Or maybe the issue is that you need to compute the profile (the canonical form) and doing so is expensive, or that there are no good profiles. Let us look up the exact question again more carefully.
Let us analyze the front carefully.


## Other metadata

```json
{
  "finished_at": 1793582895.6776168,
  "started_at": 1793577095.9680016
}
```
