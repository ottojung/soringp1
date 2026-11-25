# unary-threshold-downward-selfreduction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

XzbbL1ZnOdcqFQVmB1yCCe-recurs

## exit_state

clearexit

## question

For all n>=2 and k>=1, can SORT-BOUND-U membership 1^n#1^k be decided by a deterministic polynomial-time oracle Turing reduction that queries only SORT-BOUND-U instances 1^m#1^j with m < n and total query/input length poly(n+k), using a locally checkable antichain-root comparison decomposition?

## basis

AGENTS.md/problem.md define SORT-BOUND-U as the active unary target; docs/research-budgeted-dfs.md gives transcript-only DFS and root-prefix sibling obstruction appears in research-frontier.json/ledger context, but no prior front tests polynomial downward self-reduction of the threshold language itself.

## falsifier

Exhibit an infinite family (n_t,k_t) where any correct root-decomposition reduction requires either some query with m_t >= n_t, superpolynomially many m_t<n_t queries, or an uncheckable optimal-branch selection not captured by polynomial-size transcripts.

## implication

A uniform downward self-reduction would constrain the structure of exact S(n) evaluation and could enable recursive compression or interact with sparsity/complexity consequences; a robust obstruction would separate S(n) from downward-self-reducible sparse threshold families.

## finding_unverified

eduction]**
   - A transcript/certificate that records a root comparison and two valid
     continuations is **sound** only relative to correct evaluation of the
     successor poset games; checking those successors is exactly the hard
     `n`-element general-poset subproblem, not a local check against `L_U(m<n)`.
   - “Locally checkable” is satisfied by the recurrence shape, but **completeness
     of a reduction to `L_U, m<n` is not**: local checkability of a comparison
     step does not supply a proof that `F(A_n+e^±)` is determined by smaller
     antichain thresholds. Any claim that it is would be an unjustified
     general-poset-to-antichain transfer (the interleaving of the ordered pair
     with the remaining `n-2` antichain elements is global over `n` elements).

4. **Concrete small witness of the axis mismatch (not a family separation claim). [deduction]**
   `n=4, k=S(4)=5`: one root move from `A_4` yields `P = (\{x<y\} ⊔ A_2)` on 4
   elements, with 12 linear extensions and `F(P)=4` (compare the other two
   elements: obtain two disjoint chains `x<y, u<v`, 6 extensions, merge in 3 more;
   total 4; information bound `ceil(log2 12)=4`). This subproblem is `G(P,4)` on
   `n=4`, not any `S(m)<=j` with `m<4`; an `L_U` oracle queried only at `m<4` can
   reveal `S(1)=0,S(2)=1,S(3)=3` but has no query for `F(P)`. This illustrates the
   obstruction; it is **not** claimed as an information-theoretic proof that
   `S(4)` is independent of `S(<4)` under all non-decompositional reductions.

## What this does **not** establish (honest limits)
- **[open]** I do **not** prove `L_U` is not (Turing) downward self-reducible in
  *every* possible poly-time sense, nor that no exotic reduction can compute
  `S(n)<=k` from oracle answers `S(m)<=j, m<n`. A full negative answer would be a
  strong structural/complexity result; the fixed sequence `S` means
  information-theoretic “`S(<n)` cannot determine `S(n)`” is not directly
  formalizable against the true oracle without an additional independence theorem.
- **[open]** I do **not** give an infinite family `(n_t,k_t)` forcing
  superpolynomially many `m_t<n_t` `L_U`-queries for *arbitrary* correct
  reductions (the falsifier’s strongest branch); that remains open.
- **[open]** I do **not** rule out downward reductions in **budget** `k` or in
  incomparable-pair count on the **general poset** game (those are real but query
  posets on `n` elements, outside `L_U`).
- No consequence `P!=PSPACE/NP!=PSPACE/P!=NP` is claimed; this is only a method
  obstruction consistent with `L_U ∈ PSPACE`.

## Mathematical finding (concise)
The proposed front’s mechanism is **disproved**: a locally checkable antichain-root
comparison decomposition cannot be a deterministic polynomial-time oracle
reduction to `SORT-BOUND-U` instances with `m<n`, because every root decomposition
step produces **general-poset** threshold subproblems on the **same `n` elements**
(`F(A_n+e^±)<=k-1`), while `L_U` contains only **antichain** thresholds
`S(m)=F(A_m)`. The comparison game is downward in budget/state, not in element
count. Any correct `m<n`-antichain-query reduction of this form would additionally
require an unprovided (and uncheckable-by-`L_U(m<n)`) sound/complete
general-poset→smaller-antichain transfer — i.e. an uncheckable optimal-branch/
successor-value selection not captured by polynomial-size `L_U(m<n)` transcripts.
The stronger claim that *no* `m<n` `L_U`-query reduction exists at all is **not**
established here.

## Other metadata

```json
{
  "finished_at": 1793866257.5821402,
  "started_at": 1793866034.3162062
}
```
