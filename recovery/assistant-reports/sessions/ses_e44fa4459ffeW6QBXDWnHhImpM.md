# antonina-r6U7qG7cfQ0wA1AZ66VHgM-tenths

Session: ses_e44fa4459ffeW6QBXDWnHhImpM
Workspace: /home/lubko/soring-fronts/curator
Created: 1794139077603; updated: 1794139302127

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 232 (msg_1bb0915a30015OfLazFQELLpbO)

Wrote `/home/lubko/soring-fronts/curator/frontier-candidates.json` with three non-duplicate fronts. Validation against the full ledger:

- All ids match `[a-z][a-z0-9-]{5,62}`, all field minima met.
- No id or normalized-question collision with the 367 ledger entries.

Proposed fronts:

1. **`sos-lasserre-minimax-exactness`** — extends the newest board LP result (`s-polynomial-size-lp-exact-value`, `minimax-lp-integrality-gap-rate`) to the next convex-hierarchy level; the ledger has no SDP/SoS entry.
2. **`randomized-average-sorting-excess`** — targets the *unconstrained* average optimum `f(n)` (the board's `R_rnd=f`, `f<S`), explicitly distinguished from the height-constrained `A(n)` front; `f≤S` gives a direct transfer to the bounded-excess question.
3. **`determinant-representation-sortnumber`** — a distinct polynomial-time algebraic route to `S_unary∈FP`; no determinant/matrix/arithmetic-circuit/VP front exists in the ledger.

No Lean, repository commits, or board posts were made; only the curator output file was written.
