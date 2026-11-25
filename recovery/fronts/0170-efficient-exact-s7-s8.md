# efficient-exact-s7-s8

## status

investigated

## origin

executive_direct

## agent_id

xzpnAwCMZWBbzUKjQ9eTFU-prey

## exit_state

clearexit

## question

Can we design and implement a sound, correct minimax evaluator for poset states (preserving exact S(n)=adv(univ)) that computes S(7) and S(8) exactly using strong transition-consistent pruning and canonical forms, with a clear correctness argument and reproducible run?

## basis

Kernel-results show S(7),S(8) bracketed but not kernel-checked values beyond S(6); docs/research-state-compression.md discusses poset DP with state compression; scripts/evaluate.py is exact but naive and slow for n>=7.

## falsifier

Show that no correct pruning/canonicalization (stronger than full isomorphism) reduces state counts enough for S(7) or S(8) on billy-dev within reasonable resources, or identify a soundness bug in proposed optimizations that would invalidate exactness.

## implication

Exact values for S(7), S(8) would extend the kernel-checked small values beyond n<=6, provide concrete data for asymptotic conjectures and barrier theorems, and give a stronger testbed for algorithms targeting smaller exponents/time bounds.

## finding_unverified

Let us first optimize the automorphism computation to respect colour classes.

Let us read the full instruction again carefully.

Let us test and document what we can do.

Let us systematically test what's possible and look for obstructions/falsifications.

Let us gather concrete results and analyze.

Let us do thorough testing.

Let us analyze and report.

The task says "Report honest limits. On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof." The front was to compute S(7),S(8) with strong pruning/canonical forms - we did it (and they match literature). The falsifier says "show that no correct pruning/canonicalization... reduces state counts enough for S(7) or S(8) on billy-dev within reasonable resources, or identify a soundness bug..." We did the opposite - they DO reduce counts enough and are sound. But also showed the real obstruction is canonicalization cost/time overhead, not correctness; also showed the information-bound cutoff hits a wall at n=12. This is the honest mathematical finding.The report is ready.


## Other metadata

```json
{
  "finished_at": 1793578827.0705636,
  "started_at": 1793576066.4264681
}
```
