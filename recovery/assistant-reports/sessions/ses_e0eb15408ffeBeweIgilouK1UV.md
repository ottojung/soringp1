# antonina-4yukf7R2K8HpshjprP5y8f-exalt

Session: ses_e0eb15408ffeBeweIgilouK1UV
Workspace: /home/lubko/soring-fronts/admissible-frontier-growth-alln
Created: 1795049827408; updated: 1795050510820

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f14eae55001zjyflC2Td7W6Jy)

I'll start by understanding the repository state, locating "billy-dev", and reading the key documents.

## Output 17 (msg_1f14eb7ee001IW66MmYbZLJQjT)

Good, I'm on `billy-dev`. Let me read the key documents and locate board #301.

## Output 55 (msg_1f14eebcb001jh0lWI2v2reFb0)

Let me read the full t12-decide-symbolic report and related frontier/board context.

## Output 93 (msg_1f14f251d001UfP4DqDEzyA8xM)

Let me study the literature and the relevant frontier/barrier research notes.

## Output 113 (msg_1f1506d85001aW6jMc52q8emSD)

I've read the key documents. Let me examine a couple more relevant research notes, then do a focused computational validation of a candidate construction.

## Output 124 (msg_1f152e7dc001R7EeeRYxnFNjjM)

Now let me write a focused scratch script to validate my candidate construction (explicit nonisomorphic admissible states at linear depth).

## Output 142 (msg_1f1533ca4001mse9dhahg5v8pE)

The caterpillar failed admissibility (insufficient entropy drop). Let me try a rigid-backbone construction where a long chain supplies surplus entropy drop, allowing exponentially many distinguishable attachments.

## Output 160 (msg_1f1567075001L2vxo0CJChpOBe)

The general subset DP is too slow for large n. Let me use an exact combinatorial formula for this structured poset.

## Output 178 (msg_1f156d9de00129o9FZlrsVILUU)

I found a bug in my admissibility comparison (threshold should be ≈ d, not B−d). Let me correct it and verify the e(P) formula against brute force on a small case.

## Output 196 (msg_1f1573e60001im8swLblyYgDPq)

Formula off by one slot. Let me fix it (gadget below h_p has p+1 slots) and use exact integer comparison.

## Output 214 (msg_1f15774420013xFiDmi0mJSL8W)

The corrected construction works for large n. Let me do a final verification that the "all gadgets at the highest position" profile is indeed the worst case (maximizes e, minimizes drop) and confirm the isomorphism invariant.

## Output 232 (msg_1f157f6d9001ceNA5EBEeGmEmL)

I spotted an off-by-one in the witness script's `comb` (should be C(ℓ+L−1, L−1)). Let me correct and rerun.

## Output 243 (msg_1f15814e9001suH3V0a96oBxdE)

Construction fully verified. Let me check how to post to board #301 and confirm no duplicate author post exists.

## Output 270 (msg_1f1586cde001yFdB7CCrc9YTsx)

No prior posts. Let me write up the finding and post it as a single deliverable to board #301.

## Output 288 (msg_1f158e147001CT0PKQhm2OCnTT)

The post succeeded. Let me verify it landed and confirm the worktree is clean.

## Output 299 (msg_1f158f9dc001f4WAxFEfSMFWro)

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
