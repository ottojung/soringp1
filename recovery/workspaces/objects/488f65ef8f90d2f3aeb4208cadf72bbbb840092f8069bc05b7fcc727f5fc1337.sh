#!/bin/sh
set -eu
root=$(CDPATH= cd "$(dirname "$0")/.." && pwd)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
mkdir -p "$tmp/state/branches" "$tmp/bin"
cat > "$tmp/bin/antonina" <<'EOF'
#!/bin/sh
case "$*" in
  "agent list --finished --page 1 --limit 500 --json")
    printf '%s\n' '{"agents":[{"title":"Viche: Clerk","state":"clearexit","finished_at":1792774800},{"title":"SoringP1 proof attempt","state":"failed","finished_at":1792774800}],"unreadable":[]}' ;;
  "board list --state open --page 1 --json")
    printf '%s\n' '[{"title":"Viche: unfinished mandate"},{"title":"SoringP1: theorem remains open"}]' ;;
  *) echo "unexpected test call: $*" >&2; exit 2 ;;
esac
EOF
chmod +x "$tmp/bin/antonina"
printf '%s\n' '{"branch":"legislature","readiness":"running","observed_at":1792774800}' > "$tmp/state/branches/legislature.json"
printf '%s\n' '{"branch":"executive","readiness":"ready","observed_at":1792774800}' > "$tmp/state/branches/executive.json"
printf '%s\n' '{"branch":"judiciary","readiness":"running","observed_at":1792774800}' > "$tmp/state/branches/judiciary.json"
VICHE_METRICS_NOW=1792774900 VICHE_TOWN_ROOT="$root" \
VICHE_STATE_ROOT="$tmp/state" VICHE_METRICS_ANTONINA="$tmp/bin/antonina" \
python3 "$root/government/outcome-metrics.py" > "$tmp/output"
python3 - "$tmp/state/institutional-outcomes/latest.json" <<'PY'
import json,sys
x=json.load(open(sys.argv[1]))
assert x['agents']['total']==2,x['agents']
assert x['agents']['by_process_outcome']=={'failed':1,'clearexit':1}
assert x['agents']['caveat'].find('NOT prove')>=0
assert x['board']['open_by_project']=={'Viche':1,'SoringP1':1}
assert x['branches']['legislature']['readiness']=='running'
assert x['delivery_verified_by_this_probe'] is False
assert x['no_prescriptive_quota'] is True
PY
# Unavailable agent inventory cannot silently become a green zero.
printf '#!/bin/sh\nexit 1\n' > "$tmp/bin/antonina"
VICHE_METRICS_NOW=1792774961 VICHE_TOWN_ROOT="$root" \
VICHE_STATE_ROOT="$tmp/state" VICHE_METRICS_ANTONINA="$tmp/bin/antonina" \
python3 "$root/government/outcome-metrics.py" > "$tmp/output"
python3 - "$tmp/state/institutional-outcomes/latest.json" <<'PY'
import json,sys
x=json.load(open(sys.argv[1]))
assert x['agents']['telemetry']=='unavailable',x['agents']
assert 'outcome_measurement_incomplete' in x['signals_for_inquiry_not_verdicts']
PY
echo 'Viche outcome feedback smoke passed'
