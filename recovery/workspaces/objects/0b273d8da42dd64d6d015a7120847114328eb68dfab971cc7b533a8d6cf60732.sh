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
  "$d/town/government/"
cp "$repo/government/AGENT-REPORTING-POLICY.md" "$d/town/government/"
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
# Recovery is bookkeeping only; it must not dispatch/replay the old prompt.
test ! -s "$MOCK_ROOT/runs"

# A safe-to-retry failure remains held below threshold, but after the lawful
# reset a clean session resumes from the actual durable open handoff.
mkdir -p "$d/safe/town/government" "$d/safe/town/records" \
  "$d/safe/seats/branches/executive" "$d/safe/state/appointments"
cp "$repo/government/appointments.sh" "$repo/government/executive-cycle.sh" \
  "$repo/government/handoff-queue.sh" "$repo/government/terminal-appointment-evidence.sh" \
  "$repo/government/predict-scorer.py" "$d/safe/town/government/"
cp "$repo/government/AGENT-REPORTING-POLICY.md" "$d/safe/town/government/"
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

# Threshold reset archives unsafe hold. If the move fails, reset must fail and
# the hold must remain available for a later retry.
mkdir -p "$d/hold/town/government" "$d/hold/seats/branches/executive" "$d/hold/state/appointments" "$d/hold/state/liveness/unsafe-holds" "$d/hold/state/liveness/archived-unsafe-holds"
printf 'c1a00001\tClerk\tintake\n' > "$d/hold/town/government/seats.tsv"
cp "$repo/government/appointments.sh" "$repo/government/branch-bootstrap.sh" \
  "$repo/government/branch-liveness.sh" "$repo/government/office-continuity.sh" \
  "$repo/government/terminal-appointment-evidence.sh" "$repo/government/policy-sync.sh" \
  "$d/hold/town/government/"
cp "$repo/government/AGENT-REPORTING-POLICY.md" "$d/hold/town/government/"
git -C "$d/hold/seats/branches/executive" init -q
git -C "$d/hold/seats/branches/executive" -c user.name=test -c user.email=test@example.test commit --allow-empty -qm baseline
printf 'executive\tsafe-id\n' > "$d/hold/state/appointments/appointments.tsv"
run_hold() {
  VICHE_STATE_ROOT="$d/hold/state" VICHE_TOWN_ROOT="$d/hold/town" \
    VICHE_SEATS_ROOT="$d/hold/seats" /bin/sh \
    "$d/hold/town/government/branch-bootstrap.sh" executive
}
set_status failed "$((base+10))" hold-inv-1 upstream_endpoint_unavailable true false safe-id
run_hold
test -s "$d/hold/state/liveness/unsafe-holds/executive"
set_status failed "$((base+11))" hold-inv-2 upstream_endpoint_unavailable true false safe-id
run_hold
set_status failed "$((base+12))" hold-inv-3 upstream_endpoint_unavailable true false safe-id
printf 'executive\tunrelated-id\tunrelated-invocation\n' >> "$d/hold/state/liveness/unsafe-holds/executive"
# An apparently valid but partial archive for the same appointee must not
# authorize removal of all active hold rows for that appointee.
printf 'executive\tsafe-id\thold-inv-1\n' > "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset"
if run_hold >/dev/null 2>&1; then echo 'Archive failure reported successful Act19 recovery' >&2; exit 1; fi
test -s "$d/hold/state/liveness/unsafe-holds/executive" ||
  { echo 'Archive failure lost retryable unsafe hold' >&2; exit 1; }
pending_successor=$(VICHE_STATE_ROOT="$d/hold/state" /bin/sh "$d/hold/town/government/appointments.sh" resolve executive)
test "$pending_successor" != safe-id
test "$(jq -r .state "$MOCK_ROOT/safe-id.json")" = failed
test -s "$d/hold/state/liveness/reset-pending-executive"
test -s "$d/hold/state/liveness/last-reset-executive"
test -s "$d/hold/state/liveness/failures/events.tsv"
# A failed retry must preserve the marker and refuse to mutate the appointment.
if VICHE_STATE_ROOT="$d/hold/state" VICHE_TOWN_ROOT="$d/hold/town" \
  VICHE_SEATS_ROOT="$d/hold/seats" VICHE_BRANCH_NOW="$((base+20))" \
  /bin/sh "$d/hold/town/government/branch-bootstrap.sh" executive >/dev/null 2>&1; then
  echo 'Occupied archive destination was not retried safely' >&2; exit 1
