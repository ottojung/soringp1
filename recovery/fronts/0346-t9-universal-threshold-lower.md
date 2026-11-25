# t9-universal-threshold-lower

## status

investigated

## origin

ai_proposal_unverified

## agent_id

bWE4JEnoXwa6RdSq0zccBX-gradual

## exit_state

clearexit

## question

Is every finite poset with at most 143 linear extensions sortable using at most eight adaptive comparisons, that is, does the uniform tightness threshold satisfy T(9) >= 143?

## basis

Newest board #301 states that T(9)=143 is predicted but not established and that the audited core census reaches e=88; docs/research-obstruction-next.md records T(r) only through r=8 and leaves the all-r Fibonacci identity open.

## falsifier

An explicit finite poset with e(P) <= 143 and m(P) >= 9, checked by exact minimax evaluation or by a sound lower-bound certificate for the remaining comparisons.

## implication

Establishing T(9) >= 143 would extend the all-n threshold staircase from the recorded T(8)=88 to the next Fibonacci level and enlarge the sound pruning base for exact unary threshold evaluation; a counterexample would refute the global F_{r+3}-1 prediction at r=9.

## finding_unverified

duplicate acknowledged, no external effects

## Other metadata

```json
{
  "finished_at": 1794116935.5691092,
  "started_at": 1794116768.3129106
}
```
