# extension-inversion-decision-complexity-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

2fRSuW989IOJGtS7ulLNJ9-amenable

## exit_state

clearexit

## question

For an explicit n-element poset P given by its transitive reduction, determine the complexity for all n of deciding whether P has any sibling extension inversion (a minimax-optimal comparison whose minimax-harder child has strictly fewer linear extensions than its easier child), and of deciding whether P is all-inverted.

## basis

Board #301 (2026-11-22 05:30Z) introduces sibling extension inversions, reports a paper proof that tight states are inversion-free, and exhaustively verifies Claim C through n=9. The ledger records #P/PP-hardness of linear-extension counting on reachable posets but no complexity question for the inversion predicate itself.

## falsifier

Give a polynomial-time algorithm for either decision problem, or a reduction from exact linear-extension counting (#P) or 3-SAT showing that inversion detection is #P-hard or NP-hard uniformly for all n.

## implication

The complexity of recognizing the newest board result's inversion predicate governs whether extension-inversion-based pruning and canonical monotone strategies can be applied algorithmically; hardness would bar cheap detection of the very condition the structural theorem uses.

## finding_unverified

e effect.) No duplicates.

## Mathematical finding

**Claim attacked (all‑n, falsifiable):** INV-EXISTS(P) and ALL-INV(P) are polynomial-time decidable for every explicit n-poset, so inversion-based pruning is cheaply applicable. I tried to falsify it with a #P/3SAT reduction and **failed** — the claim is not refuted.

What I did establish (all general-poset deductions, none transferred to S(n)):

1. **Sharp soundness bounds.** From `m(Q) ≤ e(Q)−1`: any inversion forces `m(P) ≥ 5`, `e(H) ≥ m(P)`, `m(P)+1 ≤ e(E) ≤ 2^{m(P)−2}`, and `e(P) ≤ 2^{m(P)−1}−1` (slack ≥ 1). Hence `m ≤ 4` ⇒ no inversion, and that slice is poly-time decidable. The n=6 witness confirms tightness (`m=6, e=30, e(H)=14, e(E)=16=2^{m−2}`).
2. **Exact obstruction for ALL-INV.** `ALL-INV` is empty **iff** the board's open Claim C holds. So any hardness proof for ALL-INV would refute Claim C; a poly algorithm would not settle it. The complexity question is hostage to an open structural problem.
3. **Upper bound:** both problems ∈ PSPACE (`DTIME(2^{O(n² log n)})`): count `e` by permutation enumeration, evaluate the minimax game by poly-space DFS, scan O(n²) pairs.
4. **Counting hardness ≠ comparison hardness.** For `P_Q = Q` plus two new maxima, `e(P_{a<b}) = e(P_{b<a}) = e(Q)` — both #P-hard to compute (Brightwell–Winkler), yet their comparison is constant NO. Also `INV-EXISTS(A⊕B) = INV-EXISTS(A) ∨ INV-EXISTS(B)`, so the natural embedding template is inert. Sound filters are necessary, never complete.
5. **Why the reduction failed precisely.** Children differ by one relation, so inversion is a "precedes odds" comparison; forcing a pair to be *minimax-optimal* needs global control of `m` at O(n²) alternatives — a PSPACE-level game property that the tight-state theorem and small-n enumerations do not supply. Conversely, no poly algorithm: optimal status is not determined by extension counts (n=6 state with identical `{10,16}` child-e multisets but different optimal status).

**Honest limits:** no hardness or poly-time classification, no Claim C progress, no new bound for `SORT-BOUND-U`/`S(n)` (general-poset hardness would not transfer to the sparse antichain language without an encoding-preserving reduction), no NP/coNP placement. Process success here is one board post; the hardness claim remains open.
Understood — I will not re-post or re-run the task. Let me re-verify what effects actually happened and whether anything remains unfinished.
Re-inspection complete. **No action taken this turn** — everything from the previous turn already happened and is verified:

- **Git:** clean at `6a96398` on `billy-dev`; reflog shows only the original clone. No commits, Lean files, tests, or repo changes.
- **Board #301:** exactly **one** comment for my front (`05:54:39.208Z`, author `SoringP1 frontier: extension-inversion-decision-complexity-alln`). No duplicate.
- **Ledger:** front `extension-inversion-decision-complexity-alln` still `running` with no `finding_unverified` — that field is keeper-managed and I did not edit it.
- **Scratch:** only `/tmp/opencode/post_invdec*` (report text plus the successful post result); nothing in the workspace.

The task is finished: the mathematical finding (sharp inversion soundness bounds, the ALL-INV ↔ Claim C equivalence, PSPACE upper bound, counting-vs-comparison separation, and the failed reduction with its exact obstruction) was posted once, with no external side effects remaining. Nothing is uncertain and no effect needs review or repetition.

## Other metadata

```json
{
  "finished_at": 1795326951.3500006,
  "started_at": 1795326095.0581462
}
```
