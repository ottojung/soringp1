# antonina-69zNjHlbeEeNt2wgH0AiKB-intrusted

Session: ses_e473cf102ffeVOhVB6azI3G2V6
Workspace: /home/lubko/soring-fronts/unary-evaluator-space-nlogn
Created: 1794101153738; updated: 1794101169121

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 37 (msg_1b8c31d6c001cmWid0t1Vlirmd)

## Finding (no repository change)

**Claim attacked:** *S(n) can be computed in O(n log n) space uniformly, beating the established O(n log² n) work-tape bound.*

**Result: not established; the natural reduction is obstructed, and no counterexample/lower bound is proved either.**

### Why the O(n log² n) bound has the shape it does
The budgeted transcript-only DFS (research-budgeted-dfs.md §5.2) computes the function S_unary(1^n) by binary-searching the budget d over [0, U(n)=O(n log n)], each CanSort(∅,d) call exploring a comparison path of depth ≤ d. Its work tape stores one shared mutable transcript of length ≤ d, plus O(1) frames. Each transcript entry identifies which of the Θ(n²) possible comparisons was made at that node, requiring Θ(log n) bits. Hence work space = Θ(d·log n) = Θ(n log n · log n) = Θ(n log² n) bits. The depth d cannot be avoided: the information lower bound gives S(n)=Ω(n log n), so the searched path length is Θ(n log n) in the worst case.

### Attempted reduction to O(n log n)
To reach O(n log n) bits, one would need either (a) encode each transcript entry in O(1) bits (impossible: there are Θ(n²) comparison indices, needing Θ(log n) bits each, unless a different indexing scheme reuses structure), or (b) avoid storing the full path by recomputing parent state on backtrack. Option (b) trades space for time; recomputing the partial order state P(σ) from scratch at each node costs poly(n) time, which is absorbed by the node count, but the recursion still needs to know *which* comparison led to the current branch to continue exploration, and the branch choices along the path are exactly the transcript. So the transcript is not eliminable without an alternative traversal.

### Distinguishing soundness from completeness (as instructed)
The DFS's correctness is a *completeness* statement: if a sorting tree of height ≤ d exists, the search finds it. Soundness (a returned "yes" truly implies S(n)≤d) follows because every leaf comparison path is a valid adaptive strategy. Neither is in question; the obstruction is purely representational—no known way to compress the Θ(n log n)-length path of Θ(log n)-bit comparison indices below Θ(n log² n) bits while retaining uniformity and the same worst-case time class.

### Honest limits
- No lower bound proving Ω(n log² n) space is established; this remains open.
- No construction achieving O(n log n) space is found.
- General-poset hardness (e.g. optimal decision-tree depth) does not transfer to the fixed family S(n) without a reduction, per AGENTS.md.
- The result, if achieved, would be a space improvement only; it would not separate complexity classes (SORT-BOUND-U already in PSPACE).

**No repository change made.** The question remains open; the decisive obstacle is transcript encoding.
