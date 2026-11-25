#!/bin/sh
# Act 29: the Ministry of Economy is an Executive office. Dormant until the Act is
# enacted; then the deterministic model refresh runs without a model call, and
# the Ministry's agent is dispatched only when its stable inputs change.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/town/government" "$d/seats" "$d/state" "$d/bin"
g=$d/town/government
for f in executive-economy-cycle.sh dispatch-gate.sh proceed-by-default.sh terminal-continuity.sh \
         MINISTRY-OF-ECONOMY.md AGENT-REPORTING-POLICY.md; do
  cp "$repo/government/$f" "$g/$f"
done
printf 'c1a00001\tClerk\tx\n' > "$g/seats.tsv"
cat > "$g/appointments.sh" <<'STUB'
#!/bin/sh
[ "$1 $2" = 'ensure economy' ] || exit 2
echo c1e00012
STUB
cat > "$g/branch-bootstrap.sh" <<'STUB'
#!/bin/sh
[ "$1" = economy ] || exit 2
mkdir -p "$VICHE_SEATS_ROOT/branches/economy"
STUB
# Stand-in for the funding instrument: records that it ran (the real one is tested separately).
cat > "$g/economy-models.py" <<'STUB'
#!/usr/bin/env python3
import os, sys
open(os.environ["MOCK_REFRESH_LOG"], "a").write(" ".join(sys.argv[1:]) + "\n")
if os.environ.get("MOCK_REFRESH_SLOW"):
    import time; time.sleep(2)
STUB
cat > "$g/economy-resources.py" <<'STUB'
#!/usr/bin/env python3
import os, sys
open(os.environ["MOCK_RESOURCES_LOG"], "a").write(" ".join(sys.argv[1:]) + "\n")
STUB
cat > "$d/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
case "$1 $2" in
  'agent status') printf '{"state":"%s"}\n' "$MODE" ;;
  'agent run')
    case "$*" in *'MINISTRY OF ECONOMY'*'Act 29'*'Luna models'*'at the very bottom'*) : ;;
      *) echo 'prompt lacks the Ministry mandate or the tier rule' >&2; exit 1 ;; esac
    case "$*" in *'LATEST FUNDING REPORT'*'funding_risk'*) : ;; *) echo 'no funding report in prompt' >&2; exit 1 ;; esac
    case "$*" in *'LATEST RESOURCE REPORT'*'availability of EVERY scarce resource'*'NEEDS-FOUNDER:'*) : ;;
      *) echo 'prompt lacks the resource report or the broadened mandate' >&2; exit 1 ;; esac
    printf 'sent\n' >> "$DISPATCHES" ;;
  *) echo "unexpected: $*" >&2; exit 9 ;;
esac
MOCK
chmod +x "$d/bin/antonina"
git -C "$d/town" init -q
git -C "$d/town" -c user.name=t -c user.email=t@example.invalid add -A
git -C "$d/town" -c user.name=t -c user.email=t@example.invalid commit -qm fixture
printf 'Founder test constitution\n' > "$d/constitution"
mkdir -p "$d/state/economy"
printf '{"at":"x","funding_risk":"none","free_available_now":3,"order":[],"probes_run":[]}\n' > "$d/state/economy/report.json"
export PATH="$d/bin:$PATH" VICHE_TOWN_ROOT="$d/town" VICHE_SEATS_ROOT="$d/seats" VICHE_STATE_ROOT="$d/state" \
  VICHE_CONSTITUTION="$d/constitution" MODE=idle DISPATCHES="$d/runs" MOCK_REFRESH_LOG="$d/refresh.log" \
  MOCK_RESOURCES_LOG="$d/resources.log"
: > "$d/runs"; : > "$d/refresh.log"; : > "$d/resources.log"
cycle() { /bin/sh "$g/executive-economy-cycle.sh"; }
dispatches() { wc -l < "$d/runs"; }
settle() { # wait for the backgrounded refresh to finish
  i=0; while [ "$i" -lt 50 ] && ! { [ -s "$d/refresh.log" ] || [ "${1:-}" = none ]; }; do sleep 0.1; i=$((i+1)); done
}

# Dormant: Act 29 is not enacted, so nothing runs and no state appears.
printf '# Laws\n\n## Act 25 — Executive Innovation Office Act\n' > "$g/LAWS.md"
cycle
test "$(dispatches)" -eq 0; test ! -s "$d/refresh.log"; test ! -e "$d/state/executive/economy"

# Enacted: the refresh runs in the background (no model), the agent is dispatched once.
printf '\n## Act 29 — Ministry of Economy Act (enacted by Founder directive, 2026-11-16)\n' >> "$g/LAWS.md"
cycle
settle
grep -q '^refresh$' "$d/refresh.log"
test "$(dispatches)" -eq 1
jq -e '.office == "economy" and .executive_office == true and .legislative_branch == false and .voting_seat == false
       and .controlled_by == "executive" and .readiness == "dispatched"' "$d/state/executive/economy/health.json" >/dev/null
