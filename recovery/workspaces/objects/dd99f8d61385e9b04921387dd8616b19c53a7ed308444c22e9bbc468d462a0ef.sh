#!/bin/sh
# Judiciary investigates outcomes without Clerk or Executive summons.
set -eu
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
seats=${VICHE_SEATS_ROOT:-/var/lib/lubko/wd/viche-seats}
root=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/oversight
charter=${VICHE_CONSTITUTION:?authoritative Founder charter required}
now=${VICHE_OVERSIGHT_NOW:-$(date +%s)}
mkdir -p "$root"
mailbox="$root/judiciary-mailbox"
mkdir -p "$mailbox/inbox" "$mailbox/reviewed"
if [ "${VICHE_AUDIT_CHECKS:-1}" = 1 ]; then
  python3 "$town/government/audit-accountability.py" check > "$root/random-check.log" || exit 1
fi
id=$(/bin/sh "$town/government/appointments.sh" ensure judiciary)
[ -s "$charter" ] && [ -d "$seats/branches/judiciary" ] || exit 1
[ -f "$root/observations.tsv" ] || exit 0
# The Judiciary has its own durable officer; parliamentary summons never gate it.
meta=$(antonina agent status --id "$id" --json)
kind=$(printf '%s\n' "$meta" | jq -r '.state')
case "$kind" in running) exit 0;; failed) echo 'Judiciary: failed agent, independent recovery required' >&2; exit 1;; idle|clearexit) :;; *) exit 1;; esac

# Investigate an incident at least every half hour; also run independent
# broad audits at least once every six hours when there is no incident.
incident=no
cadence=21600
cases='{"open_cases":[]}'
if [ -f "$town/government/institutional-cases.py" ]; then
  cases=$(python3 "$town/government/institutional-cases.py" report) || exit 1
fi
if [ -s "$root/incident.json" ] || [ -s "$root/random/incident.json" ] ||
   [ -n "$(find "$mailbox/inbox" -maxdepth 1 -type f -print -quit)" ] ||
   [ "$(printf '%s\n' "$cases" | jq -r '.open_cases|length')" -gt 0 ]; then
  incident=yes
  cadence=1800
fi
last=0
if [ -s "$root/last-audit-dispatch" ]; then last=$(cat "$root/last-audit-dispatch"); fi
case "$last" in ''|*[!0-9]*) last=0;; esac
[ $((now-last)) -ge "$cadence" ] || exit 0

evidence='No ordinary incident.'
[ ! -s "$root/incident.json" ] || evidence=$(cat "$root/incident.json")
[ ! -s "$root/random/incident.json" ] || evidence="$evidence $(cat "$root/random/incident.json")"
selection='Test-only no sample'
if [ "${VICHE_AUDIT_SELECTION:-1}" = 1 ]; then
  # The audit cycle belongs to a FROZEN randomized draw, not each repeat
  # dispatch. Incident checks may recur every 30 minutes with the SAME draw.
  # That must not mint additional correction slots for a case.
  fresh_sample=no
  if [ -s "$root/random/latest.json" ]; then
    sample_at=$(jq -r '.at // -1' "$root/random/latest.json")
    case "$sample_at" in ''|*[!0-9]*) fresh_sample=yes;; *)
      if [ "$now" -lt "$sample_at" ] || [ $((now-sample_at)) -ge 21600 ]; then fresh_sample=yes; fi ;;
    esac
  else fresh_sample=yes
  fi
  if [ "$incident" = yes ] && [ "$fresh_sample" = no ]; then
    selection=$(cat "$root/random/latest.json")
  else
    selection=$(python3 "$town/government/audit-selection.py") || exit 1
  fi
fi
# Identity is stable for the exact sampled case cohort. Repeated incident
# dispatches and restarts of the same frozen draw reuse one cycle token.
# Test-only no-selection mode uses a deterministic six-hour fixture bucket.
if [ "$selection" = 'Test-only no sample' ]; then
  cycle_id=$(printf 'test-only:%s\n' "$((now/21600))" | sha256sum | cut -c1-32)
