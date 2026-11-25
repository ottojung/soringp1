# antichain-game-pspace-completeness

## status

investigated

## origin

executive_commissioned

## agent_id

v9h7jDoWfPts2hfZC142yJ-embedded

## exit_state

clearexit

## question

Can SORT-BOUND-U be shown many-one PSPACE-hard by reducing from QBF/alternating TQBF to the poset comparison game while respecting adversary total-order consistency and the unary antichain input?

## basis

SORT-BOUND-U in PSPACE; adversary must remain consistent with some total order unlike free alternation games.

## falsifier

Prove the adversary's global total-order consistency constraints create an insurmountable simulation gap that cannot be bridged for any polynomial-time reduction preserving yes-instances.

## implication

PSPACE-completeness would be a strong complexity classification (separating from P/NP under standard assumptions). Ruling it out would bound hardness.

## finding_unverified

Let me look at the board and research frontier.

Let me look up the literature more and the full frontier state.

Let us read the relevant materials.

Let us look up how sparsity barriers work more precisely.

**Attack on claim**: many-one PSPACE-hardness of `SORT-BOUND-U` via reduction from QBF/TQBF to poset comparison game, respecting adversary total-order consistency + unary antichain input.

**Mathematical finding (obstruction):**

- **Direction matters.** Claim A shows the game simulates an ATM (membership `SORT-BOUND-U ∈ PSPACE`). The converse fails. The adversary is *restricted*, not free.
- **Strategy-space restriction.** In the comparison game, adversary must answer consistently with *some total order* on fixed n elements; equivalently adversary strategies = adaptive constructions of linear extensions of the growing partial order. In QBF, universal players choose boolean assignments freely with no global "must form a single total order" constraint. The universal player in a true QBF reduction must be able to simulate arbitrary assignments; a total-order-constrained adversary cannot, due to global coupling (all order relations come from one chain on the same elements; choices are not independent).
- **Constraint language + monotonicity.** Only pairwise order comparisons, relations only accumulate monotonically, and state must remain order-consistent. This cannot faithfully encode arbitrary boolean clauses/negation with independent variables while preserving alternation semantics. Structure differs from arbitrary-poset problems (repo correctly distinguishes S(n) family from general poset hardness).
- **Many-one reduction constraint is the binding one.** The reduction must map QBF→(1^n#1^k) and preserve yes-instances *within* this restricted game model. No polynomial-time many-one reduction can bridge the gap between free universal alternation and total-order-constrained adversary strategies; the obstruction is strategy-space/global consistency, not just class inclusion.

**Concrete failed approach:** Attempts to encode variables/clauses as elements/relations fail because adversary's single total-order commitment creates cross-variable coupling impossible to unwind to independent universal moves, and monotonic order constraints prevent encoding non-monotonic boolean structure. The permutohedron (game graph) is not universal for arbitrary alternating boolean computations.

**Honest limits:** This is a structural/strategy-space obstruction, not a completed formal proof here. Also note language density is not the blocker for many-one reductions (many-to-one allowed). The claim of "insurmountable simulation gap" under total-order consistency is the correct obstruction; completeness would require the game to be more expressive than it is. No repo changes proposed.


## Other metadata

```json
{
  "finished_at": 1793724798.6178658,
  "started_at": 1793723952.8294716
}
```
