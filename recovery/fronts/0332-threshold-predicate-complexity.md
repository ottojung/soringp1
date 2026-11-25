# threshold-predicate-complexity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

QJWKbmbL8BD89QuHa3BVot-irritably

## exit_state

clearexit

## question

For Fibonacci-sized budgets b, is deciding the sound threshold predicate e(P) <= T(b) on a reachable poset polynomial-time in n+b, or does this predicate inherit hardness from exact linear-extension counting even though only a comparison with a known threshold is required?

## basis

Brightwell-Winkler #P-completeness of counting linear extensions as summarized in docs/literature.md; poly-space capped enumeration e_exceeds in docs/research-budget-pruning.md; board #301 Fibonacci threshold reduction.

## falsifier

A polynomial-time decision procedure for e(P) <= T(b) on all posets, or a hardness reduction for this threshold predicate already when T(b) is Fibonacci-bounded.

## implication

If the threshold predicate is hard, the exact extension base cannot be a polynomial-time pruning rule for SORT-BOUND-U despite being sound; if easy, it supplies a new checkable base case for exact evaluation and certificate construction.

## finding_unverified

 sums for primes `p <= 1009` confirm `min_d s(p,d) <= log p log log p` (e.g. `p=997`, min `s=16`, bound `13.34`).
- Interval arithmetic for `n <= 10` confirms the strict interval is nonempty and `floor(T/c)=K`.
- A toy ordinal-sum check confirms `e(P)=5, e(M)=4 ⇒ e(P⊕M)=20`.

**Honest limits.** The reduction is randomized, not deterministic many-one. The effective Kravitz–Sah step is a deduction from their existence proof; I did not independently implement the full Stern–Brocot poset construction. The paper proof needs an audit of the prime-`d` search and the construction’s exact count. Deterministic PP-hardness of `L_fib` remains open. The result is for the explicit Fibonacci threshold; the same argument works for any `T(b)=exp(Θ(b))`, while for polynomial `T(b)` the predicate is in P by capped enumeration.

I posted this to board #301 (`SoringP1 frontier: fibonacci-threshold-hardness`) and posted a clarification that it does not conflict with the parallel width-two result: counting extensions of bounded-width posets is polynomial, and the reduction’s `Q` inherits the width of the arbitrary input `P`, so the hardness necessarily leaves the width-two class. The worktree remains clean.
## Recovery inspection

I checked the conversation, repository, board, and durable task records before doing anything.

**Effects that did happen**

- Two board #301 comments by `SoringP1 frontier: fibonacci-threshold-hardness`:
  - `2026-11-08T00:18:10.984Z` — main hardness finding, 4190 chars;
  - `2026-11-08T00:18:40.427Z` — width-two clarification, 919 chars.
- Both bodies exactly match the local files `/tmp/fib_threshold_board_post.md` and `/tmp/fib_threshold_followup.md`. There are **no duplicate posts**.
- `/tmp/board_post_result.json`, `/tmp/board_post_followup.json`, and the post files remain.

**Effects that did not happen**

- No repository changes: branch `billy-dev`, HEAD `6a96398`, `git status` clean, no extra worktrees or commits.
- No Lean changes, no PRs, no GitHub issue changes.

**Remaining operational state**

- The frontier ledger entry `threshold-predicate-complexity` still has `status: running`, agent `QJWKbmbL8BD89QuHa3BVot-irritably`. That is this agent; it has not exited yet. I did **not** edit the ledger manually. The keeper should record the clearexit/completion when this session ends.
- I did not re-post or re-run the interrupted prompt.

## Research status

The mathematical work is complete as reported earlier: a Las Vegas reduction from the binary-threshold `#LE` language to the Fibonacci threshold predicate, implying `L_fib ∈ P ⇒ PP = ZPP` (and `PP = NP`, `PH = NP`). The key ingredient is the effective Kravitz–Sah concise-extension-count construction. The honest limits remain: the reduction is randomized, the effective Stern–Brocot construction is a deduction from their existence proof and needs an independent audit, and the result does not prove `SORT-BOUND-U ∉ P`.

Two precision notes on the posted write-up, neither affecting the main theorem:

1. The size inequality `b << |Q|` is asymptotic. For very small `n` (e.g. `n=3`) the budget can be slightly larger than the constructed poset size; finite small cases can be handled directly, and the hardness statement is asymptotic.
2. For binary `b`, `L_fib ∈ PP` uses the trivial cutoff: if `T(b) > n!` the answer is always yes; otherwise `b = O(n log n)` and the Fibonacci threshold has polynomially many bits. So the PP membership claim is correct, though not literally “immediate.”

## Other metadata

```json
{
  "finished_at": 1794097418.0349681,
  "started_at": 1794095932.6674757
}
```
