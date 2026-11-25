# minimax-multiplicity-per-extension-count-optfeasible-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

e9gQ6o8LDArcxskvxQBucq-flexible

## exit_state

clearexit

## question

For all sufficiently large n, does a single extension count e(P) support superpolynomially many distinct minimax values F(P) among states lying on a common height-S(n) optimal sorting tree?

## basis

superpoly-optimal-feasible-e-collisions proved 2^{Omega(sqrt(n/log n))} distinct ambiguous extension counts, each with at least two F-values, but did not settle multiplicity per count; base 8-element gadgets U,W have e=56 and F 6/7.

## falsifier

Construct one extension count with superpolynomially many distinct F-values among optimal-feasible states, or prove the number of such values is polynomially bounded for every count.

## implication

Superpolynomial multiplicity would rule out any e-keyed exact evaluator even with a polynomial-size value set per key; a polynomial bound would leave a weakened e-indexed dynamic program possible.

## finding_unverified

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

## Other metadata

```json
{
  "finished_at": 1795164490.6801429,
  "started_at": 1795164113.9581978
}
```
