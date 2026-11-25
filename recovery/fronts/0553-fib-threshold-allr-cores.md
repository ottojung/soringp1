# fib-threshold-allr-cores

## status

investigated

## origin

ai_proposal_unverified

## agent_id

yrfpArapnVuaw2CqNjv6BP-buckwheat

## exit_state

clearexit

## question

Let T(r) be the largest integer E such that every finite poset with at most E linear extensions satisfies m(P) <= r, where m is the exact adaptive minimax depth. research-core-threshold.md proves T(r) = F_{r+3} - 1 for r <= 8 and conjectures it for all r. Does this Fibonacci extension-count threshold law hold for every r, i.e. is T(r) = F_{r+3} - 1 universally over cores?

## basis

research-core-threshold.md paper proof for r <= 8, research-width-two-threshold.md GPC-based width-two law, Fibonacci staircase tightness, and the independently checked superpolynomial core-census growth reported on board #301.

## falsifier

Find, for some r > 8, a core with e(P) <= F_{r+3} - 1 but m(P) >= r+1 (e.g. by pushing the exact core census past E=88), or otherwise prove the equality fails for large r.

## implication

An all-r Fibonacci threshold law would give an exact extension-count-to-depth dictionary for every core, sharpening the reachable-state lower-bound program and minimax structural theory; it is not itself an NP or coNP certificate or a class separation.

## finding_unverified

 = 0` answer leaves free segments `i` and `L−i−1`, costing `≥ i + (L−i−1) = L−1` by induction, hence `D(L) ≥ L`; query-all gives `D(L) ≤ L`. So `D(L) = L` and `m(W_n) = D(n−1) = n−1`. Checks: exact minimax matches `n = 1..10`; recurrence verified to `L = 40`. This makes the threshold's **tightness half unconditional for all `r`** (and the width-two threshold exact for all `r`, via Peczarski's width-two GPC).

**Theorem B — no fence superposet is a counterexample.** The prior failed front named “add one relation to a fence” the sharpest quick falsifier. For any superposet of `W_n`, free edges form segments `L₁..L_t`, with `e = ∏ F_{L_j+2}` and `m = Σ L_j`. The identity `F_p F_q = F_{p+q−2} + F_{p−2}F_{q−2}` gives `F_p F_q > F_{p+q−2}` for `p,q ≥ 3`, so `∏ F_{L_j+2} > F_{Σ L_j+2}` when `t ≥ 2` (equality iff `t = 1`). Hence `e ≥ F_{m+2}` for **all** fence superposets at **all** `n`, independent of GPC. Exhaustively checked over all consistent orientation patterns of `W_n`, `n = 2..7`: formula holds, zero violations.

## Failed falsification attempts
- `e ≤ 88` census rerun: 22,120 cores, 0 failures — correct but **not new** (board already has `T(10)=232`).
- `E = 143` census: aborted for runtime and **superseded** — since `T(10)=232`, `e ≤ 143 ⇒ m ≤ 10`, so it could not be first.
- Fence superposets: **proved impossible** (Theorem B).
- GPC-certificate completeness / balancing route: prior fronts establish these are sound-only; no completeness theorem.

## Exact obstruction and honest limits
I found **no counterexample and no new finite threshold** — the two deliverables the Executive dispatch requested. Deciding the all-`r` law is exactly the general Fibonacci inequality, a long-standing open problem implied by (but not equivalent to) GPC. A surviving counterexample must be a `≥15`-element core outside the known GPC classes with `F_{m+1} ≤ e ≤ F_{m+2} − 1`, `m ≥ 12`. My contribution is to close the two natural finite routes and prove the previously computational tightness half; the mathematical status of the law itself is unchanged. **No complexity consequence for `SORT-BOUND-U`**: this is minimax-game structure on partial orders, the `S(n)` root being the antichain with `e = n!` far outside the threshold range, and no certificate or class separation follows.
**Recovery inspection (no actions taken):**

- **Working directory / Git:** `/home/lubko/soring-fronts/fib-threshold-allr-cores` is clean on `billy-dev` (`billy-dev...origin/billy-dev`, HEAD `6a96398`, no uncommitted changes, no commits made).
- **External side effects that actually happened:** exactly one board comment was posted to Antonina issue #301 by `SoringP1 frontier: fib-threshold-allr-cores-20261119exec` at `2026-11-19T10:01:53.339Z` (confirmed present; 1 matching post). No repository, Lean, test, workflow, or ledger changes were made.
- **Local/scratch artifacts:** analysis scripts, notes, and outputs exist only under `/tmp/opencode/fiballr` (no durable repo/task-record side effects). No related processes (`ctc.py`/`level143`/etc.) are running.
- **Unfinished work:** none for this front.

I did not repeat the interrupted prompt or duplicate any post/commit/purchase. No uncertain external effects identified; the completed report (Theorem A: `m(W_n)=n-1` for all `n`; Theorem B: no fence-superposet counterexample; failed/closed falsification attempts; exact obstruction at the general Fibonacci/GPC frontier; no consequence for `SORT-BOUND-U`) is already delivered on the board.

## Other metadata

```json
{
  "finished_at": 1795082592.629507,
  "started_at": 1795081686.2485294
}
```
