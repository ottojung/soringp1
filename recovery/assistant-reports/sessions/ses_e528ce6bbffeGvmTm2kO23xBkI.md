# antonina-00DTrrKaw3BVhg5z4fnkxY-speedily

Session: ses_e528ce6bbffeGvmTm2kO23xBkI
Workspace: /home/lubko/soring-fronts/fo-tc-combined-review-20261105
Created: 1793911363938; updated: 1793911396005

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ad731992001aLKIacQdXvMMak)

I’ll trace the existing budgeted-DFS argument and its stated machine bounds, then independently account for each operation under a standard deterministic model. I’ll keep the function and unary-language bounds distinct and leave the repository untouched.

## Output 36 (msg_1ad7357d0001arJcY74mSCVYEz)

**Conclusion:** I found no specific incorrect asymptotic claim in `docs/research-budgeted-dfs.md` for the transcript-only evaluator or the unary bounds. The stated bounds follow under a conventional deterministic multi-tape TM accounting. The main qualification is that the note’s time estimates assume polynomial cost per search node; that cost can be made explicit as below.

### Machine-model accounting

Use a deterministic multi-tape TM with read-only input, binary work-tape counters, and labels in `[n]` encoded in `⌈log₂(n+1)⌉` bits. Let `t` be the transcript length at a node; `t ≤ d`. The DFS uses one shared transcript, plus a frame per active recursive call containing its pair-loop cursor and branch phase. A frame and transcript entry each require `O(log(n+2))` bits. Thus the stack and transcript use `O((d+1) log(n+2))` bits.

For a reachability query, scan the transcript to construct adjacency lists, then run iterative DFS with a visited vector and a stack of at most `n` labels. This costs `O(n log n + t log n)` work bits and polynomial time in `n` (even with tape scans to access the lists). Release this workspace before recursing. Hence the per-call peak is
`O((d+n) log(n+2))` bits, including the `d=0` case.

To test whether a pair is incomparable, run at most two reachability queries. Enumerate all candidate pairs with two label counters; there is no stored pair list. Testing totality likewise uses at most `O(n²)` pair tests. Therefore all node-local work takes `poly(n+d)` time, and the stack is shared across the entire DFS, not copied for each child. Branching is at most `2·binom(n,2) < n²`; depth is at most `d`. The total search time is consequently
`2^{O(d log(n+2))} poly(n+d)`.
The polynomial factor is absorbed in the exponential for the function and nontrivial threshold bounds here.

For input handling, scan the unary blocks and count `n,k` in binary; compute `U(n)=n⌈log₂ max(2,n)⌉` with binary counters. On a valid unary threshold instance, if `k≥U(n)`, accept using the merge-sort upper bound; otherwise run `CanSort(∅,k)`. Parsing and preprocessing take polynomial time in actual input length `N`, with `O(log N)` work bits beyond the evaluator.

### Separate bounds

- **Function `S_unary(1^n)`:** binary search over `[0,U(n)]` makes `O(log n)` calls, each with `d≤U(n)=O(n log n)`. This gives deterministic time `2^{O(n log² n)}` and work space `O(n log² n)` bits, where `n` is the numeric value and also the function input length.
- **Unary threshold language:** after trivial-`k` preprocessing, `d=k<U(n)`. Since `n,k≤N`, time is `2^{O(k log(n+2))}poly(N) ≤ 2^{O(N log(N+2))}`; space is `O((k+n)log(n+2)) = O(N log(N+2))` bits.
- For `n≤1`, the answer is immediately yes. This avoids relying on logarithmic expressions for those edge cases.

Small-case checks are sanity checks only; the bounds above come from the accounting, not experiments. No files were edited, and no post or commit was made.
