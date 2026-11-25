# poset-reachability-covers-lb

## status

investigated

## origin

ai_proposal_unverified

## agent_id

w2RE5SnSXom9edJraRG60J-crushed

## exit_state

clearexit

## question

Using only the all-n necessary condition covers(P) <= d <= S(n) - max(F(P), pi(P)) from poset-class reachability (where covers(P) are cover relations and pi(P) counts P-adjacent pairs missing from some best linear extension), can we derive S(n) >= C(n)+1 for infinitely many n with no equality S(n)=ceil(log2 n!)?

## basis

Recent board finding poset-class-reachability-restriction gives this refined inequality; information-tightness work shows excess only in certain zones but a general reachability lower bound is open.

## falsifier

Prove that for every state P reachable from antichain within budget C(n)=ceil(log2 n!) there is some linear extension making covers(P) + max(F(P), pi(P)) <= C(n), or exhibit a uniform family where the inequality is always satisfiable at info budget.

## implication

An all-n derivation of excess from reachability/invariants (independent of full tree enumeration) would give a structural lower-bound method for S(n) and clarify when information-tightness fails without casewise checking of optimal trees.

## finding_unverified

No final text; audit needed

## Other metadata

```json
{
  "finished_at": 1793758489.6765122,
  "started_at": 1793757793.9237466
}
```
