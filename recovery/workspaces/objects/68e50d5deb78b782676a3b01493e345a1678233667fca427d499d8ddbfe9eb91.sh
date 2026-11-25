#!/bin/sh
# End-to-end Act 19 recovery through actual appointment and supervisor scripts.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/bin" "$d/town/government" "$d/seats/branches/executive" "$d/seats/c1a00001" "$d/state" "$d/mock"
printf 'c1a00001\tClerk\tintake\n' > "$d/town/government/seats.tsv"
cp "$repo/government/appointments.sh" "$repo/government/branch-bootstrap.sh" \
  "$repo/government/clerk-liveness.sh" "$repo/government/branch-liveness.sh" \
  "$repo/government/executive-cycle.sh" "$repo/government/office-continuity.sh" \
  "$repo/government/terminal-appointment-evidence.sh" "$repo/government/policy-sync.sh" \
  "$repo/government/seat-liveness.sh" "$repo/government/predict-scorer.py" \
  "$repo/government/delivery-candidates.py" "$repo/government/eligible-work.py" \
  "$repo/government/AGENT-REPORTING-POLICY.md" \
  "$d/town/government/"
git -C "$d/seats/branches/executive" init -q
git -C "$d/seats/branches/executive" -c user.name=test -c user.email=test@example.test commit --allow-empty -qm baseline
git -C "$d/seats/c1a00001" init -q
git -C "$d/seats/c1a00001" -c user.name=test -c user.email=test@example.test commit --allow-empty -qm clerk
cat > "$d/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
case "$1 $2" in
  'agent status')
    id=$4
    [ -s "$MOCK_ROOT/$id.json" ] || exit 3
    cat "$MOCK_ROOT/$id.json" ;;
  'agent new')
    n=0; [ ! -s "$MOCK_ROOT/next" ] || n=$(cat "$MOCK_ROOT/next")
    n=$((n+1)); printf '%s\n' "$n" > "$MOCK_ROOT/next"
    id="id-$n"
    printf '{"state":"idle","model":null,"variant":null}\n' > "$MOCK_ROOT/$id.json"
    printf '%s\n' "$id" ;;
  'agent log')
    # Oscillating agent may have restarted running after its terminal event
    # but before the threshold reset; quiesce it before replacing.
    id=$4
    if [ "${MOCK_REVIVE_ON_LOG:-}" = "$id" ] && [ -s "$MOCK_ROOT/$id.json" ] &&
       [ "$(jq -r .state "$MOCK_ROOT/$id.json")" = failed ]; then
      jq '.state="running"' "$MOCK_ROOT/$id.json" > "$MOCK_ROOT/$id.next"
      mv "$MOCK_ROOT/$id.next" "$MOCK_ROOT/$id.json"
    fi
    printf 'captured log\n' ;;
  'agent stop')
    id=$4
    printf '%s\n' "$id" >> "$MOCK_ROOT/stops"
    if [ "${MOCK_STOP_FAIL:-}" = yes ]; then exit 3; fi
    jq '.state="stopped"' "$MOCK_ROOT/$id.json" > "$MOCK_ROOT/$id.next"
    mv "$MOCK_ROOT/$id.next" "$MOCK_ROOT/$id.json" ;;
  'agent run') printf 'run\n' >> "$MOCK_ROOT/runs"; printf '%s\n' "$*" >> "$MOCK_ROOT/run-args" ;;
  # An empty board: the ordinary eligible-issue inventory now always runs
  # beside open handoffs (Founder directive 2026-11-16).
  'board list') printf '[]\n' ;;
  'board show') printf '{"body":"","messages":[]}\n' ;;
  *) echo "unexpected Antonina call: $*" >&2; exit 9 ;;
esac
MOCK
chmod +x "$d/bin/antonina"
export PATH="$d/bin:$PATH" MOCK_ROOT="$d/mock" VICHE_TOWN_ROOT="$d/town" \
  VICHE_SEATS_ROOT="$d/seats" VICHE_STATE_ROOT="$d/state" VICHE_BRANCH_NOW=2000000000