else
  cycle_id=$(printf '%s\n' "$selection" | python3 -c '
import hashlib,json,sys
v=json.load(sys.stdin)
if not isinstance(v,dict) or not isinstance(v.get("at"),int) or not isinstance(v.get("cases"),list) or not isinstance(v.get("seed_after_snapshot"),str):
    raise SystemExit("invalid frozen audit batch")
payload={"at":v["at"],"seed_after_snapshot":v["seed_after_snapshot"],
         "cases":[c.get("case_id") for c in v["cases"]]}
print(hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()[:32])
') || exit 1
fi

prompt=$(cat <<EOF
You are the independent Viche Judiciary under Act 4, accountable to
Parliament and the Founder, not to the Executive or Clerk. Your sole role is
fact-finding, adjudication of sampled evidence, and reporting measurements
to the Legislature. Independently audit
whether Viche is making the Founder happier: quality of assigned work,
timeliness, and conservation of Founder attention (Acts 8 and 9). Examine
actual Git changes, tests, merges, deployment, live owners and board issues.
The sample is drawn from the board without executive cooperation. Auditing an
unassigned issue is not acquiring it for productive work.
For host compliance, distinguish Viche agent execution from GitHub Actions
verification. GitHub-hosted CI, including Lean and tests, is explicitly allowed.
Treat disabling CI solely due to agent host assignment as a policy mistake.
An agent being alive or writing a report is NOT evidence of useful delivery.
Do not equate number of commits or a stale local main checkout with success.
Separate verified evidence, uncertainty, and mere leading indicators.

=== AUTHORITATIVE CONSTITUTION ===
$(cat "$charter")
=== END AUTHORITATIVE CONSTITUTION ===

Current audit dispatch cycle ID (include exactly as --cycle-id on every
--correction command): $cycle_id
Operational definition: the same frozen sampled batch has one durable
audit-cycle ID, EVEN IF the Judiciary is summoned again during an incident.
A later independent sample is a new cycle. This is not a retroactive
adjudication of historical cycles or the contested PR #32 corrections.

Current deterministic watchdog evidence:
$evidence
MANDATORY CROSS-BRANCH CORRECTIVE CASES:
$cases
These are health observations, NOT verdicts or legislative authorizations.
Independently investigate persistent cases, cite evidence and report to
Parliament. Do not propose, enact or implement policy from Judiciary.

Judiciary blocker mailbox: $mailbox/inbox. Independently investigate every
pending report using logs, live service state and actual evidence of delivery.
Missing positive evidence counts AGAINST claiming success, not as proof of
misconduct. Record a durable disposition before moving any report to
$mailbox/reviewed; preserve originals, uncertainties and unresolved cases.
Escalate operational repairs to Executive, legal questions to Parliament.

Evidence-quality requirement: a report claiming no blockers, listing live agents,
or announcing progress without an actual impediment is NOT a Judiciary case.
Do not turn such reports into an independently-verified success statement.
A legitimate disposition identifies each *independent* artifact actually read,
specific verifiable paths/commits or live observations, claims tested,
contrary evidence and unresolved limitations. Reading a report is not independent
verification. Label unverified conclusions as unverified. No boilerplate
'verified' and no invented timestamps. Keep genuinely blocked work open.

Retrospective correction priority: inspect existing reviewed mailbox entries,
especially 20261102T183925Z-founder-charter-deployment-blocked.md and
20261102T193457Z-founder-constitution-correction.md. The Founder WITHDREW
the proposed constitutional amendment; it must NOT be deployed. The earlier
disposition demanding host installation is factually superseded. Publish
a dated correction/addendum referencing the exact prior report, explaining
which conclusions were unsupported. Preserve the original historical record.
Review a meaningful sample of other generic dispositions; independently check
evidence where feasible, otherwise retract verification claims explicitly.
This is a ONE-TIME corrective review, not an instruction to repeat it every
cycle: once evidence-backed addenda are filed, revisit only on new substantive
evidence or an independently identified error.
Do this as independent judicial fact-finding without changing law or your own
measurement machinery. Stop stamping routine Executive status updates.

For continuity_unverified OFFICE, independently inspect the old terminal
evidence at state/appointments/terminal-evidence/ID, preserved Git/board
effects and actual new agent progress. Only if those are demonstrably reconciled
write state/continuity/verified-OFFICE.json with verified_by "judiciary",
verification_scope "external_effect_reconciled", previous_agent and
successor_agent exactly from its reconciliation receipt, and a specific
independent evidence_ref. A successful agent exit is NOT sufficient.
If uncertain, retain the open case and report why.
Randomized audit cases (bounded deep review):
$selection

For each sampled open issue, verify actual host assignment from its description
and latest Founder comments, then investigate unjustified neglect if assigned.
For sampled completed work verify delivery; for government decisions check
lawfulness and effect. Submit an evidence-backed verdict for EVERY sampled case
using $town/government/audit-accountability.py report with --case, --verdict
(verified, not_assigned, finding, inconclusive) and --evidence. Record a
finding for neglect or false delivery, not for a mere absence of information.
For --correction, also supply --cycle-id "$cycle_id". Corrections without this
current dispatch token, or with a token from another dispatch, are rejected.
Use verified_fixed with new evidence only for later independent correction.

Inspect the complete, current ordinary laws at $town/government/LAWS.md and
oversight guidance at $town/government/OVERSIGHT.md.
Independently investigate adverse signals and limitations, publish reproducible
findings and measurement limitations for legislative consideration. Present findings, methods, sampling uncertainty, false positives, missing
measurements and the effectiveness of the Judiciary's OWN operations to the
Legislature. In particular distinguish lack of evidence from a clean result.
The Judiciary may request a parliamentary inquiry and may describe an
observed measurement weakness, but MUST NOT propose, sponsor, ratify or
implement reforms to measurement systems, audit algorithms, institutional
rules or its own operation. Reform proposals and ratification belong ONLY to
the Legislature; authorized implementation belongs to the Executive.
The Clerk MUST consider judicial evidence at every sitting.
Independently measure the effects of previously ratified corrections and report
the evidence, including failures of judicial measurement, to Parliament. Do not merely ask the executive whether
it thinks it is effective. Use Antonina-managed agents; model selection is Antonina's responsibility. Never perform unrelated projects. This is a judicial evidence review, not a legislative vote.
EOF
)
recovery=
if [ -f "$town/government/terminal-continuity.sh" ]; then
  recovery=$(/bin/sh "$town/government/terminal-continuity.sh" instruction judiciary) || exit 1
fi
prompt=$(printf '%s\n\n%s\n' "$prompt" "$recovery")
# Publish identity BEFORE launching a detached agent, otherwise a fast agent
# may correctly report a correction before the CLI has made its token valid.
# The registered token remains the same across repeated dispatches of a
# frozen draw. A failed/ambiguous launch is recorded and not replayed
# immediately, because it may already have started a side-effecting agent.
umask 077
if [ ! -f "$root/audit-cycle-identities.tsv" ] ||
   ! awk -F '\t' -v token="$cycle_id" '$2==token{found=1} END{exit !found}' "$root/audit-cycle-identities.tsv"; then
  printf '%s\t%s\n' "$now" "$cycle_id" >> "$root/audit-cycle-identities.tsv"
fi
printf '%s\n' "$cycle_id" > "$root/current-audit-cycle.tmp"
mv "$root/current-audit-cycle.tmp" "$root/current-audit-cycle"
printf '%s\n' "$now" > "$root/last-audit-dispatch"
policy_file="$town/government/AGENT-REPORTING-POLICY.md"
[ -s "$policy_file" ] || { echo "Viche: mandatory Founder agent policy missing" >&2; exit 1; }
prompt=$(printf '%s\n\n%s\n' "$prompt" "$(cat "$policy_file")")
if ! antonina agent run --id "$id" --cwd "$seats/branches/judiciary" --prompt "$prompt" --detach; then
  printf '%s\t%s\tlaunch_failed_or_ambiguous\n' "$now" "$cycle_id" >> "$root/audit-dispatches.tsv"
  echo "Judiciary: audit launch failed or ambiguous, preserving cycle identity" >&2
  exit 1
fi
printf '%s\t%s\taccepted_not_verified\n' "$now" "$incident" >> "$root/audit-dispatches.tsv"
