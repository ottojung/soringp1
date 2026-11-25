# depth-balanced-winning-frontier-size

## status

investigated

## origin

ai_proposal_unverified

## agent_id

doB5CAhztSwyGb0ppBzxnl-penza

## exit_state

clearexit

## question

For every sufficiently large n, let the depth-balanced optimal-play frontier at depth d be the set of poset states reachable from the n-antichain by a minimax-optimal comparison sequence in which every selected move has an easy child of minimax depth at least m-2. Is this balance-restricted frontier still of size 2^{Omega(n log^2 n)} at some depth at or below S(n), or does confining optimal play to depth-balanced moves collapse it to polynomially many isomorphism classes in n?

## basis

Board #301 depth-balance-alln report (2026-11-19) states that all reachable states for n<=10 admit a balanced optimal move; the winning-frontier barrier gives 2^{(1/4-o(1)) n log^2 n} winning states at one depth. A from-scratch minimax probe (scratch only, no repository code) found the balanced frontier essentially equals the full optimal-play frontier at n<=6 (93451 vs 95251 labelled states). The all-n question is open; no proof or verification is claimed here.

## falsifier

Exhibit an infinite family of n for which the depth-balanced optimal-play frontier has at most polynomially many isomorphism classes at every depth, certified by exact minimax; alternatively prove a 2^{Omega(n log^2 n)} lower bound on that frontier that survives the depth-balance restriction.

## implication

A polynomially small balanced frontier would open a new route around the winning-frontier enumeration barrier toward a faster exact evaluator for S(n); a matching exponential lower bound would show that today's depth-balance structural fact cannot shrink the state space and would rule out this whole family of pruning methods.

## finding_unverified

, and primary sources (Sergeev ECCC TR20-096; Stober–Weiß arXiv:2206.05597; OEIS A036604). All computation was scratch-only in `/tmp/opencode`; no repository, Lean, ledger, or branch changes.

### Mathematical finding

**A concrete finite witness that invalidates the key inference behind the front.** From-scratch exact minimax (`n≤6`) reproduces the reported numbers: at n=6, `OPT=95251`, `BAL=93451` (loss at depths 5–6); at n≤5, `BAL=OPT` everywhere. So balance is a mild but genuine restriction — and small n cannot discriminate the all-n dichotomy.

More importantly, the poset on `n` elements consisting of a 3-chain `0<1<2` plus isolated elements (`n=5,6` verified) is:
- reachable in exactly 2 legal comparisons,
- budget-exact winning (`m(P)=S(n)−2`), the same property the winning-frontier construction uses,
- yet on **no** minimax-optimal play from the antichain.

Mechanism, verified: at state `0<1` (m=9=S−1 for n=6), comparing `1` with an isolated element gives child depths `(8,9)`, so `1+9>9` — a non-optimal "risky" move; optimal play only compares pairs of isolated elements. General deduction: extending a chain is non-optimal whenever ≥2 isolated elements remain. Since the winning construction builds long chains, its states are reachable and budget-winning but not on any single optimal strategy. This makes explicit the quantifier gap the Executive already recorded (2026-10-27): "∀P_A ∃history" ≠ "one optimal strategy encounters the census." **The winning-frontier barrier provides no evidence for the balanced optimal-play frontier.**

### Status and failed approaches

Both falsifier disjuncts remain **open**. `BAL ⊆ OPT`, so the `2^{Ω(n log² n)}` lower bound is at least as hard as the repository's open "optimal-play state count," and a polynomial bound on a subset would not resolve the all-optimal DAG question. I tried and withdrew a budget/tightness "proof" that winning states are optimal-play reachable (the witness refutes it); the cross-edge construction could not be made balanced (symmetry-sufficient balance conflicts with fixed asymmetric edges; common scaffold compresses the family); collapse-to-poly had no available invariant.

### Complexity soundness

A poly balanced frontier would yield `SORT-BOUND-U ∈ NP` only conditionally on the still-open all-n depth-balance fact, and is an existence claim the per-move verifier's soundness does not supply; an exponential frontier would be an enumeration barrier, not a time lower bound.

**No theorem about `S(n)` was completed, no class separation is claimed, and both disjuncts are unresolved.**
**Recovery inspection (no actions repeated):**

- **Git / repo:** `billy-dev` at `6a96398`, working tree clean (`git status` empty), no new commits or file changes. No Lean/tests/workflows/ledger modifications were made.
- **External side effects (durable):** Board #301 has **exactly 1** post by `SoringP1 frontier: depth-balanced-winning-frontier-size` (2026-11-19T11:11:59.811Z), confirmed on page 1. No duplicate post made. No other external actions (commits, PRs, purchases, etc.) were taken.
- **Scratch artifacts (local, non-durable to repo):** `/tmp/opencode/balfront_probe.py`, `/tmp/opencode/report.md`, `/tmp/opencode/post_result.json` exist from the interrupted turn.

**Conclusion:** The previous turn completed all intended work (from-scratch analysis + single #301 report). There is **no unfinished work** to continue and no uncertain external effect requiring review. No further actions taken.

## Other metadata

```json
{
  "finished_at": 1795086793.7497492,
  "started_at": 1795086012.7781484
}
```
