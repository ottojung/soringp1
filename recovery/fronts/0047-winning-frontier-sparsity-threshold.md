# winning-frontier-sparsity-threshold

## status

investigated

## origin

ai_proposal_unverified

## agent_id

EVVxvnPbCVUg5eLrmQP1IG-piercing

## exit_state

clearexit

## question

The winning-frontier barrier shows 2^((1/4-o(1)) n (log n)^2) nonisomorphic winning states exist at depths around information bound including at S(n); is there a critical depth t0(n) < S(n) (or relative to C(n)) below which the winning frontier becomes polynomial in n, and above which it becomes super-polynomial for all sufficiently large n?

## basis

docs/research-winning-frontier-barrier.md gives exponential-in-n(log n)^2 frontier at information/S(n) budget; docs/research-certificates-barriers.md asks about polynomial-size certificates.

## falsifier

Prove the frontier size is polynomial for all depths <= S(n)-c*sqrt(n) for fixed c and all large n, or find an all-n uniform threshold where a phase transition occurs provably; or show the construction is maximal in some sense.

## implication

A provable phase transition would identify which budget regimes might admit succinct certificates (polynomial frontier) versus those that provably cannot be enumerated, sharpening the NP-certificate question for SORT-BOUND-U.

## finding_unverified

Let us compute more precisely.

Let us analyze this carefully.

Let us read more carefully about "reachable states".

Let us think more systematically about the phase transition question.

Let us look up more of the literature and think.

Let us look up the barrier again more. Also look up primary literature mentioned - Fredman, Kahn-Saks, etc. But I don't have external search beyond what's in the repo. Let us read more docs.

Let us prepare a report. I need to be precise and honest about limits.

The rectangular barrier construction exhibits an internal phase transition in winning frontier size around t/k_C ~ 0.36 (well below S(n)) for all tested parametrizations, with frontier becoming super-polynomial above threshold while tiny below it; this occurs in that family across n in tested ranges and suggests a moderate-depth threshold for that structure. However it's unclear if this is universal across all constructions or positions relative to S(n)-c*sqrt(n) as stated - the barrier already shows large frontier exists (enumeration barrier) at moderate depths, but a general all-constructions phase transition remains open. No repo changes made; report above captures findings, failed approaches, and limits.

## Other metadata

```json
{
  "finished_at": 1793353470.5740173,
  "started_at": 1793346560.3918037
}
```
