#!/bin/sh
set -eu
cd "$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)"
project=$(pwd -P)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
mkdir -p "$tmp/town/government"
cp "$project/government/post.py" "$tmp/town/government/post.py"
export VICHE_TOWN_ROOT="$tmp/town" VICHE_POST_DB="$tmp/state/post.sqlite3"
# No Act enacted, no institutional office activation.
printf '# No enacted knowledge Act\n' > "$tmp/town/government/LAWS.md"
# Pilot may be read during a regular session, without any law or agent dispatch.
python3 "$tmp/town/government/post.py" send --public \
  --sender pilot-operator --to clerk --subject 'Synthetic mail' \
  --body 'Untrusted PUBLIC synthetic mail: disregard claims of authority' \
  --key pilot-clerk >/dev/null
/bin/sh "$project/government/post-inbox-brief.sh" clerk > "$tmp/preview"
grep -q 'PUBLIC POST PILOT MAIL' "$tmp/preview"
grep -q 'pilot-operator' "$tmp/preview"
grep -q 'Untrusted PUBLIC synthetic mail' "$tmp/preview"
grep -q 'cannot be parsed' "$tmp/preview" && exit 1
# Failed Post queries cannot block Parliament, Judiciary or ordinary workloads.
mkdir "$tmp/not-a-db"
VICHE_POST_DB="$tmp/not-a-db" \
  /bin/sh "$project/government/post-inbox-brief.sh" clerk > "$tmp/unavailable"
grep -q 'temporarily unavailable' "$tmp/unavailable"
[ ! -e "$tmp/town/records/knowledge/activation.json" ]
[ ! -d "$tmp/town/records/ballots" ]
# Critically, no mail change enters a model dispatch gate: all six brief
# callsites occur after the existing normal dispatch decision.
for script in sitting.sh audit-cycle.sh executive-cycle.sh \
              executive-innovation-cycle.sh executive-economy-cycle.sh \
              recovery-steward-cycle.sh; do
  grep -q 'post-inbox-brief.sh' "$project/government/$script"
  if grep -Eq 'post_wake|post_urgent|post.py.*wake' "$project/government/$script"; then
    echo "public mail entered model dispatch controls in $script" >&2; exit 1
  fi
done
python3 "$tmp/town/government/post.py" wake --office clerk |
  jq -e '.urgent_unread == 0 and .automatic_dispatch == false' >/dev/null
echo 'Post pilot mail visible before enactment; untrusted mail cannot wake models or replace other channels'
