# antonina-8rt7ow8JStVuzAjFcb1re1-shone

Session: ses_e17b212d4ffeZImzTWUbnSntqV
Workspace: /home/lubko/soring301-exec-framed-dag-n12-20261117b
Created: 1794898783533; updated: 1794899399029

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 151 (msg_1e85719cb001dJ6pw2MnsWbQzy)

Inspected worktree state first (recovery check): clean git status, no pre-existing `exec-report.md` or `*witness*n12*`/`*framed*dag*n12*` artifacts, and the mentioned tools/docs present (`scripts/check_framed_strategy.py`, `scripts/strategy_dag_probe.py`, `docs/research-framed-certificate-frontier.md`, etc.). No prior external side effects from this task were found to continue or duplicate.

**Work completed (durable artifacts in this worktree)**
- `exec-report.md`: problem statement and `S(12)` baseline incl. gap vs `C(12)`, methods/tools/commands, concrete results/witness and obstruction with evidence, verification performed, and open questions/next falsifiable step.
- `witness-bubble-n12.json`: explicit permutation-framed strategy DAG certificate for `n=12` (generated via `triangular_bubble_certificate(12)`).

**Key results (claims labeled)**
- **Literature/stated baseline (not re-proved):** `S(12)=30`, while `C(12)=ceil(log2(12!))=29` (gap `+1`); see `docs/problem.md`, `docs/literature.md`/Peczarski 2012, Wells, OEIS A036604 context.
- **Computed:** `12!=479001600`, `log2(12!)≈28.835455` ⇒ `C(12)=29`; `F_FJ(12)=∑ ceil(log2(3j/4))=30` (matches `S(12)` as a value, **not** a framed-certificate construction); standard merge-sort recurrence `M(12)=33`; triangular bound `66`.
- **Verified framed DAG witness (best verified height produced):** `witness-bubble-n12.json` — `n=12`, `budget=66`, checker `ACCEPT: depth=66, nodes=67`, `132` outcome edges (66 comparison nodes + 1 leaf, length-66 compare-exchange path). This is an explicit checkable certificate but **not** optimal (far above 30).
- **Exact-height-30 framed DAG for `n=12`:** not produced/verified. Obstruction/evidence documented: no existing FJ/merge-sort framed-cert generator in repo; FJ height-30 candidate requires full recursive frame/join construction with pending audit (`docs/research-framed-certificate-frontier.md` §3); optimal-policy/minimax DAG enumeration infeasible at `n=12` (small-`n` context from `strategy_dag_probe.py --max-n 5` included in report); unshared optimal trees can be exponentially large so sharing/join correctness is the hard part.
- **Verification performed:** `python3 -m unittest tests/test_framed_strategy.py` → 6 tests OK; `check_certificate`/CLI acceptance of `witness-bubble-n12.json` (`depth=66`, `nodes=67`). No literature re-proof, no height-30 witness, no Lean/kernel changes.

**Next falsifiable step (see report §5):** implement/generate an explicit framed certificate for a height-30 candidate at `n=12` (e.g. fully specified Ford–Johnson, since `F_FJ(12)=30`) and check with `python3 scripts/check_framed_strategy.py <witness>` for `ACCEPT` with `depth<=30`; alternatively implement the §2/§3 framed generators to obtain smallest-budget *verified* constructions with measured profile.
