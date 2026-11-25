# split-critical-poset-exact-reset

## status

investigated

## origin

ai_proposal_unverified

## agent_id

BJpSyJmB5NPXNsu9c0Y8t6-languid

## exit_state

clearexit

## question

Are there posets P other than the antichain such that every nontrivial comparison from P induces a balanced extension split relative to the gcd of all possible leaf class sizes for any exact reset, and does the class of such split-critical posets form an infinite all-n family with universal exact-reset impossibility?

## basis

Root split is always balanced for antichain; docs/research-exact-reset-realizability.md branch-divisibility obstruction; need to distinguish from general-poset lower bounds with no root-transfer shown before.

## falsifier

Identify a non-antichain split-critical P admitting some exact reset to F', or show the antichain is the only root-reachable split-critical poset under the model; alternatively characterize all split-critical P and find one with an explicit exact-reset tree.

## implication

A nontrivial split-critical class would generalize the branch-divisibility obstruction beyond the antichain root and constrain which reachable states can appear as exact-reset leaves in any tight certificate for evaluating S(n).

## finding_unverified

ain such that every nontrivial comparison from P induces a balanced extension split relative to the gcd of all possible leaf class sizes for any exact reset, and does the class of such split-critical posets form an infinite all-n family with universal exact-reset impossibility?
> FALSIFIER: Identify a non-antichain split-critical P admitting some exact reset to F', or show the antichain is the only root-reachable split-critical poset under the model; alternatively characterize all split-critical P and find one with an explicit exact-reset tree.
> COMPLEXITY IMPLICATION: A nontrivial split-critical class would generalize the branch-divisibility obstruction beyond the antichain root and constrain which reachable states can appear as exact-reset leaves in any tight certificate for evaluating S(n).
> EVIDENCE: Root split is always balanced for antichain; docs/research-exact-reset-realizability.md branch-divisibility obstruction; need to distinguish from general-poset lower bounds with no root-transfer shown before.
> If resuming after an infrastructure failure, inspect earlier work and avoid repeating side effects or claims. 
> On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof."

Let us think systematically.

**Mathematical finding (disproof of the proposed hypothesis):**

Weak orders form a large class with the split-critical property. Every nontrivial comparison in a weak order is within some incomparability block (transitive incomparability classes), and by block permutation automorphisms gives a balanced extension split (exactly half). The antichain A_n is W(1,n); W(k,m), k≥2 are root-reachable split-critical posets different from antichain.

Crucially, these do **not** have universal exact-reset impossibility. For any weak order P=W(k,m), we can do exact resets to intermediate states obtained by resolving comparisons inside blocks while keeping other blocks intact (e.g. W(2,2) on {a1,a2,b1,b2} with all between-block relations can be reset in 1 comparison a1 vs a2 to F' = {a1<a2} ∪ all between-block relations, giving leaf classes of size e(F')=2 partitioning e(P)=4). The branch-divisibility obstruction requires that for the chosen target F', e(F') divides every branch size along all paths; this condition is satisfiable for many F' (intermediate states, chains) for weak orders.

Also "gcd of all possible leaf class sizes for any exact reset" interpreted as gcd{e(F') | ∃ exact reset P→F'} gives 1 for all finite posets since sorting to a chain is always possible (e(chain)=1). The obstruction is target-specific (as in A_n→star for odd n), not universal to the class. So the hypothesis that only antichain is root-reachable split-critical with universal exact-reset impossibility is false; weak orders provide an infinite all-n family of split-critical posets that admit explicit exact resets.

**Failed/obstructed approach:** Trying to make the obstruction universal fails because weak orders remain "resettable" along their symmetric block structure and always admit trivial resets to chains. The key distinction is not just "every nontrivial comparison gives balanced split" but whether that symmetry is preserved under comparisons or destroyed (antichain loses symmetry immediately; weak orders can preserve block symmetry). This matches the existing note's point that you need to check branch divisibility recursively and that asymmetric states break the obstruction.


## Other metadata

```json
{
  "finished_at": 1793698026.8829517,
  "started_at": 1793693039.4801533
}
```