fi
test -s "$d/hold/state/liveness/reset-pending-executive"
test "$(VICHE_STATE_ROOT="$d/hold/state" /bin/sh "$d/hold/town/government/appointments.sh" resolve executive)" = "$pending_successor"
# Expanded legacy archive matching current active rows remains ambiguous and
# must not authorize deletion, even though its bytes now appear complete.
printf 'executive\tsafe-id\thold-inv-1\n' > "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset"
printf 'executive\tsafe-id\thold-inv-1\nexecutive\tsafe-id\thold-inv-2\nexecutive\tsafe-id\thold-inv-3\n' >> "$d/hold/state/liveness/unsafe-holds/executive"
printf 'executive\tsafe-id\thold-inv-1\nexecutive\tsafe-id\thold-inv-2\nexecutive\tsafe-id\thold-inv-3\n' > "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset"
rm -f "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset.act19-proof"
if VICHE_STATE_ROOT="$d/hold/state" VICHE_TOWN_ROOT="$d/hold/town" VICHE_SEATS_ROOT="$d/hold/seats" /bin/sh "$d/hold/town/government/branch-bootstrap.sh" executive >/dev/null 2>&1; then
  echo 'Expanded unproven archive authorized active hold deletion' >&2; exit 1
fi
test -s "$d/hold/state/liveness/reset-pending-executive"
test "$(wc -l < "$d/hold/state/liveness/unsafe-holds/executive")" -eq 7
rm -f "$d/hold/state/liveness/unsafe-holds/executive" "$d/hold/state/liveness/reset-pending-executive" \
  "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset" \
  "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset.act19-manifest"
printf 'executive\tsafe-id\thold-inv-1\nexecutive\tunrelated-id\tunrelated-invocation\n' \
  > "$d/hold/state/liveness/unsafe-holds/executive"
printf 'executive\tsafe-id\thold-inv-1\n' \
  > "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset"
printf '%s\n' safe-id > "$d/hold/state/liveness/reset-pending-executive"
# Reconstruct the interrupted registry-commit boundary directly: a prepared
# intent must not authorize cleanup under an unrelated current successor.
mkdir -p "$d/hold/state/appointments/replacement-intents"
jq -cn --arg successor "$pending_successor" --arg tx recovery-tx \
  '{state:"prepared",office:"executive",expected_prior_id:"safe-id",
    proposed_successor:$successor,transaction:$tx,caller:"branch-bootstrap",trigger:"act19_failure_threshold"}' \
  > "$d/hold/state/appointments/replacement-intents/interrupted.json"
printf 'executive\tmanual-successor\n' > "$d/hold/state/appointments/appointments.tsv"
if VICHE_STATE_ROOT="$d/hold/state" VICHE_TOWN_ROOT="$d/hold/town" \
  VICHE_SEATS_ROOT="$d/hold/seats" VICHE_BRANCH_NOW="$((base+20))" \
  /bin/sh "$d/hold/town/government/branch-bootstrap.sh" executive >/dev/null 2>&1; then
  echo 'Prepared replacement intent authorized reset recovery' >&2; exit 1
fi
test -s "$d/hold/state/liveness/reset-pending-executive"
test -s "$d/hold/state/liveness/unsafe-holds/executive"
# The earlier deliberate partial archive remains untouched on rejected recovery.
grep -Fqx 'executive	safe-id	hold-inv-1' \
  "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset"
# Remove the obstruction, then restore the registry to the intent's successor.
rm "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset"
printf 'executive\t%s\twrong-tx\n' "$pending_successor" > "$d/hold/state/appointments/appointments.tsv"
if VICHE_STATE_ROOT="$d/hold/state" VICHE_TOWN_ROOT="$d/hold/town" \
  VICHE_SEATS_ROOT="$d/hold/seats" VICHE_BRANCH_NOW="$((base+20))" \
  /bin/sh "$d/hold/town/government/branch-bootstrap.sh" executive >/dev/null 2>&1; then
  echo 'Mismatched registry transaction authorized reset recovery' >&2; exit 1
