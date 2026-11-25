#!/bin/sh
# ballot-completeness.sh smoke test (hermetic; POSIX /bin/sh).
# Proves the consolidation audit re-fetches and reports an origin ballot branch
# whose seat line is absent from the durable ballot record (the 2026-10-21 Act 22
# defect), and passes when every origin branch is counted.
set -eu

repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT

origin=$scratch/origin.git
town=$scratch/town
git init -q --bare "$origin"
git clone -q "$origin" "$town"
mkdir -p "$town/government" "$town/records/ballots"
cp "$repo/government/ballot-completeness.sh" "$town/government/"
git -C "$town" config user.email t@t
git -C "$town" config user.name t
echo seed > "$town/seed"
git -C "$town" add -A
git -C "$town" commit -qm init
git -C "$town" push -q origin HEAD:main
git -C "$town" branch -q main 2>/dev/null || true

for seat in c1a00001 c1a00002; do
    git -C "$town" checkout -q -b "ballot/$seat-b"
    mkdir -p "$town/records/ballots"
    printf '%s\tyes\tdeadbeef\n' "$seat" > "$town/records/ballots/b.tsv"
    git -C "$town" add -A
    git -C "$town" commit -qm "$seat ballot"
    git -C "$town" push -q origin "ballot/$seat-b"
    git -C "$town" checkout -q main
done

# Durable record counts only c1a00001 -> c1a00002 must be reported missing.
mkdir -p "$town/records/ballots"
printf 'c1a00001\tyes\tdeadbeef\n' > "$town/records/ballots/b.tsv"
if VICHE_TOWN_ROOT=$town /bin/sh "$town/government/ballot-completeness.sh" b; then
    echo "FAIL: expected a missing-ballot failure"; exit 1
fi

# Count c1a00002 too -> complete.
mkdir -p "$town/records/ballots"
printf 'c1a00001\tyes\tdeadbeef\nc1a00002\tyes\tdeadbeef\n' > "$town/records/ballots/b.tsv"
VICHE_TOWN_ROOT=$town /bin/sh "$town/government/ballot-completeness.sh" b >/dev/null

echo "ballot-completeness smoke passed"
