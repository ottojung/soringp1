# antonina-MONEJRtmouMRFso5Nglht7-safe

Session: ses_e15f336adffeOkFm9yRQtkeVGB
Workspace: /home/lubko/soring301-exec-info-gap-invariant-20261117c
Created: 1794928068988; updated: 1794928225397

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 83 (msg_1ea0f00c40018P9UK667clpidk)

## Completed
- Read all requested files: `AGENTS.md`, `docs/problem.md`, `docs/research-plan.md`, `docs/research-n12-nontightness.md`, `docs/research-one-ply-obstruction.md`, `docs/research-structural-lower-bounds.md`, `docs/research-sergeev-asymptotic.md`.
- Wrote `exec-report.md` in `/home/lubko/soring301-exec-info-gap-invariant-20261117c` (only file created/edited).

## Report summary (`exec-report.md`)
- **Fresh tack (distinct from prior n12-gap/one-ply/structural notes):** analyzed the rooted strategic hierarchy of **k-ply extension-balance (lookahead information) certificates** `L_k` / `Cert_k(n)` as a class of global, computable necessary conditions for `S(n)=C(n)`.
- **Hypothesis tested (all-n, falsifiable):** some fixed/uniform bounded ply `k` characterizes tightness (`S(n)=C(n) ⇔ Cert_k(n)`).
- **Derivation/evidence:** `L_k` is sound for all `k,n` (induction); root symmetry collapses `k=1`; general form is a pathwise balance invariant over horizon `k` with slack `σ(n)=2^{C(n)}/n!`.
- **Falsification/counterexamples:** `k=1` separates no `n`; `k=2` fails at `n=12` (a 1/2 second split is admissible under `C(12)=29`, so `Cert₂(12)` holds, but literature gives `S(12)=30`). Fixed-`k` characterization is obstructed for the specified class; full-horizon `k=C(n)` is tautological (equivalent to full minimax). Consistency checked against known values `n≤22`.
- **Consequence / decisive obstacle:** no bounded-lookahead leaf-count invariant of this natural class characterizes `S(n)>C(n)` for all `n`; a non-tautological all-`n` characterization must be sensitive to unbounded/late-depth failures or compress the full adversarial game (succinct-certificate barrier). Next sharp question: lower-bound the first forced-failure depth as a function of `n`.

No repo-wide edits, no Lean, no PR/comments. Claims labeled (definition/literature/deduction/experiment); `S(n)` values and n=12 search facts cited as literature.
