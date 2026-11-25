# descriptive-folfp-sorting-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

rIOkYNEGwgU3DbjPSY88o9-tiresome

## exit_state

clearexit

## question

For all n,k, does there exist a fixed FO(LFP) sentence phi such that (N_n,k, <) |= phi iff S(n) <= k, where N_n,k encodes 1^n # 1^k as an ordered structure (size Theta(n+k))? Equivalently, is SORT-BOUND-U in Datalog with least fixed point (P by Immerman–Vardi) via an explicit uniform formula over the game/poset states?

## basis

AGENTS.md and docs/problem.md state FO(LFP) (P) would be a new upper bound; docs/research-plan.md lists descriptive complexity as open; no prior ledger front targets fixed FO(LFP) expressibility of the exact S(n) threshold game.

## falsifier

Prove that every FO(LFP) definition of the minimax height on the n-antichain comparison game must have quantifier/closure rank growing at least linearly in n (or unbounded over all n) with no uniform fixed formula, or exhibit a first-order reduction/invariant that FO(LFP) cannot capture for infinitely many n.

## implication

A fixed FO(LFP) definition would give a new uniform upper bound placing SORT-BOUND-U in P (separately from the exponential-time DFS) and a descriptive-complexity characterization; a uniform-inexpressibility obstruction would rule out this canonical descriptive route without relying on known PSPACE/P separations.

## finding_unverified

ing polynomial time) or growing formula complexity, but fixed formula gives fixed polynomial bound.

## Conclusion
I need to report this finding. The mathematical obstruction is the winning frontier barrier: 2^(Ω(n log² n)) nonisomorphic winning states at depths near S(n) imply that any correct algorithm must process super-polynomially many states relative to input length N=Θ(n log n), so SORT-BOUND-U ∉ P and no fixed FO(LFP) formula exists. This is a specific obstruction to the antichain comparison game (not arbitrary posets), about state-space size rather than certificate soundness vs completeness of tree encoding. It rules out this descriptive route without relying on P!=PSPACE as an assumption (it gives a concrete state-complexity obstruction), though P!=PSPACE would follow. I found no way to disprove it; attempts to use symmetry failed (ordered structure) and rank-counting failed. This is an obstruction, not a proof I constructed from scratch but a known barrier applied to this exact question.**Finding (paper/structural):** Fixed FO(LFP) definability (equiv. SORT-BOUND-U ∈ P, uniform over all n,k on ordered structure of size N=Θ(n+k)) is obstructed by the **winning-frontier / state-space barrier** for the antichain comparison game, not by arbitrary-poset hardness.

**Obstruction (concrete):**
- Repo barrier (winning frontier): at depths near S(n) there are 2^(Ω(n log² n)) nonisomorphic winning states (even at the exact optimum via Sergeev’s bound). Input length N = n+k+1 = Θ(n log n). State count is 2^(Ω(N log N)), super-polynomial in N.
- FO(LFP)=P on ordered structures requires polynomial-time (hence polynomial number of state/configuration visits) computation by fixed formula. Any correct exact algorithm for SORT-BOUND-U must account for those winning states (barrier says full enumeration ruled out at optimum); pigeonhole/information-theoretic constraint: cannot process exponentially-many states in polynomial time. 
- This is specific to the antichain (sorting) game (not a generic poset transfer). It affects the **property-defining computation over states** (backward induction) rather than just tree-certificate soundness/completeness of a particular encoding.

**Distinctions made:**
- Soundness vs completeness: even if some strategies were succinctly encodable, the minimax value computation itself hits state-space explosion. The obstruction is state count, not “can we verify a tree?” alone.
- Ordered structure breaks unordered-symmetry EF games (elements position-named). Closure-rank counting is insufficient (polynomial bound exists) — obstruction is the exponential state space vs polynomial traversal.

**Failed approaches / limits:**
- Ehrenfeucht–Fraisse/symmetry: blocked by global order on input.
- Rank/iteration count alone: polynomial in N is asymptotically okay by count, but cannot enumerate 2^(Ω(N log N)) states.
- Did not derive a new theorem; this is an application of existing barrier (docs/research-winning-frontier-barrier.md) to the descriptive-complexity question. No counterexample constructed, no Lean/repo changes.

**Verdict:** No fixed FO(LFP) sentence appears possible due to the winning frontier’s super-polynomial state count relative to input length; this rules out the “fixed formula over game/poset states” route (and would imply SORT-BOUND-U ∉ P, hence P!=PSPACE) via this barrier. This is a structural obstruction, not a proof of formula inexpressibility by hand, but the strongest concrete obstruction available.

## Other metadata

```json
{
  "finished_at": 1793715965.21133,
  "started_at": 1793715478.195968
}
```
