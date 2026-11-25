#!/bin/sh
# Shared POSIX helpers for probing a managed Antonina agent's state.
# Sourced, never executed. No network, no scheduler, no state of its own.
#
# Why: Antonina intermittently reports state "unknown" (or fails the status
# query) while a session transitions or recovers. One such sample is not
# evidence that an office is dead, and it is also not evidence that it is idle.
# Callers must therefore re-probe boundedly and then decide; this helper only
# reports what was observed and never invents a state.
#
# agent_state_probe <agent-id> [retries] [delay-seconds]
#   Sets:
#     AGENT_STATE           final observed state, or "unknown"
#     AGENT_STATE_ATTEMPTS  number of status probes performed
#     AGENT_STATE_REASON    why the final value is not a recognized state
#     AGENT_STATE_RAW       single-line, truncated last raw status
#     AGENT_STATE_META      last raw status JSON, or empty
#   Always returns 0.
agent_state_probe() {
  as_id=$1
  as_retries=${2:-3}
  as_delay=${3:-1}
  case "$as_retries" in ''|*[!0-9]*|0) as_retries=1 ;; esac
  case "$as_delay" in ''|*[!0-9]*) as_delay=1 ;; esac
  AGENT_STATE_ATTEMPTS=0
  AGENT_STATE_REASON=
  AGENT_STATE_RAW=
  AGENT_STATE=
  AGENT_STATE_META=
  while [ "$AGENT_STATE_ATTEMPTS" -lt "$as_retries" ]; do
    AGENT_STATE_ATTEMPTS=$((AGENT_STATE_ATTEMPTS + 1))
    if as_meta=$(antonina agent status --id "$as_id" --json 2>/dev/null); then
      AGENT_STATE_META=$as_meta
      AGENT_STATE_RAW=$(printf '%s' "$as_meta" | tr '\n' ' ' | cut -c1-200)
      AGENT_STATE=$(printf '%s\n' "$as_meta" | jq -r '.state // empty' 2>/dev/null) || AGENT_STATE=
      [ -n "$AGENT_STATE" ] || AGENT_STATE=unknown
    else
      AGENT_STATE=unknown
      AGENT_STATE_REASON="status query failed"
    fi
    case "$AGENT_STATE" in
      unknown) [ -n "$AGENT_STATE_REASON" ] || AGENT_STATE_REASON="agent reports 'unknown'" ;;
      *) return 0 ;;
    esac
    [ "$AGENT_STATE_ATTEMPTS" -lt "$as_retries" ] || break
    sleep "$as_delay"
  done
  return 0
}

# dispatch_failure_log <logfile>
# Surface the captured dispatch log instead of hiding the concrete cause in a
# file only an operator would find. Prints the path and its last lines to stderr.
dispatch_failure_log() {
  df_log=$1
  if [ -s "$df_log" ]; then
    printf 'Viche: dispatch log %s (last lines):\n' "$df_log" >&2
    tail -n 5 "$df_log" 2>/dev/null | sed 's/^/Viche:   /' >&2 || :
  else
    printf 'Viche: dispatch log %s is empty or missing\n' "$df_log" >&2
  fi
}
