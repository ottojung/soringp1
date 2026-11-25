# Act 19 (Office Continuity and Handoff Integrity Act) §3 shared supervisor
# helpers. Sourced by the office supervisors; never executed directly.
# POSIX /bin/sh only: no `local`, no bashisms, no top-level side effects.
# All variables are prefixed oc_ so callers are not clobbered.
#
# §3.1 starting values set by the Legislature (records/bills/office-continuity-act.md):
#   oc_threshold consecutive transient failures, oc_window seconds (30 min),
#   oc_cooldown seconds between resets for the same office (1800 s).
# Retuning is a recorded, Judiciary-reviewed change to this file, not a silent knob.

oc_threshold=3
oc_window=1800
oc_cooldown=1800

# A failure counts toward the reset only when the runtime classifies it as
# transient: the observed classes from the 2026-10-17 API-key expiry
# (unrecognized_backend_failure) and endpoint outages, or any classification
# whose `transient` flag is true. Everything else is permanent: surfaced, never
# silently reset.
oc_is_transient() {
  [ "$2" = true ] && return 0
  case "$1" in
    upstream_endpoint_unavailable|unrecognized_backend_failure) return 0 ;;
  esac
  return 1
}

# Record a terminal invocation once, independently of its disposable agent ID.
# Event identity is (agent ID, finished_at, invocation id when supplied). This
# makes repeated polling idempotent while preserving separate runs of one agent.
# Line format: "<finished_at> <agent-id> <invocation-id> <classification> <head>".
# Progress guard (§3.1.2): a durable commit since the previous failure breaks
# the consecutive streak, so the record is truncated before appending.
oc_record_failure() {
  # $1 liveness dir, $2 office key, $3 agent id, $4 invocation identity,
  # $5 classification, $6 finished_at, $7 retry-safe (yes/no), $8 now,
  # $9 workdir
  mkdir -p "$1/failures" || return 1
  oc_log=$1/failures/events.tsv
  oc_sha=$(git -C "$9" rev-parse HEAD 2>/dev/null || printf -- -)
  if [ -n "$4" ]; then oc_event=$4; elif [ -n "$6" ]; then oc_event=$6; else return 1; fi
  if [ -n "$6" ]; then oc_finished=$6; else return 1; fi
  case "$oc_event" in ''|*[!a-zA-Z0-9_.:-]*) return 1;; esac
  # Antonina's finished_at is often fractional UNIX seconds. Preserve the
  # exact invocation identity, but use integer seconds for the window math.
  printf '%s\n' "$oc_finished" | grep -Eq '^[0-9]+(\.[0-9]+)?$' || return 1
  oc_finished_seconds=${oc_finished%%.*}
  if [ -s "$oc_log" ] && awk -F '\t' -v office="$2" -v id="$3" -v inv="$oc_event" \
      '$2==office && $3==id && $4==inv {found=1} END {exit !found}' "$oc_log"; then
    return 0
  fi
  # A head transition is durable progress even if a later checkout returns to
  # an earlier commit. Advance the per-office streak watermark before the new
  # event so pre-progress rows can never be counted again.
  oc_head_marker=$1/last-head-$2
  oc_previous_head=
  if [ -s "$oc_head_marker" ]; then
    oc_previous_head=$(cat "$oc_head_marker")
  elif [ -s "$oc_log" ]; then
    oc_previous_head=$(awk -F '\t' -v office="$2" '$2==office {head=$7} END {print head}' "$oc_log")
  fi
  if [ "$oc_sha" != - ] && [ -n "$oc_previous_head" ] && [ "$oc_previous_head" != "$oc_sha" ]; then
    oc_count=$(wc -l < "$oc_log")
    printf '%s\n' "$oc_count" > "$1/reset-sequence-$2"
  fi
  if [ "$oc_sha" != - ]; then printf '%s\n' "$oc_sha" > "$oc_head_marker"; fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$oc_finished_seconds" "$2" "$3" "$oc_event" "$5" "$7" "$oc_sha" >> "$oc_log"
  return 0
}

# Before a lawful threshold reset, require the existing invocation to be
# quiescent so two live agents cannot edit the same seat worktree. Stop only
# when the current observed invocation is running; preserve evidence first.
oc_quiesce_for_reset() {
  oc_reset_id=$1
  oc_stop_meta=$(antonina agent status --id "$oc_reset_id" --json) || return 1
  oc_stop_state=$(printf '%s\n' "$oc_stop_meta" | jq -er '.state') || return 1
  case "$oc_stop_state" in
    running)
      antonina agent stop --id "$oc_reset_id" >&2 || return 1
      oc_stop_try=0
      while [ "$oc_stop_try" -lt 8 ]; do
        oc_stop_meta=$(antonina agent status --id "$oc_reset_id" --json) || return 1
        oc_stop_state=$(printf '%s\n' "$oc_stop_meta" | jq -er '.state') || return 1
        case "$oc_stop_state" in stopped|killed|failed) return 0 ;; esac
        oc_stop_try=$((oc_stop_try+1))
        sleep 1
      done
      echo "Viche: $oc_reset_id did not quiesce; keeping current appointment" >&2
      return 1 ;;
    idle|clearexit|stopped|killed|failed) return 0 ;;
    *) return 1 ;;
  esac
}

