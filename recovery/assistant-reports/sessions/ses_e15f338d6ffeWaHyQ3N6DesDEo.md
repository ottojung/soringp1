# antonina-eJSJAaGzvjGwzqDSHo4ujm-disc

Session: ses_e15f338d6ffeWaHyQ3N6DesDEo
Workspace: /home/lubko/soring301-exec-disjoint-defect-minsize-20261117c
Created: 1794928068488; updated: 1794928217972

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 96 (msg_1ea0ed010001rPmaieimi4pHEa)

## Investigated front
Fresh independent tack on `disjoint-union-defect-min-size` in `/home/lubko/soring301-exec-disjoint-defect-minsize-20261117c` (read `AGENTS.md`, `docs/problem.md`, `docs/research-plan.md`, `docs/research-parallel-duality.md`, `docs/research-structural-lower-bounds.md`, `docs/literature.md`; searched `docs`/`scripts` for `disjoint union defect` / `defect min size` — no existing matches). No repo-wide edits, no Lean, no PR/comments.

## Falsifiable question (all-`n`)
For disjoint-union states `P = A ⫫ B`, determine the minimum total size `n = |A|+|B|` and conditions under which the information defect `d(P)=F(P)-⌈log₂ e(P)⌉` is nonzero/controlled, and whether this yields any all-`n` structural/lower-bound/certificate consequence for `F`/`S(n)` or a clear obstruction.

## Result (written to `exec-report.md`)
- **Definitions:** adaptive minimax `F(P)`/`S(n)`, extensions `e(P)`, information bound `info(P)=⌈log₂ e(P)⌉`, defect `d(P)=F(P)-info(P)`, disjoint union `A ⫫ B` with `e(A ⫫ B)=C(|A|+|B|,|A|)e(A)e(B)`, and chain-merge factors `Merge(a,b)` with certified gap `δ(a,b)=M(a,b)-⌈log₂ C(a+b,a)⌉` (model/literature per `docs/problem.md`, `docs/research-structural-lower-bounds.md`).
- **Claim (deduction + bounded experiment):** minimum total size with `d(A ⫫ B)>0` is **6**. For all disjoint-union class-pairs with `n<=5`, `d(P)=0`; for `n=6` there are **70** ordered isomorphism-class pairs with `d(P)>0`, all with `d(P)=1` (includes certified chain merge `Merge(2,4)`: `e=15, info=4, F=5`, and also non-chain/component cases across splits 1+5,2+4,3+3,4+2,5+1).
- **Argument/computation:** certified merge-gap deduction (`M(a,b)=a+b-1` in tape range ⇒ smallest nonzero at `(2,4), n=6`) plus exhaustive deterministic computation over all quotient-class pairs `A,B`, `|A|+|B|<=6` (using repo poset machinery/APIs from `scripts/benchmark_symmetry_quotients.py` and `scripts/parallel_module_probe.py`, exact `e/F` DP/minimax).
- **Falsification:** H1 (defect at `n<=5`) refuted (0 cases); H2 (only chain-chain at minimum) refuted (`n=6` includes non-chain components, all `d=1`); H3 (larger defect at `n=6`) not observed. Bounded to `n<=6`; no asymptotic/uniform claim inferred.
- **Consequence/obstruction:** a **local** structural fact — the information bound is tight for all parallel states up to size 5 but fails by 1 already at size 6, so information-only pruning/lower bounds on disjoint-union subgames are strictly dominated in certified/block cases. This gives no all-`n` asymptotic, certificate, or uniform-complexity consequence for evaluating `S(n)`/`SORT-BOUND-U` (and none is claimed, consistent with project separation barriers).

**Artifact:** [`exec-report.md`](/home/lubko/soring301-exec-disjoint-defect-minsize-20261117c/exec-report.md) (definitions, claim, argument/computation, falsification, consequence, labels, reproducibility). No other files modified.
