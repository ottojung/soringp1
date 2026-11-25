#!/bin/sh
# Act 18 (Board Reporting Act) §7 — the board-trail index is GENERATED from the
# curated records/board-trail/originating.tsv mapping (NOT parsed from bill/LAWS
# prose, which mis-maps issues that bills cite as examples) plus the board's
# terminal-update check. Hermetic: mock board, scratch town.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
town=$scratch/town
mkdir -p "$town/government" "$town/records/board-trail" "$town/records/bills" "$scratch/bin"
cp "$repo/government/board-trail-index.py" "$town/government/"
# Hermetic fixture mapping (NOT the live records file): the live
# records/board-trail/originating.tsv changes as new originating issues appear,
# so coupling this test to it makes a legitimate records update break the full
# suite (observed 2026-10-21: adding #313/#314 broke this test on main).
printf 'issue\twork_id\tact\tenacted_epoch\ttype\n' > "$town/records/board-trail/originating.tsv"
printf '303\tjudiciary-independence\t15\t1792241160\tlaw\n' >> "$town/records/board-trail/originating.tsv"
printf '307\tinnovation-centre-act\t14\t1792241160\tlaw\n' >> "$town/records/board-trail/originating.tsv"
printf '308\tepistemic-adversarialism-act\t16\t1792241160\tlaw\n' >> "$town/records/board-trail/originating.tsv"
printf '309\toversized-history\t18\t1792400760\tlaw\n' >> "$town/records/board-trail/originating.tsv"
printf '312\tboard-reporting-act\t18\t1792400760\tlaw\n' >> "$town/records/board-trail/originating.tsv"
printf '310\tdetector-calibration-act\t-\t0\tdraft\n' >> "$town/records/board-trail/originating.tsv"
cp "$repo/government/LAWS.md" "$town/government/"
cp "$repo"/records/bills/judiciary-independence.md "$repo"/records/bills/board-reporting-act.md "$town/records/bills/"

# Mock board: #307's terminal update is on page 3 behind two full pages;
# #312 has a terminal verification update on page 1, and #303 only mentions a
# terminal token as prose.
# #303 carries a stage marker plus a PROSE MENTION of the terminal token: the §7
# declaration-position rule must reject it (regression for the §5/§7 false positive).
cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
case "$1 $2" in
"board show")
  case "$*" in
    *"303"*) printf '{"title":"Three-branch legislation","messages":[{"author":"agent","body":"Stage marker: verification. We must not claim verification:confirmed in this prose sentence."}]}' ;;
    *"307"*"--page 1"*) python3 -c 'import json,sys; json.dump({"title":"Innovation Centre","messages":[{"author":"agent","body":"ordinary comment %d" % i} for i in range(50)]},sys.stdout)' ;;
    *"307"*"--page 2"*) python3 -c 'import json,sys; json.dump({"title":"Innovation Centre","messages":[{"author":"agent","body":"ordinary page-2 comment %d" % i} for i in range(50)]},sys.stdout)' ;;
    *"307"*) printf '{"title":"Innovation Centre","messages":[{"author":"Viche Clerk","body":"TERMINAL UPDATE — verification:confirmed. Stage marker: verification. Evidence: records/bills/innovation-centre-act.md"}]}' ;;
    *"308"*"--page 1"*) python3 -c 'import json,sys; json.dump({"title":"Epistemic Adversarialism","messages":[{"author":"agent","body":"ordinary comment %d" % i} for i in range(50)]},sys.stdout)' ;;
    *"308"*) echo 'mock page 2 unavailable' >&2; exit 90 ;;
    *"309"*) page=1; prev=; for arg do [ "$prev" = "--page" ] && page=$arg; prev=$arg; done; printf '%s\n' "$page" >> "$SCRATCH/309-pages"; python3 -c 'import json,sys; json.dump({"title":"Long history","messages":[{"author":"agent","body":"x"*2048} for _ in range(50)]},sys.stdout)' ;;
    *"310"*) printf '{"title":"Detector Calibration Act","messages":[]}' ;;
    *"312"*) printf '{"title":"Board Reporting Act","messages":[{"author":"c1e00002","body":"Stage marker: verification. Terminal state verification:confirmed. Evidence records/ballots/board-reporting-act.tsv"}]}' ;;
    *) printf '{"title":"unknown","messages":[]}' ;;
  esac ;;
*) echo "unexpected mock: $*" >&2; exit 90 ;;
esac
MOCK
chmod +x "$scratch/bin/antonina"
export SCRATCH=$scratch
PATH="$scratch/bin:$PATH"
VICHE_TOWN_ROOT="$town" VICHE_STATE_ROOT="$scratch/state" VICHE_BOARD_TRAIL_RETRIES=1 python3 "$town/government/board-trail-index.py" >/dev/null

idx="$town/records/board-trail/index.json"
[ -s "$idx" ]

# Mapping comes from originating.tsv, not prose: #303 -> Act 15, #312 -> Act 18.
jq -e '.issues[] | select(.issue==303) | .work | test("Act 15")' "$idx" >/dev/null
jq -e '.issues[] | select(.issue==312) | .work | test("Act 18")' "$idx" >/dev/null
jq -e '.issues[] | select(.issue==308) | .work | test("Act 16")' "$idx" >/dev/null
# #310 is a draft: not enacted, terminal not_enacted, no git_only_gap.
jq -e '.issues[] | select(.issue==310) | .terminal_status=="enactment:not_enacted" and .git_only_gap==false' "$idx" >/dev/null
# Enacted law #303 without a terminal update is a gap; #307's older page-3
# terminal update must still be found after two full pages.
jq -e '.issues[] | select(.issue==303) | .git_only_gap==true and .stage=="enactment"' "$idx" >/dev/null
jq -e '.issues[] | select(.issue==307) | .git_only_gap==false and .terminal_status=="verification:confirmed"' "$idx" >/dev/null
# If any page is unreadable, do not infer a missing terminal update from the
# partial history; the issue is explicitly marked unreadable instead.
jq -e '.issues[] | select(.issue==308) | .board_readable==false and .git_only_gap==false' "$idx" >/dev/null
# A full page 20 is an incomplete scan, not proof of a terminal gap; the index
# generator must stop at the shared bounded history limit and fail closed.
jq -e '.issues[] | select(.issue==309) | .board_readable==false and .git_only_gap==false' "$idx" >/dev/null
[ "$(wc -l < "$scratch/309-pages")" -eq 20 ]
# #312 has a terminal verification update -> not a gap, terminal confirmed.
jq -e '.issues[] | select(.issue==312) | .git_only_gap==false and .terminal_status=="verification:confirmed"' "$idx" >/dev/null
# Owning office: legislative items are Clerk-owned.
jq -e '.issues[] | select(.issue==303) | .owning_office=="Clerk"' "$idx" >/dev/null
# Titles come from the board.
jq -e '.issues[] | select(.issue==303) | .title=="Three-branch legislation"' "$idx" >/dev/null

echo 'Act 18 board-trail index smoke passed'
