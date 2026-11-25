# antonina-XJnFrsaJbMzlNW210LxLtT-sealing

Session: ses_e51b37af2ffewiFcHw0PyPJTnv
Workspace: /home/lubko/soring-fronts/parallel-reversal-congruence-20261106
Created: 1793925612816; updated: 1793925708325

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ae4c8537001UNlSxGRt15Ajm4)

I’ll first inspect the requested planning/frontier documents and repository state, then focus on whether annotation diversity is constrained in the exact antichain-root certificate model rather than in arbitrary DAGs.

## Output 90 (msg_1ae4d04cb001T0tviYqGFSEOAh)

The identity controls summed annotation forgetting, but it may not control the number of labels a path visits: even zero-loss paths can change the poset by comparisons. I’m checking whether a concrete family separates these quantities while still having the exact antichain-root optimum, rather than relying on a generic poset counterexample.

## Output 141 (msg_1ae4dea3a001EIbsUPQWx9iB2l)

Added [`docs/research-annotation-diversity.md`](docs/research-annotation-diversity.md).

The result is deliberately limited: exact-history annotations can have zero forgetting loss while changing repeatedly, so the identity alone does not count annotations. The insertion-sort witness is **not** a superpolynomial counterfamily, and its height is not `S(n)`. I found no bridge from this observation to exact antichain-root optimality; the note states the missing obstacle and stops there. No commit or board post.
