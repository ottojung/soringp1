#!/bin/sh
# Hermetic institutional continuity, case lifecycle and executive-only enactment gate.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/bin" "$d/town/government" "$d/seats/branches/innovation-centre" "$d/state/branches" "$d/mock"
git -C "$d/seats/branches/innovation-centre" init -q
git -C "$d/seats/branches/innovation-centre" -c user.name=fixture -c user.email=fixture@example.com commit --allow-empty -qm baseline
printf 'old-agent\n' > "$d/mock/registry"
printf '{"state":"failed","alive":false,"active_runner":false,"native_session_id":"ses_fixture","steers_pending":0,"backend_error":{"transient":true,"automatic_retry_safe":false,"classification":"transient_backend_server_error"}}\n' > "$d/mock/old-agent.json"
printf '{"state":"idle","alive":false,"active_runner":false}\n' > "$d/mock/new-agent.json"
cat > "$d/town/government/appointments.sh" <<'MOCK'
#!/bin/sh
case "$1" in
  resolve|ensure) cat "$MOCK_ROOT/registry" ;;
  replace)
    [ "$3" = "$(cat "$MOCK_ROOT/registry")" ] || exit 1
    printf '%s\n' "$*" >> "$MOCK_ROOT/replacements"
    printf 'new-agent\n' > "$MOCK_ROOT/registry"
    printf 'new-agent\n' ;;
  *) exit 5 ;;
esac
MOCK
cat > "$d/bin/antonina" <<'MOCK'
#!/bin/sh
case "$1 $2" in
  'agent status') cat "$MOCK_ROOT/$4.json" ;;
  'agent run') printf '%s\n' "$*" >> "$MOCK_ROOT/runs" ;;
  *) exit 6 ;;
esac
MOCK
chmod +x "$d/bin/antonina" "$d/town/government/appointments.sh"
cp "$repo/government/EXECUTIVE-INNOVATION.md" "$d/town/government/EXECUTIVE-INNOVATION.md"
cp "$repo/government/AGENT-REPORTING-POLICY.md" "$d/town/government/AGENT-REPORTING-POLICY.md"
printf '# Historic Act 14 — Legislative Centre\n' > "$d/town/government/LAWS.md"
printf 'Founder-controlled fixture Constitution\n' > "$d/charter"
export PATH="$d/bin:$PATH" MOCK_ROOT="$d/mock"
export VICHE_TOWN_ROOT="$d/town" VICHE_SEATS_ROOT="$d/seats" VICHE_STATE_ROOT="$d/state" VICHE_CONSTITUTION="$d/charter"

# No legislative transfer without an actually enacted law record.
if /bin/sh "$repo/government/executive-innovation-cycle.sh" 2>/dev/null; then
  echo 'Executive migration accepted without legal enactment' >&2; exit 1
fi
test ! -e "$MOCK_ROOT/runs"

# One terminal 5xx is sufficient for a NEW reconciliation appointment,
# never for literal replay of the failed native turn. Preserve original id.
 /bin/sh "$repo/government/terminal-continuity.sh" recover innovation-centre
test "$(cat "$MOCK_ROOT/registry")" = new-agent
test "$(wc -l < "$MOCK_ROOT/replacements")" -eq 1
jq -e '.state=="awaiting_reconciliation" and .previous_agent=="old-agent" and .successor_agent=="new-agent" and .old_session_preserved==true' "$d/state/continuity/reconciliation-innovation-centre.json" >/dev/null
/bin/sh "$repo/government/terminal-continuity.sh" recover innovation-centre
test "$(wc -l < "$MOCK_ROOT/replacements")" -eq 1
/bin/sh "$repo/government/terminal-continuity.sh" instruction innovation-centre > "$d/reconciliation-prompt"
grep -Fq 'Do NOT blindly' "$d/reconciliation-prompt"
grep -Fq 'old-agent' "$d/reconciliation-prompt"

# Deterministic cross-branch case survives agent/process restarts.
printf '{"signals":["innovation_stale"],"observed_at":1000}\n' > "$d/state/branches/incident.json"
export VICHE_CASE_NOW=1000
python3 "$repo/government/institutional-cases.py" reconcile > "$d/cases"
jq -e '.open_cases | length==2' "$d/cases" >/dev/null
jq -e '.state=="open" and .owner=="executive"' "$d/state/institutional-cases/continuity_unverified_innovation-centre.json" >/dev/null
jq -e '.state=="open" and .owner=="executive" and .first_seen==1000' "$d/state/institutional-cases/innovation_stale.json" >/dev/null
rm "$d/state/branches/incident.json"
VICHE_CASE_NOW=1100 python3 "$repo/government/institutional-cases.py" reconcile >/dev/null
jq -e '.state=="open"' "$d/state/institutional-cases/innovation_stale.json" >/dev/null
VICHE_CASE_NOW=1200 python3 "$repo/government/institutional-cases.py" reconcile >/dev/null
jq -e '.state=="verified_closed" and .clear_observations==2' "$d/state/institutional-cases/innovation_stale.json" >/dev/null
jq -e '.state=="open"' "$d/state/institutional-cases/continuity_unverified_innovation-centre.json" >/dev/null
# Only a matching independent Judiciary verification can discharge the
# uncertain-effects reconciliation case.
printf '{"previous_agent":"old-agent","successor_agent":"new-agent","verified_by":"judiciary","verification_scope":"external_effect_reconciled","evidence_ref":"fixture:independent-reviewed-effects"}\n' > "$d/state/continuity/verified-innovation-centre.json"
VICHE_CASE_NOW=1300 python3 "$repo/government/institutional-cases.py" reconcile >/dev/null
VICHE_CASE_NOW=1400 python3 "$repo/government/institutional-cases.py" reconcile >/dev/null
jq -e '.state=="verified_closed"' "$d/state/institutional-cases/continuity_unverified_innovation-centre.json" >/dev/null

# After a real enactment, Executive unit runs on preserved worktree, not a
# parliamentary summons. Mock only the branch-bootstrap and deployment.
printf '## Act 23 — Executive Innovation Office Act (enacted 2026-10-25 by recorded vote)\n' > "$d/town/government/LAWS.md"
printf '#!/bin/sh\nexit 0\n' > "$d/town/government/branch-bootstrap.sh"
chmod +x "$d/town/government/branch-bootstrap.sh"
cp "$repo/government/institutional-cases.py" "$d/town/government/institutional-cases.py"
cp "$repo/government/terminal-continuity.sh" "$d/town/government/terminal-continuity.sh"
/bin/sh "$repo/government/executive-innovation-cycle.sh"
jq -e '.executive_office==true and .legislative_branch==false and .controlled_by=="executive" and .voting_seat==false' "$d/state/executive/innovation-office/health.json" >/dev/null
grep -Fq 'EXECUTIVE INNOVATION OFFICE' "$MOCK_ROOT/runs"
! grep -Fq 'permanent LEGISLATIVE' "$MOCK_ROOT/runs"
echo 'Institutional continuity + executive innovation gate smoke passed'
