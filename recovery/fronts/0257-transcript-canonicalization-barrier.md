# transcript-canonicalization-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

oTkXr6LuKffKByTyl7zWyC-biting

## exit_state

clearexit

## question

For all sufficiently large n, is there an all-n uniform lower bound showing that any deterministic TM deciding SORT-BOUND-U on input 1^n#1^k with k<=S(n) must enumerate or distinguish >= 2^((1/4-o(1)) n (log n)^2) non-isomorphic reachable poset classes despite budgeted pruning, forcing time >= 2^((1/4-o(1)) n (log n)^2)/poly(n)?

## basis

Winning frontier barrier (docs/research-winning-frontier-barrier.md) gives >=2^((1/4-o(1))n log^2 n) non-isomorphic winning states; budgeted DFS reaches 2^(O(n log^2 n)) states total but frontier count is the barrier; AGENTS states barriers to whole families of methods are in scope.

## falsifier

Construct a uniform algorithm for SORT-BOUND-U that runs in time 2^(o(n (log n)^2)) on all unary inputs (or shows the winning frontier states are compressible by a canonical form testable in subexponential time per class) refuting the enumeration lower bound for uniform solvers.

## implication

A proved all-n enumeration barrier for uniform algorithms would separate the selective/minimax search from naive frontier traversal and give a concrete exponential time lower bound in numeric n for the unary decision problem without relying on P!=PSPACE circuit methods.

## finding_unverified

I'll read the full key documents first.

Let us start by exploring the full board #301 context if possible and related code/scripts.

Let us first look up the full board #301 context and related frontier items more.

Let us report the finding.

Done. The key point is distinguishing a family/barrier (excludes enumerating all classes) from a general TM lower bound for all uniform algorithms; the cited theorem does not support the stronger claim as stated. No repo/Lean changes made.

## Other metadata

```json
{
  "finished_at": 1793758331.99847,
  "started_at": 1793757793.5427902
}
```
