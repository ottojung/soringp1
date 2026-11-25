# dimension-two-fibonacci-threshold

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Q96aWuONDRikP9MGsVfffe-guardian

## exit_state

clearexit

## question

Does every finite poset of order dimension at most two satisfy e(P) >= F_{m(P)+2}, so that the Fibonacci extension threshold T(r)=F_{r+3}-1 holds on the whole two-dimensional class for every r?

## basis

Peczarski (Order 23, 2006) establishes GPC for width two, semiorders and posets of at most 11 elements; Gupta (arXiv:2607.23926v2, 2026) extends GPC through 14 elements; every width-two poset has dimension at most two, and the newest board note treats width two as the only closed Fibonacci class.

## falsifier

An explicit two-dimensional poset, presented as the intersection of two linear orders, with e(P) < F_{m(P)+2}, checked by exact linear-extension counting and exact minimax evaluation.

## implication

An affirmative result would extend the published width-two Fibonacci threshold to a class of unbounded width and add a new all-n GPC-satisfying class; a counterexample would place the first GPC failure outside width two and change which structural bounds can feed threshold pruning.

## finding_unverified

I'll start by inspecting the environment state to determine what work (if any) already happened.


Front is `running` with no recorded finding and a clean worktree — so the interrupted turn left no durable result. Let me check existing tooling before computing.


Now let me build an exact probe: enumerate all cores with small extension count, test order dimension ≤ 2 (via pairs of linear extensions), compute exact `m`, and check the Fibonacci inequality.


duplicate acknowledged, no external effects

## Other metadata

```json
{
  "finished_at": 1794116935.6803548,
  "started_at": 1794116769.0118532
}
```
