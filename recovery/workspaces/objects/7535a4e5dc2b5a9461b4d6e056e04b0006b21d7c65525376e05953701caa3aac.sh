#!/bin/sh
# Independent durable government offices, never parliamentary voting seats.
set -eu
[ "$#" -eq 1 ] || exit 2
branch=$1
case "$branch" in
  executive) id=c1e00002; title=Executive ;;
  judiciary) id=c1e00008; title=Judiciary ;;
  innovation-centre) id=c1e00011; title="Legislative Innovation Centre" ;;
  *) exit 2 ;;
esac
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
seats=${VICHE_SEATS_ROOT:-/var/lib/lubko/wd/viche-seats}
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
liv=$state/liveness
cwd=$seats/branches/$branch
if cut -f 1 "$town/government/seats.tsv" | grep -Fxq "$id"; then
  echo "Office $branch must never share a parliamentary voting seat" >&2
  exit 1
fi
if [ ! -f "$cwd/.git" ] && [ ! -d "$cwd/.git" ]; then
  if [ -d "$cwd" ] && [ -n "$(ls -A "$cwd")" ]; then
    echo "Refusing to replace occupied office worktree: $cwd" >&2
    exit 1
  fi
  mkdir -p "$(dirname "$cwd")"
  git -C "$town" worktree add --detach "$cwd" HEAD
fi
. "$(CDPATH= cd "$(dirname "$0")" && pwd -P)/office-continuity.sh"
mkdir -p "$liv"
umask 077
bootstrap_lock=$liv/branch-bootstrap-$branch.lock
bootstrap_lock_held=no
lock_try=0
while ! mkdir "$bootstrap_lock" 2>/dev/null; do
  lock_pid=
  [ ! -s "$bootstrap_lock/pid" ] || lock_pid=$(cat "$bootstrap_lock/pid")
  case "$lock_pid" in ''|*[!0-9]*) lock_pid= ;; esac
  # mkdir is the ownership claim. Missing/malformed PID can simply be the
  # winner between mkdir and pid publication; never remove another lock.
  if [ -n "$lock_pid" ] && ! kill -0 "$lock_pid" 2>/dev/null; then
    echo "stale or ambiguous bootstrap lock for $branch; refusing takeover" >&2
    exit 1
  fi
  lock_try=$((lock_try+1))
  [ "$lock_try" -lt 30 ] || { echo "Act 19 bootstrap lock busy for $branch" >&2; exit 1; }
  sleep 1
done
printf '%s\n' "$$" > "$bootstrap_lock/pid"
bootstrap_lock_held=yes
cleanup_locks() {
  if [ "${appointment_lock_held:-no}" = yes ]; then
    lock_pid=
    [ ! -s "$appointment_lock/pid" ] || lock_pid=$(cat "$appointment_lock/pid")
    if [ "$lock_pid" = "$$" ]; then
      rm -f "$appointment_lock/pid"
      rmdir "$appointment_lock" 2>/dev/null || :
    fi
    appointment_lock_held=no
  fi
  if [ "${bootstrap_lock_held:-no}" = yes ]; then
    bootstrap_owner=
    [ ! -s "$bootstrap_lock/pid" ] || bootstrap_owner=$(cat "$bootstrap_lock/pid")
    if [ "$bootstrap_owner" = "$$" ]; then
      rm -f "$bootstrap_lock/pid"
      rmdir "$bootstrap_lock" 2>/dev/null || :
    fi
    bootstrap_lock_held=no
  fi
}
trap 'cleanup_locks' EXIT
trap 'exit 129' HUP
trap 'exit 130' INT
trap 'exit 143' TERM

