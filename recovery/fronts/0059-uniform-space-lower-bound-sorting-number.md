# uniform-space-lower-bound-sorting-number

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ogB9icxDmDERQoEsmEIHDa-scanned

## exit_state

clearexit

## question

For SORT-BOUND-U = {1^n # 1^k : S(n)<=k} on multitape TMs with input length N=n+k+1, is there an all-n uniform space lower bound Ω(N log N / log log N) ruling out o(N log N / log log N) work tape for all large N, or does some uniform algorithm achieve strictly smaller space for all (n,k)?

## basis

research-budgeted-dfs.md gives O(N log N) work tape; AGENTS.md allows space/upper-bound improvements as a productive frontier distinct from circuit lower bounds.

## falsifier

Construct a deterministic uniform TM deciding SORT-BOUND-U for all (n,k) using S(N)=o(N log N / log log N) space for all sufficiently large N with an explicit correctness and space analysis.

## implication

A uniform space lower bound would tighten the known O(N log N) bound below PSPACE in a nontrivial way; a constructive falsifier would show the transcript-only DFS bound is not asymptotically tight for space and suggest better evaluators exist.

## finding_unverified

 using a method with less stack space?

Another idea: use a tree automaton or other method?

Alternatively, notice that this is similar to some "path constraints" and use a different representation.

Or consider using a technique with O(sqrt(N log N)) or some other bound? Probably not obvious.

Alternatively, let us look up the compress-exact-space-evaluator again more. They tried root-replay (reconstruct from root each time) and said "Storing a DFS-node rank has a straightforward worst-case cost of O(k log n) bits, the same order as the path stack. Regenerating a target node from the root at each frame can repeatedly traverse earlier subtrees; the direct bound grows to 2^(O(k^2 log n)), rather than the existing 2^(O(k log n)) time. This rules out that naive reconstruction strategy, but does not prove that every exact evaluator needs the path stack or rule out a better canonical encoding."

So a better canonical encoding might help. Maybe find a more compact canonical form of the partial order state?

Or use a different representation of the search path?

Alternatively, use a technique where we don't store the full path but store checkpoints?

For example, store state every m levels and reconstruct from nearest checkpoint? That would give space O(m log n) plus reconstruction overhead in time. If we choose m well...

But is it possible to do better than O(k log n) total? Maybe O(sqrt(k) log n)?

Let us think. If we store checkpoints every t levels: store t+1 checkpoints max in some scheme? Or store checkpoints at positions t, 2t, 3t,... Total checkpoints = d/t. Each checkpoint needs to store the full state at that point. State is similar size to a full transcript up to that point? Or we can store the transcript up to checkpoint.

Alternatively, use a technique with O(sqrt(D)) space for DFS of depth D? Not exactly. Or use "tree decomposition".

Or more generally, use a technique where you trade time for space - store some states and recompute others.

But for DFS with backtracking, it's a bit tricky.

Alternatively, use a method where we record the "path signature" and can reconstruct quickly?

Maybe use a persistent data structure with path copying? No, worse.

Alternatively, use a technique called "recursive DFS with limited stack" or use a explicit stack with only necessary information.

Another possibility is to use a different algorithm like iterative deepening A* or other methods? Probably not applicable.

Alternatively, notice that the bound N log N / log log N - can we achieve something like O(N log N / log something)? Maybe using more efficient data structures?

Or use bit packing more aggressively?

Or notice that some values don't need full log n bits?

Probably not giving asymptotic improvement.
Let us analyze this checkpointing approach more carefully.

I'll analyze this space question systematically.

I examined the space complexity of deciding SORT-BOUND-U via the transcript DFS (with Savitch for reachability). No such lower bound appears in the repo's established results - only that poset-state size doesn't force Ω(n^2). The current worst-case O(N log N) is dominated by the stack of comparisons+cursors (depth k = O(n log n), each frame needing O(log n) bits). Removing cursors or using checkpoints gives partial improvement, but beating N log N / log log N in the worst case would require reducing k/log n factors; no obstruction or construction is apparent from the examined literature/codebase. This remains an open question.


## Other metadata

```json
{
  "finished_at": 1793374287.9439662,
  "started_at": 1793367315.5654497
}
```