set_status() {
  printf '{"state":"%s","model":null,"variant":"arbitrary-antonina-variant","finished_at":"%s","invocation_id":"%s","backend_error":{"classification":"%s","transient":%s,"automatic_retry_safe":%s}}\n' \
    "$1" "$2" "$3" "$4" "$5" "$6" > "$MOCK_ROOT/$7.json"
}
office=executive
ledger=$VICHE_STATE_ROOT/liveness/failures/events.tsv
registry=$VICHE_STATE_ROOT/appointments/appointments.tsv
base=$(date +%s)
run_branch() { /bin/sh "$VICHE_TOWN_ROOT/government/branch-bootstrap.sh" "$office"; }

# Real Antonina finished_at is a decimal UNIX second, not always an integer.
# This must be accepted and counted with an exact distinct invocation identity.
. "$repo/government/office-continuity.sh"
mkdir -p "$d/fractional"
oc_record_failure "$d/fractional" executive fixture-frac-id run-frac \
  upstream_endpoint_unavailable "$base.125" yes "$base" "$d/seats/branches/executive" ||
  { echo 'Act19 lost a legitimate fractional finished_at failure' >&2; exit 1; }
test -s "$d/fractional/failures/events.tsv"

# Failures are actually discovered by branch-bootstrap before the next ensure.
# Re-polling one failed invocation is idempotent; three identities across the
# original and replacement IDs trigger precisely one threshold reset.
mkdir -p "$VICHE_STATE_ROOT/appointments"
mkdir -p "$VICHE_SEATS_ROOT/branches/executive"
printf 'executive\texecutive-agent\n' > "$VICHE_STATE_ROOT/appointments/appointments.tsv"
id=executive-agent
set_status idle 99 initial idle false true "$id"
run_branch
# An unreadable status query may be a transient transport failure. It is NOT
# evidence that the incumbent stopped; never spawn a duplicate live appointee.
mv "$MOCK_ROOT/$id.json" "$MOCK_ROOT/$id.saved"
if /bin/sh "$VICHE_TOWN_ROOT/government/appointments.sh" ensure executive >/dev/null 2>&1; then
  echo 'Unsafe duplicate appointment on unreadable old status' >&2; exit 1
fi
test "$(awk -F '\t' '$1=="executive" {print $2}' "$registry")" = "$id"
mv "$MOCK_ROOT/$id.saved" "$MOCK_ROOT/$id.json"
set_status failed "$base" run-1 upstream_endpoint_unavailable true true "$id"
run_branch
test "$(wc -l < "$ledger")" -eq 1
id2=$(/bin/sh "$VICHE_TOWN_ROOT/government/appointments.sh" resolve "$office")
test "$id2" = "$id"
set_status failed "$((base+1))" run-2 upstream_endpoint_unavailable true true "$id2"
run_branch
id3=$(/bin/sh "$VICHE_TOWN_ROOT/government/appointments.sh" resolve "$office")
test "$id3" = "$id2"
set_status failed "$((base+2))" run-3 upstream_endpoint_unavailable true true "$id3"
MOCK_REVIVE_ON_LOG=$id3 run_branch
test "$(grep -c -Fx "$id3" "$MOCK_ROOT/stops")" -eq 1 ||
  { echo 'Running appointee was not stopped exactly once before reset' >&2; exit 1; }
id4=$(/bin/sh "$VICHE_TOWN_ROOT/government/appointments.sh" resolve "$office")
test "$id4" != "$id3"
# A concurrent supervisor still holding the old agent identity must NOT
# replace the new appointment after another observer won the reset.
if /bin/sh "$VICHE_TOWN_ROOT/government/appointments.sh" replace executive "$id3" concurrency-test stale_supervisor 'stale contender' >/dev/null 2>&1; then
  echo 'Stale supervisor overwrote newly recovered appointment' >&2; exit 1
fi
test "$(/bin/sh "$VICHE_TOWN_ROOT/government/appointments.sh" resolve executive)" = "$id4"
# The third distinct failure causes ONE replacement, not two. An earlier
# implementation called appointments.sh replace twice inside one supervisor.
test "$(cat "$MOCK_ROOT/next")" -eq 1 || { echo 'Multiple replacements for one Act19 threshold event' >&2; exit 1; }
test "$(wc -l < "$VICHE_STATE_ROOT/liveness/recoveries.log")" -eq 1
test "$(wc -l < "$ledger")" -eq 3
jq -e --arg prior "$id3" '.caller=="branch-bootstrap" and .trigger=="act19_failure_threshold" and .expected_prior_id==$prior and .reason!=""' \
  "$VICHE_STATE_ROOT/appointments/replacement-provenance.jsonl" >/dev/null
