# antonina-doB5CAhztSwyGb0ppBzxnl-penza

Session: ses_e0c892adaffen4MAhy7vZl4nWh
Workspace: /home/lubko/soring-fronts/depth-balanced-winning-frontier-size
Created: 1795086013821; updated: 1795086762366

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f376dd07001Gmzw7l9No6Wx3L)

I'll start by understanding the repository state, the branch situation, and the relevant documents.

## Output 25 (msg_1f376ef10001jJVCgI82xf1pc1)

I'm already on `billy-dev`. Let me gather the board #301 context, the literature, and the relevant research notes in parallel.

## Output 44 (msg_1f377132a0014ZHiqmFRq5YcpC)

Let me read the winning-frontier barrier note and find the depth-balance report in full. I need the precise definitions.

## Output 63 (msg_1f37726990011YtL8o1yHhyf8J)

Let me fetch the full text of the two depth-balance reports from board #301 directly.

## Output 74 (msg_1f3773e51001xii3Xg5WjfEgiX)

Let me check whether the "winning states are optimal-play reachable" observation already exists, and read related strategy/compression notes plus the gap-tightness report.

## Output 93 (msg_1f3794716001fWeYdjWqWl8YwC)

Let me read the passages about optimal-play state counts and the certificates-barriers section, to ground what's already known and open.

## Output 112 (msg_1f3795e12001NcbaX647NPNLHD)

I've found a crucial subtlety: "winning + reachable at budget" does not certify per-move optimality, so the winning-frontier barrier may not transfer. Let me verify this with a clean scratch computation (no repo changes) and pin down concrete examples.

## Output 132 (msg_1f37ac42a001T47ZGaVHZctnO4)

BAL = OPT for n≤5, but TIGHT (budget-exact reachable) strictly contains OPT — a concrete validation that the winning-frontier barrier doesn't transfer. Let me run n=6 to see the first BAL/OPT split.

## Output 143 (msg_1f37c3cdf001d0ffXxmGE1YLxM)

This from-scratch probe exactly reproduces the reported OPT=95251 / BAL=93451 at n=6, and finds a concrete reachable+winning state that is on **no** optimal play. Let me now check the primary literature to ground the claims and avoid rediscovery.

## Output 184 (msg_1f37cc11c001dUfHXZ4ymPOST2)

The from-scratch probe reproduces the reported numbers exactly. Let me identify this front's exact ID and check for duplicate prior posts before writing anything.

## Output 199 (msg_1f37defcc00107IkgbFCUGCI2N)

Important: there are prior board posts on exactly this "winning frontier → optimal play" connection. Let me read them to avoid rediscovery.

## Output 210 (msg_1f37e126e001ih6DBqFr1m0BJ1)

The executive already flagged the quantifier gap on 2026-10-27; my concrete finite witness sharpens it. Let me extract and verify the witness fully before posting.

## Output 230 (msg_1f37f8f78001F3Nmxep7TdWi5t)

Let me verify the mechanism behind the witness (why building the 3-chain is not optimal play).

## Output 241 (msg_1f3801e8a0015gr3LgG0bT3wE0)

The mechanism is clean: extending a chain is a non-optimal (risky) move, so the budget-exact 3-chain state is on no optimal play. Let me check the Antonina post command syntax before reporting.

## Output 268 (msg_1f3812883001h8f3hwkykkX7B0)

No duplicate prior post. Let me write the report to a scratch file and post it to board #301.

## Output 295 (msg_1f381aac4001MpinYiz5CVm3vZ)

Let me verify the comment actually posted.

## Output 306 (msg_1f381c563001Ym0KFCWHFqt3yy)

The report is posted to board #301 (message at 2026-11-19T11:11:59Z). Final worktree is clean.

## Summary

I worked on `billy-dev` (branch `billy-dev` @ 6a96398), read `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, the full #301 depth-balance and depth-balance-gap reports, the winning-frontier note, the strategy-certificates/DAG notes, and primary sources (Sergeev ECCC TR20-096; Stober–Weiß arXiv:2206.05597; OEIS A036604). All computation was scratch-only in `/tmp/opencode`; no repository, Lean, ledger, or branch changes.

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

## Output 331 (msg_1f38224ca001NbGGPvTpAUxJlV)

**Recovery inspection (no actions repeated):**

- **Git / repo:** `billy-dev` at `6a96398`, working tree clean (`git status` empty), no new commits or file changes. No Lean/tests/workflows/ledger modifications were made.
- **External side effects (durable):** Board #301 has **exactly 1** post by `SoringP1 frontier: depth-balanced-winning-frontier-size` (2026-11-19T11:11:59.811Z), confirmed on page 1. No duplicate post made. No other external actions (commits, PRs, purchases, etc.) were taken.
- **Scratch artifacts (local, non-durable to repo):** `/tmp/opencode/balfront_probe.py`, `/tmp/opencode/report.md`, `/tmp/opencode/post_result.json` exist from the interrupted turn.

**Conclusion:** The previous turn completed all intended work (from-scratch analysis + single #301 report). There is **no unfinished work** to continue and no uncertain external effect requiring review. No further actions taken.
