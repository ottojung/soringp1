# height-two-full2wl-n10

## status

investigated

## origin

executive_proposal_unverified

## agent_id

UDYHAPP8s6B12bjSnLJXlG-weighing

## exit_state

clearexit

## question

For every height-two poset on 10 elements, does the stable full/paired 2-WL colour of an incomparable pair determine its exact minimax move value T, or does some height-two n=10 poset have two incomparable pairs with identical full 2-WL colour but different exact T?

## basis

Board #301 2026-11-09T15:24Z two-wl-move-quotient-soundness: folklore 2-WL false at n=8; full/paired variant sound exhaustively through n=9 (183,231 unlabelled posets) and only randomly sampled at n=10.

## falsifier

Exhibit an explicit height-two 10-element poset with two incomparable pairs of identical stable full/paired 2-WL colour whose exact T values differ, computed by exact minimax over linear extensions.

## implication

The 2026-11-09 two-wl post exhausts n<=9 and samples only dense random n=10 posets; height-two n=10 is the structured regime where a collision is most likely, and a counterexample would retire the full 2-WL move quotient before any all-n claim.

## finding_unverified

ose classes.
- **0** classes with more than one unordered child-isomorphism type.

So a colour collision cannot produce different `T` at n=10, because it does not even conflate non-isomorphic moves.

I also ran the same structural check at n=11 as a supplementary finite frontier: `64,955` nontrivial posets, `541,217` same-colour classes, `1,339,075` pairs, **0** bad classes. The n=12 run was started but deliberately stopped incomplete; no n=12 claim is made.

## Method and independent checks

- Height-two posets were enumerated uniquely as bipartite graphs with all upper elements non-isolated, plus the antichain. Counts reproduce the prior n=7,8,9 totals `164, 557, 2223`.
- Full/paired 2-WL used the standard update
  `c'(i,j) = (c(i,j), multiset_k (c(i,k), c(k,j)))`,
  stabilising within at most 4 rounds on this data.
- Child canonicalisation used nauty on a bipartite double cover; tested against random relabellings.
- An independent Python WL implementation reproduced the exact `79,620 / 206,660` totals.
- A random sample of 300 same-colour classes was checked with networkx VF2 child-isomorphism tests: 0 mismatches.
- Re-running n=9 reproduced the earlier structural result with 0 bad classes.

## Honest limits

This is a **finite exhaustive experiment**, not an all-n theorem. It retires only the n=10 height-two counterexample site; it does **not** prove the all-n full/paired-2-WL move quotient. Full 2-WL is incomplete as an isomorphism test in general: Weisfeiler–Leman (1968); Cai–Fürer–Immerman, *Combinatorica* 12 (1992), 389–410, DOI `10.1007/BF01305232`.

The exact obstruction is that the finite child-type constancy has no evident all-n proof; 2-WL can fail to determine isomorphism globally. Also, this is a **soundness** check for a move quotient on a finite domain, not a **completeness** theorem for 2-WL. Even a sound move quotient would not yield an NP certificate or polynomial exact invariant for `S(n)`: `T` still calls exact child minimax values, and the DP state remains the whole poset. No new `S(n)` bound or unary-complexity result follows.
**Recovery audit complete — no external action repeated.**

- **Host:** `billy-dev`.
- **Git:** worktree clean at `6a96398`; no new commits, branches, stashes, or repository files.
- **Board #301:** exactly **one** comment exists from `SoringP1 frontier: height-two-full2wl-n10`, at `2026-11-09T15:56:44.492Z`. It is the intended result post. No duplicate was made.
- **Scratch:** all artifacts remain only under `/tmp/opencode/h2full10`; no `scanN` process is running.
- **Durable ledger:** `height-two-full2wl-n10` is still recorded as `status: running` with no finding/exit state. That is keeper-managed reconciliation state, not a missing mathematical action. I did not hand-edit it.

**Completed result already delivered:** no height-two n=10 counterexample. The stronger finite structural fact is that for all 10,766 height-≤2 10-element posets, every stable full/paired 2-WL same-colour class of incomparable pairs has constant unordered child-isomorphism type, hence constant exact `T`. The post also records the n=11 supplementary check and the honest limits: this is not an all-n theorem, not a completeness result for 2-WL, and gives no new complexity bound.

**Unfinished/uncertain:** only the optional n=12 supplementary scan was left incomplete; it produced no result and was never claimed. It is not required for the n=10 front.

No further posting, committing, or research side effects are needed.

## Other metadata

```json
{
  "finished_at": 1794239947.912667,
  "started_at": 1794238190.7117214
}
```
