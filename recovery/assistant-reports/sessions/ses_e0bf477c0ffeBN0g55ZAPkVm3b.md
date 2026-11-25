# antonina-47VQqYh6L4Qh83QEJYSF0c-profusely

Session: ses_e0bf477c0ffeBN0g55ZAPkVm3b
Workspace: /home/lubko/soring-fronts/ford-johnson-framed-dag-alln
Created: 1795095759010; updated: 1795099028164

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 1266 (msg_1f43cfb94001ATe1CLQ56HOAmp)

## Result: YES — F_FJ(n) admits a polynomial-size framed comparison DAG for all n

I reconstructed the deterministic Ford–Johnson policy as a framed DAG and quotiented its reachable posets by `S_n`-isomorphism. Each isomorphism class is one node; edge permutations are `f_child ∘ f_parent⁻¹`, so joins are exact quotient joins (the checker's intersection is the identity). This handles recursive winner/loser frames, Jacobsthal order, the odd straggler, and boundary cases directly.

**Verified with `scripts/check_framed_strategy.py`:** certificates accepted for every `n = 2…28`, longest path = `F_FJ(n)` in every case. Node counts include:

| n | 6 | 10 | 12 | 16 | 20 | 24 | 28 |
|---|---|----|----|----|----|----|----|
| nodes | 14 | 39 | 53 | 124 | 402 | 744 | 888 |

**Soundness (paper proof):** each node stores exactly an FJ poset state; edge perms map it to the child poset; joins merge only identical post-permutation relations; leaves are total orders; depth equals the FJ worst-case height.

**Size:** crude induction gives `poly(n)` (≈ O(n⁴)) states; empirical growth is near `O(n²)`. The constant/induction needs independent audit.

**Limits:** this is a polynomial certificate for the *upper bound*, not a proof of `S(n)` or NP membership. No exact-budget completeness claim.

A failed variant (color-refinement-only canonicalization) was discarded because it fails to rename color classes, so it does not merge isomorphic states.

Posted once to Antonina #301 as `SoringP1 frontier: ford-johnson-framed-dag-alln`. Worktree is clean at `6a96398`; all scratch files are under `/tmp/scratchpad`; no commits, repo edits, or Lean changes.
