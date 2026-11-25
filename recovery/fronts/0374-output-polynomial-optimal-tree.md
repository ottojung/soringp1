# output-polynomial-optimal-tree

## status

investigated

## origin

ai_proposal_unverified

## agent_id

nJVAutU5vpht2MTyRi1ajp-neighbors

## exit_state

clearexit

## question

Is there a constant c and a uniform algorithm that, on unary input 1^n, outputs a correct comparison tree of height exactly S(n) in time O((n!)^c), i.e. time polynomial in the number of nodes of the tree, for every n?

## basis

docs/problem.md records the 2^{O(n log^2 n)} budgeted-DFS evaluator; an optimal tree has 2*n!-1 nodes, so output-polynomial time is 2^{O(n log n)}, and no ledger front isolates output-sensitive tree construction from value evaluation.

## falsifier

Construct such an output-polynomial constructor with a verified height-S(n) proof, or prove that for an infinite family every correct height-S(n) tree requires super-polynomial-in-n! construction time under a stated uniform model.

## implication

Success would improve the exact evaluator to 2^{O(n log n)} time and yield a constructive optimal-tree certificate, while failure would separate evaluating the value S(n) from constructing an optimal witness.

## finding_unverified

l tree — cannot be proved without at least proving `P ≠ PSPACE`. This is stronger than “separating value evaluation from witness construction.”

A more targeted sufficient condition is also visible: `COMPL` contains generalized poset sorting `GEN-SORT` as the single-hole case. Hence `GEN-SORT ∈ P ⇒ COMPL ∈ P ⇒` the front. The natural construction route therefore needs a polynomial-time exact generalized-sorting decider, not merely a faster evaluator of unary `S(n)`.

## Concrete upper bound and failed approach

The known top-down construction uses the budgeted DFS as a `CanSort` oracle:

- output tree size: `2·n!−1` nodes, hence `Ω(n! log n)` output bits;
- known construction time: `O(n²·n!·2^{O(n log² n)}) = 2^{O(n log² n)} = (n!)^{O(log n)}`;
- the exposed gap is a factor `log n` in the exponent.

I verified the constructor for `n ≤ 5` (heights `1,3,5,7`, all permutations correct). An `n=6` run exceeded a 3-minute temporary budget, consistent with the exponential oracle cost. The only unconditional lower bound found is `c > 1`, forced by output length.

The failed route is therefore precise: **top-down completion with the existing exact `F` oracle is not output-polynomial**, because each residual completion query is a generalized-poset problem costing `2^{O(n log² n)}`.

## Soundness versus completeness

- **Soundness:** given an explicit tree, correctness and height are checkable in `poly(output)`.
- **Value evaluation:** the budgeted DFS decides `S(n) ≤ k` in `2^{O(n log² n)}`.
- **Completeness/construction:** neither gives an output-polynomial *search* algorithm. The missing object is a completion oracle for arbitrary residual prefixes, i.e. generalized sorting.

General-poset hardness results (Hyafil–Rivest; Laber–Nogueira) concern arbitrary subset tests and do not transfer to pairwise comparison trees. Conversely, they do not supply a constructor.

## Honest limits

- I did **not** construct an output-polynomial algorithm.
- I did **not** prove an unconditional impossibility.
- The barrier is one-sided: `P=PSPACE` is sufficient but not necessary, and the original empty-prefix front could in principle be true even if `COMPL ∉ P`.
- A failure of the front would not by itself separate value from construction in the usual class sense: the known value upper bound is `2^{O(n log² n)}`, above the `2^{ω(n log n)}` threshold of front failure.
- No claim about `SORT-BOUND-U ∈ P` or `∈ NP` is made.

**Effects:** one board post, no repository or Lean changes, clean worktree.
Recovery inspection complete. I did **not** repeat the research prompt or any external action.

**Effects that actually happened**
- Git: worktree is clean on `billy-dev` at `6a96398`; no commits, repo edits, or Lean changes.
- Board #301: exactly **one** matching post from this front, at `2026-11-08T13:36:13Z` (“uniform negative lower bound …”). No duplicate post exists.
- Temporary artifacts only: `/tmp/opencode/board_output_poly.txt` and `/tmp/opencode/build_tree_check.py`.
- Durable ledger: the `output-polynomial-optimal-tree` entry is still `status: "running"` with the live agent ID. That is normal keeper-managed bookkeeping; I did not manually edit it.

**Unfinished work**
None. The mathematical finding, upper bound, failed approach, barrier theorem, and honest limits are already recorded in the single board post.

**Uncertainty**
No external effect is ambiguous. The only pending state is the ledger’s `running` status, which the keeper transitions after agent exit.

## Other metadata

```json
{
  "finished_at": 1794145097.8186417,
  "started_at": 1794144375.5928938
}
```
