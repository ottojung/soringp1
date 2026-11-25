# antonina-myCZ964GBTrnRO2FVk6ud1-expectant

Session: ses_e181f1a0affeInr8YpEQcuf6x1
Workspace: /home/lubko/soring301-exec-space-dfs-20261117
Created: 1794891638310; updated: 1794892290124

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 159 (msg_1e7ea9160001a8FFhKFUve5bBa)

**Recovery/state inspection (no duplicated external actions)**
- Worktree: `/home/lubko/soring301-exec-space-dfs-20261117`, HEAD `6a96398`, git status clean before work; no pre-existing `exec-report.md`.
- Checked Antonina board #301 (pages 1–4) for title/phrase `SoringP1 frontier: budgeted-dfs-space-lower-bound`: no prior match found. No commits/PRs/Lean changes made.

**Work completed**
- Read required materials: `AGENTS.md`, `docs/problem.md`, `docs/research-plan.md`, `docs/research-budgeted-dfs.md`, `docs/upper-bound.md`.
- Recorded durable evidence in `./exec-report.md` (uncommitted), including recovery/side-effect audit, space decomposition, baseline bounds, and evidence labels.
- Posted one concise, evidence-labeled summary to Antonina board issue #301: **“SoringP1 frontier: budgeted-dfs-space-lower-bound”** (author `soring301-budgeted-dfs-agent`, 2026-11-17T05:10:57.960Z, id `sha256:PvPTkBtgongeteVJQCH9ty4viFEvKg0pS-jffcDz_AQ`), verified present. No duplicate post.

**Research result (falsifiable, method-class barrier)**

Question: can exact evaluation of `S(n)` / decision of `SORT-BOUND-U` by budgeted-DFS/exhaustive game search be done in `o(n log^2 n)` bits work space (numeric `n`, uniform deterministic) while keeping sub-`2^{O(n^2)}` time?

- **(a) Space-improved algorithm:** none found. Baseline transcript-only budgeted DFS remains `O(n log^2 n)` bits for numeric-`n` evaluation (`O((d+n)log(n+2))`, `d<=U(n)=O(n log n)`), with `2^{O(n log^2 n)}` time; decision form `O(N log(N+2))` in unary input length `N=n+k+1` (per `docs/research-budgeted-dfs.md`).

- **(b) Barrier [deduction, C_path]:** for a clearly stated class **C_path** (deterministic transcript/path-storing budgeted DFS that stores, at depth `t`, an explicit ordered path sufficient to identify the `t` comparison outcomes and resume ancestor candidate/cursor choices after backtracking; may recompute comparability/reachability in separate reusable workspace; sub-`2^{O(n^2)}` time), any successful run reaching depth `S(n)` needs `Omega(S(n) log n)=Omega(n log^2 n)` bits for all sufficiently large `n` (information bound `S(n)=Theta(n log n)`, `Theta(log n)` bits per level for move/outcome/cursor-resumption). Thus `o(n log^2 n)` (incl. `O(n log n)`, `O(n)`, polylog in relevant regime) is obstructed for C_path. Time is orthogonal.

- **Space decomposition (precise):** path/stack `Theta(t log n)`; poset/state implicit in transcript-only vs closure-matrix-per-frame `Theta(d n^2)` (worse, `Theta(n^3 log n)`); reachability workspace reusable `O(n log n)` (`n` visited bits + queue/stack of labels) or `Theta(n)`–`Theta(n log n)`; counters `O(log n)`–`O(log(d+n))`. Peak transcript-only: `Theta(t log n + n log n)`.

- **Other classes [open/partial, not a theorem]:** closure-storing DFS is worse; checkpoint/replay or Savitch-style path recomputation may trade time for path storage but no concrete `o(n log^2 n)`-bit scheme with correctness and preserved sub-`2^{O(n^2)}` time was established here; non-path-storing/exhaustive paradigms outside C_path remain open. No universal lower bound for all algorithms claimed.

- **Consequences:** method barrier only; does **not** claim complexity separations and does not change `SORT-BOUND-U ∈ PSPACE` / existing upper bounds. Falsifier for §2: a C_path algorithm using `o(n log^2 n)` bits on an infinite family (or all sufficiently large `n`) while correct and sub-`2^{O(n^2)}` time.

Full details and evidence labels are in `exec-report.md`. No repo files were modified beyond creating `exec-report.md`; no Lean/tests/commits/PRs.
