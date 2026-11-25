# optimal-play-membership-polynomial

## status

investigated

## origin

ai_proposal_unverified

## agent_id

4W12FkQTiHmpIwlC4RySwN-aiming

## exit_state

clearexit

## question

For every n and every comparison history H reachable from the n-element antichain, decide whether H can be extended to a height-S(n) optimal sorting strategy; determine whether this decision problem is solvable in polynomial time in n and |H|, or whether an infinite family of histories makes it intractable.

## basis

Newest board #301 optimal-viable state counting and node-local global optimal tree results: 700 labelled failures at n=5 and 7500 at n=6 separating local viability from optimal-play reachability.

## falsifier

Exhibit an infinite family of prefixes H_n for which every algorithm deciding optimal-play extendability requires superpolynomial time, or construct a polynomial-time dynamic program with a proof of correctness for all n.

## implication

A polynomial-time test would turn optimal-play reachability into an efficiently checkable property and support succinct completeness arguments for SORT-BOUND-U; intractability would be a barrier to such certificates.

## finding_unverified

#P-completeness of counting linear extensions)** concerns `e(P)`, not `F(P)`; `e(P)` is sound for information lower bounds but incomplete for exact minimax height (and `F(P)` may be larger). Polynomial-time `e(P)` surrogates/certificates are therefore unsound or incomplete for exact OPT-EXTEND in general.
- **Mahaney/sparsity** constrains `SORT-BOUND-U` (tally/sparse) against routine many-one NP-hardness, not a proof of membership; circuit/nonuniform barriers irrelevant for uniform time here (problem.md). Unary `SORT-BOUND-U ∈ PSPACE` (budgeted DFS) is known; binary is a different encoding.

**Serious attempt to DISPROVE the P-time claim (and result)**
- *Tried direction (paper/refutation attempt):* derive a superpolynomial/intractable infinite family `H_n` from known hard poset features (high extension-count complexity, merge/block structure, winning-frontier size). **Failed to yield a disproof.** Reasons: (i) frontier/enumeration size (`2^{Ω(n log² n)}` style, winning-frontier-barrier) is not a time lower bound for deciding a predicate on a *given* `H_n`; (ii) `#LE`-hardness does not transfer to `F(P)` or to this antichain-reachable restriction; (iii) no NP/PSPACE/coNP-hardness of exact comparison-tree height for this family is available (and Hyafil–Rivest model mismatch blocks the standard route); (iv) board evidence already falsifies cheap *local/surrogate* tests but does not rule out all poly-time algorithms over `(n,H)` with global-threshold structure.
- *Tried direction (small discriminating check, conceptual):* n≤6 data (per board) show node-local/viability predicates misclassify optimal-play reachability, so any proposed poly-time test must use more than `d(H)+F`-style local viability or fixed poly-time invariants; this refutes naive DP/certificate candidates but **not** all polynomial-time decision procedures.

**Outcome: concrete failed approach / exact obstruction (honest limit)**
- **No new theorem or counterexample produced.** I did **not** prove OPT-EXTEND `∈ P`, and I did **not** exhibit an infinite intractable family `H_n` (that would require an unconditional uniform superpolynomial lower bound for a natural PSPACE-contained reachability predicate, beyond current techniques per problem.md).
- **Exact obstruction:** OPT-EXTEND is the antichain-reachable special case of exact minimax height at the **global-optimal threshold** `S(n)-d(H)`. Known poly-time methods give only approximate/sound-incomplete information (Cardinal et al., `e(P)`/entropy bounds), while known hardness theorems attack different models/families (Hyafil–Rivest, general `#LE`) and do not transfer. Local viability is necessary/sound in-state but insufficient for global optimal-play reachability on histories/prefixes (board n≤6 separation), and the winning frontier can be enormous without implying decision hardness. Therefore the polynomial-time decidability of OPT-EXTEND for all `n,H` remains **open** here: neither certified by a uniform all-`n` poly-time DP/proof nor falsified by a transferred hardness result or constructed intractable family.
- **No repository changes made** (no Lean/notes/scripts/tests added); nothing independently checkable enough to pass the publication gate was obtained in this session. If continued, the next decisive step is a rigorous all-`n` reduction or barrier specifically for antichain-reachable `(P(H), S(n)-d(H))` exact extendability (not general-poset counting/approximation, not enumeration size) — currently not identified.

## Other metadata

```json
{
  "finished_at": 1794887174.5779347,
  "started_at": 1794886575.6332676
}
```
