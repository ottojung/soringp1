#!/bin/sh
# Never mistake missing data or an empty curator result for research completion.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
script=$repo/government/research-frontier-status.py
SORING_FRONTIER_STATE=$d/missing.json python3 "$script" |
  jq -e '.status=="unavailable" and (.action|contains("do not infer zero work"))' >/dev/null
printf 'not-json\n' > "$d/frontier.json"
SORING_FRONTIER_STATE=$d/frontier.json python3 "$script" |
  jq -e '.status=="unavailable"' >/dev/null
cat > "$d/frontier.json" <<'JSON'
{"version":1,"curator":{"exit_state":"clearexit","added":0,"last_finished_at":1000},
 "fronts":[
 {"id":"first","status":"investigated","finding_unverified":"No new theorem"},
 {"id":"second","status":"blocked","finding_unverified":"No final text; audit needed"}
 ]}
JSON
SORING_FRONTIER_STATE=$d/frontier.json python3 "$script" |
 jq -e '.status=="depleted_after_empty_curation" and .fronts_total==2
        and .counts.investigated==1 and .counts.blocked==1
        and .blocked_without_final_finding==["second"]
        and (.action|contains("NEW research directions"))' >/dev/null
python3 - "$d/frontier.json" <<'PY'
import json,sys
p=sys.argv[1]
d=json.load(open(p));d['fronts'].append({'id':'third','status':'ready'})
open(p,'w').write(json.dumps(d))
PY
SORING_FRONTIER_STATE=$d/frontier.json python3 "$script" |
 jq -e '.status=="fronts_claimed_or_ready_not_verified" and .counts.ready==1' >/dev/null
# This tool is a diagnostic, never an action or a researcher dispatcher.
grep -Fq 'READ-ONLY DIAGNOSTIC' "$repo/government/executive-cycle.sh"
echo 'Viche research frontier exhaustion diagnostic smoke passed'
