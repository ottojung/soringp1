# g-completeness-sharp-band-constant-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

rQcBlIV1ty7CEUQugF6Nis-redress

## exit_state

clearexit

## question

The board's sharp necessary condition says a defect-free finite poset P with F(P)=L(P)=ell and e(P) > 3*2^(ell-2) is g-certifiable. Is this constant sharp for all n, i.e. is there some n and a defect-free poset with 2^(ell-1) < e(P) <= 3*2^(ell-2) (at ell=5: 17 <= e <= 24) for which the sound predicate g fails, or can the threshold be lowered to 2^(ell-1) for every finite poset?

## basis

Board #301 14:19Z sharp necessary-condition result and 14:05Z g-completeness conjecture; my independent exhaustive enumeration of all posets on n<=6 found no counterexample and no violation of the 3*2^(ell-2) theorem on that finite range only.

## falsifier

Exhibit a finite defect-free poset with 2^(L-1) < e(P) <= 3*2^(L-2) and g(P)=false, refuting the sharpened claim; or give a paper argument that g(P) holds whenever F(P)=L(P) and e(P)>2^(L-1) for all finite posets.

## implication

Resolving the sharp band either refutes completeness of the sound predicate g and closes the polynomial-size g-certificate route toward SORT-BOUND-U in NP, or yields the strongest local soundness theorem and tightens exact-search base cases.

## finding_unverified

condition. The proof cannot force `g` below `3*2^(ell-2)`.

**Exact remaining obstruction [deduction].** Any counterexample to lowering `3*2^(ell-2)` to `2^(ell-1)` (equivalently any defect-free non-`g` poset in the band) must be: `F(P)=L(P)=ell>=5`, `2^(ell-1)<e(P)<=3*2^(ell-2)`, and for every balanced `g`-candidate pair, at least one child is a one-level-hidden defect: defective `S` with `8<=e(S)<=2^(ell-2)` (smallest defective poset has `e=8`), while the other child may be defect-free with `L=L(P)-1`. This is the same hidden-defect obstruction as 14:19Z, now localized exactly to the band.

### 2) Finite falsification attempt: no counterexample in the L=5 band for n<=10 [experiment]

Fresh independent exact checker (`/tmp/opencode/band_lib.py`, `band_search.py`): transitive-closed bitmask posets; `e(P)` by subset DP over downsets; `F(P)` by memoized minimax; `g(P)` by recursive predicate. Sanity: `F(A_n)=S(n)` gives `0,1,3,5,7,10` for `n=1..6`. Generation completeness sanity: for `n=4`, all 40 transitive sub-orders of the chain equal cover-removal closure.

Searched all sub-orders of the `n`-chain (covers all labeled posets up to isomorphism by relabeling along a linear extension) with `e<=24`, i.e. including the entire L=5 band `17..24`:

| n | posets with e<=24 | band (17<e<=24, L=5) defect-free states | g-FALSE in band |
|---:|---:|---:|---:|
| 5 | 276 | 55 | 0 |
| 6 | 1377 | 626 | 0 |
| 7 | 4010 | 2258 | 0 |
| 8 | 8401 | 5134 | 0 |
| 9 | 14438 | 9249 | 0 |
| 10 | 22293 | 14787 | 0 |

Also checked defective `e=8` children exist (needed by obstruction): `n=5:8, n=6:16, n=7:24` labeled defective `e=8` posets in this representation. No band counterexample found. A larger `n=8, e<=96` run (covering higher bands) timed out during analysis after generating 175,962 states; **not a result**.

## Conclusion on the asked front

- **Is the `3*2^(ell-2)` constant sharp for the theorem?** Yes, for the 14:19Z proof: the implication step fails exactly at `3*2^(ell-2)` and cannot be lowered by that argument [deduction].
- **Is there a defect-free band poset with `g(P)=false`?** Not found. Exhaustive up to `n<=10, e<=24` finds 0 [experiment, finite only].
- **Can the threshold be lowered to `2^(ell-1)` for all finite posets?** **Open.** I obtained neither a counterexample nor an all-n proof. The band `(2^(ell-1), 3*2^(ell-2)]` is exactly the remaining possible location of `C`-counterexamples; closing it would require either constructing a hidden-defect band witness or proving every defect-free band state has an alternative g-witness.

## Failed / limited approaches

- **Direct threshold lowering in Theorem 1 proof**: fails because a child may have `e<=2^(ell-2)` and be defective. [deduction]
- **Finite exhaustive search n<=10, e<=24**: no counterexample; finite evidence only, not an all-n proof. [experiment]
- **Bigger e/n band scan (n=8,e<=96; n=9,e<=96)**: compute-limited / timed out; no completed result. [inconclusive]
- **“Forget relation” parent construction around defective e=8 child** (same idea as 14:19Z): observed alternative g-witnesses in tested cases, not a proof. [experiment]

## Honest limits

- No new theorem completing C, no counterexample, no new `S(n)` value, no SORT-BOUND-U class placement. 
- General-poset result only; not transferred to antichain `A_n`. 
- Soundness/completeness distinction preserved: `g` is sound; completeness remains conjectural.
- I did not post to #301 or change the repository; this is the requested report.

## Other metadata

```json
{
  "finished_at": 1795447401.3168132,
  "started_at": 1795444728.173661
}
```
