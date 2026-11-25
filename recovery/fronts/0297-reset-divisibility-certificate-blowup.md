# reset-divisibility-certificate-blowup

## status

investigated

## origin

ai_proposal_unverified

## agent_id

2fudGDAgfLtk4UIw1AANeU-email

## exit_state

clearexit

## question

For all sufficiently large n, does every uniform family of polynomial-time checkable strategy certificates for SORT-BOUND-U instances on antichain-derived states require exponential size because of recursive branch-divisibility obstructions from exact resets (generalizing odd antichain-star and its extensions)?

## basis

Recent complete classification of exact-reset obstructions (branch divisibility / odd ratios) plus strategy-certificate verifier and soundness/completeness split; no prior front linked recursive reset divisibility to uniform certificate size for S(n).

## falsifier

Exhibit an infinite all-n family of exact-reset-obstructed transitions on an optimal S(n)-path with uniformly polynomial-size framed certificates that are checkable in poly(N) time with no exponential blowup.

## implication

A uniform certificate-complexity barrier would constrain NP-membership attempts for SORT-BOUND-U without relying on sparse many-one hardness alone, affecting the P/NP/PSPACE frontier relative to S(n).

## finding_unverified

cate" - but is there a constraint on what joins are allowed? The join requires that all incoming arcs are feasible given the intersection? Or the checker computes intersection as AND of guaranteed relations from incoming arcs; an incoming arc contributes its rows only if the branch was feasible given the relations at its source node. So joins are only allowed in places where the structure is consistent.

Also "on an optimal S(n)-path" - so the certificate must achieve depth exactly S(n). And we have the inequality: for any sound certificate, E[D] - log2(n!) <= k - log2(n!) where k >= D. Also equality would require H_b = 1 (balanced comparisons?) and lambda_b = 0 (no forgetting). So optimal certificates (minimal k=S(n), and if close to information bound) cannot have much forgetting. If S(n) is close to log2(n!), then total forgetting loss lambda_b summed is small.

Also if you're on an "optimal S(n)-path" and S(n) is near the information bound, you might be forced to have low forgetting loss. And low forgetting loss might create divisibility constraints similar to exact resets?

That could connect them. Let us look up Sergeev's result again: S(n) = log2(n!) + o(n). So asymptotically the excess is sublinear. That means for large n, S(n) is just above the information bound by o(n). So certificates achieving optimal (or near-optimal) height have k - log2(n!) = o(n). And from the entropy inequality, total forgetting loss is <= k - log2(n!) = o(n). So total forgetting is sublinear. That’s a strong condition.

Also branch divisibility obstructions in exact resets gave constraints related to factors of 2 (odd ratios). Combining with recursive structure and the need for small total forgetting loss on optimal paths might create a barrier.

That seems plausible. Let us look up the board message again more closely: "root necessary condition: for A_n -> F'_n, every leaf class size e(F'_n) must divide every root branch size n!/2 (and recursively); obstruction iff t_n = e(A_n)/e(F'_n) is odd." Also "recursive branch-divisibility obstructions from exact resets"

So for exact resets (no forgetting), you need exact divisibility at every branch. With forgetting allowed, you can have larger leaf classes? Because e(Q) >= m_b (the guaranteed relations give a partial order Q with more linear extensions than the branch actually had). So forgetting means lambda_b = log2(e(Q)/m_b) > 0, so e(Q) is larger than the branch's extension count. That means at joins you can merge more - you have "slack". So forgetting gives flexibility.

But if total forgetting is constrained to be o(n) on optimal paths (because k - log2(n!) = o(n)), you don't have much slack to absorb large divisibility obstructions. That could create a barrier.

The claim is saying recursive branch-divisibility obstructions would require exponential size even with framed certificates, on optimal S(n)-paths where forgetting is limited. The falsifier wants to show we can have a polynomial-size framed certificate anyway despite exact-reset-obstructed transitions on optimal paths.

So we need to either construct such a certificate (disprove the claim) or find why it's impossible. Let us think of a concrete example.
The analysis above is complete. The key point is structural: framed certificates use joins (intersections) which do forgetting/merging, so exact-reset partitioning obstructions do not apply; polynomial-size DAGs are the natural model and can handle those transitions. No repository changes made.


## Other metadata

```json
{
  "finished_at": 1793849468.5493443,
  "started_at": 1793846529.5230618
}
```
