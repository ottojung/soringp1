# uniform-advice-extraction-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

6mUDpIEVHGcVmQbk0POHXr-blissful

## exit_state

clearexit

## question

Is there an all-n uniform deterministic algorithm to compute S(n) that avoids non-uniform pruning advice by constructing its search strategy on-the-fly, or does every such uniform algorithm require 2^(Ω(n log n)) time for infinitely many n due to the cost of extracting admissible pruning rules from the game graph without precomputation tables?

## basis

Stober–Weiß use a pruned backward pass as advice for forward search; uniform-sergeev-transition-machine concluded extracting finite uniform parameters is a separate task with discipline constraints not obviously ruled out.

## falsifier

Give a uniform algorithm (no hardcoded advice per n beyond the standard model) that computes S(n) for all n in time 2^(o(n log n)) with correctness proof relative to the minimax model, or alternatively prove the extraction cost is unavoidable for some infinite family.

## implication

Would quantify the uniformity gap between non-uniform/exhaustive methods (e.g. pruned backward search used with advice in exact-value computations) and fully uniform exact evaluation of S(n), a distinction emphasized by the Sergeev uniformization discussion.

## finding_unverified

Let us look at the research-sergeev-asymptotic and bidirectional advice docs and also the board issue 301 if we can access it.
**Finding (mathematical):** There is already a uniform, on-the-fly algorithm (the transcript/budgeted DFS in `docs/research-budgeted-dfs.md`, no per-n hardcoded advice tables, strategy constructed by minimax search over the game graph) that computes `S(n)` for all `n` in time `2^{O(n \log^2 n)}` and space `O(n \log^2 n)` bits relative to the minimax model. So the “no non-uniform pruning advice” branch is satisfied by an existing uniform construction; the falsifier’s algorithm disjunct is not obviously false in principle, just that achieving `2^{o(n\log n)}` is the hard part.

**Obstruction / failed route:** The naive AND–OR tree lower bound is `2^{\Omega(n\log n)}` from depth `\ge \lceil \log_2(n!)\rceil=\Omega(n\log n)`. The budgeted DFS pays an extra `\log n` factor because at each node the sorter must consider `\binom{n}{2}=O(n^2)` incomparable pairs (branching over moves) while the adversary branches by 2; you cannot do better than branching factor ≥2 and you cannot reduce depth below the information bound. Reducing the exponent below `n\log^2 n` would require either (1) reducing depth below information bound (impossible) or (2) reducing the effective branching/move search below polynomial without precomputation. 

**Why on-the-fly extraction is costly:** The “pruning rules” used by non-uniform methods (e.g. Stober–Weiß backward pass as advice) are exactly which posets/branches are winning. The winning frontier barrier (`docs/research-winning-frontier-barrier.md`) shows there are `2^{\Omega(n(\log n)^2)}` reachable winning states at the information budget (and at exact optimum), and local invariants fail badly (as shown in `docs/research-obstruction-next.md`: `m(P)` not a function of `e(P), width, #min/#max`, merge-like and other structures create gaps). Without a precomputed table, a uniform algorithm must *discover* which of these branches are admissible by exploration; a memoization cache avoids recomputations but the cache itself must be built on-the-fly and in the worst case will need to account for a large frontier (and storing it is costly). The `uniform-sergeev-transition-machine` analysis on the board notes extracting finite uniform parameters is a separate task with discipline constraints not obviously ruled out - consistent with extraction being nontrivial even if not obviously impossible.

**Conclusion:** I cannot produce an unconditional `2^{\Omega(n\log n)}` time lower bound for all uniform algorithms (AGENTS explicitly forbids spending time on unconditional super-polynomial lower bounds for the unary language; circuit/P/poly tools don’t apply). I also do not have a uniform algorithm achieving `2^{o(n\log n)}`. The concrete obstruction is the depth+pair-branching product plus the need to extract admissible pruning rules on-the-fly in the presence of a large, locally non-reducible winning frontier - this matches the stated “extraction cost” intuition, but it remains a barrier/complexity intuition rather than a proved lower bound. No repository changes are warranted.

## Other metadata

```json
{
  "finished_at": 1793444387.192183,
  "started_at": 1793443894.3332283
}
```
