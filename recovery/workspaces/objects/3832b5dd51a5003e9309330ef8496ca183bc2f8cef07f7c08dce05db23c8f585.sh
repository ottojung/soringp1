#!/bin/sh
# Act19 integration: actually exercise appointments, distinct invocation
# identities, fractional finished timestamps and legal reset/cooldown.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
/bin/sh "$repo/tests/appointment-recovery-integration-smoke.sh"

# The separate Part 2 tests durable handoff non-supersession in isolation.
d2=$(mktemp -d)
trap 'rm -rf "$d2"' EXIT HUP INT TERM

# --- Part 2: durable handoff queue and non-supersession (executive-cycle, §3.2) ---
mkdir -p "$d2/bin" "$d2/town/government" "$d2/town/records" "$d2/seats/branches/executive" "$d2/state"
printf 'c1a00001\tClerk\tintake\nc1e00002\tExecutive\tdelivery\n' > "$d2/town/government/seats.tsv"
printf 'Founder charter fixture\n' > "$d2/charter"
printf '%s\n' c1e00002 > "$d2/town/records/SUMMONED.txt"
cp "$repo/government/eligible-work.py" "$d2/town/government/eligible-work.py"
cp "$repo/government/executive-cycle.sh" "$d2/town/government/executive-cycle.sh"
cp "$repo/government/handoff-queue.sh" "$d2/town/government/handoff-queue.sh"
cp "$repo/government/predict-scorer.py" "$d2/town/government/predict-scorer.py"
# The real executive-cycle.sh requires the Founder agent-reporting policy and
# reads the delivery-candidate inventory. Stage both so the fixture exercises
# the actual code path instead of failing on files it never copied.
cp "$repo/government/AGENT-REPORTING-POLICY.md" "$d2/town/government/AGENT-REPORTING-POLICY.md"
cp "$repo/government/delivery-candidates.py" "$d2/town/government/delivery-candidates.py"
cat > "$d2/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
case "$1 $2" in
  'board list')
    [ "${BOARD_DOWN:-no}" != yes ] || exit 3
    echo '[{"number":"301","title":"SoringP1"}]' ;;
  'board show')
    echo '{"body":"All agent execution and development work must happen on billy-dev.","messages":[]}' ;;
  'agent status')
    printf '{"state":"%s","model":"%s","variant":"low"}\n' "$MODE" "$MODEL" ;;
  'agent run')
    printf '%s\n' "$*" > "$PROMPT_FILE"
    printf 'accepted\n' >> "$OUTPUT" ;;
  *) echo "Unexpected: $*" >&2; exit 10 ;;
esac
MOCK
chmod +x "$d2/bin/antonina"
touch "$d2/state/inaugurated"
PATH="$d2/bin:$PATH"
mkdir -p "$d2/town/government"
cp "$repo/tests/appointment-id-stub.sh" "$d2/town/government/appointments.sh"
VICHE_TOWN_ROOT="$d2/town"
VICHE_SEATS_ROOT="$d2/seats"
VICHE_STATE_ROOT="$d2/state"
VICHE_CONSTITUTION="$d2/charter"
MODE=idle MODEL=test-provider/example
OUTPUT="$d2/dispatched"
PROMPT_FILE="$d2/prompt"
export PATH VICHE_TOWN_ROOT VICHE_SEATS_ROOT VICHE_STATE_ROOT VICHE_CONSTITUTION MODE MODEL OUTPUT PROMPT_FILE

# With no open handoffs the generic eligible-issue dispatch is unchanged.
/bin/sh "$d2/town/government/executive-cycle.sh"
test "$(wc -l < "$OUTPUT")" -eq 1
grep -Fq '301' "$PROMPT_FILE"
test -s "$d2/state/branches/eligible-issues.json"

# Atomic steer: the steer writes the queue entry at steer time.
id1=$(/bin/sh "$d2/town/government/handoff-queue.sh" add "$d2/town" 'Viche Clerk c1a00001' 'board #313 2026-10-19T11:14Z' 'Deliver the Act 18 section 7 step: verify the tally and publish')
id2=$(/bin/sh "$d2/town/government/handoff-queue.sh" add "$d2/town" 'Viche Clerk c1a00001' 'board #313 2026-10-19T11:14Z' 'Second open handoff item')
test -n "$id1"
test "$id1" != "$id2"
test -s "$d2/town/records/handoffs/$id1.txt"
grep -Fq 'status: open' "$d2/town/records/handoffs/$id1.txt"
# list-open is the dispatch input: one line per open handoff, id and work present.
listed=$(/bin/sh "$d2/town/government/handoff-queue.sh" list-open "$d2/town")
test "$(printf '%s\n' "$listed" | wc -l)" -eq 2
printf '%s\n' "$listed" | grep -Fq "$id1"
printf '%s\n' "$listed" | grep -Fq "$id2"
printf '%s\n' "$listed" | grep -Fq 'Deliver the Act 18 section 7 step'
test "$(printf '%s\n' "$listed" | head -n 1 | awk -F '\t' '{print NF}')" -eq 3

