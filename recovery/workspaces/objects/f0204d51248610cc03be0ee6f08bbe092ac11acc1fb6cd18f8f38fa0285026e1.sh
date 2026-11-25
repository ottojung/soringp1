#!/bin/sh
# Act 29 section 6: the Ministry of Economy measures every scarce resource, forecasts
# time to full and acts early through the Janitor pipeline, without a model call.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/state/economy" "$d/town" "$d/seats" "$d/cg"
cat > "$d/janitor.sh" <<'STUB'
#!/bin/sh
printf '%s\n' "$*" >> "$MOCK_JANITOR_LOG"
echo "janitor: $1 complete"
STUB
export VICHE_TOWN_ROOT="$d/town" VICHE_SEATS_ROOT="$d/seats" VICHE_STATE_ROOT="$d/state" \
  VICHE_ECONOMY_JANITOR="$d/janitor.sh" VICHE_ECONOMY_FS_OVERRIDE="$d/fs.json" VICHE_ECONOMY_CGROUP="$d/cg" \
  VICHE_ECONOMY_NO_DU=1 MOCK_JANITOR_LOG="$d/janitor.log" HOME="$d/home" \
  VICHE_ECONOMY_LOAD_OVERRIDE='{"load1":0.10,"load5":0.10,"load15":0.10}'
NOW=1794830400
: > "$d/janitor.log"
res="python3 $repo/government/economy-resources.py"
report=$d/state/economy/resources.json
GIB=1073741824
fs() { # fs TOTAL_GIB AVAIL_GIB -> filesystem override
  printf '{"state":{"total":%s,"avail":%s,"files":1000000,"ffree":900000}}\n' "$(( $1 * GIB ))" "$(( $2 * GIB ))" > "$d/fs.json"
}
run() { VICHE_ECONOMY_NOW=$1 $res refresh ${2:+"$2"}; }
calls() { cat "$d/janitor.log" | tr '\n' ','; }
reset() { : > "$d/janitor.log"; rm -f "$d/state/economy/action-state.json" "$d/state/economy/resource-history.jsonl" "$d/state/economy/actions.log"; }

# Healthy: nothing runs.
fs 1000 500
run $NOW | jq -e '.overall == "ok" and .actions == 0 and .needs_founder == 0' >/dev/null
test ! -s "$d/janitor.log"
jq -e '.resources["disk:state"].status == "ok" and .resources["disk:state"].used_pct == 50' "$report" >/dev/null

# Watch (72% used): refresh the Janitor's inventory and classification only; not repeated inside the interval.
reset; fs 1000 280
run $NOW | jq -e '.overall == "watch" and .actions == 2' >/dev/null
test "$(calls)" = 'inventory,classify,'
run $((NOW + 1800)) | jq -e '.actions == 0' >/dev/null
test "$(calls)" = 'inventory,classify,'
run $((NOW + 21600)) | jq -e '.actions == 2' >/dev/null

# Short (85% used): the whole pipeline, in order, each step logged.
reset; fs 1000 150
run $NOW | jq -e '.overall == "short" and .actions == 7 and .needs_founder == 0' >/dev/null
test "$(calls)" = 'inventory,classify,scratch-quarantine,quarantine,reclaim-idle-caches,reclaim,reclaim-quarantined,'
test "$(wc -l < "$d/state/economy/actions.log")" -eq 7
jq -e 'select(.mode == "quarantine") | .ok == true and .level == "short"' "$d/state/economy/actions.log" >/dev/null
# Still short at the next pass: the Founder hears about it exactly once the pipeline has had its turn.
run $((NOW + 21600)) | jq -e '.needs_founder == 1' >/dev/null
$res needs | grep -q '^NEEDS-FOUNDER: disk state is short (85.0% used, 150.0 GiB free'

# Critical (92% used): NEEDS-FOUNDER at once, and the pipeline reruns after half the interval.
reset; fs 1000 80
run $NOW | jq -e '.overall == "critical" and .needs_founder == 1' >/dev/null
run $((NOW + 10000)) | jq -e '.actions == 0' >/dev/null
run $((NOW + 11000)) | jq -e '.actions == 7' >/dev/null

# Under 5 GiB free is critical whatever the percentage.
reset; fs 100000 4
run $NOW | jq -e '.overall == "critical"' >/dev/null

# Forecast: 60% used now, but 200 GiB gone in the last 24 h, so full in 48 h: short.
reset; fs 1000 400
printf '{"at":%s,"fs":{"state":{"avail":%s}}}\n' "$((NOW - 86400))" "$(( 600 * GIB ))" > "$d/state/economy/resource-history.jsonl"
run $NOW | jq -e '.overall == "short"' >/dev/null
jq -e '.resources["disk:state"].hours_to_full > 47 and .resources["disk:state"].hours_to_full < 49' "$report" >/dev/null
# Space freeing up is not a forecast of anything.
reset; fs 1000 400
printf '{"at":%s,"fs":{"state":{"avail":%s}}}\n' "$((NOW - 86400))" "$(( 300 * GIB ))" > "$d/state/economy/resource-history.jsonl"
run $NOW | jq -e '.overall == "ok"' >/dev/null
jq -e '.resources["disk:state"].hours_to_full == null' "$report" >/dev/null

