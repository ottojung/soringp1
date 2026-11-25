#!/bin/sh
# Check parliamentary ballot tally under POSIX sh (no agent or network needed).
set -eu
root=$(git rev-parse --show-toplevel)
python3 - "$root/government/sitting.sh" <<'PY'
import sys
text=open(sys.argv[1]).read()
gate=text.index('Before publishing any bill for ballots, run government/predict-gate.sh BILL_ID')
solicit=text.index('solicit individual ballots')
assert gate < solicit, 'Act 22 pre-ballot gate must precede ballot solicitation instruction'
PY
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' 0
git -C "$scratch" init -q
git -C "$scratch" config user.name test
git -C "$scratch" config user.email test@example.invalid
mkdir -p "$scratch/government" "$scratch/records/bills" "$scratch/records/ballots"
cp "$root/government/seats.tsv" "$scratch/government/seats.tsv"
cp "$root/government/voting.conf" "$scratch/government/voting.conf"
cp "$root/government/predict-gate.sh" "$scratch/government/predict-gate.sh"
cp "$root/government/predict-ledger.py" "$scratch/government/predict-ledger.py"
mkdir -p "$scratch/records/predictions"
printf 'test-1\n' > "$scratch/records/predictions/pilot.tsv"
resolution_date=$(python3 -c 'import datetime; print((datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(days=1)).strftime("%Y-%m-%d"))')
registration_time=$(($(date +%s)-60))
for author in seat-a seat-b; do
    VICHE_TOWN_ROOT=$scratch VICHE_PREDICT_NOW=$registration_time \
        python3 "$root/government/predict-ledger.py" register --bill test-1 \
        --proposition "Pilot outcome from $author" --probability 0.6 \
        --resolution-date "$resolution_date" --evidence "fixture:$author" \
        --author "$author" >/dev/null
done
printf '%s\n' "A proposed statute" > "$scratch/records/bills/test-1.md"
digest=$(sha256sum "$scratch/records/bills/test-1.md" | cut -d ' ' -f1)
tab=$(printf '\t')
# Take an explicit ballot from every current seat, irrespective of seat count.
while IFS="$tab" read -r seat title focus; do
    [ -n "$seat" ] || continue
    printf '%s\tyes\t%s\n' "$seat" "$digest"
done < "$scratch/government/seats.tsv" > "$scratch/records/ballots/test-1.tsv"
VICHE_TOWN_ROOT=$scratch; export VICHE_TOWN_ROOT
if /bin/sh "$root/government/tally.sh" test-1 >/dev/null 2>&1; then
    echo "Untracked post-registration ballot file bypassed the Act 22 time gate" >&2
    exit 1
fi
git -C "$scratch" add . && git -C "$scratch" commit -qm 'publish registered pilot ballot'
/bin/sh "$root/government/tally.sh" test-1 | grep -Fx 'PASSED'
# The tally cannot silently bypass Act 22 when the gate executable is absent.
mv "$scratch/government/predict-gate.sh" "$scratch/government/predict-gate.missing"
if /bin/sh "$root/government/tally.sh" test-1 >/dev/null 2>&1; then
    echo "Missing Act 22 gate executable bypassed the gate" >&2
    exit 1
fi
mv "$scratch/government/predict-gate.missing" "$scratch/government/predict-gate.sh"
# With the pilot registry missing, tally must invoke the gate and fail closed.
rm "$scratch/records/predictions/pilot.tsv"
if /bin/sh "$root/government/tally.sh" test-1 >/dev/null 2>&1; then
    echo "Missing Act 22 pilot registry bypassed the gate" >&2
    exit 1
fi
printf 'test-1\n' > "$scratch/records/predictions/pilot.tsv"
# The exact bill hash is binding: a revision must invalidate every old ballot.
printf '%s\n' "Unapproved new text" >> "$scratch/records/bills/test-1.md"
if /bin/sh "$root/government/tally.sh" test-1 >/dev/null 2>&1; then
    echo "Old ballots incorrectly passed a changed bill" >&2
    exit 1
fi
printf '%s\n' "Viche: votes for the original bill pass; stale ballots rejected"
