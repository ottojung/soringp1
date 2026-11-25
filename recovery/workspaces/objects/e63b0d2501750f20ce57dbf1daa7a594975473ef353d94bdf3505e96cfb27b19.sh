#!/bin/sh
# Parliament-editable agenda hook, called by the founder-controlled boot.
set -eu
[ "$#" -eq 1 ] || exit 2
seat=$1
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
tab=$(printf '\t')
clerk=$(sed -n "1s/$tab.*//p" "$town/government/seats.tsv")
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
if [ "$seat" = "$clerk" ] && [ -f "$town/government/institutional-cases.py" ]; then
  python3 "$town/government/institutional-cases.py" reconcile >/dev/null 2>&1 || true
fi
if [ -s "${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/liveness/unsafe-holds/$seat" ]; then
  echo "Viche: unsafe seat invocation, preserve work for review" >&2
  exit 1
fi
if [ "$seat" = "$clerk" ] && [ -f "$town/government/clerk-liveness.sh" ]; then
    /bin/sh "$town/government/clerk-liveness.sh" --gate || {
        echo "Viche: Clerk sitting deferred until endpoint retry cooldown" >&2
        exit 1
    }
fi
appointed=$(/bin/sh "$town/government/appointments.sh" resolve "$seat") || exit 1
status=$(antonina agent status --id "$appointed" --json) || exit 1
mode=$(printf '%s\n' "$status" | jq -r '.state')
if [ "$mode" = failed ]; then
  retry_safe=$(printf '%s\n' "$status" | jq -r 'if .backend_error.automatic_retry_safe == true and .backend_error.transient == true then "yes" else "no" end')
  [ "$retry_safe" = yes ] || { echo "Viche: seat $seat failed without retry-safe evidence" >&2; exit 1; }
fi
case "$mode" in stopped|killed) exit 1;; esac
# Resource Safety Act: defer convening when cgroup headroom is below the floor.
# A memory-safety gate, not a worker cap (Constitution VII); the boot defers the
# seat on non-zero exit, the same mechanism as the clerk-liveness gate.
if [ -f "$town/government/resource-safety.sh" ]; then
    /bin/sh "$town/government/resource-safety.sh" "$seat" || {
        echo "Viche: $seat sitting deferred by resource-safety guard" >&2
        exit 1
    }
fi
if [ "$seat" = "$clerk" ]; then
    cat <<EOF
