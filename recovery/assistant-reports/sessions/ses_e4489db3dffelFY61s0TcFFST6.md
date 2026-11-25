# antonina-e3lFUCi9p6OjLFVF9ds2fm-tinge

Session: ses_e4489db3dffelFY61s0TcFFST6
Workspace: /home/lubko/soring-fronts/split-merge-k18-window
Created: 1794146444494; updated: 1794150608734

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1bb7627090010GMpD4seh6wtTu)

I'll start by inspecting the existing work and infrastructure state before doing anything.

## Output 195 (msg_1bb7a30ab00101nywIx6xsQGmE)

Infrastructure is clear. Let me set up the working directory with the checkpointed engine.

## Output 1158 (msg_1bbb58418001EpMxnr4IoupAmV)

Posted exactly one finding to Antonina board **#301** (author `SoringP1 frontier: split-merge-k18-window`, `updatedAt 2026-11-08T15:09:46Z`). No repository files, Lean files, or workflows were changed (`git status --porcelain` empty). Working scripts/data live under `/tmp/opencode/splitmerge/k18/`.

## Finding

**Front `split-merge-k18-window`.** The checkpointed exact DP was extended to `n_k` for k=18 and k=19. `m(n)/n` is still descending along both `n_k` and `2^k`; the distance to the FJ coefficient 0.02766 shrinks by a near-constant factor ≈0.956 per step over k=14..19. It has not crossed, and at k=19 it is still 2.44× the coefficient.

### Results [experiment]

Using `L(n)=min_{a≤n/2}[L(a)+L(n-a)+⌈log2 C(n,a)⌉]`, Kahan `lf=log2(n!)`, `FJ(n)=Σ_{j≤n}⌈log2(3j/4)⌉` (reproduces the prior ten `n_k` FJ values exactly):

| k | n_k | L | FJ | L−FJ | m | m/n | opt |
|---|---|---|---|---|---|---|---|
| 8 | 341 | 2414 | 2392 | 22 | 31.3790 | .09202044 | 2 |
| 9 | 682 | 5504 | 5461 | 43 | 61.7910 | .09060269 | 1 |
| 10 | 1365 | 12372 | 12291 | 81 | 118.7002 | .08695986 | 1 |
| 11 | 2730 | 27462 | 27306 | 156 | 231.4336 | .08477422 | 1 |
| 12 | 5461 | 60375 | 60078 | 297 | 447.9855 | .08203360 | 1 |
| 13 | 10922 | 131640 | 131071 | 569 | 871.0042 | .07974768 | 1 |
| 14 | 21845 | 285080 | 283993 | 1087 | 1691.1266 | .07741481 | 1 |
| 15 | 43690 | 613748 | 611668 | 2080 | 3288.2865 | .07526405 | 2 |
| 16 | 87381 | 1314703 | 1310724 | 3979 | 6395.6913 | .07319316 | 1 |
| 17 | 174762 | 2803815 | 2796201 | 7614 | 12447.4158 | .07122496 | 1 |
| **18** | **349525** | **5956503** | 5941935 | **14568** | 24234.9499 | **.06933681** | 2 |
| **19** | **699050** | **12610792** | 12582910 | **27882** | 47215.9330 | **.06754300** | 2 |

Requested `2^k` sequence: 
`m/n = .07591490, .07380387, .07179468, .06987838, .06805619` at k=14..18; `.06631827` at `2^19=524288` (extra).

### Method and exactness gate [experiment/deduction]

- C engine, `int64` L, `a≤n/2`, float `logc`, exact repair at all near-integer pairs. Two scans: strict `<1e-7` flags and a 10× wider `<1e-6` candidate scan.
- Exact ceilings decided by 80-digit `loggamma`, falling back to `math.comb` when the value was within 1e-50 of an integer; **all repairs and fallbacks were individually cross-checked against `math.comb`/`bit_length`, 0 mismatches**.
- Measured floating error vs 80-digit values: max `1.36e-9` over all 60,713 near-integer candidates at N=349525 (`1.27e-9` over 11,001 random points) — a ~70× margin under the 1e-7 radius, so non-flagged ceilings are safe under the measured bound.

### Falsifier checks [experiment]

- Reproduced **all 262,145 entries** of the saved `L_262144.npy` exactly, including `n_k` k=14..17 and `L(262144)=4358249`.
- Full-range scan at N=262144 gives **6,645 flags / 6 repairs**, exactly matching the old `dp262.log` (half-range: 3,324 / 4).
- N=349525: 6,017 strict flags, 6 repairs. N=699050: 24,194 strict flags, 63 repairs (all strict; 63/63 confirmed by `math.comb`), 243,779 wide candidates.
- 28 independent point re-evaluations of `L(n)` in `(262144,699050]` match the stored array.

### Checkpoint / recovery evidence [experiment]

- Checkpoints every 10,000 n (L, opt, progress marker), resume from `n_done`.
- k=18 resumed from the validated `n_done=262144`; k=19 was cleanly aborted at `n=401938` and resumed to 699050. Peak RSS **16 MB**, vectors ≈14 MB — no OOM exposure.
- Synthetic abort-at-n=39/resume reproduced an independent full N=80000 run exactly.

### Trend and honest limits [experiment]

Gap ratios `(r(k)−0.0276575)/(r(k−1)−0.0276575)` are `0.9552, 0.9568, 0.9565, 0.9568, 0.9567, 0.9570` at k=14..19 along `n_k`, and `0.9563…0.9570` along `2^k`. So the descent is at the same slow geometric rate in both families. At k=19 the ratio is `0.067543` (2.44× the coefficient); its excess `0.039885` is 1.44× the coefficient. A literal extrapolation of these finite differences would suggest convergence to 0.02766 from above, while a different limit would make the strict inequality true; the window decides neither.

Only finite numerical statements are supported: any uniform linear bound valid through the computed range has `c ≤ 0.066318` (at 2^19), and along `n_k`, `c ≤ 0.067543`. No all-n, asymptotic, or unboundedness claim is made. Exactness rests on the measured floating-error bound plus exact `math.comb` resolution of every near-integer case, not on a kernel-checked proof.
