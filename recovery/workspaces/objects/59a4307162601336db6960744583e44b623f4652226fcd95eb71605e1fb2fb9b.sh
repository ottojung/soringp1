#!/bin/sh
set -eu
root=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
mkdir -p "$scratch/bin" "$scratch/state" "$scratch/oversight" "$scratch/health" "$scratch/town"
cat > "$scratch/bin/s6-svstat" <<'MOCK'
#!/bin/sh
echo 'up (pid 10 pgid 10) 200 seconds'
MOCK
chmod +x "$scratch/bin/s6-svstat"
# Hermetic board: never touch the real Town Hall. Fail so the sentinel's
# durable outbox path (pending-message preserved when the board is
# unreachable) is the one exercised. Without this mock, a set
# VICHE_TOWNHALL_ID in the caller's environment makes check.sh post to the
# real board and the test's outbox assertion fails.
cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
exit 1
MOCK
chmod +x "$scratch/bin/antonina"
git -C "$scratch/town" init -q
git -C "$scratch/town" config user.name test
git -C "$scratch/town" config user.email test@example.invalid
printf 'hello\n' > "$scratch/town/file"
git -C "$scratch/town" add file
git -C "$scratch/town" commit -qm initial
git -C "$scratch/town" update-ref refs/remotes/origin/main HEAD
printf '100000\n' > "$scratch/health/government-setup.last"
printf '100000\t0\tidle\t0\t0\tnone\tclear\n' > "$scratch/oversight/observations.tsv"
PATH="$scratch/bin:$PATH"
VICHE_SENTINEL_NOW=100000
VICHE_SENTINEL_STATE=$scratch/state
VICHE_TOWN_ROOT=$scratch/town
VICHE_OVERSIGHT_STATE=$scratch/oversight
VICHE_GOV_HEALTH_STATE=$scratch/health
# Pin a dummy Town Hall id so the publication path is exercised deterministically
# against the failing mock above, independent of the caller's environment.
VICHE_TOWNHALL_ID=999
export PATH VICHE_SENTINEL_NOW VICHE_SENTINEL_STATE VICHE_TOWN_ROOT
export VICHE_OVERSIGHT_STATE VICHE_GOV_HEALTH_STATE VICHE_TOWNHALL_ID
/bin/sh "$root/sentinel/check.sh"
[ ! -e "$scratch/state/incident.json" ]
# Inject a real unmerged index without losing committed fixture data.
hash=$(printf 'conflict\n' | git -C "$scratch/town" hash-object -w --stdin)
printf '100644 %s 2\tfile\n100644 %s 3\tfile\n' "$hash" "$hash" |
    git -C "$scratch/town" update-index --index-info
VICHE_SENTINEL_NOW=103601
export VICHE_SENTINEL_NOW
/bin/sh "$root/sentinel/check.sh"
jq -e '.first_seen==103601 and (.signals|index("government_git_conflict"))' "$scratch/state/incident.json" >/dev/null
[ -s "$scratch/state/pending-message" ]
VICHE_SENTINEL_NOW=107201
export VICHE_SENTINEL_NOW
/bin/sh "$root/sentinel/check.sh"
jq -e '.first_seen==103601 and (.signals|index("oversight_stale"))' "$scratch/state/incident.json" >/dev/null
git -C "$scratch/town" reset --hard -q HEAD
printf '107201\n' > "$scratch/health/government-setup.last"
printf '107201\t0\tidle\t0\t0\tnone\tclear\n' >> "$scratch/oversight/observations.tsv"
VICHE_SENTINEL_NOW=107202
export VICHE_SENTINEL_NOW
/bin/sh "$root/sentinel/check.sh"
[ ! -e "$scratch/state/incident.json" ]
[ -s "$scratch/state/history.jsonl" ]
[ -s "$scratch/state/pending-message" ] # outbox preserved if external board unavailable
echo 'Hourly Sentinel smoke checks passed'
