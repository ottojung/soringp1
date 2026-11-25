# optimal-path-forced-e-gap-family

## status

investigated

## origin

ai_proposal_unverified

## agent_id

EiFlpgWn6gGISijrtvUOpm-metivier

## exit_state

clearexit

## question

Is there an explicit infinite family of posets P_{n,d} reachable from A_n within S(n) comparisons along every optimal sorter strategy for those n, such that F(P_{n,d}) - ceil(log2 e(P_{n,d})) >= 1 uniformly, yielding a root-forced local information gap?

## basis

research-obstruction-next.md shows local gaps exist (smallest e=8, merge families) but states local failures do not imply global/root gaps; quantified-root-adversary-proof found no all-n root-forcing invariant bridging hard reachable posets to every sorter.

## falsifier

Prove that every poset P with F(P) > ceil(log2 e(P)) can be avoided by some S(n)-optimal root strategy for all relevant n, or produce the required unavoidable family with a rigorous reachability-and-gap argument.

## implication

An unavoidable gap family would identify a structural source of the global S(n) > ceil(log2 n!) phenomenon and give a sound local obstruction invariant for exact lower bounds; avoidance would show local gaps are not adversarially forcible from the root.

## finding_unverified

e root instances: `{A_n : n in {12,16,17,18}}` (gap 1), from cited literature. `[literature]`
- An **infinite, proved** explicit family `P_{n,d}` with uniform forced gap is **open**: it would require either infinitely many proved `S(n)>C(n)` instances placed into a forced-gap form, or a structural argument forcing a gapped descendant for all large `n`. Neither is available here. The merge family gives unbounded *local* gap `F(P)-L0(P)` on two-chain posets (`M(m,m)-ceil(log2 C(2m,m)) -> +∞`, `research-obstruction-next.md` §6), but those posets are **not shown** reachable/forced from `A_n` along every `S(n)`-optimal strategy; general-poset/local-poset hardness does not transfer without a reduction (`AGENTS.md`).

## Complexity implication (careful)
- **Soundness of local obstruction invariant:** `gap(P)>=1` (equivalently `L0(P)>=d+1 => F(P)>=d+1`) is a sound lower-bound/cut invariant for the poset minimax; this is standard/used in the project (`F>=L0`). `[deduction]`
- **Forcibility from root:** only established here as root-forcing in the trivial sense when `S(n)>C(n)`; not as a new structural invariant explaining/forcing the global gap for an infinite family. Avoidance by an optimal sorter is possible in all checked tight cases (`n<=6`), so local gaps are **not** generically adversarially forcible. `[experiment]`
- **Uniform complexity of exact unary `S(n)`/`SORT-BOUND-U`:** no consequence proved. A comparison/poset obstruction does not separate computation classes for `S(n)`; `SORT-BOUND-U ∈ PSPACE` remains the relevant ceiling and `P != PSPACE`-equivalent barriers apply (`AGENTS.md`, `problem.md`). I make **no** NP/coNP/P claim.

## Exact obstruction / why no “genuinely substantive” new theorem here
1. **Root triviality:** whenever `S(n)>C(n)` the front’s condition is met already by `A_n`; any nontrivial theorem must force a *descendant* or give an infinite structural family — neither proved.
2. **Avoidance in tight cases:** optimal strategies can route around all local-gap states for `n<=6, S=C` (exact check), blocking a universal “gaps are root-forced” narrative.
3. **No reduction from general/local gap to `S(n)`:** large merge/local gaps exist, but reachability under *every* optimal antichain strategy is the missing all-`n` bridge (and generic poset hardness is out of scope).
4. **Data limit:** exact `S(n)>C(n)` is known only at scattered `n` (12,16,17,18,… as above); not an explicit infinite proved family.

## Honest limits
- I did not compute `n=7+` optimal-strategy avoidance (state space/cost); the `n<=6` result is small but exact and directly discriminating for tight cases.
- I did not reproduce Stober–Weiß/Wells searches; I relied on cited literature values.
- I found no repo/branch artifact adding a theorem beyond existing notes; `quantified-root-adversary-proof` worktree has no relevant changes. No Lean/repository changes were made (no independently checkable new all-`n` theorem emerged).
- Distinguish clearly: **sound local invariant** ≠ **completeness/forcibility**; **poset gap** ≠ **complexity-class separation** for computing `S(n)`.

**Summary (one line):** literal “unavoidable local gap” holds trivially at the root for known `S(n)>C(n)` values (so strong global avoidance is false there) but is non-explanatory; in checked tight cases `n<=6` an optimal strategy avoids *all* gapped descendants, and no rigorous explicit infinite forced descendant-gap family (hence no new structural all-`n` obstruction theorem) was obtained.

## Other metadata

```json
{
  "finished_at": 1793877617.707042,
  "started_at": 1793877209.8531525
}
```
