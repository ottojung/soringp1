# r-valued-relaxation-ladder-exact-evaluator-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

vgMPA21ZjfLhkwQjcNdcAf-reopening

## exit_state

clearexit

## question

For r-valued labelled keys under the (value,index) tie convention, let B_r(n) be the minimum height to sort all r^n assignments, so B_2(n)=B(n) and B_n(n)=S(n), with B_r monotone in r by subset embedding. Can the whole ladder B_2(n), B_3(n), ..., B_n(n) be evaluated in total time 2^{o(n log^2 n)} uniformly in n, giving a new exact route to S_unary(1^n)?

## basis

Computed B(n) far below S(n) in the faithful tie convention; Sergeev's o(n) surplus; the winning-frontier barrier excluding transcript enumeration; no r-valued relaxation ladder among the 657 ledger fronts.

## falsifier

Show that some intermediate r already forces a state space of size 2^{Omega(n log^2 n)}, so no ladder method beats the known exponent, or that the r-valued relaxations lose exactness before r=n; small-n computation of B_3(n) and B_4(n) is the first discriminating check.

## implication

Either a faster uniform exact evaluator for S_unary(1^n) or a method-family barrier for relaxation-based evaluation. No membership claim for SORT-BOUND-U in P, NP, or a smaller class follows directly.

## finding_unverified

(β+o(1))n log n`, dividing `binom(M,m)` by `n!` labellings yields

`≥ 2^{(β(1−β)−o(1))·n log₂²n}` nonisomorphic reachable winning states at budget `B_r(n)`

(β=1/2 recovers the repo's 1/4 constant; `k` is pinned by `ceil(log₂|X_r|) ≤ B_r(n) ≤ S(n)=log₂(n!)+o(n)`, Sergeev TR20-096 Thm 3). Hence any evaluator of such a rung that enumerates its winning state space needs `2^{Ω(n log₂²n)}` time — the known exponent. Only subpolynomial rungs are cheap, and there `B_r(n)=O(n log r)=o(S(n))` with an Ω(n log n) value gap, so no cheap correction formula recovers `S(n)`'s leading term.

**Horn B [deduction].** `B_r(n)≤S(n)` is sound but complete only at r=n; a winning frontier state is a sound certificate `B_r(n)≤k`, not a complete evaluator. General-poset excess `F(P)−⌈log₂e(P)⌉` is unbounded on arbitrary posets but does not transfer to the fixed outcome family `X_r`.

## Honest limits

- This is an **enumeration barrier**, not a general time lower bound. The strict claim "whole ladder in `2^{o(n log²n)}`" is **not** refuted for selective/compact/symbolic methods; selective minimax is exactly what the source barrier doc leaves open.
- No membership or separation for `SORT-BOUND-U` in P/NP/PSPACE follows; tally/sparse constraints still apply. Sergeev is used only as an asymptotic, non-effective `o(n)` surplus (no finite threshold).
- Web search was cancelled in this environment; literature relies on the repo's curated baseline and the local Sergeev text, noted as such in the post.
- n=7 completed only for r=2 (r=3,4 hit the time cap); no all-`n` formula for `B_r(n)` is claimed from finite data.

Scratch record: `/tmp/opencode/rval_ladder_finding.md`, `rval_eval.py`, `rval_subset.py`.
I'll do a read-only audit to confirm what already happened. I will not post, commit, or otherwise write anything.
## Read-only recovery audit — result: work already complete, nothing to redo

**Git state.** Branch `billy-dev`, clean working tree, HEAD `6a96398`. Reflog contains only the original clone — **no commits, branches, or repo/Lean/test/CI/ledger changes** were made by this front.

**Board #301.** Exactly **one** post by this front: 2026-11-21T22:32:16.290Z, author `SoringP1 researcher: r-valued-relaxation-ladder-exact-evaluator-alln`, body length 3858 — the RESULT comment containing the finding. (The newest board message, 22:35:43Z, belongs to a *different* front, `binary-test-universe-height-gap-alln`; I did not touch it.) Count of my posts = **1**, so no duplicate post occurred and none is needed.

**Durable scratch records** all intact under `/tmp/opencode`: `rval_ladder_finding.md`, `rval_eval.py`, `rval_subset.py`, `rval_post_body.md`, `rval_post_result.json`.

**Effects that actually happened in the prior turn:** scratch computation + one board comment. **Effects that did not:** any repository mutation, any second post, any commit/purchase/other external action.

**Unfinished work:** none. The research task's deliverable (a mathematical finding with honest limits) was produced and reported in that single post: the model validation, the exact `B_r(n)` table, the frontier-enumeration barrier on every polynomially large rung `r=n^β`, the subpolynomial-rung exactness loss, and the explicit scope caveats (enumeration barrier only; no complexity-class claim). The `n=7, r=3,4` computations that timed out were explicitly recorded as an honest limit, not an outstanding obligation.

No further external action taken this turn — I only read Git state and the board.

## Other metadata

```json
{
  "finished_at": 1795300887.8322747,
  "started_at": 1795299334.5167873
}
```
