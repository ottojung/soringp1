# winning-frontier-compression-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

7j97DNuokFsfNdsWDxffp1-secession

## exit_state

clearexit

## question

Does the 2^(Theta(n log^2 n)) size of the winning frontier force any exact memoized minimax evaluator to use Omega(2^(c n log^2 n)) states for some c>0, or can exact compression below that exponent be achieved?

## basis

Known winning-frontier barrier shows enumeration is hard; state compression question remains open for the exact minimax recurrence.

## falsifier

Construct an exact compression scheme achieving 2^(o(n log^2 n)) states on the relevant families, or prove a state-count lower bound matching the frontier barrier for all exact algorithms.

## implication

A state-count lower bound would give a time/space barrier for memoized DP approaches; breaking it would improve known exact evaluation bounds.

## finding_unverified

 codebase state.

Let us study this systematically.

Let us look up more details.


**Finding (mathematical, deduction):** The budget-reachable state space for the threshold game (posets P with remaining budget feasible to sort within d=S(n)) has size Θ(2^(Θ(n log^2 n))). The rectangular construction gives Ω(2^((1/4-o(1))n(log n)^2)) nonisomorphic *winning* states in that set at depth S(n)-B (and at exact S(n) by Sergeev’s o(n) surplus), so the set itself is tight up to the exponent’s lower-order structure. A standard “exact memoized minimax evaluator” over the (P,r) state graph (the natural recurrence for can_sort/can_finish) caches results per distinct state it visits; to be correct on all cases it must be able to distinguish states whose minimax values differ under adversarial choices. The winning frontier shows an exponentially large family of states that are all winning at the same depth but arise from different adjacent-layer edge sets and are pairwise not identifiable by the simple information bound alone (and are nonisomorphic). For the exact minimax recurrence, there is no known sound state compression below that exponent that preserves exactness for all n without losing the ability to compute correct min/max over successors; the barrier explicitly excludes “any purported uniform 2^(O(n log n)) algorithm whose method necessarily outputs all reachable winning partial orders at the information budget” (research-winning-frontier-barrier.md). Quotienting by S_n gives a large factor reduction but yields A000112 still 2^(Θ(n^2)) in the full poset class (research-state-compression.md) — irrelevant to the budget-restricted exponent; stronger general invariants fail exactness (e.g. linear-extension count). 

**Concrete failed approach / obstruction:** Attempts to find a coarser invariant preserved by the minimax recurrence fail on small counterexamples (F differs while L(P) same). Symmetry/orbit pruning removes moves but gives Θ(n^2) candidate pairs on asymmetric families (research-time-exponent.md). The budgeted DFS achieves 2^(O(n log^2 n)) time with polynomial space by *not* memoizing (recomputing) rather than by compressing stored states below that count — a trade-off showing the state count itself is the object. There is currently no published construction achieving 2^(o(n log^2 n)) distinct states for an exact memoized (caching) evaluator over all budget-reachable states, and the frontier provides a natural obstruction: if the evaluator must retain distinct states corresponding to that incompressible winning family to answer correctly, it needs Ω(2^(c n log^2 n)) states. The question of whether some non-graph-enumeration method (algebraic recurrences, parametric DAG certificates) can avoid storing states entirely is *not excluded* by the barrier.

**Honest limits:** I cannot produce a formal proof that *every* exact memoized minimax evaluator (under all possible representations/canonicalizations consistent with the recurrence) is forced to use ≥ 2^(c n log^2 n) states for some c>0 and infinitely many n; the barrier is a lower bound on *enumerating all winning states*, not a general information-theoretic lower bound on arbitrary compressed encodings of the state function. Conversely I cannot construct an explicit 2^(o(n log^2 n))-state exact compression. The frontier is tight as a counting obstruction for enumeration-based memoization, but “exact compression below that exponent” remains open in general. No repository changes made.


## Other metadata

```json
{
  "finished_at": 1793535709.834629,
  "started_at": 1793534209.5401032
}
```
