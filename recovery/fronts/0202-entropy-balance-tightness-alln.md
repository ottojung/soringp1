# entropy-balance-tightness-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

pX6UNZfmeNqKXL2ai3sfvy-pigmented

## exit_state

clearexit

## question

Does the Kahn-Saks graph-entropy / balanced-comparison paradigm force S(n) >= log2(n!) + c*n / something, or can one construct an all-n family of comparison strategies beating entropy-balance predictions to approach log2(n!) closer than o(n) in a structured way?

## basis

Kahn-Saks/Kahn-Kim give algorithmic approximations; Sergeev gives asymptotic S(n)=log2(n!)+o(n); need to know if the gap is realizably shrinkable by comparison constraints.

## falsifier

Show that for all comparison strategies, the entropy deficit accumulates to >= delta(n) with delta(n)/n bounded below along some infinite subsequence, or construct an explicit all-n strategy achieving S(n) - log2(n!) = o(n / g(n)) for some function g(n)->infty contradicting current best o(n) forms.

## implication

Tight bounds on the entropy-excess would sharpen the search window for exact S(n) algorithms and clarify whether the sublinear gap from Sergeev is improvable or has structural barriers.

## finding_unverified

eed deficit forced. But Sergeev exhibits a strategy with excess $o(n)$, hence no linear lower bound $c n$ is forced for all strategies by these balance arguments. In fact the balance paradigm is the *source* of better upper bounds, not a lower-bound force. So the implication is backwards.

Also note: Kahn–Saks gives a *guaranteed* good comparison exists at each step for any poset state - this is exactly what allows building a balanced strategy (the "graph entropy" / "sorting by comparisons" algorithms use such balanced comparisons). So the paradigm is enabling, not forcing excess.

## Obstructions / things I could not do
- I did not find any theorem in the repo or common literature stating that entropy-balance forces $\Omega(n / \log^c n)$ excess for all sorting strategies. The force runs the other way.
- I did not find an explicit published obstruction to improving Sergeev's polylog factor beyond $1/5$; it appears to be a matter of algorithmic refinement of group-insertion/analysis rather than a known structural barrier from comparison constraints. That said, proving better bounds or proving a barrier would be substantial.
- The board #301 doesn't show this exact front being actively worked in the recent posts I scanned; other fronts dominate.
- I cannot construct a new strategy or prove a new theorem here - I need to report findings/obstructions.

## Honest answer
**Finding:** The Kahn–Saks/Kahn–Kim "balanced comparison / graph entropy" paradigm is **enabling, not forcing**. Kahn–Saks guarantees some balanced comparison exists per poset state (used to build $O(\log e(P))$ strategies); it does not imply that *every* correct sorting strategy has linear entropy deficit. The exact identity is $S - \log_2(n!) = E[k-D] + \sum q_v (1-h_2(p_v)) \ge$ average deficit. Sergeev (2020) constructs strategies with $S(n)-\log_2(n!) = O(n/(\log n)^{1/5}) = o(n)$, directly contradicting any claim that the paradigm forces excess $\Omega(n)$. 

**On the falsifier:** (1) No known result forces $\delta(n)/n$ bounded below along infinite subsequence for all strategies - evidence opposes it. (2) Achieving $o(n/g(n))$ better than current forms would mean improving Sergeev's polylog factor; I see no published structural obstruction from comparison constraints alone in the literature surveyed, but I also have no construction/improvement. This is an open algorithmic question, not obviously ruled out. 

**Complexity implications:** Tighter excess bounds affect search windows for exact $S(n)$ algorithms and certificate sizes, but don't directly touch unary PSPACE/P/NP separations (those are blocked by different barriers - sparsity/Mahaney, $P/poly$). The entropy identity is about the *tree* (comparison count), not about uniform computation time except through the search. 

**Distinction:** General poset results transfer to "sorting under partial information" but not to hardness of *evaluating $S(n)$* on the antichain; certificate **soundness** (entropy necessary conditions) is clear, **completeness/succinctness** (polynomial exact certificates) is open and not implied by constant-factor approximation algorithms. 

**Failed/obstructed approach:** Attempting to get a linear lower bound from "balance paradigm" is the wrong direction - it's constructive. No obvious obstruction found to sublinear improvement, but no improvement found either; this remains open algorithmically. No repo changes proposed (not a substantive new theorem/counterexample ready for integration).

## Other metadata

```json
{
  "finished_at": 1793648072.8012123,
  "started_at": 1793647382.7771308
}
```
