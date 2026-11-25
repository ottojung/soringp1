# antonina-kcookLUJNaEMT052En7jIm-status

Session: ses_e168b3818ffesalR6dWkdT4yg9
Workspace: /home/lubko/soring301-exec-certsize-lowerbound-smalln-20261117
Created: 1794918107186; updated: 1794918255680

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 100 (msg_1e976e180001nbGLEE8NexcuYx)

Created `exec-report.md` in the worktree with the requested analysis.

**What was done**
- Read and followed: `AGENTS.md`, `docs/problem.md`, `docs/research-plan.md`, `docs/research-framed-certificate-frontier.md`, `scripts/check_framed_strategy.py`, `scripts/strategy_dag_probe.py` (plus related tests).
- Reproduced/extended experiments for small `n`:
  - Ran `python3 scripts/strategy_dag_probe.py --max-n 5` and `python3 scripts/check_framed_strategy.py --bubble 4`.
  - Computed single-policy/poset-DAG/quotient data for `n<=6` and all-optimal union/quotient data for `n<=6` using repo script logic.
- Analyzed minimal permutation-framed DAG certificate sizes among optimal height-`S(n)` strategies/canonical optimal-play quotients vs optimal decision-tree size `2*n!-1`, with structural compression limits/enablers and careful all-`n` extrapolation (conjecture/obstacle).

**Key concrete findings (reported in `exec-report.md`)**
- For `n<=6`, single optimal policies show no poset-state hash-consing compression: poset DAG nodes = unshared tree = `2*n!-1` (`1,3,11,47,239,1439`) with `n!` leaves and canonical quotient state counts `1,2,4,7,11,27`.
- All-optimal unions share many states (`1,3,19,181,1551,65551` for `n<=6`) with small canonical quotients (`1,2,5,12,19,134`), but sound permutation-framed joins are structurally constrained by relation intersection/information loss.
- Best supported explicit optimal framed-certificate size in this study is `2*n!-1` for `n<=6` (no smaller sound optimal-height framed DAG demonstrated); compression below tree scale remains obstructed for examined optimal strategies.
- `n=7` was not computed (not tractable in-session); extrapolation beyond `n<=6` is stated as conjecture/obstacle with evidence.

**Worktree changes**
- Created only: `exec-report.md` (no repo/Lean/PR changes).
