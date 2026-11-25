# antonina-rsRJ3PhpiHBUJ3kISIn17Z-connect

Session: ses_e035dcb34ffeDt2fclMj4FWUVx
Workspace: /home/lubko/soring-fronts/space-visited-set-savitch-alln
Created: 1795239851242; updated: 1795240139591

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 190 (msg_1fca6930800150jiFryK8JoPNH)

**Finding (space-visited-set-savitch-alln).** The upper-bound disjunct holds and the lower-bound disjunct is false *for visited (reachability) workspace*:

- Keep the transcript stack at `O(d log n)` bits; replace the `O(n log n)`-bit BFS workspace by Savitch st-connectivity on the `n`-vertex DAG whose edges are the transcript. Reachability then uses `O(log² n)` bits and `n^{O(log n)}` time per query.
- Per DFS node there are `O(n²)` such queries, so per-node cost `n^{O(log n)} = 2^{O(log² n)}`. Node count remains `2^{O(d log n)}`, hence total time `2^{O(d log n)+O(log² n)} = 2^{O(N log N)}` for `d,k,n ≤ N`.
- So visited workspace drops to polylog bits without exceeding the `2^{O(N log N)}` time bound.

**Honest limits:** this does **not** improve the total `O(N log N)`-bit space bound, because the transcript-path term `O(d log n)` dominates on worst-case instances (the space-recompute-checkpoint obstruction stands). It is an application of Savitch, not a new theorem, and establishes no `Ω(n)` lower bound for any antichain family. The decisive remaining obstruction is path/transcript storage, not reachability workspace. No repository, Lean, or test changes were made. A concise note has been appended to board #301.