fi
test -s "$d/hold/state/liveness/reset-pending-executive"
printf 'executive\t%s\trecovery-tx\n' "$pending_successor" > "$d/hold/state/appointments/appointments.tsv"
# Simulate failure before registry swap: old row plus prepared intent is not
# commit evidence. Recovery must leave all reset evidence untouched.
printf 'executive\t%s\n' "$pending_successor" > "$d/hold/state/appointments/appointments.tsv"
printf 'executive\t%s\tpre-swap-invocation\n' "$pending_successor" \
  >> "$d/hold/state/liveness/unsafe-holds/executive"
printf '%s\n' "$pending_successor" > "$d/hold/state/liveness/reset-pending-executive"
jq -cn --arg prior "$pending_successor" --arg tx pre-swap-tx \
  '{state:"prepared",office:"executive",expected_prior_id:$prior,
    proposed_successor:"not-yet-swapped",transaction:$tx,caller:"branch-bootstrap",trigger:"act19_failure_threshold"}' \
  > "$d/hold/state/appointments/replacement-intents/pre-swap.json"
pre_swap_holds=$(cat "$d/hold/state/liveness/unsafe-holds/executive")
pre_swap_archive=$d/hold/state/liveness/archived-unsafe-holds/executive-$pending_successor-act19-reset
if VICHE_STATE_ROOT="$d/hold/state" VICHE_TOWN_ROOT="$d/hold/town" \
  VICHE_SEATS_ROOT="$d/hold/seats" VICHE_BRANCH_NOW="$((base+20))" \
  /bin/sh "$d/hold/town/government/branch-bootstrap.sh" executive >/dev/null 2>&1; then
  echo 'pre-swap prepared intent incorrectly authorized recovery' >&2; exit 1
fi
test "$(cat "$d/hold/state/appointments/appointments.tsv")" = "$(printf 'executive\t%s' "$pending_successor")"
test "$(cat "$d/hold/state/liveness/unsafe-holds/executive")" = "$pre_swap_holds"
test -s "$d/hold/state/liveness/reset-pending-executive"
test ! -e "$pre_swap_archive"
rm -f "$d/hold/state/appointments/replacement-intents/pre-swap.json"
printf 'executive\t%s\trecovery-tx\n' "$pending_successor" > "$d/hold/state/appointments/appointments.tsv"
# Crash after the atomic registry swap, before provenance and ID output. The
# prepared transaction must be sufficient for an idempotent recovery retry.
crash_prior=$pending_successor
if VICHE_STATE_ROOT="$d/hold/state" VICHE_TOWN_ROOT="$d/hold/town" VICHE_SEATS_ROOT="$d/hold/seats" \
  VICHE_TEST_CRASH_AFTER_REGISTRY_SWAP=yes /bin/sh "$d/hold/town/government/appointments.sh" \
  replace executive "$crash_prior" branch-bootstrap act19_failure_threshold 'crash boundary fixture' >/dev/null 2>&1; then
  echo 'post-swap crash injection unexpectedly succeeded' >&2; exit 1
fi
crash_successor=$(awk -F '\t' '$1=="executive" {print $2}' "$d/hold/state/appointments/appointments.tsv")
test "$crash_successor" != "$crash_prior"
crash_tx=$(awk -F '\t' '$1=="executive" {print $3}' "$d/hold/state/appointments/appointments.tsv")
test -n "$crash_tx"
crash_intent=$d/hold/state/appointments/replacement-intents/$crash_tx.json
test -s "$crash_intent"
test "$(wc -l < "$d/hold/state/appointments/replacement-provenance.jsonl")" -eq 1
test "$(jq -r '.expected_prior_id' "$crash_intent")" = "$crash_prior"
printf 'executive\t%s\tcrash-boundary-invocation\n' "$crash_prior" \
  >> "$d/hold/state/liveness/unsafe-holds/executive"
printf '%s\n' "$crash_prior" > "$d/hold/state/liveness/reset-pending-executive"
VICHE_STATE_ROOT="$d/hold/state" VICHE_TOWN_ROOT="$d/hold/town" VICHE_SEATS_ROOT="$d/hold/seats" \
  /bin/sh "$d/hold/town/government/branch-bootstrap.sh" executive
