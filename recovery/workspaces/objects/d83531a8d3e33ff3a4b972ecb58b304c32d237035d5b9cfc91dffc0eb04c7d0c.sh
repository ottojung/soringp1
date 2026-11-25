#!/bin/sh
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
mkdir -p "$scratch/bin" "$scratch/town/government" "$scratch/town/records/board-trail" "$scratch/state/oversight/random"
cp "$repo/government/board-trail-check.sh" "$scratch/town/government/board-trail-check.sh"
cp "$repo/government/judiciary-measurements.py" "$scratch/town/government/judiciary-measurements.py"
cat > "$scratch/town/records/board-trail/originating.tsv" <<'MAP'
# fixture mapping
100	law-a	1	1000	law
101	law-b	2	1000	law
102	law-c	3	1000	law
103	draft-d	-	0	draft
104	law-e	4	1000	law
105	law-f	5	1000	law
106	law-g	6	1000	law
MAP
cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
case "$1 $2" in
"board show")
    id=; prev=
    for a in "$@"; do [ "$prev" = "--id" ] && id=$a; prev=$a; done
    case "$id" in
    100) printf '%s\n' '{"messages":[{"author":"c","createdAt":"1970-01-01T00:10:00.000Z","body":"ballot yes"},{"author":"c","createdAt":"1970-01-01T00:20:00.000Z","body":"Stage marker: verification. verification:confirmed."}]}' ;;
    101) printf '%s\n' '{"messages":[{"author":"openclaw","createdAt":"1970-01-01T00:20:00.000Z","body":"[scheduler-turn] state: working"}]}' ;;
    102) printf '%s\n' '{"messages":[]}' ;;
    103) printf '%s\n' '{"messages":[{"author":"c1e00011","createdAt":"1970-01-01T00:20:00.000Z","body":"Stage marker: proposal."}]}' ;;
    104) printf '%s\n' '{"messages":[{"author":"agent","createdAt":"1970-01-01T00:20:00.000Z","body":"We must not claim verification:confirmed in this prose sentence."}]}' ;;
    105) printf '%s\n' '{"messages":[{"author":"agent","createdAt":"1970-01-01T00:20:00.000Z","body":"Stage marker: verification. We must not claim verification:confirmed in this prose sentence."}]}' ;;
    106) printf '%s\n' '{"messages":[{"author":"c","createdAt":"1970-01-01T00:20:00.000Z","body":"TERMINAL UPDATE — verification:confirmed (Act 18 §8 reconciliation). Stage marker: verification."}]}' ;;
    *) printf '%s\n' '{"messages":[]}' ;;
    esac ;;
*) echo "unexpected mock call: $*" >&2; exit 90 ;;
esac
MOCK
chmod +x "$scratch/bin/antonina"
PATH=$scratch/bin:$PATH
VICHE_TOWN_ROOT=$scratch/town
VICHE_STATE_ROOT=$scratch/state
VICHE_BRANCH_NOW=2000000000
export PATH VICHE_TOWN_ROOT VICHE_STATE_ROOT VICHE_BRANCH_NOW
sh "$scratch/town/government/board-trail-check.sh" > "$scratch/rows"
[ "$(wc -l < "$scratch/rows")" -eq 7 ]
jq -e 'select(.issue=="100") | .terminal==1 and .stage_markers=="verification" and .post_completion==1 and .chatter==0' "$scratch/rows" >/dev/null
jq -e 'select(.issue=="101") | .terminal==0 and .stage_markers=="" and .chatter==1' "$scratch/rows" >/dev/null
jq -e 'select(.issue=="102") | .post_completion==0 and .terminal==0' "$scratch/rows" >/dev/null
jq -e 'select(.issue=="103") | .stage_markers=="proposal" and .chatter==0' "$scratch/rows" >/dev/null
# Regression (Act 18 §3.3/§3.4): a terminal token in a prose/quoted mention must
# NOT count, even when a stage marker is present; only a DECLARED terminal state
# (declaration position) counts. 104 has no marker, 105 has a marker but prose.
jq -e 'select(.issue=="104") | .terminal==0 and .stage_markers=="" and .post_completion==1' "$scratch/rows" >/dev/null
jq -e 'select(.issue=="105") | .terminal==0 and .stage_markers=="verification" and .post_completion==1' "$scratch/rows" >/dev/null
jq -e 'select(.issue=="106") | .terminal==1 and .stage_markers=="verification" and .post_completion==1' "$scratch/rows" >/dev/null
python3 "$scratch/town/government/judiciary-measurements.py" >/dev/null
report=$scratch/state/branches/judiciary-measurements.json
jq -e '.board_trail.status=="measured"' "$report" >/dev/null
jq -e '.board_trail.completed_total==6 and .board_trail.terminal_reached==2 and .board_trail.fraction_terminal==0.3333' "$report" >/dev/null
jq -e '(.board_trail.git_only_gaps|length)==1 and .board_trail.git_only_gaps[0].issue=="102"' "$report" >/dev/null
jq -e '.board_trail.dangling_trails==4 and .board_trail.content_standard_failures==1' "$report" >/dev/null
jq -e '.no_proposals==true and .measurement_reliability=="not_established"' "$report" >/dev/null
echo 'Board-trail completeness lens smoke passed'
