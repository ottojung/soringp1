#!/bin/sh
# Hermetic regression: busy clerk must receive Founder messages despite sitting skip.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' 0
mkdir -p "$d/bin" "$d/town/government" "$d/state" "$d/seats/c1a00001" "$d/charter" "$d/mock"
printf 'c1a00001\tClerk\tFounder intake\n' > "$d/town/government/seats.tsv"
printf 'Protected constitution fixture\n' > "$d/charter/CONSTITUTION.md"
cat > "$d/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
case "$1 $2" in
'board show')
  while [ "$#" -gt 0 ]; do
    case "$1" in --page) page=$2; shift 2;; *) shift;; esac
  done
  jq -c --argjson page "$page" '{messages:(.messages | (length) as $n | .[([0,$n-$page*50]|max):($n-($page-1)*50)])}' "$MOCK_DIR/comments"
  ;;
'board feed')
  echo '{"entries":[]}'
  ;;
'agent status')
  printf '{"state":"%s"}\n' "$(cat "$MOCK_DIR/status")"
  ;;
'agent run')
  if [ "${MOCK_FAIL:-0}" = 1 ]; then exit 9; fi
  printf '%s\n' "$*" >> "$MOCK_DIR/prompts"
  while [ "$#" -gt 0 ]; do
    if [ "$1" = --prompt ]; then
      shift
      printf '%s\n' "$1" > "$MOCK_DIR/last-prompt"
      break
    fi
    shift
  done
  printf '1\n' >> "$MOCK_DIR/calls"
  ;;
*) echo "Unexpected mock Antonina call: $*" >&2; exit 9;;
esac
MOCK
chmod +x "$d/bin/antonina"
cat > "$d/mock/comments" <<'JSON'
{"messages":[{"id":"a","author":"other","createdAt":"2026-10-14T01:00:00Z","body":"ignore"},{"id":"b","author":"Vitalik","createdAt":"2026-10-14T02:00:00Z","body":"Issue #298 Janitor Office"}]}
JSON
printf 'running\n' > "$d/mock/status"
PATH="$d/bin:$PATH"
MOCK_DIR="$d/mock"
VICHE_TOWNHALL_ID=302
mkdir -p "$d/town/government"
cp "$repo/tests/appointment-id-stub.sh" "$d/town/government/appointments.sh"
cp "$repo/government/AGENT-REPORTING-POLICY.md" "$d/town/government/AGENT-REPORTING-POLICY.md"
VICHE_TOWN_ROOT="$d/town"
VICHE_SEATS_ROOT="$d/seats"
VICHE_STATE_ROOT="$d/state"
VICHE_CONSTITUTION_DIR="$d/charter"
export PATH MOCK_DIR VICHE_TOWNHALL_ID VICHE_TOWN_ROOT VICHE_SEATS_ROOT VICHE_STATE_ROOT VICHE_CONSTITUTION_DIR
/bin/sh "$repo/government/founder-intake.sh"
[ "$(wc -l < "$d/mock/calls")" -eq 1 ]
grep -q -- '--steer' "$d/mock/prompts"
grep -Fq "current $d/town/AGENTS.md and $d/town/government/LAWS.md" "$d/mock/last-prompt"
grep -Fq 'initiate or delegate productive work only for issues explicitly assigned to billy-dev through the Antonina execution-target/dispatch surface' "$d/mock/last-prompt"
grep -Fq 'an issue title alone is not an assignment' "$d/mock/last-prompt"
grep -Fq 'Preserve existing in-flight work and handoffs' "$d/mock/last-prompt"
grep -Fq 'Antonina controls provider and model selection' "$d/mock/last-prompt"
if grep -Fq 'Viche+Kawun exclusive scope' "$d/mock/last-prompt" ||
   grep -Fq 'free model' "$d/mock/last-prompt" ||
   grep -Fq 'model pin' "$d/mock/last-prompt"; then
  echo 'Stale project or model restriction remains in Founder-intake prompt' >&2; exit 1
fi
[ "$(find "$d/state/founder-inbox/ack" -type f | wc -l)" -eq 0 ]
[ "$(find "$d/state/founder-inbox/sent" -name '*.json' | wc -l)" -eq 1 ]
/bin/sh "$repo/government/founder-intake.sh"
[ "$(wc -l < "$d/mock/calls")" -eq 1 ]
# Failed backend retains durable pending queue; an idle clerk can be restarted.
cat > "$d/mock/comments" <<'JSON'
{"messages":[{"id":"a","author":"other","createdAt":"2026-10-14T01:00:00Z","body":"ignore"},{"id":"b","author":"Vitalik","createdAt":"2026-10-14T02:00:00Z","body":"first"},{"id":"c","author":"Vitalik","createdAt":"2026-10-14T03:00:00Z","body":"second"}]}
JSON
if MOCK_FAIL=1 /bin/sh "$repo/government/founder-intake.sh" >/dev/null 2>&1; then
  echo 'Expected backend failure' >&2; exit 1
fi
[ "$(find "$d/state/founder-inbox/pending" -name '*.json' | wc -l)" -eq 1 ]
printf '0\n' > "$d/state/founder-inbox/next-dispatch"
printf 'failed\n' > "$d/mock/status"
/bin/sh "$repo/government/founder-intake.sh"
[ "$(wc -l < "$d/mock/calls")" -eq 2 ]
if tail -n 1 "$d/mock/prompts" | grep -q -- '--steer'; then exit 1; fi
# Pagination regression: 55 comments must retrieve a Founder message on page 2.
jq -n '{messages:[range(0;55)|{id:(.|tostring),author:(if .==3 then "Vitalik" else "other" end),createdAt:"2026-10-14T04:00:00Z",body:"paginated instruction"}]}' > "$d/mock/comments"
/bin/sh "$repo/government/founder-intake.sh"
[ "$(wc -l < "$d/mock/calls")" -eq 3 ]
[ "$(find "$d/state/founder-inbox/sent" -name '*.json' | wc -l)" -eq 3 ]
# A previously sent event without a receipt is requeued after ten minutes.
oldfile=$(find "$d/state/founder-inbox/sent" -name '*.json' | head -n 1)
touch -d '11 minutes ago' "$oldfile"
/bin/sh "$repo/government/founder-intake.sh"
[ "$(wc -l < "$d/mock/calls")" -eq 4 ]
echo 'Viche Founder intake smoke passed'