# A failed stop may not begin reset cooldown or replace a live appointee.
oc_quiesce_for_reset_test_id=$id4
set_status running "$((base+5))" run-running idle false true "$oc_quiesce_for_reset_test_id"
. "$repo/government/office-continuity.sh"
if MOCK_STOP_FAIL=yes oc_quiesce_for_reset "$oc_quiesce_for_reset_test_id"; then
  echo 'Failed quiescence incorrectly reported success' >&2; exit 1
fi
test "$(/bin/sh "$VICHE_TOWN_ROOT/government/appointments.sh" resolve executive)" = "$id4"
test "$(jq -r .state "$MOCK_ROOT/$id4.json")" = running
# Stop directly to restore a benign terminal state for subsequent fixtures.
oc_quiesce_for_reset "$oc_quiesce_for_reset_test_id"
test "$(jq -r .state "$MOCK_ROOT/$id4.json")" = stopped
test "$(awk -F '\t' '$1=="executive" {n++} END {print n+0}' "$registry")" -eq 1

# latest durable handoff and dirty worktree survive replacement; no duplicate
# IDs are registered or multiple replacements occur for a single event.
printf 'uncommitted handoff\n' > "$VICHE_SEATS_ROOT/branches/executive/handoff.txt"
git -C "$VICHE_SEATS_ROOT/branches/executive" status --short > "$d/dirty.status"
grep -Fq 'handoff.txt' "$d/dirty.status"
test "$(awk -F '\t' '$1=="executive" {n++} END {print n+0}' "$registry")" -eq 1

# Permanent authorization failure is surfaced and not entered in transient
# history; unsafe automatic retry gets a fresh appointment without replay.
set_status failed 103 run-auth invalid_api_key false false "$id4"
before=$(wc -l < "$registry")
run_branch
test "$(wc -l < "$registry")" -eq "$before"
grep -Fq 'permanent_failure classification=invalid_api_key' "$VICHE_STATE_ROOT/liveness/permanent-incidents.log"

set_status failed 104 run-unsafe upstream_endpoint_unavailable true false "$id4"
run_branch
id5=$(/bin/sh "$VICHE_TOWN_ROOT/government/appointments.sh" resolve "$office")
test "$id5" = "$id4"
test "$(wc -l < "$registry")" -eq 1
test -s "$VICHE_STATE_ROOT/liveness/unsafe-holds/executive"
printf 'founder charter fixture\n' > "$d/charter"
touch "$VICHE_STATE_ROOT/inaugurated"
export VICHE_CONSTITUTION="$d/charter"
if /bin/sh "$VICHE_TOWN_ROOT/government/executive-cycle.sh"; then
  echo 'unsafe terminal event must hold redispatch' >&2; exit 1
fi
test ! -s "$MOCK_ROOT/runs"

# A safe-to-retry failure remains held below threshold, but after the lawful
# reset a clean session resumes from the actual durable open handoff.
mkdir -p "$d/safe/town/government" "$d/safe/town/records" \
  "$d/safe/seats/branches/executive" "$d/safe/state/appointments"
cp "$repo/government/appointments.sh" "$repo/government/executive-cycle.sh" \
  "$repo/government/handoff-queue.sh" "$repo/government/terminal-appointment-evidence.sh" \
  "$repo/government/predict-scorer.py" \
  "$repo/government/delivery-candidates.py" "$repo/government/eligible-work.py" \
  "$repo/government/AGENT-REPORTING-POLICY.md" \
  "$d/safe/town/government/"
printf 'c1a00001\tClerk\tintake\n' > "$d/safe/town/government/seats.tsv"
printf 'executive\tsafe-id\n' > "$d/safe/state/appointments/appointments.tsv"
printf '{"state":"idle","model":null,"variant":null}\n' > "$MOCK_ROOT/safe-id.json"
printf 'charter\n' > "$d/safe/charter"
safe_id=$(/bin/sh "$d/safe/town/government/handoff-queue.sh" add "$d/safe/town" test evidence 'resume this latest safe handoff')
mkdir -p "$d/safe/state"
touch "$d/safe/state/inaugurated"
export VICHE_TOWN_ROOT="$d/safe/town" VICHE_SEATS_ROOT="$d/safe/seats" \
  VICHE_STATE_ROOT="$d/safe/state" VICHE_CONSTITUTION="$d/safe/charter"
