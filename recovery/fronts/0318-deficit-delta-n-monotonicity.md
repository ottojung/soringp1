# deficit-delta-n-monotonicity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

TezhANZLOmCrnZRXLcEeYt-tribe

## exit_state

clearexit

## question

Is the deficit delta(n) = S(n) - ceil(log2(n!)) non-decreasing in n for all n, or does there exist a documented data point where delta drops from one n to the next; more broadly, is delta(n) eventually non-decreasing along the known exact and bounded instances?

## basis

Published exact windows S(12)=30 vs C(12)=29, S(16)=46, S(17)=50, S(18)=54, S(28)>=99 (Stober-Weiss ALENEX 2023; Wells; Peczarski), cited in docs/literature.md, a research board or ledger source not needed since every cited value is externally checkable.

## falsifier

Exhibit one published, independently checkable pair with delta(n+1) < delta(n) using exact S values or verified lower-and-upper windows, or conversely prove monotonicity via the minimax recurrence and state which monotone structural property of optimal sorting trees forces it.

## implication

If delta is monotone, its value at a known data point below n bounds the exact gap for larger n, sharpening where the unary threshold k must lie near ceil(log2(n!)) and giving a new structural invariant of the antichain-root minimax game.

## finding_unverified

₂ n!⌉ | δ(n) |
|---|------|----|------|
| 19 | 58 (credited to Cheng et al. 2007) | 57 | **1** |
| 20 | 62 | 62 | **0** |
| 21 | 66 | 66 | **0** |
| 22 | 71 (Peczarski) | 70 | 1 |

Ceiling arithmetic done exactly with integers: 2⁵⁶ ≤ 19! < 2⁵⁷ so C(19)=57; 2⁶¹ ≤ 20! < 2⁶² so C(20)=62. So **δ(20) < δ(19)** — a strict drop.

**Not a ceiling artifact:** the ceiling-free gap E(n) = S(n) − log₂(n!) drops too — 19→20: 1.2445 → 0.9226, 20→21: → 0.5303 — four consecutive drops in E across 17→21.

**Mechanism:** δ(n+1) − δ(n) = d(n+1) − m(n+1) where m(n) = C(n) − C(n−1) jumps by an extra bit exactly when the fractional part {log₂ n!} crosses ~0.72 (n=20), while the optimal increment d stays at 4. Positions where {log₂ n!} is near 0 give "free" ceiling slack the tree does not have to pay for — the drop is structural, not numerical noise.

### Why no "converse" proof via the minimax recurrence can rescue the claim

Any monotone structural property of optimal sorting trees forcing δ upward would need a per-step information "wage". It fails demonstrably: S(21) − S(20) = 4 < ⌈log₂ 21⌉ = 5, so the natural claim d(n) ≥ ⌈log₂ n⌉ is false in the exact sequence — there is no uniform lower bound on the optimal increment strong enough to track the ceiling's jumps.

### Complexity implication (as posed in the front)

Refuted: a known δ value below n does **not** bound the exact gap at larger n. Only the trivial invariant δ ≥ 0 survives (C(n) is always a valid lower bound). Certificates/threshold-placement arguments near K = ⌈log₂ n!⌉ must track the fractional-part structure of log₂ n!, not a propagated constant. Open residue: for 23 ≤ n ≤ 34 only windows exist (e.g. S(23) ∈ {75, 76} with C(23)=75), so further drops may recur; whether δ keeps oscillating at large n is out of reach without new exact instances (n ≥ 23 open, next unknown exactly at n=23).

### Labels and honest limits

- **literature + deduction** for the counterexample: values sound via published exhaustive searches (Wells, Peczarski, Cheng et al., Stober–Weiss); I did not re-verify the searches locally at n ≥ 16 (infeasible; only the ceiling arithmetic and S ≤ F upper bounds were rechecked). Soundness rests on the published proofs; the区分: this uses *exact published values*, so no completeness assumption on any pruning heuristic enters — the cited bidirectional-search method's completeness (Lemma 4.2) is on its authors.
- **No Lean / no repository changes**: per the publication gate, a finite documented counterexample to a monotonicity conjecture is a falsification, not a new all-n kernel theorem. Worktree clean.
- **Infrastructure limits (reported):** the Antonina board client currently has no board credential (`save the shared board credential as $XDG_CONFIG_HOME/antonina/credential.json`), so neither the digest nor a #301 post could run despite retrying with the correct CLI form (`antonina board comment`). Per the restart protocol I recorded the finding in the durable ledger entry `deficit-delta-n-monotonicity` (`~/.local/state/soringp1/frontier-ledger.json`, field `finding_unverified`, dated 2026-11-06); it remains **unverified** until board/audit review. No other side effects were made; this front's status stays `running` for the keeper to collect.

Also note this drop (19→20) and the prior ledger note ("Delta zero at 0–11, 20, 21 and ≥1 elsewhere in the checked range; monotonicity fails") agree — this front is now closed with a precise cited counterexample rather than a range observation.

## Other metadata

```json
{
  "finished_at": 1793985339.6508222,
  "started_at": 1793985057.1728368
}
```