# Decide from the failure record alone (§3.1.5) whether a bounded reset is due:
# at least oc_threshold failures inside oc_window, cooldown expired. The
# currently-observed agent state is irrelevant to this decision.
oc_reset_due() {
  # $1 liveness dir, $2 office key, $3 now; returns 0 when a reset is due
  oc_log=$1/failures/events.tsv
  [ -s "$oc_log" ] || return 1
  oc_count=0
  oc_after=0
  if [ -s "$1/reset-sequence-$2" ]; then
    oc_after=$(cat "$1/reset-sequence-$2")
    case "$oc_after" in ''|*[!0-9]*) oc_after=0;; esac
  fi
  oc_now_sha=
  if [ -n "${oc_worktree:-}" ]; then
    oc_now_sha=$(git -C "$oc_worktree" rev-parse HEAD 2>/dev/null || true)
  fi
  oc_line=0
  while IFS="$(printf '\t')" read -r oc_finished oc_office oc_agent oc_inv oc_cls oc_safe oc_sha; do
    oc_line=$((oc_line+1))
    [ "$oc_line" -gt "$oc_after" ] || continue
    case "$oc_finished" in ''|*[!0-9]*) continue ;; esac
    [ "$oc_office" = "$2" ] || continue
    if [ -n "$oc_now_sha" ] && [ "$oc_sha" != "$oc_now_sha" ]; then continue; fi
    if [ $((oc_finished + oc_window)) -gt "$3" ]; then
      oc_count=$((oc_count + 1))
    fi
  done < "$oc_log"
  [ "$oc_count" -ge "$oc_threshold" ] || return 1
  oc_last=0
  if [ -s "$1/last-reset-$2" ]; then
  oc_last=$(cat "$1/last-reset-$2")
    case "$oc_last" in ''|*[!0-9]*) oc_last=0 ;; esac
  fi
  [ $((oc_last + oc_cooldown)) -le "$3" ] || return 1
  return 0
}

# Clear the consecutive-failure record after a reset so the next streak starts
# at zero. History remains auditable in recoveries.log and the incident log.
oc_clear_failures() {
  # Keep the append-only history and establish the next per-office streak
  # boundary at the event ledger's current end.
  mkdir -p "$1/failures" || return 1
  oc_log=$1/failures/events.tsv
  oc_count=0
  [ ! -f "$oc_log" ] || oc_count=$(wc -l < "$oc_log")
  printf '%s\n' "$oc_count" > "$1/reset-sequence-$2"
  return 0
}

# Mark an unsafe failed invocation as requiring explicit handoff review before
# any new session can dispatch work. The durable intent remains open in the
# handoff queue; this marker prevents an automatic duplicate side effect.
oc_mark_unsafe_hold() {
  # $1 liveness dir, $2 office key, $3 agent id, $4 invocation
  mkdir -p "$1/unsafe-holds" || return 1
  oc_hold_file=$1/unsafe-holds/$2
  oc_hold_line=$(printf '%s\t%s\t%s' "$2" "$3" "$4")
  # Repeated 3-minute observations are not new invocations; the same
  # unsafe hold must be recorded ONCE, not 158 times or once per sitting.
  if [ -s "$oc_hold_file" ] && grep -Fxq "$oc_hold_line" "$oc_hold_file"; then
    return 0
  fi
  printf '%s\n' "$oc_hold_line" >> "$oc_hold_file"
}

# Surface a permanent or UNCLASSIFIED failure exactly once per agent and
# classification. An absent backend_error is NOT evidence of permanence.
# Durable incident records survive restart without flooding each sitting.
oc_surface_permanent() {
  # $1 liveness dir, $2 agent id, $3 classification
  mkdir -p "$1" || return 1
  case "$2:$3" in *[!a-zA-Z0-9_:-]*|'') return 1;; esac
  if [ -n "$3" ]; then
    oc_kind=permanent_failure
    oc_class=$3
  else
    oc_kind=unclassified_failure
    oc_class=missing_backend_classification
  fi
  # The durable append IS the dedup marker. A crash before appending
  # must not leave a separate empty marker that suppresses future reports.
  # Every seat/agent has its own immutable id; repeated observations of that
  # same incident cannot increment the count. Concurrent record attempts
  # may append the same line twice, but can never erase or suppress it.
  oc_record="id=$2 $oc_kind classification=$oc_class surfaced-not-reset"
  if [ -f "$1/permanent-incidents.log" ] &&
     grep -Fq "$oc_record" "$1/permanent-incidents.log"; then
    return 0
  fi
  printf '%s %s\n' "$(date -u +%FT%TZ)" "$oc_record" >> "$1/permanent-incidents.log" || return 1
  echo "Viche: $oc_kind id=$2 classification=$oc_class surfaced, not reset (Act 19 §3.1)" >&2
  return 0
}

# Per-office commit-age signal (§3.3): recorded only while the office has
# uncommitted work. This is an observation (weak proxy), not a quota: it makes
# bounded work loss visible instead of looking merely "busy".
oc_commit_age_signal() {
  # $1 liveness dir, $2 agent id, $3 workdir, $4 now
  if [ ! -d "$3/.git" ] && [ ! -f "$3/.git" ]; then
    return 0
  fi
  oc_dirty=$(git -C "$3" status --porcelain 2>/dev/null || true)
  [ -n "$oc_dirty" ] || return 0
  oc_head=$(git -C "$3" rev-parse HEAD 2>/dev/null) || return 0
  [ -n "$oc_head" ] || return 0
  oc_cts=$(git -C "$3" show -s --format=%ct "$oc_head" 2>/dev/null) || return 0
  case "$oc_cts" in ''|*[!0-9]*) return 0 ;; esac
  mkdir -p "$1/commit-age" || return 1
  oc_age=$(($4 - oc_cts))
  printf '%s id=%s head=%s commit_age_seconds=%s uncommitted=yes\n' \
    "$(date -u +%FT%TZ)" "$2" "$oc_head" "$oc_age" >> "$1/commit-age.log"
  printf '%s %s %s\n' "$4" "$oc_cts" "$oc_head" > "$1/commit-age/$2"
  return 0
}
