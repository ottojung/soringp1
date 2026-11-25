# fo-lfp-p-membership

## status

investigated

## origin

ai_proposal_unverified

## agent_id

g0DAnKQkZ8Jg3CGt6WnodM-notable

## exit_state

clearexit

## question

Can SORT-BOUND-U be defined by a fixed-point logic formula (FO(LFP)) on ordered structures with polynomial-time data complexity, giving a new P-membership route distinct from explicit algorithmic recurrences?

## basis

PSPACE capture (Immerman–Vardi) gives FO(PFP); FO(LFP) captures P. Research plan asks whether FO(LFP) definition exists for SORT-BOUND-U. AGENTS.md states realistic outcomes include membership in NP/coNP/P via succinct certificates or other routes.

## falsifier

Show that any FO(LFP) definition of the minimax height condition for the sorting game requires exponential growth on ordered structures or is equivalent to the game alternation (PSPACE) by known descriptive complexity theorems.

## implication

An FO(LFP) (or Datalog) characterization would place exact comparison counting in P in the descriptive complexity sense and give a new algorithmic avenue; a barrier would sharpen the alternation/PSPACE connection.

## finding_unverified

requires either (a) embedding all 2^(Θ(n²)) encodings into the structure (domain/tuple space exponential in N), which destroys polynomial-time data complexity relative to the unary input length, or (b) restricting to a quotient (isomorphism classes, canonical forms) – but as shown in prior work on root-reachable equivalences/certificates, no known polynomial quotient is complete for all optimal strategies and you risk losing soundness/completeness of the exact threshold.

3. **Alternation vs least fixed point.** FO(PFP) captures PSPACE precisely because it can express the alternating reachability of the game graph (sorter ∃, adversary ∀). FO(LFP) is the least fixed point (monotone, giving a kind of inductive closure) corresponding to P. The comparison game is an alternating game whose "move graph" on poset states is exponential; collapsing that alternation to a monotone least fixed point over a poly-sized input structure is not possible by known descriptive complexity theorems. If you force the structure to be exponential to be faithful, the complexity correspondence becomes trivial/meaningless relative to input length N. This matches the falsifier: equivalence to game alternation (PSPACE) or exponential growth on ordered structures.

### Distinctions (important)
- **Soundness vs completeness:** A formula might be sound on some restricted state space or complete for a class of strategies, but faithfulness to the *exact* minimax over all posets is the issue. This is the same gap seen in certificate work (sound checker ≠ complete all-n certificate).
- **General posets vs antichain root:** The problem is not "hardness over arbitrary posets" – it's the representation of the *game graph* derived from the fixed comparison model starting at the antichain, encoded on a unary structure of size N.
- **Complexity classes:** FO(LFP) would imply P (data complexity), FO(PFP) implies PSPACE. The obstruction prevents the faithful FO(LFP) route; FO(PFP) is the natural descriptive complexity match for the known PSPACE membership via ATM.

### Concrete failed approach / exact obstruction
Any attempt to write an FO(LFP) formula that directly inducts over "winning positions" by quantifying over poset states will either (i) only quantify over elements/tuples of the input structure and miss exponentially many reachable posets (incomplete/wrong for exact S(n)), or (ii) quantify over encoded posets requiring exponential tuple space (exponential structure growth) breaking polynomial-time data complexity. No known polynomial quotient preserves exact minimax faithfulness. This is a representation/faithfulness obstruction, not a claim that no formula exists in some non-standard sense.

### Limits
- This is an obstruction argument, not a formal disproof in the sense of a theorem with full details. A rigorous proof would need to make the "faithful encoding" notion precise and rule out all possible encodings.
- It doesn't forbid a non-faithful characterization, but non-faithful would not give a tight complexity correspondence to the exact minimax/S(n) as defined.
- No repository/Lean changes are warranted; the existing minimax correspondence is combinatorial and remains correct.

**Bottom line:** The falsifier holds. An FO(LFP) (P) route is blocked by exponential state space / faithfulness + the alternation/PSPACE barrier; FO(PFP) aligns with the established PSPACE membership. This sharpens the alternation/PSPACE connection rather than giving a new P-membership route.

## Other metadata

```json
{
  "finished_at": 1793438876.6321945,
  "started_at": 1793438599.0990057
}
```
