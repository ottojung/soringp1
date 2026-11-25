# antonina-IXgcaUoevjcPL6KQCGj3zy-cigar

Session: ses_e4b6d86eeffe4TbX7qKaSpfbnJ
Workspace: /home/lubko/soring-fronts/exec-optimal-frontier-basis-20261107
Created: 1794030860609; updated: 1794030888347

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b4927ac8001VC4SPRdS1UGo4J)

I’ll treat this as a paper-analysis task only: inspect the theorem and basis note, then test whether the frontier family controls the minimal layer under the actual state order. No repository or artifact changes.

## Output 27 (msg_1b4928eff0018vHUWZfdiJK62Q)

**Result: unresolved; the exact-optimal frontier theorem does not by itself imply a large minimal layer.** The missing step is substantive: the independent-edge family does not have the “exactly \(t\) relations” property that made the earlier disjoint-pair states automatically minimal.

Write \(P_A\) for the transitive closure of the column-chain edges and the \(m\) selected adjacent-level edges \(A\). Although each installed comparison advances exactly one level, closure also contains relations across multiple levels whenever there is a path. Thus \(P_A\) generally has **more than** \(t=t_0+m\) comparable pairs. Reachability in exactly \(t\) comparisons gives a state at least \(t\) comparable pairs, but no longer forces a reachable \(Q\subseteq P_A\) to equal \(P_A\). The disjoint-pair proof’s key equality argument therefore fails.

For fixed \(n,t,r\), let
\[
W=\{P:\ P\text{ is reachable in exactly }t\text{ comparisons and }F(P)\le r\},
\]
ordered by relation inclusion. A state \(P_A\in W\) is minimal only if there is no distinct \(Q\in W\) with \(Q\subsetneq P_A\). The frontier theorem establishes many \(P_A\in W\), including at \(r=S(n)-t\); it does not show that these states lie in the minimal layer, nor bound how many \(P_A\)'s a minimal \(Q\) can dominate. Counting an antichain among the \(P_A\)'s would not settle that: minimal dominators could lie outside the family.

**Precise unresolved claim.** For infinitely many \(n=2^{2r_0}\) (using a different symbol for the theorem’s exponent), at its stated common depth \(t\) and residual budget \(S(n)-t\), prove a superpolynomial lower bound on the number of inclusion-minimal elements of \(W\); or prove a sufficiently small upper bound on the number of frontier members dominated by each minimal element. A counterexample to the proposed inference would be a family of reachable winning \(Q\subsetneq P_A\) that covers enough of the constructed frontier to collapse its minimal layer. The theorem does not currently supply such a family or rule one out.

If proved, this would rule out polynomial-size **relation-inclusion dominance bases** for those fixed exact-optimal \((n,t,r)\) instances. It would not imply a lower bound for arbitrary evaluators, symbolic summaries, or any complexity-class separation. A falsifier is an all-\(n\) domination argument showing the constructed frontier is covered by only polynomially many minimal winning states (or an explicit such covering at the relevant parameters).

The decisive obstacle is controlling **winning, exactly-\(t\)-reachable suborders of the full transitive closures \(P_A\)**. The edge-choice count, nonisomorphism count, and pairwise incomparability within the constructed family do not provide that control. No artifact or computation was warranted.
