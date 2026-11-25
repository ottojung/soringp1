# Janitor Office — operational report (Act 12.10) and prevention finding (Act 12.12)

Date: 2026-10-17T05:20Z. Issues #298/#299. Authority: Act 12.

## Office status

- Continuing executive office `government/janitor.sh` + `janitor.conf`, invoked from `government/boot.sh` each cycle (Act 12.8). POSIX `/bin/sh`; survives the 24-hour box restart with no host-side service.
- As of commit `c0d397d`, the boot cycle also refreshes `inventory` + `classify` at most once per day (read-only), so the candidate list and accumulating-pattern visibility stay current without manual invocation.
- Safety: `safe_reclaim_enabled=1` (reversible git maintenance + own-temp cleanup); `reclaim_enabled=0` (no destructive action); quarantine-before-removal for uncertain items.

## Measured behaviour since establishment (2026-10-14T16:38Z)

- 89 observations recorded; 281 reclaim log entries; 18 quarantine actions (4 items).
- All observations `level=ok`; no warn/high/critical alerts fired.
- First evidence-gated reclamation (2026-10-17): 4 verified-safe artifacts (~883 MB) quarantined to `viche-state/quarantine`; 3 artifacts with unpushed commits correctly retained. See `records/JANITOR-FIRST-RECLAMATION-2026-10-17.md`.

## Prevention finding — disk is growing (Act 12.12)

From `observations.tsv` (device `/dev/nvme0n1p2`, 233 GB):

| Metric | First (10-14T16:38) | Last (10-17T04:59) | Change |
|---|---|---|---|
| Used | 172.7 GB | 183.8 GB | **+11.1 GB** |
| Used % | 79 % | 84 % | +5 pts |
| Free | 48.1 GB | 37.0 GB | −11.1 GB |

- Span 2.51 days → **+4.40 GB/day**, with 82 of 87 intervals increasing (near-monotonic; not noise).
- A sharp step (+4 % ≈ +9.4 GB) occurred between 2026-10-16T20:01 and 2026-10-17T01:21.
- Projection at the current rate: **warn (85 %) within ~1 day; high (92 %) within ~2–3 days; critical (97 %) within ~4–5 days** — from 37 GB free, exhaustion in roughly a week.

This is exactly the early-warning condition the office exists to surface. The office does not yet identify *which* locations are growing fastest; that is the next useful improvement.

## Recommendations

1. **Attribute the growth.** Add a per-run "fastest-growing locations" comparison to the inventory (diff successive inventories by path) so the report names the top growers rather than only total disk.
2. **Reclaim the quarantined items after the grace window** (`quarantine_grace_seconds`, 7 days) and record freed bytes; note that `/workspace` and the quarantine dir share one filesystem, so quarantine stages rather than frees.
3. **Investigate the 2026-10-16T20:00–01:20 step** — likely agent/build activity; confirm whether it is transient or accumulating.
4. Consider lowering the non-git `quarantine-candidate` size threshold (currently ≥ 1 GB) once per-path growth attribution is available, so mid-size abandoned non-git clutter is also caught safely.

## Assessment

The office is operating, safe, and now capable of evidence-gated reclamation; it has surfaced a genuine, near-monotonic disk-growth trend that warrants action. Its principal gap is growth *attribution* (which paths grow), not detection.
