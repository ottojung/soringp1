# budgeted-dfs-algebraic-decision-lower-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

3xb9SLTFeyfT5CCbxCJQ0s-hurry

## exit_state

clearexit

## question

In algebraic decision/comparison models that capture transcript-only budgeted DFS over extension-count and reachability predicates, must every exact SORT-BOUND-U decider perform 2^{Omega(n)} predicate evaluations on infinitely many unary inputs, even when allowed polynomial workspace?

## basis

docs/research-budgeted-dfs.md gives 2^{O(N log(N+2))} time/O(N log(N+2)) space; minimax-andor-eval-implicit found no subexponential description but no model lower bound. Prior fronts did not formulate an all-n algebraic-decision predicate lower bound tied to exact transcript-only evaluation.

## falsifier

Give a uniform exact algorithm in that model family with 2^{o(n)} predicate evaluations for all sufficiently large n, or prove the model fails to capture a known exact method such as budgeted DFS/pruning variants relevant to all-n S(n).

## implication

A model-specific exponential predicate lower bound would sharpen understanding of why current exact evaluators are costly without claiming a separation from P/PSPACE; a subexponential exact simulation would directly improve the algorithmic frontier.

## finding_unverified

y DFS” subfamily (no `ExtGt`)
- Captured exactly: `scripts/transcript_dfs.py` uses `Reach/Total` on `σ` and explores the minimax AND-OR game `CanSort` (`docs/research-budgeted-dfs.md` §2–4). `ExtGt`-style counting is *not* a reachability predicate; capped enumeration costs `2^{O(d)}·poly(n)` time (not unit) — so treating `ExtGt` as unit-cost is an oracle idealization (soundness of the answer preserved, cost model changes). Orbit/automorphism pruning (`orbits`) is **not** captured by `{ExtGt,Reach,Total}`. [deduction/definition]
- **Failed disproof (no `2^{o(n)}` algorithm found):** I found no uniform exact `2^{o(n)}`-predicate method. Generic AND-OR/memo/symmetry-quotient avenues were examined in prior ledger fronts (`minimax-andor-eval-implicit`: no subexponential description; winning-frontier gives `>=2^{(1/4-o(1))n(log n)^2}` nonisomorphic winning states, an enumeration barrier not a predicate lower bound). Plain DFS is `2^{O(n log² n)}` predicates/nodes; all known exact relevant methods remain exponential in `n`-polylog factors. [deduction; no new algorithm]
- **No proof of `2^{Ω(n)}` (honest limit):** `2^{Ω(n)}` is far weaker than known `2^{Θ(n log² n)}` DFS behavior, yet proving it *for every* algorithm in the family fails: (a) Ben-Or algebraic-decision-tree component bounds are for real polynomial tests, not directly these discrete poset predicates; (b) the instance is computed from `(n,k)` (not an adversarial hidden input), so standard query-complexity lower bounds don’t transfer; (c) AND-OR refutation/certificate sizes depend on strategy but give no uniform `2^{Ω(n)}` predicate lower bound across all possible interleavings/shortcut predicate uses. For hard NO gap instances a DFS refutation explores many states, but a *model lower bound* is not established. [obstruction]

## Model-capture verdict
- Captures: transcript-only budgeted DFS (Reach/Total) and extension-count/HI-base *decision* pruning when those are primitive predicates. **Fails to capture as unit predicates / as stated cost:** the actual `e_exceeds`/orbit computations (their internal work), and automorphism move-reduction. So “predicate evaluations” conflates oracle tests with algorithmic subroutines; a 1-eval `ExtGt` oracle is stronger-than-implementation on hard states but weaker in what it can express than full computation. [deduction]

## Conclusion (mathematical finding)
**Literal claim C is refuted for the stated ExtGt-inclusive model on its easiest infinite subclass**: `ExtGt(A_n,2^k)` decides all `k <= ⌈log₂ n!⌉-1` in 1 evaluation (`n>=3`), so not `2^{Ω(n)}` on infinitely many inputs. The meaningful residue is: *on information-nontight gap instances* `(n,⌈log₂ n!⌉)` with `S(n)>⌈log₂ n!⌉` (root not `ExtGt`-prunable), does any `{ExtGt,Reach,Total}`/transcript polynomial-workspace decider need `2^{Ω(n)}` evaluations? — **open**. I found (i) no `2^{o(n)}` algorithm (falsifier not achieved), (ii) no unconditional `2^{Ω(n)}` lower bound (gap infinitude open; no transfer from Ben-Or/query/AND-OR to this computed-input predicate model), (iii) a concrete cost-model/scope gap (oracle vs implemented `e_exceeds`; non-captured orbit pruning). **No separation from P/PSPACE claimed; no Lean/repo changes warranted (no independently checkable new theorem/counterexample beyond this refutation+obstruction).** Distinction kept throughout: general-poset/#P/counting facts and certificate soundness ≠ completeness, and none transfer to exact all-n `S(n)` without a stated reduction.

## Other metadata

```json
{
  "finished_at": 1793866445.7231684,
  "started_at": 1793866035.9345438
}
```
