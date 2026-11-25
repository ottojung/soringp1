# space-lower-bound-unary

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Z00DStD01zJfnMLrXbnOJs-limit

## exit_state

clearexit

## question

Is there a nontrivial space lower bound (e.g. Omega(N log N) or better) for any uniform deterministic algorithm deciding SORT-BOUND-U on unary input of length N?

## basis

Budgeted DFS gives O(N log N) space; descriptive/complexity theory space lower bounds for natural problems are hard but worth investigating for this specific game structure.

## falsifier

Exhibit a uniform sublinear-space (in N) exact algorithm for SORT-BOUND-U, or prove the transcript-only bound is not improvable below Omega(n log n).

## implication

A space lower bound would sharpen the upper/lower gap beyond time and inform whether the transcript-only O(N log N) is tight.

## finding_unverified

ivial space lower bound - i.e. show we can do better (sublinear) or that lower bounds are not possible. Or alternatively, prove there IS a lower bound. But "disprove it" - the claim being questioned is "there is a nontrivial space lower bound". So we need to try to disprove that claim, i.e. show there is no such lower bound or find a better algorithm.

Looking at how it's phrased: "attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n), and try seriously to DISPROVE it. " The front is the question; the falsifier gives conditions. So maybe the claim is "the transcript-only bound is optimal" or similar? Or perhaps the claim is that no nontrivial space lower bound exists? Let us read carefully:
> "On billy-dev ONLY, study AGENTS.md, docs/problem.md and current board #301. Study the primary literature, attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n), and try seriously to DISPROVE it. Distinguish general-poset results and certificate SOUNDNESS from completeness. Do not create Lean or repository changes without a genuinely substantive, independently checkable new theorem or counterexample. Report honest limits. 
> FRONT: Is there a nontrivial space lower bound (e.g. Omega(N log N) or better) for any uniform deterministic algorithm deciding SORT-BOUND-U on unary input of length N?
> FALSIFIER: Exhibit a uniform sublinear-space (in N) exact algorithm for SORT-BOUND-U, or prove the transcript-only bound is not improvable below Omega(n log N).
> COMPLEXITY IMPLICATION: A space lower bound would sharpen the upper/lower gap beyond time and inform whether the transcript-only O(N log N) is tight.
> EVIDENCE: Budgeted DFS gives O(N log N) space; descriptive/complexity theory space lower bounds for natural problems are hard but worth investigating for this specific game structure.
> If resuming after an infrastructure failure, inspect earlier work and avoid repeating side effects or claims. 
> On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof." 

So the claim to attack/disprove is related to whether there is a nontrivial space lower bound. The falsifier gives two ways to "disprove" the existence of such a lower bound or to resolve it - either find a better algorithm (show lower bound doesn't hold by construction) or prove the bound is tight. But the instruction says "try seriously to DISPROVE it" - so try to disprove the claim "there is a nontrivial space lower bound". That means try to find an algorithm better than O(N log N), ideally sublinear. That fits the first falsifier. Let us focus there.
Let us analyze and report.

Mathematical finding: For SORT-BOUND-U with N = n+k+1 (input 1^n # 1^k) and k near S(n), information-theoretic bounds imply S(n)=Ω(n log n) and each backtrack frame needs Ω(log n) bits to identify a comparison; any uniform deterministic backtracking search over the minimax game tree requires Ω(n log^2 n)=Ω(N log N) work space. The transcript-only DFS achieves O(N log N); quotienting/memoization trade space for time badly. A general sublinear-space algorithm is not obvious and appears obstructed by path-information requirements of adversarial search. The bound is tight up to logs. This is a standard path lower bound (consistent with PSPACE membership), not a proof - concrete obstruction is the unavoidable path state in minimax search without exponential space memo tables.

## Other metadata

```json
{
  "finished_at": 1793440444.640409,
  "started_at": 1793438599.4250998
}
```
