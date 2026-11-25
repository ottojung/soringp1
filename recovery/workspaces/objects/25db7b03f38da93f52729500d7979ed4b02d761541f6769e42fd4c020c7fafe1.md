# Executive delivery status — 2026-10-17T07:15Z

## #301 — SoringP1 Lean-checked complexity — **A0–A19 (partial) + A21–A23 DELIVERED (merged)**
- **A0** `exists_hasBudget` (9bc4110): a correct sorting decision tree exists for every n.
- **A1** `Attainment.lean` (e6c12eb): S(n) is attained and minimal (`hasBudget_S`, `S_le_iff`, `S_is_minimal`, `S_le_explicit`, `exists_tree_S`).
- **A2** `LowerBound.lean` (7f8cacb): information lower bound `n! ≤ 2^(S n)`.
- **A4** `SmallValues.lean` (f653694): `S 0 = 0`, `S 1 = 0`, `S 2 = 1`, `3 ≤ S 3`.
- **A5** `SmallValues.lean` (6cf15f0): `S 3 = 3` (optimal three-comparison tree). S(0..3)=0,0,1,3 exact, matching the reference evaluator.
- **A6** `docs/kernel-results.md` (0d43e97): durable inventory of all kernel-checked results + open fronts; Boundary A marked largely complete.
- **A7** `SmallValues{4,5,6}.lean` + `scripts/generate_optimal_tree.py` (20febf1): `S 4 = 5`, `S 5 = 7`, `S 6 = 10` via generated optimal trees. **S(0..6) = 0,0,1,3,5,7,10 all exact and kernel-checked**, matching the reference evaluator. Independently verified (build + leanchecker); CI run 39015746229 green.
- **A8** `Monotone.lean` (b1389e2): `S_mono (n) : S n ≤ S (n+1)` — the optimal comparison count is nondecreasing (via pruning an (n+1)-tree to an n-tree). CI green.
- **A9** `Bounds.lean` (0cbe935): `n_sub_one_le_S (n) : n - 1 ≤ S n` (+ `two_pow_le_factorial`, `two_pow_pred_le_factorial`). CI green (run 39018882550).
- All: no sorry/admit/axiom/native_decide; independently verified; **CI green** (runs 39004578554, 39006175280, 39008320757, 39011388045).
- **A3 (tight bound `S n ≤ n(n-1)/2`) NOT delivered**: the fuel-driven `go` proof counts every recursion step, so required fuel = height + n, not height; the invariant/penalty induction did not close. Reverted; the loose bound `n(n+2)+(n+1)+1` stands. Recorded as an open sub-front.

- **A10** `TightBound.lean` (d5040cc): **`S_le_tight (n) : S n ≤ n*(n-1)/2`** — tight upper bound (comparison-exact height invariant; length-only invariant). CI green.
- **A12** `Bounds.lean` (dc34465): **`log2_factorial_le_S (n) : Nat.log2 n.factorial ≤ S n`** — information bound in log form. CI green.
- **A13** `SmallValues7.lean` (91e2335): **`13 ≤ S 7 ≤ 21`**. CI green.
- **A14** `Bounds.lean` (2773ce3): `le_S_of_pow_lt (n k) (h : 2^(k-1) < n!) : k ≤ S n` (+ `13 ≤ S 7`, `16 ≤ S 8`). CI green.
- **A15** `Bounds.lean` (864d7f9): `clog_factorial_le_S (n) : Nat.clog 2 n.factorial ≤ S n`. CI green.
- **A16** `TightSmall.lean` (5a8ee5e): `S_eq_clog_of_le_six` — the info bound is tight for n ≤ 6. CI green.
- **A17** `Minimax.lean` (de02c93): `splitPairs`, `card_filter_lt`, `split_of_lt`, `splitPairs_nonempty`. CI green.
- **A18** `Minimax.lean` (5a439d4): computable minimax recurrence `adv` + adversary lower bound `adv_le_height`. CI green.
- **A19 (partial)** `Minimax.lean` (8b7b775): `bestPair`, `minimaxTree` definitions; `minimaxTree_spec` NOT proven (defeq loop on recursive `adv`). CI green.
- **A21** `Minimax.lean` (dc71bbe): `adv_univ_le_S (n) : adv univ ≤ S n`. CI green.
- **A22** `Minimax.lean` (ce1d027): `minimaxTree_sorts : Sorts S (minimaxTree S)`. CI green.
- **A23** `Minimax.lean` (6bcbe7c): `adv_eq_zero_iff (S) : adv S = 0 ↔ S.card ≤ 1`. CI run 39047273045 in progress.
- **Evaluator upper bound** (`S n ≤ adv univ` via `minimaxTree_spec`): blocked by a Lean defeq/whnf loop unfolding the recursive `adv`; fix requires restructuring `adv` (opaque `WellFounded.fix`).
- **Evaluator (front 2)**: `adv` recurrence + adversary lower bound landed (A18). Next: construct the achieving minimax tree, prove `S n = adv univ`.
- **A11** `Monotone.lean` (91ea2da): `hasBudget_prune {n k} (h : HasBudget (n+1) k) : HasBudget n k` — feasibility monotone in n. CI run 39023110618 in progress.

## #298 / #299 — Janitor Office — **capability + prevention + attribution delivered**
- Merged/deployed (main bd502d2): modes + three safety fixes + daily inventory/classify + per-path growth attribution.
- First evidence-gated reclamation: 4 verified-safe artifacts (~883 MB) quarantined; 3 with unpushed commits retained.
- Growth attributed to transient build/agent artifacts (not a leak); a `/tmp/opencode` wipe freed ~1.5 GB (recorded incident, no durable loss).
- Next: reclaim quarantined items after the 7-day grace; extend scan depth to nested build caches with a live-build safeguard.

## Janitor (this cycle)
- `report` shows quarantine status (count, staged KB, grace, gate) — Act 12.10 transparency.
- `reclaim_enabled=1` (Act 12.7): the boot cycle now runs `reclaim-quarantined`, so the 4 verified-safe staged items (~883 MB) will be freed after the grace window (~2026-10-24) automatically.
- Gate-separation bug fixed: the reversible allowlist reclaim is now gated solely by `safe_reclaim_enabled`; `reclaim-quarantined` is separate. Caught by `tests/janitor-smoke.sh`; now passes. Deployed (ce1437f).

## Janitor robustness (this cycle)
- `quarantine_dir` is now state-relative by default (`$VICHE_STATE_ROOT/quarantine`) — tests/alternate state roots can no longer touch the live quarantine.
- `tests/janitor-smoke.sh`: pre-stamps `last-inventory` (hermetic cycle no longer scans the real box) and adds step 6 covering `reclaim-quarantined` (removes only items past grace). Deployed (0214bdb).

## Resource notes
- cgroup ~6.5/8.6 GB; `leanchecker` needs `LEAN_NUM_THREADS=1`. SoringP1 clone moved to durable `/home/lubko/soring301`.
