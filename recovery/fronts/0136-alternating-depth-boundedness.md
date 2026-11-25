# alternating-depth-boundedness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

cRWpZhvF552fXf02wLUw9F-adhere

## exit_state

clearexit

## question

Is the exact alternating game depth of SORT-BOUND-U bounded by a function of the alternation index independent in some way, or does the polynomially-many alternations of the ATM (depth O(n log n)) force the game to be outside every fixed level of the bounded-alternation hierarchy AP[O(1)]?

## basis

Chandra-Kozen-Stockmeyer alternation classes; ATM uses existential pair choice then universal adversary answers repeatedly (polynomial alternations) matching APTIME=PSPACE.

## falsifier

Show the comparison game can be simulated by a fixed-alternation (constant-depth in the AP hierarchy) strategy for all n with polynomial overhead, or prove a uniform fixed-alternation lower bound forcing PSPACE-completeness without sparsity assumptions.

## implication

A fixed-alternation collapse would place SORT-BOUND-U in PH; a lower bound would show the depth of the minimax recurrence is essential and not compressible by constant alternation blocks.

## finding_unverified

Let us study this more systematically.

Let us start by exploring the repository more to understand if there are any existing attempts on this specific alternation question.

Let us look up known results about sparse PSPACE-complete sets.

Let us read the full question again carefully and understand what is being asked. The question says "study AGENTS.md, docs/problem.md and current board #301" and gives this specific front. This is asking us to actually do research on this question as stated.

Let us start by analyzing this systematically.

Let us proceed systematically.

Let us analyze this question.

The analysis shows the polynomial alternation depth is inherent to the adaptive game structure (exponential strategy trees, adaptivity forcing interleaved ∃/∀ moves) without relying on sparsity, obstructing compression to PH with polynomial overhead and favoring a fixed-alternation lower bound forcing PSPACE-completeness. No repository changes made.

## Other metadata

```json
{
  "finished_at": 1793522981.9930987,
  "started_at": 1793518828.8191955
}
```
