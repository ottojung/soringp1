# reachable-optimal-slack-at-most-one-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

9KeIjGtfgQ0DkXxtw5RXmV-refusing

## exit_state

clearexit

## question

For every n >= 1 and every poset P reachable from the n-element antichain along an optimal sorting path of length at most S(n)-m(P), is the local slack m(P)-ceil(log2 e(P)) at most one?

## basis

Board #301 positive-slack hunt through n=7; docs/research-obstruction-next.md local frontier; independent n<=5 exhaustive slack check.

## falsifier

Exhibit one n and one such reachable poset P with slack at least two; independent checks rule this out for n <= 5 over all posets and the positive-slack hunt reports no such poset for n <= 7.

## implication

If true, exact minimax remains within one bit of the information bound throughout optimal play, yielding a sharp pruning invariant for exact evaluators without any complexity-class separation.

## finding_unverified

verified: 1 matching comment, no prior post existed). Scratch scripts are only in `/tmp/opencode`.

### Mathematical finding (honest, not a proof)
**No counterexample found. The claim is now verified over ALL posets for every n ≤ 7, and remains unproven for all n.**

Independent exhaustive computation of `slack(P) = m(P) − ⌈log₂ e(P)⌉` over the **entire** reachable poset space (= all labelled posets, since every poset is reachable from the antichain):

| n | posets | S(n) | posets with slack ≥ 2 | max slack |
|---|--------|------|----------------------|-----------|
| 5 | 4,231 | 7 | 0 | 1 |
| 6 | 130,023 | 10 | 0 | 1 |
| 7 | 6,129,859 (= A001035) | 13 | **0** | 1 |

The n=7 run completed (~12 min; `minimax(root)=13` confirms the engine). This is **strictly stronger than the front's requirement** (which only concerns optimal-path states) and stronger than the capped reachable-optimal DFS already on the board (883K records, no falsifier). For n ≤ 7 the claim holds a fortiori. I did not find a slack-2 poset at any n I could reach.

### Exact obstruction (paper deduction, verified algebraically)
Along a tight optimal path `m` drops by exactly 1 per comparison. For the adversary's max-m child `Q` of an optimal comparison at `P`:

`slack(Q) − slack(P) = ⌈log₂ e(P)⌉ − ⌈log₂ e(Q)⌉ − 1` (checked exactly on all 3,871 n=5 states with m>1, 0 violations).

So **slack can exceed 1 only if some optimal comparison has its max-m child `Q` with `e(Q) ≤ 2^{m(P)−3}`** — i.e. the *harder* child is also the *lower-entropy* child (roughly `e(Q) < e(P)/4`). The minimax recurrence does **not** preserve `slack ≤ 1` by itself (the sorter minimises max remaining cost, not max extension count), so no purely local induction proves the claim. Peczarski's n=13 `P16/Q'16` phenomenon (fewer extensions but harder) is precisely the mechanism this obstruction needs — so the claim is plausible but genuinely open, not structurally forced.

### Failed counterexample attempt
`Merge(a,a)` has slack `(2a−1) − ⌈log₂ C(2a,a)⌉ ≈ ½log₂(πa) − 1`, reaching **2 at `Merge(21,21)`** (n=42: `e≈5.4e11`, `m=41`, `⌈log₂e⌉=39`). But reaching two 21-chains costs 40 within-chain comparisons, so `d+m=81 ≪ S(42)≈170` — an "easy" state reached with a huge **surplus budget**, not a worst-case optimal-path state (which would need depth ≈129, impossible once cross-chain comparisons are forced). **General-poset unbounded slack does not transfer to optimal-path reachability** — this is why the merge family cannot falsify this front.

### Required distinctions
- **General posets vs. reachable-on-optimal-path**: arbitrary posets have unbounded slack (merge family), but those states are not reached on adversarial optimal play. The restriction is essential and is exactly where the open content lies.
- **Soundness vs. completeness**: even if true, the invariant only gives a *sound pruning rule* for exact evaluators (never a completeness/NP result). No complexity-class separation follows; sparsity/Mahaney and the exponential-tree-vs-certificate barriers still apply. I made no NP-membership claim.

### Honest limits
- n ≥ 8 brute force is infeasible: A001035 grows as `2^{Θ(n²)}` (n=8 ≈ 4.3×10⁸ labelled posets).
- For all n, the claim is **neither proved nor disproved**; n ≤ 7 is verified over all posets. The precise remaining possibility is an extension-unbalanced optimal split at n ≥ 8; no witness and no proof for it were produced. This is a concrete failed approach and an exact obstruction, **not** a proof.

## Other metadata

```json
{
  "finished_at": 1795320393.2588468,
  "started_at": 1795318826.4210155
}
```
