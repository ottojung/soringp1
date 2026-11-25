# comparison-restriction-hardness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

eBmcmh9EfY77vBLEflIdeM-soul

## exit_state

clearexit

## question

For pairwise comparison tests (a restricted subclass of all possible tests), is the minimum-height decision tree problem NP-hard for the sorting function class, or does the total-order constraint make computing S(n) polynomial-time equivalent to easier problems despite arbitrary-test NP-hardness?

## basis

Hyafil–Rivest and Laber–Nogueira show arbitrary-test minimum-height trees are NP-hard/NP-hard to approximate; AGENTS notes sorting is restricted to pairwise comparisons and sparsity gives Mahaney barrier, but the comparison-restriction hardness gap is unaddressed.

## falsifier

Give a polynomial-time reduction from an NP-complete problem to SORT-BOUND-U under many-one reductions with correct unary encoding, or prove a complexity-theoretic barrier that blocks such a reduction given the comparison-model restriction and sparsity constraints.

## implication

NP-hardness under many-one reductions would force P=NP by sparsity of SORT-BOUND-U; polynomial-time tractability would separate the comparison-restricted model from arbitrary tests and place computing S(n) in P.

## finding_unverified

arisons without changing the test family. The “total-order constraint” (sorting all permutations, antichain initial state) is the opposite regime of arbitrary posets. (docs/research-hardness-boundaries.md §§1-2)

3. **Test-family restriction + structure.** Pairwise comparisons generate only the comparison graph/order constraints; the state space is the weak Bruhat order. There’s no known way to encode arbitrary 3-SAT/EC3 subset constraints as comparison outcomes that force a particular comparison tree structure of bounded height equivalent to the NP instance, while keeping `(n,k)` polynomial in instance size under *unary* encoding. Also `e(P)` doesn’t determine `S(P)` (Prop 5.1) so you can’t just count linear extensions. Cardinal et al. give polytime *constant-factor* approximation of comparisons, not exact `S(P)`. No primary source shows NP-hardness for exact minimum-height comparison trees on the sorting (antichain) class. (docs/research-hardness-boundaries.md §§3,5)

4. **P/log nonuniformity is trivial.** `SORT-BOUND-U ∈ P/log` by monotonicity of `n+S(n)` (Thm 4.3) — advice is just the cutoff, computable nonuniformly; this matches sparsity and is consistent with tractability/non-tractability without settling either.

**Attempted refutation (concrete):**
- Looked for reductions: cstheory-like leads mention “hardness of optimal sorting” but no primary reduction found (docs/research-hardness-boundaries.md §6). 
- Tried to imagine gadgeting EC3 into comparisons: comparisons only give pairwise order; to force subset tests you need to encode membership — seems to require either exponential blowup in `n` relative to formula size or to lose the “all permutations” (total order target) constraint. Also need exact height equivalence.
- Checked small witnesses: information bound non-tightness is the issue, not counting hardness.

**Conclusion (honest):**
- **No polynomial-time many-one reduction from an NP-complete problem to `SORT-BOUND-U` is known.** Given (1)-(3), such a reduction is *highly implausible* under the pairwise-comparison restriction + total-order constraint. 
- **Sparsity gives a strong conditional barrier:** any many-one NP-hardness would force `P=NP` (Mahaney). Combined with comparison-model restriction (no arbitrary subset tests, target is all permutations), this blocks the “arbitrary-test NP-hardness lifts directly” intuition. 
- **The comparison-restriction vs arbitrary-test gap is real.** Arbitrary tests ⇒ NP-hard (Hyafil–Rivest); restricting to pairwise comparisons on the sorting class is a severe restriction with no known transfer. Whether exact `S(n)` is polynomial-time computable (uniform) remains open in the sense no classification exists, but it’s *not* the same as arbitrary-test hardness and is constrained by sparsity/P/log.

**Exact obstruction to falsifier:** I cannot produce a many-one reduction, and I cannot produce an unconditional proof that none exists — only barriers (Mahaney + model restriction). The decisive obstruction is: to satisfy many-one reduction you must encode arbitrary NP constraints into pairwise comparisons over a total order instance with polynomial blowup in unary input length; Hyafil–Rivest gadgets don’t survive this restriction, and sparsity means success would be a major complexity consequence (P=NP). No constructive reduction or known theorem rules it out absolutely, but all evidence points to the barrier holding. No repository changes made (no new theorem/counterexample meeting the gate).

## Other metadata

```json
{
  "finished_at": 1793536108.909555,
  "started_at": 1793535954.6583936
}
```
