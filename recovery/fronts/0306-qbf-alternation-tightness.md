# qbf-alternation-tightness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

1AOoTHQm48MlQSPUFu5qn0-savior

## exit_state

clearexit

## question

For the budgeted alternating/positional game characterizing SORT-BOUND-U, is the minimal all-n alternation depth Ω(n) or can it be shown O(n / polylog n) for some uniform ATM recognizing SORT-BOUND-U on unary input?

## basis

SORT-BOUND-U in PSPACE via alternating TM (research-certificates-barriers); blocked prior on ATM alternation but no tight all-n alternation bound exists.

## falsifier

Prove for all large n that every uniform ATM deciding SORT-BOUND-U in time polynomial in N=n+k+1 requires alternation depth Ω(n / polylog n) on some input, or construct one with depth o(n / polylog n) for all n.

## implication

Tight alternation bounds would clarify the ATM-level position below PSPACE without relying on circuit lower bounds and without conflating numeric n with binary length.

## finding_unverified

 to prove `Ω(n/polylog n)` for every uniform polynomial-time ATM — out of scope / separation-equivalent
Assume for contradiction a uniform ATM decides `SORT-BOUND-U` in time `poly(N)` with alternation depth `o(n/polylog n)` on all relevant inputs, or more strongly alternation depth `0`/deterministic polynomial time. In particular, if `SORT-BOUND-U ∈ P`, there is a deterministic polynomial-time TM, i.e. alternation depth `0` suffices. Therefore any unconditional theorem of the form

> for all large `n`, every uniform ATM deciding `SORT-BOUND-U` in time `poly(N)` requires alternation depth `≥ g(n)` on some input, with `g(n) ≥ 1` (and certainly with `g(n)=Ω(n/polylog n)`)

implies `SORT-BOUND-U ∉ P`, which would imply `P ≠ PSPACE` by the project’s established `SORT-BOUND-U ∈ PSPACE`. This is an open separation and is out of scope for current methods. `[deduction from problem.md/AGENTS.md “Realistic outcomes”]`

Even weaker “not in low alternation” conclusions (e.g. forcing superconstant depth while staying in polytime, if interpreted as excluding PH placement in strong forms) are not supported by known techniques for a natural PSPACE tally language in `P/poly`; circuit/nonuniform methods do not separate it from `P`. No all-`n` ATM alternation-depth lower bound was obtained. `[barrier; not a proof]`

## Falsification status
- **`Ω(n)` (informal) vs `O(n/polylog n)` as stated in front:** the direct `G(n,k)` ATM gives `Θ(n log n)` on threshold instances, so it refutes `O(n/polylog n)` *for that ATM* only; it does **not** refute/establish the claim for the **minimal** all-`n` alternation depth over all uniform polynomial-time ATMs.
- **Falsifier arm “`Ω(n/polylog n)` for every uniform polytime ATM”:** not proved; proving it would imply `P ≠ PSPACE` (open). I did not find a restricted model where it becomes provable without that consequence, except trivial observations (direct simulation is already `Ω(n log n)`).
- **Falsifier arm “construct depth `o(n/polylog n)` for all `n`”:** not constructed. Adaptivity of exact comparison sorting blocks naive round-compression; succinct complete strategy guessing is unavailable (soundness ≠ completeness). No counterexample ATM found.

## Mathematical finding / precise obstacle (honest limit)
**Deduction (paper-level, checkable):** The budgeted alternating game `G(n,k)` yields a uniform ATM for `SORT-BOUND-U` with `time O(N³)`, `space O(n²)`, and alternation depth `O(k)`. On the information-tight threshold regime `k = Θ(S(n)) = Θ(n log n)`, this is `Θ(n log n)=ω(n/polylog n)` and `Ω(n)`. This is an **upper-bound witness** for the direct game characterization, not a minimax alternation-depth lower bound for all ATMs.

**Exact obstacle:** Any unconditional `Ω(n/polylog n)` alternation-depth lower bound (indeed any `≥1`) for *all* uniform polynomial-time ATMs deciding `SORT-BOUND-U` would separate it from `P` and therefore prove `P ≠ PSPACE`; conversely any `o(n/polylog n)` polynomial-time ATM would be a new structural upper bound and must overcome the sequential `∃/∀` dependency of adaptive comparisons (or supply a complete succinct representation of the minimax strategy). Neither arm is resolved here.

**No new theorem/counterexample** suitable for the publication gate; no Lean; no repo files changed. The front remains open as stated, with the resolution tightly coupled to `P ?= PSPACE` on the lower-bound side and to an unknown adaptive-to-low-alternation/succinct-complete simulation on the upper-bound side.

## Other metadata

```json
{
  "finished_at": 1793863871.7607381,
  "started_at": 1793859043.42038
}
```
