#!/bin/sh
# A frozen sampled cohort, not each incident dispatch, is one correction cycle.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/town/government" "$d/state/oversight/random" "$d/seats/branches/judiciary" "$d/bin"
cp "$repo/government/audit-cycle.sh" "$d/town/government/audit-cycle.sh"
cp "$repo/government/AGENT-REPORTING-POLICY.md" "$d/town/government/AGENT-REPORTING-POLICY.md"
printf 'Charter\n' > "$d/charter"
printf 'observation\n' > "$d/state/oversight/observations.tsv"
printf 'incident\n' > "$d/state/oversight/incident.json"
cat > "$d/town/government/appointments.sh" <<'APPOINT'
#!/bin/sh
printf 'judicial-fixture-agent\n'
APPOINT
cat > "$d/town/government/audit-selection.py" <<'SAMPLE'
import json,os,pathlib
now=int(os.environ['VICHE_OVERSIGHT_NOW'])
r=pathlib.Path(os.environ['VICHE_STATE_ROOT'])/'oversight/random'
v={'at':now,'seed_after_snapshot':'b'*64,
   'cases':[{'case_id':'0123456789abcdef01'}]}
(r/'latest.json').write_text(json.dumps(v)+'\n')
print(json.dumps(v))
SAMPLE
cat > "$d/bin/antonina" <<'ANTONINA'
#!/bin/sh
case "$1 $2" in
 'agent status') printf '{"state":"idle"}\n' ;;
 'agent run')
    root=$VICHE_STATE_ROOT/oversight
    [ -s "$root/current-audit-cycle" ] || exit 3
    token=$(cat "$root/current-audit-cycle")
    awk -F '\t' -v t="$token" '$2==t{found++} END{exit found!=1}' \
      "$root/audit-cycle-identities.tsv" || exit 4
    printf '%s\n' "$token" >> "$MOCK_RUNS"
    [ "${MOCK_FAIL_RUN:-no}" != yes ] ;;
 *) echo "Unexpected Antonina: $*" >&2; exit 2 ;;
esac
ANTONINA
chmod +x "$d/town/government/appointments.sh" "$d/bin/antonina"
base=2000000000
python3 - "$d/state/oversight/random/latest.json" "$base" <<'PY'
import json,sys
open(sys.argv[1],'w').write(json.dumps({'at':int(sys.argv[2]),
 'seed_after_snapshot':'a'*64,'cases':[{'case_id':'0123456789abcdef01'}]})+'\n')
PY
export VICHE_STATE_ROOT="$d/state" VICHE_TOWN_ROOT="$d/town" \
 VICHE_SEATS_ROOT="$d/seats" VICHE_CONSTITUTION="$d/charter" \
 VICHE_OVERSIGHT_NOW="$base" VICHE_AUDIT_CHECKS=0 VICHE_AUDIT_SELECTION=1 \
 MOCK_RUNS="$d/runs" PATH="$d/bin:$PATH"
run() { /bin/sh "$d/town/government/audit-cycle.sh"; }
run
first=$(cat "$d/state/oversight/current-audit-cycle")
[ "${#first}" -eq 32 ]
[ "$(wc -l < "$d/state/oversight/audit-cycle-identities.tsv")" -eq 1 ]
[ "$(wc -l < "$MOCK_RUNS")" -eq 1 ]

# The incident-driven 30min dispatch retains the same frozen sample.
VICHE_OVERSIGHT_NOW=$((base+1801));export VICHE_OVERSIGHT_NOW
run
second=$(cat "$d/state/oversight/current-audit-cycle")
[ "$second" = "$first" ] || { echo 'Duplicate cycle for frozen batch' >&2; exit 1; }
[ "$(wc -l < "$d/state/oversight/audit-cycle-identities.tsv")" -eq 1 ]
[ "$(wc -l < "$MOCK_RUNS")" -eq 2 ]

# A fresh sample after six hours opens a new legally distinguishable cycle.
VICHE_OVERSIGHT_NOW=$((base+21601));export VICHE_OVERSIGHT_NOW
run
third=$(cat "$d/state/oversight/current-audit-cycle")
[ "$third" != "$first" ] || exit 1
[ "$(wc -l < "$d/state/oversight/audit-cycle-identities.tsv")" -eq 2 ]
[ "$(wc -l < "$MOCK_RUNS")" -eq 3 ]

# Ambiguous detached launch must have durable token before it starts and
# cannot cause an immediate duplicate dispatch on retry.
VICHE_OVERSIGHT_NOW=$((base+43202));export VICHE_OVERSIGHT_NOW
if MOCK_FAIL_RUN=yes run >/dev/null 2>&1; then
 echo 'Ambiguous launch unexpectedly succeeded' >&2; exit 1
fi
fourth=$(cat "$d/state/oversight/current-audit-cycle")
[ "$fourth" != "$third" ] || exit 1
[ "$(wc -l < "$d/state/oversight/audit-cycle-identities.tsv")" -eq 3 ]
before=$(wc -l < "$MOCK_RUNS")
run
[ "$(wc -l < "$MOCK_RUNS")" -eq "$before" ] ||
 { echo 'Immediate duplicate after ambiguous launch' >&2; exit 1; }
echo 'Act17 frozen-sample identity and pre-launch durability passed'
