# s-unary-fp-time-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

u0TLbqibzGg9LBtZM0yoMq-street

## exit_state

clearexit

## question

Can the unary function S_unary(1^n) be computed in deterministic time 2^(o(n log n)) uniformly in n, or is there an all-n superlinear-in-nlogn time obstruction for exact evaluation?

## basis

Current budgeted DFS gives 2^(O(n log^2 n)) time for function on 1^n; AGENTS.md states faster exact evaluators are in principle achievable but no all-n tight time barrier is established.

## falsifier

Give a uniform algorithm running in 2^(epsilon * n log n) time for all epsilon>0 and all large n with a correctness proof and resource accounting, or prove a time lower bound exceeding 2^(c n log n) for some c>0 from the poset/game model.

## implication

A subexponential-in-nlogn (in that exponent sense) exact evaluator would sharply improve on current 2^(O(n log^2 n)) bounds; an unconditional obstruction would constrain the path to SORT-BOUND-U in P without invoking PSPACE separation.

## finding_unverified

**Finding (mathematical, honest): no decisive refutation of either horn with currently known methods.**

### Status of the two horns
- **Algorithmic (improve exponent):** The budgeted DFS gives time `2^(O(n log^2 n))` on input `1^n` (branching factor `O(n^2)`, depth `O(n log n)=S(n)`, no memoization). The exponent has an extra `log n` factor from depth. Possible routes to `2^(o(n log n))` (subexponential in the exponent relative to `n log n`): add memoization over reachable posets with canonicalization, exploit symmetries, use stronger pruning (e.g. better `F(P)` lower bounds than the information bound), or find a better search strategy. None of these are present in the codebase/literature reviewed; worst-case asymptotic gains are not obvious (the state graph of labeled posets is large and relabeling symmetries are limited). I found no constructive algorithm achieving `2^(o(n log n))` with a complete resource/accounting proof.
- **Lower bound (obstruction):** A proof of `time >= 2^(c n log n)` for some `c>0` uniformly for all large `n` would mean `S_unary ∉ FP`, hence `SORT-BOUND-U ∉ P`, hence `P != PSPACE`. By AGENTS.md and `problem.md`: circuit lower bounds don't apply (tally language in `P/poly`), and unconditional super-polynomial lower bounds for this unary language are not a productive route with known techniques. The information-theoretic lower bound is only on `S(n)` itself (the height), not on the computation time of the minimax value. No combinatorial lower bound from the poset/game model exceeding `2^(c n log n)` is known.

### Concrete failed/blocked approaches
1. **Trivial information bound:** `S(n)=Ω(n log n)` is a height lower bound, not a time lower bound on computing the value. Cannot yield `2^(c n log n)` time without extra assumptions.
2. **State graph counting alone:** Total paths give `2^(O(n log^2 n))`; distinct posets are fewer but still exponential in `n log^2 n` in worst cases with no strong canonical collapse obvious. Counting doesn't by itself give a lower bound against all algorithms.
3. **Class-based obstruction:** Mahaney blocks many-one NP-hardness; PSPACE membership is proved. Any direct exponential lower bound is equivalent to a major class separation with no known method.

### Verdict
The claim is **open**. I cannot seriously disprove it by either horn with existing techniques. The most honest conclusion is that a subexponential-in-`n log n` algorithm is not ruled out in principle (and "faster exact evaluators are in principle achievable" per AGENTS.md), while a direct combinatorial exponential lower bound is not currently feasible and would carry PSPACE-separation consequences. No repository/Lean changes are warranted; no board post of a proof/counterexample is justified. The decisive obstacle remains: we lack both a better algorithm and a nontrivial lower-bound method for this exact minimax value computation.


## Other metadata

```json
{
  "finished_at": 1793711564.0101013,
  "started_at": 1793711058.5532537
}
```
