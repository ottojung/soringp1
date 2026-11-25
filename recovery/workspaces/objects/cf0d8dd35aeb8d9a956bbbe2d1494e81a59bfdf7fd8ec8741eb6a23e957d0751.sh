#!/bin/sh
# Continuously reconcile executive delivery without parliamentary summons.
# Called by ordinary government boot; does not modify protected constitution.
set -eu
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
seats=${VICHE_SEATS_ROOT:-/var/lib/lubko/wd/viche-seats}
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
charter=${VICHE_CONSTITUTION:?founder-owned charter required}
[ -f "$state/inaugurated" ] || exit 0
# Act 22 §3.3: regenerate the derived calibration report on every active
# Executive cycle. A malformed ledger is an operational failure, not a quiet
# successful cycle with stale or missing metrics.
python3 "$town/government/predict-scorer.py" || {
  echo "Viche: Act 22 calibration regeneration failed" >&2
  exit 1
}
id=$(/bin/sh "$town/government/appointments.sh" ensure executive)
[ -n "$id" ] || { echo "Viche: missing executive seat" >&2; exit 1; }
if [ -s "$state/liveness/unsafe-holds/executive" ]; then
  echo "Viche: unsafe Executive failed invocation is on durable hold" >&2
  exit 1
fi
# Act 19 §3.2: the durable handoff queue at $town/records/handoffs/ is the
# dispatch's single input. Read it FIRST, before any failure-prone work
# (board fetch, agent status). If the script fails before this read, no
# dispatch occurs at all — the agent is never re-dispatched generically from
# a pre-read failure; the open handoff remains and the next successful run
# honours it.
handoffs=$(/bin/sh "$town/government/handoff-queue.sh" list-open "$town") || exit 1
status=$(antonina agent status --id "$id" --json)
current=$(printf "%s\n" "$status" | jq -r ".state")
case "$current" in
  running) exit 0 ;;
  failed)
    retry_safe=$(printf '%s\n' "$status" | jq -r 'if .backend_error.automatic_retry_safe == true and .backend_error.transient == true then "yes" else "no" end')
    [ "$retry_safe" = yes ] || { echo "Viche: failed Executive not provably retry-safe" >&2; exit 1; }
    ;;
  idle|clearexit) : ;;
  *) echo "Viche: unexpected executive state $current" >&2; exit 1 ;;
