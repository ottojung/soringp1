# static-dag-forgetting-loss-obstruction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

i1yoIrf4Cx10rIfICNaXgp-doran

## exit_state

clearexit

## question

For any sound framed comparison DAG achieving height exactly S(n) for the n-antichain and all orderings, is there an infinite sequence of n with total forgetting loss Lambda = sum lambda_b >= Omega(n log n) over some root-to-terminal path family that is unavoidable, forcing DAG size >= exp(Omega(n log n) / delta) or directly obstructing polynomial size?

## basis

Framed certificate entropy identity (section 4) plus large winning frontier at exact budget; distinguish static DAG completeness from search algorithms and from polynomial-size witnesses for non-optimal sorts.

## falsifier

Construct for all n a polynomial-size sound framed DAG at budget S(n) with uniformly bounded per-join forgetting loss and no Omega(n log n) aggregate loss, or prove an all-n lower bound on aggregate loss impossible.

## implication

If unavoidable aggregate forgetting loss grows superlogarithmically in a way incompatible with polynomial joins, it would give a concrete obstruction to SORT-BOUND-U in NP via static framed certificates (separating soundness from completeness).

## finding_unverified

sing this as a question/hypothesis to attack. The instruction says "attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n), and try seriously to DISPROVE it." The "claim" being attacked is the FRONT hypothesis. Also says "FALSIFIER: ..." as part of the setup - perhaps suggesting ways to falsify/disprove the FRONT claim.

And EVIDENCE says "Framed certificate entropy identity (section 4) plus large winning frontier at exact budget" - the identity gives E[sum(1-H + lambda_b)] = S(n)-log2(n!) = o(n). So aggregate of (1-H+lambda_b) is o(n). The FRONT is claiming aggregate forgetting loss Lambda = sum lambda_b >= Omega(n log n) is unavoidable. But if total is o(n) and 1-H_b >= 0, then sum lambda_b <= sum(1-H_b + lambda_b) = o(n). That would mean aggregate forgetting loss Lambda = sum lambda_b <= o(n) is necessary, not >= Omega(n log n). That would DISPROVE the FRONT claim.

Also "large winning frontier at exact budget" - at exact budget S(n), you still have exponentially many winning states (theorem in winning frontier says it extends to S(n) since excess is o(n)). The identity says even with optimal height, the total forgetting loss is constrained to be o(n) on average. That seems contradictory to "forcing DAG size >= exp(Omega(n log n)/delta)" if the loss is actually small.

But also the identity is under "auxiliary random walk" - is every root-to-terminal path in that DAG a path of this random walk? Or is it a property of the structure? The auxiliary walk samples according to q_b computed from current annotation. But in the actual DAG, different input orderings take different paths; the structure is fixed. Is there a constraint linking all paths?

Also look up how the identity applies - "Consider the following auxiliary random walk through a sound certificate: sample each outgoing arc with probability q_b computed from its current annotation..." This is a randomized process defined on the certificate structure. The expectation gives the identity. But the FRONT says "total forgetting loss Lambda = sum lambda_b >= Omega(n log n) over some root-to-terminal path family that is unavoidable" - so over some paths/family of paths (not necessarily the expectation over this random walk). Could individual paths have large sum lambda_b while average is small?

For example, some paths could have large lambda_b and others small to compensate? Since sum is telescoping to log2 e(leaf)-log2 e(root) = -log2(n!) independent of path? Wait - let us check the telescoping again carefully.

Let us verify the math once more carefully.

The FRONT claim is false. For any sound framed comparison DAG achieving height D ≤ k, every root-to-terminal **annotation-majority** path (exists at every node since q_b + q_{b'} = 1) satisfies
$$
\sum_{b\in\mathrm{path}} \lambda_b \le \sum_{b\in\mathrm{path}} \bigl(\log_2(2q_b)+\lambda_b\bigr)=D - \log_2(n!) \le k - \log_2(n!).
$$
With $k=S(n)=\log_2(n!)+o(n)$ (Sergeev), unavoidable annotation-majority paths have total forgetting loss $\Lambda=o(n)$, contradicting $\Lambda\ge\Omega(n\log n)$. The identity gives the obstruction direction: $\sum (1-H+\lambda_b)$ averages to $D-\log_2(n!)$ over the random walk but the stronger per-path bound holds for majority paths; large aggregate loss is incompatible with height near the information bound, so polynomial-size static framed certificates at optimal height are not ruled out by this loss mechanism—separating soundness from completeness remains open.


## Other metadata

```json
{
  "finished_at": 1793398228.9560647,
  "started_at": 1793396650.4618096
}
```
