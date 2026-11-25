#!/bin/sh
# Act 18 §5/§7 — bounded pagination fails closed at the shared page cap, and
# long page histories are aggregated without passing large JSON arrays in argv.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
town=$scratch/town
mkdir -p "$town/government" "$town/records/board-trail" "$scratch/bin" "$scratch/state"
cp "$repo/government/board-trail-index.py" "$repo/government/board-trail-check.sh" "$town/government/"
printf 'issue\twork_id\tact\tenacted_epoch\ttype\n999\tlong-history\t18\t1000\tlaw\n' > "$town/records/board-trail/originating.tsv"
cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
id= page=1 prev=
for arg do
    [ "$prev" = "--id" ] && id=$arg
    [ "$prev" = "--page" ] && page=$arg
    prev=$arg
done
[ "$id" = 999 ] || exit 90
printf '%s\n' "$page" >> "$SCRATCH/pages"
python3 -c 'import json,sys; json.dump({"title":"Long history","messages":[{"author":"agent","createdAt":"2026-10-27T00:00:00Z","body":"x"*2048} for _ in range(50)]},sys.stdout)'
MOCK
chmod +x "$scratch/bin/antonina"
export SCRATCH=$scratch PATH="$scratch/bin:$PATH" VICHE_TOWN_ROOT=$town VICHE_STATE_ROOT=$scratch/state VICHE_BOARD_TRAIL_RETRIES=1

python3 "$town/government/board-trail-index.py" >/dev/null
jq -e '.issues[] | select(.issue==999) | .board_readable==false and .git_only_gap==false' "$town/records/board-trail/index.json" >/dev/null
[ "$(wc -l < "$scratch/pages")" -eq 20 ]

: > "$scratch/pages"
sh "$town/government/board-trail-check.sh" > "$scratch/check.jsonl"
jq -e 'select(.issue=="999") | .board_readable==false and .terminal==null and .comments_total==null' "$scratch/check.jsonl" >/dev/null
[ "$(wc -l < "$scratch/pages")" -eq 20 ]
[ "$(wc -l < "$scratch/check.jsonl")" -eq 1 ] # mapping header is not an originating issue
echo 'Act 18 board pagination cap and large-history smoke passed'
