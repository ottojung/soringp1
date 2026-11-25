#!/bin/sh
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
mkdir -p "$scratch/bin" "$scratch/state/oversight" "$scratch/seats/branches/judiciary" "$scratch/town/records"
printf 'charter fixture\n' > "$scratch/charter"
printf 'observation\n' > "$scratch/state/oversight/observations.tsv"
: > "$scratch/town/records/SUMMONED.txt"
cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
case "$1 $2" in
"board list")
  case "$*" in
    *"--state closed"*) echo '[{"number":8,"title":"Claimed completed work"}]' ;;
    *"--page 1"*) echo '[{"number":301,"title":"SoringP1"},{"number":155,"title":"Kawun"},{"number":66,"title":"Other task"},{"number":302,"title":"Town Hall"}]' ;;
    *) echo '[]' ;;
  esac ;;
"board show")
  echo '{"body":"Execution host: billy-dev. Independent task.","messages":[{"author":"Vitalik","body":"Carry out assigned work."}]}' ;;
"agent list")
  echo '{"agents":[{"id":"c1e00008"}],"unreadable":0}' ;;
"agent status")
  echo '{"state":"idle","model":"test-provider/example","variant":"low"}' ;;
"agent new")
  printf "generated-audit-agent-1\n" ;;
"agent run")
  printf 'invoked\n' >> "$DISPATCHES" ;;
*) echo "unexpected mock call: $*" >&2; exit 90 ;;
esac
MOCK
chmod +x "$scratch/bin/antonina"
PATH=$scratch/bin:$PATH
VICHE_STATE_ROOT=$scratch/state
VICHE_TOWN_ROOT=$repo
VICHE_SEATS_ROOT=$scratch/seats
VICHE_CONSTITUTION=$scratch/charter
VICHE_OVERSIGHT_NOW=2000000000
VICHE_AUDIT_EVIDENCE_DEADLINE=7200
DISPATCHES=$scratch/dispatches
export PATH VICHE_STATE_ROOT VICHE_TOWN_ROOT VICHE_SEATS_ROOT VICHE_CONSTITUTION VICHE_OVERSIGHT_NOW VICHE_AUDIT_EVIDENCE_DEADLINE DISPATCHES
python3 "$repo/government/audit-selection.py" > "$scratch/sample"
jq -e '.universe.ignored_work==4 and .universe.claimed_delivery==1 and .universe.government_decision>0 and (.cases|length)==4 and ([.cases[].case_id]|unique|length)==4' "$scratch/sample" > /dev/null
jq -e '([.cases[].population]|sort)==["claimed_delivery","government_decision","ignored_work","ignored_work"]' "$scratch/sample" >/dev/null
# All selections happen from board, independent of executive supplied task claims.
[ "$(find "$scratch/state/oversight/random/cases" -type f | wc -l)" -eq 4 ]
/bin/sh "$repo/government/audit-cycle.sh"
[ "$(wc -l < "$DISPATCHES")" -eq 1 ]
# Both ordinary oversight and randomized findings are linked to evidence.
id=$(jq -r '.cases[0].case_id' "$scratch/sample")
python3 "$repo/government/audit-accountability.py" report --case "$id" --verdict finding --evidence "commit:abc" >/dev/null
python3 "$repo/government/audit-accountability.py" check > "$scratch/check"
jq -e '[.signals[].type]|index("unresolved_finding")' "$scratch/check" >/dev/null
python3 "$repo/government/audit-accountability.py" report --case "$id" --verdict verified_fixed --evidence "commit:def" >/dev/null
python3 "$repo/government/audit-accountability.py" check > "$scratch/check"
jq -e '(.signals|length==0)' "$scratch/check" >/dev/null
VICHE_OVERSIGHT_NOW=2000010000
export VICHE_OVERSIGHT_NOW
python3 "$repo/government/audit-accountability.py" check > "$scratch/check"
jq -e '[.signals[].type]|index("unreported_sample")' "$scratch/check" >/dev/null
[ -s "$scratch/state/oversight/random/incident.json" ]
echo 'Randomized audit selection and accountability smoke passed'
