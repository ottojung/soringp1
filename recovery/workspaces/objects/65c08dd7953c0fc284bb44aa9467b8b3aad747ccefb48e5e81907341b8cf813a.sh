#!/bin/sh
# This launcher does not decide what needs repair. The agent does.
set -eu
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
seats=${VICHE_SEATS_ROOT:-/var/lib/lubko/wd/viche-seats}
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
root=$state/recovery-steward
cwd=$seats/branches/recovery-steward
mkdir -p "$root" "$(dirname "$cwd")"
umask 077
exec 9>"$root/dispatch.lock"
flock -n 9 || exit 0
if [ ! -f "$cwd/.git" ] && [ ! -d "$cwd/.git" ]; then
  [ ! -e "$cwd" ] || { echo 'Recovery worktree path occupied' >&2; exit 1; }
  git -C "$town" worktree add --detach "$cwd" HEAD
fi
id=$(/bin/sh "$town/government/appointments.sh" ensure recovery-steward)
meta=$(antonina agent status --id "$id" --json)
mode=$(printf '%s\n' "$meta" | jq -er '.state')
fresh=no
case "$mode" in
  running) exit 0 ;;
  failed|stopped|killed)
    # No replay: the appointment service snapshots the old session first.
    printf '%s\n' "$meta" | jq -e '.alive == false' >/dev/null ||
      { echo 'Cannot duplicate active runner' >&2; exit 1; }
    id=$(/bin/sh "$town/government/appointments.sh" replace recovery-steward "$id" recovery-steward terminal_new_session 'Fresh recovery investigator after terminal failure; no prompt or tool replay')
    fresh=yes ;;
  idle|clearexit) : ;;
  *) echo "Unrecognized recovery runner state: $mode" >&2; exit 1 ;;
esac
now=$(date +%s)
last=0
[ ! -s "$root/last-dispatch" ] || last=$(cat "$root/last-dispatch")
case "$last" in ''|*[!0-9]*) last=0 ;; esac
interval=3600
if [ -s "$state/branches/incident.json" ] ||
   [ -s "$state/oversight/random/incident.json" ] ||
   [ -s "$state/oversight/incident.json" ]; then interval=600; fi
if [ "$fresh" != yes ] && [ "$last" -gt 0 ] && [ "$now" -ge "$last" ] &&
   [ $((now-last)) -lt "$interval" ]; then exit 0; fi
charter=${VICHE_CONSTITUTION:-}
[ -n "$charter" ] && [ -s "$charter" ] ||
  { echo 'Authoritative Founder charter unavailable' >&2; exit 1; }
[ -s "$town/government/RECOVERY-STEWARD.md" ] ||
  { echo 'Recovery stewardship mandate missing' >&2; exit 1; }
prompt=$(cat <<EOF
=== AUTHORITATIVE FOUNDER CONSTITUTION ===
$(cat "$charter")
=== END CONSTITUTION ===
$(cat "$town/government/RECOVERY-STEWARD.md")
Current town: $town
Current durable state: $state
Your worktree: $cwd
Current UTC: $(date -u +%FT%TZ)
EOF
)
policy_file="$town/government/AGENT-REPORTING-POLICY.md"
[ -s "$policy_file" ] || { echo "Viche: mandatory Founder agent policy missing" >&2; exit 1; }
prompt=$(printf '%s\n\n%s\n' "$prompt" "$(cat "$policy_file")")
antonina agent run --id "$id" --cwd "$cwd" --prompt "$prompt" --detach > "$root/dispatch.log" 2>&1
printf '%s\n' "$now" > "$root/last-dispatch"
printf '%s\t%s\t%s\n' "$(date -u +%FT%TZ)" "$id" "$fresh" >> "$root/dispatches.tsv"
echo "Recovery steward dispatched: $id"
