#!/bin/sh
set -eu
cd "$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)"
repo=$(pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/town/government" "$d/town/records/knowledge" \
  "$d/seats/branches/statistics" "$d/state" "$d/bin" "$d/failing-post"
: > "$d/seats/branches/statistics/.git"
printf 'Synthetic charter fixture\n' > "$d/charter"
printf 'Synthetic reporting policy fixture\n' > "$d/town/government/AGENT-REPORTING-POLICY.md"
printf 'Synthetic governance fixture\n' > "$d/town/government/KNOWLEDGE-OFFICES.md"
printf '## Act 32 — Institutional Knowledge and Communications Act (enacted for test)\n' > "$d/town/government/LAWS.md"
printf 'Synthetic frozen baseline\n' > "$d/town/records/knowledge/baseline-20261119.json"
cp "$repo/government/post.py" "$repo/government/post-inbox-brief.sh" \
   "$repo/government/knowledge-activation-verify.sh" "$d/town/government/"
cat > "$d/town/government/branch-bootstrap.sh" <<'SH'
#!/bin/sh
exit 0
SH
cat > "$d/town/government/appointments.sh" <<'SH'
#!/bin/sh
printf '%s\n' test-appointed-statistics
SH
cat > "$d/town/government/terminal-continuity.sh" <<'SH'
#!/bin/sh
echo 'Synthetic continuity: no holds'
SH
cat > "$d/bin/antonina" <<'SH'
#!/bin/sh
set -eu
case "$1 $2" in
  'agent status') echo '{"state":"idle","alive":false}' ;;
  'agent run') printf '%s\n' "$@" > "$MOCK_RUN_LOG" ;;
  *) exit 5 ;;
esac
SH
chmod +x "$d/bin/antonina"
now=$(date +%s)
jq -n --argjson now "$now" '{
  schema:"viche-knowledge-activation-v1",
  offices:{statistics:{
    enabled:true,authorized_by:"act:32:statistics",
    not_before:($now-30),expires_at:($now+3600)
  }}}' > "$d/town/records/knowledge/activation.json"
export PATH="$d/bin:$PATH"
export VICHE_TOWN_ROOT="$d/town" VICHE_STATE_ROOT="$d/state"
export VICHE_SEATS_ROOT="$d/seats" VICHE_CONSTITUTION="$d/charter"
export VICHE_POST_DB="$d/failing-post" MOCK_RUN_LOG="$d/run.txt"
# The Post DB is a DIRECTORY, not a usable sqlite database. Core work must
# still dispatch, and the public preview must declare its uncertainty.
/bin/sh "$repo/government/knowledge-office-cycle.sh" statistics
test -s "$MOCK_RUN_LOG"
grep -Fq 'Post temporarily unavailable' "$MOCK_RUN_LOG"
jq -e '.status=="dispatched" and .verification=="not_established"' \
  "$d/state/knowledge/offices/statistics/health.json" > /dev/null
# A broken/forged communication channel cannot authorize an office; no law
# still means zero dispatches even when activation.json remains true.
: > "$MOCK_RUN_LOG"
printf '# No Act enacted\n' > "$d/town/government/LAWS.md"
rm -f "$d/state/knowledge/offices/statistics/last-dispatch"
/bin/sh "$repo/government/knowledge-office-cycle.sh" statistics
test ! -s "$MOCK_RUN_LOG"
echo 'knowledge office liveness independent of failed Post; enactment still required'
