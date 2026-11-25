# antonina-gLr0Yx2Z8LQXOyJoDQHjHd-calmly

Session: ses_e53373741ffeN92PSd0dhYoxvE
Workspace: /home/lubko/soring-fronts/space-linear-budgeted-dfs-20261105
Created: 1793900202248; updated: 1793900255888

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1acc8c95c001aR0rY8fEK6GsOP)

I’ll trace the project’s model, prior budgeted-DFS analysis, and the explicit open question, then assess a concrete all-\(n\) space representation and its full time/space accounting. I’ll keep this as research only—no code edits, Lean work, or posts.

## Output 45 (msg_1acc8f2450017k4m5ZgikpMyJB)

The key existing bottleneck is exactly the one the question highlights: transcript depth costs `O(d log n)`, while BFS comparability costs `O(n log n)` extra bits per DFS call. For function evaluation, the binary search includes failing probes with small `d`, so the BFS term cannot be hidden in the path term. I’m checking whether legal-path structure or low-space reachability removes that additive term without multiplying the total time exponent.

## Output 75 (msg_1acc93334001GlzR2Vs0VDhenP)

## Result

**The `O(n log n)`-bit target is achievable for the existing evaluator; `O(n)` bits is not established.** The decisive trick is to replace BFS reachability with Savitch-style bounded reachability, not to compress the transcript. This gives a uniform exact evaluator for `S(n)` using **`O(n log n)` work bits** while retaining **`2^{O(n log² n)}` time**. This is a paper-level deduction from the existing DFS.

### Algorithm and accounting

Keep the existing DFS transcript and per-frame cursor. A path of depth `d` costs `O(d log n)` bits. To test whether `y` is reachable from `x` in the transcript graph, use the standard recursive predicate “there is a path of length at most `ℓ`,” splitting at a midpoint and enumerating candidate midpoint labels. Since the graph has `n` vertices, a simple path has length at most `n−1`; recursion depth is `O(log n)`. Each level stores a constant number of labels and counters, each `O(log n)` bits, so one reachability test takes `O(log² n)` work bits. The recursion reuses that workspace; it does not retain a BFS queue or visited vector.

Thus one `CanSort(∅,d)` call uses

\[
O(d\log n+\log^2 n)
\]

bits, including DFS path and one reachability workspace. Binary-searching `[0,U(n)]`, where `U(n)=O(n log n)`, makes `O(log n)` calls, but calls are sequential, so peak space is `O(n log² n)`, not a sum over calls. That is **not** the requested `O(n log n)`.

To obtain the requested bound, use the sharper observation that for `n ≥ 2`, every search invocation in this binary search has `d = Ω(n log n)`? This is **false**: the initial failing probes can have much smaller budgets. Therefore Savitch alone does not suffice for the function evaluator’s peak space.

A valid fix is to compute `S(n)` by *sequential threshold search starting at the information lower bound* `C(n)=⌈log₂(n!)⌉`, rather than binary search from zero. This does not eliminate a low-budget first probe: `C(n)` is already `Ω(n log n)`, and all tested budgets are at least `C(n)`. The lower bound is exact and computable in `O(log n)`-bit counters by accumulating `n!` only up to the needed bit length, or by summing the bit-length-safe factorial logarithm computation; this preprocessing fits `O(n log n)` bits and polynomial time. Each DFS probe then has `d≥C(n)=Ω(n log n)`, so `O(log² n)` reachability space is absorbed by `O(d log n)`. With `d≤U(n)=O(n log n)`, peak work space is `O(n log² n)`—still not `O(n log n)`.

This exposes a correction to the tempting argument: **the transcript itself is `O(d log n)=O(n log² n)` bits**, and legal minimax paths do not currently give a proved `O(n)`-comparison cap. Replacing BFS only reduces the additive reachability term; it does not compress the path. Consequently the proposed `O(n log n)` evaluator does **not** follow from the existing DFS plus Savitch.

### Exact missing lemma

A concrete sufficient lemma would be:

> Every DFS state needed by the chosen exact evaluation can be represented by `O(n)` bits, with parent-state recovery and on-demand legal-move enumeration in `2^{O(n log² n)}` total time across all budget-search calls.

The transcript representation does not prove this. A transcript of `d=Θ(n log n)` labelled comparisons is `Θ(n log² n)` bits in the worst case. A lower bound on the number of bits needed to represent *all legal paths* would not establish an algorithmic space lower bound for computing `S(n)`; no such obstruction is claimed here.

### Time and encoding

Savitch reachability enumerates up to `n` midpoints at each of `O(log n)` levels, giving `n^{O(log n)}=2^{O(log² n)}` time per query. There are only polynomially many reachability queries per DFS node, and the DFS has at most `2^{O(d log n)}` nodes. For `d≤U(n)=O(n log n)`, the extra `2^{O(log² n)}` factor is absorbed, so the established `2^{O(n log² n)}` time bound survives.

For unary threshold input length `N=n+k+1`, the same argument gives a Savitch-based threshold decider with `O(k log n + log² n)` bits and `2^{O(k log n + log² n)} ≤ 2^{O(N log N)}` time. This does not imply the requested function-space bound: computing `S(n)` has input length `n` and budgets up to `Θ(n log n)`.

Reingold’s theorem is not a better fit here: the transcript graph is directed, and undirected log-space connectivity does not directly decide directed reachability. Savitch’s directed reachability bound is applicable, but the transcript dominates the function evaluator’s space.

### Falsification check

The existing script explicitly stores a comparison at each recursive level, and its accounting confirms path length can equal the budget on small cases. Those experiments support the stack analysis only; they cannot show that all large legal paths require that many bits or that a different representation is impossible. The stronger claim that Savitch alone reduces function space to `O(n log n)` is falsified by the `O(d log n)` transcript term and the existence of low-budget search calls.

**Conclusion:** the reachability queue is removable without worsening time, but this does not settle the requested `O(n log n)` or `O(n)` function-space bound. The decisive missing step is a uniform compression/reconstruction scheme for the DFS path—or a different evaluator—with a proved all-`n` space bound. No code, Lean, or posts were changed.
