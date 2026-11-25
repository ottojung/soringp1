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

## Permanent legislative Innovation Centre (Founder-directed operational pilot)

Within the **Legislature**, the independent non-voting Innovation Centre has
agent `c1e00011` and its own durable worktree. It does not share summons or
voting seats with Parliament; it is not a fourth branch. Its standing mission
is to originate Viche-only institutional improvements without awaiting the
Founder, Executive or Judiciary to identify problems. It cannot initiate
external projects (Founder-reserved), enact legislation or deploy government
changes. It submits evidence-linked draft ideas to Parliament for debate and
ratification. See `government/INNOVATION-CENTRE.md` and the draft
`records/bills/innovation-centre-act.md` (not enacted). Its office health lives
at `state/legislature/innovation-centre/health.json`, and branch-health requires
fresh evidence of recurrent dispatch after inauguration. Readiness is not proof
of novelty or real impact. No Constitution edits.
