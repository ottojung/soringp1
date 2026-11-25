# antonina-P7iMtLyEyaQc7U63VqLZo1-verse

Session: ses_e17fbf0ddffedzq7Fe4WHPXrPB
Workspace: /home/lubko/soring301-exec-d-quotient-20261117
Created: 1794893942621; updated: 1794894516576

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 59 (msg_1e80c9cc3001XZYR0B8RJVqGt2)

Inspected recovery state first: this worktree was clean at `HEAD 6a96398` with no pre-existing `./exec-report.md`, no local commits/PR/Lean/test artifacts for this task, and no durable local record of a completed post; I did not find evidence of external side effects to repeat, so I continued only the unfinished reporting/analysis work (board-post status outside local inspection remains uncertain and I did not post).

Completed work:
- Read `AGENTS.md`, `docs/problem.md`, `docs/research-plan.md`, `docs/research-winning-frontier-barrier.md`, `docs/research-compression-next.md`, and `/home/lubko/soring301-exec-optplay-lb-20261117/exec-report.md`.
- Analyzed the asked question for all-`n` optimal height-`S(n)` strategies with `(d1)` distinct labelled poset states, `(d2)` distinct unlabelled isomorphism classes, and `(d3)` minimum over optimal strategies.
- Recorded findings in `exec-report.md` (no commits/PRs/Lean).

Main conclusions (labeled deduction in the report):
- **(d1) lower bound (forced):** every correct reduced strategy has `n!` distinct labelled leaf total orders, so `d1(T) >= n!`; a nontrivial excess above `n!` for every optimal strategy / for `d3_{labelled}` was not established.
- **(d2) leaf collapse:** all `n!` leaves are isomorphic (chain), so the `n!` count does not transfer to unlabelled classes; no nontrivial all-`n` lower bound `> Omega(n)` or `> n!` for `d2/d3_{unlabelled}` was established.
- **Universal upper bound / falsifier:** for any optimal reduced tree, `d1(T), d2(T) <= 2*n! - 1 = 2^{Theta(n log n)}` (Stirling), hence `d3 <= 2^{O(n log n)}` for labelled and unlabelled distinct-state counts. This refutes any super-`2^{Theta(n log n)}` (e.g. `2^{Omega(n log^2 n)}`) all-`n` lower bound on the minimum over optimal strategies, while remaining consistent with the global winning-frontier existence of `2^{Omega(n log^2 n)}` states (which cannot all fit at one depth of a height-`S(n)` tree).
- **Open:** a meaningful stronger all-`n` lower bound for `d3` in the gap above trivial/`Omega(n)` but `<= 2^{O(n log n)}`, and an explicit infinite family of optimal strategies with provably small distinct quotient states (optimality is the main obstacle). No small-`n` experiments were run (guidance only per instructions).

No genuine new theorem/decisive frontier advance was claimed, so I did **not** post to `#301` as “SoringP1 frontier: optimal-strategy-distinct-quotient-states”.

Artifacts: `exec-report.md` in the worktree.
