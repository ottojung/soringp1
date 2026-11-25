# split-completion-coupling-penalty-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

edtwmbSgBGHxoyOrAFq5pY-deemed

## exit_state

clearexit

## question

For the split-schema completion cost C(m,n) - the exact minimax number of further comparisons needed to sort n keys given a known sorted m-subset - is the coupling penalty pi(m,n)=C(m,n)-ceil(log2(n!/m!)) uniformly at most 1 for every 1<=m<n and all n, or does pi grow without bound on some infinite family of splits? This is the residual quantity left open by the newest split-schema phase-coupling publication.

## basis

Newest board #301 / origin/main publication 2026-11-20 (docs/research-fo-tc-split-schema.md, commit 9018729) defines C(m,n); my independent scratch minimax observes pi in {0,1} on all cells through n=8 plus (2,9), all-n status open; this quantity is distinct from the investigated two-phase miss-mass tau(n) and split-merge gap fronts.

## falsifier

Compute C(m,n) exactly for larger cells (exhaustive minimax over rank-tuple knowledge states, every legal splitting pair tried) and exhibit any pair (m,n) with pi(m,n)>=2; alternatively derive a general argument that pi(m,n)<=1 for all m<n.

## implication

A uniform pi<=1 bound would show the phase-coupling tax on the natural compositional FO(TC)/ESP split compiler is at most one comparison for every split and every n; pi unbounded would strengthen the barrier excluding fixed-split compositional exact programs for SORT-BOUND-U.

## finding_unverified

tober–Weiß 2023) the gap `S(n)-⌈log2(n!)⌉` is 0 or 1 (first 1 at `n=12`). Hence a **uniform proof** of `π(m,n) <= 1` would settle (in the affirmative direction, as a strong bound) a long-standing open behavior of `S(n)` itself — far beyond what is currently reachable. This is an obstruction to the “derive `π<=1` for all m<n” horn, independent of implementation.
3. **General-poset vs this family [model fidelity].** For arbitrary finite posets, `sort(P) >= ⌈log2 e(P)⌉` but balancing/overhead phenomena (Fredman; Kahn–Saks; 1/3–2/3 / 11/40-type balancing, Kahn–Kim et al.) concern general `P`; such results do not automatically yield either a uniform +1 bound or a +2 example for the specific structured family `P_{m,n}` (chain plus `r=n-m` free elements). No general-poset fact was used here as a claim about `C(m,n)` without a reduction.
4. **Soundness vs completeness (route-level).** `π(m,n)>=1` on a cell is a sound witness that the information price is not achievable for that split completion (a concrete coupling penalty, extending 9018729). Conversely, `π(m,n)=0` on tested cells is only existence of an optimal-height completion for those instances (and of the counting-feasible split where applicable), **not** completeness of any fixed compositional FO(TC)/ESP schema for all `n`, and not a proof that `π` stays ≤1.
5. **No new theorem.** I did **not** prove `π(m,n) <= 1` for all `m<n`, did **not** find a counterexample `π(m,n) >= 2`, and did **not** resolve any `S(n)`/`SORT-BOUND-U`/class-membership question. The front remains open.

## Failed approaches and exact obstructions
- **Exhaustive exact falsification at larger `n` [failed/incomplete approach].** Exact `C(m,n)` is minimax over all comparison decision trees on `L(m,n)=n!/m!` extensions. Even with symmetry-aware canonicalization and pruning, feasible exact search (in my implementations, on this host) reached ~`10^4`–`2*10^4` extensions comfortably and stalled/was interrupted beyond (naive full-permutation initialization also made `n>=14` cases fail in v1/v2). Cells left **uncomputed/uncertain** here include `10,14` (`24024`), `11,15` (`32760`) and larger `n` — precisely where a first `π>=2`, if it exists, might appear; I cannot claim their values.
- **Deriving a uniform `π<=1` bound [obstruction].** Any all-`n` proof must in particular bound `π(1,n)=S(n)-⌈log2(n!)⌉ <= 1` (point 2 above), which is an open global problem. A proof specialized to `m>=2` would need a structural argument on `P_{m,n}` strong enough to preclude a two-comparison information loss accumulating over all splits and all `n`; I identified no such argument, and none follows from the computed cells.
- **What would be decisive next:** an exact `π(m,n)>=2` certificate on any feasible larger cell (with independent replay/lower-bound verification, as in 9018729), or a genuine structural theorem bounding the coupling penalty for the `P_{m,n}` family (carefully separated from general-poset heuristics) — neither achieved.

## Bottom line
- **Falsifier:** not found. On every cell I computed exactly and independently verified against published data (table above), `π(m,n) ∈ {0,1}`.
- **All-`n` status:** **open**. Uniform `π<=1` is unrefuted but unproved and would imply the strong open corollary `S(n) <= ⌈log2(n!)⌉+1`; a counterexample, if any, lies beyond the exactly searched range.
- **Limits:** computational evidence only; no kernel-checked result; no claim of process success as proof; no repo/board/Lean/external side effects.

## Other metadata

```json
{
  "finished_at": 1795146085.5558007,
  "started_at": 1795143776.053183
}
```
