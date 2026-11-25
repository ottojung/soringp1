#!/bin/sh
# Hermetic test of independent, clocked failure detection and auditor dispatch.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
mkdir -p "$scratch/bin" "$scratch/town/government" "$scratch/town/records" "$scratch/state" "$scratch/seats/branches/judiciary"
printf 'authoritative fixture\n' > "$scratch/charter"
: > "$scratch/town/records/SUMMONED.txt"
cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
case "$1 $2" in
"board comment")
    printf "posted\\n" >> "$NOTICES"
    ;;
"board list")
    printf '%s\n' "$MOCK_BOARD"
    ;;
"agent status")
    case "$*" in
        *c1e00008*) printf '{"state":"%s","model":"%s","variant":"%s"}\n' "$AUDIT_STATE" "$MODEL" "$VARIANT";;
        *) printf '{"state":"%s","last_activity_at":%s,"backend_error":{"classification":"%s"}}\n' "$EXEC_STATE" "$LAST" "$ERROR";;
    esac
    ;;
"agent run")
    case "$*" in
        *"authoritative fixture"*) printf 'audit-dispatch\n' >> "$DISPATCHES";;
        *) exit 70;;
    esac
    ;;
*) exit 90 ;;
esac
MOCK
chmod +x "$scratch/bin/antonina"
PATH=$scratch/bin:$PATH
mkdir -p "$scratch/town/government"
cp "$repo/tests/appointment-id-stub.sh" "$scratch/town/government/appointments.sh"
cp "$repo/government/AGENT-REPORTING-POLICY.md" "$scratch/town/government/AGENT-REPORTING-POLICY.md"
cp "$repo/government/delivery-candidates.py" "$scratch/town/government/delivery-candidates.py"
cp "$repo/government/agent-state.sh" "$scratch/town/government/agent-state.sh"
VICHE_TOWN_ROOT=$scratch/town
VICHE_SEATS_ROOT=$scratch/seats
VICHE_STATE_ROOT=$scratch/state
VICHE_CONSTITUTION=$scratch/charter
VICHE_KAWUN_REPO=$scratch/unavailable-kawun
VICHE_OVERSIGHT_NOW=20000
MOCK_BOARD='[{"number":152,"title":"Kawun: audit secrets"},{"number":43,"title":"Unrelated project"}]'
EXEC_STATE=failed
ERROR=upstream_endpoint_unavailable
LAST=19500
AUDIT_STATE=idle
MODEL=test-provider/example
VARIANT=low
DISPATCHES=$scratch/dispatches
NOTICES=$scratch/notices
VICHE_TOWNHALL_ID=302
export PATH VICHE_TOWN_ROOT VICHE_SEATS_ROOT VICHE_STATE_ROOT VICHE_CONSTITUTION
export VICHE_KAWUN_REPO VICHE_OVERSIGHT_NOW MOCK_BOARD EXEC_STATE ERROR LAST
VICHE_AUDIT_SELECTION=0
VICHE_AUDIT_CHECKS=0
export AUDIT_STATE MODEL VARIANT DISPATCHES NOTICES VICHE_TOWNHALL_ID VICHE_AUDIT_SELECTION VICHE_AUDIT_CHECKS
/bin/sh "$repo/government/oversight-watch.sh"
incident=$scratch/state/oversight/incident.json
jq -e '.first_seen == 20000 and (.signals | index("executive_failed")) and .open_kawun_issues_first_page == 1' "$incident" >/dev/null
/bin/sh "$repo/government/audit-cycle.sh"
[ "$(wc -l < "$DISPATCHES")" -eq 1 ]
/bin/sh "$repo/government/audit-cycle.sh"
[ "$(wc -l < "$DISPATCHES")" -eq 1 ]

VICHE_OVERSIGHT_NOW=28001
export VICHE_OVERSIGHT_NOW
/bin/sh "$repo/government/oversight-watch.sh"
jq -e '.parliamentary_response_overdue == true and .parliamentary_hearing_recorded == false and .first_seen == 20000' "$incident" >/dev/null
[ "$(wc -l < "$NOTICES")" -eq 1 ]
/bin/sh "$repo/government/oversight-watch.sh"
[ "$(wc -l < "$NOTICES")" -eq 1 ]

printf '%s\n' '{"incident_id":20000,"evidence_ref":"https://example.com/hearing"}' > "$scratch/state/oversight/hearings/20000.json"
/bin/sh "$repo/government/oversight-watch.sh"
jq -e '.parliamentary_response_overdue == false and .parliamentary_hearing_recorded == true' "$incident" >/dev/null
printf '%s\n' c1a00008 > "$scratch/town/records/SUMMONED.txt"
/bin/sh "$repo/government/audit-cycle.sh"
[ "$(wc -l < "$DISPATCHES")" -eq 2 ]

: > "$scratch/town/records/SUMMONED.txt"
MODEL=other-provider/other-model
export MODEL
/bin/sh "$repo/government/audit-cycle.sh"
[ "$(wc -l < "$DISPATCHES")" -eq 2 ]
MODEL=test-provider/example
EXEC_STATE=idle
MOCK_BOARD='[]'
export MODEL EXEC_STATE MOCK_BOARD
/bin/sh "$repo/government/oversight-watch.sh"
[ ! -e "$incident" ]
[ -s "$scratch/state/oversight/history.jsonl" ]
echo 'Independent oversight smoke checks passed'
