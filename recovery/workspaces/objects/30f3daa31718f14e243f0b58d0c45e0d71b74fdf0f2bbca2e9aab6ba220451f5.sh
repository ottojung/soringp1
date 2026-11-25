#!/bin/sh
# Act 31 §8: a bill's state comes from the records that decide it, never from
# its own (often stale) header or from file times.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
t=$d/town
mkdir -p "$t/government" "$t/records/bills" "$t/records/ballots"
git -C "$t" init -q -b main
git -C "$t" config user.name Fixture
git -C "$t" config user.email fixture@example.invalid
git -C "$t" config commit.gpgsign false
printf 'c1a00001\tClerk\tx\nc1a00002\tA\tx\nc1a00003\tB\tx\n' > "$t/government/seats.tsv"
# Enacted bills keep a stale "DRAFT ... NOT ENACTED" header; the law decides.
printf '# DRAFT — Old Act (NOT ENACTED)\n' > "$t/records/bills/old-act.md"
printf '# Laws\n## Act 3 — Old Act (enacted by recorded vote on bill old-act)\n' > "$t/government/LAWS.md"
printf '# DRAFT — Gate Act (NOT ENACTED)\n' > "$t/records/bills/gate-act.md"
printf '*`government/tally.sh gate-act` PASSED.*\n' >> "$t/government/LAWS.md"
# Withdrawn by its sponsor even though ballots were once solicited.
printf '# WITHDRAWN — Bad Act\n' > "$t/records/bills/bad-act.md"
printf 'vote\n' > "$t/records/ballots/bad-act-vote-instructions.md"
# A draft nobody solicited ballots for is not vote business.
printf '# DRAFT — Idea\n' > "$t/records/bills/idea.md"
# An open bill: solicited; one seat voted on the current text, one on an old text.
printf '# Live Act\n' > "$t/records/bills/live-act.md"
printf 'vote\n' > "$t/records/ballots/live-act-vote-instructions.md"
digest=$(sha256sum "$t/records/bills/live-act.md" | cut -d ' ' -f 1)
printf 'c1a00002\tyes\t%s\nc1a00003\tno\tstale\n' "$digest" > "$t/records/ballots/live-act.tsv"
# Versions: v1 is superseded by a solicited v2; the old upper-case marker counts.
printf '# Twin Act\n' > "$t/records/bills/twin-act.md"
printf 'vote\n' > "$t/records/ballots/twin-act-vote-instructions.md"
printf '# Twin Act v2\n' > "$t/records/bills/twin-act-v2.md"
printf 'vote\n' > "$t/records/ballots/TWIN-ACT-V2-VOTE.md"
# Lapsed: solicited, then nothing for more than 14 days (by commit time).
printf '# Stale Act\n' > "$t/records/bills/stale-act.md"
printf 'vote\n' > "$t/records/ballots/stale-act-vote-instructions.md"
git -C "$t" add records/bills/stale-act.md records/ballots/stale-act-vote-instructions.md
GIT_COMMITTER_DATE='2026-10-01T00:00:00Z' GIT_AUTHOR_DATE='2026-10-01T00:00:00Z' git -C "$t" commit -qm stale
git -C "$t" add -A
git -C "$t" commit -qm rest
touch "$t/records/bills/stale-act.md"          # a fresh file time must not reopen it

export VICHE_TOWN_ROOT="$t" VICHE_BILLS_NOW
VICHE_BILLS_NOW=$(date -u -d 2026-11-18T12:00:00Z +%s)
b() { python3 "$repo/government/bills.py" "$@"; }
state() { b status "$1" | jq -r .state; }
test "$(state old-act)" = enacted
test "$(state gate-act)" = enacted
test "$(state bad-act)" = withdrawn
test "$(state idea)" = draft
test "$(state live-act)" = open
test "$(state twin-act)" = superseded
test "$(state twin-act-v2)" = open
test "$(state stale-act)" = lapsed
b status live-act | jq -e '.voted == ["c1a00002"] and .not_voted == ["c1a00001","c1a00003"]' >/dev/null
test "$(b open --json | jq -r '[.[].id] | join(" ")')" = 'live-act twin-act-v2'
if b status no-such-bill >/dev/null 2>&1; then echo 'unknown bill accepted' >&2; exit 1; fi
echo 'bills smoke passed'