test ! -e "$d/hold/state/liveness/reset-pending-executive"
test -s "$d/hold/state/liveness/archived-unsafe-holds/executive-$crash_prior-act19-reset"
# Carry the committed registry transaction through every recovery fixture.
# Registry swap is the transaction commit point; prepared intent plus matching
# current registry successor is valid even if provenance publication was lost.
VICHE_STATE_ROOT="$d/hold/state" VICHE_TOWN_ROOT="$d/hold/town" \
  VICHE_SEATS_ROOT="$d/hold/seats" VICHE_BRANCH_NOW="$((base+20))" \
  /bin/sh "$d/hold/town/government/branch-bootstrap.sh" executive
test ! -e "$d/hold/state/liveness/reset-pending-executive"
awk -F '\t' '$1=="executive" && $2=="unrelated-id" {found=1} END {exit !found}' \
  "$d/hold/state/liveness/unsafe-holds/executive"
# Recreate a committed recovery state for the later archive-retry test.
printf '%s\n' safe-id > "$d/hold/state/liveness/reset-pending-executive"
printf 'executive\tsafe-id\thold-inv-1\nexecutive\tunrelated-id\tunrelated-invocation\n' \
  > "$d/hold/state/liveness/unsafe-holds/executive"
printf 'executive\t%s\tarchive-recovery-tx\n' "$pending_successor" > "$d/hold/state/appointments/appointments.tsv"
: > "$d/hold/state/appointments/replacement-provenance.jsonl"
jq -cn --arg successor "$pending_successor" --arg tx archive-recovery-tx \
  '{state:"committed",office:"executive",expected_prior_id:"safe-id",
    successor:$successor,transaction:$tx,caller:"branch-bootstrap",trigger:"act19_failure_threshold"}' \
  > "$d/hold/state/appointments/replacement-provenance.jsonl"
# Set up an independent committed-provenance state for archive crash recovery.
mkdir -p "$d/hold/state/liveness/unsafe-holds" \
  "$d/hold/state/liveness/archived-unsafe-holds"
printf '%s\n' safe-id > "$d/hold/state/liveness/reset-pending-executive"
printf 'executive\tsafe-id\thold-inv-1\nexecutive\tsafe-id\thold-inv-2\nexecutive\tsafe-id\thold-inv-3\nexecutive\tunrelated-id\tunrelated-invocation\n' \
  > "$d/hold/state/liveness/unsafe-holds/executive"
printf 'executive\t%s\tarchive-recovery-tx\n' "$pending_successor" > "$d/hold/state/appointments/appointments.tsv"
: > "$d/hold/state/appointments/replacement-provenance.jsonl"
jq -cn --arg successor "$pending_successor" --arg tx archive-recovery-tx \
  '{state:"committed",office:"executive",expected_prior_id:"safe-id",
    successor:$successor,transaction:$tx,caller:"branch-bootstrap",trigger:"act19_failure_threshold"}' \
  > "$d/hold/state/appointments/replacement-provenance.jsonl"
# Model a crash after manifest commit but before archive publication.
rm -f "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset" \
  "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset.act19-manifest"
printf 'act19-manifest-v1\tsafe-id\tarchive-recovery-tx\nexecutive\tsafe-id\thold-inv-1\nexecutive\tsafe-id\thold-inv-2\nexecutive\tsafe-id\thold-inv-3\n' > "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset.act19-manifest"
# Model a crash after the recovery row was appended but before reset-pending
# was removed. The retry must recognize this exact reset event, not log twice.
printf '%s branch=executive session_reset=failure_count event=act19-reset-executive-safe-id recovery=completed-after-archive-retry\n' \
  "$(date -u +%FT%TZ)" > "$d/hold/state/liveness/recoveries.log"
rm -f "$d/hold/state/appointments/replacement-provenance.jsonl"
jq -cn --arg successor "$pending_successor" --arg tx archive-recovery-tx \
  '{state:"committed",office:"executive",expected_prior_id:"safe-id",
    successor:$successor,transaction:$tx,caller:"branch-bootstrap",trigger:"act19_failure_threshold"}' \
  > "$d/hold/state/appointments/replacement-provenance.jsonl"
