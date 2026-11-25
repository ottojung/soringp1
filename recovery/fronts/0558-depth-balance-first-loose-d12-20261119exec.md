# depth-balance-first-loose-d12-20261119exec

## status

investigated

## origin

ai_proposal_unverified

## agent_id

uhS6ek21ZZN17d3HhgCpag-supplied

## exit_state

clearexit

## question

Resolve d(12): at the first information-loose n (S(12)=30 > C(12)=29), does there exist a poset reachable from A_12 along a height-30 optimal strategy that violates DEPTH-BALANCE B? Use a method materially distinct from brute-force exhaustive reachable-state enumeration, which was attempted and left incomplete by the investigated depth-balance-gap-tightness front (that front certified d(n)=0 only for n<=9).

## basis

The verified 10:59Z depth-balance-gap-tightness report left d(12) explicitly open after its exhaustive n=10,11,12 attempts were incomplete; the 11:11Z report supplied a reachable-vs-winning quantifier-gap witness. This is a documented research failure and a method-distinct follow-up, not a relaunch of the same computation.

## falsifier

Exhibit a poset reachable from A_12 along a height-30 optimal strategy with an exact certified minimax/extension-count witness violating B, establishing d(12)=1; or rigorously prove B holds on all height-30 optimal A_12 paths.

## implication

d(12) decides whether the balanced-optimal normal form survives at the first information-loose n: d(12)=1 kills the route that depth-balance always holds on optimal play, while d(12)=0 gives positive structural evidence toward normal-form evaluators.

## finding_unverified

Posted exactly one #301 comment under `SoringP1 frontier: depth-balance-first-loose-d12-20261119exec` (verified: 1 post by that exact author). `d(12)` is **not resolved**; deliverable is the honest obstruction (c), with certified partial results: `d(n)=0` for tight `n≤9`, root `A_12` is `B`-balanced, and any counterexample must satisfy `e(P) ≤ (5/8)2^m` with an information-tight hard child. Blocker: exact minimax cost at `n=12` (one-relation state did not finish in ~4.5 min / ~2.3 GB) and no SAT/CP solver available. Git worktree clean; no repo/Lean/test changes. No model pinned or audited.

## Other metadata

```json
{
  "finished_at": 1795090100.3500614,
  "started_at": 1795088068.9510741
}
```
