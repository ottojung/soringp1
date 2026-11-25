# antichain-reachable-state-count-subquadratic-exponent

## status

investigated

## origin

ai_proposal_unverified

## agent_id

9kBTemfyafdW7ZvMnbnum6-tact

## exit_state

clearexit

## question

For all sufficiently large n, is the total number of distinct partial orders P reachable from the n-element antichain by some optimal minimax comparison strategy bounded above by 2^{o(n^2)} (in contrast to the known 2^{O(n^2)} state-enumeration upper bound for the recurrence)? A single explicit infinite family of n with every optimal strategy path visiting >=2^{c n^2} distinct reachable P for some fixed c>0 would falsify this subquadratic-exponent claim.

## basis

AGENTS/problem report the 2^{O(n^2)} numeric-n minimax recurrence and PSPACE context for SORT-BOUND-U; board work on space/transcript and oracle necessity shows state growth is a live obstruction, while no proved o(n^2)-exponent state bound for reachable optimal paths is established.

## falsifier

Give an infinite sequence of n and a proof that all optimal minimax paths from the n-antichain visit >=2^{c n^2} distinct poset states for some fixed c>0, or exhibit a concrete counterexample n with that lower bound over all optimal paths.

## implication

A yes would tighten uniform state-space bounds behind exact S(n) evaluation (affecting DP/memoization prospects and the 2^{O(n^2)} numeric-n analysis) without implying a complexity-class separation; a no (cubic-in-exponent behavior) would reinforce an intrinsic combinatorial barrier for naive state DP and focus effort on structural/branching methods for SORT-BOUND-U.

## finding_unverified

 any separation for `SORT-BOUND-U`.

## Primary literature / basis consulted
- **[literature]** L. R. Ford Jr. & S. M. Johnson (1959), merge-insertion sorting; D. E. Knuth, *TAOCP* Vol. 3 §5.3.1 — comparison-count model and `Theta(n log n)` worst-case scale for sorting/`S(n)`.
- **[literature]** M. Peczarski, *Towards optimal sorting of 16 elements* (2012) — exact/comparison-count context; F. Stober & A. Weiß, ALENEX 2023 (arXiv:2206.05597) — exact `S(16..18), S(28)` lower bounds (confirms `S(n)` grows on the `n log n` scale in known range). (Used only for scale/context; no small-`n` enumeration performed here.)
- **[repo/established]** docs/problem.md, docs/upper-bound.md, docs/research-budgeted-dfs.md (esp. §4,5.3,13): partial-order minimax game, `2^{O(n^2)}` DP enumeration bound, and the `(2B)^d = 2^{O(d log n)}` reachable-within-budget node bound / `2^{O(n log^2 n)}` DFS accounting. docs/literature.md for the source map.

## Serious disproof attempt and failed/blocked directions
- **Attempted falsifier (disprove the `2^{o(n^2)}` upper bound):** find `c>0` and infinitely many `n` where every optimal strategy’s reachable set has size `>=2^{c n^2}`. **[deduction — fails]** Impossible by the depth bound above: any height-`S(n)` strategy has at most `2^{O(n log^2 n)} \ll 2^{c n^2}` total nodes/states for large `n`, independent of which comparisons are optimal. No optimal-path choice, adversary behavior, or symmetry argument can create more distinct states than there are steps × branchings available.
- **Alternate angle considered:** force many *distinct* posets (avoid collisions) along optimal plays to approach the node upper bound. **[open/inconclusive but non-falsifying]** Even if collisions were minimized, the ceiling is `2^{O(n log^2 n)}=2^{o(n^2)}`; tightening the *lower* envelope of `max_{π optimal}|Reach(π)|` or of the union over optimal strategies (e.g. can one guarantee `2^{Omega(n log^2 n)}` distinct states for all large `n`?) remains open here and was not resolved. It cannot yield a `2^{Omega(n^2)}` falsifier.
- **General-poset/state-space confusion checked:** large `2^{Theta(n^2)}` counts refer to all (labelled) partial orders or to DP state enumeration, not to states *reachable under an `S(n)`-bounded optimal strategy*; transferring the former to the latter would be unsound (and is exactly what the node/depth bound rules out).

## Honest limits
- **[deduction scope]** Result rests on the standard height/branching counting (`(2B)^{S(n)}` nodes) plus `S(n)=Theta(n log n)`; it assumes the usual adaptive-comparison minimax model (problem.md). It addresses *state counts reachable within optimal depth*, not the cost of representing, recognizing, or recomputing those states.
- **No new theorem beyond stated bounds claimed:** this is a direct consequence of recorded/standard bounds, reported to resolve the posed front/falsifier; it gives no improved algorithm, no tightened exponent below `O(n log^2 n)`, no NP/certificate result, and no complexity-class separation.
- **Open (distinct) questions:** exact growth of the number of states reachable by *optimal* strategies (union or worst optimal strategy) between `n log n`-scale and `O(n log^2 n)` in the exponent; structural characterization of which of the `2^{Theta(n^2)}` posets are ever optimal-reachable. I did not create Lean artifacts or repository changes (finding is a deduction from established bounds, not a new independently checkable theorem/counterexample requiring integration).

## Other metadata

```json
{
  "finished_at": 1794948612.6196094,
  "started_at": 1794948516.3566048
}
```
