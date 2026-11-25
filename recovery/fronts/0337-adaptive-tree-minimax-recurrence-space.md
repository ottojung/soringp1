# adaptive-tree-minimax-recurrence-space

## status

investigated

## origin

ai_proposal_unverified

## agent_id

3hwzaO2NFqEsNJcwVUE2fW-lestrade

## exit_state

clearexit

## question

Is the partial-order minimax recurrence computable in polynomial space in n (as a function of numeric n) without exponential time, by exploiting structure of the antichain root?

## basis

docs/problem.md partial-order minimax recurrence time 2^O(n^2); AGENTS.md upper-bound frontier.

## falsifier

A proof that recurrence evaluation for the fixed antichain family requires 2^Omega(n^2) time for all algorithms, or an algorithm running in poly(n) space and subexponential time.

## implication

Would either yield a faster exact evaluator or a barrier against recurrence-based methods for S(n).

## finding_unverified

arbitrary consistent strict partial order on the `n` keys (`F(P)`; see `docs/upper-bound.md`). The initial state is the empty order, but **the antichain property is destroyed by the first comparison**: every nontrivial successor has a nonempty comparability relation.
- The set of states reachable from the antichain root is essentially the family of all consistent partial orders on `n` labelled elements (every partial order extends to a total order, hence is reachable by some transcript). There is no known compression of this family to a polynomial-size parameter that preserves the minimax value `F`.
- Consequently the crude ternary-matrix count `3^{n(n-1)/2}` is not obviously improvable by root structure; the antichain start gives no "small-width" invariant (width becomes `n-1` after one chain, and can be large throughout).

### Space vs. time tradeoff (paper argument)

- Memoized recurrence: `2^{O(n²)}` time, `2^{O(n²)}` space (state table).
- Naive DFS without memoization: `O(n²)` space (depth ≤ number of incomparable pairs) but `3^{O(n²)}` time — worse, not better.
- To get `poly(n)` space *and* subexponential time one would need either (a) a recurrence whose state count is subexponential in `n` while remaining correct, or (b) a closed form for `F` on the antichain family. Neither is known; the budgeted transcript DFS only reaches `O(n log² n)` space at `2^{O(n log² n)}` time (`docs/problem.md`), still exponential.

### Relation to poset hardness (and the required caveat)

- General-poset predicates are hard: `#LE` is `#P`-complete (Brightwell–Winkler), and the Fibonacci-threshold predicate is PP-hard under Las Vegas reductions (board #301). But these concern *arbitrary* posets, not the fixed antichain family, and do **not** transfer to recurrence evaluation for `S(n)` without an encoding-preserving reduction (AGENTS.md model fidelity). I do not claim such a reduction here.
- Soundness vs. completeness: a threshold rule `e(P) ≤ T(b)` being sound (prunes only sortable states) is different from being complete/efficient. The board's width-two Fibonacci result is soundness on a restricted class; it does not give a poly-space evaluator for the antichain root.

### Obstruction to a `2^{Ω(n²)}` lower bound

- A matching lower bound for recurrence evaluation would have to show that no algorithm can avoid exploring an exponential fraction of the state DAG. The state DAG has `3^{Θ(n²)}` nodes, but many are unreachable or equivalent under relabelling; the exact reachable/equivalence count for the antichain family is not known to me, and no counting argument in the repository closes this gap.
- Hence I cannot assert `2^{Ω(n²)}` time for all algorithms, nor can I assert a poly-space subexponential algorithm. The recurrence's complexity on the antichain family remains open between `2^{Ω(n log n)}`-type lower bounds (threshold-pruning spine) and `2^{O(n²)}` upper.

### Honest limits

- No new theorem, counterexample, or repository change is warranted; this is an obstruction note, not a proof.
- The decisive missing ingredient is a state-compression or canonical-form result for partial orders reachable from the antichain that preserves `F` and has subexponential count. Absent that, neither the upper nor the lower target is reachable by recurrence-structure arguments alone.

**Next decisive obstacle:** find (or rule out) a canonical form for reachable partial orders under comparison transcripts with `poly(n)`-size description and `F`-invariant value.

## Other metadata

```json
{
  "finished_at": 1794101188.0873594,
  "started_at": 1794101153.5937734
}
```
