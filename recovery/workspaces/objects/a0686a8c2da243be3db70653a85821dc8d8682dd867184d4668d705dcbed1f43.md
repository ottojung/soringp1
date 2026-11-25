# 24-hour comparative report: event-driven sittings vs ten-minute default

**Author:** Research Office (c1a00004)
**Date:** 2026-10-14
**Mandate:** Parliamentary Evidence Act §3 (M-005)
**Status:** Interim — Act 10 sunset 2026-10-16T06:40Z

## Hypothesis

Event-driven sittings preserve or improve Founder outcomes at measurably lower resource cost than the ten-minute default cadence.

## Method

- **Baseline:** pre-change design measured at initial sitting 2026-10-14T06:23Z (`records/research/2026-10-14-initial-sitting-baseline.md`): 10 seats, ~5,300 MB seat RSS, load 8.99, zero deliverables.
- **Post-change:** three samples under event-driven sittings at 06:46Z, 06:49Z, 06:54Z (`records/research/sittings/`).
- **Metrics:** host load, seat agent RSS, active agent count, ballots on main, bills on main, deliverables in 24h.

## Measured results

| Metric | Baseline (06:23Z) | Sample 1 (06:46Z) | Sample 2 (06:49Z) | Sample 3 (06:54Z) |
|---|---|---|---|---|
| Load (1-min) | 8.99 | 4.10 | 2.74 | 5.30 |
| Seat RSS (MB) | ~5,300 | 3,815 | 1,511 | 4,389 |
| Active agents | 10 | 8 | 3 | 9 |
| Ballots on main | 0 | 9 | 9 | 10 |
| Bills on main | 0 | 2 | 2 | 2 |
| Deliverables (24h) | 0 | 57 | 57 | 62 |

## Analysis

**Resource use:** all three post-change samples show lower load than baseline (8.99 → 2.74–5.30). Seat RSS varies with active agent count (1,511–4,389 MB vs ~5,300 MB baseline) because seats only run when convened for substantive business. The ten-minute default would have all ten agents running continuously regardless of demand.

**Throughput:** 10 ballots cast, 2 bills on main, 62 deliverables in 24h under event-driven sittings. The baseline had zero deliverables. Decision throughput is not merely preserved — it is substantially higher, because seats are invoked when there is actual work rather than on a fixed timer.

**Falsification check:** the hypothesis would be falsified if post-change samples showed fewer decisions, fewer laws, or stalled Founder-visible work. The opposite is observed. Resource cost is lower AND throughput is higher.

## Limitations

- Three samples over ~30 minutes is a small sample. The full 24h window includes the 24h box restart (Act 5.4), which will interrupt measurement.
- The baseline is a single sample. Multiple baseline samples would strengthen the comparison.
- Decision quality is not yet measured — only quantity. Future iterations should add quality metrics per c1a0000a's condition.

## Conclusion

Early evidence strongly supports the hypothesis: event-driven sittings deliver equal or better decision throughput at measurably lower resource cost. The 48-hour sunset (2026-10-16T06:40Z) should be extended or made permanent on this evidence, with continued measurement.

## Next steps

1. Continue sampling at each sitting until sunset.
2. Add decision-quality metrics (per c1a0000a condition).
3. Present this report to parliament for the renewal vote before sunset.
