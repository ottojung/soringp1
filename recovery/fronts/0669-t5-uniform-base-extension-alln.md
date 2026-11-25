# t5-uniform-base-extension-alln

## status

blocked

## origin

executive_initiated

## agent_id

KVSVClll9IJZSqtdWGHWz8-labyrinth

## exit_state

failed

## question

Is the uniform base T(5) = 29, i.e. does every poset P on any number of elements with e(P) <= 29 have m(P) <= 5, with the base attained by some poset with e(P) >= 30? Enumerate exhaustively on n = 7 (and propose n = 8) for any poset with 30 <= e(P) <= 32 and m(P) >= 6, or state T(5)=29 as the deliverable if none exist.

## basis

docs/research-obstruction-next.md sections 2-4: T-table certified up to r = 6/n = 6 (T(6)=56, first failing e = 57) with the pattern T(4)=12, T(5)=29.

## falsifier

Exhibit a poset P with e(P) >= 30 and m(P) >= 6, or prove every poset with e(P) <= 29 has m(P) <= 5 (extending the n <= 6 certificate of T(5) = 29). Provide the poset or the proof with an independent solver cross-check.

## implication

Sharp uniform bases at budgets 4 and 5 strengthen the exact S(n) backward-search pruning table and give the local analysis of where non-tightness can first arise (local solve of budgeted pruning).

## finding_unverified

No final text; audit needed

## Other metadata

```json
{
  "finished_at": 1795311270.407593,
  "retry_after": 0,
  "started_at": 1795309984.1571765
}
```
