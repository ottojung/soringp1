# one-outcome-attainment-set-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

FCsfNCEIan7B5HBFoXvUy3-deposit

## exit_state

clearexit

## question

Wells-style one-outcome (single-successor) adversary search is reported to certify exact optimality at n=12 but to fail at n=13 and n=14. Is the set of n for which such a restricted adversary search attains the full minimax value S(n) finite, with a characterizable largest element, or are there infinitely many n beyond the small cases where it still attains S(n)?

## basis

Board #301 n=12 certificate audit (2026-11-20T14:28Z) cites Stober-Weiss arXiv:2206.05597 section 1 (one-outcome suffices at 12, not 13/14) and Peczarski 2012 section 3; docs/literature.md and docs/research-obstruction-next.md section 5 ground the model and the soundness-versus-completeness distinction.

## falsifier

Prove finiteness by showing one-outcome search is strictly below S(n) for every n at or above some explicit threshold, or exhibit an infinite family of larger n at which the restricted adversary attains S(n).

## implication

A characterization would be a structural theorem about when the two-branch minimax game collapses to a single adversary path, refining certificate-size understanding; it does not by itself yield a complexity-class separation for SORT-BOUND-U.

## finding_unverified

, for `S(n)>C(n)` the true refutation may require answering some comparison with a non-max-extension branch; MEOO attains such an `n` only if a max-extension choice remains a winning adversary move at every algorithm decision along the required certificate (a pathwise alignment, not guaranteed by `e` alone). This explains `12 ∈ A` vs `13..19 ∉ A` without asserting a general large-`n` law.

## Best current characterization (conditional) and exact obstruction

From (1)–(4): `A = E ∪ G` where `E := {n : S(n)=C(n)} ⊆ A` (all-`n`, proved above) and `G ⊆ {n : S(n)>C(n)}` are gap instances whose optimal adversary can be realized by max-extension responses (known: `12 ∈ G`; `13..19 ∉ G`).

- **Infinitude:** sufficient if `E` is infinite. (`E` infinite ⇒ `A` infinite.) Also possible in principle via infinite `G`, but no witness beyond `n=12` is known.
- **Finitude:** possible only if `E` is finite and `G` is finite. No finite characterization/largest element is supported: 12 is the largest *known* element of `G`, but not a largest element of `A` (20–22 exceed it), and no theorem bounds `A` above.
- **What remains open [open].** (i) Whether `S(n)=ceil(log2 n!)` holds infinitely often (hence whether `E` is infinite) is not settled by current results cited here. (ii) Whether any `n >= 23` with `S(n)>C(n)` admits an MEOO certificate (`G` infinite/nonempty beyond 12) is unknown. (iii) In particular `S(23)` is open in the cited literature baseline, so membership of 23 is undetermined here.

**Conclusion (honest, checkable):** Under the MEOO formalization matching the cited Wells/Peczarski behavior, the set is **not** finite with largest element 12 and **not** confined to the small cases (refuted by `20,21,22 ∈ A` via the all-`n` ITLB theorem). A complete dichotomy “finite with a characterizable largest element” vs “infinite beyond small cases” **cannot be resolved from established results**: infinitude is implied by the open condition that the information bound is tight infinitely often, while finiteness would require eventual non-tightness *and* eventual failure of max-extension certification on all gap instances—neither proved nor disproved here. I did not find (and do not claim) a proof of finiteness, an explicit threshold, or an infinite family of large-`n` MEOO gap-attainments.

## Concrete failed/insufficient approaches considered
- **Pure threshold-by-known-values / “largest is 12”**: failed immediately on `20,21,22` once the all-`n` ITLB/MEOO argument is applied.
- **Ascribing success/failure solely to `S(n)>C(n)`**: failed both ways (`12` succeeds, `13–19` fail).
- **Deriving an all-large-`n` failure from local `F`-vs-`e` non-monotonicity alone**: insufficient—local structural inversions exist (Peczarski/obstruction), but turning them into an all-`n` (or all sufficiently large gap-`n`) obstruction for the *specific* max-extension paths induced from the antichain would require a global root strategy argument not available here.
- **Settling infinitude without resolving `{n:S(n)=C(n)}`**: blocked; `E ⊆ A` makes the equality set decisive in one direction.

**Complexity implication (as requested):** a characterization of `A` would be a structural theorem about when the two-branch minimax/adversary game collapses to the single (max-extension) successor path (refining certificate/search understanding); by itself it yields no separation for `SORT-BOUND-U` and does not change the unary `PSPACE` upper-bound / tally barrier context (`docs/problem.md`).

## Other metadata

```json
{
  "finished_at": 1795192178.5350666,
  "started_at": 1795191193.5484939
}
```
