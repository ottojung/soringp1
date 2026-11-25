#!/bin/sh
# Deterministic institutional watchdog: runs without AI, Clerk, or executive consent.
# An alert is a mandatory investigation, NOT a judgment of misconduct.
set -eu
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
root=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/oversight
kawun=${VICHE_KAWUN_REPO:-/workspace/skrynia-apps}
now=${VICHE_OVERSIGHT_NOW:-$(date +%s)}
mkdir -p "$root/hearings"
umask 077
case "$now" in ''|*[!0-9]*) echo 'Invalid watchdog clock' >&2; exit 2;; esac

# Read the actual Antonina board, rather than inferring work from agent activity.
board_ok=true
board=$(antonina board list --state open --page 1 --json 2>"$root/board-error.log") || board_ok=false
open=0
if [ "$board_ok" = true ]; then
    open=$(printf '%s\n' "$board" | jq -er '[.[] | select((.title // "") | test("Kawun|kawunapp|skrynia-apps"; "i"))] | length') || board_ok=false
fi

agent_ok=true
exec_id=$(/bin/sh "$town/government/appointments.sh" resolve executive 2>"$root/agent-error.log") || agent_ok=false
if [ "$agent_ok" = true ]; then
    meta=$(antonina agent status --id "$exec_id" --json 2>"$root/agent-error.log") || agent_ok=false
fi
mode=unknown
reason=unknown
age=-1
if [ "$agent_ok" = true ]; then
    mode=$(printf '%s\n' "$meta" | jq -er '.state') || agent_ok=false
    reason=$(printf '%s\n' "$meta" | jq -r '.backend_error.classification // "none"')
    last=$(printf '%s\n' "$meta" | jq -r '(.last_activity_at // 0) | floor')
    case "$last" in ''|*[!0-9]*) last=0;; esac
    if [ "$last" -gt 0 ] && [ "$last" -le "$now" ]; then age=$((now-last)); fi
fi

# Git is a *leading signal*, not proof of correct completion.
# A stale local tracking branch is explicitly only a local observation.
#
# Delivery age (CA-M): the delivery signal must reflect the newest commit across
# the delivery lines, not origin/main alone. Kawun's active delivery line is
# origin/release/* (e.g. origin/release/along-long-namespace); measuring only
# main false-positives whenever work lands on the release line. We therefore take
# the NEWEST commit across origin/main and every origin/release/* ref. A fresh
# commit on ANY delivery line suppresses the signal. This stays a weak leading
# indicator — not a quota and not proof of deployment. The signal NAME
# `no_recent_main_commit` is retained for continuity with existing incident
# records; its measurement basis is delivery-wide.
main_age=-1
delivery_age=-1
if [ -d "$kawun/.git" ]; then
    if [ "${VICHE_OVERSIGHT_FETCH:-0}" = 1 ]; then
        # Optional, bounded, read-only fetch so delivery refs reflect the remote.
        # Off by default to keep the watchdog deterministic and testable.
        if command -v timeout >/dev/null 2>&1; then
            timeout 30 git -C "$kawun" fetch --quiet --prune 2>/dev/null || :
        else
            git -C "$kawun" fetch --quiet --prune 2>/dev/null || :
        fi
    fi
    newest=
    release_refs=$(git -C "$kawun" for-each-ref --format='%(refname)' refs/remotes/origin/release 2>/dev/null) || release_refs=
    for ref in refs/remotes/origin/main $release_refs; do
        ts=$(git -C "$kawun" log -1 --format=%ct "$ref" 2>/dev/null) || ts=
        case "$ts" in ''|*[!0-9]*) :;; *)
            if [ -z "$newest" ] || [ "$ts" -gt "$newest" ]; then newest=$ts; fi
        ;; esac
    done
    if [ -n "$newest" ] && [ "$newest" -le "$now" ]; then delivery_age=$((now-newest)); fi
    last_commit=$(git -C "$kawun" log -1 --format=%ct refs/remotes/origin/main 2>/dev/null) || last_commit=
    case "$last_commit" in ''|*[!0-9]*) :;; *)
        if [ "$last_commit" -le "$now" ]; then main_age=$((now-last_commit)); fi
    ;; esac
