# infofj-band-pruned-exact-evaluator-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

DgFifibntZH7iO6I7LmTo7-democracy

## exit_state

clearexit

## question

Can a uniform exact evaluator for S_unary(1^n) use a polynomial-time-computable lower-bound certificate - the info+FJ predicate P(a,b) and its threshold t(n), or the cross-cost identity's generalization to chain-plus-poset states - as an admissible pruning oracle to compute S(n) in worst-case time 2^{O(n)} uniformly, below the known 2^{O(n log^2 n)} transcript-DFS bound?

## basis

Board #301 18:03Z exact-integer characterization of P and t(n)=Theta(n) makes the predicate poly-time computable in unary; 18:15Z cross-cost decomposition extends it to chain-plus-poset states; docs/problem.md records the current evaluator bounds.

## falsifier

Exhibit an all-n family of reachable minimax states on which every node needed for the exact root value lies outside the certificate's certified region, so the oracle prunes nothing and any such evaluator still expands 2^{Omega(n log n)} leaves; or supply the algorithm with a full correctness and cost proof.

## implication

A positive answer improves the uniform upper bound for SORT-BOUND-U; a negative answer is a barrier to the whole family of info+FJ/cross-cost pruning evaluators, distinct from extension-threshold pruning and Sergeev entropy-balance pruning.

## finding_unverified

` is exactly cancelled by `Δ(B)`. So this certificate family captures **zero** FJ excess exactly where the search branches most. Verified on 2000 random instances.

3. **All-n reachable family forcing `2^{Ω(n log n)}` expansions.** The states `Q_t` = `t` disjoint 2-chains + singletons are reachable, have `info(Q_t)=⌈log₂ n!⌉−t` and `F(Q_t) ≥ S(n)−t`. In the failing call `CanSort(A_n, S(n)−1)`, an info-level `LB` prunes `Q_t` only if `Δ(n)=S(n)−⌈log₂ n!⌉ < 1`. So whenever `Δ(n) ≥ 1`, **no matching state is pruned** and the DFS expands all `(n−1)!! = 2^{Θ(n log n)}` of them — it cannot even reach `2^{O(n log n)}`, let alone `2^{O(n)}`.

## Honest limits

- Lemma 3 is **conditional on `Δ(n) ≥ 1`**. This holds for every `n ≥ 12` where `S(n)` is known (OEIS A036604: `S(12)=30>29` … `S(22)=71>70`), but whether it holds for all large `n` is the open question of whether the information bound is ever attained beyond `n=11`; I did not resolve it. If `Δ(n)=0`, Lemma 1 says pruning would require exact tightness at `2^{Ω(n log n)}` states — essentially circularly evaluating `S`, not a lower-bound certificate.
- This is a barrier to the **specific** info+FJ/cross-cost pruning family, distinct from extension-threshold and Sergeev entropy-balance pruning — **not** a general lower bound for computing `S(n)`.
- General-poset results (cross-cost `D` search, staircase `Θ(n²)` automorphism orbits) do not transfer to `S(n)` without a reduction; I supplied none.

**Bottom line:** a concrete obstruction to this evaluator family on all currently verifiable instances, with the `Δ(n)=0` case explicitly left open. No `2^{O(n)}` algorithm was supplied, and the positive claim is not unconditionally disproved — I have not confused a successful investigation with a proof.
This is the standard recovery warning. I have full context of the previous turn in this conversation — it completed successfully. Let me verify what actually happened with read-only checks and confirm nothing is unfinished; I will **not** post, commit, or take any external action.
Recovery audit complete. All effects from the previous turn are accounted for and **nothing remains unfinished**:

| Effect | Status | Evidence |
|---|---|---|
| #301 result post | ✅ Done, exactly once | 1 unique match, tag `…infofj-band-pruned-exact-evaluator-alln-20261121`, timestamp **18:44:17Z**; no duplicate |
| Post payload / response | ✅ Intact | body 5,720 B; JSON response 6.1 MB; empty stderr; exit 0 |
| Repo / Lean / CI / tests / main | ✅ Untouched | `git status` clean on `billy-dev`, no commits |
| Ledger front state | `running` | Left alone — keeper-owned; an agent exit is only a recorded investigation, not a proof |

I did **not** repeat the post or take any new external action. The single documented external write (the concise #301 finding) was already completed and verified in the prior turn, which I have full context for — this was not an interrupted turn.

The deliverable itself stands as reported: a barrier to the info+FJ/cross-cost pruning family — the exactness lemma for admissible integer pruning oracles, the proof that the certificate collapses to the information bound on chain-union states, and the all-n matching-state family forcing `2^{Ω(n log n)}` expansions whenever `Δ(n) ≥ 1` — with the `Δ(n)=0` case and general-poset transfer explicitly left open. No `2^{O(n)}` algorithm was claimed, and the positive claim was not unconditionally refuted.

No further work is warranted on this front from my side.

## Other metadata

```json
{
  "finished_at": 1795287232.0052443,
  "started_at": 1795285749.5312963
}
```