test -d "$d/seats/branches/economy"

# Same inputs, 12h pass: not dispatched again (stable-input gate), and the 6h refresh interval holds.
printf '1\n' > "$d/state/executive/economy/last-dispatch"      # dispatched "long ago" (12h gate open)
printf '1\n' > "$d/state/executive/economy/last-refresh"
: > "$d/refresh.log"
cycle
settle
jq -e '.readiness == "skipped_unchanged"' "$d/state/executive/economy/health.json" >/dev/null
test "$(dispatches)" -eq 1
grep -q '^refresh$' "$d/refresh.log"                           # refresh is independent of the agent gate

# Volatile report fields do not wake the agent; a real change in funding does.
printf '1\n' > "$d/state/executive/economy/last-dispatch"
printf '{"at":"y","funding_risk":"none","free_available_now":3,"order":[],"probes_run":["m"],"backup":"b"}\n' > "$d/state/economy/report.json"
cycle
test "$(dispatches)" -eq 1
printf '1\n' > "$d/state/executive/economy/last-dispatch"
printf '{"at":"z","funding_risk":"high","free_available_now":0,"order":[],"probes_run":[]}\n' > "$d/state/economy/report.json"
cycle
test "$(dispatches)" -eq 2
jq -e '.readiness == "dispatched"' "$d/state/executive/economy/health.json" >/dev/null

# A busy agent is never interrupted; an unknown state is reported unhealthy.
printf '1\n' > "$d/state/executive/economy/last-dispatch"
MODE=running cycle
test "$(dispatches)" -eq 2
jq -e '.readiness == "running"' "$d/state/executive/economy/health.json" >/dev/null
rc=0; MODE=failed cycle 2>/dev/null || rc=$?
test "$rc" -eq 1

# At risk, the refresh runs hourly rather than every six hours.
now=$(date +%s)
printf '%s\n' "$((now - 4000))" > "$d/state/executive/economy/last-refresh"
: > "$d/refresh.log"
cycle
settle
grep -q '^refresh$' "$d/refresh.log"
printf '%s\n' "$((now - 4000))" > "$d/state/executive/economy/last-refresh"
printf '{"at":"z","funding_risk":"none","free_available_now":3,"order":[],"probes_run":[]}\n' > "$d/state/economy/report.json"
: > "$d/refresh.log"
cycle
sleep 0.3
test ! -s "$d/refresh.log"                                     # healthy funding: 4000s < 6h, no refresh

# Resource steward: runs on the first cycle with no model call, then every 30 minutes; every 10 while short.
i=0; while [ "$i" -lt 50 ] && [ ! -s "$d/resources.log" ]; do sleep 0.1; i=$((i+1)); done
grep -q '^refresh$' "$d/resources.log"
: > "$d/resources.log"
printf '%s\n' "$((now - 1000))" > "$d/state/executive/economy/last-resource-refresh"
cycle; sleep 0.3
test ! -s "$d/resources.log"                                     # 1000s < 30 min
printf '{"overall":"short","resources":{"disk:state":{"status":"short","used_pct":85}},"needs_founder":[]}\n' > "$d/state/economy/resources.json"
cycle
i=0; while [ "$i" -lt 50 ] && [ ! -s "$d/resources.log" ]; do sleep 0.1; i=$((i+1)); done
grep -q '^refresh$' "$d/resources.log"                           # 1000s >= 10 min while short
# While short the agent is dispatched every two hours instead of twelve, and the prompt carries the report.
printf '%s\n' "$((now - 8000))" > "$d/state/executive/economy/last-dispatch"
printf '{"overall":"critical","resources":{"disk:state":{"status":"critical","used_pct":93}},"needs_founder":["NEEDS-FOUNDER: disk state is critical"]}\n' > "$d/state/economy/resources.json"
runs_before=$(dispatches)
cycle
test "$(dispatches)" -eq $((runs_before + 1))
# A resource that merely drifts by a fraction of a percent does not wake it again.
printf '%s\n' "$((now - 8000))" > "$d/state/executive/economy/last-dispatch"
printf '{"overall":"critical","resources":{"disk:state":{"status":"critical","used_pct":93.4}},"needs_founder":["NEEDS-FOUNDER: disk state is critical"]}\n' > "$d/state/economy/resources.json"
cycle
test "$(dispatches)" -eq $((runs_before + 1))

# A slow refresh never blocks the cycle.
printf '1\n' > "$d/state/executive/economy/last-refresh"
start=$(date +%s)
MOCK_REFRESH_SLOW=1 cycle
test $(( $(date +%s) - start )) -lt 2

echo 'economy cycle smoke passed'
