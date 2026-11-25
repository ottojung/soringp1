# antonina-WjKBtn002tv6rzoE4ebKQx-tundra

Session: ses_df82ff7b4ffe2P6bKYQqVbHCnC
Workspace: /home/lubko/soring-fronts/prime-defect-local-surrogates-n12-20261123
Created: 1795427403904; updated: 1795427929129

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 207 (msg_207d6bba1001xmz5DUECGA5lsn)

## Access obstruction

[experiment] I could not read the two requested #301 posts (`cert-enriched-perblock-completeness`, 2026-11-23T07:02:59Z, and its referee, 07:06:03Z): `/home/lubko/.local/bin/gh` is a browser-opener shim (`v0.0.4`), no real GitHub CLI/token/credentials are available in this environment, and unauthenticated GitHub API access to `ottojung/soringp1` returned 404 (private/auth-gated). I also searched the repo/git history for `cert-enriched`, `perblock`, and `prime defect` and found no local copy. The analysis below therefore treats the witness data given in the prompt as the input specification; I cannot confirm whether #301 used different depth-1/depth-6 A_12 witness states than the symmetry/default ones below.

## Question

[definition] Let `e(P)` be the number of linear extensions of a finite poset `P`, `F(P)` the exact minimax comparison cost to sort/identify a linear extension of `P` (SUPI), `info(P)=ceil(log2 e(P))`, and prime defect `D(P)=F(P)-info(P)`. A surrogate certifies defect if it implies `D(P)>=1`. It is sound if it never certifies defect when `D(P)<=0`. The tested constraint is: poly-time computable from the poset/order graph, local/structural, no enumeration of linear extensions, and no #P-hard exact `e` on general blocks.

## Named witnesses (as given / independently checked)

[experiment] Computation by exact DP on successor-bitmask posets (`linear_extensions` downset DP, `minimax` memoized game DP; script in `/tmp/opencode`, not in repo).

| Witness | e | info | F | D | check |
|---|---:|---:|---:|---:|---|
| A_12 root (antichain, d=0) | 12!=479001600 | 29 | 30 | 1 | `F=S(12)=30` [literature: Wells; see docs/literature.md]; `e,info` exact arithmetic |
| A_12 depth-1 (symmetry) | 12!/2=239500800 | 28 | 29 | 1 | one comparison splits antichain equally; by antichain symmetry `F=S(12)-1` [deduction] |
| Qp=(22,20,0,16,0,24), n=6 | 16 | 4 | 5 | 1 | exact DP: `e=16, F=5, D=1` [experiment] |

[experiment] Qp structure: 6 elements, two 3-chains `0<1<2`, `5<3<4` with cross relations `0<4,1<4`; 7 incomparabilities, width 2, height 3, dimension 2 (realizer `(0,1,2,5,3,4),(5,3,0,1,4,2)`), and one incomparability-graph component (series-prime). I could not verify the specific depth-6 A_12 witness from #301; this is an obstruction for that named case.

## Candidates tested

### 1. Merge-decomposition residual (certified, Theorem B style)

[definition] For an ordinal-sum `P=P1⊕...⊕Pk` where every block is a singleton/chain or a certified two-chain merge `Merge(a,b)` with literature-certified `M(a,b)`, let `LB_F=sum info(Pi)+sum delta_i`, `UB_info=ceil(log2 prod e(Pi))`. Certify defect if `LB_F>UB_info`. Here `e(Pi), info(Pi), delta_i` are poly-time for these certified blocks (factorials/binomials/closed merge values); no general-block LE enumeration is used. If any block is general, return not applicable.

[deduction] Sound when applicable: `F(P)=sum F(Pi) >= sum(info(Pi)+delta_i)=LB_F` and `info(P)=ceil(log2 prod e(Pi))=UB_info`, so `LB_F>UB_info => D(P)>=1`. This is the Theorem B / ordinal-sum additivity argument (`docs/research-structural-lower-bounds.md`, `docs/research-series-decomposition.md`; Jain-Klauck-Sántha 2010).

[experiment] Small-n exhaustive all posets (reachable = all posets in this comparison model):

| n | posets | D>=1 | certified-applicable | certified defect | unsound |
|---:|---:|---:|---:|---:|---:|
| 0-4 | 1,1,3,19,219 | 0 | 1,1,3,18,150 | 0 | 0 |
| 5 | 4231 | 120 | 1530 | 0 | 0 |
| 6 | 130023 | 15810 | 18450 | 720 | 0 |

[experiment] The 720 n=6 certifications are exactly the labelled `Merge(2,4)` relabelings (`C(6,2)*2!*4!=720`), matching the known strict witness `e=15, info=4, F=5, D=1`. On named witnesses: A_12 root not applicable (single non-certified block); A_12 depth-1 not applicable (one 2-chain + 10 singletons gives a connected incomparability graph, series-prime); Qp not applicable (series-prime general block). Verdict: **sound, poly-time, but fails to certify all named prime-defect witnesses except certified-merge ordinal-sum shapes**.

