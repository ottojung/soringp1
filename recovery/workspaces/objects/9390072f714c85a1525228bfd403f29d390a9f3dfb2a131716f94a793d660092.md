# Independent institutional outcome feedback

`government/outcome-metrics.py` is a read-only evidence collector executed
non-blockingly by `government/boot.sh`, separate from executive dispatch and
legislative voting. It persists `institutional-outcomes/latest.json` and a
timestamped JSONL history below `VICHE_STATE_ROOT`.

The measurements distinguish (1) Antonina process exits by project/outcome,
(2) main-branch Git commits and PR merges as delivery signals,
(3) readiness ages of the Legislature, Executive, Judiciary and permanent
non-voting Innovation Centre, (4) still-open work seen on the Antonina board,
and (5) claimed, investigated, blocked and independently curated SoringP1
research fronts.

**No proxy proves completed work.** A green agent exit is not a merged
artifact; a merged commit is not evidence of independent quality; an AI
proposed research question is not a theorem; branch readiness is not
institutional effectiveness. Each unavailable source is marked unavailable,
not silently converted to zero.

The independent Judiciary includes the snapshot in its measurements. The
Clerk reads the evidence when preparing its agenda. Only the Legislative
branch may debate, propose and ratify changes. Neither the measurements nor
this document impose quotas, models, a project list, or substantive goals on
the autonomous Innovation Centre.

## Failure of evidence is an incident (Founder directive, 2 November 2026)

The existing branch-health cycle checks executable Python and freshness of
outcomes, corrective cases and judicial measurements. Stale or absent positive
evidence is an adverse signal that requires independent investigation and
durable case reconciliation. A running process and a stale empty index cannot
establish good health or close a case.
