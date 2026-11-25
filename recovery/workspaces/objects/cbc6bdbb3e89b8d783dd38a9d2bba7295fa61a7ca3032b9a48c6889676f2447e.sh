#!/bin/sh
# Act 18 §2/§7 — a transient/persistent board-call failure MUST NOT fabricate a
# Git-only gap. The §7 generator and the §5 lens must retry a transient error and
# record a persistent one as board_readable:false (unreadable), distinct from a
# genuine absence of a terminal update. Hermetic: mock board, scratch town.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
export SCRATCH=$scratch
town=$scratch/town
mkdir -p "$town/government" "$town/records/board-trail" "$scratch/bin" "$scratch/state"
cp "$repo/government/board-trail-index.py" "$town/government/"
cp "$repo/government/board-trail-check.sh" "$town/government/"
cp "$repo/government/judiciary-measurements.py" "$town/government/"

# 400: enacted, board readable, no terminal update -> a GENUINE gap.
# 401: enacted, board persistently unreadable -> must NOT be a gap.
# 402: enacted, board fails once then returns a terminal update -> retried.
cat > "$town/records/board-trail/originating.tsv" <<'MAP'
# fixture mapping
400	genuine-gap	-	1000	law
401	unreadable	-	1000	law
402	transient-then-terminal	-	1000	law
MAP

cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
id=; prev=
for a in "$@"; do [ "$prev" = "--id" ] && id=$a; prev=$a; done
case "$id" in
400) printf '%s\n' '{"title":"gap","messages":[]}' ;;
401) exit 1 ;;
402)
    n=0
    [ -f "$SCRATCH/c402" ] && n=$(cat "$SCRATCH/c402")
    n=$((n + 1))
    printf '%s\n' "$n" > "$SCRATCH/c402"
    if [ "$n" -le 1 ]; then exit 1; fi
    printf '%s\n' '{"title":"retry","messages":[{"author":"c","createdAt":"1970-01-01T00:20:00.000Z","body":"Stage marker: verification. verification:confirmed."}]}' ;;
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

# Genuine gap preserved.
jq -e '.issues[] | select(.issue==400) | .board_readable==true and .git_only_gap==true' "$idx" >/dev/null
# Persistent board failure: unreadable, NOT a fabricated gap.
jq -e '.issues[] | select(.issue==401) | .board_readable==false and .git_only_gap==false and .terminal_status==null' "$idx" >/dev/null
# Transient failure was retried and the true terminal state recovered.
jq -e '.issues[] | select(.issue==402) | .board_readable==true and .terminal_status=="verification:confirmed" and .git_only_gap==false' "$idx" >/dev/null
[ "$(cat "$SCRATCH/c402")" -eq 2 ] # first attempt failed, retry succeeded

# §5 lens: must not abort on the persistent failure; report it as unreadable.
sh "$town/government/board-trail-check.sh" > "$scratch/s5"
jq -e 'select(.issue=="400") | .board_readable==true and .terminal==0' "$scratch/s5" >/dev/null
jq -e 'select(.issue=="401") | .board_readable==false and .terminal==null' "$scratch/s5" >/dev/null
jq -e 'select(.issue=="402") | .board_readable==true and .terminal==1' "$scratch/s5" >/dev/null

# The §5 measurement excludes unreadable issues from the gap/rate computation.
python3 "$town/government/judiciary-measurements.py" >/dev/null
report=$scratch/state/branches/judiciary-measurements.json
jq -e '.board_trail.status=="measured" and .board_trail.completed_total==3 and .board_trail.readable_total==2' "$report" >/dev/null
jq -e '.board_trail.terminal_reached==1 and .board_trail.fraction_terminal==0.5' "$report" >/dev/null
jq -e '(.board_trail.git_only_gaps|length)==1 and .board_trail.git_only_gaps[0].issue=="400"' "$report" >/dev/null
jq -e '(.board_trail.board_unreadable|length)==1 and .board_trail.board_unreadable[0].issue=="401"' "$report" >/dev/null

echo 'Act 18 board-error (no fabricated gap) smoke passed'
