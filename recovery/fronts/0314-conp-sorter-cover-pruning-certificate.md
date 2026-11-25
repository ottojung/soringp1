# conp-sorter-cover-pruning-certificate

## status

investigated

## origin

ai_proposal_unverified

## agent_id

hmeaFP3A4yMjAnNV20Qkfn-reflected

## exit_state

clearexit

## question

For all n,k with S(n) > k, is there a polynomial-size (in n+k) certificate that covers every root sorter strategy by locally polynomial-time checkable height-k pruning/refutation annotations, establishing SORT-BOUND-U membership in coNP via a strategy-covering dual?

## basis

SORT-BOUND-U is the complement-threshold of a bounded minimax game (SORT-BOUND-U in PSPACE, problem.md); dual/refutation certificates differ from existential sorter-strategy witnesses and from single adversary-invariant fronts (alln-adversary-universal-certificate, co-np-refuter-local-invariant-completeness).

## falsifier

Exhibit an explicit infinite family (n, k_n) with S(n) > k_n and prove a superpolynomial lower bound on total size for any sound certificate of this locally-checkable strategy-covering form; or show a fixed local annotation scheme is unsound (accepts some S(n)<=k_n) or incomplete on a concrete all-n extendable family.

## implication

A sound, complete, polynomial-size strategy-covering pruning certificate would place SORT-BOUND-U in coNP; an unconditional-in-form superpolynomial size barrier for a precise local calculus would constrain coNP-membership approaches by dual strategy covers (certificate soundness must be distinguished from completeness).

## finding_unverified

uction from literature values].** For `n=12,k=29`, `S(12)=30>29` (Wells/Peczarski line; see `docs/literature.md`), while `I(12)=ceil(log2 12!)=29`, so `12! ≈ 4.79e8 < 2^29 ≈ 5.37e8`. Hence at root `(antichain_12,29)`, `e(root)=12! <= 2^29`: **neither `e(P)>2^d` nor any antichain-factorial bound of the same magnitude can fire at root**. The same near-boundary phenomenon occurs at every known gap-1 instance `n∈{12..19}` where `S(n)=I(n)+1` (`docs/literature.md` values: 12→30/29,13→34/33,14→38/37,15→42/41,16→46/45,17→50/49,18→54/53,19→58/57). Therefore any sound SCR calculus whose prunes are only root/ancestor information bounds of this strength **must** use Cover below the root on these known NO instances; it cannot compress them to a one-step local prune.

## 3. Why this is not a falsifier of the FRONT
This does **not** prove a superpolynomial lower bound for SCR, nor for “any sound certificate of this locally-checkable strategy-covering form”:
1. **No explicit infinite NO family available.** Exhibiting `(n,k_n)` with `S(n)>k_n` for infinitely many explicit `n` requires knowing `S(n)` (open in general; `S(n)-log2(n!)` infinitely often ≥1 is open). So I cannot construct the requested infinite falsifying family.
2. **Richer local calculi remain open.** A stronger poly-checkable `L` (poset invariants, monotone potential-function witnesses, proof-complexity-style local rules stronger than raw extension counting but still poly-checkable) is not ruled out by the width/info-root obstruction.
3. **Unsoundness not found.** No fixed natural local annotation scheme examined here was shown unsound (accepting some `S(n)<=k_n`); Base/Cover/valid prunes are sound.
4. **Completeness (poly-size) remains open.** The calculus is complete in principle only at exponential size.

## 4. Complexity consequence (careful)
- A sound, **complete**, polynomial-size, polynomial-time checkable strategy-covering refutation system for all NO instances would place `SORT-BOUND-U ∈ coNP` [deduction]. This would be a major certificate result (still far below any separation claim; `P vs coNP` implications for this tally-like setting need the usual care).
- The obstruction shows **certificate soundness must be distinguished from poly-size completeness**, and shows the natural extension-count local prune is either non-poly-checkable or exponential-size and fails at the root on known hard gap instances. It is a **constraint on coNP-via-dual-strategy-covers approaches using only such prunes**, not an unconditional barrier for all local calculi.

## 5. Primary sources / anchors
`docs/problem.md` (model, `G(n,k)`, `SORT-BOUND-U`, realistic outcomes), `docs/research-certificates-barriers.md` (game/`APTIME` view, no succinct cert known), `docs/research-budget-pruning.md` (info cutoff `e(P)>2^d` sound; poly-space via capped enumeration but not a poly-size/checkable-from-P-alone certificate), `docs/literature.md` (exact `S(n)`, gaps, Wells/Peczarski/Stober–Weiß). Brightwell–Winkler (counting linear extensions #P-complete) is the standard reason exact `e(P)` witnesses are problematic [literature].

**Limits:** no Lean/repo changes made (no substantive new kernel-checkable theorem established here). No infinite family constructed, no superpolynomial lower bound proved, no unsound scheme found. The honest status is an exact obstruction to the obvious local-prune route on known non-tight instances, with poly-size strategy-covering `coNP` certificates for exact unary `S(n)` remaining open.

## Other metadata

```json
{
  "finished_at": 1793872925.089009,
  "started_at": 1793872540.890646
}
```
