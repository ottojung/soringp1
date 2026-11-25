# and-or-tree-evaluation-class

## status

investigated

## origin

ai_proposal_unverified

## agent_id

223Drx97BJAci1wXVTPY12-berlin

## exit_state

clearexit

## question

Is the decision problem SORT-BOUND-U complete for some natural subclass of PSPACE (e.g. AC^0 reductions to AND-OR tree evaluation on poset games) or does the fixed antichain family place it strictly below the complexity of evaluating arbitrary AND-OR trees?

## basis

The minimax game is exactly an AND-OR tree on comparison outcomes; alternation fronts investigated but no front maps SORT-BOUND-U to AND-OR evaluation complexity classes.

## falsifier

Give an all-n AC^0 (or logspace) reduction from some PSPACE-complete AND-OR tree evaluation instance to SORT-BOUND-U, or prove SORT-BOUND-U has a structural property (e.g. bounded alternation in some normalized form) incompatible with completeness for general AND-OR trees.

## implication

A completeness result would classify S(n) evaluation relative to standard game-tree complexity; strict containment would explain why general AND-OR bounds don't apply and may suggest better algorithms.

## finding_unverified

Let us start by exploring the actual current state of this specific front if it exists as a working copy somewhere?

Let us look at the full board activity and also understand the game/alternation structure better.

Let us analyze this systematically.

Let us start by understanding the full picture of what's known.

Let us think carefully about the reduction classes.

Let us analyze the structure.

The analysis is complete. I need to report honestly as instructed.

The analysis above addresses both branches of the falsifier. Neither is satisfied by existing results - sparsity/collapse arguments obstruct reductions, bounded alternation remains unproven. No repo/Lean changes made; no new theorem/counterexample. This is the honest report.


## Other metadata

```json
{
  "finished_at": 1793419705.636759,
  "started_at": 1793414023.8094454
}
```
