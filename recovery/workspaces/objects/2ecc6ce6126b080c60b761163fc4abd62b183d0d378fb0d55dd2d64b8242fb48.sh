#!/bin/sh
# Persistent, autonomous legislative idea generation without voting or summons.
# Research and proposals are NOT laws or implementation authorizations.
set -eu
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
seats=${VICHE_SEATS_ROOT:-/var/lib/lubko/wd/viche-seats}
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
charter=${VICHE_CONSTITUTION:?Founder-controlled Constitution required}
cwd=$seats/branches/innovation-centre
root=$state/legislature/innovation-centre
mkdir -p "$root"
umask 077
now=${VICHE_INNOVATION_NOW:-$(date +%s)}
interval=${VICHE_INNOVATION_INTERVAL:-21600}
case "$now:$interval" in *[!0-9:]*|:*|*:) exit 2;; esac
[ "$interval" -gt 0 ] || { echo 'Innovation cadence must be positive' >&2; exit 2; }
[ -s "$charter" ] || exit 1
# The Founder's constitutional first boot inaugurates the town. Research starts
# on the next cycle, without treating pre-inauguration as a failed office.
[ -f "$state/inaugurated" ] || exit 0
/bin/sh "$town/government/branch-bootstrap.sh" innovation-centre \
    > "$root/bootstrap.log" 2>&1 || { echo 'Innovation Centre bootstrap failed' >&2; exit 1; }
id=$(/bin/sh "$town/government/appointments.sh" ensure innovation-centre)
. "$town/government/agent-state.sh"
agent_state_probe "$id"
status=$AGENT_STATE_META
mode=$AGENT_STATE
last=0
[ ! -s "$root/last-dispatch" ] || last=$(cat "$root/last-dispatch")
case "$last" in ''|*[!0-9]*) echo 'Invalid Innovation Centre timestamp' >&2; exit 1;; esac
dispatched=false
case "$mode" in
  running) readiness=running ;;
  idle|clearexit)
    readiness=ready
    if [ "$last" -eq 0 ] || [ "$now" -lt "$last" ] || [ $((now-last)) -ge "$interval" ]; then
      prompt=$(cat <<EOF
You are Viche's permanent LEGISLATIVE INNOVATION CENTRE, a non-voting and
independent legislative research institution. No parliamentary summons
or executive assignment is required for you to think and work.

=== FOUNDER-CONTROLLED CONSTITUTION ===
$(cat "$charter")
=== END CONSTITUTION ===

Read the standing mandate at $town/government/INNOVATION-CENTRE.md,
the current ordinary laws and recent constitutional Founder mandates,
the legislative programme, recent Judiciary reports, independent audit
evidence, Executive performance, and existing innovation proposals.
Do not infer that a prior proposal was enacted.

YOUR MISSION: Continuously invent and rigorously investigate ORIGINAL ways
to improve Viche ITSELF: governance, institutional architecture, work
coordination, quality, accountability, incentives, safety, and effectiveness.
Look for problems no Founder has mentioned and opportunities without a
preexisting failure. Draw on outside scientific and institutional ideas.

FOUNDER PRIORITY — HIGHEST EXPECTED MARGINAL RETURN ON INVESTMENT:
Judge ideas against continuing with the CURRENT working system, not an
imaginary perfect one. Prioritize plausible large improvements in Viche's
mission throughput, quality, autonomy, or simplicity per TOTAL effort:
implementation, integration, upkeep, regression risk, and especially scarce
Founder and parliamentary attention. Opportunity cost matters.
Look past small repairs and governance polish when they improve something
that already works adequately. Seek high-leverage architectural alternatives
that remove whole classes of friction or failures; explore high-upside
uncertain hypotheses with cheap, falsifiable probes before big commitments.
A tiny intervention with huge payoff is good; a large redesign without
credible gains is bad. Do not create numeric ROI rituals or complexity quotas.
Before promoting a proposal, compare plausible alternatives, state what
valuable work it displaces, and explain why it is a better use of attention.
Do not manufacture a new Act for routine low-impact housekeeping. Genuine
urgent defects can still warrant small targeted fixes.

STRICT SCOPE: You cannot originate or authorize external projects such
as AssemblyP1, SoringP1, or new Founder work goals. Founder alone supplies
new productive missions. Internal Viche reforms may improve how it performs
those existing missions; do not change which missions Viche undertakes.

Explore competing approaches and counterarguments. Examine prior initiatives
to avoid repackaged duplicates. Consult available measurements, and name
uncertainty; independent experiments and disposable prototypes are allowed
ONLY without changing production systems or committing law.
Prefer original, carefully justified ideas over large numbers of proposals.
When relevant, seriously investigate EXISTING software (especially free/open
source) instead of assuming that Viche should build another subsystem.
Compare adopting, adapting, building, or retaining the current approach.
Assess practical fit, flexibility, integration effort, reliability, security,
licensing, maintenance, project health, reversibility, and total cost.
Do NOT assume existing software must be adopted; reject it if unsuitable,
with reasons. The Centre may propose reuse or replacement to Parliament,
but must NOT install, replace or deploy production systems itself.
For each serious candidate record a baseline, expected benefit, estimated
cost/risk, dependencies, counterarguments, falsifiable predictions and how
the Judiciary could independently evaluate adoption. Reject weak ideas.

Develop serious DRAFT legislative proposals for Parliament, using Antonina
board issues titled 'Viche Innovation proposal: ...' and clearly marked
'LEGISLATURE-ONLY / NOT ENACTED / NOT ASSIGNED EXECUTIVE WORK'.
Link evidence and identify alternatives. Never impersonate the Founder.
Parliament alone may debate, amend, and ratify institutional reforms;
Executive implements ONLY duly authorized legislation; Judiciary observes.
You have NO vote, NO autonomous lawmaking, NO authority to deploy changes.
Do not modify government/LAWS.md, voting rules, government boot, constitutional
files or deployment services. Do not merge your own bills as law.

Even when no promising proposal exists, keep an evidence-linked research
trail: what you examined, hypotheses rejected, and remaining uncertainties.
Submit new ideas without waiting for the Founder or parliamentary summons.
Read prior proposals before creating another; no quota or ceremonial reports.

Your independent research worktree is $cwd. Deliver genuinely new insight.
EOF
)
      recovery=
      if [ -f "$town/government/terminal-continuity.sh" ]; then
        recovery=$(/bin/sh "$town/government/terminal-continuity.sh" instruction innovation-centre) || exit 1
      fi
      prompt=$(printf '%s\n\n%s\n' "$prompt" "$recovery")