esac
cwd=$seats/branches/executive
[ -d "$cwd" ] && [ -s "$charter" ] || exit 1
if [ -n "$handoffs" ]; then
  # Act 19 §3.2.3: while any open handoff exists the generic eligible-issue
  # prompt MUST NOT run; the dispatch carries the open handoffs only.
  prompt=$(cat <<EOF
You are Viche executive liaison. This is independent executive delivery,
NOT a parliamentary sitting. Do not do the parliamentary Clerk work.
=== AUTHORITATIVE CONSTITUTION ===
$(cat "$charter")
=== END AUTHORITATIVE CONSTITUTION ===
Follow current Founder mandates and current ordinary laws. Report contradictory older law rather than treating an unenacted bill as law.
Before interacting with Antonina board or agents, read $town/government/antonina-interface.md. Use the documented commands and JSON shapes; consult command-specific --help when uncertain. Treat parser failures as errors, never as empty work or zero comments.
Standing Founder priority: Continue SoringP1 until the final theorems for S(n)/SORT-BOUND-U are rigorously proved and independently checked and all authorized SoringP1 obligations are truly closed. At every pass inspect #301, SoringP1 main, current AGENTS.md, docs/research-plan.md, open issues, existing researchers and unresolved proof obligations. If every packet was consumed but theorems are still open, identify new independent, falsifiable mathematical fronts from literature and research failures, and dispatch useful researchers without a numeric cap. Do not produce filler, repeat completed work, demand Founder input for routine research direction, or interpret an agent exit as theorem completion. Research takes priority over monitoring and premature Lean formalization.
Follow the standing operational agenda at $town/government/executive-agenda.md, including continuous SoringP1 research-pool maintenance; unrelated one-off handoffs do not suspend this duty.
Act 19 §3.2: the following OPEN DURABLE HANDOFFS at $town/records/handoffs/ govern this dispatch. Do NOT run the generic eligible-issue cycle while any open handoff exists; act on each open handoff now, then mark it done (with an evidence link) or superseded (by a newer handoff) in the queue:
$handoffs
A billy-dev assignment governs WHERE agents execute and keep worktrees, NOT ordinary GitHub infrastructure: GitHub Actions CI/tests/builds/Lean verification on GitHub-hosted runners is expressly authorized and must stay enabled for any repo (incl. SoringP1). Never delete or disable working workflows merely because an issue is assigned to billy-dev. Require verified passing CI when applicable (a green run, not a claim).
Maintain durable issue ownership, dependencies, completed work and blockers.
Verify current issue comments, agents and PRs before assigning; avoid duplicates.
Prioritize tested merged deliverables, not ceremonial discussion or agent counts.
Parallelize constructive independent work without numerical worker limits.
Use Antonina-managed agents, leaving model selection to Antonina.
Your worktree is $cwd.
EOF
)
else
  eligible=$(python3 "$town/government/eligible-work.py") || exit 1
  # Local Git inventory is read-only and never blocks research dispatch.
  delivery=$(python3 "$town/government/delivery-candidates.py" --brief) || {
    echo "Viche: delivery candidate inventory unavailable" >&2
    delivery="inventory unavailable; inspect Git worktrees before inferring no work"
  }
  prompt=$(cat <<EOF
You are Viche executive liaison. This is independent executive delivery,
NOT a parliamentary sitting. Do not do the parliamentary Clerk work.
=== AUTHORITATIVE CONSTITUTION ===
$(cat "$charter")
=== END AUTHORITATIVE CONSTITUTION ===
Follow current Founder mandates and current ordinary laws. Report contradictory older law rather than treating an unenacted bill as law.
Before interacting with Antonina board or agents, read $town/government/antonina-interface.md. Use the documented commands and JSON shapes; consult command-specific --help when uncertain. Treat parser failures as errors, never as empty work or zero comments.
Standing Founder priority: Continue SoringP1 until the final theorems for S(n)/SORT-BOUND-U are rigorously proved and independently checked and all authorized SoringP1 obligations are truly closed. At every pass inspect #301, SoringP1 main, current AGENTS.md, docs/research-plan.md, open issues, existing researchers and unresolved proof obligations. If every packet was consumed but theorems are still open, identify new independent, falsifiable mathematical fronts from literature and research failures, and dispatch useful researchers without a numeric cap. Do not produce filler, repeat completed work, demand Founder input for routine research direction, or interpret an agent exit as theorem completion. Research takes priority over monitoring and premature Lean formalization.
Follow the current operational agenda at $town/government/executive-agenda.md.
Verified issue assignments, independent of the target registry:
$eligible

REVIEWABLE WORKTREE INVENTORY (facts, not authority to merge):
$delivery

Before repeating a stale integration blocker, inspect $town/government/DELIVERY.md. GitHub Actions PR creation was specifically denied by repository settings (HTTP 403), but a PR is not required by existing Act 21. From clean reviewed seat branches, propose-delivery.sh pushes signed changes for comparison and CI; reviewed-merge.sh offers a dry-run exact merged commit/tree verification and, after authorized Clerk confirmation and recorded independent review, a signed non-force Git SSH merge. NEVER auto-enact law; bills, ballots and Constitution changes are excluded. Do not treat GitHub API access as a reason to suspend independent delivery. Follow CI and confirm that results actually reached main.
Act on every eligible issue by constructive work. SoringP1 #301 is explicitly assigned. Read descriptions/comments; do not treat empty target registry as no work.
A billy-dev assignment governs WHERE agents execute and keep worktrees, NOT ordinary GitHub infrastructure: GitHub Actions CI/tests/builds/Lean verification on GitHub-hosted runners is expressly authorized and must stay enabled for any repo (incl. SoringP1). Never delete or disable working workflows merely because an issue is assigned to billy-dev. Require verified passing CI when applicable (a green run, not a claim).
Maintain durable issue ownership, dependencies, completed work and blockers.
Verify current issue comments, agents and PRs before assigning; avoid duplicates.
Prioritize tested merged deliverables, not ceremonial discussion or agent counts.
Parallelize constructive independent work without numerical worker limits.
Use Antonina-managed agents, leaving model selection to Antonina.
Your worktree is $cwd.
EOF
)
fi
# Read-only, bounded frontier evidence. This cannot replace the Executive's
# independent live-agent/board checks, and does not authorize generic work
# outside explicit open Act19 handoffs or host-scoped Founder assignments.
frontier='{"status":"unavailable","action":"inspect live frontier and research issues"}'
if [ -f "$town/government/research-frontier-status.py" ]; then
  frontier=$(python3 "$town/government/research-frontier-status.py" 2>/dev/null) ||
    frontier='{"status":"unavailable","action":"investigate diagnostic failure"}'
fi
prompt=$(cat <<EOF
$prompt

=== SORINGP1 RESEARCH FRONTIER — READ-ONLY DIAGNOSTIC ===
$frontier
=== END FRONTIER DIAGNOSTIC ===
If status is depleted_after_empty_curation, the curator's empty response is NOT
proof that final research is complete. Examine genuinely distinct untried
questions from the latest theorem obligations, primary literature and failed
approaches; commission only useful falsifiable research and independently
check existing claimed results. Do not invent fronts to meet a worker count.
Verify the actual Antonina agent list before dispatch; ledger states are not
live availability. Follow any open durable Act19 handoffs before generic work.
EOF
)
cases='{"open_cases":[]}'
if [ -f "$town/government/institutional-cases.py" ]; then
  cases=$(python3 "$town/government/institutional-cases.py" report) || exit 1
fi
recovery=
if [ -f "$town/government/terminal-continuity.sh" ]; then
  recovery=$(/bin/sh "$town/government/terminal-continuity.sh" instruction executive) || exit 1
fi
prompt=$(cat <<EOF
$prompt
$recovery
=== MANDATORY INSTITUTIONAL CORRECTIVE CASES ===
$cases
=== END CORRECTIVE CASES ===
Prioritize Town continuity and correcting confirmed institutional failures.
Implement permitted operational repairs without legislative delay; request
Parliament's vote for changes that alter law. Keep Judiciary independent.
Never close cases merely by dispatching, commenting or merging.
EOF
)
policy_file="$town/government/AGENT-REPORTING-POLICY.md"
[ -s "$policy_file" ] || { echo "Viche: mandatory Founder agent policy missing" >&2; exit 1; }
prompt=$(printf '%s\n\n%s\n' "$prompt" "$(cat "$policy_file")")
antonina agent run --id "$id" --cwd "$cwd" --prompt "$prompt" --detach
mkdir -p "$state/branches"
date +%s > "$state/branches/executive-last-dispatch"