### 2. Width / Dilworth `S(width(P))` lower bound

[definition] Candidate `LB_F := S(width(P))`, certify defect if `S(width(P)) > UB_info(P)` for some poly-time `UB_info`.

[deduction/experiment] **Not proved sound; do not use as a sound surrogate.** An antichain subset `A` of size `w` has induced `e(A)=w!`, but comparisons may involve elements outside `A`; this does not give a proof that total `F(P)>=S(w)`. Exhaustive search found no counterexample with `S(width(P))>F(P)` for `n<=6` (174496 posets), but absence of small counterexample is not soundness. Also it would not certify A_12 root without independently certifying `S(12)>=30`.

### 3. Chain-cover upper bound on info

[definition] Dilworth chain cover `C1,...,Ck` gives subposet `P_C ⊆ P`, hence `e(P)<=e(P_C)=n!/prod |Ci|!` and `UB_info=ceil(log2 e(P_C))`, poly-time, no exact `e`.

[experiment] Sound as an upper bound on info, but too weak as a defect certificate: A_12 root UB_info=29 (equals actual info, gives no gap); A_12 depth-1 UB_info=28; Qp gives chains [3,3], `UB_e=20`, `UB_info=5` while actual info is 4, so it cannot certify Qp's defect. Verdict: **sound component, insufficient alone**.

### 4. Greene-Kleitman / height-width / comparability-incomparability invariants

[deduction] Width, height, comparability degree stats, incomparability edge count are poly-time local graph invariants. I found no sound rule turning them into `D(P)>=1` without exact `e` or an F lower bound strong enough to beat info. Width/height do not determine `F` or `D` (known non-tightness phenomenon; see docs/research-n12-nontightness.md). Verdict: **no sound defect certificate found**.

### 5. Bump/jump-number / dimension-2

[literature/deduction] Jump number is NP-complete in general (Pulleyblank; Bouchitte-Habib), so not an admissible poly-time general surrogate. Dimension 2 is poly-time recognizable, and Qp is dimension 2, but dimension 2 does not imply defect; it is a structural class, not a defect certificate. Verdict: **inadmissible or non-certifying**.

### 6. Forcing/entropy local bounds

[deduction] Any surrogate of this form must produce a poly-time `LB_F` and/or `UB_info`. With `UB_info` from chain cover and no exact `e`, certifying A_12 root requires `LB_F>=30` while only `UB_info>=29` is available; certifying Qp requires either `UB_info<=4` (chain cover gives 5) or `LB_F>=5` by a method stronger than info. No tested local forcing rule achieved this. Verdict: **no candidate found**.

## Falsification attempts

[experiment] (1) Exhaustive soundness scan for merge-residual-certified on all 174496 posets, `n<=6`: 0 unsound certifications. (2) Width-`S(w)` counterexample search, `n<=6`: none found, but proof obligation unmet so candidate rejected as sound surrogate. (3) Qp used as explicit falsifier: chain-cover UB_info too large (5>4), merge-residual not applicable (series-prime general block), dimension-2 non-certifying. (4) A_12 root/depth-1 used as falsifiers for all non-exact-e local LB_F candidates: certifying D=1 there requires beating the exact information bound, i.e. proving an S(12)-level F lower bound.

## Verdict

[deduction] **No poly-time, local/sound surrogate satisfying the stated constraints was found that certifies prime defect on the full named witness set.** The only sound poly-time candidate identified, certified merge-decomposition residual, certifies only ordinal-sum states whose blocks have poly-time `e` and certified merge gaps; it certifies 720/15810 n=6 defects and 0/120 n=5 defects, and fails on Qp, A_12 root, and symmetric A_12 depth-1 because those witnesses are series-prime/general or require an F lower bound above info.

## Impact on cert-enriched-perblock-completeness / `SORT-BOUND-U`

[deduction] This is a negative local-surrogate result, not a theorem-completion claim. It suggests that "cert-enriched per-block completeness" cannot be obtained by cheap local poset invariants alone: prime defect at A_12-root/depth witnesses is exactly the +1 gap above the information bound, so any certifier must either (a) compute/use exact `e` on the relevant block (allowed only when poly-time/special, not general #P-hard), or (b) supply a stronger-than-info `F` lower-bound certificate. That pushes certificate completeness toward richer global/per-block proof objects (e.g. strategy/DAG certificates with explicit F lower-bound content), rather than local graph surrogates. It does **not** imply `SORT-BOUND-U ∉ NP`, does **not** give a new upper/lower complexity bound, and does **not** resolve optimal-size completeness; it only rules out the tested local surrogate family under the stated soundness/poly-time/no-general-#P-e constraints.
