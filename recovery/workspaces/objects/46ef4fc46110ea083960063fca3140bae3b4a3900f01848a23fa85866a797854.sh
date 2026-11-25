#!/bin/sh
# Act 18 §5/§7 — the §5 lens (government/board-trail-check.sh) and the §7
# generator (government/board-trail-index.py) MUST classify the same board the
# same way: an originating issue whose work is complete is terminal in BOTH iff
# it carries a DECLARED terminal update. This test pins the terminal rule,
# including the quoted-fixture false positive that made #312 terminal in §5 but
# non-terminal in §7.
#
# Hermetic: mock board, scratch town. Runs both instruments on the SAME board
# and asserts agreement plus per-fixture expectations.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
town=$scratch/town
mkdir -p "$town/government" "$town/records/board-trail" "$scratch/bin" "$scratch/state"
cp "$repo/government/board-trail-check.sh" "$town/government/"
cp "$repo/government/board-trail-index.py" "$town/government/"
cp "$repo/government/judiciary-measurements.py" "$town/government/"

# Fixture issues 200..211 (all enacted laws, epoch 1000) — one row per terminal
# class. Expected terminality is asserted below for BOTH instruments.
cat > "$town/records/board-trail/originating.tsv" <<'MAP'
# fixture mapping
200	genuine-bare	1	1000	law
201	genuine-terminal-prefix	2	1000	law
202	quoted-fixture-backtick	3	1000	law
203	quoted-fixture-doublequote	4	1000	law
204	scheduler-turn	5	1000	law
205	terminal-handoff	6	1000	law
206	progress-checkpoint	7	1000	law
207	mixed-case-tag	8	1000	law
208	prose-no-marker	9	1000	law
209	prose-with-marker	10	1000	law
210	deferred	11	1000	law
211	no-comments	12	1000	law
MAP

cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
case "$1 $2" in
"board show")
    id=; prev=
    for a in "$@"; do [ "$prev" = "--id" ] && id=$a; prev=$a; done
    case "$id" in
    200) printf '%s\n' '{"title":"t200","messages":[{"author":"c","createdAt":"1970-01-01T00:20:00.000Z","body":"Stage marker: verification. verification:confirmed."}]}' ;;
    201) printf '%s\n' '{"title":"t201","messages":[{"author":"c","createdAt":"1970-01-01T00:20:00.000Z","body":"TERMINAL UPDATE — verification:confirmed (Act 18). Stage marker: verification."}]}' ;;
    202) printf '%s\n' '{"title":"t202","messages":[{"author":"agent","createdAt":"1970-01-01T00:20:00.000Z","body":"The fixture `\"Stage marker: verification. verification:confirmed.\"` is quoted in prose here. Stage marker: verification."}]}' ;;
    203) printf '%s\n' '{"title":"t203","messages":[{"author":"agent","createdAt":"1970-01-01T00:20:00.000Z","body":"Quote: \"Stage marker: verification. verification:confirmed.\" end. Stage marker: verification."}]}' ;;
    204) printf '%s\n' '{"title":"t204","messages":[{"author":"openclaw","createdAt":"1970-01-01T00:20:00.000Z","body":"[scheduler-turn]\nStage marker: verification. verification:confirmed."}]}' ;;
    205) printf '%s\n' '{"title":"t205","messages":[{"author":"agent","createdAt":"1970-01-01T00:20:00.000Z","body":"[terminal-handoff]\nStage marker: verification. verification:confirmed."}]}' ;;
    206) printf '%s\n' '{"title":"t206","messages":[{"author":"agent","createdAt":"1970-01-01T00:20:00.000Z","body":"[progress-checkpoint]\nStage marker: verification. verification:confirmed."}]}' ;;
    207) printf '%s\n' '{"title":"t207","messages":[{"author":"openclaw","createdAt":"1970-01-01T00:20:00.000Z","body":"[Scheduler-Turn]\nStage marker: verification. verification:confirmed."}]}' ;;
    208) printf '%s\n' '{"title":"t208","messages":[{"author":"agent","createdAt":"1970-01-01T00:20:00.000Z","body":"We must not claim verification:confirmed in this prose sentence."}]}' ;;
    209) printf '%s\n' '{"title":"t209","messages":[{"author":"agent","createdAt":"1970-01-01T00:20:00.000Z","body":"Stage marker: verification. We must not claim verification:confirmed in this prose sentence."}]}' ;;
    210) printf '%s\n' '{"title":"t210","messages":[{"author":"c","createdAt":"1970-01-01T00:20:00.000Z","body":"Stage marker: verification. status: deferred"}]}' ;;
    211) printf '%s\n' '{"title":"t211","messages":[]}' ;;
    *) printf '%s\n' '{"title":"unknown","messages":[]}' ;;
    esac ;;
