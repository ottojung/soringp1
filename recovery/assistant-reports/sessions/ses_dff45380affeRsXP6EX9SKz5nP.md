# antonina-3PWfcAal0ArgCs5h4Y1d71-cherry

Session: ses_dff45380affeRsXP6EX9SKz5nP
Workspace: /home/lubko/soring-fronts/sortboundu-conp-membership-alln
Created: 1795308570700; updated: 1795308799893

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 437 (msg_200be33d3001niuWZZzSwDMZfO)

I investigated the coNP-membership front for `SORT-BOUND-U` on `billy-dev` and posted the result to board issue #301.

**Finding:** `SORT-BOUND-U ∈ coNP` remains open. No uniform polynomial-time verifier for no-instance certificates and no infinite family of `n,k` with a proved superpolynomial certificate lower bound was found.

**What was ruled out / obstructed (class-specific):**
1. **Explicit adversary/refuter DAG certificates:** semantic completeness holds (adversary wins iff `S(n)>k`), but verification requires universal totality over all incomparable pairs in each state; explicit state enumeration has at least the labelled-poset count `2^{Θ(n²)}`, superpolynomial in `N=Θ(n log n)`. So explicit-frontier refuters are ruled out, not all certificates.
2. **Finite-memory adversary machines:** no polynomial bound on optimal refuter memory; natural memory is the current poset/transcript, whose state space is exponential.
3. **Potential/weighting adversaries:** only recover the information bound `S(n) ≥ ⌈log₂ n!⌉`; cannot prove exact gaps such as `n=12, k=29`. Exact lower bounds require more than entropy; counting linear extensions is `#P`-complete and not tight.
4. **Encoding barriers:** Mahaney/Fortune/Ogiwara–Watanabe constrain hardness routes for the sparse unary language but give neither coNP membership nor non-membership.

**Soundness vs. completeness:** A supplied adversary DAG can be sound, but coNP membership requires an all-`n` polynomial-size complete family of no-certificates; no such family is known. Conversely, nonexistence of small DAGs would be only a class-specific obstruction, not a separation.

**Next decisive question:** Find a polynomially checkable adversary invariant for a fixed infinite gap family (e.g. `n=12,k=29` or Sergeev's `S(n)−log₂(n!)=o(n)` gaps), or prove that any such invariant must encode exponentially many poset states.

No repository, Lean, test, or branch changes were made; the worktree remains clean.
