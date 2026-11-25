#!/bin/sh
# Executive Ministry of Economy under enacted Act 29.
#
# Two independent halves:
#   1. Funding refresh: deterministic, no model call (it probes FREE models only).
#      Keeps the Antonina model list in tier order: free, contributor, paid, Luna.
#      Runs in the background under a lock, every 6h (hourly while funding is
#      at risk), and never blocks any other office.
#   2. The Ministry's agent: researches free models, ranks them within the free
#      tier, finds waste elsewhere in the Town. Dispatched at most every 12h and
#      only when what it reads has changed (dispatch-gate.sh).
set -eu
town=$(printenv VICHE_TOWN_ROOT || printf '%s\n' /var/lib/lubko/wd/viche)
seats=$(printenv VICHE_SEATS_ROOT || printf '%s\n' /var/lib/lubko/wd/viche-seats)
state=$(printenv VICHE_STATE_ROOT || printf '%s\n' /var/lib/lubko/wd/viche-state)
charter=$(printenv VICHE_CONSTITUTION || true)
grep -Eq '^## Act [0-9]+ — Ministry of Economy Act ' "$town/government/LAWS.md" || exit 0
root=$state/executive/economy
econ=$state/economy
cwd=$seats/branches/economy
mkdir -p "$root" "$econ"
now=$(date +%s)

# ---- 1. deterministic funding refresh --------------------------------------
if [ -f "$town/government/economy-models.py" ]; then
  last=0
  [ ! -s "$root/last-refresh" ] || last=$(cat "$root/last-refresh")
  case "$last" in ''|*[!0-9]*) last=0 ;; esac
  interval=21600
  if [ -s "$econ/report.json" ] &&
     [ "$(jq -r '.funding_risk // "unknown"' "$econ/report.json" 2>/dev/null)" != none ]; then
    interval=3600
  fi
  if [ $((now-last)) -ge "$interval" ]; then
    printf '%s\n' "$now" > "$root/last-refresh"
    (
      flock -n 9 || exit 0
      timeout 900 nice python3 "$town/government/economy-models.py" refresh ||
        echo "Viche: economy model refresh failed; model list left as it was" >&2
    ) 9>"$root/refresh.lock" >> "$root/refresh.log" 2>&1 < /dev/null &
  fi
fi

# ---- 1b. deterministic resource steward (disk, inodes, memory, load) ----------
# Measures, forecasts time-to-full and acts early through the Janitor's own
# pipeline; no model call. Every 30 minutes, every 10 while anything is short.
resource_level=ok
if [ -f "$town/government/economy-resources.py" ]; then
  last=0
  [ ! -s "$root/last-resource-refresh" ] || last=$(cat "$root/last-resource-refresh")
  case "$last" in ''|*[!0-9]*) last=0 ;; esac
  interval=1800
  if [ -s "$econ/resources.json" ]; then
    resource_level=$(jq -r '.overall // "ok"' "$econ/resources.json" 2>/dev/null || echo ok)
    case "$resource_level" in short|critical) interval=600 ;; esac
  fi
  if [ $((now-last)) -ge "$interval" ]; then
    printf '%s\n' "$now" > "$root/last-resource-refresh"
    (
      flock -n 8 || exit 0
      timeout 3000 nice python3 "$town/government/economy-resources.py" refresh ||
        echo "Viche: economy resource refresh failed; nothing was changed by it" >&2
    ) 8>"$root/resources.lock" >> "$root/resources.log" 2>&1 < /dev/null &
  fi
fi

# ---- 2. the Ministry's agent -------------------------------------------------
[ -n "$charter" ] && [ -s "$charter" ] || exit 0
[ -f "$town/government/MINISTRY-OF-ECONOMY.md" ] || { echo 'Ministry mandate missing' >&2; exit 1; }
if [ ! -e "$cwd/.git" ]; then
  [ ! -e "$cwd" ] || { echo "Refusing occupied non-Git Ministry workspace" >&2; exit 1; }
  git -C "$town" worktree add --detach "$cwd" HEAD || exit 1
