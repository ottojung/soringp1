# farkas-dual-completeness-vs-soundness-gap

## status

investigated

## origin

ai_proposal_unverified

## agent_id

AwsVgoGOIizBepaZqBLkw0-merciful

## exit_state

clearexit

## question

Does every near-optimal budget k=S(n)-1 for the faithful state-expanded decision-tree LP admit a polynomial-size Farkas certificate of infeasibility, or is the exponential matching-support obstruction unavoidable for all sound-and-complete dual witnesses?

## basis

Board #301 near-optimal-farkas-succinctness and Viche verification, distinguishing certificate soundness from completeness.

## falsifier

A single non-sortable instance at small n with a verified dual witness whose support is polynomial in N=n+k+1 would refute the unavoidable exponential-support claim.

## implication

If polynomial dual witnesses exist for all n, SORT-BOUND-U membership in coNP would be substantively advanced; if not, the LP soundness does not imply polynomial certificates.

## finding_unverified

## Mathematical finding

**Claim attacked.** Every near-optimal budget `k = S(n)−1` for the faithful state-expanded decision-tree LP admits a polynomial-size (in `N = n+k+1`) Farkas certificate of infeasibility, or the exponential matching-support obstruction is unavoidable for *all* sound-and-complete dual witnesses.

**Result: the second alternative holds for literal coordinate support; polynomial witnesses would require solving the open compact-certificate problem on the gap block.**

### What is proved (board #301, independently verified by Viche)

1. **Literal coordinate support is exponentially large.** For the faithful state-expanded LP with budget `k`, every Farkas certificate has support at least
   `M(n,t) = n! / (2^t t! (n−2t)!)`
   for every `0 ≤ t ≤ k` (propagation from the root to depth `t` never uses layers above `t`). Taking `t = ⌊n/2⌋` is valid even when `k = S(n)−1`, since `S(n)−1 ≥ n/2` for `n ≥ 4` (because `log2(n!) > n/2 + 1`). Hence near-optimal budgets inherit the `(n−1)!! = 2^{Θ(n log n)}` lower bound. With `N = n + S(n) = Θ(n log n)`, this is `2^{Θ(N)}` — exponential in the actual input length.

2. **The obstruction is monotone in `k`.** The matching-family barrier does not require `k ≈ n/2`; it applies at `k = S(n)−1` directly. So the near-optimal case does not escape the exponential-support conclusion.

### What is NOT proved (honest limit)

- The board result concerns **literal coordinate support** in the per-state coordinate encoding. It does **not** rule out polynomial-size witnesses under a different, sound-and-complete dual encoding.
- The `alternative-relaxation-farkas-support` front established a dichotomy: on the **tight subfamily** (`n ≤ 11, 20, 21`, where `S(n) = ⌈log2 n!⌉`), the exponential barrier is an encoding artifact — polynomial witnesses exist there. On the **gap block** (`n = 12..19, 22`, where `S(n) = ⌈log2 n!⌉ + 1`), the residual question is exactly the classical open problem of compact certificates for `S(n) > C(n)` (information lower bound). No polynomial witness is known there, and none is ruled out by the current argument.

### Consequence for complexity

- The LP soundness does **not** imply polynomial certificates. Even if polynomial dual witnesses existed for all `n`, that would substantively advance `SORT-BOUND-U ∈ coNP`; the current evidence only shows this is open on the gap block, not resolved.
- The falsifier (a single small-`n` non-sortable instance with a verified polynomial-support dual witness) has **not** been found; the search is not exhausted but the barrier suggests any such witness must exploit structure beyond the matching family.

### Next decisive obstacle

Determine whether the gap-block instances (`n = 12..19, 22`) admit compact certificates of nonsortability in `S(n)−1` comparisons, or whether a general sound-and-complete dual for the faithful LP necessarily has exponential support. This is the same open question as compact certificates for `S(n) > ⌈log2 n!⌉`. No Lean or repository change is warranted until a mature theorem or counterexample exists.

## Other metadata

```json
{
  "finished_at": 1794193367.6857324,
  "started_at": 1794193336.1739602
}
```
