# antonina-TezhANZLOmCrnZRXLcEeYt-tribe

Session: ses_e4e286d15ffeJFQsj2PPGx5N9j
Workspace: /home/lubko/soring-fronts/deficit-delta-n-monotonicity
Created: 1793985057582; updated: 1793985324114

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 104 (msg_1b1d87b82001HrUSak824uLWq2)

We're on billy-dev. Board access via Antonina is currently failing (credential mismatch), but the durable frontier ledger is readable. Let me pull the key prior context and the literature, then do the mathematics.

## Output 130 (msg_1b1d8e28d001rry2yedjaP2JZH)

Now the key data: exact S(n) for n ≤ 22 are established (Stober–Weiss ALENEX 2023, which proves S(16)=46, S(17)=50, S(18)=54 and closes the lower bound for n≤22). Let me get the full exact list from OEIS A036604 and compute delta.

## Output 141 (msg_1b1d90391001ioscZkKGQdU1ty)

The counterexample may already be in the exact values. Computing delta for n=1..22 from the published exact values:

## Output 156 (msg_1b1d9750b001Nl6F27oKCZHJCh)

The abstract confirms: before Stober–Weiss, exact S(n) was known for all n ≤ 22 except 16, 17, 18 — so S(19)=58 and S(20)=62 are established published exact values. Let me check the ledger for this front's exact entry/id, and verify the raw (uncorrelated with ceiling) gap behavior too.

## Output 167 (msg_1b1da132800142XZM5UrMXRQZ3)

This front's falsifier asks for one published, independently checkable pair. I've found a strong candidate. Let me independently verify each published value's provenance before claiming the drop.

## Output 182 (msg_1b1da370a0014FmF0Cb4Pmk0iB)

A001768 confirms the Ford–Johnson upper bounds (58, 62, 66, 71 at n=19–22) matching the exact values. Let me verify the exact-integer ceiling arithmetic (no floating point) and cross-check the Stober–Weiss paper's own table for n=19–22.

## Output 197 (msg_1b1da9cf6001rGSPTm6AArJeyN)

The paper confirms provenance (Peczarski + Nankai Stars computed exact S(19); Peczarski 2004 proved FJ optimality at n=14, 22). Let me check the paper's experimental table for the exact S(19), S(20), S(21) entries.

## Output 215 (msg_1b1dac316001vhS23d20CrnZKU)

All checks converge. The chain of published evidence is complete. Let me try to post the finding to board #301 (as the contract requires) and record it in the durable frontier ledger, keeping the worktree clean.

## Output 254 (msg_1b1db439d001X6GzhZ9jWR6IKY)

Board posting is blocked by the missing Antonina board credential (infrastructure failure, unfixable without the shared credential). Following the contract's restart-protocol, I record the finding in the durable frontier ledger instead.

## Output 265 (msg_1b1db66a4001FyIlICM3PHL8px)

## Report — FRONT `deficit-delta-n-monotonicity`: the falsifier exists, monotonicity is refuted

### Mathematical finding (the claim is FALSE)

**Data point (published, independently checkable):** δ(19) = 1 > δ(20) = 0.

From Stober–Weiss, *Lower Bounds for Sorting 16, 17, and 18 Elements*, ALENEX 2023 ([arXiv:2206.05597](https://arxiv.org/abs/2206.05597), **Table 7**, which fixes exact S(n) for all n ≤ 22):

| n | S(n) | C(n)=⌈log₂ n!⌉ | δ(n) |
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
