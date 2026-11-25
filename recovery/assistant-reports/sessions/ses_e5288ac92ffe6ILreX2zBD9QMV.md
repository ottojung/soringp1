# antonina-TGBT5S85P6mz33NS2NlIDA-resting

Session: ses_e5288ac92ffe6ILreX2zBD9QMV
Workspace: /home/lubko/soring-fronts/fo-tc-combined-review-20261105
Created: 1793911640955; updated: 1793911677521

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 46 (msg_1ad778f2700177jLX3zhAbCjSi)

The existing frontier note establishes a state-count barrier only for explicit enumeration, not for selective symbolic certificates. I’m checking the audit caveats now; the proposed route must preserve disjunctions exactly, not relax them into the existing meet/join invariant.

## Output 62 (msg_1ad77ae9f001h0I8lE2w2HJW5E)

## Result: distinct route, but completeness is still open

A decision DAG whose nodes store **sets of still-compatible permutations** is a distinct route from the existing framed rank-envelope construction: it keeps the exact disjunction of possible histories rather than replacing it at joins by a common guaranteed partial order. It also avoids the bounded-disjunction approach by allowing an unrestricted set at each node. The tradeoff is that this exact representation can itself be enormous.

### Precise certificate grammar

For fixed \(n\), a certificate is a finite acyclic graph with a root, query nodes labelled by unordered pairs of slot indices, and two outcome arcs from each query. Every node \(v\) carries an explicit set \(A_v\subseteq S_n\), represented as a list of permutations of the \(n\) input labels in current slot order.

- Root: \(A_{\rm root}=S_n\), with the identity slot frame.
- For a query \((i,j)\), split \(A_v\) into \(A_v^{i<j}\) and \(A_v^{j<i}\). Each arc has an explicit slot permutation \(\pi\); its child set must be **exactly** the corresponding split, with every order transported by \(\pi\).
- A terminal is accepted only if all permutations in its set have the same sorted output order. Empty-set arcs may be omitted.
- The graph’s maximum root-to-terminal query count is at most \(k\).

This is an exact-set grammar, not a rank-envelope abstraction or a bounded number of disjuncts. A verifier checks permutations, exact splits/transports, terminal correctness, acyclicity and longest-path depth in time polynomial in the explicit certificate length and \(n\). But the root annotation alone has \(n!\) permutations. So this grammar does **not** supply polynomial-size certificates; its all-\(n\) size bound is at least \(\Omega(n!)\), regardless of the DAG sharing.

### Exact remaining lemma

To get a polynomial certificate, one would need a succinct set representation with all three operations—comparison split, permutation transport, and exact equality/containment checking—polynomial-time verifiable, plus a **uniform polynomial-size bound** for some height-\(S(n)\) root strategy using that representation. The exact-set list grammar fails that size requirement immediately. I found no proof that any succinct variant is complete for all optimal root strategies, and no concrete counterexample to a precisely specified succinct grammar; specifying one without smuggling in the unresolved compression property is the remaining lemma/design obstacle.

The known winning-frontier result is not a refutation: it counts many nonisomorphic *reachable winning states* and excludes full frontier enumeration, but does not show they must all occur in one optimal strategy or cannot be represented symbolically. The audit notes likewise scope the barrier to explicit frontier listing and do not establish a lower bound for selective or symbolic methods.

**Stopping point:** the exact set-of-permutations route is distinct, but its direct grammar is factorial-size and the succinct-completeness question has not been resolved. No repository changes or posts made.
