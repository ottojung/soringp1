# reachable-state-fibonacci-inequality

## status

investigated

## origin

ai_proposal_unverified

## agent_id

WTFVNEH55I6AMfwHkXOduj-permeated

## exit_state

clearexit

## question

For every n and every poset P reachable from the n-element antichain along some height-S(n) optimal comparison strategy, does the Fibonacci extension inequality e(P) >= F_{m(P)+2} hold, where m(P) is the exact minimax continuation cost and F_1=F_2=1?

## basis

docs/research-core-threshold.md reports T(r) only for r<=8 against all posets and leaves the all-r inequality open; docs/research-width-two-threshold.md derives it only for width two, while the antichain root has width n, so the reachable-state restriction is untouched.

## falsifier

Exhibit an explicitly reachable poset P with an optimal-path reachability witness and a minimax computation giving e(P) < F_{m(P)+2}; since the inequality is reported only for width-two posets and for all posets with m at most 8, any counterexample must have m(P) at least 9.

## implication

A positive answer would supply a sound, cheap lower-bound invariant on continuation cost for antichain-reachable states and could tighten pruning in exact evaluators; a reachable counterexample confines the Fibonacci route to general posets and removes it from antichain-root algorithms.

## finding_unverified

uestion.
The minimax computation is too expensive for the full danger zone. Let me verify my key theoretical findings with exact arithmetic on the tractable ranges.
Let me check the posting interface and prepare the report.
I have my findings. Let me post a concise report to board #301.
## Report — `reachable-state-fibonacci-inequality` (billy-dev)

I attacked the front claim and tried seriously to **disprove** it. **No counterexample was found; the claim remains open.** I posted the full finding to board #301 (author `SoringP1 frontier: reachable-state-fibonacci-inequality`). The worktree is clean at `6a96398` — no Lean, test, note, PR or ledger changes; all scratch is in `/tmp/opencode/rfib`.

### What I established

1. **Logical position** `[literature + deduction]`. `e(P) ≥ F_{m(P)+2}` for *all* finite posets follows from Peczarski's Gold Partition Conjecture (GPC), open in general but proved for width two and for every poset on ≤14 elements (Gupta, arXiv:2607.23926v2). The verified threshold `T(10)=232` additionally gives the inequality for all posets with `m ≤ 11`. So any counterexample — reachable or not — needs **n ≥ 15, m ≥ 12, and `F_{m+1} ≤ e ≤ F_{m+2}−1`**. A reachable counterexample would refute GPC; a positive answer here would *not* prove GPC.

2. **Obstruction to the natural transfer** `[deduction, new]`. For any fixed `Q`, the padded poset `A_k ⊔ Q` satisfies Fib for all sufficiently large `k`: `e = (k+q)!/q!·e(Q)`, while `m ≤ S(k)+m(Q)+(k+q)−1`, and the `k log₂k` term in `log₂ e` dominates `0.694·FJ(k)` (exact integer check: sufficient bound holds for all `k ≥ 18` when `q ≤ 12`). Chain padding repairs it likewise. **An arbitrary counterexample cannot be converted to a reachable one by padding** — so the reachable restriction is not reducible to the general case by the standard closure, and a reachable counterexample must be found directly. This is the requested distinction between general-poset results and the antichain-root question.

3. **Finite check** `[experiment]`. Exact BFS over all states reachable along a height-`S(n)` optimal strategy for `n ≤ 5` (1,551 states at `n=5`): zero Fib violations and zero failures of the balancing property (optimal comparison with child depths `m−1` and `≥ m−2`). `n=6` did not finish in 80 s.

4. **Staircases are excluded at small `n`** `[experiment/deduction]`. The Fib-tight `W_n` (`e=F_{n+1}, m=n−1`) has `c(W_n)+m(W_n)=2n−2 > S(n)` for `4 ≤ n ≤ 11` (`c` = cover count = minimum comparisons to build it), so it is not reachable along an optimal strategy there. At `n=12` equality holds, so this is not an all-`n` exclusion.

5. **Soundness ≠ completeness** `[deduction]`. Fib is a *sound* one-way invariant (`m ≤ ~log_φ e`), so small-`e` states can be declared finished. It is **not** a complete continuation-cost test — the converse is precisely the open inequality — so no pruning improvement for exact evaluators follows without the missing proof.

### Failed disproof and exact obstruction

The danger zone is narrow but computationally hard: exact minimax on one boundary case (`W_13`, `e=377`, `n=13`) exceeded 120 s, putting an exhaustive danger-zone search beyond the available compute. **Honest verdict: unresolved.** The decisive remaining obstacle is either a reachability-specific proof of the balancing property (which would yield Fib for all reachable states by the standard induction) or a direct construction of an `n ≥ 15` reachable state with `e < F_{m+2}`. Neither is supplied here.

## Other metadata

```json
{
  "finished_at": 1795076073.1203399,
  "started_at": 1795074872.3168976
}
```
