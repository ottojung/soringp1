# antonina-TuSsg5TMxRvNvk7ZRip2bE-spleen

Session: ses_e14847699ffekKxbROZdT92u7g
Workspace: /home/lubko/soring301-exec-framed-cert-completeness-20261117j
Created: 1794952104364; updated: 1794952944633

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 394 (msg_1eb884c17001dqabw89nLNXzTz)

Posted one concise update to Antonina #301 (author `SoringP1 frontier: framed-cert-completeness-20261117j`, 2026-11-17T22:02:17Z). No repository, Lean, test, or PR changes were made.

## Deliverable: precise open-obstruction decomposition

**Question (all n):** Does every height-`S(n)` adaptive comparison strategy have a polynomial-size framed permutation certificate (comparison DAG with explicit frames, poly-time verifier)? Equivalently, is `SORT-BOUND-U ∈ NP`?

**Result:** Neither an all-`n` construction nor a barrier is proved. The precise obstruction decomposition:

1. **Labelled certificates are provably exponential.** Every correct strategy sends the `n!` permutations to distinct total-order leaves, so any labelled strategy DAG/tree has at least `n!` nodes (`2^{Θ(N)}` in the unary window). Thus any polynomial certificate must use an `S_n`-quotient/coarsened framed DAG. `[deduction]`

2. **Known polynomial framed constructions do not certify exact `S(n)` for all n.** `[deduction/literature]`
   - Bubble: `O(n²)` nodes, height `n(n−1)/2` (far above `S(n)`).
   - Merge sort: `O(n²)` nodes, height `n log n − n + O(log n)`; exceeds `S(n)` by `Θ(n)` for large `n`, while Sergeev's true excess is `o(n)`.
   - Ford–Johnson rank-envelope: `O(n²)` nodes, height `F_FJ(n)`; `F_FJ = S(n)` for `n ≤ 22`, but FJ is not optimal for all `n` (Manacher: first failure at `n = 47`), and the recursive frame/odd-case construction remains unaudited.

3. **The quotient node count is the single unknown.** Default single-policy quotient counts for `n ≤ 6` are `1,2,4,7,11,27`, growing rapidly; but an audited `n = 7` canonical quotient construction has only **19 nodes** at height `13 = S(7)` (checker: `ACCEPT: n=7, depth=13, nodes=19`). This shows policy choice can drastically compress, but no asymptotic bound is known either way. `[experiment]`

4. **No proof-system lower bound is known.** The winning-frontier barrier counts `2^{Θ(n log² n)}` nonisomorphic exact winning states, but it does not show that no polynomial-size coarsening/cover of them can retain exact minimax value `S(n)`. The entropy/forgetting conditions are necessary only. `[deduction/open]`

**Conclusion:** The question remains open. Progress requires one of: (a) an audited all-`n` exact framed construction, (b) a proof that every polynomial-size framed DAG exceeds `S(n)` for infinitely many `n`, or (c) a new compact canonical object for optimal play. Stop condition not met.
