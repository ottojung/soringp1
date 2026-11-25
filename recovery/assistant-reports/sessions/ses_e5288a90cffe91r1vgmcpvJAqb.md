# antonina-KnFxv05LQgD5yY7jdKN55G-histories

Session: ses_e5288a90cffe91r1vgmcpvJAqb
Workspace: /home/lubko/soring-fronts/average-redundancy-lower-bound-20261024
Created: 1793911641850; updated: 1793911664491

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 50 (msg_1ad778f99001ncnUrSCpymuhaS)

The potential-family route hits a precise obstruction: entropy deficit can certify only sublinear *aggregate* imbalance under a near-optimal tree, not force a linear comparison excess on a root path.

For any correct sorting tree of worst-case depth \(k\), with uniform random input permutation, the exact identity is
\[
k-\log_2(n!)=\mathbb E[k-D]+\sum_v q_v\bigl(1-h_2(p_v)\bigr),
\]
where \(D\) is the realized depth and \(p_v\) is a node’s conditional outcome probability. Both terms on the right are nonnegative. Thus an adversary potential based only on accumulated entropy deficit is bounded by the tree’s *existing* redundancy; it does not independently produce a stronger lower bound. In particular, Sergeev’s \(S(n)-\lceil\log_2(n!)\rceil=o(n)\) upper bound is compatible with only \(o(n)\) expected total entropy deficit on that sorting tree. It does not rule out occasional high-deficit paths, but it prevents this expectation identity alone from forcing a uniform linear excess.

This is an inequality obstruction for the entropy-deficit potential, not an all-\(n\) lower-bound proof or a no-go for richer potentials. The transcript-tree identity concerns the actual antichain-root tree; it does not rely on arbitrary reachable hard posets. I made no repository changes, as requested.

**Basis:** deduction from the entropy identity recorded in `docs/research-sergeev-asymptotic.md` (itself a paper deduction); Sergeev’s upper bound is cited there to ECCC TR20-096, Theorem 3. The notes also caution that expected-path statements do not imply adversarial-branch guarantees.
