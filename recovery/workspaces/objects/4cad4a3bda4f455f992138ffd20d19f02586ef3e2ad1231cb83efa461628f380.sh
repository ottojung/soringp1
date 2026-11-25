#!/bin/sh
set -eu
cd "$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)"
runner=$(pwd -P)/government/knowledge-office-cycle.sh
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/town/government" "$d/town/records/knowledge"
cp government/knowledge-activation-verify.sh "$d/town/government/"
printf '%s\n' '## Act 32 — Institutional Knowledge and Communications Act (enacted 2026-11-19)' \
    > "$d/town/government/LAWS.md"
cat > "$d/town/records/knowledge/activation.json" <<'JSON'
{"schema":"viche-knowledge-activation-v1","offices":{"statistics":{"enabled":false,"authorized_by":"act:32:statistics","not_before":0,"expires_at":4102444800}}}
JSON
now=$(date +%s)
jq --argjson now "$now" '.offices.statistics.not_before=$now-30 | .offices.statistics.expires_at=$now+3600' "$d/town/records/knowledge/activation.json" > "$d/new"
mv "$d/new" "$d/town/records/knowledge/activation.json"
export VICHE_TOWN_ROOT="$d/town" VICHE_STATE_ROOT="$d/state" VICHE_SEATS_ROOT="$d/seats"
# False activation must NOT create an appointment or require Constitution.
VICHE_CONSTITUTION=/no/such/file /bin/sh "$runner" statistics
[ ! -d "$d/seats" ] || { echo "disabled office created seats" >&2; exit 1; }
jq '.offices.statistics.enabled=true' "$d/town/records/knowledge/activation.json" > "$d/new"
mv "$d/new" "$d/town/records/knowledge/activation.json"
# An enabled office with no prelaunch baseline must refuse.
if VICHE_CONSTITUTION=/no/such/file /bin/sh "$runner" statistics > "$d/out" 2>&1; then
    echo "activated without a frozen baseline" >&2; exit 1
fi
grep -q 'frozen prelaunch baseline' "$d/out"
# An activation without a bounded 45-day interval must not dispatch.
jq '.offices.statistics.not_before=0 | .offices.statistics.expires_at=4102444800' "$d/town/records/knowledge/activation.json" > "$d/new"
mv "$d/new" "$d/town/records/knowledge/activation.json"
VICHE_CONSTITUTION=/no/such/file /bin/sh "$runner" statistics
[ ! -d "$d/seats" ] || { echo "oversized office term created seats" >&2; exit 1; }
# Expiry overrides a missing baseline and disables the office.
jq '.offices.statistics.expires_at=1' "$d/town/records/knowledge/activation.json" > "$d/new"
mv "$d/new" "$d/town/records/knowledge/activation.json"
VICHE_CONSTITUTION=/no/such/file /bin/sh "$runner" statistics
[ ! -d "$d/seats" ] || { echo "expired office created seats" >&2; exit 1; }
echo 'knowledge activation requires enactment, explicit office record, baseline and unexpired term'
