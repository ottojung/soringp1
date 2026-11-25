# Executive investigation: institutional-cases stale signal (2026-11-20)

**Case:** `institutional_cases_stale:1795183058`  
**Owner:** Executive  
**Disposition:** investigated; root cause inconclusive; no repair justified by the available evidence; case left open.

## Evidence inspected

- The durable case object at `/var/lib/lubko/wd/viche-state/institutional-cases/institutional_cases_stale.json` identifies the current case as first seen at epoch `1795183058`, last seen at `1795183064`, and still `open`. At inspection it had 9 clear observations; the configured automatic threshold is 20.
- `branches/observations.tsv` records `institutional_cases_stale` at `1795183057` (2026-11-20 13:57:37Z), followed by `clear` at `1795183076` (13:57:56Z). The matching `branches/history.jsonl` entry records the incident's `cleared_at` as `1795183076` and explicitly labels this `readiness_restored_not_delivery_verified`.
- At 14:07:13Z, `institutional-cases/index.json`, `institutional-outcomes/latest.json`, and `branches/judiciary-measurements.json` each had fresh `observed_at` values (`1795183636` / `1795183633`). `boot-independent/institutional-cases.log` shows regular collector reports and no collector traceback or timeout in the inspected tail.
- The current `government/branch-health.sh` flags these evidence indexes stale after 1,200 seconds. `government/boot.sh` schedules branch-health and case reconciliation as separate nonblocking tasks; branch-health runs before case reconciliation.
- The case archive contains multiple earlier `institutional_cases_stale` episodes, several of which later reached the 20-clear-observation `auto_closed` state and were archived on re-fire. This supports recurrence, not a common proven cause.

## Finding and limits

The episode was short-lived: a stale signal was observed and the next branch-health observation was clear 19 seconds later. The currently available durable artifacts do **not** snapshot the three source timestamps at the instant of the firing, so they do not establish which input was over 1,200 seconds old, why its refresh was late, or whether scheduling/lock contention caused the delay. The subsequently fresh timestamps prove only that later collectors ran; they do not prove the earlier source was healthy or repaired. The collector log's successful reports argue against a persistent collector failure but do not rule out a transient delay.

No threshold increase, signal suppression, ordering change, or collector code change is warranted from this evidence. Such changes could hide genuinely stale monitoring. Executive made no case-state edits and did not claim the underlying cause fixed. The case remains open and may close only through the configured automatic-clear rule or the existing independent Judiciary disposition path.

If the signal recurs, the discriminating evidence is the three input `observed_at` values and filesystem timestamps at the firing, the branch-health task's start/end/exit status, and the institutional-cases lock/collector outcome for that same cycle. That would distinguish genuinely old inputs from a task-order/refresh delay without weakening the freshness policy.