*) echo "unexpected mock call: $*" >&2; exit 90 ;;
esac
MOCK
chmod +x "$scratch/bin/antonina"
PATH="$scratch/bin:$PATH"
VICHE_TOWN_ROOT="$town"
VICHE_STATE_ROOT="$scratch/state"
VICHE_BOARD_TRAIL_NOW=2000000000
export PATH VICHE_TOWN_ROOT VICHE_STATE_ROOT VICHE_BOARD_TRAIL_NOW

sh "$town/government/board-trail-check.sh" > "$scratch/s5"
python3 "$town/government/board-trail-index.py" >/dev/null
idx="$town/records/board-trail/index.json"

# expect <issue> <1|0>: assert §5 terminal, §7 terminality, and agreement.
expect() {
    n=$1 want=$2
    got5=$(jq -r --arg n "$n" 'select(.issue==$n) | .terminal' "$scratch/s5")
    got7=$(jq -r --argjson n "$n" '.issues[] | select(.issue==$n) | (.terminal_status!=null)' "$idx")
    if [ "$want" = 1 ]; then w7=true; else w7=false; fi
    [ "$got5" = "$want" ] || { echo "FAIL #$n §5 terminal=$got5 want=$want" >&2; exit 1; }
    [ "$got7" = "$w7" ] || { echo "FAIL #$n §7 terminality=$got7 want=$w7" >&2; exit 1; }
}

# A genuine declaration is terminal in BOTH instruments.
expect 200 1
expect 201 1
# A QUOTED copy of the fixture (backtick+doublequote, or doublequote alone) is
# NOT a declaration: this is the false positive that hid #312's Git-only gap.
expect 202 0
expect 203 0
# Automated scheduler/agent status lines are not updates (Act 18 §3.3.4),
# case-insensitively (fixes the §5 case-sensitivity asymmetry).
expect 204 0
expect 205 0
expect 206 0
expect 207 0
# Bare prose mentions are not declarations.
expect 208 0
expect 209 0
# A declared deferred terminal is terminal in BOTH (agreement on §3.4(4)).
expect 210 1
# No comments: not terminal.
expect 211 0

# §7 reports the specific declared state.
jq -e '.issues[] | select(.issue==200) | .terminal_status=="verification:confirmed"' "$idx" >/dev/null
jq -e '.issues[] | select(.issue==210) | .terminal_status=="deferred"' "$idx" >/dev/null
# §5 and §7 agree issue-by-issue (belt and braces).
for n in 200 201 202 203 204 205 206 207 208 209 210 211; do
    t5=$(jq -r --arg n "$n" 'select(.issue==$n) | .terminal' "$scratch/s5")
    t7=$(jq -r --argjson n "$n" '.issues[] | select(.issue==$n) | if .terminal_status!=null then 1 else 0 end' "$idx")
    [ "$t5" = "$t7" ] || { echo "FAIL #$n §5=$t5 §7=$t7 disagree" >&2; exit 1; }
done

echo 'Act 18 §5/§7 terminal agreement smoke passed'
