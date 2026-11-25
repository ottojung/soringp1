# n12-obstruction-generalization

## status

investigated

## origin

executive_manual

## agent_id

Cxsw38xOPP28c59VzyHAXY-passing

## exit_state

clearexit

## question

What combinatorial invariant causes S(12)-C(12)=1 (the n=12 obstruction)? Does this invariant generalize to an infinite family where S(n)-C(n) >= c*something or creates a uniform lower-bound barrier?

## basis

research-plan.md lists 'Can the n = 12 obstruction be explained by an invariant that generalizes?' as open; Stober-Weiss results document the excess.

## falsifier

Find a uniform invariant explaining all known excess values S(n)-C(n) or prove the n=12 case is isolated with no infinite generalization.

## implication

Generalizing the obstruction could yield improved effective lower bounds and a better understanding of when the information bound fails.

## finding_unverified

Let us look deeper at the board and research frontier, and also understand n=12 obstruction.
Let us explore the codebase to understand the obstruction better.

Let us look up the known excess values S(n)-C(n) from literature.

**FALSIFIER ATTEMPT (uniform invariant for all excess S(n)-C(n))**

Tried to find a reusable combinatorial invariant explaining all known excess values. Tested candidates against literature + local probes (scripts/one_ply_obstruction.py, scripts/obstruction_probe.py):

**Candidates tested (all falsified or insufficient):**
- Monotonicity in e(P): falsified (n=6 P1 e=13 m=5 > P2 e=14 m=4). Same-e different-m at n>=5 falsifies "m is function of e". 
- Scalar (e, width, #min, #max): collisions remain at n=6 (e.g. (13,2,2,2) gives m in {4,5}). 
- Efficiency/slack ratio: n=5 tight with less slack than n=12 (inversion across n=20/n=22). Forced prefix occurs at tight n (5,10) too. 
- Local one-ply bound L1 > L0: gives strict improvement (smallest witness n=5 e=8 m=4>L0=3) but is local (one ply), doesn't predict global routing; also can't be computed cheaply in general. 
- Merge/disjoint chains: explain some local failures (e.g. Merge(2,4) m=5>4) but smallest frontier failure e=8 is not a chain-union; balanced merge gives unbounded local gap m-ceil(log2 e)->∞ in general, but no known reduction from antichain P0 to a single merge bottleneck family gives a uniform invariant for all n.

**Known excess pattern (from values):** tight through n=11 (excess 0), excess 1 at 12-19, back to 0 at 20,21, excess 1 at 22; n>=23 open. Irregular, no obvious arithmetic progression.

**Finding:** No known uniform invariant explains all excess values. The n=12 obstruction is structural/global (routing of all n! permutations through the decision tree) - Peczarski notes sortability not monotone in e and symmetry can help; Stober-Weiss show it's certified by exhaustive search (Wells) with no published compact certificate/localized bottleneck set. Local information-bound failures appear early but don't imply global gaps.

**Generalization:** Local gap is unbounded in arbitrary posets (merge family), but transferring to the fixed antichain family S(n) is nontrivial with no known reduction. No evidence of an infinite family forced by the same invariant giving S(n)-C(n) >= c*n^α; the excess appears sporadically. Also distinction matters: L1 is sound lower bound (certificate-soundness) but not complete; Hanamura-Iwata gives sufficient condition for small e (completeness for that class) not a general invariant.

**Complexity implication:** Even if found, this is a comparison lower bound on S(n) (not obviously giving a uniform lower bound for computing S(n) in unary). Unary SORT-BOUND-U is in PSPACE/sparse (Mahaney barrier) - circuit lower bounds don't apply; unconditional super-polynomial lower bounds for computing it are equivalent to P!=PSPACE/NP!=PSPACE. A better effective lower bound on the value is different from complexity lower bound for the evaluation function.

**Conclusion:** Falsification failed - no uniform invariant found. n=12 appears isolated in pattern relative to tested invariants; no obvious infinite generalization. Obstruction remains certified by exhaustive search only. Concrete obstruction: non-scalar/global routing + non-monotonicity of m in e(P) blocks all scalar poset invariants tested.


## Other metadata

```json
{
  "finished_at": 1793334432.4319818,
  "started_at": 1793334139.5025752
}
```
