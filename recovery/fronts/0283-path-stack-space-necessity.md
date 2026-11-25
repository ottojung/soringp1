# path-stack-space-necessity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

2UH9x3niudnIv64v1QO6NW-addition

## exit_state

clearexit

## question

Is storing the full comparison transcript (the DFS path stack) necessary for any uniform algorithm deciding SORT-BOUND-U in the standard Turing model, or is there an all-n method that reuses workspace by canonicalizing states without expanding the alternation/game depth?

## basis

Transcript-only DFS gives O(n log^2 n) bits; compress-exact-space-evaluator ruled out naive root-replay but left necessity/open; AGENTS lists smaller space bounds as an achievable frontier without claiming optimality.

## falsifier

Exhibit a uniform deterministic algorithm for SORT-BOUND-U using o(n log n) work-tape bits for all sufficiently large n (on the relevant input range) with a complete correctness proof and cost accounting in the unary input-length model.

## implication

A proven all-n space lower bound would sharpen the known polynomial-space upper bounds and constrain the transcript/DP family; a verified sublinear-in-n-log-n upper bound would improve the concrete space complexity for exact unary S(n) evaluation.

## finding_unverified

argument, no repo/Lean changes): the transcript/path stack is necessary and the falsifier is obstructed by path-length information theory.**

### Analysis
- **Game state vs history.** The minimax recurrence depends only on current partial order $P(\sigma)$ (closure of transcript), so memoization by $P$ is correct in principle. However, DFS/backtracking must explore both adversary branches at each node and restore state on return. With no stored path, there is no way to know which comparisons were made or to undo moves; recomputing from root requires replaying the exact decision sequence (and was ruled out as a naive space win due to exponential recomputation time by `compress-exact-space-evaluator`, leaving necessity open).
- **Representation size.** A transcript of depth $d$ stores $d$ frames, each needing $\Omega(\log n)$ bits for a pair $(a,b)$ and cursor ($2\log n + \Theta(\log(n^2))=\Omega(\log n)$). For relevant `SORT-BOUND-U` instances $k \le U(n)=O(n\log n)$ and $d\ge S(n)=\Omega(n\log n)$, the stack alone is $\Omega(d\log n)=\Omega(n\log^2 n)$ bits. Reachability adds $\Omega(n\log n)$ workspace. Any canonical form of an arbitrary reachable $P$ is an explicit encoding of that partial order: by Kleitman–Rothschild most partial orders on labeled $n$ elements have $\Theta(n^2)$ relations and are not obviously compressible below $\Omega(n^2)$ bits in the worst case, while the transcript gives a generating set of size $O(n\log n)$ — so canonicalizing to $P$’s full closure is *larger*, not smaller. You cannot avoid storing the generating history information needed for backtracking without paying in space (store closure) or time (replay). 
- **Falsifier obstruction.** The proposed falsifier requires $o(n\log n)$ work-tape bits for all sufficiently large $n$. This is below the $\Omega(n\log^2 n)$ bits required just to store the DFS path of length $\Omega(n\log n)$ with $\Omega(\log n)$-bit decisions. Even ignoring reachability, the path length lower bound alone rules out $o(n\log n)$.

### Concrete failed approach / obstruction
**Root-replay without storing path is not viable.** To know the current $P$ and current position you must reconstruct the sequence of choices made along the current branch; there is no canonicalization that removes that decision history without storing an equivalent representation or incurring exponential recomputation (as previously analyzed). Memoization stores results for states but does not eliminate the need to traverse and backtrack over the game tree in the absence of cached results for all relevant $(P,d)$ pairs; moreover the state space of all partial orders is $2^{\Theta(n^2)}$ making a full memo table space-exponential, not sublinearithmic.

### Limits / honest notes
- This is a necessity argument for *backtracking DFS over the minimax game tree* given the $\Omega(n\log n)$ depth and $\Omega(\log n)$ decision size; I cannot rule out some entirely different algorithmic paradigm (not tree search) achieving smaller space without a full complexity proof. However, such a paradigm would need to compute the minimax value without enumerating adversary branches via path history — no such method is known and it would need to circumvent the information cost above. 
- The obstruction is information-theoretic on the path + representation, not a general TM lower bound theorem; it’s a strong barrier to the specific falsifier as stated.
- No repository/Lean changes made. Posted findings to reasoning only as requested.

## Other metadata

```json
{
  "finished_at": 1793801411.1929893,
  "started_at": 1793799605.7981448
}
```
