# antonina-gd1fI8TVrsLodAVrAbk6Do-miller

Session: ses_e3334e8ddffeOy1AuIMxOmfpVn
Workspace: /home/lubko/soring-fronts/n12-obstruction-invariant-20261111
Created: 1794437224258; updated: 1794446815820

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1cccb1dca001WhNNHs8Pzy93AG)

I'll start by reading the required documents and surveying the repo structure.

## Output 159 (msg_1cd10bb72001odOUwNCIgl9VxJ)

Let me survey the available computational tooling and prior artifacts.

## Output 249 (msg_1cd5ccf1f001zP6XqLkOhXVGzM)

## Recovery / state (no duplicate external effects)
- Inspected `/home/lubko/soring-fronts/n12-obstruction-invariant-20261111`: clean detached checkout of `6a96398` (`git status` clean, no repo modifications, no commits/branches/PRs created).
- Checked durable records: `~/.local/state/soringp1/frontier-ledger.json` shows `n12-obstruction-generalization` as `investigated` (clearexit, `Cxsw38xOPP28c59VzyHAXY-passing`); no prior #301 post from this worktree author.
- Board post action performed **once** (after an initial failed attempt due to missing `--author`): comment posted successfully to Antonina board issue **#301** as `n12-obstruction-invariant-20261111` (comment id `sha256:M7Y9Vmj8QBciXC6QMmXG_0bOGyuNVMlBn473NNABL70`, 2026-11-12T01:26:06.814Z). No other external side effects taken/repeated.

## Read (as requested)
- `docs/research-plan.md`, `docs/problem.md`, `AGENTS.md`, `docs/literature.md`, `docs/research-one-ply-obstruction.md`, `docs/research-structural-lower-bounds.md`, `docs/research-n12-nontightness.md`
- Surveyed relevant tooling/scripts (`scripts/evaluate.py`, `nontightness_experiments.py`, `one_ply_obstruction.py`, `structural_lower_bounds.py`, `benchmark_symmetry_quotients.py`, `obstruction_probe.py`) and existing n=8 class artifacts under `~/soring-fronts/fibonacci-threshold-n8-ordered-20261111/` (for feasibility/context).

## Sharp question
Is there a computable poset invariant `I(P)` with `C(P)=ceil(log2 e(P)) <= I(P) <= F(P)=S(P)` that is strictly above `C(P)` on an infinite or structurally characterized class, generalizing `S(12)=30 > C(12)=29` (Wells)?

**Consequence if found:** a uniform, checkable strengthening of the information bound certifying non-tightness on that class, potentially narrowing the exact-search/threshold window for computing `S(n)` (structural lower-bound/certificate contribution) — without implying complexity separations (per `problem.md`/`AGENTS.md`, unary super-polynomial lower bounds are out of scope).

## Candidates, precise falsifiable claims, and refutation evidence (numbers)

1. **L1 — one-ply adversarial information bound** (sound, `C<=L1<=F`; `docs/research-one-ply-obstruction.md`)  
   `L1(P)=0` if total else `1 + min_{i<j incomp} max(C(P+i<j),C(P+j<i))`.  
   - *Claim (to generalize n=12 antichain):* `L1(A_n)>C(n)` on an infinite antichain family including n=12.  
   - *Refuted on antichains:* `L1(A_n)==C(n)` for all `n=2..12` (balanced first split n!/2,n!/2); `n=12: e=479001600, C=29, L1=29`.  
   - *Local slack coverage (all unlabeled posets, exact F ground truth):* n<=4: 0 slack. n=5 (63): slack 1, detects 1, misses 0. n=6 (318): slack 36, detects 8, misses 28 (e.g. `e=13,C=4,L1=4,F=5`). n=7 (2045): slack 391, detects 168, misses 223.  
   - *n=8 (all 16999 unlabeled classes, `classes_n8.json`; no F):* `L1>C` on 544/16999, but `L1(A_8)=C(A_8)=16`.  
   - *Verdict:* sound local refiner; **does not** lift/generalize the n=12 root antichain obstruction.

