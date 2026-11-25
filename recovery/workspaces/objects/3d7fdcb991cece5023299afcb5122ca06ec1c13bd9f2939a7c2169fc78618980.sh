#!/bin/sh
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
mkdir -p "$scratch/branches"
VICHE_STATE_ROOT=$scratch
VICHE_BRANCH_NOW=1000
VICHE_BOARD_TRAIL_CHECKS=0
export VICHE_STATE_ROOT VICHE_BRANCH_NOW VICHE_BOARD_TRAIL_CHECKS
for branch in legislature executive judiciary; do
  printf '{"branch":"%s","observed_at":1000,"readiness":"ready"}\n' "$branch" > "$scratch/branches/$branch.json"
done
# Positive evidence must exist before any green health claim.
mkdir -p "$scratch/institutional-outcomes" "$scratch/institutional-cases"
printf '{"observed_at":1000}\n' > "$scratch/institutional-outcomes/latest.json"
printf '{"observed_at":1000,"count":0}\n' > "$scratch/institutional-cases/index.json"
printf '{"observed_at":1000}\n' > "$scratch/branches/judiciary-measurements.json"
sh "$repo/government/branch-health.sh"
# Mailbox reports must be visible as unresolved health evidence.
mkdir -p "$scratch/oversight/judiciary-mailbox/inbox"
echo "blocked" > "$scratch/oversight/judiciary-mailbox/inbox/test.md"
sh "$repo/government/branch-health.sh" >/dev/null 2>&1 && exit 1
jq -e '.signals|index("judiciary_mailbox_pending")' "$scratch/branches/incident.json" >/dev/null
VICHE_CASE_NOW=1000 python3 "$repo/government/institutional-cases.py" reconcile >/dev/null
jq -e '.owner=="judiciary" and .state=="open"' "$scratch/institutional-cases/judiciary_mailbox_pending.json" >/dev/null
rm "$scratch/oversight/judiciary-mailbox/inbox/test.md"
# A mailbox holding only the reviewer's own disposition is not a pending
# impediment and must not hold the signal red indefinitely.
printf 'resolved\n' > "$scratch/oversight/judiciary-mailbox/inbox/20261109T000000Z-judiciary-disposition-test.md"
sh "$repo/government/branch-health.sh"
[ ! -e "$scratch/branches/incident.json" ]
# An undisposed impediment report still raises the signal.
printf 'blocked\n' > "$scratch/oversight/judiciary-mailbox/inbox/20261109T000001Z-report-test.md"
sh "$repo/government/branch-health.sh" >/dev/null 2>&1 && exit 1
jq -e '.signals|index("judiciary_mailbox_pending")' "$scratch/branches/incident.json" >/dev/null
rm "$scratch/oversight/judiciary-mailbox/inbox/20261109T000000Z-judiciary-disposition-test.md" \
   "$scratch/oversight/judiciary-mailbox/inbox/20261109T000001Z-report-test.md"
sh "$repo/government/branch-health.sh"
# Remove the outcome evidence without changing agent readiness: fail closed.
rm "$scratch/institutional-outcomes/latest.json"
sh "$repo/government/branch-health.sh" >/dev/null 2>&1 && exit 1
jq -e '.signals|index("outcomes_stale")' "$scratch/branches/incident.json" >/dev/null
VICHE_CASE_NOW=1000 python3 "$repo/government/institutional-cases.py" reconcile >/dev/null
jq -e '.count>0' "$scratch/institutional-cases/index.json" >/dev/null
printf '{"observed_at":1000}\n' > "$scratch/institutional-outcomes/latest.json"
sh "$repo/government/branch-health.sh"
[ ! -e "$scratch/branches/incident.json" ]
sed -i s/ready/unhealthy/ "$scratch/branches/judiciary.json"
sh "$repo/government/branch-health.sh" >/dev/null 2>&1 && exit 1
jq -e '.signals|index("judiciary_unhealthy")' "$scratch/branches/incident.json" >/dev/null
[ -s "$scratch/branches/executive.json" ]
sed -i s/unhealthy/ready/ "$scratch/branches/judiciary.json"
sh "$repo/government/branch-health.sh"
[ ! -e "$scratch/branches/incident.json" ]
VICHE_BRANCH_NOW=3001
export VICHE_BRANCH_NOW
sh "$repo/government/branch-health.sh" >/dev/null 2>&1 && exit 1
jq -e '.signals|index("legislature_stale")' "$scratch/branches/incident.json" >/dev/null
python3 "$repo/government/judiciary-measurements.py" >/dev/null
jq -e '.destination=="Legislature" and .no_proposals==true and .false_negative_rate==null' "$scratch/branches/judiciary-measurements.json" >/dev/null
echo 'Three-branch liveness and Judiciary self-measurement smoke passed'