fi
/bin/sh "$town/government/branch-bootstrap.sh" economy > "$root/bootstrap.log" 2>&1 || exit 1
id=$(/bin/sh "$town/government/appointments.sh" ensure economy)
meta=$(antonina agent status --id "$id" --json)
mode=$(printf '%s\n' "$meta" | jq -r '.state // "unknown"')
last=0
[ ! -s "$root/last-dispatch" ] || last=$(cat "$root/last-dispatch")
case "$last" in ''|*[!0-9]*) exit 1 ;; esac
readiness=$mode
case "$mode" in
  running) readiness=running ;;
  idle|clearexit)
    readiness=ready
    agent_interval=43200
    case "$resource_level" in short|critical) agent_interval=7200 ;; esac
    # Public Post content cannot change the Economy office's launch cadence.
    if [ "$last" -eq 0 ] || [ $((now-last)) -ge "$agent_interval" ]; then
      orders='No specific Executive order: keep the Town funded, research the free models, find waste.'
      [ ! -s "$econ/orders.md" ] || orders=$(cat "$econ/orders.md")
      report='{"note":"no funding report yet; the first refresh runs within the hour"}'
      [ ! -s "$econ/report.json" ] || report=$(cat "$econ/report.json")
      resources='{"note":"no resource report yet; the first refresh runs within the hour"}'
      [ ! -s "$econ/resources.json" ] || resources=$(jq -c 'del(.policy)' "$econ/resources.json" 2>/dev/null || cat "$econ/resources.json")
      cases='{"open_cases":[]}'
      [ ! -f "$town/government/institutional-cases.py" ] ||
        cases=$(python3 "$town/government/institutional-cases.py" report) || exit 1
      recovery=$(/bin/sh "$town/government/terminal-continuity.sh" instruction economy) || exit 1
      proceed=
      [ ! -f "$town/government/proceed-by-default.sh" ] ||
        proceed=$(/bin/sh "$town/government/proceed-by-default.sh" brief "$town" economy) || proceed=
      gate=dispatch
      if [ -f "$town/government/dispatch-gate.sh" ]; then
        # Fingerprint only stable inputs: timestamps and probe logs change every refresh.
        if { printf '%s\n%s\n%s\n' "$orders" "$recovery" "$proceed"
             printf '%s\n' "$report" | jq -cS 'del(.at,.backup,.probes_run,.previous_order)' 2>/dev/null || printf '%s\n' "$report"
             # Resources: only the status of each, so a percentage drifting by 0.1 does not wake the agent.
             if [ -s "$econ/resources.json" ]; then
               jq -cS '{overall, s: (.resources | map_values(.status)), needs: .needs_founder}' "$econ/resources.json" 2>/dev/null || :
             fi
             printf '%s\n' "$cases" | jq -cS '[.open_cases[]? | {id,signal,state,owner}]' 2>/dev/null || :
             git -C "$town" rev-parse HEAD; } |
           /bin/sh "$town/government/dispatch-gate.sh" check economy 86400 > "$root/gate.log"; then
          gate=dispatch
        else
          gate=skip
        fi
      fi
      if [ "$gate" = dispatch ]; then
        prompt=$(cat <<EOF
You are the MINISTRY OF ECONOMY, an Executive office (Act 29) reporting to the
Executive coordinator. You are not a fourth branch or a parliamentary voter and
you cannot enact law. Judiciary independently measures results. The Founder
alone originates external productive missions.
=== FOUNDER CONSTITUTION ===
$(cat "$charter")
=== END CONSTITUTION ===
Read your mandate at $town/government/MINISTRY-OF-ECONOMY.md and the CANONICAL
$town/government/LAWS.md (Acts 29 and 30 in particular). Your working files are
in $econ; your worktree is $cwd.
Model order is tiered and enforced by government/economy-models.py: free models
first, then contributor models, then paid models, and Luna models (and every
paid model) at the very bottom. You steer within a tier through
$econ/model-policy.json; you never put a paid model above a free one.
=== EXECUTIVE ORDERS ===
$orders
=== END ORDERS ===
=== LATEST FUNDING REPORT (deterministic, from the last refresh) ===
$report
=== END FUNDING REPORT ===
=== LATEST RESOURCE REPORT (deterministic: disk, inodes, memory, load, Town-owned growth) ===
$resources
=== END RESOURCE REPORT ===
Your mandate is the availability of EVERY scarce resource, not only model funding
(Act 29 section 6). government/economy-resources.py measures and forecasts and has
already run the safe Janitor steps listed under actions_this_pass; you act on what
it cannot: pick quarantine candidates with evidence (Act 12.4), run
government/janitor.sh modes yourself when the report says short or critical, ask
another office for a bounded action through government/proceed-by-default.sh, and
raise anything still short as one line beginning NEEDS-FOUNDER: on Town Hall.
You never touch records/, government/, credentials, live processes or anything
unverified (Act 12.5), and you never delete outside the Janitor's quarantine path.
=== PERSISTENT HEALTH CASES ===
$cases
=== END CASES ===
$recovery
$proceed
EOF
)
        if [ -f "$town/government/post-inbox-brief.sh" ]; then
          post_mail=$(/bin/sh "$town/government/post-inbox-brief.sh" economy) || post_mail='Post preview unavailable'
          prompt=$(printf '%s\n\n%s\n' "$prompt" "$post_mail")
        fi
policy_file="$town/government/AGENT-REPORTING-POLICY.md"
        [ -s "$policy_file" ] || { echo "Viche: mandatory Founder agent policy missing" >&2; exit 1; }
        if [ -f "$town/government/handover.sh" ]; then
          prompt=$(printf '%s\n%s\n' "$prompt" "$(/bin/sh "$town/government/handover.sh" show economy "$id" || :)")
        fi
        prompt=$(printf '%s\n\n%s\n' "$prompt" "$(cat "$policy_file")")
        antonina agent run --id "$id" --cwd "$cwd" --prompt "$prompt" --detach > "$root/dispatch.log" 2>&1 || exit 1
        [ ! -f "$town/government/dispatch-gate.sh" ] || /bin/sh "$town/government/dispatch-gate.sh" commit economy
        printf '%s\n' "$now" > "$root/last-dispatch"
        last=$now
        readiness=dispatched
      else
        readiness=skipped_unchanged
      fi
    fi ;;
  *) echo "Ministry of Economy unhealthy: $mode" >&2; exit 1 ;;
esac
tmp=$(mktemp "$root/health.XXXXXXXX")
jq -n --arg id "$id" --arg mode "$mode" --arg ready "$readiness" \
   --argjson now "$now" --argjson last "$last" \
  '{office:"economy",executive_office:true,legislative_branch:false,
    voting_seat:false,controlled_by:"executive",agent_id:$id,agent_state:$mode,
    readiness:$ready,observed_at:$now,last_dispatch_at:$last,
    quality_verified:false,note:"readiness_not_proof_of_efficiency"}' > "$tmp"
mv -f "$tmp" "$root/health.json"
