# antonina-QIM5M7ZGKxuYvectK239JR-dish

Session: ses_e181ebb23ffex6z9rdf6w72qAw
Workspace: /home/lubko/soring301-exec-optplay-lb-20261117
Created: 1794891662662; updated: 1794892287541

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 118 (msg_1e7ea5f3c001zZZj0KiRxzOWbI)

## Recovery / side-effect check
- Worktree: `/home/lubko/soring301-exec-optplay-lb-20261117`, branch `exec/optplay-lb-20261117`, HEAD `6a96398` (clean before work; no prior `exec-report.md`).
- Read: `AGENTS.md`, `docs/problem.md`, `docs/research-plan.md`, `docs/research-winning-frontier-barrier.md`, `docs/research-compression-next.md`, `docs/operations.md`, `docs/literature.md`, `docs/research-certificates-barriers.md`.
- Board duplicate check (via `board_digest.py --contains "optimal-play-reachable-quotient-lower-bound"`, page 1): **no match found**. No prior durable record of this specific question found in this worktree. No commits/PRs/Lean/tests created; **no Antonina #301 post made** (no definitive “genuine new theorem” established beyond clarification deductions; posting deferred to avoid uncertain/low-signal external side effect).

## Question addressed
All-`n`, falsifiable: stronger lower bound on states (labelled or unlabelled/quotient by Aut) that must appear on **some** optimal height-`S(n)` strategy/tree beyond `n!` leaves (e.g. `2^{Ω(n log^2 n)}` or super-`2^{Θ(n log n)}`), or an infinite family of optimal strategies with smaller (polynomial / `2^{O(n log n)}`) state/quotient count. Distinguished (a) budget-root-reachable, (b) information-admissible, (c) locally viable `d+F(P)≤S(n)`, (d) on some optimal strategy. Assessed whether winning-frontier `2^{(1/4-o(1))n log^2 n}` states can be bridged to (d) or are separated.

## Findings (evidence-labeled, recorded in `exec-report.md`)
- **[deduction, definition] Counting model clarified:** for (d), distinguish labelled node occurrences, distinct labelled posets, and distinct unlabelled/Aut (poset-isomorphism) classes. A reduced correct comparison tree has exactly `n!` leaves and `2*n!-1` nodes; optimal height-`S(n)` trees exist (model attainment).
- **[deduction] D1 (upper bound / refutes super-`2^{Θ(n log n)}` node-count growth on d):** every optimal reduced tree has `2*n!-1 = 2^{Θ(n log n)}` labelled node occurrences total (`log n! = Θ(n log n)`). Hence, in node/state-occurrence terms, (d) admits an all-`n` upper bound `2^{O(n log n)}` (take any optimal reduced tree) and cannot satisfy a super-`2^{Θ(n log n)}` (e.g. `2^{Ω(n log^2 n)}`) lower bound. Quotienting labels by Aut can only decrease counts, so the minimum unlabelled class count over optimal strategies is also `≤ 2*n!-1 = 2^{O(n log n)}`.
- **[deduction + paper-level theorem citation] D2 (winning frontier separated from “all on one optimal tree”):** any height-`S(n)` binary tree has `≤ 2^d ≤ 2^{S(n)} ≤ 2^{O(n log n)}` nodes at depth `d` and `≤ 2^{O(n log n)}` total. The winning-frontier construction (`docs/research-winning-frontier-barrier.md`, including extension to budget `S(n)` via Sergeev `S(n)-C(n)=o(n)`, asymptotic) yields `2^{(1/4-o(1))n log^2 n}` nonisomorphic winning states at a common depth with remaining budget - far exceeding what any single optimal strategy can contain at that depth. Therefore the full frontier **cannot be bridged** onto one optimal play path/tree; this is an upper/capacity separation, not a proof that some optimal strategy visits many frontier states.
- **[deduction, partial] Quotient note:** leaves are all Aut-isomorphic as total orders (class count 1), so “beyond trivial leaves” is nontrivial only for internal/distinct structure; unlabelled (d) still inherits the `2^{O(n log n)}` upper bound from D1.
- **[context, not re-proved]** Prior stated fact used: (a)-(c) are not all on some optimal strategy for `n=5,6` (optimal-viable-state-counting).

## Status / open (no definitive resolution claimed)
- **Not proved here:** a stronger all-`n` lower bound on (d) in terms of *distinct* internal labelled posets or *distinct* unlabelled classes required by every/some optimal strategy beyond trivial leaf/permutation forcing.
- **Not constructed here:** an infinite family of optimal strategies with polynomial or `o(n log n)`-exponent distinct-state/quotient count (only the trivial `2^{O(n log n)}` optimal-tree upper bound is observed).
- **Not settled:** whether some optimal strategy must pass through a large (`2^{Ω(n log^2 n)}` or other super-`2^{Θ(n log n)}`-class) subset related to the winning frontier; D2 rules out containing the whole family/per-depth realization, but positive bridging remains open.

## Durable evidence
- `exec-report.md` created in worktree root with full evidence-labeled writeup, definitions, D1/D2, open items, and suggested next falsifiable steps (precise (d1)-(d3) counting; small-`n`/structural reuse checks; attempts to force many nonisomorphic outcomes along any optimal strategy). Worktree now has this untracked report only.
