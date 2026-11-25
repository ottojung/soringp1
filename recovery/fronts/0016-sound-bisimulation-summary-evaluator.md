# sound-bisimulation-summary-evaluator

## status

investigated

## origin

ai_proposal_unverified

## agent_id

z6wWUx7u0kGFzEPvAD7kN9-vehemence

## exit_state

succeeded

## question

Is there a sound interface summary (a bisimulation-style congruence coarser than labelled-poset isomorphism) defined on the states reachable by a budget-critical threshold DFS, such that two congruent states provably share the same minimax budget, yet the induced quotient has only sub-exponentially many classes relative to the Theta(n log^2 n)-bit isomorphism-fine identity proven necessary?

## basis

Board #301 antonina-time-exponent 2026-10-27: isomorphism-fine memo keys of Theta(n log^2 n) bits are forced (Cs >= CI(m, min(k, m^2/2))/(m!^2) non-isomorphic critical-depth states, omega(n log n) bits, verified n <= 88), and the post explicitly leaves a sound coarser summary as the unattempted route; no existing front targets soundness of state identity.

## falsifier

Exhibit two budget-critical reachable states that must be identified by every candidate coarse invariant (e.g., one proposing an explicit polynomial-size summary: usable-prefix chain counts, height profiles, or extension-count classes) but which differ in minimax budget at the antichain-root game; or prove any proposed congruence collapses to isomorphism on the reachable set.

## implication

A verified sound-and-polynomial-bounded summary would let a canonical memoised evaluator evade the proven 2^{Theta(n log^2 n)} family barrier from board #301 and reopen uniform exact evaluation of S_unary at 2^{O(n log n)} time; every prior front only bounded the isomorphism-identity (completeness) side.

## finding_unverified

Now I have the model and the #301 barrier post. Let me set up the falsification experiment for the front. The sharpest attack: the most natural "sound-interface summary" candidate is the **poset's linear-extension count** `e(P)` (Fredman's information bound `F(P) ≥ log₂ e(P)` is exact for many natural families, and `e(P)` takes ≤ `n log n` bits — far under the forced `Θ(n log² n)` isomorphism-identity). The all-n falsifiable claim I will try to *disprove*:

> **Claim E:** on every budget-critical reachable state of the threshold game, the minimax budget `F(P)` is determined by the extension-count class `e(P)` (hence an `e`-keyed memoised evaluator with `O(n log n)`-bit keys is sound and evades the barrier).

A single pair of reachable bipartite states with `e(P)=e(Q)` but `F(P)≠F(Q)` kills it.
The prior turn read #301 and began a temporary experiment in `/tmp`; I have not attempted any board post or repository edit. I’ll verify the worktree and durable task records, then continue only the unfinished mathematical check.
**No mathematical result was established.** The previous turn started an experiment testing whether the linear-extension count \(e(P)\) determines the minimax continuation budget \(F(P)\) for reachable height-two states, but the experiment did not produce a valid pair or a completed check. Its temporary scripts in `/tmp/opencode/bisim/` are incomplete and should not be treated as evidence.

Recovery checks found no repository edits or commits: the worktree is clean on `main`, and the host is `billy-dev`. The durable frontier ledger still marks this front as `running`. I made no Antonina post and did not change that record.

The precise unresolved point is whether a proposed summary—such as \(e(P)\)—merges budget-critical reachable states with different \(F(P)\), or whether some sound, coarser congruence can avoid the #301 isomorphism-fine state-count barrier. I did not verify a primary-literature result resolving that question, nor establish the required antichain-root connection. **No claim about summary soundness, quotient size, or an improved uniform evaluator follows from this attempt.**

## Other metadata

```json
{
  "finished_at": 1793130172.6025348,
  "started_at": 1793127989.5535538
}
```