VICHE_STATE_ROOT="$d/hold/state" VICHE_TOWN_ROOT="$d/hold/town" \
  VICHE_SEATS_ROOT="$d/hold/seats" VICHE_BRANCH_NOW="$((base+21))" \
  /bin/sh "$d/hold/town/government/branch-bootstrap.sh" executive
hold_after=$(VICHE_STATE_ROOT="$d/hold/state" /bin/sh "$d/hold/town/government/appointments.sh" resolve executive)
test "$hold_after" = "$pending_successor"
test "$hold_after" = "$(VICHE_STATE_ROOT="$d/hold/state" /bin/sh "$d/hold/town/government/appointments.sh" resolve executive)"
awk -F '\t' '$1=="executive" && $2=="unrelated-id" && $3=="unrelated-invocation" {found=1} END {exit !found}' "$d/hold/state/liveness/unsafe-holds/executive"
test -s "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset"
! grep -Fq 'unrelated-id' "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset"
test ! -e "$d/hold/state/liveness/reset-pending-executive"
test "$(grep -c 'event=act19-reset-executive-safe-id ' "$d/hold/state/liveness/recoveries.log")" -eq 1
# Repeated invocation after completion must not replace the replacement.
next_after_reset=$(cat "$MOCK_ROOT/next")
VICHE_STATE_ROOT="$d/hold/state" VICHE_TOWN_ROOT="$d/hold/town" \
  VICHE_SEATS_ROOT="$d/hold/seats" VICHE_BRANCH_NOW="$((base+22))" \
  /bin/sh "$d/hold/town/government/branch-bootstrap.sh" executive >/dev/null 2>&1
test "$(VICHE_STATE_ROOT="$d/hold/state" /bin/sh "$d/hold/town/government/appointments.sh" resolve executive)" = "$hold_after"
test "$(cat "$MOCK_ROOT/next")" = "$next_after_reset"

# Hold recovery inside the archive boundary: a writer (including a competing
# replacement) must wait for the same appointment lock and cannot swap registry.
printf '%s\n' safe-id > "$d/hold/state/liveness/reset-pending-executive"
printf 'executive\tsafe-id\thold-inv-1\n' > "$d/hold/state/liveness/unsafe-holds/executive"
rm -f "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset" \
  "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset.act19-manifest"
printf 'executive\t%s\tarchive-recovery-tx\n' "$pending_successor" > "$d/hold/state/appointments/appointments.tsv"
gate=$d/hold/archive-gate
env VICHE_TEST_RECOVERY_GATE="$gate" VICHE_STATE_ROOT="$d/hold/state" VICHE_TOWN_ROOT="$d/hold/town" \
  VICHE_SEATS_ROOT="$d/hold/seats" VICHE_BRANCH_NOW="$((base+23))" \
  /bin/sh "$d/hold/town/government/branch-bootstrap.sh" executive & recovery_pid=$!
i=0; while [ ! -e "$gate" ]; do i=$((i+1)); [ "$i" -lt 20 ] || exit 1; sleep 1; done
env VICHE_STATE_ROOT="$d/hold/state" VICHE_TOWN_ROOT="$d/hold/town" VICHE_SEATS_ROOT="$d/hold/seats" \
  /bin/sh "$d/hold/town/government/appointments.sh" replace executive "$pending_successor" concurrency-test fixture 'competing replacement' \
  > "$d/hold/writer.out" 2>&1 & writer_pid=$!
sleep 2
test "$(awk -F '\t' '$1=="executive" {print $2}' "$d/hold/state/appointments/appointments.tsv")" = "$pending_successor"
test -e "$d/hold/state/appointments/lock"
: > "$gate.release"
wait "$recovery_pid"
wait "$writer_pid"
test ! -e "$d/hold/state/appointments/lock"
replacement=$(awk -F '\t' '$1=="executive" {print $2}' "$d/hold/state/appointments/appointments.tsv")
test -n "$replacement" && test "$replacement" != "$pending_successor"
test ! -e "$d/hold/state/liveness/reset-pending-executive"
test -s "$d/hold/state/liveness/archived-unsafe-holds/executive-safe-id-act19-reset"
test ! -e "$d/hold/state/liveness/unsafe-holds/executive"