# P3 (Founder directive 2026-11-16): an open handoff is CARRIED in the
# dispatch but no longer suspends the ordinary eligible-issue work. A handoff
# owned by another office must never stall Executive delivery.
rm -f "$d2/state/branches/eligible-issues.json"
/bin/sh "$d2/town/government/executive-cycle.sh"
test "$(wc -l < "$OUTPUT")" -eq 2
grep -Fq 'OPEN DURABLE HANDOFFS' "$PROMPT_FILE"
grep -Fq 'Act 18 section 7 step' "$PROMPT_FILE"
grep -Fq "$id1" "$PROMPT_FILE"
grep -Fq 'Verified issue assignments' "$PROMPT_FILE"
grep -Fq 'never' "$PROMPT_FILE"
grep -Fq 'let it suspend the eligible-issue work' "$PROMPT_FILE"
test -s "$d2/state/branches/eligible-issues.json"

# The steer's own evidence and assigning authority are durable in the entry.
grep -Fq 'assigned-by: Viche Clerk c1a00001' "$d2/town/records/handoffs/$id1.txt"
grep -Fq 'evidence: board #313 2026-10-19T11:14Z' "$d2/town/records/handoffs/$id1.txt"

# Marking done is atomic and only open handoffs can transition.
/bin/sh "$d2/town/government/handoff-queue.sh" mark "$d2/town" "$id1" done 'Act 18 section 7 published, evidence in PROCEEDINGS.md'
grep -Fq 'status: done' "$d2/town/records/handoffs/$id1.txt"
if /bin/sh "$d2/town/government/handoff-queue.sh" mark "$d2/town" "$id1" done 'again' 2>/dev/null; then
  echo "re-closing a closed handoff must fail" >&2
  exit 1
fi
# One open handoff is still carried, alongside the generic dispatch.
/bin/sh "$d2/town/government/executive-cycle.sh"
test "$(wc -l < "$OUTPUT")" -eq 3
grep -Fq "$id2" "$PROMPT_FILE"
grep -Fq 'Verified issue assignments' "$PROMPT_FILE"
if grep -Fq "$id1" "$PROMPT_FILE"; then echo "a done handoff must not be carried" >&2; exit 1; fi
/bin/sh "$d2/town/government/handoff-queue.sh" mark "$d2/town" "$id2" superseded 'newer durable handoff arrived'
# With no open handoffs the handoff section disappears.
/bin/sh "$d2/town/government/executive-cycle.sh"
test "$(wc -l < "$OUTPUT")" -eq 4
grep -Fq '301' "$PROMPT_FILE"
if grep -Fq 'OPEN DURABLE HANDOFFS' "$PROMPT_FILE"; then echo "empty handoff section emitted" >&2; exit 1; fi
test -s "$d2/state/branches/eligible-issues.json"

# No dispatch at all when the script fails before the queue read: a queue
# read crash exits non-zero and leaves the agent undispatched.
cat > "$d2/town/government/handoff-queue.sh" <<'BROKEN'
#!/bin/sh
echo "simulated queue read crash" >&2
exit 1
BROKEN
if /bin/sh "$d2/town/government/executive-cycle.sh" 2>/dev/null; then
  echo "dispatch must not occur when the queue read fails" >&2
  exit 1
fi
test "$(wc -l < "$OUTPUT")" -eq 4
# A missing charter is likewise a pre-read failure: no dispatch.
cp "$repo/government/handoff-queue.sh" "$d2/town/government/handoff-queue.sh"
if env -u VICHE_CONSTITUTION /bin/sh "$d2/town/government/executive-cycle.sh" 2>/dev/null; then
  echo "dispatch must not occur without the charter" >&2
  exit 1
fi
test "$(wc -l < "$OUTPUT")" -eq 4

echo 'Act 19 office-continuity and handoff smoke checks passed'
