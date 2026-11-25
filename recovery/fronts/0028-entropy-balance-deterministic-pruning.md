# entropy-balance-deterministic-pruning

## status

investigated

## origin

manual_executive

## agent_id

rQWBScnqn0IPFpo1E0OHJn-shortness

## exit_state

clearexit

## question

Can Sergeev's entropy-balance/o(n) surplus observation be turned into a sound deterministic worst-case pruning rule for root-optimal search that provably cuts the 2^{Theta(n log^2 n)} winning frontier without excluding any height-S(n) optimal strategy?

## basis

docs/research-plan.md and board entropy-balance notes; average-case fact needs worst-case soundness proof.

## falsifier

Show any proposed local entropy-balance potential is either unsound (prunes some optimal strategy) on a concrete family, or preserves an exponential class family equivalent to isomorphism classes.

## implication

A verified sound pruning rule would give a practical path toward better exact evaluators and clarify barrier structure.

## finding_unverified

me threshold derived from C(n)=log2(n!). Since V(P) not determined by e(P), adversarial families exist in principle where optimal first move is locally imbalanced (or balanced branches are all suboptimal). No finite-threshold rule derived from extension counts is obviously sound for all n; proving soundness would require showing the threshold is implied by V(P) <= k for all cases — contradicts n12-nontightness / proxy vs value.
- **“Typical path” filter:** Restricting to paths where running entropy surplus stays o(n) would be an *admissible* heuristic only if every height-S(n) strategy is “typical” — false by minimax (strategies can be adversarial to balance; also different optimal strategies exist). Unsound in general.
- **Orbit+balance hybrid:** Aut orbit pruning already gives no exponent gain; adding balance (also class-invariant in effect) cannot create exponent gain against nonisomorphic class family. Obstruction (b).
- **Approximate e(P):** Even if computable, approximation errors make worst-case soundness impossible without huge safety margins that would prune nothing useful, or margins that become unsound. Exact e(P) is #P-hard in general for posets and computing it at scale is infeasible; worst-case soundness proof is unclear.

### Verdict
**No sound deterministic worst-case pruning rule based solely on a local entropy-balance potential is obvious, and there is a strong mathematical obstruction.** 

- **Against (b) (frontier cut):** Any potential invariant under isomorphism/Aut orbits preserves the 2^((1/4-o(1)) n log^2 n) nonisomorphic winning states identified by the winning-frontier barrier; local balance metrics of extension-count type are orbit-invariant. This is a direct obstruction to cutting that frontier.
- **Against (a) (soundness):** Since V(P) (minimax height) is not determined by e(P), a rule “prune imbalanced moves” is a greedy proxy with no worst-case guarantee. The average o(n) surplus is not a necessary condition on all height-S(n) strategies. Proving soundness for all n appears false in principle without additional strong invariants that don’t follow from entropy alone.

**Honest limits:** I did not construct an explicit n,k,poset counterexample on disk here (the user asked to try seriously to disprove; the obstruction is structural from existing results). A concrete counterexample would require either (i) finding a poset family where some height-S(n)-optimal strategy makes a locally “imbalanced” first move (by any natural threshold) or (ii) demonstrating the class-invariance explicitly. The existing literature already gives the ingredients (n12 nontightness + winning frontier). Without running large search, the structural disproof is: (b) is a proven obstruction for class-invariant potentials; (a) is obstructed by proxy/value mismatch. Either way, the proposed front is not viable for a *sound* worst-case rule that cuts the frontier.

**Complexity implication note:** A verified *sound* pruning rule would be interesting, but “verified sound” is the hard part here; the barrier structure suggests you cannot get exponent reduction from balance alone because the obstacle is class count (isomorphism/winning states), not “imbalance”. Also ties back to certificates: you can’t prune solutions.

**No repository/Lean changes proposed.** This is a negative/obstruction result, not a substantive new theorem ready for kernel-check without a concrete counterexample or a formal invariant. I report limits honestly as requested.

## Other metadata

```json
{
  "finished_at": 1793317666.1010628,
  "started_at": 1793317536.8631458
}
```
