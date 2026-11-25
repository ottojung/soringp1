#!/bin/sh
# Recover a terminally failed Clerk while retaining all work and evidence.
# The only model remains the one configured by Antonina's constitutional boot.
set -eu
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
seats=${VICHE_SEATS_ROOT:-/var/lib/lubko/wd/viche-seats}
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/liveness
mkdir -p "$state"
umask 077
seat_id=$(head -n 1 "$town/government/seats.tsv" | cut -f1)
id=$(/bin/sh "$town/government/appointments.sh" ensure "$seat_id")
[ -n "$id" ] || exit 1
metadata=$(antonina agent status --id "$id" --json)
kind=$(printf '%s\n' "$metadata" | jq -r '.state')
reason=$(printf '%s\n' "$metadata" | jq -r '.backend_error.classification // ""')
# The intake and sitting gates must never reuse a terminally failed
# continuation if Antonina classifies automatic retry as unsafe. A cooldown
# expiring authorizes supervisor recovery, NOT direct reuse of that session.
. "$(CDPATH= cd "$(dirname "$0")" && pwd -P)/office-continuity.sh"
now=$(date +%s)
tflag=$(printf '%s\n' "$metadata" | jq -r '.backend_error.transient // false')
unsafe=$(printf '%s\n' "$metadata" | jq -r 'if .backend_error.automatic_retry_safe == false then "yes" else "no" end')
invocation=$(printf '%s\n' "$metadata" | jq -r '.invocation_id // .run_id // .finished_at // ""')
finished=$(printf '%s\n' "$metadata" | jq -r '.finished_at // ""')
if [ "$kind" = failed ]; then
  if oc_is_transient "$reason" "$tflag"; then
    retry_safe=$(printf '%s\n' "$metadata" | jq -r 'if .backend_error.automatic_retry_safe == true and .backend_error.transient == true then "yes" else "no" end')
    oc_record_failure "$state" "$seat_id" "$id" "$invocation" "$reason" "$finished" "$retry_safe" "$now" "$seats/$seat_id"
    [ "$retry_safe" = yes ] || oc_mark_unsafe_hold "$state" "$seat_id" "$id" "$invocation"
  else
    oc_surface_permanent "$state" "$id" "$reason"
  fi
fi
oc_commit_age_signal "$state" "$id" "$seats/$seat_id" "$now"
# Act 19 §3.1: failure-count-based reset, decidable from the durable record
# regardless of the currently-observed state; §3.1.3: permanent failures are
# surfaced above, never silently reset.
oc_worktree=$seats/$seat_id
reset_due=false
if oc_reset_due "$state" "$seat_id" "$now"; then reset_due=true; fi
if [ "$reset_due" = true ]; then
  [ -d "$seats/$seat_id" ] || exit 1
  snapshot=$(mktemp -d "$state/recovery-$(date -u +%Y%m%dT%H%M%SZ)-XXXXXX")
  printf '%s\n' "$metadata" > "$snapshot/agent-status.json"
  antonina agent log --id "$id" --lines 200 > "$snapshot/agent-log-tail.txt" 2>&1 || :
  git -C "$seats/$seat_id" status --short > "$snapshot/worktree-status.txt"
  git -C "$seats/$seat_id" rev-parse HEAD > "$snapshot/worktree-head.txt"
  # Persist the attempted recovery before any destructive agent-metadata operation.
  oc_quiesce_for_reset "$id" || exit 1
  id=$(/bin/sh "$town/government/appointments.sh" replace "$seat_id" "$id" clerk-liveness act19_failure_threshold 'Act 19 threshold reset after durable failure evidence and quiescence')
  printf '%s\n' "$now" > "$state/last-reset-$seat_id"
  oc_clear_failures "$state" "$seat_id"
  printf '%s session_reset=failure_count threshold=%s window=%s cooldown=%s evidence=%s\n' \
    "$(date -u +%FT%TZ)" "$oc_threshold" "$oc_window" "$oc_cooldown" "$snapshot" \
    >> "$state/recoveries.log"
  reset_due=true
  # The preceding verified replacement is the sole reset for this event.
fi
if [ "$reset_due" != true ] && [ "$kind" = failed ] &&
   [ -f "$town/government/terminal-continuity.sh" ]; then
  /bin/sh "$town/government/terminal-continuity.sh" recover "$seat_id" || exit 1
  id=$(/bin/sh "$town/government/appointments.sh" resolve "$seat_id")
  metadata=$(antonina agent status --id "$id" --json)
  kind=$(printf '%s\n' "$metadata" | jq -r '.state')
fi
if [ "${1:-}" = --gate ]; then
  if [ "$kind" = failed ]; then
    retry_safe=$(printf '%s\n' "$metadata" | jq -r 'if .backend_error.automatic_retry_safe == true and .backend_error.transient == true then "yes" else "no" end')
    [ "$retry_safe" = yes ] && [ ! -s "$state/unsafe-holds/$seat_id" ] ||
      { echo "Viche: Clerk terminal failure not safe to re-dispatch" >&2; exit 1; }
  fi
  exit 0
fi
