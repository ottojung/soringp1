# antonina-qSSu0wyExFCz4yTNdXsyym-brick

Session: ses_e166d4e25ffe9mc2cFV8uROWZo
Workspace: /home/lubko/soring301-exec-pathwidth-optimal-strategy-20261117
Created: 1794920067576; updated: 1794920255929

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 105 (msg_1e9955a220010Y9vOajQr6dTwI)

## Completed (SoringP1 #301, treewidth/pathwidth of optimal strategy state graph)

- **Read (as requested):** `AGENTS.md`, `docs/problem.md`, `docs/research-plan.md`, `docs/research-framed-certificate-frontier.md`, `docs/research-winning-frontier-barrier.md` (and consulted related repo sources used for definitions/data/arguments: `docs/research-strategy-certificates.md`, `docs/research-compression-next.md`, `docs/research-state-compression.md`, `scripts/strategy_dag_probe.py`).
- **Question addressed (all `n`, falsifiable):** for the directed state graph of a height-`S(n)` optimal comparison strategy (reachable poset states / canonical optimal-play states, outcome edges), characterized bounded vs polynomially-bounded vs unbounded **treewidth/pathwidth/branchwidth**, with small-`n` computation, all-`n` structural argument/obstruction, and relation to compact (polynomial-size) certificates/evaluators.
- **Small-`n` computation (experiment, `n<=5`, reproducible via `scripts/strategy_dag_probe.py` logic):** one optimal single-policy state graph (distinct reachable labelled posets) is a tree with `V=2*n!-1`, `E=V-1`, height `S(n)`; results `n=1..5`: `(S,V,tw,pw)=(0,1,0,0),(1,3,1,1),(3,11,1,2),(5,47,1,4),(7,239,1,6)`.
- **All-`n` findings (deduction, labeled in report):**
  - **Single-strategy history/labelled-poset graph (H/L):** underlying graph is a tree (hash-consing gives no sharing for a reduced single policy) ⇒ **treewidth = 1, branchwidth = 2 (bounded/constant, `n>=2`)**; **pathwidth unbounded but polynomially bounded** (`O(S(n))=O(n log n)` in numeric/unary terms), Θ(S(n)) on samples.
  - **Canonical quotient / all-optimal DAG forms:** width parameters left **open** (no all-`n` bound/obstruction derived here); sizes/growth discussed from repo evidence.
  - **Certificates/evaluators:** bounded width of this strategy tree does **not** imply compact (polynomial-size) representation (`Θ(n!)` nodes); compactness depends on polynomial graph size (open at exact `S(n)` for unary `SORT-BOUND-U` NP-certificate route), with width only conditionally useful if compact graphs exist.
- **Deliverable:** `exec-report.md` in this worktree, containing labeled evidence (`[definition]`, `[literature]`, `[deduction]`, `[experiment]`, `[open]`/`[conjecture]`), definitions, data table, all-`n` arguments, and implications.
- **Scope compliance:** no repo/Lean/PR changes; only `exec-report.md` created in this worktree. No builds/tests modified or required.
