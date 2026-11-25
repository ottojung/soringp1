# admissible-frontier-growth-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

4yukf7R2K8HpshjprP5y8f-exalt

## exit_state

clearexit

## question

For all large n and any fixed c<1, how fast must the budget-C(n) admissible canonical frontier grow at depth c*n, where a state is admissible when e(P)<=2^{C(n)-c*n}: is its size always 2^{Omega(n)} for non-tight n, or can it stay polynomially small along an infinite family, and does the measured roughly five-fold per-level growth at n=12 persist for all n?

## basis

t12-decide-symbolic (2026-11-19) measured admissible canonical frontier sizes S0..S10=1,1,2,7,27,102,456,2074,9952,49661,250310 at n=12 with about five-fold depth growth and S18 extrapolated near 9e10; this relaxation frontier differs from the winning frontier at budget S(n).

## falsifier

Exhibit an infinite family of n where the depth-c*n admissible canonical frontier under budget C(n) has only polynomially many states, or establish a uniform 2^{Omega(n)} lower bound via an explicit nonisomorphic admissible-state construction for every non-tight n.

## implication

A uniform exponential lower bound would rule out every exact evaluator that enumerates or tabulates the admissible lookahead frontier, sharpening the winning-frontier barriers; a polynomially small frontier would reveal compressible structure exploitable for a faster uniform algorithm.

## finding_unverified

ted construction works for large n. Let me do a final verification that the "all gadgets at the highest position" profile is indeed the worst case (maximizes e, minimizes drop) and confirm the isomorphism invariant.
I spotted an off-by-one in the witness script's `comb` (should be C(ℓ+L−1, L−1)). Let me correct and rerun.
Construction fully verified. Let me check how to post to board #301 and confirm no duplicate author post exists.
No prior posts. Let me write up the finding and post it as a single deliverable to board #301.
The post succeeded. Let me verify it landed and confirm the worktree is clean.
Done. Here is the outcome.

## Mathematical finding (paper-level, posted to #301)

I attacked the FRONT dichotomy for the **budget-C(n) admissible canonical frontier at linear depth d = c·n** (c<1 fixed): is it always 2^Ω(n), or polynomially small on some infinite family?

I settled it for the **admissible (relaxed) frontier** with an explicit construction:

- Build a backbone chain h₀<…<h_{L-1} (L≈c·n/2) by L−1 legal comparisons, then attach ℓ≈c·n/2 new elements below chosen backbone positions (one comparison each). Total comparisons = c·n exactly.
- The multiset of attachment positions is recoverable from the element-height multiset (an isomorphism invariant), so distinct position-multisets give **nonisomorphic** states; there are C(ℓ+L−2, L−2) = 2^Θ(cn) of them.
- Admissibility e(P) ≤ 2^{B−cn} has large slack (the backbone alone drops log₂(L!) ≫ cn bits). Worst case (all gadgets at the top position) was verified monotone and admissible by exact integer checks and brute-force linear-extension DP on n=8–10. Concrete witness: n=100, c=½, d=50 → C(49,23) ≈ 5.8×10¹³ nonisomorphic admissible states.

**Conclusion:** no infinite family has a polynomially small depth-cn admissible frontier; it is 2^Ω(n) for all large n and every fixed c<1. The same reasoning plus the report's own n=6,7,8 numbers answers the sub-question: the ~5-fold per-level growth does **not** persist as a universal constant (n=6's frontier even shrinks near the budget end).

## Serious falsification attempts that failed
- **Caterpillar/spine+leaves**: not admissible (leaves create too many extensions).
- **Length-2 chains + extra edges** (winning-frontier style at linear depth): binom(M,Θ(n))/n! < 1, so no guaranteed isomorphism class — the winning-frontier theorem fundamentally needs depth ~n log n.
- **Distinct-size disjoint blocks**: capped at 2^Θ(√n) up to isomorphism.

These failures plus the successful construction make a poly-small family implausible; I found none.

## Honest limits
- This is a **paper-level theorem** with explicit construction and computational verification — **not Lean-checked**, and I made **no repository/Lean changes** (worktree clean).
- Admissibility is a **sound (necessary) pruning condition**, not completeness: these are relaxed states, not certified winnable ones, so this is weaker than the existing winning-frontier barrier and in a different depth regime.
- It rules out polynomial-time/space enumeration of the linear-depth frontier, but does **not** beat the known 2^{O(N log N)} upper bound, sharpen the 2^Ω(n log²n) barrier, give any algorithm for S(n), or yield a complexity-class separation.
- No matching upper bound on frontier size is proved here, and the admissible-vs-winning gap at linear depth remains open.

Report is live on Antonina #301 (author `SoringP1 frontier: admissible-frontier-linear-depth-20261119exec`, 2026-11-19T01:08Z).

## Other metadata

```json
{
  "finished_at": 1795050529.62796,
  "started_at": 1795049826.6543198
}
```
