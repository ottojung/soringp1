# join-reduced-compression-size-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ADtFxrccLdWWb3MEkWHDec-skill

## exit_state

clearexit

## question

For every n and every optimal height-S(n) comparison strategy, can it be transformed by repeatedly replacing a mergeable pair (F(P)=F(Q)=F(P&Q)) with its meet and rebuilding affected subtrees into a join-reduced optimal strategy whose number of reachable states is at most the original? Finite scratch checks at n=5,6 found join-reduced optima but say nothing about size-preserving compression from an arbitrary optimum.

## basis

Freshest #301 confluence result (19:07Z) showed greedy merging is not confluent at n=5,6,7 while leaving canonical-strategy existence open; independent scratch computation found join-reduced optima at n=5 (239 states) and n=6 (1439 states), and no repo, Lean, or board changes were made.

## falsifier

Exhibit, or show must exist for infinitely many n, an optimal strategy whose every compression sequence either fails to reach a join-reduced form or strictly increases reachable-state count, checked by exact minimax enumeration.

## implication

A yes answer makes canonicalization a sound size-preserving preprocessing step, so the polynomial-size framed-DAG / NP-certificate route collapses to its join-reduced special case; a no answer turns non-confluence into a genuine state-count blowup barrier for exact S(n) certificates.

## finding_unverified

ed on **both** outcomes (`max` equality with componentwise ≥ forces equality on both). Even then children may be different posets (`R`’s children ⊆ `P`’s children, possibly strict), as in the `n=6` example, and can expand the distinct-state closure.
- **Relation to non-confluence:** non-transitivity means you cannot canonically collapse all pairwise-lossless states into one `F`-preserving representative (and a set `{P1,P3}` with `P1 !~ P3` can already be join-reduced). The size question is different: can one always *choose* a merge/rebuild sequence that reaches some join-reduced strategy without increasing count? The `n=6` strict pair shows at least some merge choices/steps are locally increasing.

# Assessment against the falsifier

- **Established:** a concrete, exact finite obstruction to the **size-preserving meet-replacement step** on antichain-reachable tight states: at `n=6` strict mergeable pairs exist and a specific pair (above) yields a strict reachable-state increase (`97 → 107`, robust over all top-level optimal choices at `P,Q` under canonical-below evaluation). At `n=5` no such step-level blowup occurs (all subset-type).
- **Not established (open):** a full falsifier “for infinitely many `n`, an optimal strategy whose **every** compression sequence either fails to reach a join-reduced form or strictly increases reachable-state count.” I did **not** enumerate all optimal strategies, all global choice combinations below children, all merge orders, nor prove an infinite family. A strategy might avoid this pair, use different below-choices changing unions, or follow a different merge order (noting non-confluence constrains but does not by itself settle global size monotonicity). Existence of *some* join-reduced optimum at `n=5,6` (basis) remains consistent with this local obstruction.
- **Limits:** finite `n=5,6` exact checks; canonical-choice DAG accounting for subtree unions (not a proof about all global sharings/strategies); no all-`n` theorem or counterexample family; no Lean, no complexity separation (`SORT-BOUND-U`/`S(n)` status unchanged).

# Failed / incomplete approaches

- Full `n=6` pairwise classification over all tight levels was too slow naively in one pass (level `F=5` has 14100 states, `F=4` 22440); completed exact classification for `F=6` (5760 states, ~33M pairs checked, strict/subset split and full `Δ` scan) within time budget, which sufficed to exhibit the phenomenon. Did not complete lower-level pairwise scans.
- Did not attempt exhaustive enumeration of all optimal strategies at `n=6` (combinatorially large) to certify a whole-strategy “every compression sequence increases” instance.

# Bottom line

**[Mathematical finding, finite/exact]:** meet-compression on optimal strategies is **not stepwise size-preserving** in general. It is deletion-only (hence locally nonincreasing) at `n=5` on tight states, but at `n=6` there exist antichain-reachable tight strict mergeable pairs (1440 at `F=6`) whose meet-replacement forces a larger reachable-state continuation (concrete witnessed increase `97 → 107`, robust over source top-level optimal choices in the checked model). This is a concrete obstruction to treating canonicalization-by-meet as a sound size-preserving preprocessing step in full generality, while falling short of the all-`n` “every compression sequence” falsifier; the global compressibility/join-reduced-certificate question for exact `S(n)` remains open. No repository, Lean, or board changes were made.

## Other metadata

```json
{
  "finished_at": 1795031880.109629,
  "started_at": 1795030231.7931457
}
```
