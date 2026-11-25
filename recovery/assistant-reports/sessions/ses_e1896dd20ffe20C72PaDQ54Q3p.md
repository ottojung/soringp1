# antonina-iQ5LxGOkfaLUce6YcFSTlO-jolted

Session: ses_e1896dd20ffe20C72PaDQ54Q3p
Workspace: /home/lubko/soring301-exec-exact-partial-information-sorting-interfaces-20261117
Created: 1794883789569; updated: 1794884933179

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 511 (msg_1e77a251c001fmFC2kdJ2cnu1F)

Task complete. Wrote `exec-report.md` in the worktree and posted a concise, independently checked result to Antonina #301.

Summary of findings:
- Ordinal-sum exact rule `F(A⊕B)=F(A)+F(B)` is sound all-n and polynomially verifiable; verified on all posets through n=5 and targeted sums. It does not apply at the series-prime antichain root.
- Disjoint chain-sum (merge) rules are exact only in certified ranges: `M(1,b)=ceil(log2(b+1))` all b, and `M(a,b)=a+b-1` only for `a≤b≤floor(3a/2)+1`. Universal `a+b-1` is falsified by `M(2,5)=5`, `M(2,6)=6`, `M(2,9)=7`.
- Ordinal composition of certified factors is exact.
- Gluing test fails for `Merge(2,4)` on the 6-antichain root: no topological order of its four chain comparabilities keeps both siblings within the height-10 budget (first obstruction `3<4` with residual budget 7 vs sibling `F=8`). Factor state is not reachable on an optimal 6-sorter, matching the prior root-prefix sibling obstruction.

No repository, Lean, PR, or branch changes were made; only `exec-report.md` was added. Existing tests pass.

## Output 540 (msg_1e77a6b5e001McDmo79020zmuK)

Recovery audit (no side effects duplicated):
- Workdir: /home/lubko/soring301-exec-exact-partial-information-sorting-interfaces-20261117 (clean HEAD 6a96398). `git status --short` shows only `?? exec-report.md` (untracked). No commits/branch/PR/repo changes made by me beyond that file write.
- Durable record: Antonina #301 has a post from this front (`SoringP1 frontier: exact-partial-information-sorting-interfaces`, 2026-11-17T03:08:10.187Z) containing the reported findings. I did not post again in this recovery turn.
- `exec-report.md` exists (7471 bytes) with the full, independently checked report (ordinal-sum identity, certified merge ranges + falsifiers M(2,5/6/9), ord-composition, gluing test failure on Merge(2,4) with sibling obstruction) and “No Lean/repo/PR/branch changes”.

Status: finished (no unfinished work). Nothing further to do unless you want `exec-report.md` committed/cleaned up.
