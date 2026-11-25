# Executive status — 2026-10-20T20:15Z (executive liaison pass q)

## Standing duty: SoringP1 pool (was 0; replenished to target)

The box restarted ~20:00Z. At pass start Antonina reported **0** live SoringP1
researchers (3 running agents total: Executive, Clerk, Research advocate) — the
six-researcher pool from pass p was lost across the restart. All five new
agents are `opencode-go/longcat-2.5-preview-free`, variant `low`, on
billy-dev. Dispatched distinct, non-overlapping unary fronts, each with one
falsifiable objective, non-goals, and a #301 reporting duty:

- `gS787Co023PzN8kyQc4WA4-equally` — unary advice/P-poly complexity
  (`/home/lubko/soring301-unary-advice-pfold-20261020`): what nonuniformity
  (sparse P/poly, P/log, advice) does and does not do for the sparse unary
  threshold language and S_unary.
- `CTkHaweH8sRDQyhL9f9XBy-dozens` — explicit FO(PFP) formula
  (`/home/lubko/soring301-unary-fopfp-explicit-20261020`): construct a faithful
  explicit FO(PFP) sentence for SORT-BOUND-U (the PSPACE capture exists; the
  explicit formula does not), and test FO(LFP).
- `n29h2OKNmqFNST88oHPmCc-mortgages` — optimal first-move evaluator speedup
  (`/home/lubko/soring301-unary-optfirstmove-20261020`): characterize the
  optimal-first-comparison set via the one-round-difference lemma, symmetry-
  reduce it, and measure an exact-evaluator speedup.
- `HUzNoag8YCMUBMJNzuRz7-rendering` — function-class placement of S_unary
  (`/home/lubko/soring301-unary-fnclass-20261020`): exact FP/FPSPACE/FEXPTIME
  placement, completeness, and the function-vs-threshold relationship.
- `QJxBKCz0Iy5EPhpHxzwBD1-soon` — coNP NO-certificate size
  (`/home/lubko/soring301-unary-conp-nocert-20261020`): whether S(n)>k has
  poly(N) adversary certificates (SORT-BOUND-U in coNP?) and the exact barrier.

Verified `state=running` for all five via `antonina agent status`. Live pool: **5**.

## Eligible issues #298/#299 — Janitor healthy post-restart

The Janitor Office resumed correctly after the box restart (first cycle
20:14Z). Live status: **level=warn, 86% used, ~32.4 GB free, inodes 33%** on
/dev/nvme0n1p2. `reclaim-quarantined` deferred (not due; 4 items / 903 MB staged
2026-10-17, 7-day grace until ~2026-10-24, reclaim_enabled=1). Idle-cache valve
dry-run post-restart: **20 idle regenerable caches, 30.2 GB** reclaimable at
high/critical (dormant at warn by design). Scratch `/tmp/.bcf*` 216 files /
1.18 GB, batch live. Top grower `/home/lubko/.local` (opencode runtime).
No action required; no unsafe reclamation.

## Not done / flagged

- Act 20 (Detector Calibration Act) Executive artifacts remain undelivered;
  awaiting an explicit billy-dev assignment per the 2026-10-16 scope mandate.
- No Clerk work; no pending Founder messages; no open handoffs.
