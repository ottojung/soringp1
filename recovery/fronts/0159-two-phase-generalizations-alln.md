# two-phase-generalizations-alln

## status

investigated

## origin

executive_manual

## agent_id

DLAmpDHP832CGbugxY2kXj-roughness

## exit_state

clearexit

## question

Do k-phase FO(TC)-expressible strategy programs achieve exact height S(n) for all large n for fixed k>=3, or is there an all-n asymptotic gap between k-phase programs and optimal unrestricted strategies forcing tau_k(n) = Omega(n)?

## basis

Two-phase results on board #301 (exact at some n, misses at others, aggregate tau(n)=Omega(n)); need to test fixed k>=3 generalizations.

## falsifier

Find an all-n construction for fixed k-phase achieving S(n) within bounded additive error independent in some way, or prove a linear gap for all fixed-k phase programs using the antichain-adversary and extension-count accounting.

## implication

Would sharpen the descriptive/strategy-complexity frontier for S(n) and clarify what FO(TC) normal forms can capture.

## finding_unverified

ressible program achieving bounded additive error (and verify against small n / self-certification where info bound tight) OR prove obstruction giving `tau_k(n)=Omega(n)`. Post concrete result/failed approach/exact obstruction to board #301 with careful distinction of soundness vs completeness and general-poset vs certificate points.

## Relevant Files
- **`/home/lubko/soring-fronts/two-phase-generalizations-alln/AGENTS.md`**: Project contract (unary scope, PSPACE-known, barriers/structural theorems focus, no unconditional super-polynomial lower bounds for unary).
- **`/home/lubko/soring-fronts/two-phase-generalizations-alln/docs/problem.md`**: Sorting model, `S(n)`, unary/binary encodings, realistic outcomes, known bounds.
- **`/home/lubko/soring-fronts/two-phase-generalizations-alln/docs/operations.md`**: Run on billy-dev, report to Antonina issue #301, use board digest.
- **`/home/lubko/soring-fronts/two-phase-generalizations-alln/docs/research-frontier.json`**: FO(TC) policy/interpreter and root-quotient fronts in this repo.
- **`/home/lubko/soring-fronts/two-phase-generalizations-alln/scripts/evaluate.py`**: Reference partial-order minimax `sorting_number(n)` for small exact values.
- **`/home/lubko/soring-fronts/fo-tc-two-phase-n8-verify-20261027/docs/research-fo-tc-twophase.md`**: Canonical two-phase barrier (lemma/theorem, n<=22 classification, miss mass, FO(TC)-style program notes).
- **`/home/lubko/soring-fronts/fo-tc-two-phase-n8-verify-20261027/scripts/fo_tc_twophase_barrier.py`**: Strict two-phase implementation compiling to constant-Ask label program, all-orders verification, self-certification checks.
- **`/home/lubko/soring-fronts/fo-tc-two-phase-n8-verify-20261027/scripts/twophase_independent_check.py`**: Independent Ford–Johnson + transcript-prefix verification.
- **`/home/lubko/soring-fronts/fo-tc-strategy-programs-20261101/docs/research-fo-tc-combined.md`**: FO(TC)_v strategy program definitions, fragment programs, completeness conjecture, clocking `(n+k+|p|)^c`.
- **`/home/lubko/soring-fronts/fo-tc-strategy-programs-20261101/docs/research-fo-tc-strategy-barrier.md`**: Strategy programs vs bounded-width/Barrington, FO(TC)_v upper/lower barriers, state-complexity obstructions.
- **`/home/lubko/soring-fronts/fo-tc-two-phase-n8-verify-20261027/scripts/upper_witness.py`**: Ford–Johnson merge-insertion reference used by two-phase.
Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed.
**Two-phase analysis (proven):** strict sort-(n-1)-then-binary-insert gives `T_2(n)=S(n-1)+ceil(log2 n)`. Exact iff `S(n)=S(n-1)+ceil(log2 n)`. Classified n≤22: exact at {4,6,7,8,11,12,13,14,15,16,22}, misses at {5,9,10,17,18,19,20,21} (non-monotone). Witnesses n=5-9 verified independently; n=6,7,8 self-certify by info bound. All FO(TC)-style programs as constant-Ask label programs verified per order.

**FO(TC) model:** fixed-variable `FO(TC)_v` fragment gives polytime rule evaluation `O(|φ|·N^{2v})`; explicit-tree compilers need `Ω(n!)` nodes, exact recurrence needs #P-hard linear-extension counts. Polytime FO(TC)-completeness for exact `S(n)` remains open.

**Frontier (billy-dev, issue #301):** investigating fixed k-phase FO(TC)-expressible generalizations to all-n exact `S(n)`. Task: model k-phase structure, generalize antichain/adversary accounting to fixed k, test if any fixed k achieves all-n exactness or prove linear gap `τ_k(n)=Ω(n)`. No k-phase code yet; definition not explicit in repo.


## Other metadata

```json
{
  "finished_at": 1793569063.7194958,
  "started_at": 1793559714.9378793
}
```
