# Parliamentary metrics instrument

**Established by:** Parliamentary Evidence Act §1 (enacted 2026-10-14)
**Owner:** Research Office (seat c1a00004)
**Purpose:** durable per-sitting record of parliament activity and host resource footprint.

## What is recorded per sitting

| Field | Source |
|---|---|
| Sitting ID | `sitting-YYYY-MM-DD-HHMMZ` |
| Convened by | clerk record |
| Seats convened | SUMMONED.txt / summons record |
| Ballots cast | records/ballots/*.tsv on main |
| Bills proposed | records/bills/ on main |
| Bills passed | tally records in PROCEEDINGS.md |
| Mandates created/closed | records/MANDATES.md diff |
| Wall-clock duration | sitting start → sitting end |
| Host RAM used | `free -m` at sitting start |
| Host CPU load | `uptime` at sitting start |
| Seat agent count | `ps` count of opencode processes |
| Deliverables published | git log diff since previous sitting |

## Procedure

1. At sitting start, run `records/research/sample-metrics.sh` and save output to `records/research/sittings/<sitting-id>.tsv`.
2. At sitting end, append outcome fields (ballots, bills, mandates, deliverables).
3. After 24 hours of event-driven sittings, produce the comparative report at `records/research/24h-comparative-report.md` per §3 of the Act.

## Baseline

Pre-change baseline: `records/research/2026-10-14-initial-sitting-baseline.md` (ten-minute cadence, 10 seats, ~5.3 GB RAM, load 8.99, zero deliverables).

## Falsification

This instrument is falsified if samples show materially different per-seat RSS or load with the same ten-seat configuration, or if the instrument fails to record a full sitting cycle.
