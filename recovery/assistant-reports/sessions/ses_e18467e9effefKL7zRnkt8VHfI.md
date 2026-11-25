# antonina-BzOBRCH48ZXm2Sb39lRx10-surprised

Session: ses_e18467e9effefKL7zRnkt8VHfI
Workspace: /home/lubko/soring-fronts/component-reversal-defect-bound
Created: 1794889056812; updated: 1794889639140

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 152 (msg_1e7c219d0001l0pjeX1R1ehvFm)

**Recovery / inspection (no duplicate external actions).** On `billy-dev`, cwd `/home/lubko/soring-fronts/component-reversal-defect-bound` (git clean at start, HEAD `6a96398`). No prior `exec-report.md` here. Durable artifacts for this front exist in sibling `/home/lubko/soring-fronts/component-reversal-defect-20261111/` (`comment_301.md`, `defect_probe.py`, `run_defect.py`, `results_max8.json`, logs). Research board #301 already has a matching post “SoringP1 frontier: component-reversal-defect-bound” (2026-11-17T02:34:15Z) plus Viche Executive verification/follow-up (2026-11-11). **No new #301 post was made** to avoid duplication.

**Work completed this session.** Wrote `exec-report.md` in this worktree summarizing the front (no repo/Lean changes, no commits).

**Sharp all-`n` question (falsifiable).** For finite disjoint posets `A,B`, let `F(P)` be the exact minimax adaptive comparison-sorting cost (model: `docs/problem.md`), `A^op` the dual, `A+B` disjoint union, and `D(A,B)=|F(A^op+B)-F(A+B)|`. For all finite `A,B`, is `D(A,B) <= 1` (or bounded by a constant), or can `D(A,B)` be arbitrarily large / exhibit some `D>=2`? A concrete pair with `D>=2` refutes the `<=1` claim.

**Result (open; no theorem, no refutation).**
- **Experiment (reported, artifacts in `component-reversal-defect-20261111`, not recomputed here):** two cross-checked exact minimax solvers (poset-state memoized DFS over transitive-closure states; extension-set memoized DFS over consistent linear extensions) agree on exhaustive pairs with `|A|+|B|<=5`, all unlabelled posets `n<=6`, a 100-pair sample at total 6, and `F` for `n<=7`. Unlabelled enumeration via `quotient_classes/make_refined_canon` matches OEIS A000112 for `n=0..8`. Exhaustive over all ordered unlabelled pairs with `|A|+|B|<=8` (46,481 pairs): **max `D=0` at every total 0..8, distribution 100% `D=0`**.
- **Literature/deduction (reported):** if `B` is self-dual up to relabelling then `D(A,B)=0`; non-self-dual `B` unsettled in general.
- **Independent verification (reported on #301 by Viche):** confirmed through labelled totals `<=6` with independent code.

**Precise boundary / obstruction.** Checked exhaustively only to `|A|+|B|<=8`; `|A|+|B|>=9` unattempted (reported next step needs ~183,231 unlabelled poset classes / ~400k+ pair evaluations at total 9). Conceptually, no all-`n` invariant/recurrence controlling `|F(A^op+B)-F(A+B)|` is established (minimax `F` not known invariant under component reversal inside parallel unions beyond special cases). Status remains **open**; finite evidence does not imply any universal bound or unboundedness.

**Consequence for evaluating `S(n)` / SORT-BOUND-U.** **No established consequence for `S(n)` or `SORT-BOUND-U` follows from present evidence.** A proved universal small defect bound would be a structural fact about disjoint-union minimax states (potentially relevant to compression/decomposition heuristics) but would not by itself yield a faster uniform evaluator, space improvement, NP/coNP certificate, or any separation for `SORT-BOUND-U`; an unbounded-defect witness would be a negative structural constraint. Either remains hypothetical.

**Evidence labels.** Definition: `F,D`, model per `docs/problem.md`. Reported literature/deduction: self-dual case, A000112 sanity. Reported experiment: solver cross-checks and exhaustive `D=0` for `|A|+|B|<=8` (`comment_301.md`/`results_max8.json`). Reported independent experiment: Viche up to labelled totals `<=6`. Conjecture/open: any all-`n` bound/unboundedness claim.

**Stopping point.** No proved bound/refutation and no demonstrated bridge to changing what is known about evaluating `S(n)`; further work would be heavier enumeration (>=9) or a new all-`n` structural argument. Local deliverable: `exec-report.md` (created). Board post not duplicated.
