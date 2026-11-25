# s-generating-function-d-algebraic

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Bm9NjSLukRLbwvUVSn83kt-last

## exit_state

clearexit

## question

Is the ordinary generating function F(z) = sum_n S(n) z^n differentially algebraic over Q(z), i.e. does it satisfy a polynomial differential equation of finite order with polynomial coefficients, or is it not D-algebraic?

## basis

Board #301 proves S is not D-finite with the Polya-Carlson argument; D-algebraic functions form a strictly larger class containing logarithms, so this is the next untested level and no ledger front addresses it.

## falsifier

Exhibit an explicit nonzero polynomial P(z, y, y', ..., y^(r)) annihilating F, or prove non-D-algebraicity for S using asymptotic, singularity, or integrality constraints.

## implication

D-algebraicity would yield a finite nonlinear recurrence for S and a strong structural law; non-D-algebraicity would extend the recent nonholonomy barrier from linear recurrences to all polynomial differential recurrences.

## finding_unverified

aises the transcendence degree by at most one. Thus \(L\), and therefore \(A=L/(1-q)\), are D-algebraic over \(\mathbb Q(q)\).

But \(D(n)\) is an integer, positive, nondecreasing, full-support sequence with

\[
D(n)=n\log n+(2\gamma-1)n+O(\sqrt n).
\]

So \(A(q)\) has radius exactly \(1\), integer coefficients, full support, nonnegative nondecreasing coefficients, the same \(\Theta(n\log n)\) growth as \(F\), divergence at every point of \(|q|=1\), and — since \(D(n)\) cannot be the coefficient sequence of a rational function — the unit circle is a natural boundary by Pólya–Carlson. It is not D-finite (D-finite plus integer coefficients plus radius \(1\) would force rationality). Thus it sits precisely in the D-algebraic/non-D-finite gap.

**Consequence:** radius \(1\), integrality, nonnegativity, monotonicity, full support, natural boundary, \(\Theta(n\log n)\) growth and boundary divergence cannot separate \(F\) from the D-algebraic class.

### Other routes checked and blocked

- **Modulo primes.** \(\theta_3(q)=\sum q^{n^2}\) is D-algebraic with integer coefficients but is not algebraic modulo \(p\) (Guttmann–Jensen–Maillard–Pantone, *J. Phys. A* 49 (2016) 504002, using Cobham). So failure of algebraic reduction mod \(p\) does not imply non-D-algebraicity.
- **Gap theorem.** Lipshitz–Rubel’s theorem needs Hadamard gaps. \(F\) has none, and full-support D-algebraic integer series such as \(A(q)\) exist.
- **“Finite nonlinear recurrence”.** This implication in the front is not correct. An ADE yields a coefficient relation with unbounded convolution memory, not a fixed-order recurrence. D-finite corresponds to finite linear P-recursive recurrences; D-algebraic does not.

### Small exact experiment

Using \(S(0),\dots,S(22)\) from OEIS A036604, I solved the linear systems for a low-order ADE. In every tested overdetermined case the nullspace was zero; all nonzero nullspaces appeared only when unknowns outnumbered equations. This is evidence only, not proof, and no finite prefix can establish non-D-algebraicity.

### Honest status

The front remains open. A proof of non-D-algebraicity must use arithmetic information specific to \(S(n)\), not the proposed asymptotic/singularity/integrality data, since the explicit D-algebraic series \(A\) above has all of them. I did not use general-poset hardness results, and this makes no claim about certificate soundness or completeness. No Lean or repository changes were made; the worktree is clean. The finding was posted to board #301.
Verified recovery state; no duplicate actions taken.

- **Board #301:** the finding was already posted exactly once at `2026-11-08T12:54:37.543Z` by `SoringP1 frontier`. A digest search finds only that one occurrence. I did **not** post again.
- **Repository:** `/home/lubko/soring-fronts/s-generating-function-d-algebraic` is clean; no commits, edits, Lean files, or tests were created.
- **Host:** `billy-dev`.
- **Durable record:** `~/.local/state/soringp1/frontier-ledger.json` still lists `s-generating-function-d-algebraic` with status `running`. I did not modify the ledger; its lifecycle transition is an operational/keeper action, so I am reporting it rather than guessing.

The mathematical work is complete for this turn: the D-algebraic integer series built from the divisor Lambert series blocks the proposed asymptotic/singularity/integrality falsifier, while the D-algebraicity of \(F(z)=\sum S(n)z^n\) itself remains open. No unfinished side effect needed repetition.

## Other metadata

```json
{
  "finished_at": 1794142611.2191472,
  "started_at": 1794141885.4714818
}
```
