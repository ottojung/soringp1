#!/bin/sh
# Act 30 §4: obligations the Town injects into prompts expire after a TTL unless
# renewed with a reason. Expiry archives, never deletes, and is "unverified".
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/town/government" "$d/town/records/handoffs" "$d/state/continuity" \
  "$d/state/oversight/judiciary-mailbox/inbox"
cp "$repo/government/obligation-expiry.py" "$repo/government/terminal-continuity.sh" \
  "$repo/government/handoff-queue.sh" "$d/town/government/"
export VICHE_TOWN_ROOT="$d/town" VICHE_STATE_ROOT="$d/state"
tool="python3 $d/town/government/obligation-expiry.py"
now=$(date -u -d '2026-11-16T12:00:00Z' +%s)
export VICHE_OBLIGATION_NOW=$now

receipt() { # office at -> awaiting_reconciliation receipt
  printf '{"state":"awaiting_reconciliation","office":"%s","previous_agent":"old-%s","successor_agent":"new-%s","classification":"x","at":"%s","terminal_evidence":"e","worktree_head":"h","old_session_preserved":true,"steers_pending":0,"next_steer":null}\n' \
    "$1" "$1" "$1" "$2" > "$d/state/continuity/reconciliation-$1.json"
}
receipt old-office 2026-11-05T15:53:12Z          # 11 days old
receipt fresh-office 2026-11-16T01:00:00Z        # 11 hours old
receipt borderline 2026-11-13T12:00:01Z          # 71h59m59s old: not yet
printf '{"state":"preparing","office":"mid","at":"2026-10-01T00:00:00Z"}\n' > "$d/state/continuity/reconciliation-mid.json"
printf '{"state":"awaiting_reconciliation","office":"backup"}\n' > "$d/state/continuity/reconciliation-backup.json.bak20260804"

handoff() { # id created status
  printf 'id: %s\nstatus: %s\nassigned-by: clerk\ncreated: %s\nevidence: e\nwork: do a thing\n' "$1" "$3" "$2" \
    > "$d/town/records/handoffs/$1.txt"
}
handoff H-1-aaaa 2026-11-08T00:00:00Z open       # 8 days
handoff H-2-bbbb 2026-11-16T10:00:00Z open       # 2 hours
handoff H-3-cccc 2026-11-01T00:00:00Z done       # old but already done

inbox=$d/state/oversight/judiciary-mailbox/inbox
printf 'old report\n' > "$inbox/20261102T202742Z-executive-old.md"
printf 'new report\n' > "$inbox/20261116T090000Z-executive-new.md"
printf 'no stamp\n' > "$inbox/undated.md"

out=$($tool sweep)
printf '%s\n' "$out" | jq -e '.receipts == ["old-office"] and .handoffs == ["H-1-aaaa"] and (.mailbox | length) == 1' >/dev/null

# Receipt: expired, unverified, original preserved, other receipts untouched.
r=$d/state/continuity/reconciliation-old-office.json
jq -e '.state == "expired" and .expired_unverified == true and .expiry_reason == "ttl_elapsed_without_renewal"' "$r" >/dev/null
jq -e '.previous_agent == "old-old-office"' "$r" >/dev/null
orig=$(jq -r '.original_preserved' "$r")
test -s "$d/state/$orig"
jq -e '.state == "awaiting_reconciliation"' "$d/state/$orig" >/dev/null
jq -e '.state == "awaiting_reconciliation"' "$d/state/continuity/reconciliation-fresh-office.json" >/dev/null
jq -e '.state == "awaiting_reconciliation"' "$d/state/continuity/reconciliation-borderline.json" >/dev/null
jq -e '.state == "preparing"' "$d/state/continuity/reconciliation-mid.json" >/dev/null
jq -e '.state == "awaiting_reconciliation"' "$d/state/continuity/reconciliation-backup.json.bak20260804" >/dev/null

# The expired receipt is no longer injected into prompts; a live one is, with its expiry.
test -z "$(/bin/sh "$d/town/government/terminal-continuity.sh" instruction old-office)"
live=$(/bin/sh "$d/town/government/terminal-continuity.sh" instruction fresh-office)
printf '%s\n' "$live" | grep -q 'MANDATORY RECOVERY'
printf '%s\n' "$live" | grep -q 'EXPIRES at 2026-11-19T01:00:00Z'
printf '%s\n' "$live" | grep -q 'obligation-expiry.py close receipt fresh-office'

