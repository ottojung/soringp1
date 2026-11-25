# excess-sequence-regularity-unary-p-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

RVlDky2cJr4121wIdzeRsV-moods

## exit_state

clearexit

## question

For every n let D(n)=S(n)-ceil(log2(n!)) be the unary sorting excess. Is D k-regular for some integer base k>=2, or P-recursive, or p-automatic for some prime p, for all n -- i.e. does the excess sequence admit any fixed finite linear digit representation or any polynomial-length linear recurrence, given that the repository's newest non-k-regularity and non-holonomy paper proofs rule these out for S(n) and for the information bound ceil(log2(n!)) but provably do NOT apply to their difference D(n)?

## basis

Newest board #301 and repository notes (k-regular-sorting-number, nonholonomy, both labelled paper proof) establish the barrier theorems for S and ceil(log2 n!) but explicitly exclude the difference because the -n/ln2 Stirling term cancels. Independent check: log2(n!)=n log2 n - n/ln2 + O(log n), so D(n)=o(n) and the transcendence/Pola-Carlson arguments do not transfer; exact literature S(n) gives D in {0,1} for n<=22, too little to refute regularity. The Nov-22 excess-distribution front left the pattern open and its 'Sergeev upper bound grows, so E unbounded' step is only an upper bound, not a refutation of boundedness. No duplicate of the 725 ledger fronts; no Lean or repository change; no proof claimed.

## falsifier

Show the k-kernel of D spans unbounded dimension over Q for k=2 or 3 (using exact S(n) for n<=22 together with Sergeev's D(n)=O(n/(log n)^(1/5))), or prove no finite-order polynomial-coefficient recurrence fits the known excess values; conversely a single explicit k-regular, P-recursive or p-automatic representation surviving every known value refutes the negative side.

## implication

A positive answer gives D(n) in O(log n) (automatic / k-regular) or poly(n) (P-recursive) time; since ceil(log2(n!)) is computable in poly(n) time on unary input 1^n, this yields S_unary in FP and hence SORT-BOUND-U in P, a new uniform upper bound. A negative answer is a clean barrier excluding every fixed closed-form or finite-recurrence evaluator of the excess, paralleling the S and information-bound barriers.

## finding_unverified

 16:51Z and no side effect had actually happened, so there was nothing to repeat.

## Mathematical finding

**1. New all-n theorem (paper deduction): the P-recursive horn collapses to eventual periodicity.**

For any integer sequence with `a_n = o(n)`, P-recursive ⟺ eventually periodic. Proof: if `G(z)=Σa_n z^n` is D-finite and not a polynomial, integer coefficients plus `o(n)` give radius exactly 1; Polya–Carlson then forces rationality (natural boundary is impossible for a D-finite function). Rational GF ⟹ eventually an LRS; `o(n)` kills all roots with `|λ|>1` and all unit-circle roots with polynomial degree ≥1, so the sequence is bounded; a bounded integer LRS has finite state space and is eventually periodic. Converse is trivial.

Applied to `D(n)=S(n)−⌈log₂ n!⌉` (integer, `o(n)` by Sergeev + information bound): **D is P-recursive iff D is eventually periodic (hence bounded).** So proving `D` unbounded or non-periodic would refute that horn outright. This uses no exact `S(n)` value and is *not* a corollary of the repository's non-holonomy theorem, whose `c·n log n` leading term cancels in `D`. It also shows the horns are genuinely inequivalent: `s₂(n)` is 2-regular, `o(n)`, unbounded, non-periodic, so k-regularity does not collapse; p-automaticity forces boundedness only under the finite-alphabet reading, not the weaker `D mod p` reading.

**2. Why the existing barriers provably cannot settle D.** The k-regular proof of `S` needs the transcendental constant `−1/ln 2` in `S(k^m)/k^m`; for `D` that limit is 0 (algebraic). The non-holonomy proof needs `S(n)~(1/ln2)n log n`; `D=o(n)` permits a rational GF with bounded coefficients. Both methods are silent on `D`.

**3. The proposed falsifier is invalid.** Sergeev is an ineffective one-sided upper bound — an `o(n)` bound cannot force unbounded k-kernel dimension. Finite data cannot either: `D(1..22)=0000000000011111111001` is trivially fit by an eventually periodic (hence P-recursive, k-regular, automatic) sequence. "Fits every known value" is a soundness check, not an all-n correctness proof, so that converse criterion is vacuous.

## Concrete obstructions / honest limits

I tried and failed to refute k-regularity via kernel-subsequence LRS growth (Sergeev permits `k^{γm}`, `γ<1`), Polya–Carlson directly (removed by `o(n)`), deriving unboundedness from Sergeev (one-sided — the Nov-22 fallacy), and Cobham-style two-base attacks (no second hypothesis). The exact obstruction: the only published lower bound is the information bound itself; no ω(1) additive lower bound on the excess is known, the infinitude of positive excess is open, and `S(23)` is unknown. **Neither horn was settled** — no representation was found and no barrier was proved; `SORT-BOUND-U` remains open, with no new placement or separation. No Lean or repository changes were made; scratch only in `/tmp/opencode`.
No unfinished work; no actions taken. State is unchanged from the audit I just reported:

- **Git/repo**: `billy-dev` at `6a96398`, clean working tree, no commits/stashes/Lean/test/CI/ledger changes.
- **Board #301**: exactly one post from `SoringP1 frontier: excess-sequence-regularity-unary-p-alln`, at `2026-11-23T17:11:51.769Z` (page 1). No duplicate.
- **Scratch**: draft/result in `/tmp/opencode/excess_regularity_post*`; no other side effects.

The front is not resolved mathematically (neither horn proved/disproved), but all reporting/side effects for this turn are already complete and nothing should be repeated.

## Other metadata

```json
{
  "finished_at": 1795454010.1092122,
  "started_at": 1795452714.0675564
}
```
