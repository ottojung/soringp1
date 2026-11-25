# antonina-0JvxMMFH56LX8SXQJ7gYOM-sleeves

Session: ses_e52998022ffe47uRKqv7UiL4yn
Workspace: /home/lubko/soring-fronts/fo-tc-varying-block-program-20261105
Created: 1793910538328; updated: 1793910595219

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 59 (msg_1ad66e55f00173LEyMh5clX6NG)

## Finding

A **Savitch-style reachability subroutine** sharpens the budgeted DFS’s *parameterized* space bound, but does **not** improve either worst-case bound named in the question. I found no general compression of the minimax recursion stack that would yield a smaller all-\(n\) asymptotic bound.

### Accounting

At recursion depth \(t\), the current state is the initial antichain plus the \(t\) comparisons on the path. The DFS must also retain the candidate-pair cursor at each suspended frame. In the ordinary transcript implementation:

- Each path comparison takes \(2\lceil\log_2 n\rceil\) bits.
- Each cursor takes \(\lceil\log_2(\binom n2+1)\rceil=O(\log n)\) bits.
- Thus the stack and transcript take \(O(t\log n)\) bits, not \(O(n^2)\) per frame.
- Reachability in the transcript graph can use a BFS workspace of \(O(n\log n)\) bits. It is temporary: only one such workspace is live at a time.
- Total space is \(O((k+n)\log(n+2))\) for a threshold call at budget \(k\), or \(O(n\log^2 n)\) for numeric \(S(n)\), since its search uses budgets up to \(U(n)=O(n\log n)\).

The existing note’s reachability discussion points to Savitch’s theorem. Applying its recursive reachability algorithm to the graph on \(n\) labels reduces the temporary workspace to \(O(\log^2 n)\) bits, plus counters and transcript access. This gives the more precise bound

\[
O\bigl((k\log(n+2))+\log^2(n+2)\bigr)
\]

for a threshold call, and \(O(n\log^2 n)\) for numeric evaluation. The recursive reachability computation costs \(n^{O(\log n)}=2^{O(\log^2 n)}\) time per query. That overhead is absorbed by the DFS’s \(2^{O(k\log(n+2))}\) total search bound (and by the numeric-function bound); it does not worsen the established time upper bounds. This is an algorithmic deduction from the standard Savitch reachability bound, not a new literature result.

For unary input length \(N=n+k+1\), after trivial cases, the parameterized space is at most \(O(N\log N)\). In the worst case \(k\) can be \(\Theta(N)\), so this does **not** improve the established worst-case \(O(N\log N)\) threshold-space bound. Likewise, numeric evaluation still has an \(O(n\log n)\)-deep search stack with \(O(\log n)\) bits of transcript/cursor data per frame, so this substitution does **not** improve its \(O(n\log^2 n)\) bound.

### Representation limitation

For this specific DFS representation, the stack stores a comparison choice and a suspended loop cursor per active level. That accounts for \(O(k\log n)\) bits. It is a bound on this representation, **not** a lower bound on the decision problem or on all uniform algorithms: a different traversal, compressed encoding, or recomputation scheme could avoid that storage. I do not have a rigorous argument excluding those approaches.

### Literature and checks

The repository’s `docs/research-budgeted-dfs.md` already identifies Savitch-based reachability as a way to remove the BFS \(+n\) workspace term, while explicitly leaving sharper overall space bounds open. The relevant standard result is Savitch’s reachability theorem: directed reachability on \(n\) vertices uses \(O(\log^2 n)\) deterministic space. It supports the subroutine improvement above, not an improvement to the complete worst-case bounds. No literature result found here establishes a smaller space bound for exact sorting-number evaluation.

I made no repository changes or posts. I did not run experiments: small-instance DFS checks cannot establish an asymptotic space improvement, and the parameterized bound follows directly from the representation and reachability accounting.
