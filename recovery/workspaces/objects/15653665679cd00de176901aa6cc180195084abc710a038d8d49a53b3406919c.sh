#!/bin/sh
# Deterministic terminal-appointment continuity under Constitution VIII / Acts 2,5.
# This is a NEW reconciliatory appointment, never a replay of an uncertain turn.
set -eu
[ "$#" -eq 2 ] || { echo 'Usage: terminal-continuity.sh recover|instruction KEY' >&2; exit 2; }
operation=$1 office=$2
case "$office" in
  ''|*[!a-zA-Z0-9_-]*) echo 'Invalid office identifier' >&2; exit 2 ;;
esac
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
seats=${VICHE_SEATS_ROOT:-/var/lib/lubko/wd/viche-seats}
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
root=$state/continuity
# Any parliamentary seat or independent office can need continuity.
if [ -r "$town/government/seats.tsv" ] &&
   awk -F '\t' -v key="$office" '$1==key {found=1} END {exit !found}' "$town/government/seats.tsv"; then
  cwd=$seats/$office
else
  cwd=$seats/branches/$office
fi
receipt=$root/reconciliation-$office.json

if [ "$operation" = instruction ]; then
  [ -s "$receipt" ] || exit 0
  jq -er '.state == "awaiting_reconciliation"' "$receipt" >/dev/null 2>&1 || exit 0
  echo '=== MANDATORY RECOVERY OF PRIOR APPOINTMENT (NOT PROMPT REPLAY) ==='
  jq -c '{office,previous_agent,successor_agent,classification,terminal_evidence,worktree_head,old_session_preserved,at}' "$receipt"
  cat <<EOF
The previous agent failed during an uncertain backend turn. Do NOT blindly
repeat its previous prompt, tools, posts, commits, grants, external actions, or
messages. The original conversation may have performed side effects.
First inspect durable Git/board/task state and the terminal evidence above.
Review any pending steering/handoffs and reconcile what was completed.
Only then continue authorized unfinished work, independently of that old
conversation. If an external effect cannot be established safely, explicitly
record the uncertainty and request independent review. Never erase evidence.
=== END RECOVERY INSTRUCTION ===
EOF
  exit 0
fi
[ "$operation" = recover ] || exit 2
mkdir -p "$root"
umask 077
# Protect from concurrent boot/rescue processes; no double appointment.
exec 9>"$root/lock-$office"
flock -x 9
id=$(/bin/sh "$town/government/appointments.sh" resolve "$office") || exit 1
meta=$(antonina agent status --id "$id" --json) || exit 1
mode=$(printf '%s\n' "$meta" | jq -er '.state')
# Crash recovery: registry commit can succeed before our receipt is finalized.
# Repair the durable handoff from the actual appointment registry, without
# allocating a second successor or losing the OLD terminal evidence.
if [ -s "$receipt" ]; then
  prior=$(jq -r '.previous_agent // ""' "$receipt")
  phase=$(jq -r '.state // ""' "$receipt")
  if [ "$phase" = preparing ] && [ -n "$prior" ] && [ "$prior" != "$id" ]; then
    tmp=$(mktemp "$root/reconciled.XXXXXXXX")
    jq -c --arg new "$id" '. + {state:"awaiting_reconciliation",successor_agent:$new}' "$receipt" > "$tmp"
    mv -f "$tmp" "$receipt"
    echo "Continuity: restored committed $office appointment after interrupted transaction" >&2
  fi
fi
[ "$mode" = failed ] || exit 0
# Failed metadata by itself does not prove the old process has exited.
printf '%s\n' "$meta" | jq -e '.alive == false and (.active_runner == false or .active_runner == null)' >/dev/null || {
  echo "Continuity: failed $office still has a live process; refuse duplicate" >&2
  exit 1
}
printf '%s\n' "$meta" | jq -e '(.intent // "") != "stop"' >/dev/null || exit 1
cls=$(printf '%s\n' "$meta" | jq -r '.backend_error.classification // "unknown"')
transient=$(printf '%s\n' "$meta" | jq -r '.backend_error.transient // false')
# Classification is useful diagnostic evidence, NOT an exhaustive permission
# table for a distinct safe investigation. Any dead agent can be replaced
# after preserving evidence. The fresh session MUST assess provider failures,
# credentials and uncertain effects before performing original work.
[ -d "$cwd" ] && git -C "$cwd" rev-parse HEAD >/dev/null || exit 1
head=$(git -C "$cwd" rev-parse HEAD)
session=$(printf '%s\n' "$meta" | jq -r '.native_session_id // ""')
# Persist the pending safety instruction first, then atomically register
# a new appointment. appointments.sh itself snapshots terminal status/log/Git.
tmp=$(mktemp "$root/pending.XXXXXXXX")
printf '%s\n' "$meta" | jq -c \
  --arg office "$office" --arg old "$id" --arg cls "$cls" \
  --arg git_head "$head" --arg at "$(date -u +%FT%TZ)" \
  --arg old_session "$session" \
  '{state:"preparing",office:$office,previous_agent:$old,
    successor_agent:null,classification:$cls,at:$at,
    terminal_evidence:("appointments/terminal-evidence/" + $old),
    worktree_head:$git_head,old_session_preserved:($old_session!=""),
    old_session_id:$old_session,steers_pending:(.steers_pending//0),
    next_steer:(.next_steer//null)}' > "$tmp"
mv -f "$tmp" "$receipt"
if ! new=$(/bin/sh "$town/government/appointments.sh" replace "$office" "$id" terminal-continuity terminal_new_appointment 'Constitution VIII: dead office reappointed with durable evidence; no replay of uncertain turn'); then
  echo "Continuity: replacement of $office failed; pending evidence retained" >&2
  exit 1
fi
tmp=$(mktemp "$root/reconciled.XXXXXXXX")
jq -c --arg new "$new" '. + {state:"awaiting_reconciliation",successor_agent:$new}' "$receipt" > "$tmp"
mv -f "$tmp" "$receipt"
# A hold on the OLD request is valid evidence, not a prohibition on a NEW
# reconciliatory appointment. Archive it instead of erasing it.
hold=$state/liveness/unsafe-holds/$office
if [ -s "$hold" ] && grep -Fq "$id" "$hold"; then
  mkdir -p "$state/liveness/archived-unsafe-holds"
  mv "$hold" "$state/liveness/archived-unsafe-holds/$office-$id" || :
fi
printf '%s\t%s\t%s\t%s\n' "$(date -u +%FT%TZ)" "$office" "$id" "$new" >> "$root/reappointments.tsv"
echo "Viche continuity: $office reappointed from $id to $new; no prompt replay" >&2
