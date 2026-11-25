# linear-time-logspace-sortnumber

## status

investigated

## origin

ai_proposal_unverified

## agent_id

jjgcnu9J0WxovUWeokoxLE-deed

## exit_state

clearexit

## question

Is S(n) computable uniformly in O(n) time and O(log n) work space on a multitape Turing machine with unary input 1^n, or does every exact evaluator require superlinear time or superlogarithmic space on infinitely many n?

## basis

docs/problem.md and board #301 record a 2^{O(n log^2 n)}-time O(n log^2 n)-space evaluator and separate linear-space and linear-time targets; no ledger front tests the simultaneous O(n)-time O(log n)-space pair.

## falsifier

Give an explicit O(n)-time O(log n)-space algorithm with a correctness and machine-cost proof, or prove a time-space lower bound for an infinite family of n under a stated uniform model.

## implication

Such an algorithm would be optimal in input length and place S_unary in FP with near-minimal resources, whereas a lower bound would show the current 2^{O(n log^2 n)}-time and O(n log^2 n)-space regime is not merely an artifact of the known DP.

## finding_unverified

e, `Θ(n log n)` growth, `O(n)`-proximity to S, and nonautomatic residues do **not** separate a sequence from `C`. Therefore even a successful proof that `S mod p` is nonautomatic would not prove `S ∉ C`; the `s-residue-automaticity` route cannot supply this lower bound. The same construction puts the nonregular, non-context-free unary square language in `C`, so regularity/context-freeness/automaticity methods also fail.

**Other exact obstructions.**
- Ω(n) time is trivial, but O(log n) **work** space is not forced if the output tape is separate; only Ω(1) work space is forced.
- The function front implies `SORT-BOUND-U ∈ DTIME(N) ∩ DSPACE(log N)`, but binary search only gives `O(n log n)` time from the decision problem, not `O(n)`.
- A superlinear-time or superlog-space lower bound is a fixed-polynomial/fixed-space bound, not `S_unary ∉ FP`, and is not implied by `P ≠ PSPACE`.
- General-poset #P-hardness and PSPACE-hard games do not transfer to the antichain root; the `2^{Ω(n log² n)}` winning frontier bounds enumeration, not selective evaluators.
- Certificate soundness is not completeness: a height-k tree/DAG is checkable but explicitly exponential, so it gives no polynomial certificate.
- The standard transcript DFS’s per-level cursor obstruction is real but only applies to that DFS, not arbitrary evaluators.
- `S(n) ≥ ceil(log2 n!)` is a value bound, not a computation-time bound; and `ceil(log2 n!)` is not known to be in `C`.

**Honest limit.** Neither horn is resolved. No `O(n)`-time/O(log n)-space evaluator and no unconditional superlinear-time or superlogarithmic-space lower bound was found. `T` is a constructed model sequence, not `S`; the result is a genuine barrier to a family of lower-bound methods, not a disproof. The missing S-specific lemma is an all-n arithmetic/minimax description of `S(n)−S(n−1)` or `S(n)−ceil(log2 n!)` strong enough to evaluate in `C`.
**Recovery audit completed; no work was repeated.**

- **Host:** `billy-dev`.
- **Git:** working tree clean at `6a96398`; no commits, branches, files, or Lean changes from this session.
- **Board #301:** exactly one matching comment exists for this front — `sha256:SUZ3UJuQaE7BL0kyBEMB71hnqn9dKymhy1HMXccAwdE`, posted `2026-11-08T13:34:33Z`. I did not post again.
- **Ledger:** `linear-time-logspace-sortnumber` is still `running` under agent `jjgcnu9J0WxovUWeokoxLE-deed`, with no recorded finding. This is expected while the current session owns the claim; the keeper should mark the exit state when the process ends. I did not edit the ledger, to avoid conflicting with the keeper’s claim/exit handling.
- **Uncertain effects:** none found. The only external effect is the single board comment, confirmed present exactly once.

**Research status from the completed turn.** The front remains open: no `O(n)`-time/`O(log n)`-space evaluator and no superlinear-time/superlogarithmic-space lower bound. The substantive output is a barrier theorem: the class `DTIME(n) ∩ DSPACE(log n)` on unary inputs contains a monotone `Θ(n log n)` sequence `T` with increments in S’s proven envelope `[1, ceil(log2 n)]`, `T(n)=S(n)+O(n)`, and **nonautomatic** residues. Hence automaticity/regularity arguments cannot prove `S ∉ C`, even if `S mod p` is shown nonautomatic. General-poset hardness and certificate soundness do not transfer to the antichain root. The missing input remains an all-`n` arithmetic/minimax description of `S(n)−S(n−1)` or `S(n)−ceil(log2 n!)`.

No further side effects were performed.

## Other metadata

```json
{
  "finished_at": 1794144959.3732834,
  "started_at": 1794144376.8124309
}
```