: > "$MOCK_ROOT/runs"
/bin/sh "$VICHE_TOWN_ROOT/government/executive-cycle.sh"
test "$(wc -l < "$MOCK_ROOT/runs")" -eq 1
grep -Fq 'resume this latest safe handoff' "$MOCK_ROOT/run-args"
grep -Fq "$safe_id" "$MOCK_ROOT/run-args"

# A *distinct, retry-safe* terminal invocation must admit a NEW explicit
# managed prompt (never automatic replay of a retry-unsafe side effect).
# Without this, no second or third real failure can occur and Act19's
# three-event threshold is unreachable despite the synthetic counter tests.
set_status failed 105 safe-run-2 upstream_endpoint_unavailable true true safe-id
: > "$MOCK_ROOT/runs"
/bin/sh "$VICHE_TOWN_ROOT/government/executive-cycle.sh"
test "$(wc -l < "$MOCK_ROOT/runs")" -eq 1 ||
  { echo 'retry-safe terminal agent cannot execute a distinct new prompt' >&2; exit 1; }

# The actual Clerk gate/liveness path exercises the same real appointment record.
export VICHE_TOWN_ROOT="$d/town" VICHE_SEATS_ROOT="$d/seats" VICHE_STATE_ROOT="$d/state"
clerk=$(/bin/sh "$VICHE_TOWN_ROOT/government/appointments.sh" ensure c1a00001)
set_status failed 105 clerk-run upstream_endpoint_unavailable true true "$clerk"
# A proven retry-safe transient Clerk may receive a NEW instruction.
# This ensures real repeated failures are possible before the threshold.
 /bin/sh "$VICHE_TOWN_ROOT/government/clerk-liveness.sh" --gate
/bin/sh "$VICHE_TOWN_ROOT/government/clerk-liveness.sh"
clerk2=$(/bin/sh "$VICHE_TOWN_ROOT/government/appointments.sh" resolve c1a00001)
test "$clerk2" = "$clerk"
test -s "$VICHE_STATE_ROOT/liveness/failures/events.tsv"
# Retry-unsafe Clerk must not re-dispatch, even before threshold/reset.
set_status failed 106 clerk-unsafe upstream_endpoint_unavailable true false "$clerk"
if /bin/sh "$VICHE_TOWN_ROOT/government/clerk-liveness.sh" --gate; then
  echo 'retry-unsafe Clerk passed sitting gate' >&2; exit 1
fi

# A non-Clerk parliamentary seat has the SAME per-office three-distinct
# event rule, with one reset, not three observations of one failed prompt.
printf 'c1a00007\tContinuity member\tLegality\n' >> "$d/town/government/seats.tsv"
mkdir -p "$d/seats/c1a00007"
git -C "$d/seats/c1a00007" init -q
git -C "$d/seats/c1a00007" -c user.name=test -c user.email=test@example.test commit --allow-empty -qm baseline
seat=$(/bin/sh "$d/town/government/appointments.sh" ensure c1a00007)
for n in 1 2 3; do
  set_status failed "$((base+n))" "seat-invocation-$n" upstream_endpoint_unavailable true true "$seat"
  /bin/sh "$d/town/government/seat-liveness.sh" c1a00007
done
seat_after=$(/bin/sh "$d/town/government/appointments.sh" resolve c1a00007)
[ "$seat_after" != "$seat" ] || { echo 'Parliamentary seat did not reset on three distinct failures' >&2; exit 1; }
[ "$(awk -F '\t' '$1=="c1a00007"{n++} END{print n+0}' "$d/state/appointments/appointments.tsv")" -eq 1 ]
test "$(grep -c 'seat=c1a00007 session_reset=' "$d/state/liveness/recoveries.log")" -eq 1
jq -e --arg prior "$seat" '.caller=="seat-liveness" and .trigger=="act19_failure_threshold" and .expected_prior_id==$prior and .reason!=""' \
  "$d/state/appointments/replacement-provenance.jsonl" >/dev/null
echo 'appointment recovery integration tests passed'
