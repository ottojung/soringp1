# free-free-second-state-tightness-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

6iZL1xgAwBqntmF4dPOzR4-insist

## exit_state

clearexit

## question

For every n >= 5, let FF_n be the poset formed by two disjoint 2-chains plus n-4 additional free keys (the free-free outcome of the second comparison at the one-relation root state). Is FF_n information-tight, i.e. F(FF_n) = ceil(log2(n!/4)) = ceil(log2(n!))-2 for all n, or do infinitely many n have positive excess at this state only two comparisons from the root?

## basis

Board #301 (2026-11-22T14:26Z and 15:40Z) reports F(FF_n) = S(n)-2 for n=5..8 and independently verifies F(FF_9)=17=ceil(log2(9!/4)); e(FF_n)=n!/4 by construction. My own from-scratch scratch minimax solver reproduced FF tightness at n=5,6,7 and V_6 non-tightness (excess 1). Distinct from the completed gap(n)=F(V_n)-F(FF_n) >= 0 commission and absent from the 694 ledger IDs.

## falsifier

Exhibit some n >= 10 with two independent exact minimax computations and a strategy witness giving F(FF_n) > ceil(log2(n!/4)), or alternatively produce height-ceil(log2(n!/4)) strategies for an infinite family to refute the positive-excess horn; either outcome is a finite all-n deciding fact, not a class separation.

## implication

If FF_n is tight for all n, shallow free-free refinements of the antichain root preserve tightness and support information-bound pruning at depth two in exact evaluators; a counterexample yields a reachable positive-excess state within two comparisons of the root, sharpening the known n=12 non-tightness as a structural obstruction. No P/NP, coNP or other placement follows.

## finding_unverified

 for any duplicate board post before deciding on the single external write.
Let me read the full text of the key board posts (the `gap(n)` commission and the FF_9 verification) to see exactly what was established for all n.
The picture is now clear. My deduction answers the exact "NEXT DECISIVE QUESTION" the prior front left open. Let me verify the arithmetic cleanly and check the posting CLI syntax before making the single external write.
Everything checks out. Let me compose the single #301 result comment (scratch file first, then one post with JSON redirected to a file).
Let me verify the post landed exactly once and that the worktree is still clean.
## Recovery audit (first)

No prior side effects to repeat: `billy-dev`, worktree clean at `6a96398`, no stash, ledger front `free-free-second-state-tightness-alln` still `running` with no finding, and zero prior #301 posts for this front (`--contains "second-state"`, `"FF_12"`, `"12!/4"`, `"two-comparison"` all empty). The posting backend is working now; I made exactly **one** #301 comment and verified a single match.

## Mathematical finding: the all‑n tightness claim is FALSE

**Theorem (paper proof).** For every n ≥ 4, `F(FF_n) ≥ S(n) − 2`, equivalently `d(FF_n) := F(FF_n) − ⌈log₂(n!/4)⌉ ≥ excess_S(n) := S(n) − ⌈log₂ n!⌉`.

*Proof.* Explicit strategy from the antichain: compare keys 0,1; then compare keys 2,3 (free before comparison 2). In every outcome combination the residual poset is isomorphic to `FF_n`. Finish with an optimal height‑`F(FF_n)` strategy. This sorts all n! permutations within `2 + F(FF_n)` comparisons, so `S(n) ≤ 2 + F(FF_n)`. Subtract `⌈log₂ n!⌉ − 2`. Contrapositive: `d(FF_n) = 0 ⇒ S(n) tight`. ∎

**Counterexample at n = 12.** Wells' value `S(12) = 30` vs `⌈log₂12!⌉ = 29` (literature, `docs/problem.md`/`literature.md`) gives `F(FF_12) ≥ 28`. But `12!/4 = 119750400`, `2²⁶ < … ≤ 2²⁷`, so `⌈log₂(12!/4)⌉ = 27`. Hence `d(FF_12) ≥ 1`: `FF_n` is **not** information‑tight for all n, and a positive‑excess state lies just two comparisons from the root. The same inequality yields `d(FF_n) ≥ 1` at every known root‑non‑tight n (13, 15–19, 22); n=12 is minimal. This is exactly the "NEXT DECISIVE QUESTION" the completed `gap(n)` commission left open.

My from‑scratch Go/Python minimax reproduced S(4..7)=5,7,10,13 and `F(FF_n)=3,5,8,11=⌈log₂(n!/4)⌉`, corroborating the tight small‑n regime; the n=12 conclusion needs no exact n≥10 search (that search is infeasible here and was not the basis of the proof).

## Honest limits
- The falsifier's *computational* route (two independent n≥10 minimax runs) was not taken; I substituted a rigorous strategy witness derived from the literature value S(12)=30. The result localises the known obstruction to depth two; it does not compute `F(FF_12)` exactly or give a new lower bound on S(n).
- "Tight for all n" is refuted; "infinitely many non‑tight n" is **not** settled — it would need infinitely many root‑excess values (open), and the root‑forcing gap blocks amplification.
- No complexity consequence: no P/NP/coNP placement, no certificate completeness result. General‑poset results and certificate soundness were kept distinct from completeness, as required.

## Side effects
- One #301 comment (`2026‑11‑22T16:32:19Z`), verified once; JSON response saved to `/tmp/opencode/ff_result_post_response.json`.
- Scratch only under `/tmp/opencode/`; **no** Lean, tests, commits, PRs, CI, or ledger edits. Worktree remains clean. S(n)/SORT‑BOUND‑U remain open.

## Other metadata

```json
{
  "finished_at": 1795365194.7290397,
  "started_at": 1795363870.7813911
}
```
