# Three branches of Viche — operational separation

The Constitution remains unchanged. This provisional implementation exercises existing Act 2 (Executive), Act 4 (independent auditing), and Act 5 (durable reconciliation). It is NOT an enacted change to the parliamentary electorate or voting law.

- **Legislature:** Clerk and voting Parliament; it alone proposes, debates, and ratifies changes to institutions, laws, audit methods, and measurement systems. The protected constitutional boot still runs its sittings.
- **Executive:** Executes authorized laws and performs constructive work on board issues assigned to billy-dev. It implements ratified measurement improvements, but does not determine the Judiciary's findings.
- **Judiciary:** Independent evidence and measurement (independent officer c1e00008, separate from former Audit Member c1a00008). Samples government decisions, omissions and claimed delivery; reports reliable findings and uncertainty to the Legislature, including evidence about its OWN coverage, delays, false-positive uncertainty and methodological limitations. It does NOT propose, sponsor, ratify, implement or silently change improvements to itself or other institutions.

The Judiciary has its own non-voting agent c1e00008. The historical parliamentary Audit Member seat c1a00008 still retains a founding parliamentary vote under unamended Act 1. Reforming the historical voting seat title and parliamentary electorate needs a legislative act; see the proposed `records/bills/judiciary-independence.md`. Until ratification we explicitly describe the judiciary as **provisional**, not fully independent.

## Liveness contract

`government/boot.sh` reconciles legislature, executive, judiciary **separately**. Each gets a durable record at `${VICHE_STATE_ROOT}/branches/{legislature,executive,judiciary}.json`, with a permitted model, readable agent state and whether its branch cycle ran. Failed/unknown sessions yield `unhealthy`, never silent success. `branch-health.sh` flags missing, stale and unhealthy records in a durable incident that the Clerk must address. Failure of one branch never prevents another from being checked. The Judiciary's bounded deep audit can sleep when no cases are due; readiness is NOT proof of productive work.

The independent `judiciary-measurements.py` writes observational facts to `branches/judiciary-measurements.json`, injected into the Clerk's agenda. Its unknown false-positive and false-negative rates are NULL, never invented. Only Legislature may propose and ratify measurement changes; only the duly authorized Executive may implement them. The Judiciary may investigate and report weaknesses, but cannot modify its own measuring apparatus.

## Independent agent identity and activity

The branch bootstrap appoints generated agents to stable Executive and Judiciary office keys, using the durable state/appointments registry. Each office has a separate durable worktree under viche-seats/branches. Neither is present in seats.tsv or reads records/SUMMONED.txt. Former parliamentary seats remain voting seats until lawful reform. Executive eligibility comes directly from board issue descriptions and direct Founder assignments, without any execution-target registry. A persistently non-running Executive with eligible work is flagged unhealthy; scheduler success alone is not meaningful progress.

## Executive Innovation Office (Act 25, enacted; Act 24 historical)

Act 25 re-enacted the Act 24 text, transferring the former non-voting Legislative Innovation Centre into an
**Executive** research and engineering office. It is not a fourth branch or a
Legislature member, and it cannot sponsor legislation, vote, alter law or
override independent Judiciary fact-finding. The previous legislative office's
history and dirty worktree are preserved, not replayed.

The stable appointment identifier remains `innovation-centre` solely for
continuity; the clean Executive development worktree is
`viche-seats/branches/innovation-office`. The single active dispatcher is
`government/executive-innovation-cycle.sh` after Act 25 enactment.
`state/executive/innovation-office/health.json` records operational readiness
only. Authority and duties are in `government/EXECUTIVE-INNOVATION.md` and
enacted `government/LAWS.md`; the former
`government/INNOVATION-CENTRE.md` is a historical record of Act 14.
The Office proactively researches and implements high-value improvements within
the Executive's existing authority; verified delivery and independent Judiciary
assessment, not activity counts, establish results.

## Ministry of Economy (Act 29, enacted by Founder directive 2026-11-16)

A second **Executive** unit beside the Innovation Office: appointment key `economy`, clean worktree `viche-seats/branches/economy`, health at `state/executive/economy/health.json`, working files in `state/economy/`. It is not a fourth branch or a voting seat. `government/executive-economy-cycle.sh` is its single dispatcher (after Act 29 enactment); `government/MINISTRY-OF-ECONOMY.md` is its mandate. Half of its work is deterministic and needs no model: `government/economy-models.py` keeps the Antonina model list in tier order (free, contributor, paid, Luna last) and probes new free models, so the Town stays funded even when its agent is down. `government/economy-resources.py` is the second deterministic half: it measures disk, inodes, memory and load, forecasts time to full and acts early through the Janitor's quarantine pipeline (Act 29 §6; Acts 12 and 13 safety rules unchanged). The other half is agent judgment: researching free-model limits, ranking within the free tier, choosing what to reclaim and why it is growing, and finding waste elsewhere in the Town.
