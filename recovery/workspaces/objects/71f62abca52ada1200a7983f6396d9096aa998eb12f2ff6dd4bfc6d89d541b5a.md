# Judiciary disposition — `institutional_cases_stale:1795183058`

Recorded 2026-11-20, after read-only investigation of the current corrective case. This is an independent fact disposition, not a closure, repair, policy proposal, or verdict about misconduct.

## Evidence inspected

- `/var/lib/lubko/wd/viche-state/institutional-cases/institutional_cases_stale.json`: case `institutional_cases_stale:1795183058`, owner `executive`, state `open`, `first_seen=1795183058` (2026-11-20T13:57:38Z), `last_seen=1795183064`, `observations=2`, `clear_observations=1`, `last_clear_observed_at=1795183093`.
- `/var/lib/lubko/wd/viche-state/institutional-cases/index.json`: `observed_at=1795183093`; the case remains in `active`. The index itself lists eight historical `verified_closed` obligations without case-bound closure evidence; these are distinct from the present stale-index signal and are not adjudicated here.
- `/var/lib/lubko/wd/viche-state/branches/observations.tsv`: the stale signal at `1795183057` is followed by `clear` at `1795183076`, `1795183088`, and `1795183124`.
- `/var/lib/lubko/wd/viche-state/branches/{legislature,executive,judiciary}.json`: at `1795183056–1795183057`, each file passed the branch-health input schema with a recent observation (`ready` for Legislature; `running` for Executive and Judiciary). Each explicitly cautions that readiness is not proof of completed work.
- `sh government/branch-health.sh` was run read-only in the canonical checkout and exited 0; the following `python3 government/institutional-cases.py report` still showed the case open with one clear observation. This is consistent with signal recovery but does not meet the 20-clear automatic closure threshold.

## Disposition and limits

The observable failure was a stale institutional-case index at the branch-health observation at `1795183057`; the index was refreshed by `1795183093`, and later branch-health observations were clear. The available evidence supports a short-lived freshness alarm, not a conclusion that an office failed, that work was neglected, or that the underlying cause was repaired. The precise reason the index was stale at the trigger is not established by these artifacts. Historical `branch-health.log` entries report independent branch-health tasks timing out, but they do not establish that those timeouts caused this index-freshness event.

The case remains **open** in durable state. Its signal has not met the configured 20 consecutive clear observations, and no Clerk closure artifact was inspected or supplied. Accountable operational owner remains the Executive; the concrete unresolved observation is why the case index missed its freshness window at `1795183057`. No evidence about Founder happiness or useful delivery is inferred from branch readiness or a successful probe.

No case state, monitor, law, mailbox item, board issue, continuity receipt, or measurement machinery was changed. No post or dispatch was made. No `continuity_unverified_*` signal was active in the current institutional-case index, so no continuity receipt was warranted.
