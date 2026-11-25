#!/bin/sh
# Bounded board-fetch retry and durable full-stderr telemetry (executive recurrence).
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
mkdir -p "$scratch/bin" "$scratch/state"

cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
calls="$MOCK_STATE/list-calls"
if [ "$1 $2" = "board list" ]; then
    n=0
    [ ! -f "$calls" ] || n=$(cat "$calls")
    n=$((n+1)); printf '%s\n' "$n" > "$calls"
    if [ "$n" -le "${FAIL_CALLS:-0}" ]; then
        # Long, uniquely identifiable stderr (>180 chars) proves durable
        # telemetry stores the complete payload, not the wrapper's 180-char tail.
        awk 'BEGIN{for(i=0;i<12;i++) printf "VERYLONGPREFIX-%03d-01234567890123456789012345678901234567890123456789\n", i}' >&2
        exit 7
    fi
    echo '[{"number":"301","title":"Assigned issue"}]'
    exit 0
fi
if [ "$1 $2" = "board show" ]; then
    echo '{"body":"All agent execution and development work must happen on billy-dev.","messages":[]}'
    exit 0
fi
echo "unexpected antonina invocation: $*" >&2
exit 9
MOCK
chmod +x "$scratch/bin/antonina"

PATH="$scratch/bin:$PATH"
VICHE_STATE_ROOT="$scratch/state"
VICHE_BOARD_RETRIES=3
VICHE_BOARD_RETRY_DELAY=0
MOCK_STATE="$scratch"
export PATH VICHE_STATE_ROOT VICHE_BOARD_RETRIES VICHE_BOARD_RETRY_DELAY MOCK_STATE

# Case 1: two transient fetch failures, then success. No failure telemetry,
# because the failure was absorbed before exhaustion.
: > "$scratch/list-calls"
FAIL_CALLS=2
export FAIL_CALLS
python3 "$repo/government/eligible-work.py" > "$scratch/out.json" 2> "$scratch/err.txt"
test "$(cat "$scratch/list-calls")" -eq 3
jq -e '.complete == true and .count == 1 and .eligible[0].number == "301"' \
    "$scratch/state/branches/eligible-issues.json" >/dev/null
test ! -e "$scratch/state/oversight/eligibility-board-errors.jsonl"

# Case 2: every attempt fails. Bounded exit, no partial issue list, and the
# complete raw stderr is preserved in the append-only telemetry file.
: > "$scratch/list-calls"
FAIL_CALLS=99
rm -f "$scratch/state/branches/eligible-issues.json"
if python3 "$repo/government/eligible-work.py" > "$scratch/out2.json" 2> "$scratch/err2.txt"; then
    echo 'FAIL: exhausted board fetch must exit nonzero' >&2; exit 1
fi
grep -q 'ELIGIBILITY_DISCOVERY_UNAVAILABLE: board command unavailable:' "$scratch/err2.txt"
test "$(cat "$scratch/list-calls")" -eq 3
test ! -e "$scratch/state/branches/eligible-issues.json"

LOG="$scratch/state/oversight/eligibility-board-errors.jsonl"
test -s "$LOG"
test "$(wc -l < "$LOG")" -eq 1
jq -e '.exit == 7 and .attempts == 3 and .stderr_bytes > 180 and
       (.command | join(" ") | contains("board list"))' "$LOG" >/dev/null
FULL=$(jq -r '.stderr_b64' "$LOG" | base64 -d)
printf '%s' "$FULL" | grep -q 'VERYLONGPREFIX-000'
printf '%s' "$FULL" | grep -q 'VERYLONGPREFIX-011'
test "$(printf '%s' "$FULL" | wc -c)" -gt 180

# Case 3: knobs are bounded, so a hostile value cannot create unbounded work.
VICHE_BOARD_RETRIES=99999
export VICHE_BOARD_RETRIES
python3 -c 'import importlib.util,sys; spec=importlib.util.spec_from_file_location("ew","'"$repo"'/government/eligible-work.py"); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); assert m.RETRIES == 10'

echo 'Eligible-work bounded retry and durable full-stderr telemetry smoke passed'
