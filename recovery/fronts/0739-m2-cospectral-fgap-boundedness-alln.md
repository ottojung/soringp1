# m2-cospectral-fgap-boundedness-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

B5QRZ7dewc0YHJBjRJHKdh-critical

## exit_state

clearexit

## question

Over all finite posets with identical depth-two extension-count profiles M2(P)=M2(Q) (and hence identical e and M1), is the minimax-value gap |F(P)-F(Q)| uniformly bounded by an absolute constant, or can it grow without bound along an all-n family, mirroring the just-established unbounded gap for M1-cospectral posets?

## basis

Board #301 23:01Z proves the M1-cospectral F-gap unbounded via ordinal powers but notes the family is M2-separated; 22:03Z and 22:45Z report that M2-completeness reduces to a single M2-conflict and that ordinal sums preserve (e,M1,M2) together with the gap; docs/problem.md fixes the certificate scope. This is a general-poset question with no claimed transfer to SORT-BOUND-U.

## falsifier

Construct an all-n family of M2-cospectral posets whose F-gap grows, for instance ordinal powers of an M2-cospectral F-different seed; alternatively prove a universal constant bound, including the zero-gap case in which no such pair differs.

## implication

An unbounded gap would show that fixed-depth extension profiles cannot certify F even approximately; a zero gap would mean M2 determines F on all finite posets, the next rung of soundness-plus-completeness below the open M_t question, still requiring a separate transfer argument to S(n).

## finding_unverified

ero-gap case).

This is consistent with and sharpens the 22:02Z/22:45Z board reduction. The 23:01Z M1-unbounded family is M2-separated (I rechecked: seed M2 differs, square M2 differs), so it does not trigger Theorem 2(b).

## Computational evidence / attempted falsification [experiment]

Fresh from-scratch engine `/tmp/opencode/m2front/engine.py` (own closure, downset-DP e, child enumeration, memoised minimax F). Reproduced the board seed exactly: `e=32, M1=(4,4,14,14,16,16,16,16,16,16,18,18,28,28), F=5/6, M2 unequal`. Verified Lemma A 500/500, Theorem 1 composition 500/500, M2->M1->e projection 400/400. Verified k=2 ordinal square of the M1-seed: `M1 equal, F=10/12, M2 unequal` (confirms M2-separation of the known M1-gap family).

I attempted an exhaustive n=10 `(e,M1,M2)` conflict census by adapting the board's validated n=9 engine (`/tmp/opencode/ordinal_lift_front/n9_census.cpp`, A000112-validated). The n=10 build compiled and started (validated A000112 through n=9 = 183231, started gen10). It was **SIGKILLed** during generation (partial log shows gen10 reached 20k/183231 bases, 419039 classes). I did not restart it. Therefore I have **no n=10 census result**. The board's independently refereed n<=9 data has zero `(e,M1,M2)` conflicts.

I also attempted a random targeted composition search (`compose_search.py`) for M2-key collisions with different composed F; it was SIGKILLed before producing output after I reduced it to 7x300 items. No candidate found, no conclusion.

## Failed approaches / exact obstruction

1. **M1-gap ordinal-power transfer to M2**: fails because the known M1-cospectral F-gap seed/family is M2-separated (verified). So the 23:01Z construction does not answer the M2 front.
2. **Exhaustive n=10 M2-conflict census**: adapted engine started but was SIGKILLed before completion; infeasible to conclude within this run. The obstruction is computational resource/time, not a mathematical counterexample.
3. **Random composition-only search**: SIGKILLed/inconclusive; also not complete even if it ran.
4. **Intermediate bounded-nonzero gap**: ruled out by Theorem 2 (paper proof), so searching for a “bounded but positive” behavior is the wrong target.

## Complexity implication (careful, general-poset only)

Theorem 2 makes the front equivalent to M2 F-completeness. An unbounded gap (a single M2-conflict) would show depth-2 extension profiles cannot certify F even approximately on general finite posets; a zero gap would mean M2 determines F on all finite posets, the next rung below open `M_t`. **Neither case, by itself, transfers to `S(n)` or SORT-BOUND-U**: no encoding-preserving reduction from the antichain root `A_n` is established, the states are general posets (not shown k-safe reachable from `A_n`), and computing `e/M1/M2` is #P-hard on general posets (Brightwell-Winkler, context). This is a general-poset structural question, as the front states.

## Honest limits

- No M2-cospectral F-different pair found; none ruled out at n>=10. The all-n M2 F-completeness / M2-gap question remains **OPEN**.
- Theorem 2 is a reduction/dichotomy, not a resolution of either branch.
- All computation is general-poset; no S(n) value, no complexity-class placement, no SORT-BOUND-U bound. `S(n)` and `SORT-BOUND-U` remain OPEN.
- n=10 census incomplete (SIGKILL); composition search inconclusive. No claim is made from killed runs.
- No Lean file, no repo change, no CI/test change, no board post, no ledger change. I did not create a new front.

## Other metadata

```json
{
  "finished_at": 1795479286.6933897,
  "started_at": 1795477872.3012028
}
```
