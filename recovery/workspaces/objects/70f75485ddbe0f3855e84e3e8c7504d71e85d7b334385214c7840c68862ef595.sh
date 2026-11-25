#!/bin/sh
# Executive-controlled innovation office under enacted Act 25.
set -eu
town=$(printenv VICHE_TOWN_ROOT || printf '%s\n' /var/lib/lubko/wd/viche)
seats=$(printenv VICHE_SEATS_ROOT || printf '%s\n' /var/lib/lubko/wd/viche-seats)
state=$(printenv VICHE_STATE_ROOT || printf '%s\n' /var/lib/lubko/wd/viche-state)
charter=$(printenv VICHE_CONSTITUTION)
grep -Eq '^## Act [0-9]+ — Executive Innovation Office Act \((re-)?enacted ' "$town/government/LAWS.md" || {
  echo 'Executive innovation requires enacted ordinary law' >&2; exit 1;
}
root=$state/executive/innovation-office
# Keep the predecessor's dirty historical worktree intact. Dispatch new
# Executive work in its own clean, Git-managed worktree.
cwd=$seats/branches/innovation-office
mkdir -p "$root"
# Create the active Executive worktree BEFORE bootstrap. Bootstrap, appointment
# resolution and terminal recovery all redirect the innovation-centre key to
# this worktree only once it exists; creating it first prevents the first
# post-enactment run from recovering or syncing against the historical
# legislative worktree.
if [ ! -e "$cwd/.git" ]; then
  [ ! -e "$cwd" ] || { echo "Refusing occupied non-Git Innovation Office workspace" >&2; exit 1; }
  git -C "$town" worktree add --detach "$cwd" HEAD || exit 1
fi
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
    # Public Post content must never preempt this office's normal cadence.
    if [ "$last" -eq 0 ] || [ $((now-last)) -ge 21600 ]; then
      orders='No specific Executive order: proactively investigate system-wide efficiency AND reliability, current problems AND unrealized opportunities; bring research-backed reform ideas through the legislative dialogue under Act 25.'
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
Read the CANONICAL $town/government/LAWS.md,
$town/government/BRANCHES.md and
$town/government/EXECUTIVE-INNOVATION.md (not stale local copies). Preserve all earlier Centre research,
Git worktrees, evidence, and rejected ideas. Prioritize high marginal benefit
relative to total cost, uncertainty, risks and opportunity costs.
Compare existing Free Software before proposing new subsystems.
Do not stop with a status memo. Pursue substantive research and informal
institutional reform ideas even without a specific Executive order. Propose
ideas to the Legislature through ongoing dialogue; do NOT originate or sponsor
formal bills, decide compliance cases, or implement unauthorized solutions.
Small reversible experiments may test hypotheses, but engineering fixes are
not the Office's primary deliverable. Evaluate actual outcomes and opportunity
costs rather than counting reports, prototypes or agents. Preserve the
predecessor worktree.
=== EXECUTIVE ORDERS ===
$orders
=== END ORDERS ===
=== PERSISTENT HEALTH CASES ===
$cases
=== END CASES ===
$recovery
EOF
)
dialogue_file="$town/government/INNOVATION-LEGISLATURE-DIALOGUE.md"
# The legacy dialogue is kept through any new Act until a separately
# accepted and reviewed cutover. Public Post is an additive pilot only.
if [ -s "$dialogue_file" ]; then
    prompt=$(printf '%s\n\n=== CONTINUOUS IMPROVEMENT AND LEGISLATIVE RESEARCH DIALOGUE ===\n%s\n=== END RESEARCH DIALOGUE ===\n' "$prompt" "$(cat "$dialogue_file")")
fi
# The pilot does not replace the working Innovation-Legislature dialogue.
if [ -f "$town/government/post-inbox-brief.sh" ]; then
    post_mail=$(/bin/sh "$town/government/post-inbox-brief.sh" innovation-centre) || post_mail='Post preview unavailable'
    prompt=$(printf '%s\n\n%s\n' "$prompt" "$post_mail")
fi
policy_file="$town/government/AGENT-REPORTING-POLICY.md"
[ -s "$policy_file" ] || { echo "Viche: mandatory Founder agent policy missing" >&2; exit 1; }
if [ -f "$town/government/handover.sh" ]; then
  prompt=$(printf '%s\n%s\n' "$prompt" "$(/bin/sh "$town/government/handover.sh" show innovation-centre "$id" || :)")
fi
prompt=$(printf '%s\n\n%s\n' "$prompt" "$(cat "$policy_file")")
      # Unchanged urgent mail can remain unread; do not repeat the same prompt.
      if [ -f "$town/government/dispatch-gate.sh" ]; then
        if ! { printf '%s\n' "$orders" "$recovery"; } |
            /bin/sh "$town/government/dispatch-gate.sh" check innovation-centre 21600 > "$root/gate.log"; then
          exit 0
        fi
      fi
      antonina agent run --id "$id" --cwd "$cwd" --prompt "$prompt" --detach > "$root/dispatch.log" 2>&1 || exit 1
      [ ! -f "$town/government/dispatch-gate.sh" ] ||
          /bin/sh "$town/government/dispatch-gate.sh" commit innovation-centre
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
