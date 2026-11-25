# greedy-state-multiplicity-per-ev-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

x61sphTi1MxFR6T9SNjRsY-hearers

## exit_state

clearexit

## question

For all sufficiently large n, does the greedy ball B_{G(n)}(n) contain superpolynomially many states sharing both the same linear-extension count e(P) and the same greedy max-extension value V(P)?

## basis

The distinct-V-values-per-e front is running or unresolved; sparse-exception, (e,width), and (e,h) refinements are refuted; state multiplicity per (e,V) pair has not been directly tested.

## falsifier

Find infinitely many n with one (e,V) pair realized by superpolynomially many greedy-ball states, or prove every such pair has only polynomially many states.

## implication

A superpolynomial family would rule out exact greedy evaluation by a table keyed by (e,V) with polynomial state sets; a polynomial bound would support compact e+V indexing after the distinct-V barrier.

## finding_unverified

Posted the final partial report to Antonina issue #301 as the single report for this front, and stopped as instructed.

Summary: strongest partial result is a labelled-state multiplicity observation: every reachable state’s full relabelling orbit lies in the same greedy ball and shares `(e,V)`, giving superpolynomially many labelled states for $(e,V)=(1,0)$ via total orders and, more substantively, via nonterminal $C_{\lfloor n/2\rfloor}\sqcup A_{\lceil n/2\rceil}$ states. Explicitly labelled as paper-level, not theorem completion; unlabelled-quotient interpretation and tabulation soundness left as honest limits. No repository/Lean/CI changes.

## Other metadata

```json
{
  "finished_at": 1795167223.5557353,
  "started_at": 1795166017.8769987
}
```