# Inodes: exhausted inodes make a roomy disk short.
reset; printf '{"state":{"total":%s,"avail":%s,"files":1000,"ffree":50}}\n' "$(( 1000 * GIB ))" "$(( 900 * GIB ))" > "$d/fs.json"
run $NOW | jq -e '.overall == "critical"' >/dev/null

# Memory: Act 13 floors. 8 GiB limit with 7 GiB unreclaimable leaves 1 GiB: critical.
reset; fs 1000 500
printf '%s\n' "$(( 8 * GIB ))" > "$d/cg/memory.max"
printf 'anon %s\nslab 0\nkernel_stack 0\nsock 0\nfile %s\n' "$(( 7 * GIB ))" "$(( 6 * GIB ))" > "$d/cg/memory.stat"
printf 'max 0\noom_kill 0\n' > "$d/cg/memory.events"
run $NOW | jq -e '.overall == "critical"' >/dev/null
jq -e '.resources.memory.status == "critical"' "$report" >/dev/null
$res needs | grep -q 'memory headroom is 1.00 GiB'
printf 'anon %s\nslab 0\nkernel_stack 0\nsock 0\n' "$(( 1 * GIB ))" > "$d/cg/memory.stat"   # page cache does not count
run $((NOW + 100)) >/dev/null
jq -e '.resources.memory.status == "ok"' "$report" >/dev/null
rm -f "$d/cg/memory.max" "$d/cg/memory.stat" "$d/cg/memory.events"

# Funding is part of the same picture.
printf '{"funding_risk":"high","free_available_now":0}\n' > "$d/state/economy/report.json"
reset; fs 1000 500
run $NOW | jq -e '.needs_founder == 1' >/dev/null
jq -e '.resources.model_funding.status == "critical"' "$report" >/dev/null
$res needs | grep -q 'no free model is available'
rm -f "$d/state/economy/report.json"

# --no-act measures only; --dry-run passes the flag to the Janitor and leaves no trace of having acted.
reset; fs 1000 150
run $NOW --no-act | jq -e '.overall == "short" and .actions == 0' >/dev/null
test ! -s "$d/janitor.log"
run $NOW --dry-run | jq -e '.actions == 7' >/dev/null
grep -q 'quarantine --dry-run' "$d/janitor.log"
test ! -e "$d/state/economy/action-state.json"
test ! -e "$d/state/economy/actions.log"

# The Ministry may tune thresholds; a malformed policy is ignored, not trusted.
reset; fs 1000 150
printf '{"disk_used_pct":[90,95,99]}\n' > "$d/state/economy/resource-policy.json"
run $NOW | jq -e '.overall == "ok"' >/dev/null
printf '{"disk_used_pct":[90],"load_per_cpu":"lots"}\n' > "$d/state/economy/resource-policy.json"
run $((NOW + 100)) | jq -e '.overall == "short"' >/dev/null
rm -f "$d/state/economy/resource-policy.json"

# A missing Janitor is reported, never fatal.
reset; fs 1000 150
VICHE_ECONOMY_JANITOR="$d/nope.sh" VICHE_ECONOMY_NOW=$NOW $res refresh | jq -e '.overall == "short"' >/dev/null
jq -e 'select(.mode == "inventory") | .ok == false' "$d/state/economy/actions.log" >/dev/null

# Nothing in the instrument deletes anything itself: only Janitor modes are ever invoked.
if grep -n 'os.remove\|os.unlink(\(path\|file\)\|shutil.rmtree\|rm -rf' "$repo/government/economy-resources.py" | grep -v 'name)' ; then
  echo 'economy-resources.py must not delete directly' >&2; exit 1
fi

# Sizes of Town-owned directories are measured when du is allowed.
reset; fs 1000 500
mkdir -p "$d/state/big" "$d/seats/branches"
dd if=/dev/zero of="$d/state/big/blob" bs=1024 count=300 2>/dev/null
env -u VICHE_ECONOMY_NO_DU VICHE_ECONOMY_NOW=$NOW $res refresh >/dev/null
jq -e '.town_owned_largest[0].path | endswith("/big")' "$report" >/dev/null

# The report never contains policy secrets or credentials, and `measure` records nothing.
before=$(wc -l < "$d/state/economy/resource-history.jsonl")
VICHE_ECONOMY_NOW=$((NOW + 5000)) $res measure | jq -e '.overall' >/dev/null
test "$(wc -l < "$d/state/economy/resource-history.jsonl")" -eq "$before"

echo 'economy resources smoke passed'
