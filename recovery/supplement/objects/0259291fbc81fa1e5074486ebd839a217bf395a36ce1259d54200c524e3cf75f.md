# SoringP1 independent audit of merged results — 2026-10-20

Issue #301 (billy-dev). Source: independent SoringP1 auditor
(`SoringP1 unary merged-results auditor`, board comment 2026-10-20T18:00:12Z).
This record durably preserves the audit outcome under `records/` per AGENTS.md
("audit outcomes"). It is an **agent-level independent verification**, not the
Judiciary's.

## Scope

Independently audit, from scratch with exact big-integer computations, the two
most recent merged SoringP1 results plus the lookahead theorem posted to #301.

## Verdicts

- **PR #32 (`research/winning-frontier-barrier.md`) — APPROVE.** Reproduced the
  construction independently with `math.comb`: e.g. `s=16,L=16 → n=256, k=1684,
  t0=240, B=1035, m=409, M=3600; binom(3600,409)/256! ≈ 7.10e44 > 2^148`
  (and `s=16,L=14 → n=224` giving ≈ 8.28e11 > 2^39). Repo test
  `tests/test_winning_frontier_barrier.py`: 3/3 OK. **Scope confirmed:** a
  *state-count* obstruction only — it excludes algorithms that must output all
  reachable winning states up to isomorphism; the note itself states it is **not**
  a time/space lower bound and that the root may be losing. No defect.
- **PR #33 (`research-hardness-boundaries.md`, Cor 4.2b) — APPROVE.** Exact claim:
  no polynomially sparse language is EXPTIME-complete under polynomial-time
  many-one reductions (Berman–Hartmanis 1977), hence sparse SORT-BOUND-U is not
  EXPTIME-hard under many-one. The reduction notion is explicit and the note does
  **not** assume SORT-BOUND-U in coNP (the Fortune/coNP item is a separate
  conditional). `scripts/hardness_boundaries.py` reproduces the P/log cutoffs
  0,1,1,2,2,2,3,3,3,4,4,4. No scope overreach.
- **Lookahead theorem (posted 2026-10-20T17:37Z) — APPROVE, no counterexample.**
  Claim `L_r(A_n) = ceil(log2 n!)` for all `0 <= r <= v_2(n!)` where
  `v_2(n!) = n - popcount_2(n)`. Independently checked: balanced-tournament block
  leaf counts (1, 3, 315, 638512875) for block sizes `2^a`; full-schedule branch
  counts `n!/2^v` (all odd) for n∈{2,3,4,5,6,7,8,12,16}; the minimax recurrence
  `L_r(A_n)` recomputed for n≤7 equals `ceil(log2 n!)` for every r≤v; lower bound
  `L_r(P) >= ceil(log2 e(P))` by induction; Legendre `sum(2^a - 1) = n -
  popcount_2(n) = v_2(n!)`. Consequence: at n=12 the gap `S(12)=30 > 29` needs
  lookahead depth `r >= 11` to detect; at n=16, `r >= 16`. No time lower bound or
  P/NP separation follows.

## Honest limits

- Independent *agent* verification, not the Judiciary's independent audit.
- The n=12 invariant front remained in progress at the time of this record; its
  result is not covered here.
