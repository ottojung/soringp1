#!/bin/sh
# Act 30 §6 as amended by Act 31 §8: Parliament sits once per UTC day, summons
# only the seats that owe a ballot on an open bill (government/bills.py), never
# touches the Clerk's own summonses, releases the seats it added once they have
# sat, and summons nobody when there is no business.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/town/government" "$d/town/records/bills" "$d/town/records/ballots" "$d/state"
cp "$repo/government/bills.py" "$d/town/government/bills.py"
for n in 1 2 3 4 5 6 7 8 9 10; do
  printf 'c1a%05d\tSeat %s\tx\n' "$n" "$n"
done > "$d/town/government/seats.tsv"
printf '# Laws\n' > "$d/town/government/LAWS.md"
export VICHE_TOWN_ROOT="$d/town" VICHE_STATE_ROOT="$d/state"
no() { if grep -q "$@"; then echo "unexpected match: $*" >&2; exit 1; fi; }
ds() { python3 "$repo/government/daily-sitting.py" "$@"; }
at() { date -u -d "$1" +%s; }
summoned=$d/town/records/SUMMONED.txt
record() { cat "$d/state/parliament/daily/$1.json"; }

# Before inauguration nothing happens.
VICHE_DAILY_NOW=$(at 2026-11-16T18:00:00Z) ds run 2>/dev/null
test ! -e "$summoned"
touch "$d/state/inaugurated"

# Before the sitting hour: nothing.
VICHE_DAILY_NOW=$(at 2026-11-16T16:59:00Z) ds run 2>/dev/null
test ! -e "$summoned"

# B1 is open (ballots solicited) and seat 4 already voted on its current text.
# B2 was withdrawn and B3 never solicited: neither is business, however recent.
printf '# B1\n' > "$d/town/records/bills/B1.md"
printf 'vote\n' > "$d/town/records/ballots/B1-vote-instructions.md"
printf 'c1a00004\tyes\t%s\n' "$(sha256sum "$d/town/records/bills/B1.md" | cut -d ' ' -f 1)" > "$d/town/records/ballots/B1.tsv"
printf '# WITHDRAWN — B2\n' > "$d/town/records/bills/B2.md"
printf 'vote\n' > "$d/town/records/ballots/B2-vote-instructions.md"
printf '# DRAFT — B3\n' > "$d/town/records/bills/B3.md"
# The Clerk had already summoned seat 3 for specific work.
printf 'c1a00003\n' > "$summoned"
mkdir -p "$d/town/records/summons"
printf 'Specific assignment from the Clerk.\n' > "$d/town/records/summons/c1a00003.md"

# Sitting: the eight non-Clerk seats that owe a ballot (all but seat 4).
VICHE_DAILY_NOW=$(at 2026-11-16T17:00:00Z) ds run 2>/dev/null
test "$(wc -l < "$summoned")" -eq 8
no '^c1a00001$' "$summoned"
no '^c1a00004$' "$summoned"
agenda=$d/state/parliament/daily/plenary-agenda.md
grep -q 'B1 (records/bills/B1.md)' "$agenda"
no 'B2' "$agenda"
no 'B3' "$agenda"
grep -q 'propose-delivery.sh --office' "$agenda"
no 'Then stop' "$agenda"
grep -q 'daily-plenary' "$d/town/records/summons/c1a00002.md"
grep -q 'Your ballot is owed on: B1' "$d/town/records/summons/c1a00002.md"
grep -q '^Specific assignment from the Clerk.$' "$d/town/records/summons/c1a00003.md"
record 2026-11-16 | jq -e '.convened == true and (.added | length) == 7 and .clerk == "c1a00001"
  and .bills_listed == ["B1"] and .owed.c1a00002 == ["B1"]' >/dev/null

# Once per day: running again adds nothing.
VICHE_DAILY_NOW=$(at 2026-11-16T17:05:00Z) ds run 2>/dev/null
test "$(wc -l < "$summoned")" -eq 8

# Seats that sat are released; seat 3 (the Clerk's own summons) is not ours.
for n in 02 05 06; do VICHE_DAILY_NOW=$(at 2026-11-16T17:10:00Z) ds dispatched c1a000$n; done
VICHE_DAILY_NOW=$(at 2026-11-16T17:10:00Z) ds dispatched c1a00003     # not in "added": ignored
VICHE_DAILY_NOW=$(at 2026-11-16T17:12:00Z) ds run 2>/dev/null
no '^c1a00002$' "$summoned"
grep -q '^c1a00003$' "$summoned"
grep -q '^c1a00007$' "$summoned"
test "$(wc -l < "$summoned")" -eq 5
record 2026-11-16 | jq -e '(.dispatched | length) == 3 and (.released | length) == 3' >/dev/null

# Seats that never sat are released after six hours (no wedged summonses).
VICHE_DAILY_NOW=$(at 2026-11-16T23:30:00Z) ds run 2>/dev/null
test "$(cat "$summoned")" = c1a00003

# The seat limit still applies to the seats that owe a ballot.
VICHE_PARLIAMENT_SEATS=3 VICHE_DAILY_NOW=$(at 2026-11-17T17:30:00Z) ds run 2>/dev/null
record 2026-11-17 | jq -e '.added == ["c1a00002"]' >/dev/null          # seats 2-4; 3 present, 4 voted
VICHE_DAILY_NOW=$(at 2026-11-17T17:31:00Z) ds status | jq -e '.day == "2026-11-17"' >/dev/null

# No business: every seat has voted, so nobody is summoned and that is recorded.
for n in 1 2 3 5 6 7 8 9 10; do
  printf 'c1a%05d\tyes\t%s\n' "$n" "$(sha256sum "$d/town/records/bills/B1.md" | cut -d ' ' -f 1)"
done >> "$d/town/records/ballots/B1.tsv"
printf 'c1a00003\n' > "$summoned"
VICHE_DAILY_NOW=$(at 2026-11-18T17:30:00Z) ds run 2>&1 | grep -q convened && { echo 'convened without business' >&2; exit 1; }
test "$(cat "$summoned")" = c1a00003
record 2026-11-18 | jq -e '.convened == false and .added == [] and .owed == {}' >/dev/null
grep -q 'No seat owes a ballot' "$agenda"

# Unreadable bill state convenes nobody and is retried (no record written).
mv "$d/town/government/bills.py" "$d/town/government/bills.py.off"
VICHE_DAILY_NOW=$(at 2026-11-19T17:30:00Z) ds run 2>/dev/null
test ! -e "$d/state/parliament/daily/2026-11-19.json"
mv "$d/town/government/bills.py.off" "$d/town/government/bills.py"

# The switch turns it off.
VICHE_DAILY_SITTING=off VICHE_DAILY_NOW=$(at 2026-11-20T18:00:00Z) ds run 2>/dev/null
test ! -e "$d/state/parliament/daily/2026-11-20.json"

echo 'daily sitting smoke passed'