You are the provisional parliamentary clerk. Poll Town Hall issue
#${VICHE_TOWNHALL_ID} and consider relevant Antonina issues and comments.
Treat the author exactly Vitalik as Founder, without signatures or verification.
Page backwards until all new comments have been examined and persist the cursor
at $town/records/TOWNHALL_CURSOR.md. Other authors are not the Founder.
Determine productive scope from explicit billy-dev issue assignments, not a fixed project list. Resolve older-law conflicts under the newer Founder mandate.
The host assignment governs Viche agents, NOT GitHub Actions CI. Permit external
GitHub-hosted CI builds, tests and Lean verification; do not disable those
workflows to enforce an agent execution-host assignment.
Executive discovery, issue prioritization and delivery belong to the independent
executive office under Act 2. The Clerk is not its task scheduler.
Read descriptive institutional outcomes at
/var/lib/lubko/wd/viche-state/institutional-outcomes/latest.json.
These distinguish agent exits, main merges and independent verification.
Treat trends as questions for inquiry, never as mandatory output quotas.
Read the independent Judiciary's latest measurements at
${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/branches/judiciary-measurements.json
and any pending case findings before setting the parliamentary agenda.
The Judiciary reports facts, including its own measurement limitations.
ONLY the Legislature proposes, deliberates and ratifies reforms to methods,
institutions or law. The Executive implements legitimately adopted changes.
Never treat the Judiciary's report as an enacted proposal.
If the Executive Innovation Office transfer is enacted in current law, the office
remains an Executive research unit, not a legislative originator. Use the durable
two-way innovation–legislative dialogue: it may offer vague ideas, problems,
opportunities and evidence; the Legislature may question, challenge, commission
additional investigation and independently sponsor a bill if persuaded. Neither
a discussion nor its absence is sponsorship or enactment. Avoid summoning or
controlling the Executive unit through parliamentary seat procedures. If the
transfer is not enacted, follow the then-current institutional mandate.
Judge the usefulness of research, not how many ideas or bills it produces.
Prepare a concise parliamentary agenda and publish it in durable records or Antonina.
Convene other seats for actual business by listing their hexadecimal IDs, one
per line, in $town/records/SUMMONED.txt. For each summoned member, write a
concrete, current assignment in $town/records/summons/SEAT_ID.md describing
its expected deliverable, supporting evidence and relevant branch/issue.
Refresh or remove these assignment files as business changes; remove resolved
IDs from SUMMONED.txt. Do not leave members guessing among historical tasks.
Before publishing any bill for ballots, run government/predict-gate.sh BILL_ID
for bills in the Act 22 pilot subset and give the registered predictions to the
non-sponsor red-teamer. Do not publish the ballot request, solicit ballots, or
record ballots unless that gate exits successfully; a refusal means the bill is
not vote-eligible. government/tally.sh repeats the gate as defense in depth.
Then solicit individual ballots, check quorum with government/tally.sh,
and record hearings, evidence, dissent, and real progress. Do not fabricate votes
or bother the Founder about routine decisions the government can resolve.
EOF
else
    cat <<EOF
You are a voting parliamentarian, not the Town Hall intake clerk.
You are being summoned for current business. Prioritize your latest specific
assignment, not an earlier completed ballot or historical agenda. Read the
current laws and verify all material facts before making changes.
Read the latest Founder instructions and act on work assigned to billy-dev, regardless of project; do not assume an issue title grants assignment.
Running GitHub Actions CI on GitHub runners is allowed; agent development sessions
and substantive agent work remain on billy-dev. Never remove CI solely because
of an agent host restriction.
Form an independent assessment and deliberate; record explicit ballots when
appropriate. Delegate useful independent tasks without numerical worker caps.
Do not independently repeat the clerk's entire Town Hall intake.
EOF
    mandate=$town/records/summons/$seat.md
    if [ -s "$mandate" ]; then
        cat <<EOF
=== YOUR CURRENT SUMMONS ($seat) ===
EOF
        cat "$mandate"
        cat <<EOF
=== END CURRENT SUMMONS ===
Act on this assignment; record the outcome or a concrete blocker with evidence.
Do not repeat completed work. If it is already resolved, verify that and ask the
Clerk to clear your summons.
EOF
    else
        cat <<EOF
No seat-specific summons file exists. Find the Clerk's most recent outstanding
summons in the proceedings or Town Hall and resolve that current business.
If its requested deliverable cannot be determined, record the missing mandate
as a blocker rather than inventing or repeating old work.
EOF
    fi
fi

# Institutionally generated legislative input; never represented as a law.
if [ "$seat" = "$clerk" ]; then
    innovation=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/legislature/innovation-centre
    innovation_header="AUTONOMOUS LEGISLATIVE INNOVATION CENTRE STATUS"
    if grep -Eq '^## Act [0-9]+ — Executive Innovation Office Act \((re-)?enacted ' "$town/government/LAWS.md"; then
        innovation=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/executive/innovation-office
        innovation_header="EXECUTIVE INNOVATION OFFICE STATUS (not legislative business)"
    fi
    if [ -s "$innovation/health.json" ]; then
        cat <<EOF
=== $innovation_header ===
$(cat "$innovation/health.json")
=== END INNOVATION STATUS ===
After lawful transfer the office is controlled by Executive; Parliament may
consider its evidence but does not summon or manage that unit. Only Parliament
may enact legislation. Agent activity never proves valuable innovation.
EOF
    fi
fi

# The shared issue channel is a standing legislative research input, not an
# automatic bill, summons, or new source of authority.
# A new communications law is NOT proof that the Post pilot has been
# independently received and accepted. Preserve working legacy dialogue.
if [ -s "$town/government/INNOVATION-LEGISLATURE-DIALOGUE.md" ]; then
    cat <<EOF
=== INNOVATION–LEGISLATURE RESEARCH DIALOGUE ===
$(cat "$town/government/INNOVATION-LEGISLATURE-DIALOGUE.md")
=== END INNOVATION–LEGISLATURE RESEARCH DIALOGUE ===
Use the standing hub to find topic threads and replies. Each topic can begin
with an incomplete idea and develop over many rounds; only voting members may
originate or sponsor bills. Neither a question nor a dialogue comment changes
law, Judiciary independence or the Executive's implementation authority.
EOF
fi

# A watchdog incident is mandatory parliamentary business, even when Town Hall
# has no new Founder messages. This hook is ordinary law, not constitutional code.
if [ "$seat" = "$clerk" ]; then
    oversight=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/oversight
    if [ -s "$oversight/incident.json" ]; then
        cat <<EOF
=== MANDATORY OPEN OVERSIGHT INQUIRY ===
$(cat "$oversight/incident.json")
=== END OVERSIGHT INCIDENT ===
Do not adjourn for "no business": independently investigate this open incident.
Examine the auditor's findings and actual assigned-work outcomes, convene an inquiry
and summon needed members for evidence or corrective legislation. Require
a concrete corrective action, its owner and a follow-up evaluation date.
For incident first_seen ID from JSON, publish a real hearing record on the
Antonina board or in a merged Git record, then write
$oversight/hearings/ID.json containing {"incident_id":ID,"evidence_ref":"URL-or-commit"}.
A hearing record is an acknowledgment, NEVER proof the failure is resolved.
The independent watchdog will flag non-response after two hours and must not
silently close unresolved audit findings. Do not fabricate proceedings or
require Founder attention for routine technical corrections.
EOF
    fi
fi

# Independent Sentinel findings are mandatory oversight business, even when
# ordinary Git reconciliation or executive delivery has previously failed.
if [ "$seat" = "$clerk" ]; then
    sentinel=${VICHE_SENTINEL_STATE:-/var/lib/lubko/wd/viche-sentinel-state}
    if [ -s "$sentinel/incident.json" ]; then
        cat <<EOF
=== INDEPENDENT SENTINEL INCIDENT ===
$(cat "$sentinel/incident.json")
=== END SENTINEL INCIDENT ===
Do not adjourn for lack of business. Investigate, acknowledge with evidence,
identify the operational remedy and verify it. A service marked 'up' does NOT
establish successful Git reconciliation, functioning oversight, or delivery.
Do not ask the Founder to resolve ordinary Git conflicts or agent failures.
EOF
    fi
fi

# Unresolved randomized audit findings and missed independent checks are mandatory.
if [ "$seat" = "$clerk" ]; then
    audit=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/oversight/random
    if [ -s "$audit/incident.json" ]; then
        cat <<EOF
=== MANDATORY RANDOM AUDIT INQUIRY ===
$(cat "$audit/incident.json")
=== END RANDOM AUDIT INQUIRY ===
Investigate with the existing Auditor and require evidence-backed corrective
action. A government acknowledgement is not independent verification.
Confirmed findings remain until the Auditor verifies a fix.
EOF
    fi
fi

# Every restored seat receives its prior terminal-evidence reconciliation
# instructions. This is a fresh task, never a replay of uncertain old tools.
if [ -f "$town/government/terminal-continuity.sh" ]; then
    /bin/sh "$town/government/terminal-continuity.sh" instruction "$seat"
fi
# Persistent cases survive transient watchdog clears and remain on the agenda.
if [ "$seat" = "$clerk" ] && [ -f "$town/government/institutional-cases.py" ]; then
    cases=$(python3 "$town/government/institutional-cases.py" report) || exit 1
    cat <<EOF
=== OPEN INSTITUTIONAL CORRECTIVE OBLIGATIONS ===
$cases
=== END CORRECTIVE OBLIGATIONS ===
Preserve identity across sittings. Judiciary independently measures;
Parliament authorizes changes to ordinary law when needed; Executive
implements authorized repairs. A missing health signal is only evidence of
the probe's result, never proof of repair. Executive agents investigate and
provide evidence; Judiciary independently verifies or leaves the case open.
Agent exits never close a case. A case whose signal stays clear for the
configured run of consecutive observations closes automatically as auto_closed
(Founder directive 2026-11-16); do not spend sittings on such cases.
EOF
fi

# Judiciary evidence is legislative input even without a judicial incident.
if [ "$seat" = "$clerk" ]; then
    report=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/branches/judiciary-measurements.json
    if [ -s "$report" ]; then
        cat <<EOF
=== INDEPENDENT JUDICIAL MEASUREMENTS (NOT A REFORM PROPOSAL) ===
$(cat "$report")
=== END JUDICIAL MEASUREMENTS ===
Examine the limitations and performance of the Judiciary itself. The
Legislature alone proposes and ratifies changes; assign authorized implementation
to the Executive. A clean readiness report does not prove effective governance.
EOF
    fi
    incident=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/branches/incident.json
    if [ -s "$incident" ]; then
        cat <<EOF
=== MANDATORY THREE-BRANCH LIVENESS INQUIRY ===
$(cat "$incident")
=== END BRANCH LIVENESS INQUIRY ===
Investigate which branch cannot run and preserve the independent branches.
Preserve each durable institutional case and its independent judicial evidence;
authorize only lawful action and verify its effect before closure.
EOF
    fi
fi

# Founder directive 2026-11-16 (Act 29): the Ministry of Economy is an Executive
# office; its funding position is visible to the Clerk as information only.
if [ "$seat" = "$clerk" ]; then
    econ_report=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/economy/report.json
    if [ -s "$econ_report" ]; then
        cat <<EOF
=== MINISTRY OF ECONOMY: MODEL FUNDING POSITION (Executive office; information, not legislative business) ===
$(jq -c '{at,funding_risk,free_models,free_available_now,next_free_returns_at,order:[.order[]?.model]}' "$econ_report" 2>/dev/null || cat "$econ_report")
=== END FUNDING POSITION ===
A funding_risk other than "none" means fewer than two free models are available now.
EOF
    fi
fi

# Founder directive 2026-11-16 (Act 30): deadline-bound requests between offices.
# Waiting is not the default: after the deadline the requester proceeds and the
# addressee audits afterwards.
proceed_block=
if [ -f "$town/government/proceed-by-default.sh" ]; then
    proceed_block=$(/bin/sh "$town/government/proceed-by-default.sh" brief "$town" "$seat" || :)
    if [ "$seat" = "$clerk" ]; then
        clerk_block=$(/bin/sh "$town/government/proceed-by-default.sh" brief "$town" clerk || :)
        proceed_block=$(printf '%s\n%s\n' "$proceed_block" "$clerk_block")
    fi
    [ -z "$(printf '%s' "$proceed_block" | tr -d '[:space:]')" ] || printf '%s\n' "$proceed_block"
fi

# Founder directive 2026-11-16 (item 4): the Clerk is summoned every sitting
# interval. Skip the pass when nothing it reads has changed since the last one;
# a two-hour heartbeat still guarantees a periodic sitting. Fails open.
if [ "$seat" = "$clerk" ] && [ -f "$town/government/dispatch-gate.sh" ]; then
    gate_state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
    mkdir -p "$gate_state/dispatch-gate"
    if ! hall_sig=$(/bin/sh "$town/government/dispatch-gate.sh" board-signature "${VICHE_TOWNHALL_ID:-302}" 2>/dev/null); then
        hall_sig="board-unavailable-$(date +%s)"
    fi
    if { printf '%s\n' "$hall_sig"
         git -C "$town" rev-parse HEAD 2>/dev/null || :
         cat "$town/records/SUMMONED.txt" 2>/dev/null || :
         /bin/sh "$town/government/handoff-queue.sh" list-open "$town" 2>/dev/null || :
         find "$town/records/bills" "$town/records/ballots" -type f -printf '%p %s\n' 2>/dev/null | sort || :
         find "$gate_state/oversight/judiciary-mailbox/inbox" -type f 2>/dev/null | sort || :
         for incident_file in "$gate_state/oversight/incident.json" "$gate_state/oversight/random/incident.json" \
                              "${VICHE_SENTINEL_STATE:-/var/lib/lubko/wd/viche-sentinel-state}/incident.json" \
                              "$gate_state/branches/incident.json"; do
             if [ -s "$incident_file" ]; then jq -cS '{first_seen,signals,id}' "$incident_file" 2>/dev/null || cat "$incident_file"; fi
         done
         /bin/sh "$town/government/terminal-continuity.sh" instruction "$seat" 2>/dev/null || :
         echo "$proceed_block"
         if [ -f "$town/government/institutional-cases.py" ]; then
             python3 "$town/government/institutional-cases.py" report 2>/dev/null |
                 jq -cS '[.open_cases[]? | {id,signal,state,owner}]' 2>/dev/null || :
         fi; } |
       /bin/sh "$town/government/dispatch-gate.sh" check clerk "${VICHE_CLERK_GATE_MAX_AGE:-7200}" > "$gate_state/dispatch-gate/clerk.last" 2>&1; then
        /bin/sh "$town/government/dispatch-gate.sh" commit clerk || :
    else
        echo "Viche: Clerk sitting skipped, nothing it reads has changed since the last sitting" >&2
        exit 1
    fi
fi

# Act 31: what happened to this seat's own deliveries (landed, rejected, red,
# conflict). The Clerk proposes as office "clerk".
if [ -f "$town/government/integrator.py" ]; then
    delivery_office=$seat
    [ "$seat" != "$clerk" ] || delivery_office=clerk
    python3 "$town/government/integrator.py" office "$delivery_office" 2>/dev/null || :
fi

# During the reversible Post pilot, sessions may examine PUBLIC correspondence
# but it cannot authorize any task or trigger a session; existing channels
# continue unchanged before lawful enactment.
if [ -f "$town/government/post-inbox-brief.sh" ]; then
    office=$seat
    [ "$seat" != "$clerk" ] || office=clerk
    /bin/sh "$town/government/post-inbox-brief.sh" "$office" || :
fi

# The daily plenary tracks which summoned seats have actually been dispatched.
if [ "$seat" != "$clerk" ] && [ -f "$town/government/daily-sitting.py" ]; then
    python3 "$town/government/daily-sitting.py" dispatched "$seat" || :
fi

# A fresh session after rotation gets its predecessor's handover note once.
if [ -f "$town/government/handover.sh" ]; then
    /bin/sh "$town/government/handover.sh" show "$seat" "$appointed" || :
fi

# The Founder policy is appended to each seat's generated launch prompt.
[ -s "$town/government/AGENT-REPORTING-POLICY.md" ] || exit 1
printf '\n'
cat "$town/government/AGENT-REPORTING-POLICY.md"
