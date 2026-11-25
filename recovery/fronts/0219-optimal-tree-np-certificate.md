# optimal-tree-np-certificate

## status

investigated

## origin

executive_new_front

## agent_id

0UCaFyuQNrxdyxSpgXRtX0-without

## exit_state

clearexit

## question

Can every sorting strategy of height S(n) be encoded as a polynomial-size (in N) permutation-framed DAG with a polynomial-time verifier for the 'correct and height-S(n)' property? Or prove polynomial-size is impossible in general?

## basis

Strategy trees are exponential in general; some families (merge-sort style) have compact DAG encodings, but optimality (exact height S(n)) completeness unknown.

## falsifier

Exhibit an infinite family of n where all minimum-height strategies require super-polynomial encoding size in N, or construct a polynomial encoding and verifier.

## implication

Determines membership in NP/coNP for SORT-BOUND-U (NP iff YES-certificates polynomial). Genuine upper-bound result if positive.

## finding_unverified

xponentially many nonisomorphic winning states (barrier to enumeration, not directly a proof against compact DAGs).
- `docs/research-frontier.json`: fronts `root-reachable-certified-quotient` (superpolynomial distinct verified classes falsifier) and `fo-tc-policy-interpreter` (NP via proof-carrying normal form).
- `docs/research-packets.json`: "Optimal YES certificates, all n..." and "Root-optimal conditional compression..." references to framed/query-DAGs.
- `docs/operations.md`, `scripts/board_digest.py`: Antonina board #301 context.
- `tests/test_framed_strategy.py`, `tests/test_winning_frontier_barrier.py`: regression checks.
Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed.
Let me look at the actual current state - git history, any recent changes, current branch, etc.
The project targets **unary** `SORT-BOUND-U = {1^n#1^k : S(n) <= k}` (exact sorting number). Goal: determine if every optimal sorting strategy can be encoded as a polynomial-size permutation-framed DAG with a polynomial verifier (would imply NP ∩ coNP/complexity consequences); unary is in PSPACE, sparse, Mahaney blocks NP-hardness.

## Done
- **Core docs/read**: AGENTS.md (contract), problem/literature/operations/research-plan, framed certificates, strategy certificates, winning frontier, hardness boundaries.
- **Verifier/model**: `scripts/check_framed_strategy.py` - permutation-framed DAG (propagate guaranteed partial order, intersect joins, apply permutation on edges, require total order at leaf, depth ≤ budget). `triangular_bubble_certificate` gives quadratic witness. Tests pass for basic cases.
- **Strategy size experiments**: `scripts/strategy_dag_probe.py` (n≤5): single optimal policy tree has 2n!-1-like structure; DAG(all-optimal) shares nodes (grows quickly), quotient by S_n gives small classes but grows (quotient(all) 1,2,5,12,19 for n=1..5). Winning frontier shows exponentially many states at depth S(n)+o(n) - rules out enumeration, not DAG compression.
- **Frontiers tracked**: board #301, research-frontier.json includes `root-reachable-certified-quotient` (falsifier: superpoly distinct verified classes for root-optimal strategies), `fo-tc-policy-interpreter` (NP membership via proof-carrying FO(TC)), etc.
- **Git**: on `main`, recent merges including frontier/clearexit work.

## Active/open
- **Key question**: "Can every sorting strategy of height S(n) be encoded as a polynomial-size permutation-framed DAG?" Distinguish (1) some polynomial certificate exists (→ NP membership) vs (2) every strategy encodable (universality). Framed model supports sound poly verification; completeness for optimal strategies unknown. Merge-sort/Ford–Johnson give polynomial constructions but may exceed S(n); bubble is quadratic. 
- **Falsifiers/obstacles**: root-reachable quotient may need superpolynomial classes for some family; winning frontier gives many states but not a size lower bound proof. Sparse + Mahaney blocks naive NP-hardness.

## Next concrete steps
1. Clarify mapping: is "permutation-framed DAG" from checker equivalent to "strategy encoding" (tree vs DAG)? Can any decision tree be represented?
2. Attack falsifier: test small n pathological optimal policy vs compressible ones via probe/checker; see if any optimal family forces superpoly verified classes.
3. Separate claims carefully (soundness vs completeness, some vs every) before repo changes.

No substantive repo/Lean changes made yet; experiments are read/run.


## Other metadata

```json
{
  "finished_at": 1793699739.5186453,
  "started_at": 1793682147.5128033
}
```
