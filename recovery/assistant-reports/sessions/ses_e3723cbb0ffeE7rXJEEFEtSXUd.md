# antonina-FtjGpWAFH9F2cyxgrZKNlm-cruelly

Session: ses_e3723cbb0ffeE7rXJEEFEtSXUd
Workspace: /home/lubko/soring-fronts/component-reversal-defect-20261111
Created: 1794371236961; updated: 1794382591783

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 638 (msg_1c988ed06001KqJHpD08IYY4wX)

## Recovery / state check (no duplicate side effects)
- Inspected cwd `/home/lubko/soring-fronts/component-reversal-defect-20261111` (initially empty, not a git repo), git state (none), and board #301 content available locally: **no prior `component-reversal-defect-bound` / defect `D(A,B)` post found**, and no existing computation artifacts before this run.
- **No external side effects performed**: did not post to #301 (no duplicate). No repo/Lean/workflow changes.

## Blocker: could not post to #301
- Posting requested to board issue #301, but no authenticated GitHub posting path is available here:
  - `/home/lubko/.local/bin/gh` is `gh` v0.0.4 (browser opener, not GitHub CLI).
  - Real GitHub CLI binaries exist (e.g. `/gnu/store/d2kigqrhk12i33va4zxzd16bxmm6iwzi-github-cli-2.83.2/bin/gh` v2.83.x) but are unauthenticated (`gh auth login` / `GH_TOKEN` required); no `GH_TOKEN`/credentials found in environment.
- Per instructions, this means I cannot satisfy “exit 0 with the post made”; instead I report the blocker and provide the complete, ready-to-post #301 report below (also saved as `comment_301.md`). **No comment was posted.**

## Computation completed (exact, exhaustive `|A|+|B| <= 8`)

### 1. Definitions
- Finite posets `A,B` on disjoint ground sets. `A^op` = dual (all relations reversed). `+` = disjoint (parallel) union (internal relations preserved, every cross pair incomparable).
- `F(P)` = exact minimax adaptive comparison-sorting cost (poset-state minimax / minimum-height decision tree):
  - `F(P)=0` if `P` total;
  - `F(P)=1 + min_{x,y incomparable} max(F(P+(x<y)), F(P+(y<x)))` otherwise (transitively closed successors). Consistent with `docs/problem.md`/`docs/upper-bound.md` and `scripts/benchmark_symmetry_quotients.py`, `scripts/parallel_module_probe.py`.
- Defect `D(A,B)=|F(A^op + B) - F(A + B)|`.
- Question: `D(A,B) <= 1` for all finite `A,B`, or can be arbitrarily large?

### 2. Method (exact, with cross-checked solvers)
- **Two independent exact solvers implemented** (`defect_probe.py`, scratch):
  1. **Poset-state minimax with memoization** (successor bitmasks, transitive closure, memo per query).
  2. **Extension-set minimax with memoization** (state = set of all consistent linear extensions / rank arrays; each comparison splits the set; minimax).
- **Cross-check agreement**:
  - Exhaustive all ordered pairs `(A,B)` with `|A|+|B| <= 5`: **246 pair-instances** (both `F(A+B)` and `F(A^op+B)` checked) — identical.
  - All individual unlabelled poset classes for `n <= 6` (406 classes): identical.
  - Random sample **100 ordered pairs** with `|A|+|B| == 6` (both forms, seed 0): identical.
  - Sanity: poset-state results agree with precomputed `F` from `quotient_classes`.
- **Enumeration (unlabelled posets, exhaustive)** via `quotient_classes(n)` / `make_refined_canon(n)` from `/home/lubko/soring301/scripts/benchmark_symmetry_quotients.py` (2-D colour refinement + lex-min canonical form; complete iso invariant). Counts match OEIS A000112: `n=0..8 → 1,1,2,5,16,63,318,2045,16999`. `genposetg` present at `/home/lubko/soring-scratch/antichain-abc/nauty2_8_8/genposetg`.
- **Exact D computation**: for each total `n`, enumerated all ordered pairs of unlabelled posets `(A,B)` with `|A|+|B|=n` (`∑_{a+b=n} A000112(a)*A000112(b)` pairs). Built exact `F` table for all canonical posets of size `n` using iso-quotient DP (`quotient_classes(n)`, poset-state minimax). For each pair: formed `A+B` and `A^op+B` (`dual`, block-shift `disjoint_union` as in `parallel_module_probe.py`), canonicalized, looked up exact `F`, recorded `D`.
- Main run: `results_max8.json` (script logic in `run_defect.py`).

### 3. Results (exhaustive for `|A|+|B| <= 8`)

| total n = \|A\|+\|B\| | ordered pairs (A,B) | distinct union canonical reps seen | max D | distribution of D |
|---:|---:|---:|---:|---|
| 0 | 1 | 0 | 0 | {0: 1} |
| 1 | 2 | 1 | 0 | {0: 2} |
| 2 | 5 | 2 | 0 | {0: 5} |
| 3 | 14 | 5 | 0 | {0: 14} |
| 4 | 46 | 16 | 0 | {0: 46} |
| 5 | 178 | 63 | 0 | {0: 178} |
| 6 | 851 | 318 | 0 | {0: 851} |
| 7 | 5,138 | 2,045 | 0 | {0: 5138} |
| 8 | 40,246 | 16,999 | 0 | {0: 40246} |

- **Totals checked:** 46,481 ordered pairs over `n=0..8`.
- **Max defect found:** `D = 0` (no pair with `D >= 1`, none with `D >= 2`).
- **Witnesses (representative, max D = 0):** every enumerated pair satisfies `F(A^op+B)=F(A+B)` exactly. E.g. `n=0`: `A=∅,B=∅, F=0,F=0,D=0`. `n=8` representative: `(a=0,b=8, A empty, B = 8-element antichain-canonical in this enumeration) -> F(A+B)=16, F(A^op+B)=16, D=0`.
- **Distribution:** 100% of pairs have `D=0` at every checked total.

### 4. Boundary / honest limits
- **Exact exhaustive boundary:** all ordered pairs `(A,B)` of unlabelled posets with `|A|+|B| <= 8` fully covered.
- **Not covered:** `|A|+|B| >= 9` not attempted (n=9: 183,231 classes/F values and heavier canonicalization; not “cheap” here). No claim for n>=9.
- **No theorem / no disproof:** `max D=0` through `n<=8` is finite exhaustive evidence only. It does **not** prove `D(A,B)<=1` (or `D=0`) for all finite `A,B`, nor prove boundedness/unboundedness. A universal bound or a first `D>=1/2` witness at larger size remains open by this computation.

### 5. Code / artifacts (scratch, cwd)
- `defect_probe.py` — poset primitives, poset-state minimax, extension-set minimax, disjoint union.
- `run_defect.py` (and variants) — enumeration/cross-check drivers.
- `results_max8.json` — per-total results (pairs, distinct union canonical reps, maxD, distribution, witnesses).
- `comment_301.md` — ready-to-post #301 report text.
- `run_max8.log`, `n7.log`, etc. — run logs.
- Read-only reused: `/home/lubko/soring301/scripts/benchmark_symmetry_quotients.py`, `/home/lubko/soring301/scripts/parallel_module_probe.py`.

**Status:** computation and cross-checks completed with `max D=0` on the full `|A|+|B| <= 8` range; **#301 post not made** due to authentication/tooling blocker described above (no duplicate, no guessed posting). Manual posting of `comment_301.md` (or equivalent) is required to complete the external reporting step.
