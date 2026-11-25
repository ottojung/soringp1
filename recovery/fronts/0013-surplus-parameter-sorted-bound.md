# surplus-parameter-sorted-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

yEw6VLuglegw29ceOPreaX-moved

## exit_state

succeeded

## question

Fixed additive parameter d = k - ceil(log2(n!)): does deciding S(n) <= ceil(log2(n!)) + d admit a uniform f(d)-poly(n) kernel or algorithm for each fixed d over all n, and can sound framed-reset accounts carry an explicit surplus register — or does some all-n family show no such parameterized representation exists?

## basis

Stober-Weiss 2023 parameterization and docs/research-packets.json front d=k-ceil(log2 n!) with the corrected warning that d+F(P) does not characterize viable root histories; S(12)=30 versus information bound 29 is the concrete positive instance, and running ceiling-audit fronts do not treat the surplus parameter.

## falsifier

Exhibit an all-n family and fixed d >= 1 where every sound framed-reset accounting that telescopes to log2(n!) must misprice the optimal strategy unless it stores superpolynomial surplus-relevant state, or conversely a paper-level f(d)-poly(n) kernel construction; small-n instances alone carry no weight.

## implication

A fixed-d kernel would give a concrete road from the known exact DP to a uniform faster evaluator along the surplus axis, while a representation obstruction would pin the true remaining obstacle of framed-certificate completeness to the surplus register rather than to ratio accounting.

## finding_unverified

I have the repo context and the front. Now I'll work the falsifier with an experiment that discriminates between the two hypotheses in the front (cheap, small-n only to *steer* the paper argument — the claim itself is all-n).
The naive F-computation was too slow. Let me rewrite with memoization and extension counting only where needed, restricted to small instances (m ≤ 4, n = 8) — just enough to discriminate between hypotheses for the paper argument.
m=2 and m=3 show F = info (gap 0) — this falsifies my initial hypothesis for small m. Let me push to m=4–5 (n=8–10) with the corrected code running longer.
I’m checking for durable effects first. The earlier work only read the board and ran a temporary local experiment; I’ll verify the worktree and board digest before deciding whether any post or repository change remains to be done.
**No side effects from the interrupted work were found:** the repository is clean, there is no new commit, and the recent #301 digest shows no post from this investigation. The only experiment was in `/tmp/opencode/surplus`; it was interrupted while computing the next case.

The mathematical question remains unresolved. One concrete failed approach was exhaustive minimax evaluation of the posets consisting of disjoint 2-element chains: it returned \(F(P)=\lceil\log_2 e(P)\rceil\) for \(m=2,3\), while the \(m=4\) computation did not finish. These small cases neither support an all-\(n\) obstruction nor establish an algorithm.

The precise obstacle is that the known winning-frontier bound rules out enumerating all reachable winning posets, but does **not** rule out selective or compressed evaluation. Likewise, sound framed certificates do not give completeness: local information counts can underprice a position’s minimax cost, and no all-\(n\) argument was established that forces a superpolynomial surplus register—or constructs an \(f(d)\operatorname{poly}(n)\) algorithm. So there is no new theorem or counterexample to report from this investigation.

## Other metadata

```json
{
  "finished_at": 1793130897.0450077,
  "started_at": 1793125937.6943104
}
```
