# Executive pass — SoringP1 reachable halving-obstruction spectrum (2026-11-20, billy-dev)

Status: research dispatch + independent check. **No theorem completion claimed.** The final
S(n)/SORT-BOUND-U uniform-complexity theorem remains open; no repo/Lean/CI/main change in the
SoringP1 project this pass. The only external writes are this record, one board comment on #301,
and one managed Antonina researcher dispatch (details below).

## State inspected this pass (live, not ledger)
- Antonina board #301: newest comments 18:03Z–18:55Z. Latest recorded open lemma (18:55Z): construct,
  for infinitely many sizes, a path from the antichain A_(6+t) to a power-of-two halving obstruction
  W6 ⊕ C_t with both children fitting the remaining global height budget at every prefix.
- Live agents: only this Executive session running; **zero** SoringP1 researchers running. Frontier
  diagnostic: 614 fronts (593 investigated, 21 blocked), curator clearexit, status depleted. The
  three newest curator fronts (halving-obstruction-infinitude-allr,
  antichain-reachable-power2-halving-obstruction, information-tightness-recognition-complexity) were
  all investigated and posted to #301 (18:43–18:47Z); their general-poset infinite families and the
  finite n=6/n=7 reachability witnesses are recorded there.
- Canonical SoringP1 base: origin/main `6cddeaa2453d4da2ae0e918e50ba61c71a7da85f`.

## Independent check performed this pass (verifies a claimed result)
From-scratch Python (transitive closure, subset-DP linear-extension count, memoized exact minimax):
- Primitive R3 = successor masks `(0,0,1,3,7)` (n=5): e=8, F=4, no exact-halving root. Confirmed.
- Ordinal-sum additivity checked on four small pairs: e(P⊕Q)=e(P)·e(Q), F(P⊕Q)=F(P)+F(Q), and
  non-halving of both factors implies non-halving of the sum. Confirmed.
- Deduction (not brute-forced at n>5): R3^(⊕k) has e=2^(3k), F=4k, gap F−log2(e)=k, no halving,
  for every k≥1. This confirms the general-poset infinite-family claim of the 18:45Z post.
  As that post correctly states, this is a **general-poset** result and transfers to S(n)/SORT-BOUND-U
  only with the still-missing antichain-reachability + sibling-budget argument.

## New dispatch (genuinely distinct front; not a repeat)
Managed researcher `7ZKyaHa4lZbUe5ERDVhQRG-hive`, isolated worktree
`/home/lubko/soring-fronts/antichain-halving-spectrum-20261120` (branch
`research/antichain-halving-spectrum-20261120` at 6cddeaa), state verified `running` after dispatch.
Question: determine the **reachability spectrum** of power-of-two halving obstructions on optimal
play from the antichain (known: n=5 NO, n=6 YES via W6, n=7 YES via Q7), then either
(A) construct an infinite family with an explicit padding lemma and a sibling-budget induction, or
(B) prove a barrier that the reachability window + one-bit-slack recurrence exclude such states for
all large n. This sharpens the predecessor's failed construction-only attempt by adding a decidable
per-n slack computation and a barrier-first goal. Falsifier and stop condition were given; no
Lean/repo/branch/commit/PR changes authorized; one board post on completion. Agent exit is not
completion — its result must be independently checked before any conclusion.

## Precise open lemma (carry forward)
For infinitely many t, construct a path from A_(6+t) to W6 ⊕ C_t such that both children at every
prefix fit the remaining global height budget; or prove no such family exists. Ordinal-sum
additivity alone does not supply antichain-root reachability or sibling-budget feasibility. This
remains the concrete unresolved obligation; the SoringP1 final theorem is not claimed closed.
