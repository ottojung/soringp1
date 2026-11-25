#!/bin/sh
# O1: stopped/killed appointments must never auto-renew. A null intent does
# NOT prove accidental termination (an out-of-band human SIGTERM looks
# identical), so ambiguous terminal states record a durable hold for
# agent-led Executive investigation instead of blindly replacing. Only a
# positively dead failed backend turn keeps the automatic reconciliatory
# appointment; explicit stop intent and live runners must never respawn.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/bin" "$d/town/government" "$d/seats/branches/innovation-centre" "$d/seats/branches/innovation-office" "$d/seats/c1a00001" "$d/state" "$d/mock"
git -C "$d/seats/branches/innovation-centre" init -q
git -C "$d/seats/branches/innovation-centre" -c user.name=fixture -c user.email=fixture@example.com commit --allow-empty -qm baseline
git -C "$d/seats/branches/innovation-office" init -q
git -C "$d/seats/branches/innovation-office" -c user.name=fixture -c user.email=fixture@example.com commit --allow-empty -qm office
git -C "$d/seats/c1a00001" init -q
git -C "$d/seats/c1a00001" -c user.name=fixture -c user.email=fixture@example.com commit --allow-empty -qm clerk
printf 'c1a00001\tClerk\tintake\n' > "$d/town/government/seats.tsv"
cat > "$d/town/government/appointments.sh" <<'MOCK'
#!/bin/sh
case "$1" in
  resolve|ensure) cat "$MOCK_ROOT/registry" ;;
  replace)
    [ "$3" = "$(cat "$MOCK_ROOT/registry")" ] || exit 1
    printf '%s\n' "$*" >> "$MOCK_ROOT/replacements"
    printf 'new-agent\n' > "$MOCK_ROOT/registry"
    printf 'new-agent\n' ;;
  *) exit 5 ;;
esac
MOCK
cat > "$d/bin/antonina" <<'MOCK'
#!/bin/sh
case "$1 $2" in
  'agent status') cat "$MOCK_ROOT/$4.json" ;;
  'agent log') echo "mock log" ;;
  *) exit 6 ;;
esac
MOCK
chmod +x "$d/bin/antonina" "$d/town/government/appointments.sh"
cp "$repo/government/terminal-continuity.sh" "$d/town/government/terminal-continuity.sh"
export PATH="$d/bin:$PATH" MOCK_ROOT="$d/mock"
export VICHE_TOWN_ROOT="$d/town" VICHE_SEATS_ROOT="$d/seats" VICHE_STATE_ROOT="$d/state"

# Control: a positively dead failed backend turn still earns the automatic
# reconciliatory appointment with durable evidence, never a prompt replay.
printf 'old-agent\n' > "$d/mock/registry"
: > "$d/mock/replacements"
printf '{"state":"failed","alive":false,"active_runner":false,"intent":null,"native_session_id":"ses_failed","steers_pending":0,"finished_at":1000.0,"backend_error":{"classification":"transient_backend_server_error","transient":true,"automatic_retry_safe":false}}\n' > "$d/mock/old-agent.json"
/bin/sh "$repo/government/terminal-continuity.sh" recover innovation-centre
test "$(cat "$d/mock/registry")" = new-agent
test "$(wc -l < "$d/mock/replacements")" -eq 1
jq -e '.state=="awaiting_reconciliation" and .previous_agent=="old-agent"' "$d/state/continuity/reconciliation-innovation-centre.json" >/dev/null

reset_office() {
  printf 'old-agent\n' > "$d/mock/registry"
  : > "$d/mock/replacements"
  rm -f "$d/state/continuity/reconciliation-innovation-centre.json"
  rm -f "$d/state/liveness/unsafe-holds/innovation-centre"
}

# Null-intent killed: ambiguous (human SIGTERM looks identical). No renewal;
# a durable hold is recorded exactly once for agent-led investigation.
reset_office
printf '{"state":"killed","alive":false,"active_runner":null,"intent":null,"native_session_id":"ses_killed","steers_pending":0,"finished_at":2000.0,"backend_error":null}\n' > "$d/mock/old-agent.json"
if /bin/sh "$repo/government/terminal-continuity.sh" recover innovation-centre 2>"$d/killed-err"; then
  echo 'killed null-intent strand auto-renewed' >&2; exit 1
fi
test "$(cat "$d/mock/registry")" = old-agent
test "$(wc -l < "$d/mock/replacements")" -eq 0
test ! -e "$d/state/continuity/reconciliation-innovation-centre.json"
grep -Fq 'old-agent' "$d/state/liveness/unsafe-holds/innovation-centre"
grep -Fq 'ambiguous intent' "$d/killed-err"
# Repeated polls are not new invocations: the same hold is recorded once.
if /bin/sh "$repo/government/terminal-continuity.sh" recover innovation-centre 2>/dev/null; then
  echo 'killed re-poll unexpectedly renewed' >&2; exit 1
