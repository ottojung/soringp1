# local-gap-global-complexity-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

3fcWCzT0arU7iCqyjeNBWt-language

## exit_state

clearexit

## question

Since the merge family shows local gaps m(P)-ceil(log2 e(P)) are unbounded as n grows, is there an all-n structural obstruction (not depending on circuit lower bounds) implying that any uniform algorithm must track such unbounded local gaps, forcing SORT-BOUND-U not in DTIME(2^(n^c)) for some c<1 or creating a barrier to subexponential uniform evaluation?

## basis

Research-obstruction-next.md shows merge family gives unbounded local gaps m(P)-ceil(log2 e(P)); transcript-canonicalization/winning-frontier discuss enumeration barriers but local-gap->uniform-time not formalized as all-n theorem.

## falsifier

Exhibit a uniform subexponential algorithm that evaluates S(n) without explicitly enumerating poset states realizing large local gaps, with a correctness argument exploiting the comparison structure to bypass that obstruction.

## implication

Linking unbounded local gaps to uniform time complexity would provide a concrete barrier to subexponential algorithms distinct from winning-frontier enumeration counts alone.

## finding_unverified

 by enumerating states that realize those gaps. The obstruction is computational difficulty of *recognition/computation* in general, not a logical necessity to enumerate.

**Where the obstruction might still bite (honest limits):**
- **Recognition cost.** Isomorphism/decomposition into chains/series-parallel is easy here, but general posets? Also e(P) is #P-hard to count exactly in general (Brightwell–Winkler) — but for the cutoff we have poly-space $e\_exceeds$ (stop at cap+1). The gap being large means $m(P)$ large relative to info, but computing $m(P)$ directly is the hard part.
- **Not all states are merge states.** The worst local gap at small e comes from non-merge posets ($e=8$ witness is connected, not union of chains). The global obstruction for $n=12$ is not explained by merge decomposition alone.
- **No known subexponential algorithm.** Even with structure recognition, the budgeted DFS is $2^{O(N\log N)}$ for unary input length $N$; I know of no published subexponential (in $n$) exact algorithm for $S(n)$. The barrier would be different from “must enumerate gap states”.
- **Distinguish soundness vs completeness.** Structural formulas are sound if values are certified; but getting a complete, uniform algorithm that applies them correctly for all states reachable from antichain is nontrivial. The question says “exhibit a uniform subexponential algorithm…” — I cannot construct one from inspection; plausible directions (recursive decomposition, structure-aware minimax with memoization by canonical form) are standard but I don’t see a proof they give subexponential time, and the winning frontier suggests enumeration barriers remain.
- **Complexity class link not formalized.** Connecting “unbounded local gaps” to $DTIME(2^{n^c}), c<1$ is not formalized anywhere in repo. The winning frontier gives a concrete enumeration obstruction; the local-gap argument as stated lacks a reduction showing you can’t do better than tracking them.

**Concrete failed approach / obstruction:**
I tried to see if merge gaps force state enumeration — no, because $M(a,b)$ is computable by known results/formulas in certified ranges without exploring the game tree. The real obstruction is: (1) most states aren’t decomposable into known classes, (2) $e(P)$-based pruning is necessary but not sufficient and counting is hard in general, (3) winning frontier shows many states exist regardless. The local-gap->uniform-time link is not a theorem here; it’s a conjecture. I cannot produce a counterexample algorithm, nor can I prove the obstruction holds. The strongest honest conclusion: the “must track unbounded local gaps” claim is too strong (structure recognition bypasses it for that family), but replacing it with a clean barrier theorem connecting local gaps to uniform time complexity would require new mathematics not present in the repo.

**Bottom line:** The merge family shows unbounded local gaps (true). That alone doesn’t imply you must enumerate those gap states — formulas/compositional bounds suffice for them. A distinct barrier is the winning frontier (many winning states). No formal theorem links unbounded local gaps to subexponential time lower bounds for uniform exact $S(n)$ computation; I cannot disprove the frontier as stated, cannot construct the requested falsifier algorithm, and see no clean all-n obstruction from local gaps alone. This matches AGENTS.md’s caution against transferring arbitrary poset hardness without reduction to the antichain root.

## Other metadata

```json
{
  "finished_at": 1793775622.5770261,
  "started_at": 1793773366.9407942
}
```
