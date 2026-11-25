# recursive-branch-mass-exact-reset

## status

investigated

## origin

ai_proposal_unverified

## agent_id

A4BhWOLyjbP6o4n9rVljh7-stump

## exit_state

clearexit

## question

For the antichain root A_n, does global extension-count divisibility e(F') | n! together with root-outcome mass divisibility e(F') | (n!/2) suffice for some comparison tree to realize an exact framed reset to a fixed target F' for all n, or must some infinite family fail at a forced deeper node?

## basis

docs/research-exact-reset-realizability.md proves only root 2-adic obstruction (odd n, A_n->V_n) and states recursive comparison-induced masses are necessary but gives no sufficiency/characterization; antichain-split-coprime-obstruction covered root coprime factors only.

## falsifier

Construct an explicit all-n family (A_n, F'_n) with e(F'_n)| (n!/2) for which every adaptive comparison tree from A_n produces a reachable node whose consistent-extension mass is not an integer multiple of e(F'_n), or exhibit a realizing tree.

## implication

A recursive branch-mass obstruction would sharpen exact-reset realizability beyond root 2-adic conditions and constrain which boundary transitions any framed certificate can use; a sufficiency theorem would delimit the realizable certificate stage algebra.

## finding_unverified

rtition all `n!` orders. Thus the target partition is `{C_w : w∈[n]}`.

Take any first comparison `(x,y)` of `A_n`. Its outcomes are `B_{x<y}={σ:x<y}` and `B_{y<x}`, each of mass `n!/2`. For `w=x`, `C_x ⊆ B_{x<y}`. For `w=y`, `C_y ⊆ B_{y<x}`. For any `w ∉ {x,y}` and `n>=4`, by symmetry of `x,y` among the `n-1` elements after placing `w` first,
`|C_w ∩ B_{x<y}| = |C_w ∩ B_{y<x}| = (n-1)!/2 = e(V_n)/2`.
Hence `C_w` is split across the two root outcomes and is a subset of neither.

But any leaf below `B_{x<y}` is a subset of `B_{x<y}`. Since `0 < |C_w ∩ B_{x<y}| < |C_w|`, no leaf below `B_{x<y}` can equal `C_w`; similarly below `B_{y<x}`. Therefore, for `n>=4`, no `C_w` with `w ∉ {x,y}` can occur as any reachable leaf, contradicting the required partition. The argument uses only the exact-reset/leaf definition, balanced antichain comparisons, and symmetry; no height bound, isomorphic-subtree duplication, or external sorting theorem is used. ∎

**Mass-divisibility consequence (distinguishing the frontier’s falsifier).** The class-crossing obstruction is stronger than “some node has mass not a multiple of `e(F')`”. A comparison tree may keep all node masses multiples of `e(V_n)` while being non-realizing by declaring a non-certificate node of mass `e(V_n)` as a leaf (example, `n=4`, `e=6`: root `a,b` gives `12,12`; compare `c,d` below `a<b` gives `6,6`; `E={a<b,c<d}` has mass `6` but mixes minima `a,c`, so it is not any framed `Ext(V_4)`). However, any proper refinement of a mass-`e(F')` non-certificate node produces children of positive mass `< e(F')`, hence not multiples of `e(F')`. Therefore every comparison tree either has a reachable leaf whose extension set is not framed `Ext(V_n)` (non-realizing) or produces a reachable node with mass not divisible by `e(V_n)`. The pure mass-not-multiple property is **not** forced for all trees as static objects, but exact framed reset realizability is impossible for all trees.

**Small checks.** `n=2`: root gives `C_1,C_2`, realizable. `n=3` (odd): `n!/2=3` not divisible by `e=2` (root mass obstruction). `n=4,6`: root-outcome divisible (`12/6=2`, `360/120=3`) but class-crossing applies.

**Complexity implication.** Recursive branch-mass divisibility is necessary but not the whole realizability story: even when global and root-outcome masses are compatible, comparison-induced partitioning can make required framed certificate classes straddle branches, so realizable framed-certificate stage transitions are constrained beyond scalar mass conditions. This sharpens exact-reset realizability/certificate-stage algebra (relevant to what framed certificates can certify) but, as in the prior note, is **not** a lower bound on `S(n)`, not a constraint on non-exact/forgetful certificates, and does not by itself yield a uniform complexity separation for `SORT-BOUND-U`.

**Limits / honesty.** I did not produce an infinite family satisfying the frontier’s literal “every adaptive tree has a mass-not-multiple node” condition under both divisibility preconditions except in the refinement sense above; constructing such a family or proving realizability in non-crossing mass-compatible cases remains open. I also did not characterize all realizable `(A_n,F'_n)` transitions. No primary external theorem beyond elementary symmetry/counting of linear extensions was needed; the result is a direct consequence of the exact framed-reset definition (cf. `docs/research-exact-reset-realizability.md`). No repository/Lean changes made.

## Other metadata

```json
{
  "finished_at": 1793877899.864682,
  "started_at": 1793877209.4661648
}
```
