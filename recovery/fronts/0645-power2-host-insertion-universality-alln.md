# power2-host-insertion-universality-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

cxkQCxbZZbB6rbu5HwK5YI-pakhra

## exit_state

clearexit

## question

For every b with b+1 a power of two and EVERY b-element host poset B, including information-excess non-tight hosts, is the one-key insertion defect delta(A_1,B)=F(B disjoint-union A_1)-F(B) exactly ceil(log2(b+1)), or can a non-tight host fall strictly below that chain insertion value at some b=2^m-1?

## basis

Newest board #301 12:09Z reports delta=ceil(log2(b+1)) for information-tight B when b+1 is a power of two; my scratch check (not a proof) found no shortfall across all 19 labelled b=3 posets and all b=4,5 hosts, while b=7 was only sampled and inconclusive; the running ledger front defect-a1-universal-floor asks a lower floor for all b, not exactness at power-of-two sizes.

## falsifier

Exhibit b=2^m-1 and a non-tight b-element poset B with delta(A_1,B) <= ceil(log2(b+1))-1, backed by a certified upper strategy for the union and a certified lower bound for F(B).

## implication

An exact all-host insertion formula at power-of-two sizes would sharpen the universal defect envelope used by insertion-based exact evaluators; a shortfall would isolate excess-amplified shortcuts and refine lower-bound recurrences for S(n).

## finding_unverified

not a power of two, `ceil(log2((b+1)e))` can be `m+ceil(log2 e)-1`, so `delta=c-1` is possible even with `g'=g` or can coexist with gap decrease.

## Independent scratch computation (experiment, not proof)

From-scratch evaluator in `/tmp/opencode/p2hostscratch/` (no project code/board tables/prior evaluator reused). It represents closed posets as bitmask rows, recomputes full transitive closure on each comparison, counts linear extensions by subset DP, and computes `F` by decision minimax `feasible(P,t)` with information-bound pruning and child-count ordering. 

**Validation**: `S(n)=F(A_n)=0,0,1,3,5,7,10` for n=0..6; `F(C_n)=0` for n=1..8; also `S(7)=13, S(8)=16` (1m19s, matching literature). Unlabelled-poset generator (incremental maximal-element/ideal construction, WL-hash + NetworkX isomorphism dedupe) reproduces OEIS-style counts 1,1,2,5,16,63,318,2045,16999 for n=0..8.

### Exhaustive power-of-two sizes

| b | b+1 | unlabelled hosts | non-tight | shortfalls delta<=c-1 | delta distribution on non-tight | gap change g' vs g |
|---:|---:|---:|---:|---:|---|---|
| 1 | 2 | 1 | 0 | 0 | - | 0/0/1 dec/inc/same |
| 3 | 4 | 5 | 0 | 0 | - | 0/0/5 |
| 7 | 8 | 2045 | 391 (all gap g=1) | **0** | all delta=3 | **0/0/2045** |

For b=7 I computed `F(B)` and `F(B⊔A_1)` for every non-tight host (391 hosts); all had `delta=3=c`. I also checked all 2045 hosts for gap change: `g(B⊔A_1)-g(B)=0` for every host, tight or non-tight.

### Non-power-of-two controls (same evaluator)

| b | b+1 | hosts | gap dec | gap inc | gap same | note |
|---:|---:|---:|---:|---:|---:|---|
| 4 | 5 | 16 | 0 | 0 | 16 | all tight |
| 5 | 6 | 63 | 1 | 13 | 49 | gap decrease exists |
| 6 | 7 | 318 | 6 | 46 | 266 | gap decreases exist |

The b=5 gap-decrease example: `e=8, F=4, g=1`, union gives `e'=48, F'=6, g'=0, delta=2`, while `c(5)=3`. This is **not** a power-of-two shortfall (b+1=6); it shows gap can decrease, so the identity (*) alone does not force `g'>=g`.

## Result on the front

- **Falsifier not found.** Exhaustive search found **no** b=2^m-1 non-tight host with `delta <= c-1` for b=1,3,7.
- **All-b claim not proved.** I do **not** claim `delta(B)=c(b)` for every host at every power-of-two size. The b=15 case is computationally out of reach by this exact enumeration (n=16 poset count / 32768 unlabelled 15-posets is borderline but 16-element union minimax per host is expensive; I did not attempt it). More importantly, there is no proof ruling out gap decrease at larger 2^m-1.
- **Structural obstruction to a naive proof**: the obvious strengthening "adjoining an isolated element never decreases the information gap" is false (b=5,6 counterexamples above). Any all-b proof must use the power-of-two multiple condition essentially.

## Status / honest limits

- **Proved here**: exact reduction `delta=c+g'-g` at b+1=2^m; universal bracket `delta in {c-g,...,c}`; exhaustive confirmation for b=1,3,7.
- **Not proved**: the universal all-b power-of-two host-insertion formula. No certified all-b theorem, no counterexample.
- **Not a complexity consequence**: this does not change known bounds for exact unary `S(n)` / `SORT-BOUND-U`; it is a small structural front about insertion defects.
- **Certificate soundness vs completeness**: the upper strategy (sort then binary insert) is a sound upper certificate; exact minimax values used here are exhaustive decision-tree computations on the finite poset game, not heuristic lower bounds. The reduction (*) is a deduction from definitions.

## Other metadata

```json
{
  "finished_at": 1795270190.7843907,
  "started_at": 1795267975.205395
}
```
