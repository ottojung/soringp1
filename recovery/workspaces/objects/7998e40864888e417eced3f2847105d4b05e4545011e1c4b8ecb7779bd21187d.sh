#!/bin/sh
# Prospective Executive-controlled innovation office; dormant until lawful enactment.
set -eu
town=$(printenv VICHE_TOWN_ROOT || printf '%s\n' /var/lib/lubko/wd/viche)
seats=$(printenv VICHE_SEATS_ROOT || printf '%s\n' /var/lib/lubko/wd/viche-seats)
state=$(printenv VICHE_STATE_ROOT || printf '%s\n' /var/lib/lubko/wd/viche-state)
charter=$(printenv VICHE_CONSTITUTION)
grep -Eq '^## Act [0-9]+ — Executive Innovation Office Act \(enacted ' "$town/government/LAWS.md" || {
  echo 'Executive innovation requires enacted ordinary law' >&2; exit 1;
}
root=$state/executive/innovation-office
cwd=$seats/branches/innovation-centre
mkdir -p "$root"
/bin/sh "$town/government/branch-bootstrap.sh" innovation-centre > "$root/bootstrap.log" 2>&1 || exit 1
id=$(/bin/sh "$town/government/appointments.sh" ensure innovation-centre)
meta=$(antonina agent status --id "$id" --json)
mode=$(printf '%s\n' "$meta" | jq -r '.state // "unknown"')
now=$(date +%s)
last=0
[ ! -s "$root/last-dispatch" ] || last=$(cat "$root/last-dispatch")
case "$last" in ''|*[!0-9]*) exit 1;; esac
case "$mode" in
  running) readiness=running;;
  idle|clearexit)
    readiness=ready
    if [ "$last" -eq 0 ] || [ $((now-last)) -ge 21600 ]; then
      orders='No specific Executive order: research high-return Viche improvements.'
      [ ! -s "$root/orders.md" ] || orders=$(cat "$root/orders.md")
      cases='{"open_cases":[]}'
      [ ! -f "$town/government/institutional-cases.py" ] ||
        cases=$(python3 "$town/government/institutional-cases.py" report) || exit 1
      recovery=$(/bin/sh "$town/government/terminal-continuity.sh" instruction innovation-centre) || exit 1
      prompt=$(cat <<EOF
You are the EXECUTIVE INNOVATION OFFICE, not a Legislative research officer.
You report to the Executive coordinator and work on useful improvements to
Viche as an ordinary operational unit. You are not a fourth branch or a
parliamentary voter. Parliament exclusively proposes and enacts laws;
you may provide evidence, comparisons, and recommendations for consideration,
but must not yourself enact law or deploy unauthorized changes.
Judiciary independently measures results. The Founder alone originates
external productive missions: invent no new external project.
=== FOUNDER CONSTITUTION ===
$(cat "$charter")
=== END CONSTITUTION ===
Read current government/LAWS.md, government/BRANCHES.md and
government/EXECUTIVE-INNOVATION.md. Preserve all earlier Centre research,
Git worktrees, evidence, and rejected ideas. Prioritize high marginal benefit
relative to total cost, uncertainty, risks and opportunity costs.
Compare existing Free Software before proposing new subsystems.
=== EXECUTIVE ORDERS ===
$orders
=== END ORDERS ===
=== PERSISTENT HEALTH CASES ===
$cases
=== END CASES ===
$recovery
EOF
)
policy_file="$town/government/AGENT-REPORTING-POLICY.md"
[ -s "$policy_file" ] || { echo "Viche: mandatory Founder agent policy missing" >&2; exit 1; }
prompt=$(printf '%s\n\n%s\n' "$prompt" "$(cat "$policy_file")")
      antonina agent run --id "$id" --cwd "$cwd" --prompt "$prompt" --detach > "$root/dispatch.log" 2>&1 || exit 1
      printf '%s\n' "$now" > "$root/last-dispatch"
      last=$now
      readiness=dispatched
    fi ;;
  *) echo "Executive innovation unhealthy: $mode" >&2; exit 1;;
esac
tmp=$(mktemp "$root/health.XXXXXXXX")
jq -n --arg id "$id" --arg mode "$mode" --arg ready "$readiness" \
   --argjson now "$now" --argjson last "$last" \
  '{office:"innovation-centre",executive_office:true,legislative_branch:false,
    voting_seat:false,controlled_by:"executive",agent_id:$id,agent_state:$mode,
    readiness:$ready,observed_at:$now,last_dispatch_at:$last,
    quality_verified:false,note:"readiness_not_proof_of_innovation"}' > "$tmp"
mv -f "$tmp" "$root/health.json"
