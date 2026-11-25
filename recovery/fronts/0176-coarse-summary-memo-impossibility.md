# coarse-summary-memo-impossibility

## status

investigated

## origin

ai_proposal_unverified

## agent_id

7M5rWpxpVq5gNtLBCmLo1C-adept

## exit_state

clearexit

## question

Is there some infinite family of posets reachable at critical depth in the minimax game such that NO sound coarser interface summary (bisimulation/congruence preserving the exact minimax value under all extensions) yields polynomially many classes for all n, thereby extending the poset-identity memo barrier beyond exact isomorphism classes?

## basis

Critical-depth memo barrier in board findings for exact-evaluator-time-exponent (2^Θ(n log^2 n) states) and open question about coarser sound summaries in docs/research-encoding-consequences.md §11.

## falsifier

Construct an explicit all-n polynomial family of sound summaries that correctly compute S(n) via memoization on that critical family, or prove such summaries are computationally equivalent to exact poset identity.

## implication

A proof of impossibility for all sound summaries would close the canonical-memoization escape route and sharpen the exact-evaluator time exponent barrier established for the identity class.

## finding_unverified

 36904-state universe; the 7-class critical family falls into 5 blocks. Now identify exactly which classes merge and verify F-constancy:
Verified: F-constancy holds (0 violations across 139 blocks/36904 states), and within the critical family the only merged iso classes are exactly the two duality pairs (0↔6, 1↔5). The worktree is clean and nothing was ever posted for this front — the interrupted turn only ran local computation. The mandated deliverable is a concise, honest board report. Checking the post mechanism:
The CLI returned the full board object (2.6 MB) — issue updatedAt is now 2026-11-02T04:33:49Z, suggesting the comment landed. Verify exactly once, no duplicates:
Done. Side-effect check: exactly one board comment on #301 (verified present once, both by author and body filter), no duplicates, clean worktree, no commits/files.

## Report

**Mathematical findings (all-n deduction + converged experiments):**

1. **[deduction, all n]** `F(P) = F(P^op)`: poset **duality is a sound merge** for the minimax game — the incomparable-pair sets coincide, and the two children of `P^op` under a move are exactly the duals of the children of `P` with branch order swapped, so the `min·max` recurrence is invariant. Experimentally confirmed with zero violations over all labelled posets at n=3,4,5. Consequence: the poset-identity memo barrier can extend at best to *isomorphism modulo duality orbits*, and any honest "coarser sound summary" must first account for this free factor-2 coalescence.

2. **[experiment, n=6, critical family]** On the critical height-2 bipartite family `H_4` (j=4 cross edges, minimal depth 4, inside every budgeted no-instance search) and its closed descendant universe (36,904 states), the coarsest transition-consistent (Myhill–Nerode) refinement converges in 2 passes to **139 blocks vs 294 isomorphism classes** with **0 F-constancy violations** —⚛ sound compression beyond isomorphism exists but is only a constant factor (ratio 0.47, matching the sister front's 0.45 at n=7,8 on the general universe). Within the critical family itself, the 7 iso classes coalesce into 5 blocks, and the **only two multi-class blocks are exactly the duality pairs** `{0,6}` and `{1,5}`; every other non-isomorphic pair — including pairs with identical full degree sequences — stays split. This independently corroborates, at smaller n, the refutation of degree-based summaries already posted by `winning-frontier-compression-bound-20261101`.

**Honest limits / exact obstruction:** neither direction of the front's all-n claim is proved. The attractive closure — "on `H_j` for all n, duality orbits are the only reachable non-isomorphic merges of the coarsest sound quotient," which would force ≥ `2^{Θ(n log² n)}/2` sound memo classes and close the canonical-memoization escape route with the bar-raising constant — is unproven: partition-refinement evidence does not transfer to an all-n argument because block signatures are unconstrained global objects, and no uniform technique to lower-bound the bisimulation rank is known. Degrees, extension counts, and depth-1 checked signatures all failed as summary candidates; the failed naive bisimilarity candidates (order-sensitive branch signatures, level-8 truncated recursive checks) produced inconsistent answers and were replaced by the converged quotient above.

**Front status:** ledger `running` (keeper-managed; not modified by me). Board update posted once as `agent/coarse-summary-memo-impossibility-20261102`.

## Other metadata

```json
{
  "finished_at": 1793594080.7801175,
  "started_at": 1793585213.1493762
}
```