fi

signals=
if [ "$board_ok" != true ] || [ "$agent_ok" != true ]; then
    signals=telemetry_unavailable
elif [ "$open" -gt 0 ]; then
    if [ "$mode" = failed ]; then signals=executive_failed; fi
    if [ "$mode" != running ] && [ "$mode" != failed ] && [ "$age" -ge 1800 ]; then
        signals=${signals:+$signals,}executive_inactive
    fi
    if [ "$mode" = running ] && [ "$age" -ge 7200 ]; then
        signals=${signals:+$signals,}running_without_recent_activity
    fi
    if [ "$delivery_age" -ge 86400 ]; then
        signals=${signals:+$signals,}no_recent_main_commit
    fi
fi

printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$now" "$open" "$mode" "$age" "$main_age" "$delivery_age" "$reason" "${signals:-clear}" >> "$root/observations.tsv"
old=$root/incident.json
if [ -z "$signals" ]; then
    if [ -s "$old" ]; then
        jq -c --argjson now "$now" '. + {closed_at:$now,closure:"signals_cleared_requires_auditor_verification"}' "$old" >> "$root/history.jsonl"
        rm -f "$old"
    fi
    exit 0
fi

first=$now
if [ -s "$old" ]; then
    prior=$(jq -r '.first_seen // 0' "$old") || prior=0
    case "$prior" in ''|*[!0-9]*) :;; *) if [ "$prior" -gt 0 ]; then first=$prior; fi;; esac
fi
hearing=$root/hearings/$first.json
answered=false
if [ -s "$hearing" ]; then
    if jq -e --argjson id "$first" '.incident_id == $id and (.evidence_ref | type == "string" and length > 0)' "$hearing" >/dev/null 2>&1; then
        answered=true
    fi
fi
overdue=false
if [ "$answered" = false ] && [ $((now-first)) -ge 7200 ]; then overdue=true; fi
temp=$(mktemp "$root/incident.XXXXXXXX")
jq -n --argjson first "$first" --argjson now "$now" --arg signals "$signals" \
   --argjson count "$open" --arg mode "$mode" --arg error "$reason" \
    --argjson agent_age "$age" --argjson git_age "$main_age" \
    --argjson delivery_age "$delivery_age" \
    --argjson board_ok "$board_ok" --argjson agent_ok "$agent_ok" \
    --argjson answered "$answered" --argjson overdue "$overdue" \
    '{first_seen:$first,observed_at:$now,signals:($signals|split(",")),open_kawun_issues_first_page:$count,executive_state:$mode,executive_error:$error,executive_last_activity_age_seconds:$agent_age,local_main_commit_age_seconds:$git_age,local_delivery_commit_age_seconds:$delivery_age,board_access_ok:$board_ok,agent_status_ok:$agent_ok,parliamentary_hearing_recorded:$answered,parliamentary_response_overdue:$overdue,assessment:"investigation_required_not_proof_of_misconduct"}' > "$temp"
mv -f "$temp" "$old"
if [ "$overdue" = true ]; then
    printf '%s\t%s\tunanswered oversight incident\n' "$now" "$first" >> "$root/escalations.tsv"
    # Keep the Founder informed even if the model provider cannot run Parliament.
    marker=$root/escalated-$first
    if [ ! -e "$marker" ] && [ -n "${VICHE_TOWNHALL_ID:-}" ]; then
        notice="Viche oversight incident $first has received no parliamentary hearing for two hours. Measured signs: $signals; visible open Kawun issues: $open; executive state: $mode ($reason). Investigation required, not a misconduct verdict. Parliament has this on its mandatory agenda. No routine Founder action requested."
        if antonina board comment --id "$VICHE_TOWNHALL_ID" --author "Viche watchdog" --body "$notice" >/dev/null 2>&1; then
            printf '%s\n' "$now" > "$marker"
        else
            echo 'Viche watchdog: Town Hall notice failed; will retry later' >&2
        fi
    fi
fi
printf 'Viche oversight: %s (incident %s, unanswered=%s)\n' "$signals" "$first" "$overdue" >&2