fi
test "$(wc -l < "$d/state/liveness/unsafe-holds/innovation-centre")" -eq 1
test "$(wc -l < "$d/mock/replacements")" -eq 0

# Explicit stop intent: a positive manual stop must never respawn.
reset_office
printf '{"state":"stopped","alive":false,"active_runner":false,"intent":"stop","native_session_id":"ses_stop","steers_pending":0,"finished_at":3000.0,"backend_error":null}\n' > "$d/mock/old-agent.json"
if /bin/sh "$repo/government/terminal-continuity.sh" recover innovation-centre 2>"$d/stop-err"; then
  echo 'intentional stop respawned' >&2; exit 1
fi
test "$(cat "$d/mock/registry")" = old-agent
test "$(wc -l < "$d/mock/replacements")" -eq 0
grep -Fq 'intentionally stopped' "$d/stop-err"

# Live runner: an uncertain active process must never be duplicated.
reset_office
printf '{"state":"stopped","alive":false,"active_runner":true,"intent":null,"native_session_id":"ses_live","steers_pending":0,"finished_at":4000.0,"backend_error":null}\n' > "$d/mock/old-agent.json"
if /bin/sh "$repo/government/terminal-continuity.sh" recover innovation-centre 2>"$d/live-err"; then
  echo 'live runner duplicated' >&2; exit 1
fi
test "$(cat "$d/mock/registry")" = old-agent
test "$(wc -l < "$d/mock/replacements")" -eq 0
test ! -e "$d/state/liveness/unsafe-holds/innovation-centre"
grep -Fq 'live process' "$d/live-err"

# Unknown: a transient observation is neither terminal nor idle evidence.
reset_office
printf '{"state":"unknown","alive":true,"active_runner":null,"intent":null,"native_session_id":"ses_unknown","steers_pending":0,"backend_error":null}\n' > "$d/mock/old-agent.json"
if ! /bin/sh "$repo/government/terminal-continuity.sh" recover innovation-centre 2>/dev/null; then
  echo 'unknown observation treated as terminal' >&2; exit 1
fi
test "$(cat "$d/mock/registry")" = old-agent
test "$(wc -l < "$d/mock/replacements")" -eq 0
test ! -e "$d/state/liveness/unsafe-holds/innovation-centre"

# Clerk gate: a terminally killed Clerk must block intake/sitting dispatch,
# not pass silently. A healthy idle Clerk still passes.
printf 'clerk-agent\n' > "$d/mock/registry"
printf '{"state":"killed","alive":false,"active_runner":false,"intent":null,"native_session_id":"ses_clerk","steers_pending":0,"finished_at":5000.0,"backend_error":null}\n' > "$d/mock/clerk-agent.json"
if /bin/sh "$repo/government/clerk-liveness.sh" --gate 2>"$d/gate-err"; then
  echo 'Clerk gate passed a killed appointment' >&2; exit 1
fi
grep -Fq 'clerk-agent' "$d/state/liveness/unsafe-holds/c1a00001"
printf '{"state":"idle","alive":false,"active_runner":false,"intent":null,"native_session_id":"ses_clerk2","steers_pending":0,"backend_error":null}\n' > "$d/mock/clerk-agent.json"
rm -f "$d/state/liveness/unsafe-holds/c1a00001"
if ! /bin/sh "$repo/government/clerk-liveness.sh" --gate 2>/dev/null; then
  echo 'Clerk gate blocked a healthy appointment' >&2; exit 1
fi

# Clerk gate branch in isolation (no terminal-continuity to run first): a
# still-terminal killed Clerk at gate time is refused reconciliation, not reuse.
mkdir -p "$d/town2/government"
cp "$d/town/government/appointments.sh" "$d/town2/government/appointments.sh"
cp "$d/town/government/seats.tsv" "$d/town2/government/seats.tsv"
printf 'clerk-agent\n' > "$d/mock/registry"
printf '{"state":"killed","alive":false,"active_runner":false,"intent":null,"native_session_id":"ses_clerk3","steers_pending":0,"finished_at":6000.0,"backend_error":null}\n' > "$d/mock/clerk-agent.json"
if VICHE_TOWN_ROOT="$d/town2" /bin/sh "$repo/government/clerk-liveness.sh" --gate 2>"$d/gate2-err"; then
  echo 'Clerk gate passed terminal killed state' >&2; exit 1
fi
grep -Fq 'reconciliation required' "$d/gate2-err"
echo 'Terminal-continuity O1 hold-not-renew smoke passed'
