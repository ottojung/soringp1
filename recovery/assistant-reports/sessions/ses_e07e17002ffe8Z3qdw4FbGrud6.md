# antonina-e9gQ6o8LDArcxskvxQBucq-flexible

Session: ses_e07e17002ffe8Z3qdw4FbGrud6
Workspace: /home/lubko/soring-fronts/minimax-multiplicity-per-extension-count-optfeasible-alln
Created: 1795164115215; updated: 1795164482968

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 370 (msg_1f8241ffb001TEt1TxM7g1UTqe)

## Mathematical finding

The front `minimax-multiplicity-per-extension-count-optfeasible-alln` is answered **NO** by a decisive but elementary range bound.

For any poset \(P\) on \(n\) labelled keys, \(F(P)\) is the minimum remaining worst-case number of comparisons, an integer. Every state that can appear on a height-\(S(n)\) optimal sorting tree satisfies

\[
0 \le F(P) \le S(n)-\operatorname{depth}(P) \le S(n),
\]

and by merge sort \(S(n)=O(n\log n)\). Therefore, for fixed \(n\), the set of possible values of \(F(P)\) has size at most \(S(n)+1=O(n\log n)\), **independently of \(e(P)\)**. Consequently, a single extension count can support at most \(O(n\log n)\) distinct minimax values — polynomially bounded, never superpolynomial.

So the literal claim (superpolynomially many distinct \(F\)-values per \(e\)-value) is impossible. The corresponding complexity implication is correspondingly weakened: distinct-\(F\)-value counting does not rule out an \(e\)-keyed evaluator with a polynomial-size value set per key.

### Honest limits

- This does **not** settle whether an \(e\)-keyed dynamic program is actually possible; it only removes the “distinct \(F\)-value multiplicity” obstacle.
- It does **not** deny the prior `superpoly-optimal-feasible-e-collisions` result: that construction still gives \(2^{\Omega(\sqrt{n/\log n})}\) states sharing one \(e\)-value, but they take only two (or, more generally, at most \(O(n\log n)\)) distinct \(F\)-values. The remaining meaningful question is state multiplicity per \((e,F)\) pair, not distinct \(F\)-values.
- No repository, Lean, test, or CI change was made; the result was posted to Antonina issue #301.
