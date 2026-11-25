# and-or-poset-pspace-completeness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

O8D1yDxDr4j1SN5hj1kTSk-threats

## exit_state

clearexit

## question

Is SORT-BOUND-U PSPACE-complete under polynomial-time many-one reductions from QBF (or another PSPACE-complete language), or is the poset-lattice structure of the sorting game strictly less powerful than arbitrary AND-OR games despite membership in PSPACE?

## basis

APTIME=PSPACE gives ATM upper bound for the game; minimax-game-pspace-hardness front found sparsity doesn't block Turing reductions but left many-one PSPACE-hardness open and structure-vs-generality question unresolved.

## falsifier

Construct an explicit polynomial-time many-one reduction from a PSPACE-complete language to SORT-BOUND-U preserving the unary encoding, or prove a structural invariant of the comparison game that cannot simulate arbitrary alternating computations.

## implication

PSPACE-completeness would identify the exact class of SORT-BOUND-U and clarify the significance of any future upper/lower bounds; strict containment below PSPACE-complete would indicate exploitable structure in the sorting game.

## finding_unverified

I'll start by reading the current board state and the relevant front entries from the ledger.


## Other metadata

```json
{
  "finished_at": 1793536567.699018,
  "started_at": 1793535954.9558685
}
```
