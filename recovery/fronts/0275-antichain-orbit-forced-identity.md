# antichain-orbit-forced-identity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

CPhDyI8qD29PCBVZ44uPkX-discuss

## exit_state

clearexit

## question

On the critical-depth states reachable by optimal-play threshold searches from the n-element antichain, is there any all-n sound state invariant coarser than labelled-poset isomorphism that is computable in time polynomial in the poset description and identifies states with provably equal minimax F(P), or does every such polynomial-time computable invariant must distinguish exponentially many non-isomorphic states on some all-n family?

## basis

sound-bisimulation-summary-evaluator was inconclusive; exact-evaluator-time-exponent proved isomorphism-fine keys forced exponential classes; this fronts the question as all-n falsifiable about polynomial-time invariants specifically.

## falsifier

Exhibit a specific polynomial-time invariant (with proof of soundness for the game value) whose quotient class count is o(2^(c n log^2 n)) for all n on optimal-play reachable sets, or prove that for any polynomial-time invariant I there is an all-n family of non-isomorphic optimal-play states with I equal but F different (soundness failure) or with I different only when forced and quotient still exponential.

## implication

A polynomial-quotient sound invariant would evade the isomorphism-fine barrier and open the door to 2^(O(n log n)) uniform evaluation of S_unary; a proof of exponential quotient for all polynomial invariants would formalize the memoization-barrier as a kind of "game isomorphism hardness" for this class.

## finding_unverified

inning non-isomorphic states at same depth/S(n); research-certificates-barriers.md mentions "optimal-play state count" on height-S(n) plays).
- `exact-evaluator-time-exponent` critical-depth memo barrier: no-instance threshold `k = ⎡log2 n!⎤-1` makes height-2 bipartite (A×B) family reachable in exactly j steps; with isomorphism-class keys under S_m×S_m gives `≥ 2^(Θ(n log^2 n))` classes (exceeds `2^(O(n log n))`). Notes coarser sound summaries (bisimulations) are the open residue.
- `sound-bisimulation-summary-evaluator` has state compression showing relabeling quotient is sound (collapses `A001035`→`A000112`, factor `2^(Θ(n log n))`) but linear-extension count is not sound (n=5 counterexample), balanced-greedy suboptimal at n=9. Canonicalization cost is bottleneck.
- `scripts/benchmark_symmetry_quotients.py` has `make_refined_canon(n)` (color refinement + brute force), equivariance argument for quotient soundness.

**Experiments on optimal-play states (height = S(n), path from antichain where each step optimal):**
- n=6: `47011` optimal-play states total; relabeling isomorphism classes all sound (0 bad groups). iso+dual also sound. By F value, different iso classes share same F at fixed F (e.g. F=5 gives 14100 states / 28 iso classes) — so merging different iso classes is possible in principle if we only cared about F-equality on that class, but need soundness for all reachable states and polynomial-time/all-n invariant.
- n=7: collected optimal-play states (grew to ~1.73M in full exploration); sampling ~1.26M gave 468 relabeling iso classes, 247 iso+dual classes. All sound so far.
- Cheap polynomial invariants tested on optimal-play states:
  - height only: 6 groups, 4 bad (unsound)
  - height+width: 13 groups, 11 bad
  - height+width+mins: 32 groups, 22 bad
  - profile (ht,wd, in-degree multiset, out-degree multiset): n=7 gave 421 groups, 4 bad
  - height+dual-height+width: 13 groups, 11 bad
  - Adding profile on top of iso+dual made it finer (506 groups) not coarser.

**Finding so far:** On optimal-play states, relabeling isomorphism is sound; known cheap degree/size invariants fail soundness or are very fine. The question is whether any polynomial-time computable invariant coarser than iso exists and is sound for all reachable states / all-n on optimal-play sets. The memo barrier shows isomorphism-fine is exponential on the critical (no-instance) height-2 family; optimal-play states are the "winning" frontier (different regime) where winning-frontier gives exponentially many non-isomorphic winning states at same depth — but sound coarser invariants might still exist or might be ruled out.

I checked the durable task record and Git state before continuing.

- The ledger still lists `antichain-orbit-forced-identity` as **running**; there’s no recorded completion.
- The worktree is clean, and the recent Git history shows no commit for this frontier.
- The previous turn performed local experiments and read repository documents, but made no repository changes.
- I found no evidence that it posted to Antonina or performed another external action.

The investigation remains unfinished: the small-instance tests show several cheap candidate invariants are unsound, but they do not establish an all-n result or resolve the exact meaning of “critical-depth states reachable by optimal-play threshold searches.” I have not repeated any external action; that terminology and the frontier status remain for review before reporting or closing the task.

## Other metadata

```json
{
  "finished_at": 1793801129.2065136,
  "started_at": 1793778320.7117999
}
```
