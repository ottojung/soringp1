#!/bin/sh
# Durable founder intake, running independently of parliamentary sittings.
set -eu
: "${VICHE_TOWNHALL_ID:?Town Hall ID required}"
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
q=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/founder-inbox
mkdir -p "$q/pending" "$q/sent" "$q/ack"
d=$(mktemp -d)
trap 'rm -rf "$d"' 0
old=
[ ! -s "$q/town-cursor" ] || old=$(cat "$q/town-cursor")
latest=
page=1
stop=0
while :; do
  antonina board show --id "$VICHE_TOWNHALL_ID" --page "$page" --json > "$d/page"
  jq -e '.messages|type=="array"' "$d/page" >/dev/null
  count=$(jq '.messages|length' "$d/page")
  [ "$count" -gt 0 ] || break
  [ -n "$latest" ] || latest=$(jq -r '.messages[-1].id // empty' "$d/page")
  [ -n "$latest" ] || exit 1
  jq -c '.messages|reverse|.[]' "$d/page" > "$d/items"
  while IFS= read -r line; do
    id=$(printf '%s\n' "$line" | jq -r '.id // empty')
    [ -n "$id" ] || exit 1
    if [ -n "$old" ] && [ "$id" = "$old" ]; then stop=1; break; fi
    [ "$(printf '%s\n' "$line" | jq -r '.author // empty')" = Vitalik ] || continue
    key=$(printf '%s' "$id" | sha256sum | cut -d ' ' -f1)
    [ ! -f "$q/pending/$key.json" ] || continue
    [ ! -f "$q/sent/$key.json" ] || continue
    printf '%s\n' "$line" | jq -c --arg issue "$VICHE_TOWNHALL_ID" '{id,author,body,createdAt,issueNumber:$issue}' > "$d/new"
    mv "$d/new" "$q/pending/$key.json"
  done < "$d/items"
  [ "$stop" -eq 0 ] || break
  [ "$count" -eq 50 ] || break
  page=$((page+1))
done
if [ -n "$latest" ]; then
  printf '%s\n' "$latest" > "$d/cursor"
  mv "$d/cursor" "$q/town-cursor"
fi
# Board activity outside Town Hall, using monotonic positions.
last=
[ ! -s "$q/feed-cursor" ] || last=$(cat "$q/feed-cursor")
# Board v4 publishes stable opaque message IDs. Older intake runs stored
# numeric positions; accept those until the next successful observation, then
# persist the entry ID instead. Never discard an unrecognized durable anchor.
last_kind=id
case "$last" in ''|*[!0-9]*) :;; *) last_kind=position;; esac
page=1
first=
# The board supports 500 entries per page. A recovered historical cursor may
# be thousands of entries behind; page through the history in bounded batches.
page_size=500
while :; do
  antonina board feed --page "$page" --limit "$page_size" --json > "$d/feed"
  jq -e '.entries|type=="array"' "$d/feed" >/dev/null
  count=$(jq '.entries|length' "$d/feed")
  [ "$count" -gt 0 ] || break
  [ -n "$first" ] || first=$(jq -r '.entries[0].id // empty' "$d/feed")
  stop=0
  jq -c '.entries[]' "$d/feed" > "$d/items"
  while IFS= read -r line; do
    pos=$(printf '%s\n' "$line" | jq -r '.position // 0')
    entry_id=$(printf '%s\n' "$line" | jq -r '.id // empty')
    if [ "$last_kind" = id ]; then
      if [ -n "$last" ] && [ "$entry_id" = "$last" ]; then stop=1; break; fi
    elif [ -n "$last" ] && [ "$pos" -le "$last" ]; then
      stop=1; break
    fi
    [ "$(printf '%s\n' "$line" | jq -r '.author // empty')" = Vitalik ] || continue
    issue=$(printf '%s\n' "$line" | jq -r '.issueNumber // empty')
    [ "$issue" != "$VICHE_TOWNHALL_ID" ] || continue
    id=$(printf '%s\n' "$line" | jq -r '.messageId // .id // empty')
    [ -n "$id" ] || continue
    key=$(printf '%s' "$id" | sha256sum | cut -d ' ' -f1)
    [ ! -f "$q/pending/$key.json" ] || continue
    [ ! -f "$q/sent/$key.json" ] || continue
    printf '%s\n' "$line" | jq -c '{id:(.messageId // .id),author,body,createdAt:.at,issueNumber:(.issueNumber|tostring)}' > "$d/new"
    mv "$d/new" "$q/pending/$key.json"
  done < "$d/items"
  [ "$stop" -eq 0 ] || break
  [ -n "$last" ] || break
  [ "$count" -eq "$page_size" ] || break
  page=$((page+1))
done
# The source may have been compacted or changed. Do not silently jump past
# an unseen Founder instruction if our exact prior event cannot be located.
if [ "$last_kind" = id ] && [ -n "$last" ] && [ "$stop" -eq 0 ]; then
  echo "Founder feed cursor not found in board history: $last" >&2
  exit 1