policy_file="$town/government/AGENT-REPORTING-POLICY.md"
[ -s "$policy_file" ] || { echo "Viche: mandatory Founder agent policy missing" >&2; exit 1; }
prompt=$(printf '%s\n\n%s\n' "$prompt" "$(cat "$policy_file")")
      antonina agent run --id "$id" --cwd "$cwd" --prompt "$prompt" --detach \
        > "$root/dispatch.log" 2>&1 ||
        { echo "Innovation Centre dispatch failed for agent $id" >&2
          dispatch_failure_log "$root/dispatch.log"; exit 1; }
      printf '%s\n' "$now" > "$root/last-dispatch"
      last=$now
      readiness=dispatched
      dispatched=true
    fi ;;
  *) echo "Innovation Centre state '$mode' unresolved after $AGENT_STATE_ATTEMPTS probe(s): $AGENT_STATE_REASON" >&2
     echo "Viche: raw_status=$AGENT_STATE_RAW" >&2
     exit 1 ;;
esac
activity=$(printf '%s\n' "$status" | jq -r '.last_activity_at // 0 | floor')
case "$activity" in ''|*[!0-9]*) activity=0;; esac
temp=$(mktemp "$root/health.XXXXXXXX")
jq -n --arg office innovation-centre --arg id "$id" \
  --arg readiness "$readiness" --arg mode "$mode" \
  --argjson at "$now" --argjson last "$last" --argjson activity "$activity" \
  --argjson dispatched "$dispatched" \
  '{office:$office,legislative_branch:true,voting_seat:false,
    separate_summons:true,agent_id:$id,observed_at:$at,readiness:$readiness,
    agent_state:$mode,last_dispatch_at:$last,last_activity_at:$activity,
    dispatched:$dispatched,quality_verified:false,
    note:"readiness_and_agent_dispatch_do_not_prove_useful_innovation"}' > "$temp"
mv -f "$temp" "$root/health.json"
echo "Viche Innovation Centre: $readiness, last_dispatch=$last"
