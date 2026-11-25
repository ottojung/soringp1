#!/bin/sh
# Mock the Antonina CLI to test S6 bootstrap using only POSIX /bin/sh.
set -eu
root=$(git rev-parse --show-toplevel)
scratch=$(mktemp -d)
town=$scratch/town
cleanup() {
    if [ -d "$scratch/seats" ]; then
        for dir in "$scratch"/seats/*; do
            if [ -f "$dir/.git" ] || [ -d "$dir/.git" ]; then
                git -C "$town" worktree remove --force "$dir" >/dev/null 2>&1 || :
            fi
        done
    fi
    rm -rf "$scratch"
}
trap 'cleanup' 0
mkdir -p "$scratch/bin" "$scratch/seats" "$scratch/state" "$scratch/mock"

# Run against a hermetic town copy. The live records/SUMMONED.txt must not change
# what a routine sitting does, so clear the summons in the copy.
git clone --quiet --no-hardlinks "$root" "$town"
# A worktree at a detached PR commit may clone its default main instead of HEAD.
# Test the exact checked-out source commit inside this disposable clone.
git -C "$town" switch -C main "$(git -C "$root" rev-parse HEAD)" >/dev/null
: > "$town/records/SUMMONED.txt"

cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
if [ "$1" = board ] && [ "$2" = list ]; then echo "[]"; exit 0; fi
[ "$1" = agent ] || exit 91
action=$2
shift 2
id= prompt=
while [ "$#" -gt 0 ]; do
    case "$1" in
        --id) id=$2; shift 2 ;;
        --cwd|--title) shift 2 ;;
        --prompt) prompt=$2; shift 2 ;;
        --json|--detach) shift ;;
        *) echo "Unexpected Antonina argument $1" >&2; exit 92 ;;
    esac
done
[ "$action" = new ] || [ -n "$id" ] || exit 93
case "$action" in
    status)
        [ -f "$MOCK_STATE/$id" ] || exit 3
        printf '%s\n' '{"state":"idle","model":null,"variant":"low"}'
        ;;
    new)
        n=0
        [ ! -f "$MOCK_STATE/created" ] || n=$(wc -l < "$MOCK_STATE/created")
        id="generated-$((n+1))"
        [ ! -f "$MOCK_STATE/$id" ] || exit 4
        touch "$MOCK_STATE/$id"
        printf '%s\n' "$id" >> "$MOCK_STATE/created"
        printf '%s\n' "$id"
        ;;
    run)
        [ -f "$MOCK_STATE/$id" ] || exit 5
        case "$prompt" in
            *"=== AUTHORITATIVE CONSTITUTION ==="*|*"=== FOUNDER-CONTROLLED CONSTITUTION ==="*) : ;;
            *) exit 6 ;;
        esac
        # Every newly launched Town agent must receive the Founder reporting rule.
        case "$prompt" in *"Report promptly to the Judiciary mailbox ONLY"*) :;; *) exit 95;; esac
        printf '%s\n' "$id" >> "$MOCK_STATE/ran"
        case "$prompt" in *"This is independent executive delivery"*) printf '%s\n' "$id" >> "$MOCK_STATE/executive-ran";; esac
        ;;
    *) exit 94 ;;
esac
MOCK
chmod +x "$scratch/bin/antonina"

MOCK_STATE=$scratch/mock
PATH=$scratch/bin:$PATH
mkdir -p "$scratch/cgroup"
printf "max\n" > "$scratch/cgroup/memory.max"
RESOURCE_SAFETY_CGROUP_DIR=$scratch/cgroup
VICHE_AUDIT_CHECKS=0
VICHE_AUDIT_SELECTION=0
VICHE_BOARD_TRAIL_CHECKS=0
# Act 18 §7 index refresh is separately tested and needs the live board; suppress
# its board scan in bootstrap smoke so the cycle stays hermetic and fast.
VICHE_BOARD_TRAIL_REFRESH=0
export RESOURCE_SAFETY_CGROUP_DIR VICHE_AUDIT_CHECKS VICHE_AUDIT_SELECTION VICHE_BOARD_TRAIL_CHECKS VICHE_BOARD_TRAIL_REFRESH
VICHE_TOWN_ROOT=$town
VICHE_SEATS_ROOT=$scratch/seats
VICHE_STATE_ROOT=$scratch/state
VICHE_SENTINEL_STATE=$scratch/sentinel
VICHE_TEST_NO_SYNC=1
VICHE_TOWNHALL_ID=999
export MOCK_STATE PATH VICHE_TOWN_ROOT VICHE_SEATS_ROOT
export VICHE_STATE_ROOT VICHE_SENTINEL_STATE VICHE_TEST_NO_SYNC VICHE_TOWNHALL_ID

# Periodic broad audit is separately tested. Suppress its timer in bootstrap smoke.
mkdir -p "$scratch/state/oversight"
date +%s > "$scratch/state/oversight/last-audit-dispatch"
# The box-wide janitor inventory (find+du over /workspace, /home/lubko, ...) is
# likewise separately tested and is not part of boot reconciliation; suppress
# its timers so the smoke is hermetic w.r.t. the host's disk layout.
mkdir -p "$scratch/state/janitor"
date +%s > "$scratch/state/janitor/last-observe"
date +%s > "$scratch/state/janitor/last-inventory"
# Monitoring snapshots exist in a correctly initialized town. A missing
# snapshot is now an incident rather than evidence of a healthy bootstrap.
now=$(date +%s)
mkdir -p "$scratch/state/institutional-outcomes" "$scratch/state/institutional-cases" "$scratch/state/branches"
printf '{"observed_at":%s}\n' "$now" > "$scratch/state/institutional-outcomes/latest.json"
printf '{"observed_at":%s,"count":0}\n' "$now" > "$scratch/state/institutional-cases/index.json"
printf '{"observed_at":%s}\n' "$now" > "$scratch/state/branches/judiciary-measurements.json"
seat_count=$(wc -l < "$town/government/seats.tsv")
[ "$seat_count" -ge 1 ]
/bin/sh "$town/constitution/boot.sh" --once
[ "$(wc -l < "$scratch/mock/created")" -ge $((seat_count+2)) ]
[ "$(wc -l < "$scratch/mock/ran")" -eq "$seat_count" ]
python3 - "$scratch/state/branches/judiciary-measurements.json" "$scratch/state/branches" <<'PY'
import hashlib, json, pathlib, sys
report=json.loads(pathlib.Path(sys.argv[1]).read_text())
block=report['suite_compliance']
assert 'per_change' not in block
detail=pathlib.Path(block['details_ref'])
assert detail.is_file() and str(detail).startswith(sys.argv[2])
blob=detail.read_bytes()
assert hashlib.sha256(blob).hexdigest()==block['details_sha256']
detail_data=json.loads(blob)
assert len(detail_data['per_change'])==block['per_change_count']
assert len(detail_data['changes_reaching_main_red'])==block['red_change_count']
PY
/bin/sh "$town/constitution/boot.sh" --once
[ "$(wc -l < "$scratch/mock/created")" -ge $((seat_count+2)) ]
centre=$(awk -F '\t' '$1=="innovation-centre" {print $2}' "$scratch/state/appointments/appointments.tsv")
[ -n "$centre" ] && [ -f "$scratch/mock/$centre" ]
[ "$(wc -l < "$scratch/mock/ran")" -ge $((seat_count+2)) ]
[ "$(wc -l < "$scratch/mock/executive-ran")" -eq 1 ]
# A summons wakes legislative seats and must NOT suppress the independent Executive.
summoned=$(sed -n '2p' "$town/government/seats.tsv" | cut -f1)
printf '%s\n' "$summoned" > "$town/records/SUMMONED.txt"
/bin/sh "$town/constitution/boot.sh" --once
[ "$(wc -l < "$scratch/mock/created")" -ge $((seat_count+2)) ]
[ "$(wc -l < "$scratch/mock/ran")" -ge $((seat_count+3)) ]
[ "$(wc -l < "$scratch/mock/executive-ran")" -eq 2 ]
# A stray ballot checkout must not strand the government. Preserve its commit
# and recover even if fetching origin also fails transiently.
git -C "$town" switch -q -c ballot/bootstrap-smoke-drift
printf 'saved vote\n' > "$town/ballot-drift-sentinel"
git -C "$town" add ballot-drift-sentinel
git -C "$town" -c user.name='Bootstrap Smoke' -c user.email='bootstrap@example.invalid' commit -qm 'Test: preserved ballot on stray branch'
ballot_head=$(git -C "$town" rev-parse HEAD)
origin_url=$(git -C "$town" remote get-url origin)
git -C "$town" remote set-url origin "$scratch/unavailable-origin"
VICHE_TEST_NO_SYNC=0 /bin/sh "$town/constitution/boot.sh" --once
[ "$(git -C "$town" branch --show-current)" = main ]
[ "$(git -C "$town" rev-parse refs/heads/ballot/bootstrap-smoke-drift)" = "$ballot_head" ]
[ ! -e "$town/ballot-drift-sentinel" ]
git -C "$town" remote set-url origin "$origin_url"
printf 'Viche: bootstrap recovered main from ballot drift without discarding the vote, despite origin outage\n'
printf 'Viche: %s seats initialized, charter injected, routine cycle runs Clerk+executive, while a parliamentary summons has precedence\n' "$seat_count"
