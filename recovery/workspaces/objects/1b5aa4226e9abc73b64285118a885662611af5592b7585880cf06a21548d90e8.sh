#!/bin/sh
# Act 18 §5/§7 — an originating issue with an OPAQUE-STRING Antonina id must be
# included and classified by the board-trail index/lens, not silently skipped
# (the numeric-only parser dropped e.g. ErkrX8EKQJXF6fCQv5fzYl-cannon). Also
# pins the deterministic order: numeric ids ascending, then opaque ids lexically.
# Hermetic: mock board, scratch town.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
town=$scratch/town
mkdir -p "$town/government" "$town/records/board-trail" "$scratch/bin" "$scratch/state"
cp "$repo/government/board-trail-index.py" "$town/government/"
cp "$repo/government/board-trail-check.sh" "$town/government/"
cp "$repo/government/judiciary-measurements.py" "$town/government/"

cat > "$town/records/board-trail/originating.tsv" <<'MAP'
# fixture mapping (numeric then opaque)
400	numeric-law	-	1000	law
ErkrX8EKQJXF6fCQv5fzYl-cannon	opaque-law	-	1000	law
MAP

cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
id=; prev=
for a in "$@"; do [ "$prev" = "--id" ] && id=$a; prev=$a; done
case "$id" in
400) printf '%s\n' '{"title":"numeric","messages":[]}' ;;
ErkrX8EKQJXF6fCQv5fzYl-cannon) printf '%s\n' '{"title":"opaque","messages":[{"author":"c","createdAt":"1970-01-01T00:20:00.000Z","body":"Stage marker: verification. verification:confirmed."}]}' ;;
*) printf '%s\n' '{"title":"unknown","messages":[]}' ;;
esac
MOCK
chmod +x "$scratch/bin/antonina"

PATH="$scratch/bin:$PATH"
VICHE_TOWN_ROOT=$town
VICHE_STATE_ROOT=$scratch/state
VICHE_BOARD_TRAIL_RETRIES=3
VICHE_BOARD_TRAIL_BACKOFF=0
VICHE_BRANCH_NOW=2000000000
export PATH VICHE_TOWN_ROOT VICHE_STATE_ROOT VICHE_BOARD_TRAIL_RETRIES
export VICHE_BOARD_TRAIL_BACKOFF VICHE_BRANCH_NOW

python3 "$town/government/board-trail-index.py" >/dev/null
idx="$town/records/board-trail/index.json"

# The opaque id is present (not skipped), classified, and terminal.
jq -e '.issues | length == 2' "$idx" >/dev/null
jq -e '.issues[] | select(.issue=="ErkrX8EKQJXF6fCQv5fzYl-cannon")
       | .board_readable==true and .terminal_status=="verification:confirmed" and .git_only_gap==false' "$idx" >/dev/null
jq -e '.issues[] | select(.issue=="ErkrX8EKQJXF6fCQv5fzYl-cannon") | .work | test("opaque-law")' "$idx" >/dev/null
# Numeric row is unchanged: still a number, and a genuine gap.
jq -e '.issues[] | select(.issue==400) | .board_readable==true and .git_only_gap==true' "$idx" >/dev/null
# Deterministic order: numeric ascending first, then opaque lexically.
jq -e '.issues[0].issue==400 and .issues[1].issue=="ErkrX8EKQJXF6fCQv5fzYl-cannon"' "$idx" >/dev/null

# §5 lens includes the opaque id too.
sh "$town/government/board-trail-check.sh" > "$scratch/s5"
jq -e 'select(.issue=="ErkrX8EKQJXF6fCQv5fzYl-cannon") | .terminal==1 and .board_readable==true' "$scratch/s5" >/dev/null
jq -e 'select(.issue=="400") | .terminal==0' "$scratch/s5" >/dev/null

# The §5 measurement counts the opaque issue in its universe.
python3 "$town/government/judiciary-measurements.py" >/dev/null
report=$scratch/state/branches/judiciary-measurements.json
jq -e '.board_trail.completed_total==2 and .board_trail.readable_total==2 and .board_trail.terminal_reached==1 and .board_trail.fraction_terminal==0.5' "$report" >/dev/null
jq -e '(.board_trail.git_only_gaps|length)==1 and .board_trail.git_only_gaps[0].issue=="400"' "$report" >/dev/null

echo 'Act 18 opaque-id board-trail smoke passed'