fi
if [ -n "$first" ]; then
  printf '%s\n' "$first" > "$d/cursor"
  mv "$d/cursor" "$q/feed-cursor"
fi
# Never confuse Antonina accepting an invocation with clerk processing it.
now=$(date +%s)
for f in "$q/sent"/*.json; do
  [ -f "$f" ] || continue
  key=$(basename "$f" .json)
  [ ! -f "$q/ack/$key" ] || continue
  stamp=$(stat -c %Y "$f")
  if [ $((now-stamp)) -ge 600 ]; then mv "$f" "$q/pending/$(basename "$f")"; fi
done
set -- "$q/pending"/*.json
[ -f "$1" ] || exit 0
retry="$q/next-dispatch"
now=$(date +%s)
next=0
[ ! -s "$retry" ] || next=$(cat "$retry")
case "$next" in ''|*[!0-9]*) next=0;; esac
[ "$now" -ge "$next" ] || exit 0
clerk=$(head -n 1 "$town/government/seats.tsv" | cut -f1)
seat=${VICHE_SEATS_ROOT:-/var/lib/lubko/wd/viche-seats}/$clerk
[ -d "$seat" ] || exit 1
charter=${VICHE_CONSTITUTION_DIR:-/var/lib/lubko/from-host/viche-constitution}/CONSTITUTION.md
[ -s "$charter" ] || exit 1
body=$(jq -rs 'sort_by(.createdAt)|map("Founder instruction "+(.id//"?")+" on issue #"+(.issueNumber//"?")+":\n"+(.body//""))|join("\n\n")' "$@")
clerk=$(/bin/sh "$town/government/appointments.sh" ensure "$clerk")
mode=$(antonina agent status --id "$clerk" --json | jq -er '.state')
# Founder instructions remain pending while a failed Clerk is cooling down.
# Do not bypass the same liveness gate used by ordinary sittings.
if [ -f "$town/government/clerk-liveness.sh" ]; then
  /bin/sh "$town/government/clerk-liveness.sh" --gate || exit 0
fi
keys=
for f in "$@"; do keys="$keys $(basename "$f" .json)"; done
charter_text=$(cat "$charter")
prompt=$(cat <<EOF
PRIORITY FOUNDER INTAKE. These independently retrieved messages are authored exactly Vitalik:
$body
Before triage, read each full linked issue and the current $town/AGENTS.md and $town/government/LAWS.md. Follow their current assignment rules: initiate or delegate productive work only for issues explicitly assigned to billy-dev through the Antonina execution-target/dispatch surface; an issue title alone is not an assignment. Preserve existing in-flight work and handoffs. Record a durable actionable mandate with an owner and next step, and convene or delegate only as appropriate to that assignment. Antonina controls provider and model selection; do not request, prescribe, or assume any model, variant, or provider.

After publicly recording meaningful triage (not just reading), write an empty receipt file in $q/ack for every processed key:$keys. Missing receipts cause automatic retry in 10 minutes. The authoritative founder-controlled Constitution is reproduced below and has highest authority; parliament may NOT amend it or its S6 bootstrap. Do not enact laws without actual votes.

=== AUTHORITATIVE CONSTITUTION ===
$charter_text
=== END AUTHORITATIVE CONSTITUTION ===
EOF
)
policy_file="$town/government/AGENT-REPORTING-POLICY.md"
[ -s "$policy_file" ] || { echo "Viche: mandatory Founder agent policy missing" >&2; exit 1; }
prompt=$(printf '%s\n\n%s\n' "$prompt" "$(cat "$policy_file")")
if [ "$mode" = running ]; then
  accepted=0
  antonina agent run --id "$clerk" --cwd "$seat" --prompt "$prompt" --steer --detach && accepted=1
else
  accepted=0
  antonina agent run --id "$clerk" --cwd "$seat" --prompt "$prompt" --detach && accepted=1
fi
if [ "$accepted" -ne 1 ]; then
  n=0
  [ ! -s "$q/failure-count" ] || n=$(cat "$q/failure-count")
  case "$n" in ''|*[!0-9]*) n=0;; esac
  n=$((n+1))
  delay=60
  i=1
  while [ "$i" -lt "$n" ] && [ "$delay" -lt 1800 ]; do delay=$((delay*2)); i=$((i+1)); done
  [ "$delay" -le 1800 ] || delay=1800
  printf '%s\n' "$n" > "$q/failure-count"
  printf '%s\n' "$((now+delay))" > "$retry"
  printf '%s failures=%s retry_seconds=%s\n' "$(date -u +%FT%TZ)" "$n" "$delay" >> "$q/failures.log"
  [ "$n" -lt 5 ] || printf 'Dispatch failure count %s; pending events retained; retry in %ss\n' "$n" "$delay" > "$q/ESCALATION"
  exit 1
fi
rm -f "$retry" "$q/failure-count" "$q/ESCALATION"
for f in "$@"; do dest="$q/sent/$(basename "$f")"; mv "$f" "$dest"; touch "$dest"; done
printf 'Founder intake dispatched %s events to clerk (prior state %s)\n' "$#" "$mode"
