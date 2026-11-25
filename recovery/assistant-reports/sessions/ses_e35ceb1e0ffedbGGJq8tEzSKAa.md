# antonina-cbuVhug7i8h6KHkkWxkXbY-premature

Session: ses_e35ceb1e0ffedbGGJq8tEzSKAa
Workspace: /home/lubko/soring-fronts/fibonacci-threshold-n8-20261111
Created: 1794393591352; updated: 1794403434509

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 404 (msg_1cac724dc001YsVJS36knkNEIM)

## Recovery / side-effect check
- CWD `/home/lubko/soring-fronts/fibonacci-threshold-n8-20261111` was initially empty (no git, no prior artifacts).
- Checked board #301 (latest page): no prior n=8 Fibonacci-threshold result posted. Latest relevant was 2026-11-11T10:39:58Z (“n=8 extension front is now running”, n≤7 verified). `fibonacci-threshold-20261111/` had n≤7 local report only (not posted). No duplicate posting performed.
- External side effect performed **once**: posted ONE comment to issue #301.

## Work performed (this attempt, scratch only)
- Read model/context from prior verified fronts (`exec-fibonacci-threshold-proof-20261107/docs/problem.md`, `solve_fib.py`, `xec_fibthr.py`): `e(P)` = #linear extensions (subset DP), `m(P)` = exact partial-order minimax comparison depth, test `e(P) >= F_{m(P)+2}` (`F_1=F_2=1`).
- Implemented/ran `n8_fib.py` (imports `fibonacci-threshold-20261111/solve_fib.py`) for unlabelled n=8 via canonical reachability from 8-antichain.
- **Enumeration/class-count:** complete and verified — `classes=16999`, `expected=16999 (A000112)`, `ok=True` (15.642s).
- **Exact (e,m) exhaustive evaluation:** not completed in-session. At last observation (2026-11-11T13:22:29Z) computation process had ~08:07 elapsed, 99.9% CPU, ~2.25 GB RSS, with **no progress checkpoint** (logged every 500) => **completed fraction 0 <= done < 500 of 16999** (exact count below 500 unknown from logs), **minimizer-so-far / min slack-so-far unknown** from this run, **no violations observed** (coverage insufficient).
- **Bottleneck:** exact memoized poset-state minimax `m(P)` on n=8 (16999 classes); >8 CPU-minutes yielded <500 classes, indicating a long run (likely hours) to exhaust all 16999. Not a certified boundary/disproof.

## #301 posting
- Posted successfully (single comment, no duplicates):
  - **Issue:** #301 (SoringP1: Lean-checked complexity of optimal sorting numbers)
  - **Author:** `SoringP1 frontier: fibonacci-threshold-n8-20261111`
  - **Created:** `2026-11-11T13:23:21.897Z`
  - **ID:** `sha256:8ABvRUZi3rvIiK7v2rFhqYvctR-i-X1hXNgNxMIy2Jg`
  - **Content:** violator-or-boundary status = **incomplete** (neither certified), exact class-count check (16999 ok), exact partial-progress bounds (<500/16999), measured bottleneck, code paths, and honest limits (no n=8 boundary/violator claimed, no all-n claim). Reported as blocker/incomplete per instructions.

## Local artifacts (scratch, cwd only)
- `/home/lubko/soring-fronts/fibonacci-threshold-n8-20261111/n8_fib.py`
- `/home/lubko/soring-fronts/fibonacci-threshold-n8-20261111/n8.log`
- `/home/lubko/soring-fronts/fibonacci-threshold-n8-20261111/comment_301.md`
- Background computation from this attempt may still be running in cwd (observed PID 22333, `python3 -u n8_fib.py 8 10600`, logging to `n8.log`) — if it completes later, any follow-up result must be posted carefully to avoid duplication.

No repo/Lean/PR/workflow changes made. Post made to #301; exiting 0.
