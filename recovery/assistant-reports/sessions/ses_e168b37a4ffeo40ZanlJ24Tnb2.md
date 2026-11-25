# antonina-UFVRBI070zkX0TZ3i1QcVR-theory

Session: ses_e168b37a4ffeo40ZanlJ24Tnb2
Workspace: /home/lubko/soring301-exec-framed-dag-n8-opt-20261117
Created: 1794918107279; updated: 1794918450524

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 160 (msg_1e979e425001XXiG9zYys0m3ah)

Created `exec-report.md` in the worktree (only added file; `git status` shows `?? exec-report.md`). No repo/Lean/PR changes.

**Outcome (framed-dag optimal n8 construct, #301):**
- **No explicit height-16 framed DAG certificate for `n=8` constructed.** Not a proof of infeasibility: `S(8)=16` is known (literature) but no audited in-repo framed embedding of an optimal strategy exists, and available exact search/export tooling was computationally insufficient here (`scripts/generate_optimal_tree.py` timed out at `n=7`/60s; `scripts/evaluate.py` returned `10` for `n=6` but timed out at `n=7`/120s), so obtaining/encoding an optimal `n=8` strategy was obstructed in this attempt.
- **Best verified partial artifact (correct, larger DAG):** explicit permutation-framed comparison DAG `triangular_bubble_certificate(8)` from `scripts/check_framed_strategy.py`.
  - **Exact size/properties:** `n=8`, `depth=28`, `budget=28`, `nodes=29`.
  - **Verification (checker):**
    - `python3 scripts/check_framed_strategy.py --bubble 8` → `ACCEPT: n=8, depth=28, nodes=29`
    - Programmatic check: `triangular_bubble_certificate(8)` / `check_certificate(...)` → `nodes 29 depth 28 budget 28`
  - **Baseline:** `python3 -m unittest tests/test_framed_strategy.py` → `Ran 6 tests ... OK` (0.011s)

Full labeled evidence, method, considered routes (direct tree framing, Ford–Johnson embedding status per `docs/research-framed-certificate-frontier.md`, tooling limits), verification outputs, and limits/next decisive steps are in `exec-report.md`.
