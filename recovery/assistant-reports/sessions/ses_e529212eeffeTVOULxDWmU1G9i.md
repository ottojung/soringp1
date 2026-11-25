# antonina-PcLx53dZ3kzGLWQTv2zu9t-took

Session: ses_e529212eeffeTVOULxDWmU1G9i
Workspace: /home/lubko/soring-fronts/fo-tc-combined-review-20261105
Created: 1793911024916; updated: 1793911059009

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ad6ded36001AvjjIqhwYnfSdn)

I’ll first locate the combined audit and the exact root-verification procedure, then select a certificate format narrowly enough to prove a soundness/completeness or verification barrier without overclaiming about certificates in general.

## Output 50 (msg_1ad6e1359001a4lMS4QuIBp7JG)

The audit’s root quantifier is over every permutation, while the game formulation branches over feasible comparison outcomes. I’m choosing a deliberately explicit inductive certificate: a complete truth table for winning states at each remaining depth. It gives a clean soundness/completeness theorem and polynomial-in-certificate verification, but I’ll distinguish that from polynomial-size verification in the unary input length.

## Output 50 (msg_1ad6e1359001a4lMS4QuIBp7JG)

## Result: explicit layered winning-region tables are sound and complete, but not succinct

**Chosen format.** For each depth \(d=0,\ldots,k\), give one bit \(W_d(P)\) for every labelled partial order \(P\) on \([n]\). The intended meaning is: from \(P\), the sorter can force a total order using at most \(d\) more comparisons. This is a complete table, not a proposed compact invariant.

### Definition and recurrence

Let \(\mathcal P_n\) be the set of transitively closed partial orders on \([n]\). Write \(P\) as a ternary relation on ordered pairs, and let \(P+(x<y)\) denote adding that comparison and taking transitive closure. The verifier checks:

\[
W_0(P)=1 \iff P\text{ is total},
\]

and, for every \(d<k\) and \(P\in\mathcal P_n\),

\[
W_{d+1}(P)=1 \iff
\left[
P\text{ is total}\ \lor\
\exists\,x,y\text{ incomparable in }P:
W_d(P+(x<y))\land W_d(P+(y<x))
\right].
\]

It also checks \(W_k(\bot)=1\), where \(\bot\) is the antichain.

### Soundness, completeness, and verification

**Soundness.** By induction on \(d\), if \(W_d(P)=1\), the recurrence supplies a strategy: stop at a total order; otherwise ask the indicated incomparable pair and use the two certified \(d\)-round strategies for the two answers. Thus \(W_k(\bot)=1\) implies \(S(n)\le k\).

**Completeness.** Conversely, if a strategy wins from \(P\) within \(d\) comparisons, its first comparison (unless \(P\) is already total) has two feasible outcomes, and its continuation wins from each resulting order within \(d-1\) comparisons. Induction gives \(W_d(P)=1\). In particular, \(S(n)\le k\) implies \(W_k(\bot)=1\).

**Every permutation is covered.** The recurrence’s two universal branches are over feasible answers, not over a sample of inputs. Every hidden total order \(X\in S_n\) is consistent with the comparisons along its execution, so induction on the execution shows that the certified strategy reaches a total order within \(k\) queries on that \(X\). Conversely, a strategy that sorts every permutation wins both feasible branches at every reached state. This ties correctness to **all permutations** while counting only comparison queries in the depth parameter \(d\); table construction and verification time are separate costs.

The verifier can check the recurrence by enumerating all table entries, pairs, and outcomes, computing transitive closures, and checking the root bit. This is polynomial in the explicit certificate length (and in \(n,k\)); it does not establish polynomial-time verification in the original unary input length.

### Why this format fails as a polynomial certificate

The table has \(k+1\) bits per partial order. The number of labelled partial orders is \(2^{\Theta(n^2)}\) (Kleitman–Rothschild; also recorded in the repository literature note), so the complete table is exponential in \(n\), even before accounting for \(k\). For relevant thresholds \(k=O(n\log n)\), the unary input length is \(N=n+k+1=\operatorname{poly}(n)\); this certificate therefore is not polynomial-sized in \(N\).

This is a barrier to **this complete-table format only**. It does not show that every state must be included in a certificate, that winning regions cannot be represented by circuits or other succinct invariants, or that no polynomially checkable certificate exists.

**Literature/context.** The recurrence is the finite minimax game used in the repository’s certificate note; the state-count barrier uses the known asymptotic enumeration of labelled posets (Kleitman–Rothschild, *Transactions of the AMS* 205 (1975)). The sorting model and unary measure are those in `docs/problem.md`. This does not transfer hardness results for arbitrary decision trees or sorting networks to \(S(n)\).

Scratch-only: no repository files changed.
