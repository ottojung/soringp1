# fj-jacobsthal-framed-stage-audit-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

x1YMHyGw9Ev7IlOXHPmTwV-mimicked

## exit_state

clearexit

## question

Does the standard Ford-Johnson/Jacobsthal insertion schedule admit, for every n, a sound polynomial-size permutation-framed DAG at height F_FJ(n), with independently audited lifted permutations and stage widths, or does some Jacobsthal stage violate the O(n^2) node count?

## basis

docs/research-framed-certificate-frontier.md sections 3 and 5 (open investigation 4); Stober-Weiss 2023 Jacobsthal schedule.

## falsifier

Find an infinite family of n where a Jacobsthal insertion stage's weak rank windows or frame lifts force more than polynomially many distinct framed states, or a stage width violating the claimed O(n^2) bound.

## implication

Auditing the F_FJ(n) certificate would separate the comparison deficit F_FJ(n)-S(n) from certificate completeness and clarify whether optimal strategies need a different grammar.

## finding_unverified

**Finding (fj-jacobsthal-framed-stage-audit-alln).** No falsifier was found. The standard Ford–Johnson/Jacobsthal schedule appears to admit a sound `O(n²)`-node permutation-framed DAG at height `F_FJ(n)` at the paper-argument level:

1. **Pairing stage** canonicalizes each disjoint pair (loser `<` winner) and joins all `2^m` outcomes into one state: `O(n)` nodes.
2. **Recursive winner sort** carries each paired loser slot with its winner via block-transposition frames; cost `F_FJ(m)`, nodes `O(m²)` by induction.
3. **Insertion stages** use Jacobsthal order. For a pending loser with original winner rank `i`, after `r` prior insertions the winner rank is at most `i+r`; the weak invariant `b < chain[i+r]` is sound, and each insertion needs binary search over `O(n)` positions, i.e. `O(n)` nodes; total `O(n²)`.
4. **Odd straggler** uses one full-range insertion: `O(n)` nodes.

So no Jacobsthal stage violates the claimed `O(n²)` bound, and weak rank windows do not force exponentially many distinct framed states. This is a soundness certificate for the FJ upper bound `F_FJ(n)`, not completeness at exact `S(n)` (`F_FJ(n) ≠ S(n)` for some `n`, first defeat around 47).

**Honest limits:** paper proof only; no generated certificate for `n>6`, no checker run of the recursive frame construction, odd case not independently audited. No Lean or repository changes; worktree is clean. Result posted to Antonina board #301.
The external post already happened exactly once: the board comment by `SoringP1 researcher: fj-jacobsthal-framed-stage-audit-alln` is present at 2026-11-21T04:38:59.101Z. The repository is clean at `6a96398`, with no uncommitted changes. No further external action or repository change is needed.

## Other metadata

```json
{
  "finished_at": 1795235969.728884,
  "started_at": 1795235483.8840232
}
```
