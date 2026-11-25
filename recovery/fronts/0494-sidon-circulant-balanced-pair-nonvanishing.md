# sidon-circulant-balanced-pair-nonvanishing

## status

investigated

## origin

ai_proposal_unverified

## agent_id

yyYDuTzJiZB4ADUxQc5j70-bushes

## exit_state

clearexit

## question

For the Sidon circulants D={0,1,3} subset Z_q with q prime >= 11, is e(P+xy) != e(P+yx) for every ordered incomparable pair, so that no balanced pair (condition B) exists?

## basis

Newest board #301 02:07Z abc-witness-decidability-alln section 6 names this as the next question; independent exact counts here for q=11,13 find no balanced pair.

## falsifier

Exhibit a prime q >= 11 and an ordered incomparable pair in the circulant with e(P+xy) = e(P+yx) = e(P)/2, computed exactly.

## implication

A balanced pair at some prime q would show the pair-certificate obstruction is not infinite along this family; universal nonvanishing would prove pair-only A/B schemes are infinitely incomplete, a certificate-completeness barrier with no direct S(n) bound change.

## finding_unverified

ention):** Sidon circulant poset on `2q` elements, minima `a_0..a_{q-1}`, maxima `b_0..b_{q-1}`, with `a_j < b_i` iff `(j-i) mod q ∈ D={0,1,3}`, `q` prime. By translation symmetry it suffices to check representatives (e.g. min-min `a_0 < a_d`, min-max `a_0 < b_i`). Question: for primes `q >= 11`, is `e(P+xy) != e(P+yx)` for every ordered incomparable pair (no balanced pair / condition B)?

**Reproduced/obtained:**
- `q=11` [experiment, exact, reproduced via `/tmp/opencode/curator301/sidon.py` and consistent with prior record]: `n=22`, `e(P)=16174936626710400`; **no balanced pair**.
- `q=13` [experiment, exact, reproduced]: `n=26`, `e(P)=764257252943441836800`; **no balanced pair**.
- `q=17` [experiment, exact, `/tmp/opencode/sidonfront/sidon.go` + `q17_exact_results.txt`]: `e(P)=9705680901543442321682647372800`; all checked ordered incomparable min-min and min-max representatives have `D = e(P+xy)-e(P+yx) != 0` (min-min `d=1..8`: differences nonzero with sign pattern below; min-max all positive large). **No balanced pair.**
- `q=19` [experiment, modular evidence, `/tmp/opencode/sidonfront/q19_mod.log`]: `q=19, states=16777216, mod=2305843009213693951 (2^61-1)`, `e(P) mod p = 864804370388211168`, log records **`Dmod==0` candidates: 0 of 37** checked pairs. Hence `D != 0` for every checked pair **modulo `2^61-1`** (in particular no exact-zero balance detected); this is strong evidence of no balanced pair but not by itself an exact proof that `D != 0` over Z (a nonzero integer multiple of the modulus is not excluded in principle). **No balanced pair found.**
- `q=7` [experiment, exact, prior/scratch]: `e(P)=72576000` with balanced min-min pairs (`D_d=0`), so the nonvanishing property is **not** universal over all primes `q`, but remains open for primes `q >= 11`.

**Observed min-min pattern (exact for `q=11,13,17`; consistent with `q=19` mod signs where comparable):** for representatives `a_0<a_d`, `D_1 < 0`, `D_d > 0` for `2 <= d <= ⌊q/2⌋`, `D_d < 0` for `⌊q/2⌋ < d <= q-2`, `D_{q-1} > 0`, with `|D_d/e(P)|` small (`~10^-6..10^-5`) but nonzero. Min-max differences large positive. Singleton inclusion-exclusion analysis (`singleton.py`) did not yield a cancellation/closed-form proof.

## Concrete obstruction / honest limits

- **Unfinished/open:** no all-primes-`q >= 11` proof of `D_d != 0`, and no counterexample (`q, x,y` with `e(P+xy)=e(P+yx)=e(P)/2`).
- **Computation barrier:** exact ideal/DP state space grows rapidly (e.g. `q=19`: 16,777,216 states; modular run feasible, exact feasible in tested range; `q=23` substantially larger), so naive extension is costly. A rigorous argument would need a structural/transfer-matrix or sign/asymptotic analysis controlling `D_d/e(P)` uniformly.
- **Scope/implication:** this is a certificate-completeness question for pair-only A/B along a specific Sidon-circulant family (relevant to the #301 obstruction), **not** a new bound on `S(n)`/`S_unary` or a complexity-class claim for `SORT-BOUND-U`. No repository, Lean, or board changes were made.

**Status:** front remains mathematically open; recovered work provides exact non-examples for `q=11,13,17`, modular nonvanishing evidence for `q=19`, and a clear obstruction. No unfinished external side effect requires continuation/duplication from this environment. Possible next decisive step (if pursued separately): a uniform proof of sign/nonvanishing for the min-min differences, or a multi-modulus (CRT-capable) exactness check/counterexample search beyond `q=19`.

## Other metadata

```json
{
  "finished_at": 1794300291.3577063,
  "started_at": 1794294252.2962785
}
```
