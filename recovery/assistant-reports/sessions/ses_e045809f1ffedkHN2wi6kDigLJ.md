# antonina-DJMRv9WrG6RcKGGX6LU1BW-train

Session: ses_e045809f1ffedkHN2wi6kDigLJ
Workspace: /home/lubko/soring-fronts/curator
Created: 1795223451158; updated: 1795224077969

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 194 (msg_1fbafe797001EdjTDCA5aiwiy3)

I have now mapped the frontier state. Let me record the curation input precisely and write the deliverable file.

## Output 221 (msg_1fbb155df001I02bVjTX0NCcnk)

```json
{
  "fronts": [
    {
      "id": "cross-charge-merge-information-alln",
      "question": "For every n, is the optimal adversary cross-component comparison charge for a reachable antichain-root composition at most the information-theoretic merge bound derived from the component linear-extension counts?",
      "falsifier": "Exhibit a reachable composition whose optimal cross charge exceeds the merge information bound by at least two comparisons, or prove the uniform control for all n.",
      "implication": "A proof would give a cross-charge certificate usable for the exact unary decision problem; a counterexample would defeat leaf-only pruning on reachable states.",
      "basis": "Newest board #301 defect-prune domination, transitivity-aware cross obstruction and adversary-composition results; docs/research-structural-lower-bounds.md Theorem B."
    },
    {
      "id": "signflip-cross-rule-optimality-alln",
      "question": "For every n, is the sign-flipped cross comparison rule optimal for the adversary in all reachable optimal plays from the n-element antichain root?",
      "falsifier": "Give a reachable composition where the sign-flipped rule is strictly suboptimal in cross charge, or prove universal sign-flip optimality for all n.",
      "implication": "Universal sign-flip optimality would give a uniform cross-charge strategy for exact unary evaluation; failure would require strategy-specific cross rules.",
      "basis": "Board #301 2026-11-21 transitivity-aware cross finding localizing a failing step and identifying a sign-flipped successor."
    },
    {
      "id": "defect-prune-reachable-antichain-alln",
      "question": "For every n, does defect-based pruning ever strictly outperform the information-bound prune on a state reachable on an optimal play from the n-antichain?",
      "falsifier": "Exhibit a reachable antichain-root state where defect pruning certifies a strictly larger feasible set at the same remaining budget, with exact values, or prove domination for all reachable states and all n.",
      "implication": "A proof would give a leaf-count-only exact evaluator for the unary threshold language; a counterexample would re-open defect pruning for SORT-BOUND-U.",
      "basis": "Board #301 exec-defect-prune-exponent-20261121 domination check through n=7; docs/research-one-ply-obstruction.md one-ply bound."
    }
  ]
}
```
