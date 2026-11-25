#!/bin/sh
# Aggregate objective branch readiness; failure mandates inquiry, not punishment.
set -eu
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
root=$state/branches
mkdir -p "$root"
now=${VICHE_BRANCH_NOW:-$(date +%s)}
max_age=${VICHE_BRANCH_MAX_AGE:-1800}
case "$now:$max_age" in *[!0-9:]*|:*|*:) exit 2;; esac
signals=
for branch in legislature executive judiciary; do
  path=$root/$branch.json
  if [ ! -s "$path" ]; then
    signals="${signals}${signals:+,}${branch}_missing"
    continue
  fi
  valid=$(jq -r --arg b "$branch" 'if .branch==$b and (.observed_at|type=="number") and
    (.readiness=="running" or .readiness=="ready" or .readiness=="unhealthy" or .readiness=="pending")
    then "yes" else "no" end' "$path" 2>/dev/null) || valid=no
  if [ "$valid" != yes ]; then
    signals="${signals}${signals:+,}${branch}_unreadable"
    continue
  fi
  at=$(jq -r '.observed_at' "$path")
  readiness=$(jq -r '.readiness' "$path")
  if [ "$at" -gt "$now" ] || [ $((now-at)) -gt "$max_age" ]; then
    signals="${signals}${signals:+,}${branch}_stale"
  elif [ "$readiness" = unhealthy ]; then
    signals="${signals}${signals:+,}${branch}_unhealthy"
  fi
done
# Mandatory legislative sub-institution. It is not a fourth government branch.
if [ -f "$state/inaugurated" ]; then
  innovation=$state/legislature/innovation-centre/health.json
  mode=legislative
  town=$(printenv VICHE_TOWN_ROOT || printf '%s\n' /var/lib/lubko/wd/viche)
  if grep -Eq '^## Act [0-9]+ — Executive Innovation Office Act \(enacted ' "$town/government/LAWS.md"; then
    innovation=$state/executive/innovation-office/health.json
    mode=executive
  fi
  if [ ! -s "$innovation" ]; then
    signals="${signals}${signals:+,}innovation_missing"
  else
    valid=$(jq -r --arg mode "$mode" '
      if .office=="innovation-centre" and .voting_seat==false and
         (($mode=="executive" and .executive_office==true and .legislative_branch==false and .controlled_by=="executive")
           or ($mode=="legislative" and .legislative_branch==true and .separate_summons==true)) and
         (.observed_at|type=="number") and (.last_dispatch_at|type=="number") and
         (.readiness=="running" or .readiness=="ready" or .readiness=="dispatched")
      then "yes" else "no" end' "$innovation" 2>/dev/null) || valid=no
    if [ "$valid" != yes ]; then
      signals="${signals}${signals:+,}innovation_unhealthy"
    else
      observed=$(jq -r '.observed_at' "$innovation")
      last=$(jq -r '.last_dispatch_at' "$innovation")
      mode=$(jq -r '.readiness' "$innovation")
      if [ "$observed" -gt "$now" ] || [ $((now-observed)) -gt "$max_age" ]; then
        signals="${signals}${signals:+,}innovation_stale"
      elif [ "$last" -eq 0 ] ||
        { [ "$mode" = ready ] && [ $((now-last)) -gt 28800 ]; }; then
        signals="${signals}${signals:+,}innovation_not_dispatched"
      fi
    fi
  fi
fi
# Monitoring is itself a fallible dependency: lack of positive evidence
# is evidence against declaring this town healthy.
evidence_age=${VICHE_EVIDENCE_MAX_AGE:-1200}
case "$evidence_age" in ''|*[!0-9]*) exit 2;; esac
fresh_evidence() {
  [ -s "$1" ] || return 1
  at=$(jq -er '.observed_at | select(type=="number" and .>=0)' "$1" 2>/dev/null) || return 1
  case "$at" in ''|*[!0-9]*) return 1;; esac
  [ "$at" -le "$now" ] && [ $((now-at)) -le "$evidence_age" ]
}
if ! command -v python3 >/dev/null 2>&1 ||
   ! python3 -c 'import json, pathlib' >/dev/null 2>&1; then
  signals="${signals}${signals:+,}python_runtime_unhealthy"
fi
for observation in "outcomes:$state/institutional-outcomes/latest.json" "institutional_cases:$state/institutional-cases/index.json" "judiciary_measurements:$state/branches/judiciary-measurements.json"; do
  evidence_name=${observation%%:*}
  evidence_path=${observation#*:}
  if ! fresh_evidence "$evidence_path"; then
    signals="${signals}${signals:+,}${evidence_name}_stale"
  fi
done
# Unreviewed agent impediments are unresolved adverse evidence.
mailbox_dir="$state/oversight/judiciary-mailbox/inbox"
if [ -d "$mailbox_dir" ] &&
   [ -n "$(find "$mailbox_dir" -maxdepth 1 -type f -name '*.md' -print -quit 2>/dev/null)" ]; then
  signals="${signals}${signals:+,}judiciary_mailbox_pending"
fi
printf '%s\t%s\n' "$now" "${signals:-clear}" >> "$root/observations.tsv"
if [ -z "$signals" ]; then
  if [ -s "$root/incident.json" ]; then
    jq -c --argjson at "$now" '. + {cleared_at:$at,closure:"readiness_restored_not_delivery_verified"}' \
      "$root/incident.json" >> "$root/history.jsonl"
    rm -f "$root/incident.json"
  fi
  exit 0
fi
tmp=$(mktemp "$root/incident.XXXXXXXX")
jq -n --argjson at "$now" --arg s "$signals" \
  '{observed_at:$at,signals:($s|split(",")),
    assessment:"mandatory_branch_inquiry_not_proof_of_misconduct",
    caveat:"running_agent_not_proof_of_useful_work"}' > "$tmp"
mv -f "$tmp" "$root/incident.json"
echo "Viche: branch health inquiry: $signals" >&2
exit 1