# Handoffs: only the old open one expired; the queue no longer lists it.
grep -q '^status: expired$' "$d/town/records/handoffs/H-1-aaaa.txt"
grep -q 'expired unverified' "$d/town/records/handoffs/H-1-aaaa.txt"
grep -q '^status: open$' "$d/town/records/handoffs/H-2-bbbb.txt"
grep -q '^status: done$' "$d/town/records/handoffs/H-3-cccc.txt"
test "$(/bin/sh "$d/town/government/handoff-queue.sh" list-open "$d/town" | cut -f2)" = H-2-bbbb

# Mailbox: stale report archived (not deleted), new and undated-fresh stay.
test ! -e "$inbox/20261102T202742Z-executive-old.md"
test -s "$d/state/oversight/judiciary-mailbox/expired/20261102T202742Z-executive-old.md"
test -s "$inbox/20261116T090000Z-executive-new.md"
test -s "$inbox/undated.md"

# Ledger and report.
test "$(wc -l < "$d/state/obligations/ledger.jsonl")" -eq 3
$tool report | jq -e '.expired_total == {"receipt":1,"handoff":1,"mailbox":1} and (.live.receipts|length) == 2 and (.live.handoffs|length) == 1 and .live.mailbox == 2' >/dev/null

# A second sweep is idempotent.
$tool sweep | jq -e '.receipts == [] and .handoffs == [] and .mailbox == []' >/dev/null

# Renewal needs a reason and restarts the clock; the receipt then survives 72h more.
if $tool renew receipt borderline --reason '' 2>/dev/null; then echo 'empty reason accepted' >&2; exit 1; fi
$tool renew receipt borderline --reason 'still reconciling the Git side'
jq -e '.renewals == 1 and .renewal_reason == "still reconciling the Git side"' "$d/state/continuity/reconciliation-borderline.json" >/dev/null
later=$((now + 3*3600 + 10))   # would have expired at 72h without the renewal
VICHE_OBLIGATION_NOW=$later $tool sweep | jq -e '.receipts == []' >/dev/null
$tool renew handoff H-2-bbbb --reason 'waiting on a CI result'
grep -q '^renewed: ' "$d/town/records/handoffs/H-2-bbbb.txt"
if $tool renew receipt old-office --reason x 2>/dev/null; then echo 'renewed an expired receipt' >&2; exit 1; fi

# The owner can close its own receipt alone, without a verifier.
$tool close receipt fresh-office --evidence 'checked Git and board: nothing was lost'
jq -e '.state == "closed_by_owner" and .independently_verified == false and .closed_by == "fresh-office"' \
  "$d/state/continuity/reconciliation-fresh-office.json" >/dev/null
test -z "$(/bin/sh "$d/town/government/terminal-continuity.sh" instruction fresh-office)"
if $tool close receipt fresh-office --evidence x 2>/dev/null; then echo 'double close accepted' >&2; exit 1; fi

# Minute-precision timestamps (used by durable handoffs) must not silently escape expiry.
handoff H-4-minute 2026-11-08T16:02Z open
$tool sweep | jq -e '.handoffs == ["H-4-minute"]' >/dev/null
grep -q '^status: expired$' "$d/town/records/handoffs/H-4-minute.txt"
grep -q 'expired unverified' "$d/town/records/handoffs/H-4-minute.txt"

# The owner can close its own open handoff alone, without a verifier.
handoff H-5-owner 2026-11-16T10:00:00Z open
$tool close handoff H-5-owner --evidence 'checked durable board: nothing pending'
grep -q '^status: closed_by_owner$' "$d/town/records/handoffs/H-5-owner.txt"
grep -q '^closure-evidence: checked durable board: nothing pending$' "$d/town/records/handoffs/H-5-owner.txt"
grep -q '^independently-verified: false$' "$d/town/records/handoffs/H-5-owner.txt"
if $tool close handoff H-5-owner --evidence x 2>/dev/null; then echo 'double handoff close accepted' >&2; exit 1; fi

# TTL 0 disables expiry entirely.
receipt eternal 2026-01-01T00:00:00Z
VICHE_OBLIGATION_TTL_HOURS=0 $tool sweep | jq -e '.receipts == []' >/dev/null
jq -e '.state == "awaiting_reconciliation"' "$d/state/continuity/reconciliation-eternal.json" >/dev/null
# A shorter TTL is honoured.
VICHE_OBLIGATION_TTL_HOURS=24 $tool sweep | jq -e '.receipts == ["eternal"]' >/dev/null

echo 'obligation expiry smoke passed'
