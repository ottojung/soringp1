# antonina-yyYDuTzJiZB4ADUxQc5j70-bushes

Session: ses_e3bba6f78ffedXUsCGGFqA92u3
Workspace: /home/lubko/soring-fronts/sidon-circulant-balanced-pair-nonvanishing
Created: 1794294256355; updated: 1794300284772

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1c445a49e001HdAEz3Lsb45hh9)

I'll start by studying the repository contract, problem statement, and current board state.

## Output 981 (msg_1c49e5c69001ZKaAyxjNC1h94J)

I've completed the investigation. Let me consolidate the findings and report honestly.

## Output 1001 (msg_1c49f227d0014lPaCU5pnOPOXm)

## Report: Sidon-circulant balanced-pair front

**Front.** For the Sidon circulant `D={0,1,3} ⊂ Z_q`, `q` prime ≥ 11, is `e(P+xy) ≠ e(P+yx)` for every ordered incomparable pair, so that no balanced pair (condition B) exists?

### What I did

I reproduced the curator's exact counts for `q=11,13`, extended the search to `q=17` (exact big-integer DP) and `q=19` (modular DP), and looked for a proof or a counterexample.

**Computational evidence (no balanced pair found):**

| q | e(P) | result |
|---|------|--------|
| 11 | 16,174,936,626,710,400 | all ordered incomparable pairs have `D ≠ 0` |
| 13 | 764,257,252,943,441,836,800 | all pairs have `D ≠ 0` |
| 17 | 9,705,680,901,543,442,321,682,647,372,800 | all pairs have `D ≠ 0` |
| 19 | `e(P) ≡ 864,804,370,388,211,168 (mod 2^61−1)` | all pairs have `D ≢ 0 (mod p)`, hence `D ≠ 0` |

Here `D = e(P+xy) − e(P+yx)`. For `q=19` the modular check is decisive: if `D = 0`, then `D mod p = 0`; no pair satisfied that.

**A stable sign pattern (exact for q=11,13,17; consistent with q=19).** For min–min pairs `a_0, a_d`, with `D_d = e(P+a_0<a_d) − e(P+a_d<a_0)`:

- `D_1 < 0`;
- `D_d > 0` for `2 ≤ d ≤ ⌊q/2⌋`;
- `D_d < 0` for `⌊q/2⌋ < d ≤ q−2`;
- `D_{q−1} > 0`.

The min–max differences are all large and positive (e.g. `D ≈ 0.89·e(P)` for `q=11`). The ratios `D_d/e(P)` are nearly independent of `q` (e.g. `d=1`: `−2.08e−5, −2.34e−5, −2.39e−5` for `q=11,13,17`), suggesting convergence to nonzero constants.

### Failed approaches

1. **Inclusion–exclusion over forbidden maxima.** The swap of `a_0` and `a_d` is blocked exactly when a maximum in `F_d = {0,−1,−3,d,d−1,d−3}` lies between them. The singleton terms are huge (`~10^15` for `q=11`) and cancel to give `D_d ~ 10^11`; the first-order approximation fails by an order of magnitude.
2. **Order-polynomial transfer matrix.** The state space is `O(k^3)` per evaluation point `k`; summing over `k=0..2q` is `O(q·k^7)`, infeasible beyond small `q`.
3. **Subset DP over order ideals.** The state count is the number of ideals, which grows exponentially (`≈1.17q`); feasible only up to `q=19` (16M states for `q=19`, 525M for `q=23`).
4. **Direct transfer matrix for linear extensions.** No small-state formulation was found; the natural state (set of placed minima) is exponential.

### Honest limits

- The claim is verified only for `q = 11, 13, 17, 19`. **No proof for all primes `q ≥ 11` is obtained, and no counterexample is found.**
- The sign pattern is a conjecture supported by exact computation and the observed convergence of `D_d/e(P)`; it is not proved.
- The `q=7` case (`e(P)=72,576,000`) has *every* min–min pair balanced (`D_d = 0`), so the claim is not universal for all `q`; the front restricts to `q ≥ 11`.
- The decisive open step is a proof that `D_d ≠ 0` for all `d` and all primes `q ≥ 11`, or a counterexample at a larger prime.

### Complexity implication

The front's stated implication is that a balanced pair at some prime would show the pair-certificate obstruction is not infinite along this family; universal nonvanishing would prove pair-only A/B schemes are infinitely incomplete, a certificate-completeness barrier with no direct `S(n)` bound change. **My result does not establish universal nonvanishing, so that implication remains open.** The A/B/C conditions are sound sufficient conditions for GPC (Peczarski); the balanced-pair question concerns *completeness* of the pair-only route, not soundness. No change to `S(n)`, `S_unary`, or `SORT-BOUND-U` follows from these computations.

No repository, Lean, or PR changes were made; scratch work is under `/tmp/opencode/sidonfront/`.

## Output 1072 (msg_1c4a0ec32001c4TFJt1RYuu60Z)

## Recovery inspection (no external actions taken)

- **Git/worktree:** `/home/lubko/soring-fronts/sidon-circulant-balanced-pair-nonvanishing`, branch `billy-dev` (tracking `origin/billy-dev`), `HEAD 6a96398`. `git status --porcelain` clean; no local commits, diffs, or untracked repo files.
- **Durable records inspected:** `~/.local/state/soringp1/frontier-ledger.json` front `sidon-circulant-balanced-pair-nonvanishing` (agent `yyYDuTzJiZB4ADUxQc5j70-bushes`, `status: running`, `started_at` 1794294252.2962785, no `finished_at`/`finding_unverified`/board-link fields recorded). Prior scratch present under `/tmp/opencode/curator301/` (`sidon.py`) and active scratch under `/tmp/opencode/sidonfront/` (`sidon.go`, compiled `sidon`, `q17_exact_results.txt`, `q19_mod.log`, `singleton.py`, board snapshots).
- **Board (#301):** searched local board snapshot `/tmp/opencode/sidonfront/board_p1.txt` and filenames in scratch for this front id/keywords; **no post, draft, or post-result artifact for `sidon-circulant-balanced-pair-nonvanishing` found**. I did not post anything (and will not duplicate).

## External effects determined

- **Occurred (confirmed by artifacts):** local computations and file writes only in `/tmp/opencode/` scratch (`/tmp/opencode/sidonfront/*`, reuse of `/tmp/opencode/curator301/sidon.py`); Go binary compiled at `/tmp/opencode/sidonfront/sidon`.
- **Not observed:** no board comment, no repository/Lean edits, no commits/PRs, no ledger updates attributable to this front. The ledger front remains `running` (keeper-managed); left untouched.

## Mathematical state for the front (from recovered artifacts; [experiment]/[deduction], not kernel-checked)

**Setup (prior convention):** Sidon circulant poset on `2q` elements, minima `a_0..a_{q-1}`, maxima `b_0..b_{q-1}`, with `a_j < b_i` iff `(j-i) mod q ∈ D={0,1,3}`, `q` prime. By translation symmetry it suffices to check representatives (e.g. min-min `a_0 < a_d`, min-max `a_0 < b_i`). Question: for primes `q >= 11`, is `e(P+xy) != e(P+yx)` for every ordered incomparable pair (no balanced pair / condition B)?

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
