# antonina-U8RoAj0o8afQqWvcrZo94l-buffalo

Session: ses_e0c495571ffeB2sq7XWUgo068v
Workspace: /home/lubko/soring-fronts/minimal-first-violation-lift-alln
Created: 1795090197238; updated: 1795090787600

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 379 (msg_1f3bf9b5d00165k9jDwtrm3tcc)

Posted the finding to Antonina board #301. No repository/Lean/test changes were made; worktree remains clean.

**Mathematical finding (conditional).** For transitively closed posets, depth-balance \(B(P)\) fails iff every optimal comparison has easy child depth \(\le m(P)-3\). Ordinal sums preserve \(B\) in the following sense: \(A\oplus B\) satisfies \(B\) iff at least one summand satisfies \(B\) (verified exhaustively on 64 small representative pairs, plus additivity). Hence:

- If a \(B\)-failing poset \(Q\) existed, then \(Q\oplus Q\) (and all \(Q^{\oplus t}\)) would also fail, so a counterexample could never be a complete singleton in the class of all posets.
- But \(Q\oplus T\) is \(B\)-satisfying whenever \(T\) is \(B\)-satisfying (e.g. a Fibonacci-minimal/tight poset), so not every ordinal-sum lift propagates the violation; tight components can absorb it.

Therefore a single small counterexample would establish violations at multiples of \(|Q|\), but would not by itself decide the all-\(n\) depth-balance question; sporadic or all-large-\(n\) violations would still require construction of series-prime (Fibonacci-type) failing extensions.

**Honest limits.** No \(B\)-failing poset is known (none through \(n=10\); any counterexample has \(n\ge 11\), is series-prime and Fibonacci-nonminimal). The propagation statements are conditional on existence, and whether Fibonacci-type extensions preserve failure remains open. No \(S(n)\) value, SORT-BOUND-U decision, or complexity separation is claimed.