# A normal threshold reset must hold the appointment lock across the replace,
# transaction validation, archive, and pending-marker cleanup.
normal_old=$(awk -F '\t' '$1=="executive" {print $2}' "$d/hold/state/appointments/appointments.tsv")
normal_head=$(git -C "$d/hold/seats/branches/executive" rev-parse HEAD)
rm -f "$d/hold/state/liveness/last-reset-executive" "$d/hold/state/liveness/reset-sequence-executive"
printf '%s\texecutive\t%s\tnormal-event-1\tupstream_endpoint_unavailable\tyes\t%s\n' \
  "$((base+1))" "$normal_old" "$normal_head" \
  > "$d/hold/state/liveness/failures/events.tsv"
printf '%s\texecutive\t%s\tnormal-event-2\tupstream_endpoint_unavailable\tyes\t%s\n' \
  "$((base+2))" "$normal_old" "$normal_head" \
  >> "$d/hold/state/liveness/failures/events.tsv"
printf '%s\texecutive\t%s\tnormal-event-3\tupstream_endpoint_unavailable\tyes\t%s\n' \
  "$((base+3))" "$normal_old" "$normal_head" \
  >> "$d/hold/state/liveness/failures/events.tsv"
printf 'executive\t%s\tnormal-unsafe-invocation\n' "$normal_old" \
  > "$d/hold/state/liveness/unsafe-holds/executive"
set_status failed "$((base+4))" normal-current upstream_endpoint_unavailable true false "$normal_old"
normal_gate=$d/hold/normal-reset-gate
env VICHE_TEST_NORMAL_RESET_GATE="$normal_gate" VICHE_STATE_ROOT="$d/hold/state" \
  VICHE_TOWN_ROOT="$d/hold/town" VICHE_SEATS_ROOT="$d/hold/seats" \
  VICHE_BRANCH_NOW="$((base+40))" /bin/sh "$d/hold/town/government/branch-bootstrap.sh" executive \
  > "$d/hold/normal-reset.out" 2>&1 & normal_reset_pid=$!
i=0; while [ ! -e "$normal_gate" ]; do i=$((i+1)); [ "$i" -lt 20 ] || exit 1; sleep 1; done
normal_successor=$(awk -F '\t' '$1=="executive" {print $2}' "$d/hold/state/appointments/appointments.tsv")
test "$normal_successor" != "$normal_old"
(
  env VICHE_STATE_ROOT="$d/hold/state" VICHE_TOWN_ROOT="$d/hold/town" VICHE_SEATS_ROOT="$d/hold/seats" \
    VICHE_TEST_LOCK_ATTEMPT="$d/hold/writer-lock-attempt" \
    /bin/sh "$d/hold/town/government/appointments.sh" replace executive "$normal_successor" \
    concurrency-test fixture 'competing normal-reset replacement' > "$d/hold/normal-writer.out" 2>&1
) & normal_writer_pid=$!
i=0; while [ ! -e "$d/hold/writer-lock-attempt" ]; do i=$((i+1)); [ "$i" -lt 20 ] || exit 1; sleep 1; done
sleep 2
test "$(awk -F '\t' '$1=="executive" {print $2}' "$d/hold/state/appointments/appointments.tsv")" = "$normal_successor"
test -e "$d/hold/state/appointments/lock"
test -s "$d/hold/state/liveness/reset-pending-executive"
test -s "$d/hold/state/liveness/unsafe-holds/executive"
: > "$normal_gate.release"
wait "$normal_reset_pid"
wait "$normal_writer_pid"
test ! -e "$d/hold/state/appointments/lock"
test ! -e "$d/hold/state/liveness/reset-pending-executive"
test -s "$d/hold/state/liveness/archived-unsafe-holds/executive-$normal_old-act19-reset"
test ! -e "$d/hold/state/liveness/unsafe-holds/executive"
normal_final=$(awk -F '\t' '$1=="executive" {print $2}' "$d/hold/state/appointments/appointments.tsv")
test -n "$normal_final" && test "$normal_final" != "$normal_successor"
test "$(awk -F '\t' '$1=="executive" {print $3}' "$d/hold/state/appointments/appointments.tsv")" != ''
test -s "$d/hold/state/appointments/replacement-provenance.jsonl"

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
