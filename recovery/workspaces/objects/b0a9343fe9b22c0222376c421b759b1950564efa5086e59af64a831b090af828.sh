#!/bin/sh
# Executive is separate from any parliamentary summons.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
mkdir -p "$scratch/bin" "$scratch/town/government" "$scratch/town/records" "$scratch/seats/branches/executive" "$scratch/state"
printf 'c1a00001\tClerk\tintake\nc1a00002\tMember\tvoting\n' > "$scratch/town/government/seats.tsv"
printf 'Founder charter fixture\n' > "$scratch/charter"
printf '%s\n' c1a00002 > "$scratch/town/records/SUMMONED.txt"
cp "$repo/government/eligible-work.py" "$scratch/town/government/eligible-work.py"
cp "$repo/government/research-frontier-status.py" "$scratch/town/government/research-frontier-status.py"
printf '{"fronts":[{"id":"completed-front","status":"investigated"}],"curator":{"exit_state":"clearexit","added":0,"last_finished_at":1000}}\n' > "$scratch/frontier.json"
cp "$repo/government/handoff-queue.sh" "$scratch/town/government/handoff-queue.sh"
cp "$repo/government/predict-scorer.py" "$scratch/town/government/predict-scorer.py"
cp "$repo/government/AGENT-REPORTING-POLICY.md" "$scratch/town/government/AGENT-REPORTING-POLICY.md"
cp "$repo/government/delivery-candidates.py" "$scratch/town/government/delivery-candidates.py"
cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
case "$1 $2" in
  "board list")
    [ "${BOARD_DOWN:-no}" != yes ] || exit 3
    echo '[{"number":"301","title":"SoringP1"},{"number":"opaque-id-xyz","title":"Second issue"}]' ;;
  "board show")
    echo '{"body":"All agent execution and development work must happen on billy-dev.","messages":[]}' ;;
  "agent status")
    if [ "$MODE" = sequence ]; then
        n=0
        [ ! -f "$MOCK_STATE/status-calls" ] || n=$(cat "$MOCK_STATE/status-calls")
        n=$((n+1)); printf '%s\n' "$n" > "$MOCK_STATE/status-calls"
        if [ "$n" -eq 1 ]; then printf '%s\n' '{"state":"unknown"}'
        else printf '%s\n' '{"state":"running"}'; fi
    else
        printf '{"state":"%s","model":"%s","variant":"low"}\n' "$MODE" "$MODEL"
    fi ;;
  "agent run")
    case "$*" in *"Founder charter fixture"*"301"*) : ;; *) exit 8 ;; esac
    case "$*" in *"SoringP1"*"research-plan.md"*) : ;; *) exit 8 ;; esac
    case "$*" in *"depleted_after_empty_curation"*) : ;; *) exit 8 ;; esac
    printf 'accepted\n' >> "$OUTPUT" ;;
  *) echo "Unexpected: $*" >&2; exit 10 ;;
esac
MOCK
chmod +x "$scratch/bin/antonina"
PATH=$scratch/bin:$PATH
mkdir -p "$scratch/town/government"
cp "$repo/tests/appointment-id-stub.sh" "$scratch/town/government/appointments.sh"
VICHE_TOWN_ROOT=$scratch/town
VICHE_SEATS_ROOT=$scratch/seats
VICHE_STATE_ROOT=$scratch/state
VICHE_CONSTITUTION=$scratch/charter
MODE=idle MODEL=test-provider/example
OUTPUT=$scratch/dispatched
SORING_FRONTIER_STATE=$scratch/frontier.json
export PATH VICHE_TOWN_ROOT VICHE_SEATS_ROOT VICHE_STATE_ROOT VICHE_CONSTITUTION MODE MODEL OUTPUT SORING_FRONTIER_STATE
MOCK_STATE=$scratch
MOCK_STATE=$MOCK_STATE
export MOCK_STATE
grep -Fq "Before interacting with Antonina board or agents" "$repo/government/executive-cycle.sh"
grep -Fq "government/antonina-interface.md" "$repo/government/executive-agenda.md"
sh "$repo/government/executive-cycle.sh"
test ! -e "$OUTPUT"
touch "$scratch/state/inaugurated"
sh "$repo/government/executive-cycle.sh"
test "$(wc -l < "$OUTPUT")" -eq 1
test -s "$scratch/town/records/predictions/calibration.json"
jq -e '.count==2 and .eligible[0].number=="301" and .eligible[1].number=="opaque-id-xyz"' "$scratch/state/branches/eligible-issues.json" >/dev/null
sh "$repo/government/executive-cycle.sh"
test "$(wc -l < "$OUTPUT")" -eq 2
MODE=running
sh "$repo/government/executive-cycle.sh"
test "$(wc -l < "$OUTPUT")" -eq 2
MODE=failed
if sh "$repo/government/executive-cycle.sh" 2>/dev/null; then exit 1; fi
MODE=idle MODEL=other-provider/other-model
sh "$repo/government/executive-cycle.sh"
test "$(wc -l < "$OUTPUT")" -eq 3
MODEL=test-provider/example
BOARD_DOWN=yes
export MODE MODEL BOARD_DOWN
if sh "$repo/government/executive-cycle.sh" 2>/dev/null; then exit 1; fi
test "$(wc -l < "$OUTPUT")" -eq 3
# A transient 'unknown' is re-read, not fatal and not treated as idle.
MODE=sequence
VICHE_AGENT_STATE_RETRIES=3 VICHE_AGENT_STATE_DELAY=0
export MODE VICHE_AGENT_STATE_RETRIES VICHE_AGENT_STATE_DELAY
rm -f "$MOCK_STATE/status-calls"
sh "$repo/government/executive-cycle.sh"
test "$(cat "$MOCK_STATE/status-calls")" -eq 2
test "$(wc -l < "$OUTPUT")" -eq 3

# A persistent 'unknown' fails closed with a specific diagnostic and no dispatch.
MODE=unknown
export MODE
if sh "$repo/government/executive-cycle.sh" 2>"$scratch/unknown.err"; then
    echo 'FAIL: persistent unknown state must not be treated as success' >&2; exit 1
fi
grep -q 'has no usable state' "$scratch/unknown.err"
grep -q "unrecognized agent state 'unknown'" "$scratch/unknown.err"
test "$(wc -l < "$OUTPUT")" -eq 3

echo 'Independent Executive dispatch and fail-closed assignment smoke passed'
