# antonina-9kBTemfyafdW7ZvMnbnum6-tact

Session: ses_e14bb34f5ffe4qDLuxKk7zblOa
Workspace: /home/lubko/soring-fronts/antichain-reachable-state-count-subquadratic-exponent
Created: 1794948516700; updated: 1794948605607

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 69 (msg_1eb4503c5001sc8AqvRLxP6jqs)

## Interpretation (fixed for this report)
- **[definition]** A (deterministic, adaptive) strategy/decision tree from the `n`-antichain has root the empty poset and, at each non-total state, a chosen incomparable pair; each answer gives one of two children and every root-to-leaf path reaches a total order. The strategy is *optimal (minimax)* if its height is `S(n)` (worst-case comparisons).
- **[definition]** “Distinct partial orders reachable … by some optimal minimax comparison strategy”: the set of transitively-closed posets `P` that appear as node states on any play consistent with a fixed optimal strategy (all its root-to-node paths). (If instead read as the union over *all* optimal strategies, the same upper bound below applies a fortiori, since that union is a subset of all states reachable within `S(n)` comparisons.)

## Front question
“For all sufficiently large n, is the total number of distinct partial orders `P` reachable from the `n`-element antichain by some optimal minimax comparison strategy bounded above by `2^{o(n^2)}`?”
**Falsifier target:** an infinite family of `n` with **every** optimal strategy visiting `>= 2^{c n^2}` distinct reachable `P` for some fixed `c>0`.

## Mathematical finding (deduction): the subquadratic-exponent upper bound holds; the stated falsifier is impossible
**Claim. [deduction]** For every `n>=2` and every optimal minimax strategy `π` from the `n`-antichain,
`|Reach(π)| <= (2*B(n))^(S(n)+1) = 2^{O(S(n) log n)} = 2^{O(n log^2 n)} = 2^{o(n^2)}`,
where `B(n)=binom(n,2)` and `Reach(π)` are the distinct poset states on `π`.

**Proof sketch.**
1. **[definition/deduction, standard minimax game; docs/upper-bound.md, docs/research-budgeted-dfs.md §1,4,13]** States are transitively-closed strict partial orders on `n` labelled elements (start empty). A move compares an incomparable pair and yields 2 possible successor closures; each step strictly decreases the number of incomparable pairs, and `S(n)=F(∅)` is the minimax height.
2. **[deduction]** An optimal strategy has height `S(n)`, so every state in `Reach(π)` lies on some root-to-node path of length `<= S(n)` and is in particular reachable within `S(n)` comparisons from the antichain.
3. **[deduction, docs/research-budgeted-dfs.md §4,13]** In the full comparison game, each nonterminal node has at most `2*B(n)=n(n-1)` children and depth `<= d`, hence the whole depth-`d` game tree has at most `sum_{t=0}^{d} (2B)^t <= (2B)^(d+1)` node-occurrences; therefore the number of *distinct* posets reachable within `d` comparisons by *any* choices is at most `(2B)^(d+1)`.
4. Taking `d=S(n)` and `B(n)<=n^2` gives `|Reach(π)| <= 2^{(S(n)+1) log2(2*n^2)} = 2^{O(S(n) log n)}`. Using the information-theoretic/constructive envelope `S(n)=Theta(n log n)` (`ceil(log2(n!)) <= S(n) <= O(n log n)`; [literature] Ford–Johnson/Knuth; problem.md) yields `|Reach(π)| <= 2^{O(n log^2 n)} = 2^{o(n^2)}` for all sufficiently large `n` (since `n log^2 n / n^2 -> 0`).

**Consequences.**
- **[deduction]** The front’s upper-bound property is **true for all sufficiently large `n`** (indeed for all `n>=2` under the stated bounds), even uniformly over *all* strategies of depth `<=S(n)`, not only some optimal one: the reachable-optimal state space is `2^{O(n log^2 n)}`.
- **[deduction]** The proposed falsifier cannot exist: for fixed `c>0`, `2^{c n^2} > 2^{O(n log^2 n)}` for all sufficiently large `n`, so no infinite family can have every optimal strategy visiting `>= 2^{c n^2}` distinct reachable states (in fact no strategy of height `S(n)` can, on any `n` past that threshold). This is a counting/depth obstruction, not a complexity-class separation.
- **[deduction, model fidelity]** This does **not** contradict the known `2^{O(n^2)}` (indeed `2^{Theta(n^2)}`) *enumeration* bound for the memoized minimax/DP over **all** labelled posets/states (docs/upper-bound.md, research-budgeted-dfs.md §13): `2^{O(n^2)}` counts the ambient poset space, whereas reachability within the `S(n)=Theta(n log n)` comparison budget cuts it to `2^{o(n^2)}`. It also does not by itself yield a faster uniform evaluator or any separation for `SORT-BOUND-U`.

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
