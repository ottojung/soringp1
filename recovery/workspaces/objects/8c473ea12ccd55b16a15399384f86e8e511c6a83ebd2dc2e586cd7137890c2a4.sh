#!/bin/sh
# A transient Antonina "unknown" status sample must not abort the Executive
# cycle or mark the branch unhealthy; a persistent unknown still fails closed
# with an actionable message and performs no dispatch.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/bin" "$d/town/government" "$d/town/records/handoffs" \
  "$d/seats/branches/executive" "$d/state" "$d/mock"
printf 'c1a00001\tClerk\tintake\n' > "$d/town/government/seats.tsv"
printf 'Founder charter fixture\n' > "$d/charter"
cp "$repo/government/appointments.sh" "$repo/government/branch-bootstrap.sh" \
  "$repo/government/branch-liveness.sh" "$repo/government/executive-cycle.sh" \
  "$repo/government/office-continuity.sh" "$repo/government/handoff-queue.sh" \
  "$repo/government/predict-scorer.py" "$repo/government/eligible-work.py" \
  "$repo/government/research-frontier-status.py" \
  "$repo/government/delivery-candidates.py" "$repo/government/AGENT-REPORTING-POLICY.md" \
  "$d/town/government/"
git -C "$d/town" init -q
git -C "$d/town" -c user.name=test -c user.email=test@example.test commit --allow-empty -qm town
git -C "$d/town" update-ref refs/remotes/origin/main HEAD
git -C "$d/seats/branches/executive" init -q
git -C "$d/seats/branches/executive" -c user.name=test -c user.email=test@example.test \
  commit --allow-empty -qm baseline
mkdir -p "$d/state/appointments"
printf 'executive\tid-exec\n' > "$d/state/appointments/appointments.tsv"
printf '{"fronts":[],"curator":{"exit_state":"clearexit","added":0,"last_finished_at":1000}}\n' \
  > "$d/frontier.json"
cat > "$d/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
case "$1 $2" in
  "board list") echo '[{"number":"301","title":"SoringP1"}]' ;;
  "board show") echo '{"body":"x","messages":[]}' ;;
  "agent status")
    n=$(cat "$MOCK_ROOT/unknown_left" 2>/dev/null || echo 0)
    if [ "$n" -gt 0 ]; then
      printf '%s\n' $((n - 1)) > "$MOCK_ROOT/unknown_left"
      printf '{"state":"unknown","model":"m","variant":"low"}\n'
    else
      printf '{"state":"%s","model":"m","variant":"low"}\n' "$(cat "$MOCK_ROOT/mode")"
    fi ;;
  "agent run") printf 'run\n' >> "$MOCK_ROOT/runs" ;;
  *) echo "unexpected Antonina call: $*" >&2; exit 9 ;;
esac
MOCK
chmod +x "$d/bin/antonina"
export PATH="$d/bin:$PATH" MOCK_ROOT="$d/mock" VICHE_TOWN_ROOT="$d/town" \
  VICHE_SEATS_ROOT="$d/seats" VICHE_STATE_ROOT="$d/state" \
  VICHE_CONSTITUTION="$d/charter" SORING_FRONTIER_STATE="$d/frontier.json"
mode_executive() { printf '%s\n' "$1" > "$d/mock/mode"; }
unknown_samples() { printf '%s\n' "$1" > "$d/mock/unknown_left"; }
runs() { wc -l < "$d/mock/runs" 2>/dev/null || echo 0; }
touch "$d/state/inaugurated"
cycle=$d/town/government/executive-cycle.sh

# 1. One transient unknown sample: the cycle must still dispatch, not abort.
mode_executive idle
unknown_samples 1
/bin/sh "$cycle"
test "$(runs)" -eq 1

# 2. Persistent unknown: fail closed, no dispatch, actionable message.
unknown_samples 99
if /bin/sh "$cycle" 2>"$d/err"; then
  echo "persistent unknown must not be treated as healthy" >&2
  exit 1
fi
test "$(runs)" -eq 1
grep -Fq "re-probe" "$d/err"

# 3. Transient unknown in the supervisor: readiness must not be unhealthy.
unknown_samples 1
out=$(/bin/sh "$d/town/government/branch-liveness.sh" executive 2>&1) || {
  echo "$out" >&2
  echo "transient unknown marked the executive branch unhealthy" >&2
  exit 1
}
jq -e '.readiness=="ready" and .cycle_accepted==true' \
  "$d/state/branches/executive.json" >/dev/null

# 4. Persistent unknown in the supervisor: still unhealthy and no dispatch.
before=$(runs)
unknown_samples 99
if /bin/sh "$d/town/government/branch-liveness.sh" executive >/dev/null 2>&1; then
  echo "persistent unknown must surface as unhealthy" >&2
  exit 1
fi
test "$(runs)" -eq "$before"
jq -e '.readiness=="unhealthy"' "$d/state/branches/executive.json" >/dev/null
echo 'Transient-versus-persistent unknown-status smoke passed'
