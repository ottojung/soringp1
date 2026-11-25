# antonina-oBR9EFfBunDZfpeKXXJeqp-tuesday

Session: ses_e178f187dffe0LzgtM0Zm0I6eZ
Workspace: /home/lubko/soring301-exec-framed-dag-n13-20261117d
Created: 1794901075958; updated: 1794901346078

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 139 (msg_1e874dafb001RfSCGQivE8TLxT)

Produced an explicit, checked permutation-framed strategy DAG certificate for `n=13` (non-optimal) and documented why an exact-height-`34` witness was not constructed/verified in this attempt.

**Durable artifacts (worktree):**
- `exec-report.md` — required report: (1) problem statement and `S(13)` baseline, (2) methods/tools/commands, (3) concrete results/witness or obstruction with evidence, (4) verification performed, (5) open questions/next falsifiable step.
- `witness_bubble_n13.json` — explicit framed DAG certificate (bubble/compare-exchange path) for `n=13`.
- `strategy_dag_n5.txt` — `scripts/strategy_dag_probe.py --max-n 5` output (small-`n` optimal state-DAG/hash-consing/quotient measurements used as evidence).

**Key results (precise):**
- Baseline: `13!=6,227,020,800`, information lower bound `ceil(log2(13!))=33`; `S(13)=34` (OEIS A036604 / Peczarski 2004, as cited in-repo).
- **Checked framed DAG witness (best verified here):** `witness_bubble_n13.json`, `n=13`, `budget=78`, **depth 78, 79 nodes, 156 edges** (linear path). Verification: `python3 scripts/check_framed_strategy.py --bubble 13` and programmatic `check_certificate(...)` both **ACCEPT** (`ACCEPT: n=13, depth=78, nodes=79`).
- **Exact-height-34 framed DAG:** not produced/verified. Context/evidence: `F_FJ(13)=34` equals `S(13)` and `merge_sort_wc(13)=37`, but no implemented/audited framed FJ/merge DAG generator or transcribed literature-optimal strategy in checker format was available; exhaustive optimal strategy/DAG construction is infeasible at `n=13` (`13!` states; rapid poset/state-DAG growth per probe/docs). See `exec-report.md` for the concrete falsifiable obstruction/availability-scale evidence and the next falsifiable step (audited FJ or literature transcription into a checker-accepted height-34 framed DAG, or a concrete failing invariant).
