# kphase-alln-linear-miss

## status

investigated

## origin

ai_proposal_unverified

## agent_id

TGt74YRvz9N0wH2cu2SV2J-propped

## exit_state

clearexit

## question

For every fixed integer k >= 1, does there exist c_k > 0 such that for all sufficiently large n, every k-phase FO(TC)-expressible comparison strategy incurs worst-case comparisons >= S(n) + c_k n, so no fixed-phase strategy achieves exact S(n) for all n?

## basis

Two-phase linear miss mass τ(n)=Ω(n) from fo-tc-two-phase-n8-verify-20261027; k-phase generalization noted but unresolved in two-phase-generalizations-alln ledger entry and SoringP1/AGENTS.md focus on root/adversary structure.

## falsifier

Exhibit for some fixed k an all-n family of k-phase strategies achieving S(n) exactly, or prove the miss mass becomes sublinear for some k>=3 while it is known linear for k=2.

## implication

A universal linear-miss theorem for all fixed k would rule out the entire fixed-phase/finite-rule class as a route to exact all-n optimality and NP-membership via that normal form, tightening barriers beyond the two-phase case.

## finding_unverified

n; the known data is consistent with δ(n)=0 infinitely often even if τ(n)=Ω(n).
2. **Try to imagine a k-phase exact family.** For example, use different strategies by residue classes or find a family where for each fixed k some k-phase construction hits S(n) at all n? Unclear. Insertion sort is effectively n-phase in some view and not optimal; merge sort is log n phases. To be exact for all n with fixed k seems to require the phase structure to adaptively achieve the optimal increment d(n) regardless of whether it equals ceil(log2 n) — the sort-then-insert forces the specific increment ceil(log2 n) plus S(n-1); a more general k-phase strategy might be able to do better by not sorting n-1 completely first. The two-phase barrier is for that specific structure; generalizing is nontrivial. I see no obvious counterexample, but also no proof of impossibility for general k-phase.

**Concrete obstruction / honest limit:**
- **For k=2:** The strongest established result is *cumulative* linear miss mass for the canonical two-phase schema; *uniform per-n* linear miss for all sufficiently large n is not proved by current evidence (non-monotonicity + unknown behavior of d(n)=S(n)-S(n-1) relative to ceil(log2 n), with Sergeev only giving o(n) excess over info bound). The question’s stated “evidence” says “linear miss mass τ(n)=Ω(n)” which matches cumulative, but the FRONT states the per-n form — that’s a slight mismatch in quantification. I cannot disprove the per-n claim from known results; I also cannot prove it.
- **For fixed k>=3:** No rigorous generalization exists in the inspected work. Any generalization of the sort-then-insert argument to k phases would need to show that every k-phase decomposition forces some increment/loss >= c_k per element regardless of structure; this is reminiscent of round complexity lower bounds in some models but achieving *exact* optimum S(n) (not just asymptotic) is much tighter. I found no published proof or refutation in this repo. The barrier is the lack of a general theory of optimal increments under fixed-phase constraints.

**Distinguish certificate soundness vs completeness:** The two-phase witnesses are *sound* (verified on all n! orders, constant-rule programs, independent cross-check) and show the schema is *not complete* for exact S(n) at those n; cumulative Ω(n) is a sound aggregate property. But “completeness” of the *entire fixed-phase class* for all-n exactness is the opposite — we want to know if fixed-phase class is complete for achieving S(n). The obstructions above speak to incompleteness of specific schemas; a general class-incompleteness (and per-n linear miss) would be stronger.

**Recommendation (no repo changes):** Do **not** claim a proof or disproof. The precise mathematical gap is quantification (cumulative vs per-n) and generalization (schema vs all k-phase). A serious attempt to disprove would require either constructing an explicit all-n k-phase exact family (I see no candidate) or proving d(n) >= ceil(log2 n) + c_k n eventually for all n under phase constraints (I see no argument). The cleanest honest report is: for k=2 only cumulative Ω(n) is established for the canonical schema; uniform per-n linear miss for all large n is unproven; generalization to fixed k>=3 is unresolved with no known refutation or proof in primary sources inspected.

No Lean changes, no files created — this is a negative/inconclusive mathematical finding consistent with the repo’s “report honest limits” policy.

## Other metadata

```json
{
  "finished_at": 1793586638.5613668,
  "started_at": 1793585213.6217823
}
```