2. **L2 — two-ply lookahead**  
   `L2(P)=0` if total else `1 + min_{i<j} max(L1(P+i<j),L1(P+j<i))`.  
   - *Claim:* sound strengthening capturing missed slack and/or antichain obstruction.  
   - *Results (all unlabeled, exact F):* `L2<=F` (0 violations), `L2>=L1` everywhere tested. n<=5: no improvement on slack cases (1/1 detected). n=6: slack 36, detects 21, exact 21, misses 15, `L2>L1` on 13 (helps e.g. `e=13,C=4,L1=4,L2=5,F=5`; misses e.g. `e=30,C=5,L2=5,F=6`). n=7: slack 391, detects 168, misses 223, `L2>L1` on 100.  
   - *Antichain:* `L2(A_n)` not computed for n>=8; but soundness requires `I(A_n)<=F(A_n)=C(n)` for tight antichains n<=11 (and `L1(A_n)==C(n)`), so no evidenced antichain lift (n=12 could in principle be 30 if sound, but unverified/unsupported).  
   - *Verdict:* partial local refinement, still incomplete; no verified generalization of n=12.

3. **B — merge-factor / ordinal-sum compositional bound** (`docs/research-structural-lower-bounds.md`)  
   `B(P)=sum_i ceil(log2 e(P_i)) + sum_i delta_i` over series blocks with certified merge gaps.  
   - *Claim:* generalizes n=12 obstruction.  
   - *Refuted for antichain:* antichain is a single non-merge block => `B(A_n)=C(n)` for all n (cannot explain `S(12)>C(12)`); strict gains only on decomposable/merge-factor states (e.g. `Merge(2,4), n=6: e=15,C=4,B=F=5`).

4. **Low-dimensional scalar/profile invariants** `I=f(e(P), width, #min, #max, |Aut(P)|)` (or monotone in `e`)  
   - *Claim:* computable scalar separates/predicts slack generally.  
   - *Refuted (literature/prior + consistency):* `F` not a function of/monotone in `e` (n=5: `e=8 -> F in {3,4}`; n=6: `e=13,F=5` vs `e=14,F=4`); `(e,width,#min,#max)` collisions at n=6 (e.g. `(13,2,2,2)->F in {4,5}`); symmetry neither necessary nor sufficient (loose with nontrivial Aut at n=6, H6). No such scalar can be a sound complete separator.

## Coverage / limits (honest)
- **Exhaustive unlabeled with exact F (slack ground truth):** n<=7 (2,5,16,63,318,2045 classes) — computed via isomorphism-quotient minimax (`quotient_classes`), n=7 in ~1.1s for F table + ~10.8s total for L2 scan.
- **n=8:** all 16999 unlabeled classes checked for `L1` vs `C` only (544 with `L1>C`, ~40.7s); **no F ground truth** (full n=8 minimax infeasible here; consistent with incomplete n=8 m(P) runs on #301).
- **n=12 obstruction region:** antichain-root values only `C(A_12)=29, L1(A_12)=29`; direct n=12 poset enumeration/minimax not feasible. No known exact `S(n)` values re-derived.
- “All unlabeled posets n<=8” with F-dependent refutation: **not completed** (n=8 F missing). Report posted as NEGATIVE/INCOMPLETE survey.

## Outcome
- **No computable invariant found** that provably lower-bounds `F(P)` strictly above `C(P)` on an infinite/structurally characterized class generalizing the n=12 antichain obstruction.
- Clean kill/refutation achieved for the tested families in the stated scope: L1/L2 give no evidenced antichain-root lift (L1(A_n)=C(n), n<=12) and miss many slack states (n<=7); merge-factor bound `B` cannot lift antichains; low-dimensional scalar/profile invariants are non-separating.

## Next decisive obstacle
A genuine generalization must raise the bound at the antichain root for n=12 (certify `F(A_12)>29`) while remaining `<=F(P)` everywhere. The `L_k` info-scored (per-pair child `e`) hierarchy showed no antichain lift and remained incomplete through n=7. Decisive step: a **provable root lift** on an infinite family containing 12, or a proof that no local/computable pair-split invariant can lift balanced antichain roots — likely requiring a global/strategic certificate beyond per-pair child extension counts (cf. Peczarski/Stober–Weiß: obstruction established by exhaustive strategic search, no compact scalar witness known).

**Posted to:** #301 comment `sha256:M7Y9Vmj8QBciXC6QMmXG_0bOGyuNVMlBn473NNABL70` (concise report with the above candidates, numbers, coverage, and obstacle). Worktree remains clean.
