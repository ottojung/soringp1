# comparison-dag-width-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

sMwxxTYz7R9yVOKi2pFgOn-urgently

## exit_state

clearexit

## question

For the comparison model, must any optimal sorting strategy for large n have comparison DAG width Omega(n log n) or treewidth Omega(n), creating a barrier to parallel evaluation, or can width be kept polylogarithmic while preserving height S(n)=Theta(n log n)?

## basis

Sorting networks have fixed structure; adaptive trees differ. Parallel complexity of sorting is well-known, but exact height-optimal adaptive strategies vs width constraints not directly analyzed for S(n).

## falsifier

Construct a width-O(log^c n) comparison DAG achieving height S(n) for all n, or prove a width lower bound Omega(n) for all height-optimal strategies.

## implication

Width/treewidth barriers would connect the sequential depth S(n) to parallel complexity (NC^1/NC^2 separation attempts) and distinguish adaptive decision trees from network-like low-width computations.

## finding_unverified

Omega(n log n)” or “treewidth Omega(n)” depends on the exact width notion (branching program width = pathwidth-related; circuit DAG width; treewidth of the graph). The existing note says “exponential in n log n (up to factors)” for pathwidth/width of that subgraph - exponential is >= Omega(n log n). So the stronger exponential lower bound is supported by current evidence; the specific linear-in-some-form lower bound Omega(n log n) is plausible as a corollary under standard translations, but not obviously the tight form from the published frontier numbers alone. The frontier gives exponential, not polynomial-in-n lower bound.

### Complexity implications / distinctions
- **Soundness vs completeness:** the verifier for a given strategy DAG is polynomial in DAG size (docs/research-strategy-certificates.md) - that’s soundness of a witness. The obstruction is to *completeness* (existence of small/polynomial or low-width witness for all-n optimal strategies). Also sparse-unary language + Mahaney is a separate barrier to certain NP-hardness routes, but width/barrier here is different (state complexity/merging).
- **General posets vs sorting (antichain):** the frontier is constructed from posets reachable from the n-antichain (rectangular chain+extra edges) and is winning at exact optimal budget - it’s directly relevant to sorting/S(n), not an arbitrary poset hardness claim pulled in without reduction.
- **Parallel complexity:** bounded-width branching programs relate to NC^1 (Barrington). Exponential width / exponential pathwidth would block fixed/polylog width compression, connecting to NC^1/NC^2 separation attempts as suggested - but this is a conditional/structural obstruction given the frontier, not a proved class separation for SORT-BOUND-U itself.

### Concrete failed/blocked approach & honest limits
- **Blocked:** polylog-width (width O(log^c n)) construction for height S(n) is blocked by the winning frontier’s exponential number of non-equivalent winning states at fixed depth that cannot be merged without sacrificing optimality. 
- **Unclear/needs precision:** exact constants for “Omega(n log n)” vs exponential depend on width definition (level width vs pathwidth vs treewidth). The strongest directly evidenced is exponential in n log^2 n states/width in that frontier. 
- **No repo/Lean changes:** no new theorem proved here; this is a deduction from existing published results in the repo (winning frontier + FO(TC)/branching program barrier). 
- **Not excluded:** selective search/proof-number search, different representations, or algorithms that don’t require materializing that frontier - the barrier is about *width/compression* of representing an optimal strategy, not about computing S(n) by other means.

**Bottom line:** the falsifier’s polylog-width construction is **obstructed** by the winning frontier (exponentially many non-equivalent winning states at same depth => exponential width required for any optimal strategy represented in level-wise/DAG form), so you cannot have width-O(log^c n) while preserving height S(n); the more precise all-n width lower bound is exponential in n log^2 n under branching-program/level-width semantics, which is stronger than Omega(n log n). Treewidth/pathwidth exponentiality matches. This is a structural barrier to low-width (NC^1-like) parallel evaluation of optimal adaptive strategies, but it’s a compression/representation barrier - not a proof separating complexity classes of SORT-BOUND-U by itself.

## Other metadata

```json
{
  "finished_at": 1793650290.6757343,
  "started_at": 1793647384.1108277
}
```
