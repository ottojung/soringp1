# parallel-reversal-symmetry

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Tp5xCqm9tMGOJGHtOE7YKE-tribe

## exit_state

clearexit

## question

For every pair of finite posets A and B, does reversing one component of their disjoint union preserve the exact minimax comparison number, i.e. is F(A^op disjoint-union B) = F(A disjoint-union B) for all A,B?

## basis

docs/research-parallel-duality.md proves the self-dual-complement case and leaves the general non-self-dual case open after n<=7. I independently reran the isomorphism-class check at n=8: 6248 pairs and 16999 classes, zero violations. No all-n proof or counterexample is claimed.

## falsifier

Exhibit one explicit finite pair A,B with F(A^op disjoint-union B) unequal to F(A disjoint-union B), or an infinite all-n family of such pairs; a single counterexample refutes the all-n statement, while exhaustive checks only decide finitely many sizes.

## implication

A positive answer makes componentwise order reversal a genuine value symmetry for the antichain-root minimax DP, extending relabelling and global duality; a counterexample shows that even disjoint-union components are not reversible and closes this state-quotient route.

## finding_unverified

## Mathematical finding: the all-`n` claim is false

The statement  
\[
F(A^{op}\mathbin{\sqcup}B)=F(A\mathbin{\sqcup}B)\qquad\text{for all finite posets }A,B
\]
has an explicit counterexample already at total size \(n=9\).

Let states be successor bitmasks: bit \(j\) of `succ[i]` means \(i<j\).

- \(A=(0,1,1)\) on keys \(0,1,2\), i.e. \(1<0,\ 2<0\) (the \(\Lambda\) poset: two minima below one maximum).
- \(B=(0,1,1,3,7,11)\) on keys \(0,\dots,5\), with Hasse relations
  \[
  5<3<1<0,\qquad 4<1,\qquad 4<2,\qquad 2<0.
  \]

Then with the \(B\)-block shifted by three labels,
\[
P=A\mathbin{\sqcup}B=(0,1,1,0,8,8,24,56,88),
\]
\[
Q=A^{op}\mathbin{\sqcup}B=(6,0,0,0,8,8,24,56,88).
\]

Exact minimax evaluation gives
\[
F(P)=12,\qquad F(Q)=11.
\]
So \(F(A^{op}\sqcup B)\ne F(A\sqcup B)\).

Both \(A\) and \(B\) are non-self-dual, so this is outside the already-proved restricted theorem. The theorem itself is not contradicted: if the complement is self-dual, reversal is still safe.

## Verification and limits

The two values were checked by three independent implementations:

1. plain labelled minimax DP with no quotient/canonicalisation: \(F(P)=12\) over 668,519 states, \(F(Q)=11\) over 675,433 states;
2. isomorphism-class DP over all \(n=9\) classes (`S(9)=19`): same two values;
3. the repository Python iso+dual DP: same two values.

The exhaustive \(n\le 8\) check still finds no violations (`6248` pairs at \(n=8\)). Thus \(n=9\) is the first size with a counterexample. At \(n=9\), among the 1840 pairs where both components are non-self-dual, 96 violate the equality, so this is not a single numerical accident. A second example is \(A=(0,1,1,5)\), \(B=(0,1,1,5,13)\), again with values \(12\) and \(11\).

The natural induction route also fails: “if a component is non-self-dual, some optimal first comparison lies inside it” is false already at \(n=5\). So the failure is structural, not merely a missing technical lemma.

## Complexity scope

This is a **general-poset exact-value result**, not a hardness theorem. It refutes componentwise reversal as a genuine value symmetry for the disjoint-union minimax DP, but it does not by itself settle any `SORT-BOUND-U` complexity class, nor does it establish or refute certificate completeness. No infinite counterexample family and no replacement theorem are claimed.

Operational state: one new board #301 post was made for this front (`2026-11-08T23:43:00Z`); no duplicate post, no commits, no Lean or repository changes, and the worktree remains clean.

## Other metadata

```json
{
  "finished_at": 1794181415.423245,
  "started_at": 1794178402.5038624
}
```
