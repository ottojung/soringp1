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

# government/boot.sh now runs independent office tasks (including the Executive)
# off the sitting critical path via nonblocking_office (the parliament-liveness
# change). The executive-ran marker is therefore written asynchronously. Wait a
# bounded time for it before asserting; the exact line-count assertions below
# are unchanged, so a genuinely missing Executive still fails the test.
wait_executive_ran() {
    _want=$1
    _i=0
    while [ "$_i" -lt 30 ]; do
        if [ -f "$scratch/mock/executive-ran" ]; then
            _n=$(wc -l < "$scratch/mock/executive-ran")
            if [ "$_n" -ge "$_want" ]; then return 0; fi
        fi
        _i=$((_i + 1))
        sleep 1
    done
    return 0
}

# Run against a hermetic town copy. The live records/SUMMONED.txt must not change
# what a routine sitting does, so clear the summons in the copy.
git clone --quiet --no-hardlinks "$root" "$town"
# A worktree at a detached PR commit may clone its default main instead of HEAD.
# Test the exact checked-out source commit inside this disposable clone.
git -C "$town" switch -C main "$(git -C "$root" rev-parse HEAD)" >/dev/null
: > "$town/records/SUMMONED.txt"

# Boot smoke verifies the *transport* of a measurement into an independent
# detail artifact. The costly full-history compliance scan has its own hermetic
# tests (tests/suite-compliance-smoke.sh). Do not make every boot test depend
# on production-sized Git history, process load, or the 60-second audit timeout.
cat > "$town/government/suite-compliance-check.sh" <<'COMPLIANCE_FIXTURE'
#!/bin/sh
printf '%s\n' '{"status":"measured","per_change":[{"commit":"fixture","status":"compliant"}],"changes_reaching_main_red":[],"red_chronology_unresolved_changes":[]}'
COMPLIANCE_FIXTURE

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
        # Assert against the marker the cycle actually emits and the real
        # reporting-policy text, not retired wording.
        # Two producers legitimately wrap the charter differently: the boot
        # sitting uses AUTHORITATIVE, the cycle scripts use FOUNDER.
        case "$prompt" in
            *"=== AUTHORITATIVE CONSTITUTION ==="*|*"=== FOUNDER CONSTITUTION ==="*) : ;;
            *) exit 6 ;;
        esac
        # Every newly launched Town agent must receive the Founder reporting rule.
        case "$prompt" in *"Standing Founder operational instructions — reporting and evidence"*) :;; *) exit 95;; esac
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
# Act 24 is enacted, so boot also runs the Executive Innovation Office cycle,
# which legitimately dispatches once in addition to the seats.
# Act 29 is enacted as well, so boot also runs the Ministry of Economy cycle: one more
# dispatch, with its own Executive-office health record.
[ "$(wc -l < "$scratch/mock/ran")" -eq $((seat_count+2)) ]
jq -e '.office == "economy" and .executive_office == true and .voting_seat == false' \
  "$scratch/state/executive/economy/health.json" >/dev/null
python3 - "$scratch/state/branches/judiciary-measurements.json" "$scratch/state/branches" <<'PY'
import hashlib, json, pathlib, sys
report=json.loads(pathlib.Path(sys.argv[1]).read_text())
block=report['suite_compliance']
assert 'per_change' not in block
# A missing detail record is a clean unreadable signal, never a crash.
# (Suite-compliance timeouts and check errors report this shape; the
# KeyError this used to raise hid the real cause behind a traceback.)
if block.get('details_ref') is None:
    assert block.get('status')=='unreadable', block
    assert block.get('reason'), block
    assert isinstance(block.get('wall_seconds'),(int,float)), block
else:
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
wait_executive_ran 1
[ "$(wc -l < "$scratch/mock/executive-ran")" -eq 1 ]
# A summons wakes legislative seats and must NOT suppress the independent Executive.
summoned=$(sed -n '2p' "$town/government/seats.tsv" | cut -f1)
printf '%s\n' "$summoned" > "$town/records/SUMMONED.txt"
/bin/sh "$town/constitution/boot.sh" --once
[ "$(wc -l < "$scratch/mock/created")" -ge $((seat_count+2)) ]
[ "$(wc -l < "$scratch/mock/ran")" -ge $((seat_count+3)) ]
wait_executive_ran 2
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
