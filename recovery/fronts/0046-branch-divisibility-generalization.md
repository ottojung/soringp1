# branch-divisibility-generalization

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ddIETGVfJPaOrC5V2kMqRs-verge

## exit_state

clearexit

## question

The exact-reset realizability obstruction (odd antichain-to-star impossible by root branch divisibility) is a local condition; is there an all-n theorem characterizing exactly which poset pairs (F,F') admit an exact reset comparison tree, and does the antichain-to-any-non-chain obstruction generalize beyond stars to a wider family for certain n?

## basis

docs/research-exact-reset-realizability.md proved odd n antichain->star impossible by root mass division; docs/research-framed-certificate-frontier.md distinguishes soundness from completeness.

## falsifier

Construct an explicit infinite family of (A_n, F'_n) with integral ratio e(A_n)/e(F'_n) and all branch masses divisible but still impossible for all n in family, or prove a complete necessary and sufficient condition (e.g. divisibility of all subtree masses under some canonical strategy) that holds iff realizable.

## implication

A general divisibility theory for exact resets would clarify certificate soundness/completeness boundaries (framed DAGs) and distinguish the "extension count" from realizable transitions, directly relevant to NP-certificate questions for SORT-BOUND-U.

## finding_unverified

ives branch mass e(F)r = K e(F') r. This is divisible by e(F') iff q | K where r=p/q in lowest terms. 
- r=1/2 (antichains, complete balanced k-partites with all parts incomparable inside, diamonds, etc.): obstruction iff K odd (same arithmetic as A_n→V_n). 
- The obstruction is at root regardless of F' structure except the ratio; F need not be an antichain. The "star" is just one example of F'.

**2) Allowed comparisons are restricted by F' and by position-dependent splits.**
When F ⊆ F', only pairs incomparable in F' may be compared (otherwise the opposite branch contradicts F'). Among those, split ratios depend on positions relative to F' constraints. For F' being a union of chains (n=4, union of two chains of size 2), e(F')|e(F) with even ratio but:
- only between-chain pairs allowed; among them, only "aligned" pairs (both first or both last of chains) gave r=1/2 (divisible branches), others gave bad ratios.
- choosing a good root pair produced state G1 where all remaining allowed pairs gave non-divisible branch masses (obstruction at level 2). Bad root choices failed earlier.

This shows that even with integral even ratio and some good root choices, deeper levels can become impossible due to asymmetry created by adding F'-consistent relations.

**3) On characterization and the falsifier**
- **Necessary and sufficient (combinatorial):** exact reset exists iff there is a strategy comparing only pairs incomparable in F' such that for every state G on path, F ⊆ G ⊆ F' and e(G ∩ Ext(F')) ≡ 0 mod e(F') until G=F'. Order constraints + per-step divisibility are both required.
- **All-n characterization:** no clean compact form is obvious from above; it’s a kind of "path existence" in the poset interval [F,F'] with move constraints and arithmetic conditions.
- **Falsifier attempt:** the union-of-chains family gives a concrete case where ratio is integral (and root has good moves) but no complete strategy maintains all branch masses divisible (they become non-divisible at level 2). This is a strong indication that "all branch masses divisible" for some strategy is not satisfiable for this family even though ratio is OK - pushing toward the "impossible despite counts" side. I could not fully construct an infinite family with counts staying divisible all the way down to a clean obstruction in the time available, but the mechanism (positional asymmetry breaking balanced splits) generalizes. Proving a complete necessary and sufficient condition appears nontrivial without deeper theory of poset extension counts.

**Concrete failed/blocked approach:** trying to use complete balanced bipartite F with added internal relations failed to preserve the clean r=1/2 obstruction or create obvious infinite family because cross-part constraints force set separation. The union-of-chains case is more promising but requires tedious counting; the pattern suggests deeper obstructions are common, but a polished infinite family needs more work.

**Complexity relevance:** this distinction (extension-count divisibility vs realizable transitions, with order constraints) directly affects certificate soundness/completeness boundaries for framed DAGs. A true general divisibility theory would clarify when exact resets (no forgetting) are possible vs when forgetting (intersections) is necessary for SORT-BOUND-U certificates. No new theorem or counterexample is proposed for repository integration; the analysis above is combinatorial with references to existing docs/scripts.

## Other metadata

```json
{
  "finished_at": 1793347197.5871146,
  "started_at": 1793346559.9051116
}
```
