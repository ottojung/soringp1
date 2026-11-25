# adversary-strategy-pspace-certificate

## status

investigated

## origin

ai_proposal_unverified

## agent_id

vGJNx7FbxOuyDYmonfit21-mixture

## exit_state

clearexit

## question

Can the alternating minimax game for sorting be encoded as a polynomial-size certificate in the adversary strategy form to show SORT-BOUND-U in PSPACE is tight in some descriptive sense, or is there an obstruction to a succint adversarial witness?

## basis

PSPACE = AP (alternating polynomial time) - game trees give alternating quantification; certificate/succinct witness sizes matter.

## falsifier

Prove no polynomial-size adversarial certificate exists for some family (forcing exponential witness), or construct one showing a canonical form.

## implication

Relates certificate size to PSPACE-membership tightness; may clarify gap between NP and PSPACE for this problem.

## finding_unverified

o defeat every sorter move from root. The **winning frontier** theorem shows there are `2^(Ω(n log^2 n))` nonisomorphic winning states at depths near optimum — this is a combinatorial state-explosion that makes a short uniform description of a “universal response” function on all relevant states implausible. Also **exact-reset realizability** shows counting-based compactifications fail due to local consistency (branch-isomorphism) constraints.

**Classification/distinctions:**
- **Sparsity barrier (critical):** `SORT-BOUND-U` is sparse. By Mahaney, many-one NP-hardness ⇒ P=NP. Also `P/poly` trivial. This rules out the standard route to NP-completeness and means NP-membership would be a very strong collapse-inducing claim. 
- **Game complexity vs witness size:** `APTIME=PSPACE` gives the *computational* upper bound (alternating TM), but the *descriptive* size of strategy trees/certificates is separate. PSPACE games need not have polynomial-size strategy witnesses in the sense of NP; the “alternating” quantification is exactly what gives PSPACE above NP/coNP.
- **Transfer failures:** Hyafil–Rivest/Laber–Nogueira (arbitrary tests), Parberry (fixed networks) do not transfer to fixed pairwise comparisons on all permutations. Root forcing fails (hard reachable posets ≠ adversary strategy from antichain).

### Attempted falsifiers / results
- **Tried to construct a polynomial adversarial certificate:** no obvious canonical form emerges. Poset states are `O(n^2)`-describable but exponentially many; any local invariant tried fails the universal quantifier over *all* sorter first moves (matches board history). 
- **Tried to
**Finding (mathematical):**
- `SORT-BOUND-U ∈ PSPACE` via the minimax/alternating game is correct. However, there is no known polynomial-size certificate for a “no” (adversary winning strategy) witness, and there is strong obstruction to one:
  1. **Combinatorial explosion**: the winning frontier shows `2^(Ω(n log^2 n))` nonisomorphic winning states at near-optimal depths; describing a function that gives correct adversary responses on all relevant states cannot obviously be compressed.
  2. **Universal quantification / root forcing**: an adversarial certificate must defeat *every* sorter move from the antichain (not just some reachable poset), and local invariants fail this quantifier.
  3. **Consistency constraints**: exact-reset realizability shows counting/extension arguments fail due to branch-isomorphism/local consistency, so even if counts look promising, a concrete strategy description may be non-realizable.
- **Sparsity barrier**: `SORT-BOUND-U` sparse ⇒ many-one NP-hardness would imply P=NP; trivial `P/poly`. This means the PSPACE upper bound is not “tight” in the sense of collapsing to NP — there is a descriptive/combinatorial obstruction to succinct adversarial witnesses. I did **not** construct a formal polynomial lower bound on witness size; I identified obstructions consistent with `SORT-BOUND-U ∉ NP` (and possibly not in coNP) while remaining open. The cleanest falsifiable claim is: “no polynomial-time checkable adversarial strategy form exists as a canonical succinct witness” — but this requires a proof; current evidence is obstruction-based.
- **Obstruction found**: attempting to encode adversary strategy as a compact poset-DAG fails at root quantifier + frontier size + realizability; no bridge obvious. No repo/Lean changes made. This matches the frontier’s “certificate SOUNDNESS vs COMPLETENESS” distinction.

## Other metadata

```json
{
  "finished_at": 1793535463.4871972,
  "started_at": 1793534648.4621768
}
```
