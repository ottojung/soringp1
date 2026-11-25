# minimal-first-violation-lift-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

U8RoAj0o8afQqWvcrZo94l-buffalo

## exit_state

clearexit

## question

If a depth-balance violation first occurs at some n, does that minimal violating state necessarily lift via ordinal sums or Fibonacci-type extensions to an infinite family of violations, or can a single counterexample be isolated and non-propagating?

## basis

Threshold-sharp front: any B-failing poset is series-prime and Fibonacci-nonminimal; ordinal sums preserve B; n<=10 enumeration found no violations.

## falsifier

An explicit first violating state whose ordinal-sum or Fibonacci lift remains B-satisfying, or proof that no first violation can be non-propagating.

## implication

Determines whether resolving d(12) or one small counterexample decides the all-n depth-balance question, or whether violations can be sporadic and harder to classify.

## finding_unverified

Posted the finding to Antonina board #301. No repository/Lean/test changes were made; worktree remains clean.

**Mathematical finding (conditional).** For transitively closed posets, depth-balance \(B(P)\) fails iff every optimal comparison has easy child depth \(\le m(P)-3\). Ordinal sums preserve \(B\) in the following sense: \(A\oplus B\) satisfies \(B\) iff at least one summand satisfies \(B\) (verified exhaustively on 64 small representative pairs, plus additivity). Hence:

- If a \(B\)-failing poset \(Q\) existed, then \(Q\oplus Q\) (and all \(Q^{\oplus t}\)) would also fail, so a counterexample could never be a complete singleton in the class of all posets.
- But \(Q\oplus T\) is \(B\)-satisfying whenever \(T\) is \(B\)-satisfying (e.g. a Fibonacci-minimal/tight poset), so not every ordinal-sum lift propagates the violation; tight components can absorb it.

Therefore a single small counterexample would establish violations at multiples of \(|Q|\), but would not by itself decide the all-\(n\) depth-balance question; sporadic or all-large-\(n\) violations would still require construction of series-prime (Fibonacci-type) failing extensions.

**Honest limits.** No \(B\)-failing poset is known (none through \(n=10\); any counterexample has \(n\ge 11\), is series-prime and Fibonacci-nonminimal). The propagation statements are conditional on existence, and whether Fibonacci-type extensions preserve failure remains open. No \(S(n)\) value, SORT-BOUND-U decision, or complexity separation is claimed.

## Other metadata

```json
{
  "finished_at": 1795090798.789865,
  "started_at": 1795090196.8022354
}
```