archive_unsafe_hold() {
  # The manifest is the transaction-bound commit record. It is atomically
  # published before the unchanged-format archive. This protects against
  # crashes and accidental corruption, not an actor able to rewrite all files.
  ah_file=$1 ah_id=$2 ah_tx=$3 ah_dest=$4
  [ -s "$ah_file" ] || return 0
  ah_manifest=$ah_dest.act19-manifest
  if [ -e "$ah_dest" ]; then
    [ -s "$ah_manifest" ] || { echo "Act 19 reset: legacy archive lacks transaction manifest" >&2; return 1; }
  fi
  if [ ! -e "$ah_manifest" ]; then
    ah_stage=$(mktemp "$liv/unsafe-hold-manifest.XXXXXXXX") || return 1
    if ! {
      printf 'act19-manifest-v1\t%s\t%s\n' "$ah_id" "$ah_tx"
      awk -F '\t' -v id="$ah_id" 'NF>=3 && $2==id {print}' "$ah_file"
    } > "$ah_stage" || [ "$(wc -l < "$ah_stage")" -lt 2 ]; then
      rm -f "$ah_stage"
      return 1
    fi
    # Verify the manifest rows are exactly the currently active filtered rows.
    ah_rows=$(mktemp "$liv/unsafe-hold-rows.XXXXXXXX") || { rm -f "$ah_stage"; return 1; }
    awk -F '\t' -v id="$ah_id" '$2==id {print}' "$ah_file" > "$ah_rows"
    tail -n +2 "$ah_stage" > "$ah_rows.manifest"
    if ! cmp -s "$ah_rows" "$ah_rows.manifest"; then
      rm -f "$ah_stage" "$ah_rows" "$ah_rows.manifest"; return 1
    fi
    rm -f "$ah_rows" "$ah_rows.manifest"
    mv "$ah_stage" "$ah_manifest" || { rm -f "$ah_stage"; return 1; }
  fi
  ah_header=$(sed -n '1p' "$ah_manifest")
  printf '%s\t%s\t%s\n' act19-manifest-v1 "$ah_id" "$ah_tx" > "$liv/unsafe-hold-expected"
  sed -n '1p' "$ah_manifest" > "$liv/unsafe-hold-header"
  if ! cmp -s "$liv/unsafe-hold-expected" "$liv/unsafe-hold-header"; then
    rm -f "$liv/unsafe-hold-expected" "$liv/unsafe-hold-header"; echo "Act 19 reset: manifest transaction mismatch" >&2; return 1
  fi
  rm -f "$liv/unsafe-hold-expected" "$liv/unsafe-hold-header"
  ah_rows=$(mktemp "$liv/unsafe-hold-rows.XXXXXXXX") || return 1
  ah_manifest_rows=$(mktemp "$liv/unsafe-hold-manifest-rows.XXXXXXXX") || { rm -f "$ah_rows"; return 1; }
  awk -F '\t' -v id="$ah_id" '$2==id {print}' "$ah_file" > "$ah_rows"
  tail -n +2 "$ah_manifest" > "$ah_manifest_rows"
  if [ ! -s "$ah_manifest_rows" ] || ! cmp -s "$ah_rows" "$ah_manifest_rows"; then
    rm -f "$ah_rows" "$ah_manifest_rows"; echo "Act 19 reset: active rows differ from manifest" >&2; return 1
  fi
  if [ -e "$ah_dest" ] && ! cmp -s "$ah_dest" "$ah_manifest_rows"; then
    rm -f "$ah_rows" "$ah_manifest_rows"; echo "Act 19 reset: archive differs from manifest" >&2; return 1
  fi
  if [ ! -e "$ah_dest" ]; then
    ah_stage=$(mktemp "$liv/unsafe-hold-archive.XXXXXXXX") || { rm -f "$ah_rows" "$ah_manifest_rows"; return 1; }
    cp "$ah_manifest_rows" "$ah_stage" || { rm -f "$ah_stage" "$ah_rows" "$ah_manifest_rows"; return 1; }
    mv "$ah_stage" "$ah_dest" || { rm -f "$ah_stage" "$ah_rows" "$ah_manifest_rows"; return 1; }
  fi
  rm -f "$ah_rows" "$ah_manifest_rows"
  ah_active=$(mktemp "$liv/unsafe-hold-active.XXXXXXXX") || return 1
  if ! awk -F '\t' -v id="$ah_id" '$2!=id {print}' "$ah_file" > "$ah_active"; then
    rm -f "$ah_active"
    return 1
  fi
  if [ -s "$ah_active" ]; then
    mv "$ah_active" "$ah_file" || { rm -f "$ah_active"; return 1; }
  else
    rm -f "$ah_active" "$ah_file"
  fi
}
# Recover an interrupted threshold reset by its durable intent, independent of
# the now-replaced appointment's state or the cleared failure counter.
pending_reset=$liv/reset-pending-$branch
if [ -s "$pending_reset" ]; then
  # Match appointments.sh writers' lock. Acquire after bootstrap_lock; no path
  # acquires these in the reverse order. Keep through archive and marker removal.
  appointment_root=$state/appointments
  mkdir -p "$appointment_root"
  appointment_lock=$appointment_root/lock
  appointment_lock_held=no
  appointment_lock_try=0
  while ! mkdir "$appointment_lock" 2>/dev/null; do
    lock_pid=
    [ ! -s "$appointment_lock/pid" ] || lock_pid=$(cat "$appointment_lock/pid")
    case "$lock_pid" in ''|*[!0-9]*) echo 'ambiguous appointment lock; refusing Act 19 recovery' >&2; exit 1;; esac
    if ! kill -0 "$lock_pid" 2>/dev/null; then echo 'stale appointment lock; refusing Act 19 recovery' >&2; exit 1; fi
    appointment_lock_try=$((appointment_lock_try+1))
    [ "$appointment_lock_try" -lt 20 ] || { echo 'appointment lock busy during Act 19 recovery' >&2; exit 1; }
    sleep 1
  done
  printf '%s\n' "$$" > "$appointment_lock/pid"
  appointment_lock_held=yes
  pending_old=$(cat "$pending_reset")
  registry_row=$(awk -F '\t' -v k="$branch" '$1==k {n++; row=$0; if(NF!=3) bad=1} END {if(n!=1 || bad) exit 1; print row}' "$appointment_root/appointments.tsv") || exit 1
  current=$(printf '%s\n' "$registry_row" | awk -F '\t' '{print $2}')
   # Registry swap is the commit point, but a prepared intent alone is not
   # proof it happened: appointments.sh can crash before its atomic roster mv.
   # Require the exact transaction's successor in the authoritative registry.
  replacement_root=$appointment_root
  registry_tx=$(printf '%s\n' "$registry_row" | awk -F '\t' '{print $3}')
  case "$current:$registry_tx" in *[!a-zA-Z0-9_:-]*|:*) exit 1;; esac
  reset_intent=
  for candidate_intent in "$replacement_root"/replacement-intents/*.json; do
    [ -f "$candidate_intent" ] || continue
    if jq -e --arg office "$branch" --arg prior "$pending_old" --arg successor "$current" --arg tx "$registry_tx" \
      '.office==$office and .expected_prior_id==$prior and .proposed_successor==$successor and
        .transaction==$tx and $tx!="" and
       .caller=="branch-bootstrap" and .trigger=="act19_failure_threshold" and
       (.state=="committed" or .state=="prepared")' "$candidate_intent" >/dev/null 2>&1; then
      reset_intent=$candidate_intent
      break
    fi
  done
  if [ -z "$reset_intent" ] && [ -s "$replacement_root/replacement-provenance.jsonl" ]; then
    if jq -e --arg office "$branch" --arg prior "$pending_old" --arg successor "$current" --arg tx "$registry_tx" \
      'select(.state=="committed" and .office==$office and .expected_prior_id==$prior and
        .successor==$successor and .transaction==$tx and $tx!="" and .caller=="branch-bootstrap" and
        .trigger=="act19_failure_threshold")' \
      "$replacement_root/replacement-provenance.jsonl" >/dev/null 2>&1; then
      reset_intent=provenance
    fi
  fi
  if [ "$current" = "$pending_old" ] || [ -z "$reset_intent" ]; then
    echo "Act 19 reset recovery: no matching committed replacement for $branch" >&2
    exit 1
  fi
  # The registry replacement is already committed. Complete only the
  # post-commit bookkeeping; never let normal threshold evaluation select the
  # old failed agent again or create another successor on an archive retry.
  pending_hold=$state/liveness/unsafe-holds/$branch
  pending_archive=$liv/archived-unsafe-holds/$branch-$pending_old-act19-reset
  if [ -s "$pending_hold" ] && awk -F '\t' -v id="$pending_old" '$2==id {found=1} END {exit !found}' "$pending_hold"; then
    mkdir -p "$liv/archived-unsafe-holds" || exit 1
    if [ "${VICHE_TEST_RECOVERY_GATE:-}" != "" ]; then
      : > "$VICHE_TEST_RECOVERY_GATE"
      while [ ! -e "$VICHE_TEST_RECOVERY_GATE.release" ]; do sleep 1; done
    fi
     archive_unsafe_hold "$pending_hold" "$pending_old" "$registry_tx" "$pending_archive" || exit 1
  fi
  recovery_event=act19-reset-$branch-$pending_old
  append_recovery=yes
  if [ -e "$liv/recoveries.log" ]; then
    if grep -F "event=$recovery_event " "$liv/recoveries.log" >/dev/null; then
      append_recovery=no
    else
      grep_status=$?
      [ "$grep_status" -eq 1 ] || exit 1
    fi
  fi
  if [ "$append_recovery" = yes ]; then
    printf '%s branch=%s session_reset=failure_count threshold=%s window=%s cooldown=%s event=%s recovery=completed-after-archive-retry\n' \
      "$(date -u +%FT%TZ)" "$branch" "$oc_threshold" "$oc_window" "$oc_cooldown" "$recovery_event" \
      >> "$liv/recoveries.log" || exit 1
  fi
  rm -f "$pending_reset"
  rm -f "$appointment_lock/pid"
  rmdir "$appointment_lock"
  appointment_lock_held=no
  exit 0
fi
id=$(/bin/sh "$town/government/appointments.sh" ensure "$branch")
meta=$(antonina agent status --id "$id" --json)
now=$(date +%s)
mode=$(printf '%s\n' "$meta" | jq -r '.state')
reason=$(printf '%s\n' "$meta" | jq -r '.backend_error.classification // ""')
tflag=$(printf '%s\n' "$meta" | jq -r '.backend_error.transient // false')
invocation=$(printf '%s\n' "$meta" | jq -r '.invocation_id // .run_id // .finished_at // ""')
finished=$(printf '%s\n' "$meta" | jq -r '.finished_at // ""')
if [ "$mode" = failed ]; then
  if oc_is_transient "$reason" "$tflag"; then
    unsafe=$(printf '%s\n' "$meta" | jq -r 'if .backend_error.automatic_retry_safe == false then "yes" else "no" end')
    retry_safe=$(printf '%s\n' "$meta" | jq -r 'if .backend_error.automatic_retry_safe == true and .backend_error.transient == true then "yes" else "no" end')
    oc_record_failure "$liv" "$branch" "$id" "$invocation" "$reason" "$finished" "$retry_safe" "$now" "$cwd" || exit 1
    [ "$retry_safe" = yes ] || oc_mark_unsafe_hold "$liv" "$branch" "$id" "$invocation"
  else
    oc_surface_permanent "$liv" "$id" "$reason"
  fi
fi
oc_commit_age_signal "$liv" "$id" "$cwd" "$now"
# Act 19 §3.1: the reset decision is decidable from the failure record alone
# and does not depend on the currently-observed state. An oscillating agent
# (failed -> re-dispatched -> running) is reset once it accumulates the
# threshold of consecutive transient failures inside the window.
oc_worktree=$cwd
reset_due=false
if oc_reset_due "$liv" "$branch" "$now"; then reset_due=true; fi
if [ "$reset_due" = true ]; then
  # Hold the shared appointment lock from replacement through all transaction
  # binding and cleanup. The owner token is accepted only while this live PID
  # is recorded in the lock directory; it is not a general lock bypass.
  appointment_root=$state/appointments
  mkdir -p "$appointment_root"
  appointment_lock=$appointment_root/lock
  appointment_lock_held=no
  appointment_lock_try=0
  while ! mkdir "$appointment_lock" 2>/dev/null; do
    lock_pid=
    [ ! -s "$appointment_lock/pid" ] || lock_pid=$(cat "$appointment_lock/pid")
    case "$lock_pid" in ''|*[!0-9]*) lock_pid= ;; esac
    if [ -z "$lock_pid" ] || ! kill -0 "$lock_pid" 2>/dev/null; then
      echo 'ambiguous/stale appointment lock; refusing Act 19 reset' >&2
      exit 1
    fi
    appointment_lock_try=$((appointment_lock_try+1))
    [ "$appointment_lock_try" -lt 20 ] || { echo 'appointment lock busy during Act 19 reset' >&2; exit 1; }
    sleep 1
  done
  printf '%s\n' "$$" > "$appointment_lock/pid"
  appointment_lock_held=yes
  snapshot=$(mktemp -d "$liv/branch-$id-recovery-XXXXXX")
  printf '%s\n' "$meta" > "$snapshot/status.json"
  antonina agent log --id "$id" --lines 200 > "$snapshot/log.txt" 2>&1 || :
  git -C "$cwd" status --short > "$snapshot/worktree.txt"
  oc_quiesce_for_reset "$id" || exit 1
  oc_old_id=$id
  printf '%s\n' "$oc_old_id" > "$pending_reset"
  id=$(VICHE_APPOINTMENT_LOCK_OWNER="$$" /bin/sh "$town/government/appointments.sh" replace "$branch" "$id" branch-bootstrap act19_failure_threshold 'Act 19 threshold reset after durable failure evidence and quiescence')
  registry_row=$(awk -F '\t' -v k="$branch" '$1==k {n++; row=$0; if(NF!=3) bad=1} END {if(n!=1 || bad) exit 1; print row}' "$state/appointments/appointments.tsv") || exit 1
  registry_successor=$(printf '%s\n' "$registry_row" | awk -F '\t' '{print $2}')
  registry_tx=$(printf '%s\n' "$registry_row" | awk -F '\t' '{print $3}')
  case "$registry_successor:$registry_tx" in *[!a-zA-Z0-9_:-]*|:*) exit 1;; esac
  if [ "$registry_successor" != "$id" ] || [ -z "$registry_tx" ]; then
    echo 'Act 19 reset: replacement registry row does not match exact successor/transaction' >&2
    exit 1
  fi
  reset_committed=no
  for candidate_intent in "$state/appointments"/replacement-intents/*.json; do
    [ -f "$candidate_intent" ] || continue
    if jq -e --arg office "$branch" --arg prior "$oc_old_id" --arg successor "$id" --arg tx "$registry_tx" \
      '.office==$office and .expected_prior_id==$prior and .proposed_successor==$successor and
       .transaction==$tx and .caller=="branch-bootstrap" and .trigger=="act19_failure_threshold" and
       (.state=="prepared" or .state=="committed")' "$candidate_intent" >/dev/null 2>&1; then
      reset_committed=yes
      break
    fi
  done
  if [ "$reset_committed" != yes ] && [ -s "$state/appointments/replacement-provenance.jsonl" ] &&
     jq -e --arg office "$branch" --arg prior "$oc_old_id" --arg successor "$id" --arg tx "$registry_tx" \
       'select(.state=="committed" and .office==$office and .expected_prior_id==$prior and
        .successor==$successor and .transaction==$tx and .caller=="branch-bootstrap" and
        .trigger=="act19_failure_threshold")' "$state/appointments/replacement-provenance.jsonl" >/dev/null 2>&1; then
    reset_committed=yes
  fi
  [ "$reset_committed" = yes ] || { echo 'Act 19 reset: exact replacement transaction has no durable intent/provenance' >&2; exit 1; }
  if [ "${VICHE_TEST_NORMAL_RESET_GATE:-}" != "" ]; then
    : > "$VICHE_TEST_NORMAL_RESET_GATE"
    while [ ! -e "$VICHE_TEST_NORMAL_RESET_GATE.release" ]; do sleep 1; done
  fi
  printf '%s\n' "$now" > "$liv/last-reset-$branch"
  meta=$(antonina agent status --id "$id" --json)
  oc_clear_failures "$liv" "$branch"
  # Archive only after replacement, but treat archive failure as incomplete:
  # leave the hold in place for retry rather than masking a stale unsafe hold.
  oc_hold=$state/liveness/unsafe-holds/$branch
  if [ -s "$oc_hold" ] && awk -F '\t' -v id="$oc_old_id" '$2==id {found=1} END {exit !found}' "$oc_hold"; then
    oc_archive=$liv/archived-unsafe-holds/$branch-$oc_old_id-act19-reset
    mkdir -p "$liv/archived-unsafe-holds" || exit 1
    archive_unsafe_hold "$oc_hold" "$oc_old_id" "$registry_tx" "$oc_archive" || {
      echo "Act 19 reset: unable to archive unsafe hold for $branch; retry required" >&2
      exit 1
    }
  fi
  printf '%s branch=%s session_reset=failure_count threshold=%s window=%s cooldown=%s evidence=%s\n' \
    "$(date -u +%FT%TZ)" "$branch" "$oc_threshold" "$oc_window" "$oc_cooldown" "$snapshot" \
    >> "$liv/recoveries.log"
  rm -f "$pending_reset"
  rm -f "$appointment_lock/pid"
  rmdir "$appointment_lock"
  appointment_lock_held=no
  reset_due=true
  # The single replacement above completed this reset.
fi
# A single terminal failure with unsafe literal replay can NEVER reach the
# three-failure oscillation threshold. Constitution VIII separately requires
# renewed institutional continuity: replace the DEAD appointment and give a
# fresh agent a reconciliation instruction (never reuse the old model turn).
# Retain Act 19's existing counter/threshold for still-recoverable oscillations.
if [ "$reset_due" != true ] && [ "$mode" = failed ] &&
   [ -f "$town/government/terminal-continuity.sh" ]; then
  /bin/sh "$town/government/terminal-continuity.sh" recover "$branch" || exit 1
  id=$(/bin/sh "$town/government/appointments.sh" resolve "$branch")
  meta=$(antonina agent status --id "$id" --json)
fi
# Antonina selects the provider/model/variant under its own current policy.
# Appointment validity is determined by the managed agent state, not a pin.
