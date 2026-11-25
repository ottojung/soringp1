# antonina-BIJ0zYB6gzPtG3KruErsKa-remedies

Session: ses_e181eeb9cffeBTfZUFTQkIJd3Y
Workspace: /home/lubko/soring301-exec-dag-lb-20261117
Created: 1794891650272; updated: 1794892304071

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 123 (msg_1e7eacc830012RmguZ94FTMnxC)

Inspected state first (recovery): `AGENTS.md` and the requested docs were read; worktree is clean at `HEAD 6a96398` (`git status` empty, recent log matches). No `exec-report.md` existed before this run. Antonina board #301 digest check (page 1, `--contains "optimal-framed-dag-node-lower-bound"`) found no matching title; recent board messages were reviewed and none matched this task. No durable local/board evidence of a completed post or other external side effect was found; prior interrupted-turn effects remain unobservable beyond this, so I did not repeat any external action.

Durable evidence written: `./exec-report.md` (`SoringP1 frontier: optimal-framed-dag-node-lower-bound`, 2026-11-17).

Assessment (evidence-labeled, no complexity-class separations claimed):
- **[deduction] F1:** Every sound certificate certifying `S(n) <= k` has path length / depth lower bound `k >= S(n) >= ceil(log2(n!)) = Ω(n log n)` (trivial, all representations/classes).
- **[deduction, supported by literature/repo] F2 (natural restricted class):** Every **unshared framed decision tree** (no feasible joins/history sharing) has `>= n!` terminals and `>= 2n!-1 = 2^{Θ(n log n)}` nodes/edges for all `n`, since each of the `n!` input orders induces a unique feasible outcome path in a deterministic tree and must be correctly certified.
- **[paper construction in repo, audit pending] F3:** Join-enabled framed permutation DAGs admit polynomial-size certificates at non-optimal heights (e.g. merge-sort `O(n^2)` nodes at `O(n log n)` height; plausible rank-envelope/Ford–Johnson upper-bound family; bubble witness in `scripts/check_framed_strategy.py`), so there is no universal superpolynomial lower bound for the unrestricted framed-DAG class without a height/optimality restriction.
- **[open] F4/F5 (optimal height `S(n)`):** No all-`n` polynomial-size framed DAG/certificate family at height `S(n)` is constructed/exhibited, and no superpolynomial/exponential node/edge lower bound for **every** join-enabled framed DAG at height `S(n)` is proved here. Exact obstruction (from repo frontier): known poly framed families are too tall (merge sort) or not proved exact/fully framed at all `n` (FJ embedding), Sergeev-compatible near-optimal strategies lack a proved polynomial global framed join/state grammar, and the winning-frontier barrier (`2^{(1/4-o(1)) n log^2 n}` nonisomorphic winning states at budget `S(n)`) rules out raw state/transcript enumeration but is not itself a framed-DAG size proof.
- **[deduction] Framed vs unframed/completeness:** framed slot-permutation+intersection joins compress differently from labelled-poset hash-consing/`S_n` quotient; completeness at optimal height requires simultaneous height `S(n)`, soundness/completeness for all inputs, and explicit poly-checkable DAG size—no known construction satisfies all three.

Conclusion: alternative **(a)** holds provably for the unshared framed decision-tree class (`2^{Θ(n log n)}`) but not established for unrestricted optimal-height framed DAGs; **(b)** is not exhibited (open). I treated this as a consolidation/obstruction analysis rather than a genuine new theorem-level finding, so I did **not** post to Antonina board #301 (and no duplicate title was found). No repo commits, PRs, or Lean changes were made.
