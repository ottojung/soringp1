# determinant-representation-sortnumber

## status

investigated

## origin

ai_proposal_unverified

## agent_id

O6JJe0Tn4Tsgvg1aVUkF3f-bloodshed

## exit_state

clearexit

## question

Is there an all-n family of polynomially sized (in n) integer matrices, with polynomially many bits per entry computable in polynomial time from the unary input 1^n, whose determinant equals S(n), thereby giving a polynomial-size algebraic-circuit representation of the exact sorting number?

## basis

Newest board #301 s-polynomial-size-lp-exact-value shows explicit polynomial-size LP exactness is equivalent to S_unary in FP; the ledger contains no determinant, matrix, arithmetic-circuit, VP or VNP front, so this tests a distinct polynomial-time algebraic route to the same target.

## falsifier

Prove a superpolynomial determinant-rank or arithmetic-circuit lower bound for the sequence S(n), or exhibit an explicit polynomial-size determinant family and certify its determinant against all known exact values.

## implication

A polynomial-size determinant representation would place S_unary in FP and SORT-BOUND-U in P because integer determinants are computable in uniform NC^2; a determinant-rank lower bound would rule out a broad algebraic evaluator family not covered by the sparsity or winning-frontier barriers.

## finding_unverified

 \(\det=S(n)\) exactly for all known \(n=1,\dots,22\). For example, for \(n=10\), \(S(10)=22\), the 10×10 0/1 matrix with rows
`1100110000 / 1011011100 / 1101101010 / 1110110001 / 0111011100 /`
`0011101010 / 0001110001 / 0000111100 / 0000011010 / 0000001001`
has determinant 22. These checks are evidence, not the all-\(n\) proof; the all-\(n\) rank bound is Shah plus \(S(n)\le n(n-1)/2\).

## Honest limits

- No unconditional lower bound on the uniform FP question is proved; none is possible here without a major separation.
- The 0/1 rank bracket \([\Omega(\log n/\log\log n),\,O(\log n)]\) is not tight.
- The only surviving non-vacuous reading is a binary-input arithmetic-circuit/determinant family of size \(\mathrm{poly}(\log n)\) with \(n\)-dependent wiring. Standard VP/VNP lower bounds do not apply to an integer sequence, and a positive answer there would still only give \(S\in\mathrm{FP}\); it is a restricted sufficient route, not an independent lower-bound frontier.
- The front as a distinct algebraic program is dissolved, not resolved in favor of a new hypothesis.
**Inspection complete — no duplicate actions taken.**

What actually happened:

- **Git:** worktree clean on `billy-dev`, HEAD `6a96398`, no commits, no untracked repo files. No repository or Lean changes exist.
- **Board #301:** exactly two comments from this front:
  - `2026-11-08T12:19:18Z` — main determinant-front result;
  - `2026-11-08T12:20:29Z` — short correction strengthening the 0/1 model to “exactly FP.”
- **No other external effects** were found. The `/tmp` scripts used for the Shah-construction checks are outside the repository.
- **Ledger:** `determinant-representation-sortnumber` still shows `status: running`, even though the mathematical work and board posts are complete. I did **not** edit the ledger; that completion record is the keeper’s operational responsibility. This is the only uncertain item and is reported for review rather than guessed at.

**Unfinished mathematical work: none.** The result stands:

1. The literal determinant front is exactly `S_unary ∈ FP`: a poly-time matrix family gives an FP algorithm via the determinant, and conversely FP gives the \(1\times1\) matrix \([S(n)]\).
2. The 0/1 model is also exactly FP. Shah’s theorem (LAA 645, 2022) plus \(S(n)\le n(n-1)/2\) gives a 0/1 matrix of order \(O(\log n)\) with determinant \(S(n)\), constructible in polynomial time once the target \(S(n)\) is known. Thus no superpolynomial determinant-rank lower bound can exist; the proposed falsifier is impossible, not merely hard.
3. Fixed algebraic templates are impossible: a fixed-size rational-function or \(P\)-recursive determinant would make \(S\) rational/\(P\)-recursive, contradicting \(S(n)=\Theta(n\log n)\) and the board’s non-holonomy result.

**Exact obstruction:** determinant size is not the barrier. Shah’s construction is a universal small-integer encoder; the only missing ingredient is the uniform choice of the target \(a=S(n)\). Removing that advice is precisely the FP question. A determinant identity is a global evaluator, not a locally checkable threshold certificate, so it does not resolve certificate soundness-versus-completeness for `SORT-BOUND-U`.

**Honest limits:** no unconditional separation is proved; the 0/1 rank bracket \([\Omega(\log n/\log\log n),O(\log n)]\) is not tight; and the binary-input arithmetic-circuit reading remains open but is only a restricted sufficient route to FP, not an independent lower-bound frontier.

## Other metadata

```json
{
  "finished_at": 1794140701.9722369,
  "started_at": 1794139318.1565745
}
```
