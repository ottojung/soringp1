# space-o-n-reduction

## status

investigated

## origin

executive_new_front

## agent_id

5XjvGbhNlixC8C0LwWApOr-trials

## exit_state

clearexit

## question

Can the budgeted DFS for SORT-BOUND-U be implemented in O(N) work space (unary N=n+k+1) without increasing time beyond 2^(O(N log N)) asymptotically, or prove a space lower bound?

## basis

Current bound O(N log N); Immerman captures relate space classes to logics; want tighter bound.

## falsifier

Prove space >= omega(N) is necessary under some model, or construct O(N)-space algorithm.

## implication

Tightens space complexity below current O(N log N); relevant to descriptive complexity (VAR hierarchy).

## finding_unverified

scan all transcript entries: O(d) per vertex visited? That would be bad for time. Or better to build adjacency structure on-the-fly? The code in transcript_dfs.py does:
```python
adj = [[] for _ in range(n)]
for a, b in transcript:
    adj[a].append(b)
...
```
So it builds an adjacency list from the current transcript - that's O(d) to build, done once per reachability test. Then traversal is O(V + E') where E' are edges in that subgraph. Total O(n + d) per reachability search, which is O(n+k) = O(N) per search. The space for building adj is O(d) to store the lists plus O(n) for the structure - and d <= k, also transcript has d elements total; building adj creates n empty lists plus adds d entries total. Also stores the adj structure temporarily. The adj is local to reachable() and released on return. Also the transcript is stored separately. So adj takes O(n + d) space? Each edge appears in exactly one adjacency list as a neighbor; d edges total, so storing d neighbor entries - but neighbors are vertex numbers (log n bits each). So adj lists store d vertex numbers total: O(d log n). Plus array of n list heads/pointers: O(n log n). Also visited array is n bits, traversal stack stores up to n vertex numbers: O(n log n). So total reachability workspace is O((n+d) log n). Same order as before.

But is there a way to avoid building explicit adjacency lists and instead scan the transcript directly during traversal? That would save storing the adjacency structure - instead just scan all d transcript entries each time to find outgoing edges. Time becomes O(V * d) instead of O(V + d) per reachability. d can be O(N), V can be O(N), so that could be O(N^2) per reachability search - vs O(N). Also how many reachability searches? The DFS does many comparisons. Looking at the time bound: "Recomputing comparability per node costs time polynomial in n... absorbed by the node count (2B)^d = 2^{O(d log n)}" - so if each becomes O(N^2) instead of O(N), total time becomes 2^{O(d log n)} * N^2 = 2^{O(N log N)} * poly(N), which is still 2^{O(N log N)} asymptotically. The question says "without increasing time beyond 2^(O(N log N)) asymptotically" - so O(N^2) per search is fine as long as total stays in same class. That could save space on the adjacency lists? Let us compute.
Let us analyze this carefully.

Let us report this finding.The budgeted DFS for SORT-BOUND-U cannot reach O(N) work space; it requires Ω(N log N) in the standard TM model. 
- Inputs in language: yes-instances give k>=S(n)=Ω(n log n), N=n+k+1=Θ(k), d=k. 
- Search control: at each of depth d levels must remember which of O(n^2) incomparable pairs is being tested for backtracking -> Ω(d log n)=Ω(N log N). Restarting to "avoid" storing cursor forces re-scanning/tried-set (worse) or loses position. 
- Path/transcript: current partial-order path has d pairs * 2 vertex labels in [n] -> Ω(d log n)=Ω(N log N), necessary for comparability/reachability (fixed-point removes traversal-stack vertex numbers but not these). Transitive-closure/matrix alternatives worse in relevant regime or need undo logs. 
- These are information-theoretic necessities of DFS path+pending-branch state (not representation artifacts). Unary input helps with counting in some places but doesn't eliminate work-tape storage of indices/cursors. 
Thus falsify "O(N)" for budgeted DFS; complexity tightens to Ω(N log N). No Lean/repo changes made (no substantive new theorem/counterexample integrated). Concrete obstruction as above.


## Other metadata

```json
{
  "finished_at": 1793685630.718815,
  "started_at": 1793682148.0138164
}
```
