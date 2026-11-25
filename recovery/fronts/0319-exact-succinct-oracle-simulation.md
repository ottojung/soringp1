# exact-succinct-oracle-simulation

## status

investigated

## origin

ai_proposal_unverified

## agent_id

QGFdnQNM6vlXhD9d6ERieu-biscuit

## exit_state

clearexit

## question

Determine whether the existing 2^{O(N log(N+2))} unary threshold DFS can be simulated by a polynomial-space alternating machine with O(log N) alternation depth while preserving exact minimax semantics at the antichain root.

## basis

docs/problem.md unary PSPACE membership and research-budgeted-dfs.md §5.3; board #301 certificate soundness versus completeness gap.

## falsifier

Exhibit an explicit root-optimal comparison history whose simulation requires superlogarithmic alternation or whose state cannot be recomputed in polynomial space.

## implication

A positive result would collapse the unary threshold into a smaller alternating class; a negative result would bound succinct simulation of exact S(n) evaluation.

## finding_unverified

I’ll keep this strictly to the requested local study: inspect the contract/problem and board #301 context, then assess the claim against primary sources and try to construct or rule out the proposed falsifier. I won’t modify repository files or create Lean work.
The key distinction is now clear: the DFS recursion depth is at most the unary budget `k`, but that is not the same as alternation depth. The minimax recurrence has alternating existential/universal choices at each comparison, so the naive translation costs Θ(k) alternations on surviving paths; the question is whether minimax structure at the antichain root admits a compression. I’m checking board #301 for prior attempts and then will test the obvious proposed compression against root-reachable states rather than arbitrary posets.
**Finding: inconclusive; no root-specific alternation compression or counterexample established.** No files were changed, and no Lean or repository work was created.

**Definition / deduction.** The budgeted DFS gives a polynomial-space algorithm whose recursion depth is at most `k`. Translating its minimax recurrence directly into an alternating machine uses an existential comparison choice followed by universal outcome branching at each recursive level. This gives an `O(k)` alternation-depth simulation, not `O(log N)`. Since `k` may be Θ(N) on nontrivial unary instances, that direct translation does not prove the proposed bound.

That is not a lower bound: DFS recursion depth does not show that every equivalent alternating simulation needs that many alternations. Nor does the requested falsifier follow from an explicit long history: a history of length Θ(k) would only refute that particular level-by-level simulation, not every polynomial-space alternating machine with logarithmic alternation depth.

**Exact obstruction.** To establish the positive claim, one needs a uniform way to compress the alternating minimax choices while preserving their order and exact root semantics. To establish the proposed negative claim, one needs a lower bound against *all* such simulations, or a concrete failure of polynomial-space state recomputation. I found neither. No general-poset complexity result supplies that root-specific lower bound, and certificate soundness alone does not establish completeness or a short complete certificate.

The board digest’s recent entries did not provide a relevant prior proof or falsification; the soundness/completeness gap remains unresolved. Therefore, the claimed collapse to a smaller alternating class is **not established**, and no negative bound on succinct simulation is established either.

## Other metadata

```json
{
  "finished_at": 1794050405.8206816,
  "started_at": 1794050342.7049556
}
```
