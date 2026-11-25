# antonina-UiHGyNCY4UsNlCE6grDlK7-anteroom

Session: ses_e51ddf580ffezCVWkMy19hfof7
Workspace: /home/lubko/soring-fronts/parallel-reversal-congruence-20261106
Created: 1793922828930; updated: 1793922887430

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ae220ab2001hvNeielG1moEDo)

I’ll keep this read-only and narrowly test the certificate bridge: first locate the current frontier note and local references, then inspect the cited primary sources and issue discussion for exact algorithm semantics.

## Output 34 (msg_1ae2228fc0017O635pX8xJTbiP)

The frontier note already flags exact optimality as the open gap. I’m retrieving the arXiv full text and #47 now; the key distinction is whether Rutschmann’s guarantee concerns an approximate adaptive sorter from a poset, or an exact minimax strategy with compact transition states.

## Output 85 (msg_1ae22a07d0013tC4zxSeMq9fI1)

## Audit result

**The Rutschmann theorem does not imply a polynomial-size framed strategy DAG of height \(S(n)\) for the antichain.** It gives a sound comparison sorter, but its guarantee is asymptotic in the number of linear extensions—not exact minimax optimality.

### What the primary text says

Rutschmann, *Sorting under Partial Information with Optimal Preprocessing Time via Unified Bound Heaps*, arXiv:2604.12653v2 (8 Oct 2026):

- **Theorem 5:** Given a DAG \(G\) on \(X\), preprocess in \(O(m)\); for any unknown linear order compatible with \(G\), sort in \(O(\log e(G))\) **time and comparisons**.
- The proof reduces to a smaller instance \(H\) on \(Y\), sorts \(Y\) with `UniTopSort`, then reconstructs the order of \(X\). For `UniTopSort` (Theorem 4), preprocessing computes a topological order; the sorting phase inserts all items in that order into an adaptive heap and repeatedly extracts the minimum. The heap’s amortized costs are analyzed using insertion/extraction indices and intervals, with the interval lemma bounding total cost by \(O(n+\log e(G))\). The reduction handles the additional \(O(n)\) term.
- The algorithm is an adaptive comparison procedure: its heap operations compare keys during the sorting phase. The \(O(m)\) preprocessing is graph processing before comparisons; \(m\) is the input DAG’s edge count. The \(O(\log e(G))\) bound is asymptotic, not an exact comparison-count formula.

Those are algorithmic and amortized-cost claims. The paper does **not** state that its comparison tree has height \(\lceil\log_2 e(G)\rceil\), that it attains the minimum worst-case number \(F(G)\) for each poset, or that its internal heap states form a polynomial-size framed DAG.

### Why this does not establish the certificate bridge

For the initial antichain, \(m=0\) and \(e(G)=n!\). Applying Theorem 5 yields a correct sorter with \(O(\log(n!))=O(n\log n)\) comparisons. Even if one unrolls its computation into a strategy DAG, that only supplies an upper-bound sorter; exactness requires a separate proof that its height is \(S(n)\). No such implication follows from the theorem’s asymptotic bound.

Moreover, a polynomial-size control/data structure is not automatically a polynomial-size **sound framed certificate** under the frontier note’s grammar. One would need to show how each heap/configuration state maps to a partial-order annotation and explicit slot-permutation frame, and that every join preserves the guaranteed relation. The paper’s amortized analysis tracks operation indices and interval bounds; it does not supply that simulation or join-soundness argument.

So the precise missing implication is:

> **Rutschmann Theorem 5 does not provide an exact-optimality bridge or a certificate-state simulation.** Its \(O(\log e(P))\) upper bound cannot be read as \(F(P)\), and its preprocessing-time bound is not a bound on the size of a framed strategy DAG.

This is not a counterexample to the possibility that a simulation or exact certificate exists; it is a counterexample to the stronger inference that those conclusions follow from the stated theorem. The frontier note’s distinction remains: a polynomial verifier establishes soundness for certificates presented, while polynomial-size certificates for **every** true \((n,k=S(n))\) instance would require an independent completeness theorem.

### Cross-checks and limits

- Issue #47 explicitly asks for exact height \(S(n)\), distinguishes soundness from all-\(n\) completeness, and labels Rutschmann’s \(O(\log e(P))\) result as not exact \(F(P)\). This audit does not duplicate a new positive or negative theorem; it confirms that the primary theorem does not close that gap.
- I could not retrieve the SODA 2025 full paper from SIAM’s PDF endpoint (403). It is unnecessary for the conclusion: Rutschmann’s primary text describes the Haeupler et al. result as \(O(m)\) preprocessing and \(O(\log e(G)+m)\) sorting time, and contrasts it with Theorem 5. Neither statement supplies exact minimax optimality.
- **Complexity consequence:** none beyond the known upper-bound sorting algorithm. This audit establishes neither polynomial certificate completeness nor membership/nonmembership of `SORT-BOUND-U` in NP, and makes no claim resolving that language.
