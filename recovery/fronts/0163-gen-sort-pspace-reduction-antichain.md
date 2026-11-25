# gen-sort-pspace-reduction-antichain

## status

investigated

## origin

ai_proposal_unverified

## agent_id

sckgjr5WYxeC28H4IexNXf-acting

## exit_state

clearexit

## question

Can GEN-SORT (sorting number for an arbitrary given poset) be reduced by a polynomial-time encoding-preserving reduction to SORT-BOUND-U (antichain case S(n)<=k) for some function of n,k and poset size, or is such a transfer provably impossible for all all-n families while respecting the unary encoding and model restrictions?

## basis

GEN-SORT listed as PSPACE-complete/open in research-hardness-boundaries.md; AGENTS states hardness of arbitrary posets does not transfer to S(n) without reduction; sparsity differs between unary antichain and arbitrary-poset encodings.

## falsifier

Construct an explicit polynomial encoding from GEN-SORT instances to (n,k) in unary with correctness for all instances, or give a general theorem showing the fixed symmetric comparison set of the antichain blocks any such reduction while GEN-SORT remains PSPACE-hard.

## implication

A positive reduction would make SORT-BOUND-U PSPACE-hard (hence PSPACE-complete given known membership), linking P!=PSPACE to the antichain sorting number; a general obstruction would sharpen the 'hardness does not transfer' boundary without assuming P!=PSPACE.

## finding_unverified

ynomial-time encoding-preserving reduction to SORT-BOUND-U... for some function of n,k and poset size". Reading that restriction literally: the target antichain parameters are
$$
n' = f(n_{in}, k_{in}, |P|),\quad k' = g(n_{in}, k_{in}, |P|)
$$
i.e. they may depend on the input size parameters and on the size of the poset $P$, but **not on the internal structure of $P$** (only on $|P|$). The encoding is preserved as unary (the form of $SORT-BOUND-U$).

This creates a decisive combinatorial obstruction:
- For fixed $n=|P|$ and fixed $k_{in}$, take two posets on $n$ elements: a chain $C_n$ ($S(C_n)=0$) and the antichain $A_n$ ($S(A_n)=S(n)$). Choose $k_{in}$ with $0 < k_{in} < S(n)$ (possible for large $n$).
- The reduction produces the same $(n',k') = (f(n,k_{in},n), g(n,k_{in},n))$ for both instances.
- Correctness requires $S(C_n)<=k_{in} \iff S(n')<=k'$ and $S(A_n)<=k_{in} \iff S(n')<=k'$. But left sides have different truth values while right side is identical. Contradiction.

The "fixed symmetric comparison set of the antichain" is exactly this: an antichain's sorting complexity is a function of its size only ($S(n')$), with full $S_{n'}$ symmetry and no partial-order constraints to encode; arbitrary posets of the same size have different $S(P)$ values depending on structure. No polynomial-time computation over the full matrix encoding can help if the target parameters are forbidden from depending on that structure - the restriction is the blocker.

## Failed approaches / limits
- **Instance-wise case analysis on full $P$**: possible combinatorially if $(n',k')$ may depend on the entire encoding of $P$, but that violates "function of n,k and poset size" (uses structure). The problem states that restriction explicitly, so we must respect it.
- **Using information bounds / $e(P)$**: $e(P)$ varies, but again to choose $(n',k')$ you'd need to encode $e(P)$; with only size dependence impossible. Also approximation doesn't give exact threshold equivalence for all instances under this restriction.
- **Sparsity/density of languages**: non-injective reductions break the naive census argument; the clean obstruction here is structural/parameter dependence, not the Mahaney density count.
- **Class completeness**: if arbitrary polynomial-time reductions were allowed, PSPACE-completeness would make reduction trivial by class theory - but that contradicts the "encoding-preserving... for some function of n,k and poset size" restriction which is clearly a stronger/combinatorial constraint on the reduction form.

## Concrete finding
Under the stated restriction (target antichain parameters depend only on input parameters and $|P|$), such a reduction is **provably impossible for all $n$-families**. The obstruction is the loss of poset-structure information: the antichain is size-determined and symmetric while $S(P)$ separates chains from antichains of equal size. This is a model-level obstruction (certificate/soundness-completeness boundary for this restricted reduction class), not something resolved by complexity-class collapses.

## Recommendation
Do not try to construct such an encoding. The falsifier's "general theorem showing the fixed symmetric comparison set of the antichain blocks any such reduction" is satisfied by the parameter-dependence argument above. Any future attempt must first clarify whether $(n',k')$ are allowed to depend on the full structure of $P$ - if not, the question is already settled negatively by this symmetry/size argument.

## Other metadata

```json
{
  "finished_at": 1793562258.552751,
  "started_at": 1793561674.5064244
}
```
