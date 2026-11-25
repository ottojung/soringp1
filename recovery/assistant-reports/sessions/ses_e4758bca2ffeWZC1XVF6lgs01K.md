# antonina-Pr3t2KD0VppZGlcC2idHjW-convened

Session: ses_e4758bca2ffeWZC1XVF6lgs01K
Workspace: /home/lubko/soring-fronts/shallow-state-fibonacci-hardness
Created: 1794099332007; updated: 1794102510126

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 83 (msg_1b8a93e2d001dl5Tmm92g6Ol5Y)

The two board posts confirm the reduction shape: `L_bin` (counting LE is #P-hard, Brightwell–Winkler) + Kravitz–Sah multipliers `e(M)=c`, then an ordinal sum `P (+) M` with `e(P(+)M) = e(P)·c ≤ T(b)` ⟺ `e(P) ≤ K`, threshold `T(b) ≥ K^4`. The clarification post already notes the gadget leaves bounded width. My job: test the *shallow* restriction precisely.

First, let me pin down what "distance S(n) in comparison-split depth from the n-antichain" means combinatorially, and gather the repo's known S(n) values.

## Output 118 (msg_1b8adc8dd001gVAh4zg2cJ4tvW)

The repo already fixes the object I need (`docs/research-compression-next.md`: state space = posets; reachability by adding relations one at a time). Let me check the realizability-window note for the depth bookkeeping, then write the exhaustive census program.

## Output 129 (msg_1b8add57c001zp1JSVeV62ia43)

Both board posts confirm the reduction shape (ordinal sum `P(+)M` with Kravitz–Sah/Stern–Brocot multiplier `e(M)=c`, threshold interval `c ∈ [T/(K+1)+1, T/K]`, `T(b) ≥ K⁴`), and the repo's `research-compression-next.md` + `research-realizability-window.md` already give me the exact machinery: state space = transitive-closed posets, cover-cost lemma ("reaching P needs ≥ covers(P) comparisons"), and an exact occurrence criterion (joint-child budget condition + wasted comparisons). That gives me two nested classes to census:

- **R^cover(n)** = `{n-posets : covers(P) ≤ S(n)}` (conservative superset — depth-≤S(n) antichain descendants),
- **R\*(n)** = states occurring on some optimal play *inside* the exact evaluator (their joint-child criterion).

I'll write one exhaustive C census for n ≤ 7 (all 2045 unlabeled classes, exact `e`, `m=F`, covers, width, automorphism counts), explore R\* exactly, and test the reduction's ordinal-sum instances against both classes.

## Output 140 (msg_1b8b512ba001HeyW1AU5CRBy17)

The file is missing the analysis tail — let me complete it.

## Output 188 (msg_1b8b5e392001FpwJECpSpvGm7G)

No compiler in PATH. Let me look for one on the system or install options.

## Output 213 (msg_1b8b65d68001sV6xpnAEp13uUf)

A working gcc exists. Compile and run the census.

## Output 312 (msg_1b8baf02b001jBXVpzznXPIG78)

Found it — in `Frec` I treated the canon return value as a key (it's a raw rel). Fixing the key/rel confusion in both `Frec` and the R\* exploration.

## Output 397 (msg_1b8c459d1001IUHhtJcV2kHSfX)

Levels up to n=6 match OEIS A000112/A001035 exactly, but n=7 labeled count (6,129,859) is off from my remembered A001035(7)=6,120,459 by 9,400. Let me verify with an independent identity: `p(n+1) = Σ_Q labeled-on-n #ideals(Q)` (strip-maximal-element bijection, no canon/aut involved).

## Output 450 (msg_1b8c70b44001ld05CK2Qrw8xqh)

The worktree in /tmp/opencode was wiped by the restart. Recreating the (fixed) census file from scratch.

## Output 475 (msg_1b8ca5bae001mHVYxsgVwjzYUl)

The census already validates and shows key structure (max covers = ⌊n²/4⌋ < S(n) for n≤7, so the shallow class is vacuously everything there; predicate shows zero unsafe prunes). Also two fixes needed: my T-array was off by one, and I added a raw-rel labeled-count cross-check. Let me check whether the run is still going.

## Output 502 (msg_1b8cb8c69001lESjrW399uWqp7)

All main data is in. The `INDEP` ideals-bijection I wrote is mathematically wrong (strip-last-element only bijects posets where that label is maximal) — I'll drop it and add a decisive **raw-relation dedup labeled count** for level 7 (bypasses the canon/aut machinery entirely). Also fix the off-by-one `T[]` array, and add: threshold-conjecture check `e(P) ≥ F_{m(P)+2}`, the cheap no-filter (`n!/2^r ≤ T(b)` with r = comparable pairs), the bottom-cone gadget demo, and occurrence-depth tracking.

## Output 605 (msg_1b8d358e30016axaP1E2tWhP8O)

The B3 (bottom-cone) gadget keeps **all** 16 demo instances inside R\* — a control distinguishing gadget shapes. But my raw-rel counter only enumerated canonical labelings (26,603 — bogus, ignore). The remaining question is whether labeled p(7)=6,129,859 matches literature. Quick check:

## Output 623 (msg_1b8d4cfa4001556Q9ImoxGjCe7)

OEIS confirms A001035(7) = **6,129,859** — my labeled census is exact (my remembered 6,120,459 was wrong). Final piece: the literature S(N) values for the reduction-scale table. Let me check what the repo has.

## Output 641 (msg_1b8d4eb0c001HenkiJbZbwSOCy)

All numerics are settled. Now the reduction-scale table (Python, quick) for the report:

## Output 700 (msg_1b8d6acca001Q2UaOJ3V1ekjn1)

All computations are complete and cross-validated. Final report:

---

# Front `shallow-state-fibonacci-hardness`: does the #301 Fibonacci-threshold PP-hardness survive the shallow-state restriction?

**Verdict: INCONCLUSIVE** — with two sharp partial results: (A) the #301 ordinal-sum reduction **provably fails to transfer as written** (it emits provably out-of-class instances in an infinite dense-domain regime, and no special-casing method is known); (B) on the evaluator-reachable class the predicate is **sound for every budget** but far from complete, and admits a cheap poly-time NO-filter — partial easiness, but no poly algorithm for the YES region. Exact computations below.

## 0. Setup and the reachability/depth identity

- State class, conservative: **R^cover(n) = { n-posets P : covers(P) ≤ S(n) }**. Distance in comparison-split depth from A_n to P is **exactly covers(P)**: necessity is the repo's cover-cost lemma (`notes/research-realizability-window.md`, Theorem 1 — every cover must itself be declared); sufficiency by adding P's cover relations one at a time (each is incomparable when declared, closure stays inside P). This is the same front as `poset-class-reachability-restriction`, so I use their exact **occurrence criterion** (joint-child budget condition `max(F(C0),F(C1)) ≤ S(n)−k−1` plus wasted comparisons) as a second, stricter class **R\*(n) ⊆ R^cover(n)** — the states actually visitable inside an optimal play.
- Exact evaluator-relevant query pairing: a state P reached at depth d is asked `e(P) ≤ T(b)` with `b = S(n) − d`; I analyze both the earliest pairing `b = S(n) − covers(P)` and a full sweep over all b.

## 1. Census (`/tmp/opencode/shallow_census.c`, out.txt, err.txt; ~2 min run)

Exhaustive all-poset census n ≤ 7 with exact `e`, `m (=F)`, covers, width, automorphisms; brute-force canonical labeling (min over all perms).

Cross-validation, all **exact**:
- class counts 1, 2, 5, 16, 63, 318, 2045 = A000112;
- labeled counts 1, 3, 19, 219, 4231, 130023, **6,129,859 = A001035(7)** (verified against OEIS; my earlier anticipation of 6,120,459 was wrong);
- `m(A_n) = S(n)` = 0, 1, 3, 5, 7, 10, 13 for n ≤ 7 (`S(8)=16`, `S(9)=19` are repo-cited values in `docs/research-state-compression.md`);
- cover-count histograms: max covers = ⌊n²/4⌋ (2, 4, 6, 9, 12 for n=3..7).

Consequently: **R^cover(n) is vacuous (contains every n-poset) for n ≤ 8** (max covers 16 = S(8) at n=8), and first bites at **n = 9** (⌊81/4⌋ = 20 > 19). All finite checks below therefore also cover the whole poset space, not just the shallow part.

## 2. Classifier of the reachable classes

| n | classes | R^cover | **R\*** (labeled fraction) | width ≤ 2 in R^cover | in R\* |
|---|---|---|---|---|---|
| 3 | 5 | 5 | 5 (100%) | 4/18 | 4/18 |
| 4 | 16 | 16 | 12 (83%) | 10/174 | 8/144 |
| 5 | 63 | 63 | 19 (37%) | 26/2370 | 12/1110 |
| 6 | 318 | 318 | 136 (52%) | 75/41850 | 63/35280 |
| 7 | 2045 | 2045 | 907 (**49.7%** = 3,044,007/6,129,859) | 225/908460 | 214/858060 |

- The **width-two threshold theory does not cover the class**: the root itself has width n and anti-chain-like states dominate; only ~11% of 7-classes (≈15% labeled) are width ≤ 2. No bounded-width formula applies to R^cover/R\*. Also `e(P) ≥ F_{m(P)+2}` is **violated** in the class (min deficit 1; 361 violations at n=7) — the width-two hypothesis in `research-width-two-threshold.md` is essential; no one-line Fibonacci inequality characterizes the shallow class.
- Occurrence vs covers: R\* is a **strict** half of the cover-ball — covers ≤ S(n) is *not* sufficient inside optimal plays (the sibling-budget criterion bites). Wasted comparisons reach only ≤ 2 extra states-depth at n=5,6 (`WASTE` rows).

## 3. The predicate `e(P) ≤ T(b)` on the class

At the evaluator pairing (P, b = S(n) − covers(P)), n=7 (1749 queried states): cells (e≤T, F≤b) = **1138 / 611 / 0 / 296** — i.e. **zero unsound prunes at every n ≤ 7**, but the predicate fires on only 296/1749 (17%) and *misses* 611 prunable states. The full b-sweep gives the class-exact thresholds `TRc(b) = min{e : P ∈ class, F(P) > b} − 1`:

- n=7: `TRc = T(b) exactly for b ≤ 5` (2,4,7,12,20) and `TRc(b) > T(b)` for b ≥ 6 (47>33, 90>54, 196>88, 398>143, 839>232, 2519>376, 5039>609). So on the class the predicate is **sound for every b ≤ S(n)−1** and strictly more permissive than the global verified T(6..8); no cascade of unsoundness, but nothing close to completeness either.
- Cheap **NO-filter** indicator: under the conjecture `e(P) ≥ n!/2^{r(P)}` (r = #comparable pairs; **zero counterexamples over all 6.1M posets n ≤ 7**, label [experiment]) the test `n!/2^r > T(b)` decides NO without counting: it resolves 129/1749 queries at n=7 (all correctly) and confines the fire region to deep states (c ≥ ∼0.3·S(n)) — where `b = S(n)−c` is small and `T(b)` is tiny.
- **No easiness proof**: the ideals-DP remains exponential on the class even with O(n) covers (bottom-cone: n−1 covers, 2^{n−1} ideals); `e` is not a function of (covers, width); no bounded-width-style formula. So "EASY-ON-SHALLOW" is *not* established — only a poly NO-filter plus sound-but-rare firing.

## 4. Where the #301 reduction leaves the class

The construction: `(P,K) ↦ (P(+)M, b)` with `T(b) ≥ K⁴`, multiplier `e(M) = c ∉` interval `[⌊T/(K+1)⌋+1, ⌊T/K⌋]`, so `c ≈ K³`, and `e(P(+)M) = e(P)·c ≤ T(b) ⟺ e(P) ≤ K`.

- **Exact covers formula** (validated on all 79 + 16 toy instances, zero violations):
  `covers(P(+)M) = covers(P) + covers(M) + |Max(P)|·min(M) ≥ covers(P) + |M|`,
  using the census-confirmed fact `covers(M) + min(M) ≥ |M|` (verified: equality for chains).
- **Toy scale (N ≤ 7)**: with the 2-antichain multiplier, of the 79 domain classes at |P| ∈ {4,5}: most outputs stay inside R^cover and R\*, a few excluded (e.g. dense P#44,58,60,61 at N=7 leave R\*). With the cheaper bottom-cone multiplier B₃ (e=2, min=1) **all 16 N=7 demo instances remain inside R\*** — so covers/criterion budgets do *not* kill sparse-domain outputs.
- **Scale analysis** (K at the hard decision boundary K ≈ n!/2, conservative |M| ≥ min{m : m! ≥ c}, covers(I) ≥ covers(P) + |M|, dense domain covers(P) ≥ ⌊n²/4⌋, permissible covers ≤ S(N), S(N) bounded above by the elementary mergesort bound N⌈lg N⌉ − 2^⌈lg N⌉ + 1):

| n (domain) | b | log₁₀ c | \|M\|lb | N=n+\|M\| | covers(P) ≥ | covers(I) ≥ | S(N) ≤ |
|---|---|---|---|---|---|---|---|
| 8 | 80 | 12.8 | 16 | 24 | 16 | 32 | 89 |
| 12 | 160 | 25.3 | 26 | 38 | 36 | 62 | 165 |
| 20 | 345 | 54.3 | 44 | 64 | 100 | 144 | 321 |
| 30 | 616 | 96.8 | 69 | 99 | 225 | 294 | 566 |
| 50 | 1226 | 192.4 | 117 | 167 | 625 | 742 | 1081 |
| 100 | 3018 | 473.3 | 242 | 342 | 2500 | 2742 | 2567 → **EXCLUDED** |
| 200 | ~7178 | 1500 | ~633 | 833 | 10000 | 10633 | 7307 → **EXCLUDED** |
| 1000 | — | 10270 | ~3326 | 4326 | 250000 | 253326 | 48047 → **EXCLUDED** |

  From n ≈ 100 onward, dense-domain outputs **provably violate covers ≤ S(N)** by a factor that grows quadratically (the extra terms `Max(P)·min(M) + covers(M)` and the stricter R\* sibling criterion only push exclusion earlier). The #301 map handles *all* L_bin instances, including these; hence **the construction as given does not establish PP-hardness of the restricted language**. Nothing in this or the #301 post rules out a *different* reduction special-casing dense domains — but every known route would need the outputs to encode `e(P) ≤ K` inside a ≤ O(n log n)-cover poset.

## 5. Verdict and the next decisive obstacle

**INCONCLUSIVE**, decomposed:
- **The reduction does not survive as written.** It leaves the shallow class in an infinite dense-domain regime (§4), so "PP-hard on unrestricted posets" does not transfer.
- **Not proven easy.** On R\*, the predicate is sound at every budget ([experiment], n ≤ 7) and admits a poly NO-filter (conditional on `e ≥ n!/2^r`, zero counterexamples), but the YES region still requires exact counting with no poly algorithm in sight — the class is root-width, not width-two.
- The two bridge questions that would settle it: (i) is **#LE (hence L_bin) #P-hard/PP-hard on {covers ≤ S(n)} posets**? (all known hardness constructions are replete with Θ(n²) relations; sparse-cover hardness is open); (ii) is there a poly algorithm for `e(P)` (or just `e(P) vs φ^b`) on that class? Point (i) plus the sibling's cover-budget pumping is exactly the missing reduction input; my R\* data additionally shows the joint-child occurrence criterion is the more restrictive and untested-in-general half of "reachable inside an exact evaluator" (bottom-chain pumping passes it at toy scale — verified here — but is unproven for the sibling-budget condition at scale).

Artifacts: `/tmp/opencode/shallow_census.c` (census program), `/tmp/opencode/out.txt` (full output), `/tmp/opencode/err.txt`. No repo files touched; nothing posted to the board, per instructions.
