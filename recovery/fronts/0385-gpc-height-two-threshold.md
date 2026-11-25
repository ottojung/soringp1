# gpc-height-two-threshold

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Qtck7L6yNI6USwgVua26Pt-styptics

## exit_state

clearexit

## question

Does every finite height-two poset satisfy the Gold Partition inequality e(P) >= F_{m(P)+2}, a class of unbounded width and dimension that is not covered by Peczarski's width-two, semiorder, or 11-element theorems?

## basis

Board #301 GPC/T(r) thread and the height-two-minimax-exact-complexity finding, which separates width-two Fibonacci evidence from height two and shows e(P)=e(Q) does not determine m; Peczarski Order 23 (2006); docs/research-obstruction-next.md. Height two is not the same class as width two, dimension two, or interval orders.

## falsifier

An explicit height-two poset, given by its two-level relation, with independently computed exact e(P) and m(P), satisfying e(P) < F_{m(P)+2}; the 11-element theorem forces at least 12 elements.

## implication

Height two contains the one-comparison family {0<1} disjoint-union A_{n-2}, whose minimax value is S(n)-1, so a positive result is a sound GPC class on states adjacent to the antichain root; a counterexample is the first GPC failure and refutes the global Fibonacci threshold. The threshold remains a sufficient condition, not a complete certificate.

## finding_unverified

an. No Lean or repository files were changed.

### Main mathematical finding: the all-`n` question is forced into a finite window

For height-two `P`, take `L` = minimal elements, `U` = maximal elements, `a=|L|`, `b=|U|`, `n=a+b`. Then `L,U` are antichains and all relations go from `L` to `U`. Two elementary bounds follow:

- `e(P) >= a! b!` — concatenate any permutation of `L` with any permutation of `U`.
- `m(P) <= S(a)+S(b)+n-1` — sort each part, then merge.

Using these, together with the literature and exact small `S(n)` values, any height-two counterexample to

\[
e(P)\ge F_{m(P)+2}
\]

must satisfy **`15 <= n <= 18`**, with only these minimax depths remaining:

| `n` | possible `m(P)` | residual `e` margin |
|---:|---|---|
| 15 | 40 or 41 | up to `2.13 ×` the minimum `7!8!` |
| 16 | 44 or 45 | up to `1.13 ×` the minimum `8!8!` |
| 17 | 49 | up to `1.39 ×` the minimum `8!9!` |
| 18 | 53 | up to `1.06 ×` the minimum `9!9!` |

`n=19` is excluded because `m<=57` and `F_59 < 9!10!`; `n=20,21,22` are excluded using exact `S(n)`; `n=23,24` using `S(23)<=76`, `S(24)<=81`; and `n>=25` by an exact split-by-split arithmetic check combining `a!b!` with `S(a)+S(b)+n-1`.

### Literature correction

The front’s “11-element theorem” is stale. Peczarski’s 2006 paper verified GPC through 11 elements, but Gupta, arXiv:2607.23926v2 (2026), Theorem 5, exhaustively verifies GPC through **14** elements. Hence the exhaustive frontier for the height-two Fibonacci target is `n<=14`, not `n<=11`.

### Failed approach / obstruction

I tried to force a counterexample from the antichain using the lower bound `m(P) >= S(n)-r` for a height-two poset with `r` cross relations. Exact sampling at split `7+8` showed the opposite of what was needed: the minimal `e` for each `r` stays far above `F_{S(15)-r+2}`. For example, at `r=10` the best sampled `e` was about `6.05e9`, while the Fibonacci threshold is only `F_{34}=5.70e6`; even at `r=42` the sampled minimum `e` was about `2.76e8`, far above `F_2=1`. So this route cannot create a violation.

Near-complete bipartite graphs also look unpromising: exact minimax for `K_{a,b}` minus a matching at `n<=10` gives only `S(a)+S(b)` or `S(a)+S(b)+1`, nowhere near `S(n)`.

### Honest limits

This is **not** a proof of the height-two Fibonacci inequality, and it is **not** a counterexample. It is a paper deduction plus exact arithmetic reducing the question to four finite orders. The `n=18` case is extremely tight — any counterexample would have `e` within about 5.6% of the complete-bipartite minimum — so it is the most constrained remaining case, while `n=15` is the most plausible place for a failure.

A counterexample would refute the global Fibonacci threshold, but it would **not** by itself give a `P`/`NP`/`PSPACE` separation. The Fibonacci threshold remains a sound sufficient certificate for sortability, not a complete characterization.
Inspected the durable state; no side effects were repeated.

- **Board #301:** the comment by `SoringP1 frontier: gpc-height-two-threshold` is present exactly once, timestamp `2026-11-08T17:50:45.446Z`. No second post was made.
- **Repository:** worktree is clean (`git status --short` empty). No commit, branch, Lean, or file change was created by the prior turn.
- **Unfinished work:** none from the prior turn. The research result and its honest limits were already reported and posted.

The prior turn completed successfully; I have not duplicated the board post or any other external action.

## Other metadata

```json
{
  "finished_at": 1794160343.2752721,
  "started_at": 1794157711.6043444
}
```
