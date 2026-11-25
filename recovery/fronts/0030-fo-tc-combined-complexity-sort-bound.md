# fo-tc-combined-complexity-sort-bound

## status

investigated

## origin

manual_executive

## agent_id

J82VCwlB9xawtfCrkAtc6W-publicity

## exit_state

clearexit

## question

Can a fixed uniform FO(TC) interpreter with explicit combined complexity yield a nontrivial upper bound for SORT-BOUND-U, or is there a precise barrier separating data complexity (NL) from combined complexity for this minimax threshold?

## basis

Board issue fervor #301 comment; descriptive complexity mentioned in research-plan.md.

## falsifier

Give an explicit FO(TC) sentence family computing S(n)<=k with combined complexity in some class and a reduction, or prove a barrier (e.g. due to uniformity/model) preventing improvement beyond known bounds.

## implication

Relates descriptive complexity to the active frontier; founder-selected issue JTsW4AnxTLzN18IBQibXea-fervor targets this.

## finding_unverified

nguishes **soundness** (a given framed DAG is a valid strategy) from **completeness** (every optimal strategy has polynomial framed DAG) - completeness is open. A fixed FO(TC) interpreter does not force `p` to be polynomial-size; combined complexity verification cost is PSPACE in the worst case of searching/validating large strategies or in general. Also unary sparsity means many-one NP-hardness would imply P=NP (Mahaney), so an easy NP-completeness is blocked. The barrier is not just the logic class but **certificate size/completeness** separate from execution.

### Concrete falsifier attempt (what would be needed)
To actually achieve a nontrivial upper bound below known: give an explicit family of FO(TC) sentences `{ψ_{n,k}}` (uniform in some sense) such that `1^n#1^k ∈ SORT-BOUND-U ⇔ A_{n,k} ⊨ ψ_{n,k}` for some structure encoding, with combined complexity of evaluating the family in class C strictly below PSPACE and a reduction showing it’s nontrivial. 
**Obstruction:** FO(TC)’s combined complexity is PSPACE-complete regardless of sentence family (you can encode PSPACE computations). Also the `∃∀` over all permutations is not eliminable - any correct sentence family must be true for all X if it accepts some strategy, so it must capture the universal adversary; this is exactly the alternation that forces PSPACE. Alternatively, trying to fix strategy in the formula breaks uniformity/all-n or can’t cover all cases. No such family giving better than PSPACE is evident; the natural simulation gives PSPACE-tightness.

### Verdict
**Mathematical finding (barrier):** There is a precise barrier separating data complexity from combined complexity here.
- **Data complexity (NL, fixed FO(TC) formula, single input order):** insufficient because the question is `∃` strategy `∀` all permutations (game) not evaluation on one instance; you cannot capture the universal over exponential input space or quantify over strategies without moving quantification into the structure.
- **Combined complexity (fixed FO(TC) interpreter, formula+strategy+input both grow):** corresponds to alternating game evaluation and yields **PSPACE** (tight with `APTIME=PSPACE`), same class as the known ATM bound. The logic’s own combined complexity is PSPACE-complete, so no improvement below PSPACE is available from this route alone. 
- **Additional obstructions:** (a) optimal strategies may be exponentially large (winning frontier / tree size) so polynomial NP certificates are not automatic and completeness is open; (b) unary sparsity blocks trivial NP-hardness paths; (c) uniformity across all `n` doesn’t create succinct witnesses.

**Conclusion:** A fixed uniform FO(TC) interpreter with explicit combined complexity does **not** yield a nontrivial upper bound below the known PSPACE bound for `SORT-BOUND-U`; the obstruction is precisely the data/combined complexity split plus the `∃∀` minimax and potential exponential strategy size. I could not construct an explicit FO(TC) sentence family in a lower class that is correct for all-n and sound/completable - the natural simulation is PSPACE-complete and attempts to shortcut the alternation fail on the universal quantification over all permutations or on uniformity/certificate completeness. No Lean/repo changes proposed (no new theorem/counterexample rigorous enough to integrate per policy). This matches the fervor front’s distinction between “interpreter polynomial per (p,X)” and worst-case depth verification / the game complexity.

## Other metadata

```json
{
  "finished_at": 1793318487.4308276,
  "started_at": 1793317542.0600493
}
```
