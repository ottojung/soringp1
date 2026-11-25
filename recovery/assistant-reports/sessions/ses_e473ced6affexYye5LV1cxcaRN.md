# antonina-3hwzaO2NFqEsNJcwVUE2fW-lestrade

Session: ses_e473ced6affexYye5LV1cxcaRN
Workspace: /home/lubko/soring-fronts/adaptive-tree-minimax-recurrence-space
Created: 1794101154645; updated: 1794101177772

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 59 (msg_1b8c33506001V3bqmm4Dxoosxm)

## Mathematical finding

**Claim tested.** The partial-order minimax recurrence for `S(n)` (root = antichain of `n` labelled keys) is computable in `poly(n)` space and subexponential time by exploiting the antichain root.

**Verdict: not established; the proposed bridge fails.**

### Why the antichain root does not reduce the state family

- The recurrence state after a transcript is an arbitrary consistent strict partial order on the `n` keys (`F(P)`; see `docs/upper-bound.md`). The initial state is the empty order, but **the antichain property is destroyed by the first comparison**: every nontrivial successor has a nonempty comparability relation.
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
