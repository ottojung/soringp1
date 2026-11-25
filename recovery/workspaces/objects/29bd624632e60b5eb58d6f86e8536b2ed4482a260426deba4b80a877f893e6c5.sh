#!/bin/sh
# Shared agent-state probe: a transient "unknown" is retried boundedly, a
# persistent one is reported with a reason, and a failed dispatch log is
# surfaced instead of hidden. Unit test of government/agent-state.sh.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/bin"
cat > "$d/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
case "$1 $2" in
  "agent status")
    n=$(cat "$MOCK_ROOT/unknown_left" 2>/dev/null || echo 0)
    if [ "$n" -gt 0 ]; then
      printf '%s\n' $((n - 1)) > "$MOCK_ROOT/unknown_left"
      case "${MOCK_SHAPE:-state}" in
        empty) printf '{}\n' ;;
        fail) exit 3 ;;
        *) printf '{"state":"unknown","model":"m","variant":"low"}\n' ;;
      esac
    else
      printf '{"state":"%s","last_activity_at":123,"model":"m","variant":"low"}\n' \
        "$(cat "$MOCK_ROOT/mode")"
    fi ;;
  "agent run") exit "${MOCK_RUN_RC:-0}" ;;
  *) echo "unexpected: $*" >&2; exit 9 ;;
esac
MOCK
chmod +x "$d/bin/antonina"
export PATH="$d/bin:$PATH" MOCK_ROOT="$d/mock"
mkdir -p "$d/mock"
printf 'idle\n' > "$d/mock/mode"
. "$repo/government/agent-state.sh"

# 1. One transient sample, then a recognized state.
printf '1\n' > "$d/mock/unknown_left"
agent_state_probe probe-agent 3 0
[ "$AGENT_STATE" = idle ]
[ "$AGENT_STATE_ATTEMPTS" -eq 2 ]

# 2. Persistent unknown: reported, not invented as idle.
printf '9\n' > "$d/mock/unknown_left"
agent_state_probe probe-agent 3 0
[ "$AGENT_STATE" = unknown ]
[ "$AGENT_STATE_ATTEMPTS" -eq 3 ]
printf '%s' "$AGENT_STATE_REASON" | grep -Fq "unknown"

# 3. A status payload without .state is unknown, not a crash.
printf '9\n' > "$d/mock/unknown_left"
MOCK_SHAPE=empty agent_state_probe probe-agent 2 0
[ "$AGENT_STATE" = unknown ]
[ "$AGENT_STATE_ATTEMPTS" -eq 2 ]

# 4. A failing status query is unknown with a reason.
printf '9\n' > "$d/mock/unknown_left"
MOCK_SHAPE=fail agent_state_probe probe-agent 2 0
[ "$AGENT_STATE" = unknown ]
printf '%s' "$AGENT_STATE_REASON" | grep -Fq "status query failed"

# 5. Dispatch failure surfaces the log tail, not an anonymous error.
: > "$d/log"
i=1
while [ "$i" -le 8 ]; do printf 'line%s\n' "$i" >> "$d/log"; i=$((i + 1)); done
dispatch_failure_log "$d/log" 2> "$d/err"
grep -Fq "line8" "$d/err"
grep -Fq "line4" "$d/err"
if grep -Fq "line3" "$d/err"; then exit 1; fi
echo 'Agent-state probe and dispatch-log transparency smoke passed'
