# antichain-pspace-completeness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

MwpjR8UVULNFWV15ulQhoD-edit

## exit_state

clearexit

## question

Is SORT-BOUND-U PSPACE-complete under polynomial-time many-one reductions for the exact adaptive comparison game on the antichain?

## basis

SORT-BOUND-U in PSPACE by ATM/alternation (research-certificates-barriers), but no primary source claims PSPACE-hardness for the antichain S(n); general-poset PSPACE-completeness is not established and does not transfer.

## falsifier

Show SORT-BOUND-U is not PSPACE-hard by exhibiting a complexity collapse obstruction for this sparse unary game, or place it in a strictly smaller class with a uniform algorithm for all n.

## implication

PSPACE-completeness would fix SORT-BOUND-U's exact class (distinct from NP/EXPTIME by the barriers) and clarify the APTIME equivalence; non-hardness would show the antichain is easier than general poset games.

## finding_unverified

ounds when `(n,k)` is unary-encoded (input length `m=n+k+1`, `O(k n^2)=poly(m)`). This is exactly Claim A in `research-certificates-barriers.md`. Unary threshold <=> function value via binary search.

### Obstructions to many-one PSPACE-hardness (unary)
- **Sparsity** (Claim B, Mahaney): `SORT-BOUND-U` is sparse in unary encoding (`O(m^2)` yes-instances of length ≤m). `P/poly` contains every sparse language. `P/poly` is closed under polynomial-time many-one reductions.
- **Collapse consequence**: If `SORT-BOUND-U` were PSPACE-hard under polynomial-time *many-one* reductions, then `PSPACE ⊆ P/poly`. `PSPACE ⊆ P/poly` implies major polynomial-hierarchy collapses (e.g. to `MA` and stronger consequences in the Karp–Lipton/`IP=PSPACE` circuit-size literature). This is a standard complexity collapse obstruction analogous in spirit to Mahaney's theorem (sparse NP-hard many-one => `P=NP`), though the exact collapse is different for PSPACE.
- **Model separation**: General poset minimax/strategy problems are not known to be PSPACE-complete for the *antichain* (sorting) instance family; Parberry's coNP-completeness is for fixed networks (different quantifier structure), Hyafil–Rivest/Laber–Nogueira are for arbitrary tests. None transfer to `S(n)`. No primary source claims PSPACE-hardness for the antichain.

### Certificate soundness vs completeness (important)
- **Soundness**: A PSPACE “certificate” in the alternating sense is the strategy (a tree of existential choices against universal adversary) — its *existence* is what the ATM verifies.
- **Completeness/witness size**: An explicit tree witness need not be polynomial-sized (Claim C) — `n!` leaves; for unary-informative inputs size exponential in `m`. Verifiability of an explicit tree is polynomial in *its own* size, not obviously giving a polynomial-time many-one reduction from arbitrary PSPACE languages without also providing a succinct witness or a direct reduction preserving the antichain structure. The sparsity barrier hits many-one completeness directly regardless of how certificates are described.

### What this shows (and does not)
- **Falsifier status**: Many-one PSPACE-hardness is obstructed by sparsity + `P/poly` closure forcing `PSPACE ⊆ P/poly`. This is a concrete complexity obstruction, not a hand-wavy “probably not”. 
- **Honest limits**: I cannot unconditionally *prove* `SORT-BOUND-U ∉ PSPACE-hard_{m-reductions}` from axioms alone — it would follow if we assume `PSPACE ⊈ P/poly` (a widely believed separation) or if we derive an even stronger collapse. Also Turing reductions are a different matter (Ogiwara–Watanabe is the NP case). No uniform polynomial-time algorithm for all `n` is known; placing in strictly smaller class than PSPACE remains open.
- **No transfer**: The large winning frontier (barrier note) rules out enumerating all winning states, but enumeration is not required for a selective/alternating algorithm — so that barrier doesn't block PSPACE membership or doesn't by itself force non-hardness; the sparsity+P/poly obstruction is the relevant one here.

**Bottom line:** `SORT-BOUND-U ∈ PSPACE`. Under polynomial-time many-one reductions, PSPACE-hardness is obstructed by sparsity (=> `PSPACE ⊆ P/poly`), which is a standard collapse obstruction with no known primary reduction for the antichain. No unconditional disproof, no known smaller class; the question reduces to circuit complexity/collapse assumptions rather than a direct combinatorial transfer from general posets.

## Other metadata

```json
{
  "finished_at": 1793503670.730735,
  "started_at": 1793503391.4434547
}
```
