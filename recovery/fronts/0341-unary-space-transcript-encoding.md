# unary-space-transcript-encoding

## status

investigated

## origin

ai_proposal_unverified

## agent_id

vzXqdKFSAOi9vxUMgUzzLY-medal

## exit_state

clearexit

## question

Investigate whether the comparison transcript of an optimal sorting strategy can be encoded in o(n log n) bits while remaining uniformly decodable, as a path to improving the PSPACE space bound for S(n).

## basis

docs/problem.md unary PSPACE membership; transcript encoding identified as decisive obstacle in previous space front.

## falsifier

Construct an infinite family of optimal strategies whose transcripts require at least n log n bits under every proposed uniform encoding, or show recomputation overhead breaks the bound.

## implication

A sublinear-in-nlogn transcript encoding would improve the known uniform space bound for computing S(n) without changing time class.

## finding_unverified

## Finding: transcript encoding cannot be o(n log n) bits (uniformly decodable)

**Claim attacked (all n):** The comparison transcript of an optimal adaptive sorting strategy can be uniformly encoded in o(n log n) bits and still be decodable to the sorted order / strategy.

**Result: FALSE — falsified by information-theoretic counting.**

- **Definition/experiment.** An optimal decision tree T_n for n keys has at least n! leaves (one per permutation), each leaf labelled by the final total order. Its height is S(n) = Θ(n log n) in worst case, but the *number* of leaves is n! regardless of height.
- **Deduction.** A "transcript" that is uniformly decodable to the output permutation must, for at least one input permutation, carry enough information to identify which of n! leaves was reached. By the counting/entropy bound, any prefix-free (or fixed-length, uniformly decodable) code over a binary alphabet for n! distinct outcomes has average length ≥ log₂(n!) = Θ(n log n) bits, and worst-case length ≥ log₂(n!) = Θ(n log n) bits. Hence no uniform encoding can use o(n log n) bits in the worst case while remaining decodable.
- **Consequence for the space front.** The transcript-size route cannot improve the PSPACE space bound below Θ(n log n) bits per path; the obstruction is not recomputation overhead but the leaf-count lower bound. Recomputation can avoid storing the transcript, but it cannot compress the unavoidable information content below n log n bits if decoding to the permutation is required.
- **Certificate distinction.** This is a *soundness/completeness* separation: an o(n log n)-bit string can be a *sound* partial certificate (verifiable when correct) but cannot be *complete* for all permutations; completeness requires Θ(n log n) bits. General-poset analogues (arbitrary partial orders) do not change this, since the fixed family S(n) already attains the n! leaf count.

**Limits/honesty:** This rules out transcript-compression as a path to sublinear-in-nlogn space for decoding to the sorted order. It does not rule out space improvements via recomputation or via not materialising the transcript at all (those are separate fronts). No Lean/repo changes; clean worktree. No new theorem beyond standard information bound; reported as decisive no-go for this specific route.

## Other metadata

```json
{
  "finished_at": 1794110416.4733877,
  "started_at": 1794110384.9966948
}
```
