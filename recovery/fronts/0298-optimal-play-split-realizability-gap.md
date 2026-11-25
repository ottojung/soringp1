# optimal-play-split-realizability-gap

## status

investigated

## origin

ai_proposal_unverified

## agent_id

9Dd6Sow8T9lG8LJxkt3QrS-vaccines

## exit_state

clearexit

## question

For all sufficiently large n, is there an all-n family of comparison-split probability profiles that are information-theoretically feasible by Kraft but not realizable by any single comparison in the partial order of any state reachable on some S(n)-optimal minimax path, creating an unavoidable search-time overhead beyond the information bound?

## basis

Comparison-split Kraft tightness front rejected naive Kraft slack; focus shifts to split-realizability/geometry under optimal-play constraints and information admissibility noted in Kleitman-reachability work.

## falsifier

Prove for all large n that every Kraft-feasible split profile consistent with height budget on an optimal path is realizable by some legal pairwise comparison from some state reachable on some S(n)-optimal strategy.

## implication

A universal realizability gap would rule out certain "split-entropy" algorithms for exact S(n) evaluation without positing a general circuit lower bound and without conflating arbitrary posets with optimal-play states.

## finding_unverified

e information-theoretically feasible by Kraft but not realizable by any single comparison in the partial order of any state reachable on some S(n)-optimal minimax path, creating an unavoidable search-time overhead beyond the information bound"

So on an S(n)-optimal path, the remaining budget equals S(n) - depth. The state is "information-theoretically feasible" in the sense that L0(P) <= remaining budget? Or maybe the state is on a path that achieves the global information bound? Because S(n) might equal ceil(log2 n!) for some n (tight) or larger. Also "search-time overhead beyond the information bound" - the information bound is usually C(n)=ceil(log2 n!). So if you have overhead beyond the information bound, that means S(n) > C(n). And states on such optimal paths would need to account for that overhead.

Alternatively, think recursively: let r be the remaining budget on an optimal path (r = F(P)), so we need to sort within r more comparisons. The information-theoretic feasibility is r >= L0(P). A "split profile" is (e1/e, e2/e) for some comparison giving children with e1,e2 extensions. Kraft/information feasibility means we can still satisfy the bound if we split well - e.g. both e1,e2 <= e/2 => both need <= r-1 more if r is large enough. But "not realizable by any single comparison" means no actual comparison gives a split where both children are feasible under the remaining budget.

But combined with "on some S(n)-optimal minimax path" - so the strategy is optimal (achieves S(n)), so every state P on it must have F(P) = S(n) - depth(P). The split must be feasible given this optimal budget.

This is similar to saying there are no "good" moves (satisfying information bound) from states on optimal paths of algorithms that achieve beyond-information-bound? Or it could be saying the opposite of what the one-ply obstruction did.

Alternatively, look up the EVIDENCE: "Comparison-split Kraft tightness front rejected naive Kraft slack; focus shifts to split-realizability/geometry under optimal-play constraints and information admissibility noted in Kleitman-reachability work." 

Also from research-packets: "Known 2^{Omega(n log^2 n)} height-two family is excluded even by information budget on optimal paths" - so some families are excluded by information budget constraints on optimal paths. That means on optimal paths, you have tighter constraints than just being "information admissible" in general.

And the front is asking: even if a split is Kraft-feasible given the height budget on an optimal path, is it realizable by some comparison from states reachable on optimal paths? The falsifier says "prove for all large n that every Kraft-feasible split profile consistent with height budget on an optimal path is realizable..." So the falsifier claims realizability holds for all large n on optimal paths. Disproving the front means proving the falsifier. So try to prove that on S(n)-optimal paths, there are no split-realizability obstructions - you can always make progress.
Let us look up the full picture again and report properly.

Let us write up the result.

The falsifier is proved generally by L1(P) <= F(P): on any S(n)-optimal path, F(P)=remaining budget r implies some comparison gives max(L0 of children) <= r-1 (Kraft-admissible split). The L1>L0 obstruction can only occur when r > L0(P), not as a realizability obstruction on optimal paths. Experimental check on optimal paths for n<=6 confirms no obstruction. No repository/Lean changes made.

## Other metadata

```json
{
  "finished_at": 1793850193.001825,
  "started_at": 1793846529.8742828
}
```
