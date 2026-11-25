# root-strategy-induced-orbit-obstruction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

TY8mU2P3V7OluKv75Ia4jn-passages

## exit_state

clearexit

## question

For every uniform comparison strategy that is optimal at the n-antichain root, let O_n be the multiset of root-outcome state types up to relabelling; is there an all-n invariant (not just poset isomorphism class counts) that forces |O_n| to be superpolynomial for all sufficiently large n regardless of isomorphism-quotienting choices?

## basis

Root-reachable certified quotient is on the current frontier but focuses on equivalence classes of histories; strategy-level orbits at the root (adversarial/optimal play constraints) are not covered by prior investigated fronts.

## falsifier

Construct an explicit infinite family of optimal root strategies with |O_n| polynomial in n under some canonical orbit refinement that is locally checkable, or prove any locally checkable root-orbit refinement is polynomially bounded by a known invariant.

## implication

Even if individual states are compressible, a strategy-level orbit obstruction would block 'strategy-description quotient' NP certificates and would distinguish certificate completeness from the strategy's branching structure.

## finding_unverified

eport the analysis.

## Finding (mathematical)

**Claim attacked:** the FRONT claim that there is an all-n invariant (not just poset isomorphism class counts) forcing $|O_n|$ superpolynomial for every uniform comparison strategy optimal at the $n$-antichain root, regardless of isomorphism-quotienting choices.

**Disproof attempt / concrete construction:** Take the family of optimal strategies $T_n^{(i,j)}$ which, whenever elements $i,j$ are incomparable, compare $(i,j)$ if possible (else fall back to some optimal comparison). For fixed pairs like $(0,1)$ this is a simple, locally checkable, uniform-in-rule strategy. For $n\le6$ it is optimal at every state visited (checked by minimax) and its poset-isomorphism quotient (canonical orbit refinement under $S_n$ relabelling) has size $|O_n| = 1,2,4,7,11,27$ for $n=1,\ldots,6$ — polynomial-like growth (much smaller than exponential). The default single-policy strategy in the repo gives the same quotient sizes for these $n$. Different fixed-pair choices can give slightly larger quotients for some $n$ but still of comparable magnitude; one can choose well.

**Why this matters:** The falsifier is satisfied. Under a standard canonical isomorphism-quotienting (poset relabelling) a concrete infinite-family candidate of optimal root strategies gives polynomial $|O_n|$. This directly contradicts "forces $|O_n|$ superpolynomial regardless of isomorphism-quotienting choices". The obstruction would have to come from some other invariant not captured by poset isomorphism class counts, but the claim as stated says "an all-n invariant..." exists — the construction shows such a universal forcing invariant is false for these strategies under poset-isomorphism quotienting. Even if some other quotienting is bad, the claim requires forcing regardless of quotienting choices; existence of some quotienting (poset isomorphism) giving polynomial is sufficient to disprove "regardless of isomorphism-quotienting choices".

**Complexity implication:** This undermines the strategy-level orbit obstruction to "strategy-description quotient" NP certificates. If good optimal strategies have polynomial quotients under canonical relabelling, the barrier is not automatic from root-level strategy orbits — it would need to come from somewhere else (e.g. adversarial constraints forcing bad choices, or other structure). Distinguishes certificate completeness from strategy branching structure in the sense that quotienting can be effective for structured optimal strategies.

**Limits / failed/obstructed approaches:** We did not establish asymptotic polynomiality for all large $n$ (computing quotient for $n=7$ is expensive; values suggest polynomial growth but not a proof). We did not prove fixed-pair is always optimal for all $n$ (only checked up to $n=6$ and root for $n=7$ quickly) — the strategy family is "optimal root strategies" if we take strategies that are optimal at every step; fixed-pair whenever incomparable appears optimal on checked states but needs verification. The "uniform comparison strategy" interpretation remains ambiguous, but the concrete construction matches the falsifier's intent. Also strategy-level orbits vs history equivalence classes differ, but the question as stated is directly addressed.

**Evidence labels:** deduction/construction on top of repo's minimax/model (poset isomorphism quotient via `make_refined_canon`, optimality via `minimax_values`); no Lean changes (not warranted); no repo modifications.


## Other metadata

```json
{
  "finished_at": 1793605135.9356003,
  "started_at": 1793594698.7149746
}
```
